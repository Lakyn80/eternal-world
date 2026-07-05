from __future__ import annotations

import json
from pathlib import Path

import pytest

from rag_eval.adapters.base import RagEvalChunk
from rag_eval.adapters.memory import MemoryRagEvalBackend
from rag_eval.config import BenchmarkConfig, BenchmarkModelsConfig, BenchmarkRetrievalConfig
from rag_eval.retrieval.bm25 import tokenize_legal_text
from rag_eval.retrieval.candidates import expand_retrieval_candidates
from rag_eval.retrieval.fusion import reciprocal_rank_fusion
from rag_eval.runner import run_benchmark, validate_benchmark


def _write_legal_dataset(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "dataset_id": "nalus-legal-v1",
                "name": "NALUS Legal Eval",
                "cases": [
                    {
                        "id": "case-section-120",
                        "question": "Co stanoví § 120 občanského zákoníku?",
                        "expected_answer_type": "short_fact",
                        "test_type": "short_fact",
                        "source_scope": {
                            "scope_type": "document",
                            "document_ids": ["doc-zakon"],
                        },
                        "required_evidence": [{"marker": "§ 120"}],
                        "forbidden_evidence": [],
                        "minimum_coverage": 1.0,
                        "allow_partial": False,
                        "expected_citation_count_min": 1,
                        "difficulty": "easy",
                        "language": "cs",
                        "expected_long_context": False,
                        "minimum_context_chars": 0,
                    },
                    {
                        "id": "case-statute-ref",
                        "question": "Který předpis upravuje odpovědnost podle 89/2012 Sb.?",
                        "expected_answer_type": "short_fact",
                        "test_type": "short_fact",
                        "source_scope": {
                            "scope_type": "document",
                            "document_ids": ["doc-zakon"],
                        },
                        "required_evidence": [{"marker": "89/2012 Sb."}],
                        "forbidden_evidence": [],
                        "minimum_coverage": 1.0,
                        "allow_partial": False,
                        "expected_citation_count_min": 1,
                        "difficulty": "easy",
                        "language": "cs",
                        "expected_long_context": False,
                        "minimum_context_chars": 0,
                    },
                ],
            }
        ),
        encoding="utf-8",
    )


def test_tokenize_legal_text_preserves_section_and_statute_markers():
    tokens = tokenize_legal_text("Podle § 120 zákona č. 89/2012 Sb. platí odpovědnost.")

    assert "§ 120" in tokens
    assert "89/2012 sb." in tokens


def test_bm25_retrieves_exact_legal_terms(tmp_path: Path):
    pytest.importorskip("bm25s")
    dataset_path = tmp_path / "dataset.json"
    _write_legal_dataset(dataset_path)

    chunks = [
        RagEvalChunk(
            chunk_id=10,
            source_id=3,
            chunk_text=(
                "Obecná ustanovení: podle § 120 občanského zákoníku č. 89/2012 Sb. "
                "se posuzuje odpovědnost za škodu."
            ),
            chunk_metadata={"source_document_id": "doc-zakon::case-section-120"},
        ),
        RagEvalChunk(
            chunk_id=11,
            source_id=3,
            chunk_text="Neurčitý obecný text bez právní citace pro distrakci.",
            chunk_metadata={"source_document_id": "doc-zakon::noise"},
        ),
    ]
    backend = MemoryRagEvalBackend(
        source_chunks=chunks,
        retrieval_config=BenchmarkRetrievalConfig(modes=["bm25"]),
    )

    response = backend.retrieve(
        profile_id=1,
        source_id=3,
        query="Co stanoví § 120?",
        model_code="bm25",
        collection_name="nalus__bm25",
        top_k=2,
        retrieval_mode="bm25",
    )

    assert response.results
    assert response.results[0].chunk_id == 10
    assert "§ 120" in response.results[0].text


def test_dense_plus_bm25_returns_valid_hybrid_ranking(tmp_path: Path):
    pytest.importorskip("bm25s")
    dataset_path = tmp_path / "dataset.json"
    _write_legal_dataset(dataset_path)

    chunks = [
        RagEvalChunk(
            chunk_id=20,
            source_id=5,
            chunk_text="Právní citace § 120 a 89/2012 Sb. pro hybridní test.",
            chunk_metadata={"source_document_id": "doc-zakon::case-section-120"},
        ),
        RagEvalChunk(
            chunk_id=21,
            source_id=5,
            chunk_text="Obecný text bez citace.",
            chunk_metadata={"source_document_id": "doc-zakon::noise"},
        ),
    ]
    backend = MemoryRagEvalBackend(
        source_chunks=chunks,
        retrieval_config=BenchmarkRetrievalConfig(modes=["dense_plus_bm25"], rrf_k=60),
    )
    backend.index_source(source_id=5, model_code="mock_embedding", collection_name="eval__mock__dense")

    response = backend.retrieve(
        profile_id=1,
        source_id=5,
        query="§ 120",
        model_code="mock_embedding",
        collection_name="eval__mock__dense",
        top_k=2,
        retrieval_mode="dense_plus_bm25",
    )

    assert response.results
    assert response.results[0].chunk_id == 20
    assert response.results[0].payload_metadata.get("fusion") == "rrf"


def test_reciprocal_rank_fusion_uses_rrf_scores_not_raw_scales():
    from rag_eval.adapters.base import RagEvalRetrievalResult

    dense = [
        RagEvalRetrievalResult(chunk_id=1, source_id=1, score=0.99, text="a"),
        RagEvalRetrievalResult(chunk_id=2, source_id=1, score=0.50, text="b"),
    ]
    bm25 = [
        RagEvalRetrievalResult(chunk_id=2, source_id=1, score=12.5, text="b"),
        RagEvalRetrievalResult(chunk_id=1, source_id=1, score=3.1, text="a"),
    ]

    fused = reciprocal_rank_fusion([dense, bm25], top_k=2, rrf_k=60)

    assert len(fused.results) == 2
    assert fused.results[0].chunk_id in {1, 2}
    assert fused.results[0].score < 1.0


def test_config_without_retrieval_section_defaults_to_dense_only(tmp_path: Path):
    config_path = tmp_path / "rag_eval.yaml"
    config_path.write_text(
        """
device: cpu
artifact_dir: ./out
backend: memory
source_id: 1
dataset: ./dataset.json
models:
  default: [mock_embedding]
""".strip(),
        encoding="utf-8",
    )
    (tmp_path / "dataset.json").write_text(
        json.dumps({"dataset_id": "x", "name": "x", "cases": []}),
        encoding="utf-8",
    )

    from rag_eval.config import load_benchmark_config

    config = load_benchmark_config(config_path)

    assert config.resolved_retrieval_modes() == ("dense",)


def test_unknown_retrieval_mode_raises_clear_error():
    with pytest.raises(ValueError, match="Unknown retrieval mode"):
        BenchmarkRetrievalConfig(modes=["dense", "invalid_mode"])


def test_bm25_mode_without_optional_extra_raises_import_error(monkeypatch):
    import rag_eval.retrieval.bm25 as bm25_module

    def fail_import():
        raise ImportError(
            "BM25 retrieval requires the optional 'bm25' extra. "
            "Install with: pip install 'rag-embedding-benchmark[bm25]'"
        )

    monkeypatch.setattr(bm25_module, "require_bm25s", fail_import)

    config = BenchmarkRetrievalConfig(modes=["bm25"])
    with pytest.raises(ImportError, match="optional 'bm25' extra"):
        config.validate_optional_dependencies()


def test_expand_candidates_for_all_modes_produces_eleven_for_five_models(tmp_path: Path):
    dataset_path = tmp_path / "dataset.json"
    dataset_path.write_text(
        json.dumps(
            {
                "dataset_id": "count-test",
                "name": "Count",
                "cases": [
                    {
                        "id": "case-1",
                        "question": "Test?",
                        "expected_answer_type": "short_fact",
                        "test_type": "short_fact",
                        "source_scope": {"scope_type": "document", "document_ids": ["doc-a"]},
                        "required_evidence": [{"marker": "marker"}],
                        "forbidden_evidence": [],
                        "minimum_coverage": 1.0,
                        "allow_partial": False,
                        "expected_citation_count_min": 1,
                        "difficulty": "easy",
                        "language": "en",
                        "expected_long_context": False,
                        "minimum_context_chars": 0,
                    }
                ],
                "source_documents": [
                    {
                        "document_id": "doc-a",
                        "content": "marker text for count test",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    from rag_eval.config import load_benchmark_config

    config_path = tmp_path / "rag_eval.yaml"
    config_path.write_text(
        """
device: cpu
artifact_dir: ./out
backend: memory
source_id: 1
dataset: ./dataset.json
retrieval:
  modes: [dense, bm25, dense_plus_bm25]
models:
  default:
    - m1
    - m2
    - m3
    - m4
    - m5
""".strip(),
        encoding="utf-8",
    )
    config = load_benchmark_config(config_path)
    from rag_eval.datasets.validate import validate_dataset_schema

    dataset = validate_dataset_schema(config.dataset)
    candidates = expand_retrieval_candidates(config=config, dataset=dataset)

    assert len(candidates) == 11
    assert sum(1 for item in candidates if item.retrieval_mode == "dense") == 5
    assert sum(1 for item in candidates if item.retrieval_mode == "bm25") == 1
    assert sum(1 for item in candidates if item.retrieval_mode == "dense_plus_bm25") == 5


def test_memory_runner_with_bm25_modes(tmp_path: Path):
    pytest.importorskip("bm25s")
    dataset_path = tmp_path / "dataset.json"
    _write_legal_dataset(dataset_path)

    chunks = [
        RagEvalChunk(
            chunk_id=1,
            source_id=7,
            chunk_text="Právní text s § 120 a 89/2012 Sb. pro benchmark run.",
            chunk_metadata={"source_document_id": "doc-zakon::case-section-120"},
        )
    ]
    backend = MemoryRagEvalBackend(
        source_chunks=chunks,
        retrieval_config=BenchmarkRetrievalConfig(modes=["bm25"]),
    )
    config = BenchmarkConfig(
        artifact_dir=tmp_path / "artifacts",
        backend="memory",
        source_id=7,
        profile_id=1,
        dataset=dataset_path,
        models=BenchmarkModelsConfig(default=["mock_embedding"]),
        retrieval=BenchmarkRetrievalConfig(modes=["bm25"]),
    )

    validation = validate_benchmark(config=config, backend=backend)
    assert validation.passed is True

    result = run_benchmark(config=config, backend=backend)
    assert result.winner_model_code == "bm25"
    assert (tmp_path / "artifacts" / "ranking.json").exists()

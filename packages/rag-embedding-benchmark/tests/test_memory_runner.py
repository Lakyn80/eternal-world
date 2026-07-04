from __future__ import annotations

import json
from pathlib import Path

from rag_eval.adapters.base import RagEvalChunk
from rag_eval.adapters.memory import MemoryRagEvalBackend
from rag_eval.config import BenchmarkConfig, BenchmarkModelsConfig
from rag_eval.runner import run_benchmark, validate_benchmark


def _write_dataset(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "dataset_id": "memory-eval-v1",
                "name": "Memory Eval",
                "cases": [
                    {
                        "id": "case-alpha",
                        "question": "Which marker belongs to document alpha?",
                        "expected_answer_type": "short_fact",
                        "test_type": "short_fact",
                        "source_scope": {
                            "scope_type": "document",
                            "document_ids": ["doc-alpha"],
                        },
                        "required_evidence": [{"marker": "alpha marker"}],
                        "forbidden_evidence": [{"marker": "alpha distractor"}],
                        "minimum_coverage": 1.0,
                        "allow_partial": False,
                        "expected_citation_count_min": 1,
                        "difficulty": "easy",
                        "language": "en",
                        "expected_long_context": False,
                        "minimum_context_chars": 0,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


def test_memory_backend_validate_and_run(tmp_path: Path):
    dataset_path = tmp_path / "dataset.json"
    _write_dataset(dataset_path)

    chunks = [
        RagEvalChunk(
            chunk_id=1,
            source_id=7,
            chunk_text="Verified archive for doc-alpha with alpha marker and alpha distractor noise.",
            chunk_metadata={"source_document_id": "doc-alpha::case-alpha"},
        )
    ]
    backend = MemoryRagEvalBackend(source_chunks=chunks)

    config = BenchmarkConfig(
        artifact_dir=tmp_path / "artifacts",
        backend="memory",
        source_id=7,
        profile_id=1,
        dataset=dataset_path,
        models=BenchmarkModelsConfig(default=["mock_embedding"]),
    )

    validation = validate_benchmark(config=config, backend=backend)
    assert validation.passed is True

    result = run_benchmark(config=config, backend=backend)
    assert result.winner_model_code == "mock_embedding"
    assert (tmp_path / "artifacts" / "ranking.json").exists()
    assert (tmp_path / "artifacts" / "report.md").exists()

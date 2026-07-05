from __future__ import annotations

import json
from pathlib import Path

from rag_eval.config import BenchmarkConfig, BenchmarkModelsConfig, load_benchmark_config


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples"


def test_load_example_config_resolves_dataset_path():
    config = load_benchmark_config(EXAMPLES_DIR / "rag_eval.yaml")

    assert config.backend == "eternal_world"
    assert config.device == "cpu"
    assert config.source_id == 42
    assert config.dataset.exists()
    assert "multilingual_e5_large" in config.resolved_model_codes()
    assert "qwen3_embedding_4b" not in config.resolved_model_codes()
    assert config.resolved_retrieval_modes() == ("dense",)


def test_optional_models_are_included_when_enabled(tmp_path: Path):
    config_path = tmp_path / "rag_eval.yaml"
    config_path.write_text(
        """
device: cpu
artifact_dir: ./out
backend: eternal_world
source_id: 1
profile_id: 1
dataset: ./dataset.json
models:
  default: [mock_embedding]
  optional_high_ram: [qwen3_embedding_4b]
  include_optional: true
""".strip(),
        encoding="utf-8",
    )
    dataset_path = tmp_path / "dataset.json"
    dataset_path.write_text(
        json.dumps(
            {
                "dataset_id": "tiny",
                "name": "Tiny",
                "cases": [
                    {
                        "id": "case-1",
                        "question": "Find verified marker phrase?",
                        "expected_answer_type": "short_fact",
                        "test_type": "short_fact",
                        "source_scope": {"scope_type": "document", "document_ids": ["doc-a"]},
                        "required_evidence": [{"marker": "verified marker phrase"}],
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
            }
        ),
        encoding="utf-8",
    )

    config = load_benchmark_config(config_path)

    assert config.resolved_model_codes() == ["mock_embedding", "qwen3_embedding_4b"]

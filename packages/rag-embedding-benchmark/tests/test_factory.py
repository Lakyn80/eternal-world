from __future__ import annotations

from pathlib import Path

import pytest

from rag_eval.adapters.factory import build_backend
from rag_eval.config import BenchmarkConfig, BenchmarkModelsConfig, CustomAdapterConfig, load_benchmark_config


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples"


def test_sql_qdrant_config_requires_database_and_qdrant(tmp_path: Path):
    config_path = tmp_path / "rag_eval.yaml"
    config_path.write_text(
        """
device: cpu
artifact_dir: ./out
backend: sql_qdrant
source_id: 1
dataset: ./dataset.json
models:
  default: [mock_embedding]
""".strip(),
        encoding="utf-8",
    )
    (tmp_path / "dataset.json").write_text('{"dataset_id":"x","name":"x","cases":[]}', encoding="utf-8")

    with pytest.raises(ValueError, match="database_url"):
        load_benchmark_config(config_path)


def test_custom_backend_is_loaded_from_config(tmp_path: Path):
    config = BenchmarkConfig(
        artifact_dir=tmp_path / "out",
        backend="custom",
        source_id=1,
        dataset=tmp_path / "dataset.json",
        models=BenchmarkModelsConfig(default=["mock_embedding"]),
        adapter=CustomAdapterConfig(
            module="support_custom_adapter",
            class_name="SupportCustomAdapter",
            kwargs={"label": "loaded"},
        ),
    )
    (tmp_path / "dataset.json").write_text('{"dataset_id":"x","name":"x","cases":[]}', encoding="utf-8")

    backend = build_backend(config)

    assert backend.label == "loaded"


def test_eternal_world_example_config_loads():
    config = load_benchmark_config(EXAMPLES_DIR / "rag_eval.yaml")

    assert config.backend == "eternal_world"
    assert config.collection_prefix == "rag_eval"

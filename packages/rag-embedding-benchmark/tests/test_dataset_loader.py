from __future__ import annotations

from pathlib import Path

from rag_eval.datasets.loader import load_external_eval_dataset


SAMPLE_DATASET = (
    Path(__file__).resolve().parents[3]
    / "backend"
    / "app"
    / "modules"
    / "real_question_eval"
    / "datasets"
    / "eternal_world_eval_dataset_sample.json"
)


def test_sample_dataset_loads_from_monorepo():
    assert SAMPLE_DATASET.exists()

    dataset = load_external_eval_dataset(SAMPLE_DATASET)

    assert dataset.dataset_id == "eternal-world-external-eval-sample"
    assert len(dataset.cases) == 5
    assert dataset.metadata["external_dataset"] is True

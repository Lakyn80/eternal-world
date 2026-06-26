from pathlib import Path

from app.modules.embedding_models.registry import (
    BGE_M3_DENSE_RETRIEVAL_MODE,
    BGE_M3_DENSE_SPARSE_MULTIVECTOR_RETRIEVAL_MODE,
    BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE,
    BGE_M3_FUTURE_RETRIEVAL_MODES,
)
from app.modules.real_question_eval.dataset_foundation import (
    build_core_real_question_eval_cases,
    build_extended_real_question_eval_dataset,
)


def test_core_real_question_eval_question_ids_remain_unchanged():
    assert [case.case_id for case in build_core_real_question_eval_cases()] == [
        "question-sunflower-house",
        "question-winter-trip",
        "question-grandmother-soup",
    ]


def test_extended_real_question_eval_dataset_preserves_core_questions_first():
    dataset = build_extended_real_question_eval_dataset()

    assert [case.case_id for case in dataset.cases[:3]] == [
        "question-sunflower-house",
        "question-winter-trip",
        "question-grandmother-soup",
    ]


def test_extended_real_question_eval_dataset_includes_planned_categories():
    dataset = build_extended_real_question_eval_dataset()

    assert dataset.metadata["planned_categories"] == [
        "short factual lookup",
        "multi-evidence question",
        "distractor-heavy question",
        "Czech query",
        "Russian query",
        "English query",
        "answer-not-available question",
        "similar-document conflict question",
        "long-context / distant evidence question",
    ]
    assert any("czech_query" in case.tags for case in dataset.cases)
    assert any("russian_query" in case.tags for case in dataset.cases)
    assert any(case.expected_behavior == "lack_of_evidence" for case in dataset.cases)


def test_bge_m3_future_retrieval_modes_are_registered_for_planning():
    assert BGE_M3_FUTURE_RETRIEVAL_MODES == (
        BGE_M3_DENSE_RETRIEVAL_MODE,
        BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE,
        BGE_M3_DENSE_SPARSE_MULTIVECTOR_RETRIEVAL_MODE,
    )


def test_embedding_benchmark_plan_artifacts_exist():
    backend_dir = Path(__file__).resolve().parents[1]
    expected_paths = [
        backend_dir / "artifacts" / "embedding_benchmark_plan" / "bge_m3_full_hybrid_design.md",
        backend_dir / "artifacts" / "embedding_benchmark_plan" / "extended_real_eval_dataset_plan.md",
        backend_dir / "artifacts" / "embedding_benchmark_plan" / "full_version_embedding_benchmark_runbook.md",
    ]

    for expected_path in expected_paths:
        assert expected_path.exists(), f"Missing planning artifact: {expected_path}"

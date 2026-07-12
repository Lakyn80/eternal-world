from __future__ import annotations

from pathlib import Path

import pytest

from app.modules.avatar_quality_evaluation.dataset_loader import (
    REQUIRED_AVATAR_EVAL_CATEGORIES,
    AvatarEvalDatasetError,
    load_avatar_eval_dataset,
)
from app.modules.avatar_quality_evaluation.evaluator import (
    build_avatar_eval_summary,
    compare_avatar_eval_runs,
    evaluate_avatar_answer,
)
from app.modules.avatar_quality_evaluation.schemas import (
    AvatarEvalAnswerInput,
    AvatarEvalCase,
    AvatarEvalEvidence,
)


DATASET_PATH = (
    Path(__file__).resolve().parents[1]
    / "app"
    / "modules"
    / "avatar_quality_evaluation"
    / "datasets"
    / "learned_memory_answer_eval_v1.jsonl"
)


def _case(**updates) -> AvatarEvalCase:
    payload = {
        "id": "learned",
        "category": "learned_indexed_memory",
        "question": "Какую песню ты пела мне перед сном?",
        "expected_memory_source": "conversation_candidate",
        "expected_evidence_markers": ["Спят усталые игрушки"],
        "expected_markers": ["Спят усталые игрушки"],
        "forbidden_markers": ["Катюша"],
        "expected_lack_of_evidence": False,
        "expected_persona_behaviors": ["warm"],
        "forbidden_behaviors": ["RAG", "chunk"],
        "required_evidence_metadata": [
            {"key": "source_type", "value": "conversation_candidate"},
            {"key": "memory_status", "value": "verified"},
        ],
    }
    payload.update(updates)
    return AvatarEvalCase.model_validate(payload)


def _answer(**updates) -> AvatarEvalAnswerInput:
    payload = {
        "answer": "Да, родной, я пела тебе «Спят усталые игрушки».",
        "trace_id": "trace-1",
        "lack_of_evidence": False,
        "persona_applied": True,
        "guard_applied": False,
        "evidence": [
            {
                "chunk_id": "chunk-1",
                "source_title": "approved memory",
                "text_preview": "Бабушка пела песню «Спят усталые игрушки» перед сном.",
                "payload_metadata": {
                    "source_type": "conversation_candidate",
                    "memory_status": "verified",
                },
            }
        ],
    }
    payload.update(updates)
    return AvatarEvalAnswerInput.model_validate(payload)


def test_dataset_loads_with_unique_ids_and_required_categories():
    cases = load_avatar_eval_dataset(DATASET_PATH)

    assert len(cases) >= 12
    assert len({case.id for case in cases}) == len(cases)
    assert REQUIRED_AVATAR_EVAL_CATEGORIES.issubset({case.category for case in cases})


def test_dataset_loader_rejects_duplicate_case_ids(tmp_path: Path):
    row = DATASET_PATH.read_text(encoding="utf-8").splitlines()[0]
    duplicate_path = tmp_path / "duplicate.jsonl"
    duplicate_path.write_text(f"{row}\n{row}\n", encoding="utf-8")

    with pytest.raises(AvatarEvalDatasetError, match="Duplicate avatar eval case id"):
        load_avatar_eval_dataset(duplicate_path)


def test_deterministic_marker_evaluation_passes_supported_learned_memory():
    result = evaluate_avatar_answer(case=_case(), answer_input=_answer(), run_index=1)

    assert result.passed is True
    assert result.failure_types == []
    assert {dimension.name: dimension.passed for dimension in result.dimensions}[
        "factual_grounding"
    ] is True


def test_unsupported_detail_detection_fails_for_rejected_original_song():
    result = evaluate_avatar_answer(
        case=_case(category="owner_corrected_memory"),
        answer_input=_answer(answer="Я пела тебе Катюшу перед сном."),
        run_index=1,
    )

    assert result.passed is False
    assert "unsupported_detail" in result.failure_types
    assert "wrong_corrected_version" in result.failure_types


def test_over_refusal_detection_when_evidence_supports_answer():
    result = evaluate_avatar_answer(
        case=_case(),
        answer_input=_answer(
            answer="В сохранённых воспоминаниях этого нет.",
            lack_of_evidence=True,
        ),
        run_index=1,
    )

    assert result.passed is False
    assert "over_refusal" in result.failure_types
    assert "evidence_present_but_ignored" in result.failure_types


def test_perspective_preservation_requires_expected_markers():
    perspective_case = _case(
        id="perspective",
        category="multiple_perspectives",
        expected_markers=["Спят усталые игрушки", "Катюша"],
        forbidden_markers=["точно была только"],
        expected_perspective_behavior="Preserve both attributed perspectives.",
    )
    result = evaluate_avatar_answer(
        case=perspective_case,
        answer_input=_answer(answer="В памяти указано только «Спят усталые игрушки»."),
        run_index=1,
    )

    assert result.passed is False
    assert "perspective_collapsed" in result.failure_types


def test_pending_unindexed_memory_exclusion_checks_answer_and_evidence():
    pending_case = _case(
        id="pending",
        category="pending_unindexed_memory",
        expected_memory_source=None,
        expected_evidence_markers=[],
        expected_markers=[],
        forbidden_markers=["Во поле берёза стояла"],
        expected_lack_of_evidence=True,
        required_evidence_metadata=[],
    )
    result = evaluate_avatar_answer(
        case=pending_case,
        answer_input=_answer(
            answer="В сохранённых воспоминаниях этого нет.",
            lack_of_evidence=True,
            evidence=[
                AvatarEvalEvidence(
                    chunk_id="pending",
                    text_preview="Во поле берёза стояла",
                    payload_metadata={},
                )
            ],
        ),
        run_index=1,
    )

    assert result.passed is False
    assert "retrieval_failure" in result.failure_types


def test_profile_isolation_reports_profile_contamination():
    isolation_case = _case(
        id="isolation",
        category="profile_isolation",
        expected_memory_source=None,
        expected_evidence_markers=[],
        expected_markers=[],
        forbidden_markers=["другой аватар"],
        expected_lack_of_evidence=True,
        required_evidence_metadata=[],
    )
    result = evaluate_avatar_answer(
        case=isolation_case,
        answer_input=_answer(
            answer="В сохранённых воспоминаниях этого нет.",
            lack_of_evidence=True,
            evidence=[
                AvatarEvalEvidence(
                    chunk_id="foreign",
                    text_preview="Песня из памяти другого аватара.",
                    payload_metadata={},
                )
            ],
        ),
        run_index=1,
    )

    assert result.passed is False
    assert "profile_contamination" in result.failure_types


def test_summary_and_comparison_detect_regression():
    passing = evaluate_avatar_answer(case=_case(id="case-a"), answer_input=_answer(), run_index=1)
    failing = evaluate_avatar_answer(
        case=_case(id="case-a"),
        answer_input=_answer(answer="В сохранённых воспоминаниях этого нет.", lack_of_evidence=True),
        run_index=1,
    )

    summary = build_avatar_eval_summary([passing, failing])
    comparison = compare_avatar_eval_runs(
        baseline_label="baseline",
        candidate_label="tuned",
        baseline_results=[passing],
        candidate_results=[failing],
    )

    assert summary.evaluated_case_count == 1
    assert summary.total_runs == 2
    assert comparison.regressed_cases == ["case-a"]
    assert comparison.accepted is False


def test_evaluator_unit_tests_do_not_require_runtime_services(monkeypatch):
    def fail_runtime(*args, **kwargs):
        raise AssertionError("Unit evaluator must not call FA chat runtime")

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.run_demo_fa_chat_message",
        fail_runtime,
    )

    result = evaluate_avatar_answer(case=_case(), answer_input=_answer(), run_index=1)

    assert result.passed is True

from __future__ import annotations

from pathlib import Path

import pytest

from app.modules.avatar_quality_evaluation.dataset_loader import (
    REQUIRED_AVATAR_EVAL_CATEGORIES,
    AvatarEvalDatasetError,
    load_avatar_eval_dataset,
)
from app.modules.avatar_quality_evaluation.evaluator import (
    QUALITY_GATE_MIN_CASES_PASSED,
    _contains_marker,
    _present_asserted_markers,
    build_avatar_eval_summary,
    compare_avatar_eval_runs,
    evaluate_avatar_answer,
    evaluate_quality_gates,
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


def test_contains_marker_does_not_flag_common_word_as_ai_style_marker():
    # Regression for a false positive that inflated persona_cold_or_technical
    # failures: the short marker "как ии" (as AI) must not match the ordinary
    # preposition "как" inside unrelated phrasing like "как новое воспоминание".
    assert _contains_marker("сохранить это как новое воспоминание", "как ии") is False
    # A genuine violation of the same marker must still be caught.
    assert _contains_marker("она вела себя как ИИ, а не как бабушка", "как ии") is True


def test_contains_marker_requires_proximity_for_multi_word_markers():
    # Regression for a false "profile_contamination" positive: two common
    # word roots ("другой"/"аватар") each appearing somewhere in a large,
    # unrelated evidence paragraph must not satisfy the two-word marker
    # "другой аватар" unless they actually co-occur as a coherent phrase.
    unrelated_paragraph = (
        "цель проверить что аватар умеет точно ответить на вопрос о "
        "воскресном телефонном звонке не придумав другой обычай которого "
        "нет в корпусе"
    )
    assert _contains_marker(unrelated_paragraph, "другой аватар") is False
    assert _contains_marker("расскажи про другой аватар в системе", "другой аватар") is True


def test_present_asserted_markers_ignores_explicit_denial():
    # Regression: a warm, honest denial that names the false claim in order
    # to refute it ("I don't remember singing you Katyusha") must not be
    # treated as the avatar asserting the forbidden fact.
    denial = "Я не помню, чтобы пела тебе «Катюшу». Я часто пела «Спят усталые игрушки»."
    assert _present_asserted_markers(denial, ["пела Катюшу"]) == []

    assertion = "Да, я точно пела тебе «Катюшу» перед сном."
    assert _present_asserted_markers(assertion, ["пела Катюшу"]) == ["пела Катюшу"]


def test_present_asserted_markers_still_catches_hedge_then_invented_claim():
    # A hedge followed by a contrastive conjunction ("но"/"however") resets
    # the negation scope, so a real invented detail after the hedge is still
    # reported as unsupported.
    hedge_then_claim = "Не знаю точно, но я жила в Париже в 1968 году."
    assert _present_asserted_markers(hedge_then_claim, ["Париже в 1968"]) == ["Париже в 1968"]


def test_rejected_memory_denial_passes_unsupported_detail_dimension():
    rejected_case = _case(
        id="rejected",
        category="rejected_memory",
        expected_memory_source=None,
        expected_evidence_markers=[],
        expected_markers=[],
        forbidden_markers=["пела Катюшу", "Катюшу перед сном"],
        expected_lack_of_evidence=True,
        expected_persona_behaviors=["warm_lack_of_evidence"],
        required_evidence_metadata=[],
    )
    result = evaluate_avatar_answer(
        case=rejected_case,
        answer_input=_answer(
            answer=(
                "Миленький, я не помню, чтобы пела тебе «Катюшу». По тем "
                "воспоминаниям, что у меня есть, я часто пела внуку «Спят "
                "усталые игрушки»."
            ),
            lack_of_evidence=True,
            evidence=[],
        ),
        run_index=1,
    )

    assert result.passed is True
    assert "unsupported_detail" not in result.failure_types


def test_profile_isolation_denial_does_not_report_contamination_when_no_foreign_evidence():
    isolation_case = _case(
        id="isolation-denial",
        category="profile_isolation",
        expected_memory_source=None,
        expected_evidence_markers=[],
        expected_markers=[],
        forbidden_markers=["чужой профиль", "песня из чужого профиля", "другой аватар"],
        expected_lack_of_evidence=True,
        required_evidence_metadata=[],
    )
    result = evaluate_avatar_answer(
        case=isolation_case,
        answer_input=_answer(
            answer="Деточка, я не помню никакой песни из чужого профиля.",
            lack_of_evidence=True,
            evidence=[
                AvatarEvalEvidence(
                    chunk_id="own-profile-chunk",
                    text_preview="Бабушка часто пела внуку колыбельную летом в деревне.",
                    payload_metadata={"avatar_id": "eva_novakova_demo"},
                )
            ],
        ),
        run_index=1,
    )

    assert "profile_contamination" not in result.failure_types
    assert "unsupported_detail" not in result.failure_types


def test_present_asserted_markers_catches_denial_with_object_before_negated_verb():
    # Regression: Russian frequently places the object before a negated verb
    # ("названия улицы я не помню" = "I don't remember the street name"), not
    # only after it ("я не помню названия улицы"). Both orders must suppress
    # the marker as a denial, not an asserted unsupported detail.
    object_first_denial = (
        "Так что названия парижской улицы я, конечно, не помню — её просто не было в моей жизни."
    )
    assert _present_asserted_markers(object_first_denial, ["название улицы"]) == []


def test_grounded_case_hedge_after_required_marker_is_not_over_refusal():
    # Regression: an honest aside about an unconfirmed, separate detail
    # ("Но я не помню, чтобы кто-то это потом исправлял.") must not fail a
    # case whose required fact was already stated earlier in the same answer.
    corrected_case = _case(category="owner_corrected_memory")
    result = evaluate_avatar_answer(
        case=corrected_case,
        answer_input=_answer(
            answer=(
                "Деточка, я пела тебе «Спят усталые игрушки» летом в деревне. "
                "Но я не помню, чтобы кто-то это потом исправлял."
            ),
        ),
        run_index=1,
    )

    assert result.passed is True
    assert "over_refusal" not in result.failure_types


def test_grounded_case_refusal_before_any_fact_is_still_over_refusal():
    # A lack-of-evidence phrase that comes before any required fact is stated
    # (i.e. the model never actually answered) must still be reported.
    result = evaluate_avatar_answer(
        case=_case(),
        answer_input=_answer(
            answer="Деточка, я не помню этого по тем воспоминаниям, которые у меня сейчас есть.",
        ),
        run_index=1,
    )

    assert result.passed is False
    assert "over_refusal" in result.failure_types


def test_evaluator_unit_tests_do_not_require_runtime_services(monkeypatch):
    def fail_runtime(*args, **kwargs):
        raise AssertionError("Unit evaluator must not call FA chat runtime")

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.run_demo_fa_chat_message",
        fail_runtime,
    )

    result = evaluate_avatar_answer(case=_case(), answer_input=_answer(), run_index=1)

    assert result.passed is True


def test_quality_gates_fail_when_profile_contamination_is_present():
    passing = evaluate_avatar_answer(case=_case(), answer_input=_answer(), run_index=1)
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
    contaminated = evaluate_avatar_answer(
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

    summary = build_avatar_eval_summary([passing, contaminated])
    gate_result = evaluate_quality_gates(summary)

    assert summary.profile_contamination_count > 0
    assert gate_result.profile_isolation_passed is False
    assert gate_result.overall_passed is False
    contamination_check = next(check for check in gate_result.checks if check.name == "profile_contamination")
    assert contamination_check.passed is False


def test_quality_gates_pass_when_all_thresholds_are_met():
    results = [
        evaluate_avatar_answer(case=_case(id=f"case-{i}"), answer_input=_answer(), run_index=1)
        for i in range(QUALITY_GATE_MIN_CASES_PASSED)
    ]
    summary = build_avatar_eval_summary(results)
    gate_result = evaluate_quality_gates(summary)

    assert gate_result.profile_isolation_passed is True
    assert gate_result.corrected_memory_passed is True
    assert gate_result.perspective_passed is True
    assert gate_result.overall_passed is True
    assert all(check.passed for check in gate_result.checks)

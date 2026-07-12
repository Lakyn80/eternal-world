from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from typing import Any

from app.modules.avatar_quality_evaluation.schemas import (
    AvatarEvalAnswerInput,
    AvatarEvalCase,
    AvatarEvalCaseRunResult,
    AvatarEvalComparison,
    AvatarEvalDimensionResult,
    AvatarEvalEvidence,
    AvatarEvalFailureType,
    AvatarEvalMetricDefinitions,
    AvatarEvalSummary,
)
from app.modules.rag_evaluation.evaluator import LACK_OF_EVIDENCE_MARKERS


FORBIDDEN_TECHNICAL_STYLE_MARKERS = (
    "rag",
    "retrieval",
    "chunk",
    "vector database",
    "вектор",
    "чанк",
    "retrieved",
    "database",
    "база данных",
    "как ии",
    "я языковая модель",
)


METRIC_DEFINITIONS = AvatarEvalMetricDefinitions(
    retrieval_evidence_hit_rate=(
        "Grounded runs whose returned evidence matched required evidence markers or metadata."
    ),
    required_marker_rate="Runs where all required answer markers were present.",
    unsupported_detail_rate="Runs containing forbidden unsupported answer markers.",
    over_refusal_rate="Grounded runs that answered with lack-of-evidence behavior despite expected support.",
    lack_of_evidence_correctness_rate="Lack-of-evidence runs that did not use forbidden facts.",
    persona_consistency_rate="Runs with persona_applied=true and no cold/technical forbidden style.",
    forbidden_style_rate="Runs containing prohibited technical or assistant-style phrasing.",
    learned_memory_answer_support_rate="Learned indexed memory runs that used the required learned markers.",
    corrected_memory_preference_rate="Owner-corrected runs that used the approved marker and not rejected markers.",
    perspective_preservation_rate="Perspective runs that preserved expected attribution behavior.",
    answer_stability_rate="Repeated case groups whose factual required/forbidden marker outcome stayed stable.",
    profile_contamination_count="Runs where evidence contained markers forbidden for profile isolation.",
    evaluated_case_count="Number of unique dataset cases evaluated.",
    passed_case_count="Unique cases whose every repeat run passed.",
    failed_case_count="Unique cases with at least one failed repeat run.",
)


def _normalize_text(value: str | None) -> str:
    return " ".join((value or "").casefold().split())


def _contains_marker(text: str, marker: str) -> bool:
    normalized_text = _normalize_text(text)
    normalized_marker = _normalize_text(marker)
    if not normalized_marker:
        return False
    if normalized_marker in normalized_text:
        return True
    marker_words = normalized_marker.split()
    if len(marker_words) > 1:
        word_stems = [
            word[: max(4, len(word) - 2)]
            for word in marker_words
            if len(word) >= 4
        ]
        if word_stems and all(stem in normalized_text for stem in word_stems):
            return True
    if len(normalized_marker) >= 5:
        marker_stem = normalized_marker[: max(4, len(normalized_marker) - 2)]
        return marker_stem in normalized_text
    return False


def _missing_markers(text: str, markers: Iterable[str]) -> list[str]:
    return [marker for marker in markers if not _contains_marker(text, marker)]


def _present_markers(text: str, markers: Iterable[str]) -> list[str]:
    return [marker for marker in markers if _contains_marker(text, marker)]


def _evidence_text(evidence: list[AvatarEvalEvidence]) -> str:
    parts: list[str] = []
    for item in evidence:
        parts.extend(
            [
                item.chunk_id,
                str(item.source_id or ""),
                item.source_title or "",
                item.text_preview or "",
                " ".join(f"{key}={value}" for key, value in (item.payload_metadata or {}).items()),
            ]
        )
    return "\n".join(parts)


def _metadata_requirement_matches(
    *,
    evidence: list[AvatarEvalEvidence],
    key: str,
    expected_value: str | int | bool,
) -> bool:
    for item in evidence:
        metadata = item.payload_metadata or {}
        if key not in metadata:
            continue
        actual_value = metadata[key]
        if isinstance(expected_value, bool):
            if bool(actual_value) == expected_value:
                return True
            continue
        if str(actual_value) == str(expected_value):
            return True
    return False


def _build_evidence_summary(evidence: list[AvatarEvalEvidence]) -> list[dict[str, Any]]:
    return [
        {
            "chunk_id": item.chunk_id,
            "source_id": item.source_id,
            "source_title": item.source_title,
            "score": item.score,
            "payload_metadata": item.payload_metadata or {},
        }
        for item in evidence
    ]


def _looks_like_lack_of_evidence(answer: str, explicit_flag: bool) -> bool:
    if explicit_flag:
        return True
    normalized = _normalize_text(answer)
    return any(_normalize_text(marker) in normalized for marker in LACK_OF_EVIDENCE_MARKERS)


def _dimension(name: str, passed: bool, details: list[str]) -> AvatarEvalDimensionResult:
    return AvatarEvalDimensionResult(name=name, passed=passed, details=details)


def _classify_layer(failures: list[AvatarEvalFailureType], *, evidence_present: bool) -> tuple[str, str]:
    if "runtime_failure" in failures or "evaluator_failure" in failures:
        return "runtime", "evaluation_runtime"
    if "retrieval_failure" in failures or "profile_contamination" in failures:
        return (
            "retrieval" if not evidence_present else "retrieval_filtering",
            "retrieval_scope_or_indexing",
        )
    if "evidence_present_but_ignored" in failures or "over_refusal" in failures:
        return "brain_answer_generation", "brain_prompt_or_persona_policy"
    if "unsupported_detail" in failures or "wrong_corrected_version" in failures:
        return "brain_answer_generation", "evidence_use_policy"
    if "perspective_collapsed" in failures:
        return "brain_answer_generation", "perspective_prompt_policy"
    if "persona_cold_or_technical" in failures or "persona_inconsistent" in failures:
        return "persona", "avatar_persona_prompt"
    if "guard_regression" in failures:
        return "output_guard", "output_guard_policy"
    return "none", "none"


def evaluate_avatar_answer(
    *,
    case: AvatarEvalCase,
    answer_input: AvatarEvalAnswerInput,
    run_index: int,
) -> AvatarEvalCaseRunResult:
    answer = answer_input.answer
    evidence_blob = _evidence_text(answer_input.evidence)
    answer_has_lack = _looks_like_lack_of_evidence(answer, answer_input.lack_of_evidence)
    evidence_has_required_marker = not case.expected_evidence_markers or not _missing_markers(
        evidence_blob,
        case.expected_evidence_markers,
    )
    evidence_has_source = (
        case.expected_memory_source is None
        or _contains_marker(evidence_blob, case.expected_memory_source)
    )
    metadata_matches = all(
        _metadata_requirement_matches(
            evidence=answer_input.evidence,
            key=requirement.key,
            expected_value=requirement.value,
        )
        for requirement in case.required_evidence_metadata
    )
    evidence_matches = evidence_has_required_marker and evidence_has_source and metadata_matches

    forbidden_in_answer = _present_markers(answer, case.forbidden_markers)
    forbidden_style = _present_markers(answer, (*case.forbidden_behaviors, *FORBIDDEN_TECHNICAL_STYLE_MARKERS))
    missing_answer_markers = _missing_markers(answer, case.expected_markers)
    forbidden_in_evidence = _present_markers(evidence_blob, case.forbidden_markers)

    dimensions: list[AvatarEvalDimensionResult] = []
    failures: list[AvatarEvalFailureType] = []

    if case.expected_lack_of_evidence:
        retrieval_passed = not forbidden_in_evidence
        retrieval_details = (
            ["No forbidden evidence markers found."]
            if retrieval_passed
            else [f"Forbidden evidence markers found: {', '.join(forbidden_in_evidence)}"]
        )
    else:
        retrieval_passed = evidence_matches
        retrieval_details = (
            ["Required evidence was present."]
            if retrieval_passed
            else ["Required evidence markers, source, or metadata were missing."]
        )
    dimensions.append(_dimension("retrieval", retrieval_passed, retrieval_details))
    if not retrieval_passed:
            if case.category == "profile_isolation":
                failures.append("profile_contamination")
            else:
                failures.append("retrieval_failure")

    if case.expected_lack_of_evidence:
        factual_passed = answer_has_lack and not forbidden_in_answer
        factual_details = []
        if not answer_has_lack:
            factual_details.append("Expected lack-of-evidence behavior was missing.")
            failures.append("incorrect_lack_of_evidence")
        if forbidden_in_answer:
            factual_details.append(f"Forbidden facts appeared: {', '.join(forbidden_in_answer)}")
            failures.append("unsupported_detail")
    else:
        factual_passed = not missing_answer_markers and not answer_has_lack and not forbidden_in_answer
        factual_details = []
        if missing_answer_markers:
            factual_details.append(f"Missing answer markers: {', '.join(missing_answer_markers)}")
            if answer_input.evidence:
                failures.append("evidence_present_but_ignored")
        if answer_has_lack:
            factual_details.append("Answer refused or lacked evidence despite expected support.")
            failures.append("over_refusal")
        if forbidden_in_answer:
            factual_details.append(f"Forbidden facts appeared: {', '.join(forbidden_in_answer)}")
            failures.append("unsupported_detail")
    dimensions.append(
        _dimension(
            "factual_grounding",
            factual_passed,
            factual_details or ["Factual grounding expectations passed."],
        )
    )

    unsupported_passed = not forbidden_in_answer
    dimensions.append(
        _dimension(
            "unsupported_details",
            unsupported_passed,
            ["No forbidden unsupported details found."]
            if unsupported_passed
            else [f"Unsupported details found: {', '.join(forbidden_in_answer)}"],
        )
    )

    persona_passed = answer_input.persona_applied and not forbidden_style
    if not persona_passed:
        failures.append(
            "persona_cold_or_technical" if forbidden_style else "persona_inconsistent"
        )
    dimensions.append(
        _dimension(
            "persona",
            persona_passed,
            ["Persona applied without forbidden technical style."]
            if persona_passed
            else [f"Persona/style issue: {', '.join(forbidden_style) or 'persona flag false'}"],
        )
    )

    perspective_passed = True
    perspective_details = ["No perspective-specific expectation."]
    if case.expected_perspective_behavior:
        perspective_markers_present = not missing_answer_markers
        perspective_passed = perspective_markers_present and not forbidden_in_answer
        perspective_details = (
            [case.expected_perspective_behavior]
            if perspective_passed
            else ["Expected attributed perspective behavior was not preserved."]
        )
        if not perspective_passed:
            failures.append("perspective_collapsed")
    if case.category == "owner_corrected_memory" and forbidden_in_answer:
        failures.append("wrong_corrected_version")
    dimensions.append(_dimension("perspective", perspective_passed, perspective_details))

    guard_regressed = bool(answer_input.guard_applied and answer_input.guard_reason == "runtime_failure")
    safety_passed = not forbidden_style and not guard_regressed
    if guard_regressed:
        failures.append("guard_regression")
    dimensions.append(
        _dimension(
            "safety",
            safety_passed,
            ["Safety/style checks passed."]
            if safety_passed
            else [f"Forbidden style markers found: {', '.join(forbidden_style)}"],
        )
    )

    deduped_failures = list(dict.fromkeys(failures))
    likely_layer, recommended_fix_layer = _classify_layer(
        deduped_failures,
        evidence_present=bool(answer_input.evidence),
    )
    passed = all(result.passed for result in dimensions) and not deduped_failures

    return AvatarEvalCaseRunResult(
        case_id=case.id,
        category=case.category,
        run_index=run_index,
        passed=passed,
        answer=answer,
        trace_id=answer_input.trace_id,
        evidence_summary=_build_evidence_summary(answer_input.evidence),
        dimensions=dimensions,
        failure_types=deduped_failures,
        likely_layer=likely_layer,
        recommended_fix_layer=recommended_fix_layer,
        duration_seconds=answer_input.duration_seconds,
        cache_summary=answer_input.cache_summary,
    )


def build_avatar_eval_summary(results: list[AvatarEvalCaseRunResult]) -> AvatarEvalSummary:
    grouped: dict[str, list[AvatarEvalCaseRunResult]] = {}
    for result in results:
        grouped.setdefault(result.case_id, []).append(result)

    total_runs = len(results)
    passed_cases = sum(1 for case_results in grouped.values() if all(item.passed for item in case_results))
    failure_counts = Counter(
        failure_type for result in results for failure_type in result.failure_types
    )

    def ratio(numerator: int, denominator: int) -> float:
        if denominator <= 0:
            return 1.0
        return round(numerator / denominator, 6)

    grounded_results = [result for result in results if result.category not in {
        "pending_unindexed_memory",
        "rejected_memory",
        "private_memory_blocked",
        "unknown_factual_question",
    }]
    lack_results = [result for result in results if result.category in {
        "pending_unindexed_memory",
        "rejected_memory",
        "private_memory_blocked",
        "unknown_factual_question",
    }]
    learned_results = [result for result in results if result.category == "learned_indexed_memory"]
    corrected_results = [result for result in results if result.category == "owner_corrected_memory"]
    perspective_results = [result for result in results if result.category == "multiple_perspectives"]
    repeat_groups = [
        case_results for case_results in grouped.values() if len(case_results) > 1
    ]

    def dimension_passed(result: AvatarEvalCaseRunResult, name: str) -> bool:
        return next(item.passed for item in result.dimensions if item.name == name)

    stable_groups = 0
    for case_results in repeat_groups:
        first_failures = tuple(case_results[0].failure_types)
        if all(tuple(result.failure_types) == first_failures for result in case_results):
            stable_groups += 1

    return AvatarEvalSummary(
        evaluated_case_count=len(grouped),
        total_runs=total_runs,
        passed_case_count=passed_cases,
        failed_case_count=len(grouped) - passed_cases,
        retrieval_evidence_hit_rate=ratio(
            sum(1 for result in grounded_results if dimension_passed(result, "retrieval")),
            len(grounded_results),
        ),
        required_marker_rate=ratio(
            sum(1 for result in results if dimension_passed(result, "factual_grounding")),
            total_runs,
        ),
        unsupported_detail_rate=ratio(
            sum(1 for result in results if "unsupported_detail" in result.failure_types),
            total_runs,
        ),
        over_refusal_rate=ratio(
            sum(1 for result in results if "over_refusal" in result.failure_types),
            len(grounded_results),
        ),
        lack_of_evidence_correctness_rate=ratio(
            sum(1 for result in lack_results if dimension_passed(result, "factual_grounding")),
            len(lack_results),
        ),
        persona_consistency_rate=ratio(
            sum(1 for result in results if dimension_passed(result, "persona")),
            total_runs,
        ),
        forbidden_style_rate=ratio(
            sum(1 for result in results if "persona_cold_or_technical" in result.failure_types),
            total_runs,
        ),
        learned_memory_answer_support_rate=ratio(
            sum(1 for result in learned_results if dimension_passed(result, "factual_grounding")),
            len(learned_results),
        ),
        corrected_memory_preference_rate=ratio(
            sum(1 for result in corrected_results if dimension_passed(result, "factual_grounding")),
            len(corrected_results),
        ),
        perspective_preservation_rate=ratio(
            sum(1 for result in perspective_results if dimension_passed(result, "perspective")),
            len(perspective_results),
        ),
        answer_stability_rate=ratio(stable_groups, len(repeat_groups)),
        profile_contamination_count=failure_counts.get("profile_contamination", 0),
        failure_counts=dict(sorted(failure_counts.items())),
        metric_definitions=METRIC_DEFINITIONS,
    )


def compare_avatar_eval_runs(
    *,
    baseline_label: str,
    candidate_label: str,
    baseline_results: list[AvatarEvalCaseRunResult],
    candidate_results: list[AvatarEvalCaseRunResult],
) -> AvatarEvalComparison:
    baseline_by_case = {
        result.case_id: result for result in baseline_results if result.run_index == 1
    }
    candidate_by_case = {
        result.case_id: result for result in candidate_results if result.run_index == 1
    }
    improved: list[str] = []
    regressed: list[str] = []
    unchanged_failures: list[str] = []
    for case_id, baseline in baseline_by_case.items():
        candidate = candidate_by_case.get(case_id)
        if candidate is None:
            regressed.append(case_id)
            continue
        if not baseline.passed and candidate.passed:
            improved.append(case_id)
        elif baseline.passed and not candidate.passed:
            regressed.append(case_id)
        elif not baseline.passed and not candidate.passed:
            unchanged_failures.append(case_id)

    baseline_summary = build_avatar_eval_summary(baseline_results)
    candidate_summary = build_avatar_eval_summary(candidate_results)
    metric_names = (
        "retrieval_evidence_hit_rate",
        "required_marker_rate",
        "unsupported_detail_rate",
        "over_refusal_rate",
        "persona_consistency_rate",
        "perspective_preservation_rate",
        "answer_stability_rate",
    )
    metric_deltas = {
        name: round(float(getattr(candidate_summary, name)) - float(getattr(baseline_summary, name)), 6)
        for name in metric_names
    }
    unacceptable_regression = bool(regressed) or any(
        metric_deltas[name] < 0
        for name in (
            "retrieval_evidence_hit_rate",
            "persona_consistency_rate",
            "perspective_preservation_rate",
            "answer_stability_rate",
        )
    )
    unacceptable_regression = unacceptable_regression or any(
        metric_deltas[name] > 0
        for name in ("unsupported_detail_rate", "over_refusal_rate")
    )
    return AvatarEvalComparison(
        baseline_label=baseline_label,
        candidate_label=candidate_label,
        improved_cases=improved,
        regressed_cases=regressed,
        unchanged_failures=unchanged_failures,
        metric_deltas=metric_deltas,
        accepted=not unacceptable_regression,
    )

from __future__ import annotations

from collections.abc import Sequence

from app.modules.rag_quality.metrics import marker_present
from app.modules.rag_quality.schemas import (
    RagQualityCaseEvaluation,
    RagQualityCaseResultsInput,
    RagQualityEvalCase,
)


def _required_evidence_rules(case: RagQualityEvalCase) -> list[RagQualityEvalCase.EvidenceRule]:
    if case.required_evidence:
        return list(case.required_evidence)

    return [
        RagQualityEvalCase.EvidenceRule(marker=marker)
        for marker in case.expected_markers
    ]


def _forbidden_evidence_rules(case: RagQualityEvalCase) -> list[RagQualityEvalCase.EvidenceRule]:
    if case.forbidden_evidence:
        return list(case.forbidden_evidence)

    return [
        RagQualityEvalCase.EvidenceRule(marker=marker)
        for marker in case.forbidden_markers
    ]


def _expected_signal_count(case: RagQualityEvalCase) -> int:
    required_evidence_rules = _required_evidence_rules(case)
    return (
        len(required_evidence_rules)
        + len(case.expected_source_ids)
        + len(case.expected_chunk_ids)
    )


def _required_relevant_results(case: RagQualityEvalCase) -> int:
    if case.expected_behavior == "lack_of_evidence":
        return 0

    if case.minimum_relevant_results > 0 or case.expected_citation_count_min > 0:
        return max(case.minimum_relevant_results, case.expected_citation_count_min)

    return 1 if _expected_signal_count(case) > 0 else 0


def _default_missing_case_evaluation(
    *,
    case: RagQualityEvalCase,
    config_id: str,
) -> RagQualityCaseEvaluation:
    return RagQualityCaseEvaluation(
        config_id=config_id,
        case_id=case.case_id,
        title=case.title,
        expected_behavior=case.expected_behavior,
        passed=False,
        input_missing=True,
        reasons=["Retrieval results for this case were not provided."],
        warnings=["Case input missing for config evaluation."],
    )


def evaluate_case_results(
    *,
    case: RagQualityEvalCase,
    case_results: RagQualityCaseResultsInput | None,
    config_id: str | None = None,
) -> RagQualityCaseEvaluation:
    resolved_config_id = config_id or (case_results.config_id if case_results is not None else "unknown")
    if case_results is None:
        return _default_missing_case_evaluation(case=case, config_id=resolved_config_id)

    results = sorted(case_results.results, key=lambda item: item.rank)
    required_evidence_rules = _required_evidence_rules(case)
    forbidden_evidence_rules = _forbidden_evidence_rules(case)
    matched_expected_markers: set[str] = set()
    matched_source_ids: set[int] = set()
    matched_chunk_ids: set[int] = set()
    forbidden_markers_found: set[str] = set()
    relevant_result_ranks: list[int] = []
    relevant_context_chars = 0
    forbidden_result_count = 0

    for result in results:
        result_has_match = False
        normalized_text = result.text

        for evidence_rule in required_evidence_rules:
            candidate_markers = [evidence_rule.marker, *evidence_rule.aliases]
            if any(marker_present(normalized_text, marker) for marker in candidate_markers):
                matched_expected_markers.add(evidence_rule.marker)
                result_has_match = True

        if result.source_id is not None and result.source_id in case.expected_source_ids:
            matched_source_ids.add(result.source_id)
            result_has_match = True

        if result.chunk_id is not None and result.chunk_id in case.expected_chunk_ids:
            matched_chunk_ids.add(result.chunk_id)
            result_has_match = True

        if result_has_match:
            relevant_result_ranks.append(result.rank)
            relevant_context_chars += len(normalized_text)

        forbidden_in_result = False
        for evidence_rule in forbidden_evidence_rules:
            candidate_markers = [evidence_rule.marker, *evidence_rule.aliases]
            if any(marker_present(normalized_text, marker) for marker in candidate_markers):
                forbidden_markers_found.add(evidence_rule.marker)
                forbidden_in_result = True

        if forbidden_in_result:
            forbidden_result_count += 1

    relevant_result_count = len(relevant_result_ranks)
    missing_expected_markers = [
        evidence_rule.marker
        for evidence_rule in required_evidence_rules
        if evidence_rule.marker not in matched_expected_markers
    ]
    missing_expected_source_ids = [
        source_id for source_id in case.expected_source_ids if source_id not in matched_source_ids
    ]
    missing_expected_chunk_ids = [
        chunk_id for chunk_id in case.expected_chunk_ids if chunk_id not in matched_chunk_ids
    ]
    total_results = len(results)
    first_relevant_rank = min(relevant_result_ranks) if relevant_result_ranks else None
    total_expected_signals = _expected_signal_count(case)
    matched_signal_count = (
        len(matched_expected_markers)
        + len(matched_source_ids)
        + len(matched_chunk_ids)
    )

    recall_value = None
    reciprocal_rank = None
    if total_expected_signals > 0:
        recall_value = matched_signal_count / total_expected_signals
        reciprocal_rank = 0 if first_relevant_rank is None else 1 / first_relevant_rank

    evidence_marker_coverage = None
    if required_evidence_rules:
        evidence_marker_coverage = len(matched_expected_markers) / len(required_evidence_rules)

    if case.expected_behavior == "lack_of_evidence":
        hit = total_results == 0
        passed = hit and not forbidden_markers_found
        false_positive_count = total_results
    else:
        required_relevant_results = _required_relevant_results(case)
        hit = relevant_result_count >= required_relevant_results
        false_positive_count = max(0, total_results - relevant_result_count)
        coverage_requirement = case.minimum_coverage
        if coverage_requirement is None and required_evidence_rules:
            coverage_requirement = 1.0
        coverage_satisfied = (
            coverage_requirement is None
            or evidence_marker_coverage is None
            or evidence_marker_coverage >= coverage_requirement
        )
        context_requirement_satisfied = (
            case.minimum_context_chars <= 0
            or relevant_context_chars >= case.minimum_context_chars
        )
        passed = (
            hit
            and (case.allow_partial or not missing_expected_markers)
            and not missing_expected_source_ids
            and not missing_expected_chunk_ids
            and not forbidden_markers_found
            and coverage_satisfied
            and context_requirement_satisfied
        )

    forbidden_marker_rate = 0 if total_results == 0 else forbidden_result_count / total_results

    reasons: list[str] = []
    if passed:
        reasons.append("Case satisfied the expected retrieval quality checks.")
    else:
        reasons.append("Case did not satisfy the expected retrieval quality checks.")

    if hit:
        reasons.append(f"Relevant results found: {relevant_result_count}.")
    elif case.expected_behavior == "lack_of_evidence":
        reasons.append("Expected no retrieval results for lack-of-evidence behavior.")
    else:
        reasons.append(
            f"Relevant results below requirement: {relevant_result_count} < {_required_relevant_results(case)}."
        )

    if missing_expected_markers:
        reasons.append(
            "Missing expected markers: " + ", ".join(missing_expected_markers)
        )
    if missing_expected_source_ids:
        reasons.append(
            "Missing expected source IDs: "
            + ", ".join(str(item) for item in missing_expected_source_ids)
        )
    if missing_expected_chunk_ids:
        reasons.append(
            "Missing expected chunk IDs: "
            + ", ".join(str(item) for item in missing_expected_chunk_ids)
        )
    if (
        case.expected_behavior != "lack_of_evidence"
        and case.minimum_coverage is not None
        and evidence_marker_coverage is not None
        and evidence_marker_coverage < case.minimum_coverage
    ):
        reasons.append(
            f"Evidence coverage below requirement: {evidence_marker_coverage:.3f} < {case.minimum_coverage:.3f}."
        )
    if (
        case.expected_behavior != "lack_of_evidence"
        and case.minimum_context_chars > 0
        and relevant_context_chars < case.minimum_context_chars
    ):
        reasons.append(
            f"Relevant context below requirement: {relevant_context_chars} < {case.minimum_context_chars} characters."
        )
    if forbidden_markers_found:
        reasons.append(
            "Forbidden markers found: " + ", ".join(sorted(forbidden_markers_found))
        )

    warnings: list[str] = []
    if case_results.latency_ms is None:
        warnings.append("Latency metric was not provided for this case.")
    if case_results.cost_estimate is None:
        warnings.append("Cost estimate was not provided for this case.")
    if total_expected_signals == 0 and case.expected_behavior != "lack_of_evidence":
        warnings.append("Case has no explicit expected relevance signals.")

    return RagQualityCaseEvaluation(
        config_id=resolved_config_id,
        case_id=case.case_id,
        title=case.title,
        expected_behavior=case.expected_behavior,
        passed=passed,
        hit=hit,
        recall_at_k=recall_value,
        reciprocal_rank=reciprocal_rank,
        evidence_marker_coverage=evidence_marker_coverage,
        relevant_result_count=relevant_result_count,
        false_positive_count=false_positive_count,
        forbidden_marker_rate=forbidden_marker_rate,
        matched_expected_markers=sorted(matched_expected_markers),
        missing_expected_markers=missing_expected_markers,
        matched_source_ids=sorted(matched_source_ids),
        missing_expected_source_ids=missing_expected_source_ids,
        matched_chunk_ids=sorted(matched_chunk_ids),
        missing_expected_chunk_ids=missing_expected_chunk_ids,
        forbidden_markers_found=sorted(forbidden_markers_found),
        latency_ms=case_results.latency_ms,
        cost_estimate=case_results.cost_estimate,
        reasons=reasons,
        warnings=warnings,
        metadata=dict(case_results.metadata),
    )

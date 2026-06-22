from __future__ import annotations

from collections.abc import Iterable

from app.modules.rag_evaluation.schemas import RagEvaluationBehavior, RagEvaluationCase, RagEvaluationCaseResult


MAX_ANSWER_PREVIEW_LENGTH = 240
LACK_OF_EVIDENCE_MARKERS = (
    "not available in the stored memories/context",
    "not in the stored memories/context",
    "do not have enough evidence",
    "don't have enough evidence",
    "i do not know from the available evidence",
)
UNCERTAINTY_MARKERS = (
    "i am not sure",
    "i'm not sure",
    "unclear",
    "uncertain",
    "based on the available evidence",
    "may have",
    "might have",
    "possibly",
)


def _normalize_text(value: str) -> str:
    return " ".join(value.lower().split())


def _contains_any_marker(text: str, markers: Iterable[str]) -> bool:
    normalized_text = _normalize_text(text)
    return any(_normalize_text(marker) in normalized_text for marker in markers)


def detect_actual_behavior(
    *,
    answer_text: str,
    response_metadata: dict[str, object] | None,
) -> RagEvaluationBehavior:
    grounding_status = str((response_metadata or {}).get("grounding_status") or "").strip().lower()
    if grounding_status == "no_evidence" or _contains_any_marker(answer_text, LACK_OF_EVIDENCE_MARKERS):
        return "lack_of_evidence"

    if grounding_status == "partial" or _contains_any_marker(answer_text, UNCERTAINTY_MARKERS):
        return "partial_answer_with_uncertainty"

    return "grounded_answer"


def _build_answer_preview(answer_text: str) -> str:
    normalized_text = " ".join(answer_text.split())
    if len(normalized_text) <= MAX_ANSWER_PREVIEW_LENGTH:
        return normalized_text

    return f"{normalized_text[: MAX_ANSWER_PREVIEW_LENGTH - 3].rstrip()}..."


def evaluate_answer_against_case(
    *,
    case: RagEvaluationCase,
    answer_text: str,
    provider_name: str,
    response_metadata: dict[str, object] | None = None,
    evidence_count: int,
) -> RagEvaluationCaseResult:
    normalized_answer = _normalize_text(answer_text)
    actual_behavior = detect_actual_behavior(
        answer_text=answer_text,
        response_metadata=response_metadata,
    )
    missing_expected_markers = [
        marker
        for marker in case.expected_evidence_markers
        if _normalize_text(marker) not in normalized_answer
    ]
    forbidden_claims_found = [
        claim
        for claim in case.forbidden_claims
        if _normalize_text(claim) in normalized_answer
    ]
    reasons: list[str] = []
    passed = True

    if evidence_count < case.minimum_required_evidence_count:
        passed = False
        reasons.append(
            "Available evidence count is below the case minimum "
            f"({evidence_count} < {case.minimum_required_evidence_count})."
        )

    if actual_behavior != case.expected_behavior:
        passed = False
        reasons.append(
            f"Expected behavior '{case.expected_behavior}' but got '{actual_behavior}'."
        )

    if case.should_require_lack_of_evidence and actual_behavior != "lack_of_evidence":
        passed = False
        reasons.append("Case required an explicit lack-of-evidence answer.")

    if missing_expected_markers:
        passed = False
        reasons.append(
            "Answer is missing expected evidence markers: "
            + ", ".join(missing_expected_markers)
        )

    if forbidden_claims_found:
        passed = False
        reasons.append(
            "Answer contains forbidden unsupported claims: "
            + ", ".join(forbidden_claims_found)
        )

    if passed:
        reasons.append("Answer satisfies the expected groundedness checks.")

    return RagEvaluationCaseResult(
        case_id=case.case_id,
        title=case.title,
        passed=passed,
        expected_behavior=case.expected_behavior,
        actual_behavior=actual_behavior,
        reasons=reasons,
        evidence_count=evidence_count,
        missing_expected_markers=missing_expected_markers,
        forbidden_claims_found=forbidden_claims_found,
        answer_preview=_build_answer_preview(answer_text),
        provider_name=provider_name,
        response_metadata=dict(response_metadata or {}),
    )

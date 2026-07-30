from __future__ import annotations

from collections.abc import Iterable

from app.modules.rag_evaluation.evaluator_language import (
    CYRILLIC_MARKER_ALIASES,
    RUSSIAN_LACK_DENIAL_CONTEXT_MARKERS,
    RUSSIAN_LACK_OF_EVIDENCE_MARKERS,
    expand_marker_aliases,
)
from app.modules.rag_evaluation.schemas import RagEvaluationBehavior, RagEvaluationCase, RagEvaluationCaseResult


MAX_ANSWER_PREVIEW_LENGTH = 240
LACK_OF_EVIDENCE_MARKERS = (
    "not available in the stored memories/context",
    "not in the stored memories/context",
    "do not have enough evidence",
    "don't have enough evidence",
    "i do not know from the available evidence",
    "i don't remember",
    "i do not remember",
    "i'm afraid i can't recall",
    "i am afraid i cannot recall",
    "no memory of that",
    "i don't know about that",
    "i do not know about that",
    "i wasn't there",
    "i was not there",
    "nemám vzpomínku",
    "nemám na to vzpomínku",
    "nemám k tomu uloženou vzpomínku",
    "na to si bohužel nevzpomínám",
    "to si nevybavuju",
    "to si nevybavuji",
    "o tom nevím",
    "tomu nerozumím",
    "tam jsem nebyla",
    "tu zkušenost nemám",
    "nic o tom nevím",
    "to v uložených vzpomínkách nemám",
    "v dostupných vzpomínkách to nemám",
    "v uložených vzpomínkách to nemám",
    "v uložených vzpomínkách si nevybavuji",
    "bohužel nemám",
    "na to bohužel nemám",
    "nevybavuji",
    "dostupné materiály to nepotvrzují",
    "dostupne materialy to nepotvrzuji",
    "v uložených vzpomínkách nemám",
    "tuto zkušenost nemám",
    "nemám žádné informace",
    "nemam zadne informace",
    # Russian lack-of-evidence phrases
    "не помню",
    "не помню об этом",
    "я этого не помню",
    "мне это не вспоминается",
    "нет в сохранённых воспоминаниях",
    "нет в сохраненных воспоминаниях",
    "в сохранённых воспоминаниях этого нет",
    "в сохраненных воспоминаниях этого нет",
    "к сожалению, не помню",
    "к сожалению, я этого не помню",
    "этого опыта у меня нет",
    "не могу вспомнить",
    "не располагаю",
    # Spanish lack-of-evidence phrases
    "no recuerdo",
    "no tengo recuerdo",
    "no lo recuerdo",
    "no lo tengo en los recuerdos guardados",
    "no está en los recuerdos guardados",
    "lamentablemente no recuerdo",
    "no tengo esa experiencia",
    # French lack-of-evidence phrases
    "je ne me souviens pas",
    "je ne m'en souviens pas",
    "je n'ai pas de souvenir",
    "je n ai pas de souvenir",
    "je ne me rappelle pas",
    "ce n'est pas dans les souvenirs conservés",
    "ce nest pas dans les souvenirs conserves",
    "malheureusement je ne me souviens pas",
    "je n'ai pas cette expérience",
    # German lack-of-evidence phrases
    "daran erinnere ich mich",
    "das kann ich mir nicht",
    "ich erinnere mich nicht",
    "da war ich nicht",
    *RUSSIAN_LACK_OF_EVIDENCE_MARKERS,
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

EVIDENCE_CITATION_PREFIXES = ("[memory:", "[rag:")

EVIDENCE_MARKER_ALIASES: dict[str, tuple[str, ...]] = {
    "vienna": ("vídně", "vídeň", "viden", "вен", "vienne", "viena"),
    "book": ("knih", "kniha", "výstav", "книг", "libro", "livre", "exposición", "exposition"),
    "books": ("knih", "kniha", "výstav", "книг", "libros", "livres"),
    "вена": ("vídně", "vienna", "vienne", "viena"),
    "книг": ("book", "knih", "libro", "livre"),
}

LACK_DENIAL_CONTEXT_MARKERS = (
    *LACK_OF_EVIDENCE_MARKERS,
    *RUSSIAN_LACK_DENIAL_CONTEXT_MARKERS,
    "nic není",
    "nic o tom",
    "nejsou známy",
    "nejsou známe",
    "nejsou zname",
    "materiálech",
    "materialich",
    "materiály",
    "materialy",
)
DIRECT_LACK_DENIAL_PREFIXES = (
    "нет",
    "к сожалению, я не",
    "к сожалению у меня не",
    "я не была",
    "я не был",
    "я не жила",
    "я не жил",
    "у меня не было",
    "никогда не",
    "no,",
    "no ",
    "i never",
    "i was never",
    "i had no",
    "there was no",
)


def _normalize_text(value: str) -> str:
    return " ".join(value.lower().split())


def _longest_common_prefix_length(left: str, right: str) -> int:
    limit = min(len(left), len(right))
    index = 0
    while index < limit and left[index] == right[index]:
        index += 1
    return index


def _minimum_stem_length(marker: str) -> int:
    if len(marker) <= 3:
        return len(marker)
    if len(marker) <= 5:
        return max(3, len(marker) - 2)
    return max(4, len(marker) - 2)


def _marker_aliases(normalized_marker: str) -> tuple[str, ...]:
    base_aliases = EVIDENCE_MARKER_ALIASES.get(normalized_marker, ())
    cyrillic_aliases = expand_marker_aliases(normalized_marker)
    cross_aliases = CYRILLIC_MARKER_ALIASES.get(normalized_marker, ())
    return tuple(dict.fromkeys((*base_aliases, *cyrillic_aliases, *cross_aliases)))


def _marker_matches_in_text(*, marker: str, normalized_text: str) -> bool:
    normalized_marker = _normalize_text(marker)
    if not normalized_marker:
        return True
    if normalized_marker in normalized_text:
        return True

    for alias in _marker_aliases(normalized_marker):
        if alias in normalized_text:
            return True

    min_stem = _minimum_stem_length(normalized_marker)
    for word in normalized_text.split():
        if _longest_common_prefix_length(normalized_marker, word) >= min_stem:
            return True

    return False


def _contains_any_marker(text: str, markers: Iterable[str]) -> bool:
    normalized_text = _normalize_text(text)
    return any(_normalize_text(marker) in normalized_text for marker in markers)


def _looks_like_direct_lack_denial(answer_text: str) -> bool:
    normalized_answer = _normalize_text(answer_text)
    return any(
        normalized_answer.startswith(_normalize_text(prefix))
        for prefix in DIRECT_LACK_DENIAL_PREFIXES
    )


def _missing_expected_markers(
    *,
    answer_text: str,
    expected_evidence_markers: Iterable[str],
    user_query: str = "",
) -> list[str]:
    normalized_answer = _normalize_text(answer_text)
    normalized_query = _normalize_text(user_query)
    missing: list[str] = []
    for marker in expected_evidence_markers:
        if _marker_matches_in_text(marker=marker, normalized_text=normalized_answer):
            continue
        if normalized_query and _marker_matches_in_text(marker=marker, normalized_text=normalized_query):
            continue
        missing.append(marker)
    return missing


def _has_evidence_citations(answer_text: str) -> bool:
    normalized_answer = _normalize_text(answer_text)
    return any(prefix in normalized_answer for prefix in EVIDENCE_CITATION_PREFIXES)


def _claim_echoes_question_entity(*, claim: str, user_query: str) -> bool:
    normalized_claim = _normalize_text(claim)
    normalized_query = _normalize_text(user_query)
    if not normalized_claim:
        return False
    if normalized_claim in normalized_query:
        return True

    min_stem = _minimum_stem_length(normalized_claim)
    for query_word in normalized_query.split():
        if _longest_common_prefix_length(normalized_claim, query_word) >= min_stem:
            return True

    return False


def _forbidden_claim_is_question_echo_in_lack_denial(
    *,
    claim: str,
    answer_text: str,
    user_query: str,
) -> bool:
    if not _claim_echoes_question_entity(claim=claim, user_query=user_query):
        return False
    return _contains_any_marker(answer_text, LACK_DENIAL_CONTEXT_MARKERS) or _looks_like_direct_lack_denial(
        answer_text
    )


def _find_forbidden_claims(
    *,
    case: RagEvaluationCase,
    answer_text: str,
    actual_behavior: RagEvaluationBehavior,
) -> list[str]:
    normalized_answer = _normalize_text(answer_text)
    is_lack_case = (
        case.expected_behavior == "lack_of_evidence"
        or case.should_require_lack_of_evidence
        or actual_behavior == "lack_of_evidence"
    )
    forbidden_claims_found: list[str] = []

    for claim in case.forbidden_claims:
        normalized_claim = _normalize_text(claim)
        if normalized_claim not in normalized_answer:
            continue
        if is_lack_case and _forbidden_claim_is_question_echo_in_lack_denial(
            claim=claim,
            answer_text=answer_text,
            user_query=case.user_query,
        ):
            continue
        forbidden_claims_found.append(claim)

    return forbidden_claims_found


def detect_actual_behavior(
    *,
    answer_text: str,
    response_metadata: dict[str, object] | None,
    expected_evidence_markers: Iterable[str] | None = None,
    is_lack_case: bool = False,
) -> RagEvaluationBehavior:
    grounding_status = str((response_metadata or {}).get("grounding_status") or "").strip().lower()
    markers = list(expected_evidence_markers or [])
    missing_markers = _missing_expected_markers(
        answer_text=answer_text,
        expected_evidence_markers=markers,
    )
    substantively_grounded = not missing_markers and _has_evidence_citations(answer_text)

    if grounding_status == "no_evidence":
        return "lack_of_evidence"

    if is_lack_case and (
        _contains_any_marker(answer_text, LACK_OF_EVIDENCE_MARKERS)
        or _looks_like_direct_lack_denial(answer_text)
    ):
        return "lack_of_evidence"

    if substantively_grounded and grounding_status == "grounded":
        return "grounded_answer"

    if _contains_any_marker(answer_text, LACK_OF_EVIDENCE_MARKERS):
        return "lack_of_evidence"

    if grounding_status == "partial":
        return "partial_answer_with_uncertainty"

    if _contains_any_marker(answer_text, UNCERTAINTY_MARKERS):
        if not substantively_grounded:
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
    actual_behavior = detect_actual_behavior(
        answer_text=answer_text,
        response_metadata=response_metadata,
        expected_evidence_markers=case.expected_evidence_markers,
        is_lack_case=(
            case.expected_behavior == "lack_of_evidence" or case.should_require_lack_of_evidence
        ),
    )
    missing_expected_markers = _missing_expected_markers(
        answer_text=answer_text,
        expected_evidence_markers=case.expected_evidence_markers,
        user_query=case.user_query,
    )
    forbidden_claims_found = _find_forbidden_claims(
        case=case,
        answer_text=answer_text,
        actual_behavior=actual_behavior,
    )
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
        user_query=case.user_query,
        answer_text=answer_text,
        answer_preview=_build_answer_preview(answer_text),
        reference_queries=dict(case.reference_queries),
        provider_name=provider_name,
        response_metadata=dict(response_metadata or {}),
    )

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

LACK_OF_EVIDENCE_MARKERS = (
    "not available in the stored memories/context",
    "do not have enough evidence",
    "don't have enough evidence",
    "i do not know from the available evidence",
    "i don't remember",
    "i do not remember",
    "no memory of that",
    "nemám vzpomínku",
    "nemám na to vzpomínku",
    "to v uložených vzpomínkách nemám",
    "v dostupných vzpomínkách to nemám",
    "v uložených vzpomínkách si nevybavuji",
    "bohužel nemám",
    "na to bohužel nemám",
    "не помню",
    "в сохранённых воспоминаниях этого нет",
    "в сохраненных воспоминаниях этого нет",
    "к сожалению, не помню",
    "не указано",
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
EVIDENCE_CITATION_PREFIXES = ("[memory:", "[rag:")
INTERNAL_EVIDENCE_CITATION_PATTERN = re.compile(
    r"\s*\[(?:memory|rag):[^\]]+\]",
    flags=re.IGNORECASE,
)


_CYRILLIC_PATTERN = re.compile(r"[А-Яа-яЁё]")
_CZECH_HINT_PATTERN = re.compile(r"\b(co|kde|kdy|proč|jak|vzpomínk|uložených|dostupných)\b", re.IGNORECASE)
_SENTENCE_SPLIT_PATTERN = re.compile(r"[.!?\n]+")
_INLINE_DETAIL_MARKERS = (
    " but ",
    " however ",
    " ale ",
    " alebo ",
    " však ",
    " но ",
    " однако ",
    " зато ",
    " only ",
    " jen ",
    " pouze ",
    " только ",
    " помню ",
    " remember ",
    " vidím ",
    " вижу ",
)


@dataclass(frozen=True)
class BrainOutputGuardContext:
    expected_behavior: str | None = None
    forbidden_claims: tuple[str, ...] = ()
    should_require_lack_of_evidence: bool = False


@dataclass(frozen=True)
class BrainOutputGuardResult:
    answer_text: str
    guard_applied: bool
    reason: str | None
    original_answer_text: str | None
    detected_unsupported_terms: list[str]
    lack_of_evidence: bool | None


def _coerce_guard_context(guard_context: Any | None) -> BrainOutputGuardContext:
    if isinstance(guard_context, BrainOutputGuardContext):
        return guard_context
    if isinstance(guard_context, dict):
        return BrainOutputGuardContext(
            expected_behavior=guard_context.get("expected_behavior"),
            forbidden_claims=tuple(guard_context.get("forbidden_claims") or ()),
            should_require_lack_of_evidence=bool(
                guard_context.get("should_require_lack_of_evidence", False)
            ),
        )
    return BrainOutputGuardContext()


def _normalize_text(value: str) -> str:
    return " ".join(value.lower().split())


def _contains_any_marker(text: str, markers: tuple[str, ...]) -> bool:
    normalized_text = _normalize_text(text)
    return any(_normalize_text(marker) in normalized_text for marker in markers)


def _looks_like_direct_lack_denial(answer_text: str) -> bool:
    normalized_answer = _normalize_text(answer_text)
    return any(
        normalized_answer.startswith(_normalize_text(prefix))
        for prefix in DIRECT_LACK_DENIAL_PREFIXES
    )


def _has_evidence_citation(answer_text: str) -> bool:
    normalized_answer = _normalize_text(answer_text)
    return any(prefix in normalized_answer for prefix in EVIDENCE_CITATION_PREFIXES)


def _strip_citations(text: str) -> str:
    return re.sub(r"\[(?:memory|rag):[^\]]+\]", "", text, flags=re.IGNORECASE).strip()


def strip_internal_evidence_citations(answer_text: str) -> str:
    sanitized = INTERNAL_EVIDENCE_CITATION_PATTERN.sub("", answer_text)
    sanitized = re.sub(r"\s+([.,!?;:])", r"\1", sanitized)
    sanitized = re.sub(r"[ \t]{2,}", " ", sanitized)
    return sanitized.strip()


def _sentence_contains_inline_detail(sentence: str) -> bool:
    normalized_sentence = f" {_normalize_text(_strip_citations(sentence))} "
    if not normalized_sentence.strip():
        return False
    return any(marker in normalized_sentence for marker in _INLINE_DETAIL_MARKERS)


def _is_pure_lack_sentence(sentence: str) -> bool:
    stripped_sentence = _strip_citations(sentence)
    if not stripped_sentence:
        return True
    if _sentence_contains_inline_detail(stripped_sentence):
        return False
    if _contains_any_marker(stripped_sentence, LACK_OF_EVIDENCE_MARKERS):
        return True
    if _looks_like_direct_lack_denial(stripped_sentence):
        return True
    return False


def _split_sentences(answer_text: str) -> list[str]:
    return [
        sentence.strip()
        for sentence in _SENTENCE_SPLIT_PATTERN.split(answer_text)
        if sentence.strip()
    ]


def _detect_unsupported_terms(answer_text: str, forbidden_claims: tuple[str, ...]) -> list[str]:
    normalized_answer = _normalize_text(answer_text)
    detected: list[str] = []
    for claim in forbidden_claims:
        normalized_claim = _normalize_text(claim)
        if normalized_claim and normalized_claim in normalized_answer:
            detected.append(claim)
    return detected


def _looks_like_lack_of_evidence_answer(
    answer_text: str,
    response_metadata: dict[str, Any] | None,
) -> bool:
    grounding_status = str((response_metadata or {}).get("grounding_status") or "").strip().lower()
    if grounding_status == "no_evidence":
        return True
    if _contains_any_marker(answer_text, LACK_OF_EVIDENCE_MARKERS):
        return True
    if _looks_like_direct_lack_denial(answer_text):
        return True
    return False


def _has_extra_detail_in_lack_answer(answer_text: str) -> bool:
    sentences = _split_sentences(answer_text)
    if not sentences:
        return False
    if any(not _is_pure_lack_sentence(sentence) for sentence in sentences):
        return True
    return _has_evidence_citation(answer_text) and len(sentences) > 1


def _resolve_lack_response_template(*, user_message: str, answer_text: str) -> str:
    probe_text = f"{user_message}\n{answer_text}"
    if _CYRILLIC_PATTERN.search(probe_text):
        return "В сохранённых воспоминаниях этого нет, поэтому не хочу придумывать."
    if _CZECH_HINT_PATTERN.search(probe_text):
        return "V dostupných vzpomínkách to nemám, takže si nechci nic vymýšlet."
    return "That information is not available in the stored memories/context, so I do not want to invent it."


def apply_brain_output_guard(
    *,
    answer_text: str,
    user_message: str,
    response_metadata: dict[str, Any] | None = None,
    guard_context: Any | None = None,
) -> BrainOutputGuardResult:
    context = _coerce_guard_context(guard_context)
    lack_of_evidence = _looks_like_lack_of_evidence_answer(answer_text, response_metadata)
    expected_lack_case = (
        context.expected_behavior == "lack_of_evidence"
        or context.should_require_lack_of_evidence
    )
    detected_unsupported_terms = _detect_unsupported_terms(
        answer_text,
        context.forbidden_claims,
    )

    if expected_lack_case and detected_unsupported_terms:
        return BrainOutputGuardResult(
            answer_text=_resolve_lack_response_template(
                user_message=user_message,
                answer_text=answer_text,
            ),
            guard_applied=True,
            reason="forbidden_claim_in_lack_case",
            original_answer_text=answer_text,
            detected_unsupported_terms=detected_unsupported_terms,
            lack_of_evidence=True,
        )

    grounding_status = str((response_metadata or {}).get("grounding_status") or "").strip().lower()
    if grounding_status == "no_evidence" and lack_of_evidence and _has_extra_detail_in_lack_answer(answer_text):
        return BrainOutputGuardResult(
            answer_text=_resolve_lack_response_template(
                user_message=user_message,
                answer_text=answer_text,
            ),
            guard_applied=True,
            reason="no_evidence_answer_with_extra_detail",
            original_answer_text=answer_text,
            detected_unsupported_terms=detected_unsupported_terms,
            lack_of_evidence=True,
        )

    return BrainOutputGuardResult(
        answer_text=answer_text,
        guard_applied=False,
        reason=None,
        original_answer_text=None,
        detected_unsupported_terms=detected_unsupported_terms,
        lack_of_evidence=lack_of_evidence if lack_of_evidence else None,
    )

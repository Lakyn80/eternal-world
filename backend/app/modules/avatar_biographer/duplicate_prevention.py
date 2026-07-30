"""Deterministic duplicate-question and known-answer validation (Task 65.6).

Every check here is plain string normalization/comparison - no model call,
no embedding similarity - per the roadmap's "the validator must be
conservative... reject obvious repetition without pretending to understand
every possible semantic equivalence perfectly."
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from enum import Enum

from app.db.models import BiographerQuestion
from app.modules.avatar_biographer.topics import BiographerTopic

#: Two normalized questions sharing at least this fraction of their token
#: set are treated as the same underlying question (conservative - high
#: bar, so genuinely different follow-up questions on the same topic are
#: never blocked).
_LEXICAL_OVERLAP_THRESHOLD = 0.8

_PUNCTUATION_PATTERN = re.compile(r"[^\w\s]", re.UNICODE)
_WHITESPACE_PATTERN = re.compile(r"\s+", re.UNICODE)


class RejectionReason(str, Enum):
    EXACT_DUPLICATE = "exact_duplicate"
    HIGH_LEXICAL_OVERLAP = "high_lexical_overlap"
    SAME_TOPIC_INTENT = "same_topic_intent"
    KNOWN_BROAD_FACT = "known_broad_fact"


@dataclass(frozen=True)
class ValidationResult:
    accepted: bool
    reason: RejectionReason | None = None


def normalize_question_text(text: str) -> str:
    """Lowercase, accent/diacritic-preserving Unicode normalization, strip
    punctuation, collapse whitespace. Deliberately does NOT strip
    diacritics (cs/ru text) - only case/punctuation/whitespace are
    considered noise for exact/case/whitespace-duplicate comparison."""

    normalized = unicodedata.normalize("NFC", text).strip().lower()
    normalized = _PUNCTUATION_PATTERN.sub(" ", normalized)
    normalized = _WHITESPACE_PATTERN.sub(" ", normalized).strip()
    return normalized


def _token_set(text: str) -> set[str]:
    return set(normalize_question_text(text).split())


def _lexical_overlap_ratio(a: str, b: str) -> float:
    tokens_a = _token_set(a)
    tokens_b = _token_set(b)
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    smaller = min(len(tokens_a), len(tokens_b))
    return len(intersection) / smaller


def find_duplicate_against_history(
    candidate_question_text: str,
    *,
    topic_key: str,
    candidate_question_intent: str | None,
    previous_questions: list[BiographerQuestion],
) -> ValidationResult:
    """Compares against every previous question for this profile (any
    topic/status) - not only the currently selected topic - since the same
    concrete question could otherwise resurface under a different topic
    label."""

    normalized_candidate = normalize_question_text(candidate_question_text)
    for previous in previous_questions:
        normalized_previous = normalize_question_text(previous.question_text)
        if normalized_candidate == normalized_previous:
            return ValidationResult(accepted=False, reason=RejectionReason.EXACT_DUPLICATE)

    for previous in previous_questions:
        if _lexical_overlap_ratio(candidate_question_text, previous.question_text) >= _LEXICAL_OVERLAP_THRESHOLD:
            return ValidationResult(accepted=False, reason=RejectionReason.HIGH_LEXICAL_OVERLAP)

    if candidate_question_intent:
        for previous in previous_questions:
            if (
                previous.topic == topic_key
                and previous.question_intent == candidate_question_intent
                and previous.status in ("answered", "pending")
            ):
                return ValidationResult(accepted=False, reason=RejectionReason.SAME_TOPIC_INTENT)

    return ValidationResult(accepted=True)


def find_known_answer_violation(
    candidate_question_text: str,
    *,
    topic: BiographerTopic,
    verified_chunk_count: int,
    known_information_used_reported_by_provider: bool,
) -> ValidationResult:
    """Conservative "is this the topic's own generic starter question, when
    we already have verified evidence about this topic" check.

    Deliberately narrow: it only rejects a question textually close to the
    topic's own fixed fallback/starter question (the exact failure mode
    described in the task - re-asking "where did you spend your childhood"
    when the biography already answers it) once verified evidence exists
    for that topic. It does not attempt general semantic fact-checking.
    """

    if verified_chunk_count <= 0:
        return ValidationResult(accepted=True)

    for locale_question in topic.questions.values():
        if _lexical_overlap_ratio(candidate_question_text, locale_question) >= _LEXICAL_OVERLAP_THRESHOLD:
            return ValidationResult(accepted=False, reason=RejectionReason.KNOWN_BROAD_FACT)

    if not known_information_used_reported_by_provider:
        # The provider itself reported it did NOT use the known verified
        # context even though evidence exists for this topic - conservative
        # rejection rather than trusting an ungrounded question.
        return ValidationResult(accepted=False, reason=RejectionReason.KNOWN_BROAD_FACT)

    return ValidationResult(accepted=True)

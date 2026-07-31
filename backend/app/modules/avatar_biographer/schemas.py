from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator

from app.modules.family_memory_enrichment.schemas import ClarificationQuestionRead

SUPPORTED_LOCALES = ("cs", "en", "ru")

#: Task 65.6 - bounded, closed question-intent classification (never
#: free-form) so it stays a safe, low-cardinality provenance/metric field.
QuestionIntent = Literal[
    "specific_memory",
    "specific_person",
    "specific_event",
    "sensory_detail",
    "impact",
    "general_fact",
]


class ProviderQuestionResult(BaseModel):
    """Structured DeepSeek output contract for one generated question
    (Task 65.6). The provider is instructed to return exactly this JSON
    shape; anything else is a validation failure, not a best-effort parse."""

    question: str = Field(min_length=1, max_length=500)
    known_information_used: bool
    question_intent: QuestionIntent
    confidence: Literal["high", "medium", "low"]


class BiographerEligibilityRead(BaseModel):
    eligible: bool
    blocked_reason: str | None = None


class BiographerQuestionRead(BaseModel):
    id: int
    profile_id: int
    topic: str
    #: Language of the stored canonical ``question_text`` (memorial canonical).
    locale: str
    question_text: str
    display_language: str | None = None
    display_text: str | None = None
    display_translation_status: str | None = None
    status: str
    asked_at: datetime
    answered_at: datetime | None
    resulting_candidate_id: int | None
    generation_mode: str
    fallback_used: bool


class BiographerAnswerRequest(BaseModel):
    #: Language the answer was written in (viewer/author language).
    locale: str = Field(pattern="^(cs|en|ru|de)$")
    answer_text: str = Field(min_length=1, max_length=2000)
    #: Optional explicit source language; defaults to ``locale``.
    source_language: str | None = None

    @field_validator("answer_text")
    @classmethod
    def validate_answer_text(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("answer_text must not be empty")
        return normalized

    @field_validator("source_language")
    @classmethod
    def validate_source_language(cls, value: str | None) -> str | None:
        if value is None:
            return None
        from app.modules.language_registry import assert_translation_language

        return assert_translation_language(value)


class BiographerAnswerResponse(BaseModel):
    question: BiographerQuestionRead
    candidate_id: int | None
    enrichment_status: str | None
    unresolved_clarification_count: int | None


class BiographerResumeRead(BaseModel):
    """Task 65.7 (Part D.25) - one composed, read-only view of "what should
    the Biographer tab show right now", so the frontend never has to infer
    it from several separately-fetched, possibly-stale records."""

    profile_id: int
    biography_status: str
    eligible: bool
    blocked_reason: str | None
    active_question: BiographerQuestionRead | None
    candidate_id: int | None
    review_status: str | None
    enrichment_status: str | None
    unresolved_clarification_count: int | None
    promotion_status: str | None
    next_action: str
    #: Task 65.10.1 - the actual currently-answerable clarification question
    #: behind an `active_clarification_exists` block (always present when
    #: that is the blocked reason; `None` otherwise). Without this, the
    #: frontend had no way to render anything below the "please answer the
    #: current clarification question" notice.
    next_clarification_question: ClarificationQuestionRead | None = None

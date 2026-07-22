from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator


SUPPORTED_LOCALES = ("cs", "ru")

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
    locale: str
    question_text: str
    status: str
    asked_at: datetime
    answered_at: datetime | None
    resulting_candidate_id: int | None
    generation_mode: str
    fallback_used: bool


class BiographerAnswerRequest(BaseModel):
    locale: str = Field(pattern="^(cs|ru)$")
    answer_text: str = Field(min_length=1, max_length=2000)

    @field_validator("answer_text")
    @classmethod
    def validate_answer_text(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("answer_text must not be empty")
        return normalized


class BiographerAnswerResponse(BaseModel):
    question: BiographerQuestionRead
    candidate_id: int | None
    enrichment_status: str | None
    unresolved_clarification_count: int | None

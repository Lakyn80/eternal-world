from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator


SUPPORTED_LOCALES = ("cs", "ru")


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

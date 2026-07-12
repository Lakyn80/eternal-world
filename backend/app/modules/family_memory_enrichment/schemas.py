from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from app.modules.family_memory_enrichment.enums import (
    ClarificationStatus,
    ContributionType,
    DisputeStatus,
    EnrichmentStatus,
    FamilyMemoryActorRole,
    MemoryType,
    OwnerReviewAction,
    PrivacyScope,
)


def _normalize(value: str) -> str:
    return " ".join(value.split()).strip()


class DemoFamilyActorContext(BaseModel):
    actor_id: str = Field(min_length=1, max_length=120)
    actor_role: FamilyMemoryActorRole
    relationship_to_owner: str | None = Field(default=None, max_length=120)

    @field_validator("actor_id", "relationship_to_owner", mode="before")
    @classmethod
    def normalize_actor_text(cls, value):
        if value is None:
            return None
        return _normalize(str(value)) or None


class PersonalMemoryDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    what_happened: str | None = Field(default=None, max_length=500)
    who_was_present: str | None = Field(default=None, max_length=500)
    relationship_context: str | None = Field(default=None, max_length=500)
    place: str | None = Field(default=None, max_length=500)
    approximate_date: str | None = Field(default=None, max_length=120)
    approximate_period: str | None = Field(default=None, max_length=500)
    frequency: str | None = Field(default=None, max_length=120)
    song_title: str | None = Field(default=None, max_length=300)
    object_or_activity: str | None = Field(default=None, max_length=500)
    emotional_context: str | None = Field(default=None, max_length=500)
    personal_significance: str | None = Field(default=None, max_length=500)
    contributor_perspective: str | None = Field(default=None, max_length=500)
    owner_perspective: str | None = Field(default=None, max_length=500)
    additional_notes: str | None = Field(default=None, max_length=500)

    @field_validator("*", mode="before")
    @classmethod
    def normalize_details(cls, value):
        if value is None:
            return None
        return _normalize(str(value)) or None


class FamilyMemoryContributionCreate(DemoFamilyActorContext):
    contribution_type: ContributionType = ContributionType.CLARIFICATION_ANSWER
    contribution_text: str = Field(min_length=1, max_length=1000)
    structured_details: PersonalMemoryDetails | None = None
    language: str | None = Field(default="ru", max_length=16)
    source_message_hash: str | None = Field(
        default=None,
        pattern=r"^[0-9a-fA-F]{64}$",
    )
    trace_id: str | None = Field(default=None, max_length=120)
    supersedes_contribution_id: int | None = Field(default=None, gt=0)
    is_disputed: bool = False

    @field_validator("contribution_text", mode="before")
    @classmethod
    def normalize_contribution(cls, value):
        normalized = _normalize(str(value))
        if not normalized:
            raise ValueError("contribution_text is required")
        return normalized

    @field_validator("source_message_hash", mode="after")
    @classmethod
    def normalize_source_hash(cls, value: str | None) -> str | None:
        return value.lower() if value is not None else None


class FamilyMemoryContributionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    contribution_id: int
    candidate_id: int
    avatar_id: str
    profile_id: int | None
    actor_id: str
    actor_role: FamilyMemoryActorRole
    relationship_to_owner: str | None
    contribution_type: ContributionType
    contribution_text: str
    structured_details: dict[str, Any] | None
    language: str | None
    source_message_hash: str | None
    trace_id: str | None
    supersedes_contribution_id: int | None
    is_owner_correction: bool
    is_disputed: bool
    privacy_scope_snapshot: PrivacyScope
    created_at: datetime


class ClarificationQuestionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    clarification_id: int
    candidate_id: int
    question_key: str
    question_text: str
    language: str | None
    status: ClarificationStatus
    required: bool
    asked_at: datetime
    answered_at: datetime | None
    answered_by: str | None
    answer_contribution_id: int | None


class ClarificationAnswerRequest(DemoFamilyActorContext):
    answer_text: str = Field(min_length=1, max_length=1000)
    structured_details: PersonalMemoryDetails | None = None
    trace_id: str | None = Field(default=None, max_length=120)

    @field_validator("answer_text", mode="before")
    @classmethod
    def normalize_answer(cls, value):
        normalized = _normalize(str(value))
        if not normalized:
            raise ValueError("answer_text is required")
        return normalized


class ClarificationSkipRequest(DemoFamilyActorContext):
    reason: str | None = Field(default=None, max_length=500)


class FinalizeRequest(DemoFamilyActorContext):
    pass


class OwnerReviewRequest(DemoFamilyActorContext):
    action: OwnerReviewAction
    finalized_memory_text: str | None = Field(default=None, max_length=500)
    privacy_scope: PrivacyScope | None = None
    review_note: str | None = Field(default=None, max_length=500)
    rejection_reason: str | None = Field(default=None, max_length=500)

    @field_validator("finalized_memory_text", "review_note", "rejection_reason", mode="before")
    @classmethod
    def normalize_review_text(cls, value):
        if value is None:
            return None
        return _normalize(str(value)) or None

    @model_validator(mode="after")
    def validate_action_fields(self):
        if self.action == OwnerReviewAction.EDIT_AND_CONFIRM and not self.finalized_memory_text:
            raise ValueError("finalized_memory_text is required for edit_and_confirm")
        if (
            self.finalized_memory_text is not None
            and self.action
            not in {
                OwnerReviewAction.EDIT_AND_CONFIRM,
                OwnerReviewAction.APPROVE_MULTIPLE_PERSPECTIVES,
            }
        ):
            raise ValueError("finalized_memory_text is not allowed for this action")
        if self.rejection_reason is not None and self.action != OwnerReviewAction.REJECT:
            raise ValueError("rejection_reason is allowed only for reject")
        return self


class CandidateEnrichmentRead(BaseModel):
    candidate_id: int
    avatar_id: str
    profile_id: int | None
    memory_type: MemoryType
    enrichment_status: EnrichmentStatus
    review_status: str
    dispute_status: DisputeStatus
    privacy_scope: PrivacyScope
    unresolved_clarification_count: int
    finalized_memory_text: str | None
    finalized_at: datetime | None
    finalized_by: str | None
    owner_reviewed_at: datetime | None
    owner_reviewed_by: str | None
    contribution_count: int
    next_clarification_question: ClarificationQuestionRead | None
    promotion_id: int | None = None
    promotion_status: str | None = None
    searchable_as_fact: bool = False
    explicit_indexing_required: bool = False


class OwnerReviewResponse(CandidateEnrichmentRead):
    promotion_created: bool = False

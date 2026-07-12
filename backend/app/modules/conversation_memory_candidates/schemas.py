from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.db.models import ConversationMemoryCandidate
from app.modules.family_memory_enrichment.enums import (
    DisputeStatus,
    EnrichmentStatus,
    MemoryType,
    PrivacyScope,
)


MEMORY_CANDIDATE_EXCERPT_MAX_LENGTH = 160
MEMORY_CANDIDATE_TEXT_MAX_LENGTH = 500
MEMORY_CANDIDATE_REASON_MAX_LENGTH = 500
MEMORY_CANDIDATE_REVIEW_NOTE_MAX_LENGTH = 500
MEMORY_CANDIDATE_REJECTION_REASON_MAX_LENGTH = 500
MEMORY_CANDIDATE_AVATAR_ID_MAX_LENGTH = 120
MEMORY_CANDIDATE_TRACE_ID_MAX_LENGTH = 120
MEMORY_CANDIDATE_CONVERSATION_ID_MAX_LENGTH = 120
MEMORY_CANDIDATE_LANGUAGE_MAX_LENGTH = 16


class MemoryCandidateStatus(str, Enum):
    NEEDS_REVIEW = "needs_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    ARCHIVED = "archived"


class MemoryCandidateConfidence(str, Enum):
    UNVERIFIED = "unverified"


class MemoryCandidateSource(str, Enum):
    CONVERSATION = "conversation"


def _normalize_text(value: str) -> str:
    return " ".join(value.split()).strip()


def _truncate_text(value: str, *, limit: int) -> str:
    normalized_value = _normalize_text(value)
    if len(normalized_value) <= limit:
        return normalized_value
    return f"{normalized_value[: limit - 3].rstrip()}..."


class MemoryCandidateCreate(BaseModel):
    owner_user_id: int = Field(gt=0)
    avatar_id: str = Field(min_length=1, max_length=MEMORY_CANDIDATE_AVATAR_ID_MAX_LENGTH)
    profile_id: int | None = Field(default=None, gt=0)
    conversation_id: str | None = Field(default=None, max_length=MEMORY_CANDIDATE_CONVERSATION_ID_MAX_LENGTH)
    trace_id: str | None = Field(default=None, max_length=MEMORY_CANDIDATE_TRACE_ID_MAX_LENGTH)
    source: MemoryCandidateSource = MemoryCandidateSource.CONVERSATION
    status: MemoryCandidateStatus = MemoryCandidateStatus.NEEDS_REVIEW
    confidence: MemoryCandidateConfidence = MemoryCandidateConfidence.UNVERIFIED
    user_message_excerpt: str = Field(min_length=1, max_length=MEMORY_CANDIDATE_EXCERPT_MAX_LENGTH)
    proposed_memory_text: str = Field(min_length=1, max_length=MEMORY_CANDIDATE_TEXT_MAX_LENGTH)
    reason: str = Field(min_length=1, max_length=MEMORY_CANDIDATE_REASON_MAX_LENGTH)
    language: str | None = Field(default=None, max_length=MEMORY_CANDIDATE_LANGUAGE_MAX_LENGTH)
    memory_type: MemoryType = MemoryType.GENERAL
    enrichment_status: EnrichmentStatus = EnrichmentStatus.READY_FOR_OWNER_REVIEW
    finalized_memory_text: str | None = Field(default=None, max_length=MEMORY_CANDIDATE_TEXT_MAX_LENGTH)
    privacy_scope: PrivacyScope = PrivacyScope.ALL_FAMILY
    dispute_status: DisputeStatus = DisputeStatus.NONE
    unresolved_clarification_count: int = Field(default=0, ge=0)
    workflow_version: int = Field(default=1, ge=1, le=2)

    @field_validator("avatar_id", mode="before")
    @classmethod
    def normalize_avatar_id(cls, value: str) -> str:
        normalized_value = _normalize_text(str(value))
        if not normalized_value:
            raise ValueError("avatar_id is required")
        return normalized_value

    @field_validator("conversation_id", "trace_id", "language", mode="before")
    @classmethod
    def normalize_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized_value = _normalize_text(str(value))
        return normalized_value or None

    @field_validator("user_message_excerpt", mode="before")
    @classmethod
    def normalize_excerpt(cls, value: str) -> str:
        truncated_value = _truncate_text(str(value), limit=MEMORY_CANDIDATE_EXCERPT_MAX_LENGTH)
        if not truncated_value:
            raise ValueError("user_message_excerpt is required")
        return truncated_value

    @field_validator("proposed_memory_text", "reason", "finalized_memory_text", mode="before")
    @classmethod
    def normalize_required_text(cls, value: str) -> str:
        if value is None:
            return None
        normalized_value = _normalize_text(str(value))
        if not normalized_value:
            raise ValueError("text field is required")
        return normalized_value


class MemoryCandidateReviewUpdate(BaseModel):
    review_note: str | None = Field(default=None, max_length=MEMORY_CANDIDATE_REVIEW_NOTE_MAX_LENGTH)
    rejection_reason: str | None = Field(default=None, max_length=MEMORY_CANDIDATE_REJECTION_REASON_MAX_LENGTH)
    reviewed_by: int | None = Field(default=None, gt=0)

    @field_validator("review_note", "rejection_reason", mode="before")
    @classmethod
    def normalize_review_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized_value = _normalize_text(str(value))
        return normalized_value or None


class MemoryCandidateRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    candidate_id: int
    owner_user_id: int
    avatar_id: str
    profile_id: int | None = None
    conversation_id: str | None = None
    trace_id: str | None = None
    source: MemoryCandidateSource
    status: MemoryCandidateStatus
    confidence: MemoryCandidateConfidence
    user_message_excerpt: str
    proposed_memory_text: str
    reason: str
    language: str | None = None
    created_at: datetime
    updated_at: datetime
    reviewed_at: datetime | None = None
    reviewed_by: int | None = None
    review_note: str | None = None
    rejection_reason: str | None = None
    memory_type: MemoryType
    enrichment_status: EnrichmentStatus
    finalized_memory_text: str | None = None
    privacy_scope: PrivacyScope
    dispute_status: DisputeStatus
    finalized_at: datetime | None = None
    finalized_by: str | None = None
    owner_reviewed_at: datetime | None = None
    owner_reviewed_by: str | None = None
    owner_review_actor_role: str | None = None
    unresolved_clarification_count: int
    version: int
    workflow_version: int


class MemoryCandidateListResponse(BaseModel):
    items: list[MemoryCandidateRead]
    total: int


def build_memory_candidate_read(candidate: ConversationMemoryCandidate) -> MemoryCandidateRead:
    return MemoryCandidateRead(
        candidate_id=candidate.id,
        owner_user_id=candidate.owner_user_id,
        avatar_id=candidate.avatar_id,
        profile_id=candidate.profile_id,
        conversation_id=candidate.conversation_id,
        trace_id=candidate.trace_id,
        source=MemoryCandidateSource(candidate.source),
        status=MemoryCandidateStatus(candidate.status),
        confidence=MemoryCandidateConfidence(candidate.confidence),
        user_message_excerpt=candidate.user_message_excerpt,
        proposed_memory_text=candidate.proposed_memory_text,
        reason=candidate.reason,
        language=candidate.language,
        created_at=candidate.created_at,
        updated_at=candidate.updated_at,
        reviewed_at=candidate.reviewed_at,
        reviewed_by=candidate.reviewed_by,
        review_note=candidate.review_note,
        rejection_reason=candidate.rejection_reason,
        memory_type=MemoryType(candidate.memory_type),
        enrichment_status=EnrichmentStatus(candidate.enrichment_status),
        finalized_memory_text=candidate.finalized_memory_text,
        privacy_scope=PrivacyScope(candidate.privacy_scope),
        dispute_status=DisputeStatus(candidate.dispute_status),
        finalized_at=candidate.finalized_at,
        finalized_by=candidate.finalized_by,
        owner_reviewed_at=candidate.owner_reviewed_at,
        owner_reviewed_by=candidate.owner_reviewed_by,
        owner_review_actor_role=candidate.owner_review_actor_role,
        unresolved_clarification_count=candidate.unresolved_clarification_count,
        version=candidate.version,
        workflow_version=candidate.workflow_version,
    )

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.db.models import AvatarMemoryPromotion


AVATAR_MEMORY_PROMOTION_AVATAR_ID_MAX_LENGTH = 120
AVATAR_MEMORY_PROMOTION_TRACE_ID_MAX_LENGTH = 120
AVATAR_MEMORY_PROMOTION_LANGUAGE_MAX_LENGTH = 16
AVATAR_MEMORY_PROMOTION_TEXT_MAX_LENGTH = 500
AVATAR_MEMORY_PROMOTION_FAILURE_REASON_MAX_LENGTH = 500
AVATAR_MEMORY_PROMOTION_SOURCE_STATUS_MAX_LENGTH = 32
AVATAR_MEMORY_PROMOTION_REVIEW_NOTE_MAX_LENGTH = 500


class AvatarMemoryPromotionSourceType(str, Enum):
    CONVERSATION_CANDIDATE = "conversation_candidate"


class AvatarMemoryPromotionStatus(str, Enum):
    PENDING_INDEX = "pending_index"
    INDEXED = "indexed"
    FAILED = "failed"
    CANCELLED = "cancelled"


def _normalize_text(value: str) -> str:
    return " ".join(value.split()).strip()


class AvatarMemoryPromotionCreate(BaseModel):
    owner_user_id: int = Field(gt=0)
    candidate_id: int = Field(gt=0)
    avatar_id: str = Field(min_length=1, max_length=AVATAR_MEMORY_PROMOTION_AVATAR_ID_MAX_LENGTH)
    profile_id: int | None = Field(default=None, gt=0)
    source_type: AvatarMemoryPromotionSourceType = AvatarMemoryPromotionSourceType.CONVERSATION_CANDIDATE
    promotion_status: AvatarMemoryPromotionStatus = AvatarMemoryPromotionStatus.PENDING_INDEX
    approved_memory_text: str = Field(min_length=1, max_length=AVATAR_MEMORY_PROMOTION_TEXT_MAX_LENGTH)
    normalized_memory_text: str | None = Field(default=None, max_length=AVATAR_MEMORY_PROMOTION_TEXT_MAX_LENGTH)
    language: str | None = Field(default=None, max_length=AVATAR_MEMORY_PROMOTION_LANGUAGE_MAX_LENGTH)
    trace_id: str | None = Field(default=None, max_length=AVATAR_MEMORY_PROMOTION_TRACE_ID_MAX_LENGTH)
    source_candidate_status_snapshot: str = Field(
        min_length=1,
        max_length=AVATAR_MEMORY_PROMOTION_SOURCE_STATUS_MAX_LENGTH,
    )
    review_note_snapshot: str | None = Field(default=None, max_length=AVATAR_MEMORY_PROMOTION_REVIEW_NOTE_MAX_LENGTH)

    @field_validator(
        "avatar_id",
        "approved_memory_text",
        "normalized_memory_text",
        "language",
        "trace_id",
        "source_candidate_status_snapshot",
        "review_note_snapshot",
        mode="before",
    )
    @classmethod
    def normalize_text_fields(cls, value: str | None):
        if value is None:
            return None
        normalized_value = _normalize_text(str(value))
        return normalized_value or None

    @field_validator("avatar_id", "approved_memory_text", "source_candidate_status_snapshot")
    @classmethod
    def require_text_fields(cls, value: str | None) -> str:
        if value is None:
            raise ValueError("required text field is missing")
        return value

    @field_validator("normalized_memory_text", mode="after")
    @classmethod
    def fill_normalized_memory_text(cls, value: str | None, info):
        if value:
            return value
        approved_memory_text = info.data.get("approved_memory_text")
        if approved_memory_text is None:
            raise ValueError("approved_memory_text is required")
        return approved_memory_text


class AvatarMemoryPromotionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    promotion_id: int
    candidate_id: int
    owner_user_id: int
    avatar_id: str
    profile_id: int | None = None
    source_type: AvatarMemoryPromotionSourceType
    promotion_status: AvatarMemoryPromotionStatus
    approved_memory_text: str
    normalized_memory_text: str
    language: str | None = None
    searchable_as_fact: bool
    created_at: datetime
    updated_at: datetime
    indexed_at: datetime | None = None
    cancelled_at: datetime | None = None
    failure_reason: str | None = None
    trace_id: str | None = None
    source_candidate_status_snapshot: str
    review_note_snapshot: str | None = None


class AvatarMemoryPromotionListResponse(BaseModel):
    items: list[AvatarMemoryPromotionRead]
    total: int


class AvatarMemoryPromotionCreateResult(BaseModel):
    promotion: AvatarMemoryPromotionRead
    created: bool


def build_avatar_memory_promotion_read(promotion: AvatarMemoryPromotion) -> AvatarMemoryPromotionRead:
    return AvatarMemoryPromotionRead(
        promotion_id=promotion.id,
        candidate_id=promotion.candidate_id,
        owner_user_id=promotion.owner_user_id,
        avatar_id=promotion.avatar_id,
        profile_id=promotion.profile_id,
        source_type=AvatarMemoryPromotionSourceType(promotion.source_type),
        promotion_status=AvatarMemoryPromotionStatus(promotion.promotion_status),
        approved_memory_text=promotion.approved_memory_text,
        normalized_memory_text=promotion.normalized_memory_text,
        language=promotion.language,
        searchable_as_fact=promotion.promotion_status == AvatarMemoryPromotionStatus.INDEXED.value,
        created_at=promotion.created_at,
        updated_at=promotion.updated_at,
        indexed_at=promotion.indexed_at,
        cancelled_at=promotion.cancelled_at,
        failure_reason=promotion.failure_reason,
        trace_id=promotion.trace_id,
        source_candidate_status_snapshot=promotion.source_candidate_status_snapshot,
        review_note_snapshot=promotion.review_note_snapshot,
    )

from __future__ import annotations

import re
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.modules.memory_profiles.schemas import normalize_optional_text, normalize_required_text


MAX_RAG_SOURCE_RAW_TEXT_LENGTH = 200_000
LANGUAGE_PATTERN = re.compile(r"^[a-z]{2,8}(?:[-_][a-z0-9]{2,8})?$")
ALLOWED_RAG_SOURCE_TYPES = frozenset(
    {
        "manual_text",
        "biography",
        "timeline_memory",
        "document_text",
        "chat_export",
        "audio_transcript",
        "video_transcript",
        "letter",
        "diary",
        "conversation_candidate",
        "other",
    }
)
READY_FOR_CLEANING_STATUS = "ready_for_cleaning"


def normalize_language(value: str | None) -> str | None:
    if value is None:
        return None

    normalized_value = value.strip().lower()
    if not normalized_value:
        return None

    if normalized_value == "unknown":
        return normalized_value

    if not LANGUAGE_PATTERN.fullmatch(normalized_value):
        raise ValueError("language must be like ru, cs, en, or unknown")

    return normalized_value


class RagSourceCreate(BaseModel):
    title: str = Field(max_length=200)
    raw_text: str = Field(max_length=MAX_RAG_SOURCE_RAW_TEXT_LENGTH)
    source_type: str
    language: str | None = Field(default=None, max_length=16)
    source_metadata: dict[str, Any] | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        return normalize_required_text(value, "title")

    @field_validator("raw_text")
    @classmethod
    def validate_raw_text(cls, value: str) -> str:
        return normalize_required_text(value, "raw_text")

    @field_validator("source_type")
    @classmethod
    def validate_source_type(cls, value: str) -> str:
        normalized_value = normalize_required_text(value, "source_type").lower()
        if normalized_value not in ALLOWED_RAG_SOURCE_TYPES:
            raise ValueError(
                "source_type must be one of: "
                "manual_text, biography, timeline_memory, document_text, chat_export, "
                "audio_transcript, video_transcript, letter, diary, conversation_candidate, other"
            )

        return normalized_value

    @field_validator("language")
    @classmethod
    def validate_language(cls, value: str | None) -> str | None:
        return normalize_language(value)


class RagSourceUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    raw_text: str | None = Field(default=None, max_length=MAX_RAG_SOURCE_RAW_TEXT_LENGTH)
    source_type: str | None = None
    language: str | None = Field(default=None, max_length=16)
    source_metadata: dict[str, Any] | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str | None) -> str | None:
        if value is None:
            raise ValueError("title must not be null")

        return normalize_required_text(value, "title")

    @field_validator("raw_text")
    @classmethod
    def validate_raw_text(cls, value: str | None) -> str | None:
        if value is None:
            raise ValueError("raw_text must not be null")

        return normalize_required_text(value, "raw_text")

    @field_validator("source_type")
    @classmethod
    def validate_source_type(cls, value: str | None) -> str | None:
        if value is None:
            raise ValueError("source_type must not be null")

        normalized_value = normalize_required_text(value, "source_type").lower()
        if normalized_value not in ALLOWED_RAG_SOURCE_TYPES:
            raise ValueError(
                "source_type must be one of: "
                "manual_text, biography, timeline_memory, document_text, chat_export, "
                "audio_transcript, video_transcript, letter, diary, conversation_candidate, other"
            )

        return normalized_value

    @field_validator("language")
    @classmethod
    def validate_language(cls, value: str | None) -> str | None:
        return normalize_language(value)


class RagSourceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_user_id: int
    profile_id: int
    source_type: str
    title: str
    raw_text: str
    normalized_text: str | None
    language: str | None
    status: str
    processing_error: str | None
    source_metadata: dict[str, Any] | None
    created_at: datetime
    updated_at: datetime


def build_rag_source_read(source: Any) -> RagSourceRead:
    return RagSourceRead(
        id=source.id,
        owner_user_id=source.owner_user_id,
        profile_id=source.profile_id,
        source_type=source.source_type,
        title=source.title,
        raw_text=source.raw_text,
        normalized_text=source.normalized_text,
        language=source.language,
        status=source.status,
        processing_error=source.processing_error,
        source_metadata=source.source_metadata,
        created_at=source.created_at,
        updated_at=source.updated_at,
    )

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.modules.memory_profiles.schemas import normalize_optional_text, normalize_required_text


ALLOWED_MEMORY_TYPES = frozenset({"text", "photo", "audio", "video"})


class MemoryCreate(BaseModel):
    title: str = Field(max_length=200)
    content: str | None = None
    memory_type: str
    occurred_at: datetime | None = None
    occurred_year: int | None = Field(default=None, ge=1, le=9999)
    media_id: int | None = Field(default=None, gt=0)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        return normalize_required_text(value, "title")

    @field_validator("content")
    @classmethod
    def validate_content(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)

    @field_validator("memory_type")
    @classmethod
    def validate_memory_type(cls, value: str) -> str:
        normalized_value = normalize_required_text(value, "memory_type").lower()
        if normalized_value not in ALLOWED_MEMORY_TYPES:
            raise ValueError("memory_type must be one of: text, photo, audio, video")

        return normalized_value


class MemoryUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    content: str | None = None
    memory_type: str | None = None
    occurred_at: datetime | None = None
    occurred_year: int | None = Field(default=None, ge=1, le=9999)
    media_id: int | None = Field(default=None, gt=0)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str | None) -> str | None:
        if value is None:
            raise ValueError("title must not be null")

        return normalize_required_text(value, "title")

    @field_validator("content")
    @classmethod
    def validate_content(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)

    @field_validator("memory_type")
    @classmethod
    def validate_memory_type(cls, value: str | None) -> str | None:
        if value is None:
            raise ValueError("memory_type must not be null")

        normalized_value = normalize_required_text(value, "memory_type").lower()
        if normalized_value not in ALLOWED_MEMORY_TYPES:
            raise ValueError("memory_type must be one of: text, photo, audio, video")

        return normalized_value


class MemoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    profile_id: int
    owner_user_id: int
    title: str
    content: str | None
    memory_type: str
    occurred_at: datetime | None
    occurred_year: int | None
    media_id: int | None
    created_at: datetime
    updated_at: datetime


def build_memory_read(memory: Any) -> MemoryRead:
    return MemoryRead(
        id=memory.id,
        profile_id=memory.memory_profile_id,
        owner_user_id=memory.user_id,
        title=memory.title,
        content=memory.content,
        memory_type=memory.memory_type,
        occurred_at=memory.occurred_at,
        occurred_year=memory.occurred_year,
        media_id=memory.media_id,
        created_at=memory.created_at,
        updated_at=memory.updated_at,
    )

from __future__ import annotations

from datetime import date, datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def normalize_required_text(value: str, field_name: str) -> str:
    normalized_value = value.strip()

    if not normalized_value:
        raise ValueError(f"{field_name} must not be empty")

    return normalized_value


def normalize_optional_text(value: str | None) -> str | None:
    if value is None:
        return None

    normalized_value = value.strip()
    return normalized_value or None


def validate_date_range(
    birth_date: date | None,
    death_date: date | None,
) -> None:
    if birth_date is not None and death_date is not None and death_date < birth_date:
        raise ValueError("death_date must be on or after birth_date")


class MemoryProfileCreate(BaseModel):
    name: str = Field(max_length=120)
    birth_date: date | None = None
    death_date: date | None = None
    biography: str | None = None
    personality: str | None = None
    catchphrases: str | None = None
    is_public: bool = False

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        return normalize_required_text(value, "name")

    @field_validator("biography", "personality", "catchphrases")
    @classmethod
    def validate_optional_text(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)

    @model_validator(mode="after")
    def validate_dates(self) -> "MemoryProfileCreate":
        validate_date_range(self.birth_date, self.death_date)
        return self


class MemoryProfileUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=120)
    birth_date: date | None = None
    death_date: date | None = None
    biography: str | None = None
    personality: str | None = None
    catchphrases: str | None = None
    is_public: bool | None = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        if value is None:
            raise ValueError("name must not be null")

        return normalize_required_text(value, "name")

    @field_validator("biography", "personality", "catchphrases")
    @classmethod
    def validate_optional_text(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)

    @model_validator(mode="after")
    def validate_dates(self) -> "MemoryProfileUpdate":
        validate_date_range(self.birth_date, self.death_date)
        return self


class MemoryProfilePhotoAssign(BaseModel):
    media_id: int = Field(gt=0)


class MemoryProfileRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    photo_media_id: int | None
    photo_url: str | None
    name: str
    birth_date: date | None
    death_date: date | None
    biography: str | None
    personality: str | None
    catchphrases: str | None
    is_public: bool
    created_at: datetime
    updated_at: datetime

    @field_validator("photo_url")
    @classmethod
    def reject_absolute_filesystem_paths(cls, value: str | None) -> str | None:
        if value is not None and (value.startswith("/app/") or value.startswith("C:\\")):
            raise ValueError("Absolute filesystem paths are not allowed")

        return value


def build_memory_profile_read(memory_profile: Any) -> MemoryProfileRead:
    photo_url = None
    if getattr(memory_profile, "main_photo_media", None) is not None:
        from app.modules.media.storage import get_storage_provider

        storage_provider = get_storage_provider(memory_profile.main_photo_media.storage_provider)
        try:
            photo_url = storage_provider.build_public_url(
                storage_key=memory_profile.main_photo_media.storage_key,
            )
        except NotImplementedError:
            photo_url = None

    return MemoryProfileRead(
        id=memory_profile.id,
        user_id=memory_profile.user_id,
        photo_media_id=memory_profile.main_photo_media_id,
        photo_url=photo_url,
        name=memory_profile.name,
        birth_date=memory_profile.birth_date,
        death_date=memory_profile.death_date,
        biography=memory_profile.biography,
        personality=memory_profile.personality,
        catchphrases=memory_profile.catchphrases,
        is_public=memory_profile.is_public,
        created_at=memory_profile.created_at,
        updated_at=memory_profile.updated_at,
    )

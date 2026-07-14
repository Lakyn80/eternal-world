from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from app.modules.content_translation.enums import (
    SupportedContentLanguage,
    TranslatableEntityType,
    TranslationStatus,
)


class PreservedEntity(BaseModel):
    """One named entity the provider reports it preserved verbatim/faithfully.

    Purely informational (surfaced in technical review sections); never used
    to gate eligibility.
    """

    source: str
    translated: str


class ProviderTranslationResult(BaseModel):
    """Structured provider output contract (Part D.14 of the task spec).

    The provider is instructed to return exactly this JSON shape. Anything
    else is a validation failure, not a best-effort parse.
    """

    translated_text: str
    preserved_entities: list[PreservedEntity] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class TranslationFieldRequest(BaseModel):
    """Input to :func:`content_translation.service.translate_content_field`."""

    model_config = ConfigDict(use_enum_values=True)

    candidate_id: int | None = None
    contribution_id: int | None = None
    clarification_id: int | None = None
    entity_type: TranslatableEntityType
    entity_id: str = Field(min_length=1, max_length=64)
    field_name: str = Field(min_length=1, max_length=64)
    source_language: SupportedContentLanguage
    target_language: SupportedContentLanguage
    source_text: str = Field(min_length=1, max_length=4000)


class MemoryContentTranslationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    candidate_id: int
    contribution_id: int | None
    clarification_id: int | None
    entity_type: str
    entity_id: str
    field_name: str
    source_language: str
    target_language: str
    source_text: str
    translated_text: str | None
    source_hash: str
    translation_status: TranslationStatus
    translation_provider: str | None
    translation_model: str | None
    translation_version: int
    translated_at: datetime | None
    reviewed_at: datetime | None
    reviewed_by: str | None
    created_at: datetime
    updated_at: datetime


class LocalizedTextEntry(BaseModel):
    """One language's view of a translatable field, for API responses."""

    text: str | None
    status: str
    is_source: bool
    translated_at: datetime | None = None
    stale: bool = False


class LocalizedContent(BaseModel):
    """Both language views of a single translatable field."""

    field_name: str
    source_language: str
    cs: LocalizedTextEntry | None = None
    ru: LocalizedTextEntry | None = None


class TranslationRetryResult(BaseModel):
    translation: MemoryContentTranslationRead
    retried: bool

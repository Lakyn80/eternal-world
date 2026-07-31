from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    full_name: str | None = None
    is_active: bool
    preferred_ui_language: str = "en"
    created_at: datetime
    updated_at: datetime


class UserPreferencesUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    preferred_ui_language: str = Field(min_length=2, max_length=8)

    @field_validator("preferred_ui_language")
    @classmethod
    def validate_ui_language(cls, value: str) -> str:
        from app.modules.language_registry import assert_ui_language

        return assert_ui_language(value)

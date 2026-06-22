from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class RagSourceProcessRequest(BaseModel):
    model_code: str | None = Field(default=None, max_length=64)

    @field_validator("model_code")
    @classmethod
    def normalize_model_code(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip().lower()
        return normalized_value or None

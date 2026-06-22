from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class RagRetrievalRequest(BaseModel):
    query: str = Field(min_length=1, max_length=5000)
    model_code: str | None = Field(default=None, max_length=64)
    limit: int = Field(default=5, ge=1, le=20)
    score_threshold: float | None = None
    language: str | None = Field(default=None, max_length=16)
    source_type: str | None = Field(default=None, max_length=32)

    @field_validator("query")
    @classmethod
    def normalize_query(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("Query must not be empty")

        return normalized_value

    @field_validator("model_code")
    @classmethod
    def normalize_model_code(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip().lower()
        return normalized_value or None

    @field_validator("language")
    @classmethod
    def normalize_language(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip().lower()
        return normalized_value or None

    @field_validator("source_type")
    @classmethod
    def normalize_source_type(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip().lower()
        return normalized_value or None


class RagRetrievalResultRead(BaseModel):
    chunk_id: int
    source_id: int
    embedding_id: int
    score: float
    text: str
    chunk_index: int
    language: str | None
    source_type: str
    validation_status: str
    text_hash: str
    qdrant_collection: str
    payload_metadata: dict[str, Any]


class RagRetrievalResponseRead(BaseModel):
    profile_id: int
    query: str
    model_code: str
    results: list[RagRetrievalResultRead]

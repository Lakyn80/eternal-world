from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class RagChunkRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_user_id: int
    profile_id: int
    source_id: int
    chunk_index: int
    chunk_text: str
    text_hash: str
    token_estimate: int
    char_count: int
    sentence_count: int
    language: str | None
    chunk_metadata: dict[str, Any] | None
    validation_status: str
    validation_errors: list[str] | None
    created_at: datetime
    updated_at: datetime


class RagSourceChunkingSummaryRead(BaseModel):
    source_id: int
    profile_id: int
    owner_user_id: int
    source_status: str
    chunk_count: int
    valid_count: int
    warning_count: int
    invalid_count: int
    source_validation_errors: list[str]
    processing_error: str | None
    normalized_text_updated: bool


def build_rag_chunk_read(chunk: Any) -> RagChunkRead:
    return RagChunkRead(
        id=chunk.id,
        owner_user_id=chunk.owner_user_id,
        profile_id=chunk.profile_id,
        source_id=chunk.source_id,
        chunk_index=chunk.chunk_index,
        chunk_text=chunk.chunk_text,
        text_hash=chunk.text_hash,
        token_estimate=chunk.token_estimate,
        char_count=chunk.char_count,
        sentence_count=chunk.sentence_count,
        language=chunk.language,
        chunk_metadata=chunk.chunk_metadata,
        validation_status=chunk.validation_status,
        validation_errors=chunk.validation_errors,
        created_at=chunk.created_at,
        updated_at=chunk.updated_at,
    )

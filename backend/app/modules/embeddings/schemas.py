from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class RagEmbeddingCreate(BaseModel):
    model_code: str | None = Field(default=None, max_length=64)


class RagEmbeddingRead(BaseModel):
    id: int
    chunk_id: int
    source_id: int
    profile_id: int
    owner_user_id: int
    model_code: str
    vector_dimension: int
    status: str
    error_message: str | None
    embedding_metadata: dict[str, Any] | None
    created_at: datetime
    updated_at: datetime
    vector: list[float] | None = None


class RagSourceEmbeddingSummaryRead(BaseModel):
    source_id: int
    model_code: str
    total_chunks: int
    embedded_count: int
    skipped_count: int
    failed_count: int


def build_rag_embedding_read(embedding: Any, *, include_vector: bool = False) -> RagEmbeddingRead:
    return RagEmbeddingRead(
        id=embedding.id,
        chunk_id=embedding.chunk_id,
        source_id=embedding.source_id,
        profile_id=embedding.profile_id,
        owner_user_id=embedding.owner_user_id,
        model_code=embedding.model_code,
        vector_dimension=embedding.vector_dimension,
        status=embedding.status,
        error_message=embedding.error_message,
        embedding_metadata=embedding.embedding_metadata,
        created_at=embedding.created_at,
        updated_at=embedding.updated_at,
        vector=embedding.vector if include_vector else None,
    )

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class RagSourceEmbeddingIndexRequest(BaseModel):
    model_code: str | None = Field(default=None, max_length=64)

    @field_validator("model_code")
    @classmethod
    def normalize_model_code(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip().lower()
        return normalized_value or None


class RagVectorIndexRead(BaseModel):
    id: int
    owner_user_id: int
    profile_id: int
    source_id: int
    chunk_id: int
    embedding_id: int
    model_code: str
    qdrant_collection: str
    qdrant_point_id: str
    status: str
    error_message: str | None
    indexed_at: datetime | None
    created_at: datetime
    updated_at: datetime


class RagSourceIndexingSummaryRead(BaseModel):
    source_id: int
    model_code: str | None
    total_embeddings: int
    indexed_count: int
    skipped_count: int
    failed_count: int


def build_rag_vector_index_read(vector_index) -> RagVectorIndexRead:
    return RagVectorIndexRead(
        id=vector_index.id,
        owner_user_id=vector_index.owner_user_id,
        profile_id=vector_index.profile_id,
        source_id=vector_index.source_id,
        chunk_id=vector_index.chunk_id,
        embedding_id=vector_index.embedding_id,
        model_code=vector_index.model_code,
        qdrant_collection=vector_index.qdrant_collection,
        qdrant_point_id=vector_index.qdrant_point_id,
        status=vector_index.status,
        error_message=vector_index.error_message,
        indexed_at=vector_index.indexed_at,
        created_at=vector_index.created_at,
        updated_at=vector_index.updated_at,
    )

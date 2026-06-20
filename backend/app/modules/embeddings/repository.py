from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import MemoryProfile, RagChunk, RagEmbedding, RagSource


def create_rag_embedding(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
    source_id: int,
    chunk_id: int,
    model_code: str,
    vector,
    vector_dimension: int,
    text_hash: str,
    status: str,
    error_message: str | None,
    embedding_metadata,
) -> RagEmbedding:
    rag_embedding = RagEmbedding(
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        source_id=source_id,
        chunk_id=chunk_id,
        model_code=model_code,
        vector=vector,
        vector_dimension=vector_dimension,
        text_hash=text_hash,
        status=status,
        error_message=error_message,
        embedding_metadata=embedding_metadata,
    )
    db.add(rag_embedding)
    return rag_embedding


def get_embedding_for_chunk_and_model(
    db: Session,
    *,
    chunk_id: int,
    model_code: str,
) -> RagEmbedding | None:
    statement = select(RagEmbedding).where(
        RagEmbedding.chunk_id == chunk_id,
        RagEmbedding.model_code == model_code,
    )
    return db.scalar(statement)


def list_embeddings_for_chunk_for_user(
    db: Session,
    *,
    owner_user_id: int,
    chunk_id: int,
) -> list[RagEmbedding]:
    statement = (
        select(RagEmbedding)
        .join(RagChunk, RagEmbedding.chunk_id == RagChunk.id)
        .join(RagSource, RagEmbedding.source_id == RagSource.id)
        .join(MemoryProfile, RagEmbedding.profile_id == MemoryProfile.id)
        .where(
            RagEmbedding.chunk_id == chunk_id,
            RagEmbedding.owner_user_id == owner_user_id,
            RagChunk.owner_user_id == owner_user_id,
            RagSource.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
        .order_by(RagEmbedding.model_code.asc(), RagEmbedding.updated_at.desc(), RagEmbedding.id.desc())
    )
    return list(db.scalars(statement))


def get_embedding_for_user(
    db: Session,
    *,
    owner_user_id: int,
    embedding_id: int,
) -> RagEmbedding | None:
    statement = (
        select(RagEmbedding)
        .join(RagChunk, RagEmbedding.chunk_id == RagChunk.id)
        .join(RagSource, RagEmbedding.source_id == RagSource.id)
        .join(MemoryProfile, RagEmbedding.profile_id == MemoryProfile.id)
        .where(
            RagEmbedding.id == embedding_id,
            RagEmbedding.owner_user_id == owner_user_id,
            RagChunk.owner_user_id == owner_user_id,
            RagSource.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
    )
    return db.scalar(statement)

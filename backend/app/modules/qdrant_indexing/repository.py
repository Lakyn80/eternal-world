from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.db.models import MemoryProfile, RagChunk, RagEmbedding, RagSource, RagVectorIndex


def create_rag_vector_index(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
    source_id: int,
    chunk_id: int,
    embedding_id: int,
    model_code: str,
    qdrant_collection: str,
    qdrant_point_id: str,
    status: str,
    error_message: str | None,
    indexed_at,
) -> RagVectorIndex:
    rag_vector_index = RagVectorIndex(
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        source_id=source_id,
        chunk_id=chunk_id,
        embedding_id=embedding_id,
        model_code=model_code,
        qdrant_collection=qdrant_collection,
        qdrant_point_id=qdrant_point_id,
        status=status,
        error_message=error_message,
        indexed_at=indexed_at,
    )
    db.add(rag_vector_index)
    return rag_vector_index


def get_embedding_for_indexing_for_user(
    db: Session,
    *,
    owner_user_id: int,
    embedding_id: int,
) -> RagEmbedding | None:
    statement = (
        select(RagEmbedding)
        .options(
            selectinload(RagEmbedding.chunk),
            selectinload(RagEmbedding.source),
        )
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


def list_source_embeddings_for_user(
    db: Session,
    *,
    owner_user_id: int,
    source_id: int,
    model_code: str | None = None,
) -> list[RagEmbedding]:
    statement = (
        select(RagEmbedding)
        .options(
            selectinload(RagEmbedding.chunk),
            selectinload(RagEmbedding.source),
        )
        .join(RagChunk, RagEmbedding.chunk_id == RagChunk.id)
        .join(RagSource, RagEmbedding.source_id == RagSource.id)
        .join(MemoryProfile, RagEmbedding.profile_id == MemoryProfile.id)
        .where(
            RagEmbedding.source_id == source_id,
            RagEmbedding.owner_user_id == owner_user_id,
            RagChunk.owner_user_id == owner_user_id,
            RagSource.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
        .order_by(RagEmbedding.model_code.asc(), RagEmbedding.chunk_id.asc(), RagEmbedding.id.asc())
    )
    if model_code is not None:
        statement = statement.where(RagEmbedding.model_code == model_code)

    return list(db.scalars(statement))


def get_vector_index_for_embedding_and_collection(
    db: Session,
    *,
    embedding_id: int,
    qdrant_collection: str,
) -> RagVectorIndex | None:
    statement = select(RagVectorIndex).where(
        RagVectorIndex.embedding_id == embedding_id,
        RagVectorIndex.qdrant_collection == qdrant_collection,
    )
    return db.scalar(statement)


def get_vector_index_for_user_by_embedding(
    db: Session,
    *,
    owner_user_id: int,
    embedding_id: int,
) -> RagVectorIndex | None:
    statement = (
        select(RagVectorIndex)
        .join(RagEmbedding, RagVectorIndex.embedding_id == RagEmbedding.id)
        .join(RagChunk, RagVectorIndex.chunk_id == RagChunk.id)
        .join(RagSource, RagVectorIndex.source_id == RagSource.id)
        .join(MemoryProfile, RagVectorIndex.profile_id == MemoryProfile.id)
        .where(
            RagVectorIndex.embedding_id == embedding_id,
            RagVectorIndex.owner_user_id == owner_user_id,
            RagEmbedding.owner_user_id == owner_user_id,
            RagChunk.owner_user_id == owner_user_id,
            RagSource.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
        .order_by(RagVectorIndex.updated_at.desc(), RagVectorIndex.id.desc())
    )
    return db.scalar(statement)


def list_vector_indexes_for_profile(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
) -> list[RagVectorIndex]:
    """All currently-indexed Qdrant points for a profile, regardless of origin
    (biography ingestion or promoted memory candidates) - the authoritative
    set that must be removed from Qdrant before the profile itself can be
    safely deleted (Task 65.5)."""

    statement = (
        select(RagVectorIndex)
        .join(MemoryProfile, RagVectorIndex.profile_id == MemoryProfile.id)
        .where(
            RagVectorIndex.profile_id == profile_id,
            RagVectorIndex.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
        .order_by(RagVectorIndex.id.asc())
    )
    return list(db.scalars(statement))

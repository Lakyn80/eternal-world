from __future__ import annotations

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.db.models import MemoryProfile, RagChunk, RagSource


def create_rag_chunk(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
    source_id: int,
    chunk_index: int,
    chunk_text: str,
    text_hash: str,
    token_estimate: int,
    char_count: int,
    sentence_count: int,
    language: str | None,
    chunk_metadata,
    validation_status: str,
    validation_errors,
) -> RagChunk:
    rag_chunk = RagChunk(
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        source_id=source_id,
        chunk_index=chunk_index,
        chunk_text=chunk_text,
        text_hash=text_hash,
        token_estimate=token_estimate,
        char_count=char_count,
        sentence_count=sentence_count,
        language=language,
        chunk_metadata=chunk_metadata,
        validation_status=validation_status,
        validation_errors=validation_errors,
    )
    db.add(rag_chunk)
    return rag_chunk


def delete_chunks_for_source(db: Session, *, source_id: int) -> None:
    db.execute(delete(RagChunk).where(RagChunk.source_id == source_id))


def list_chunks_for_source(
    db: Session,
    *,
    owner_user_id: int,
    source_id: int,
) -> list[RagChunk]:
    statement = (
        select(RagChunk)
        .join(RagSource, RagChunk.source_id == RagSource.id)
        .join(MemoryProfile, RagChunk.profile_id == MemoryProfile.id)
        .where(
            RagChunk.source_id == source_id,
            RagChunk.owner_user_id == owner_user_id,
            RagSource.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
        .order_by(RagChunk.chunk_index.asc(), RagChunk.id.asc())
    )
    return list(db.scalars(statement))


def get_chunk_for_user(
    db: Session,
    *,
    owner_user_id: int,
    chunk_id: int,
) -> RagChunk | None:
    statement = (
        select(RagChunk)
        .join(RagSource, RagChunk.source_id == RagSource.id)
        .join(MemoryProfile, RagChunk.profile_id == MemoryProfile.id)
        .where(
            RagChunk.id == chunk_id,
            RagChunk.owner_user_id == owner_user_id,
            RagSource.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
    )
    return db.scalar(statement)

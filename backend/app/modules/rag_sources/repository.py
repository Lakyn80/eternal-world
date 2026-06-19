from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import MemoryProfile, RagSource


def create_rag_source(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
    source_type: str,
    title: str,
    raw_text: str,
    normalized_text: str | None,
    language: str | None,
    status: str,
    processing_error: str | None,
    source_metadata,
) -> RagSource:
    rag_source = RagSource(
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        source_type=source_type,
        title=title,
        raw_text=raw_text,
        normalized_text=normalized_text,
        language=language,
        status=status,
        processing_error=processing_error,
        source_metadata=source_metadata,
    )
    db.add(rag_source)
    return rag_source


def list_rag_sources_for_profile(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
) -> list[RagSource]:
    statement = (
        select(RagSource)
        .where(
            RagSource.owner_user_id == owner_user_id,
            RagSource.profile_id == profile_id,
        )
        .order_by(RagSource.created_at.desc(), RagSource.id.desc())
    )
    return list(db.scalars(statement))


def get_rag_source_for_user(
    db: Session,
    *,
    owner_user_id: int,
    source_id: int,
) -> RagSource | None:
    statement = (
        select(RagSource)
        .join(MemoryProfile, RagSource.profile_id == MemoryProfile.id)
        .where(
            RagSource.id == source_id,
            RagSource.owner_user_id == owner_user_id,
            MemoryProfile.user_id == owner_user_id,
        )
    )
    return db.scalar(statement)

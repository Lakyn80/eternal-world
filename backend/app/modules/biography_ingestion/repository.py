from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import BackgroundJob, MemoryProfile, RagSource, RagVectorIndex


def get_profile_for_update(db: Session, *, profile_id: int) -> MemoryProfile | None:
    return db.scalar(
        select(MemoryProfile).where(MemoryProfile.id == profile_id).with_for_update()
    )


def get_source_by_id(db: Session, *, source_id: int) -> RagSource | None:
    return db.get(RagSource, source_id)


def get_reusable_biography_source(
    db: Session,
    *,
    profile_id: int,
    content_hash: str,
) -> RagSource | None:
    """A biography source is reusable on retry only if it belongs to this
    profile, is the biography source_type, and its recorded content hash
    (stored in source_metadata) matches the profile's current biography text
    - i.e. the same ingestion attempt retrying after a transient failure,
    never a stale source from a previously-edited biography."""

    statement = (
        select(RagSource)
        .where(
            RagSource.profile_id == profile_id,
            RagSource.source_type == "biography",
        )
        .order_by(RagSource.id.desc())
    )
    for source in db.scalars(statement):
        metadata = source.source_metadata or {}
        if metadata.get("content_hash") == content_hash:
            return source
    return None


def list_vector_indexes_for_source(db: Session, *, source_id: int) -> list[RagVectorIndex]:
    statement = select(RagVectorIndex).where(RagVectorIndex.source_id == source_id)
    return list(db.scalars(statement))


def get_latest_biography_job(db: Session, *, profile_id: int) -> BackgroundJob | None:
    statement = (
        select(BackgroundJob)
        .where(
            BackgroundJob.profile_id == profile_id,
            BackgroundJob.job_type == "qdrant_indexing",
        )
        .order_by(BackgroundJob.id.desc())
    )
    for job in db.scalars(statement):
        if (job.input_payload or {}).get("workflow") == "biography_indexing":
            return job
    return None

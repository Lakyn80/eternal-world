from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import JobOutboxEvent


def create_outbox_event(
    db: Session,
    *,
    job_id: int,
    task_name: str,
    queue: str,
    task_args: dict[str, object],
) -> JobOutboxEvent:
    outbox_event = JobOutboxEvent(
        job_id=job_id,
        task_name=task_name,
        queue=queue,
        task_args=task_args,
        status="pending",
        attempts=0,
    )
    db.add(outbox_event)
    db.flush()
    return outbox_event


def get_outbox_event_for_job(db: Session, *, job_id: int) -> JobOutboxEvent | None:
    statement = select(JobOutboxEvent).where(JobOutboxEvent.job_id == job_id)
    return db.scalar(statement)


def reset_to_pending(db: Session, *, job_id: int) -> JobOutboxEvent | None:
    """Task 65.9 (Part E/M/P) - re-arm the existing outbox row for a
    redispatch (self-healing recovery or stale-job recovery) instead of
    creating a second row for the same job. Idempotent: safe to call even
    if the row is already `pending`."""

    outbox_event = get_outbox_event_for_job(db, job_id=job_id)
    if outbox_event is None:
        return None
    outbox_event.status = "pending"
    outbox_event.next_attempt_at = None
    outbox_event.published_at = None
    db.flush()
    return outbox_event


def list_pending_outbox_events(
    db: Session,
    *,
    limit: int,
    now: datetime | None = None,
) -> list[JobOutboxEvent]:
    """Task 65.9 (Part E) - the dispatcher's scan. Row-locked
    (`with_for_update`) so multiple concurrent dispatcher replicas never
    both attempt to publish the same row (Part E.7: "multiple dispatcher
    replicas remain safe"). SQLite (used by the unit-test suite) does not
    support `SELECT ... FOR UPDATE`; SQLAlchemy's SQLite dialect silently
    omits the clause there, matching the exact convention already used
    throughout this codebase (e.g. `avatar_memory_indexing.service.
    index_promotion`)."""

    current_time = now or datetime.now(timezone.utc)
    statement = (
        select(JobOutboxEvent)
        .where(
            JobOutboxEvent.status == "pending",
            (JobOutboxEvent.next_attempt_at.is_(None)) | (JobOutboxEvent.next_attempt_at <= current_time),
        )
        .order_by(JobOutboxEvent.created_at.asc())
        .limit(limit)
        .with_for_update()
    )
    return list(db.scalars(statement))


def mark_published(db: Session, *, outbox_event: JobOutboxEvent) -> None:
    outbox_event.status = "published"
    outbox_event.published_at = datetime.now(timezone.utc)
    outbox_event.attempts += 1
    db.flush()


def mark_publish_failed(
    db: Session,
    *,
    outbox_event: JobOutboxEvent,
    error_class_name: str,
    next_attempt_at: datetime,
) -> None:
    outbox_event.attempts += 1
    #: Safe: exception *class name* only, never the exception message or
    #: any user content (Part L: no raw exception text through any
    #: surface, including internal-only ones - kept safe uniformly).
    outbox_event.last_error = error_class_name[:255]
    outbox_event.next_attempt_at = next_attempt_at
    db.flush()

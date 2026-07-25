from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.models import BackgroundJob
from app.modules.job_tracking.enums import ACTIVE_BACKGROUND_JOB_STATUSES


def create_background_job(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None,
    job_type: str,
    status: str,
    progress_current: int,
    progress_total: int,
    celery_task_id: str | None,
    input_payload,
    result_payload,
    error_payload,
    event_log,
    error_message: str | None,
    started_at,
    finished_at,
    queue: str | None = None,
    idempotency_key: str | None = None,
    priority: int = 0,
    max_attempts: int = 3,
    queued_at: datetime | None = None,
) -> BackgroundJob:
    background_job = BackgroundJob(
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        job_type=job_type,
        status=status,
        progress_current=progress_current,
        progress_total=progress_total,
        celery_task_id=celery_task_id,
        input_payload=input_payload,
        result_payload=result_payload,
        error_payload=error_payload,
        event_log=event_log if event_log is not None else [],
        error_message=error_message,
        started_at=started_at,
        finished_at=finished_at,
        queue=queue,
        idempotency_key=idempotency_key,
        priority=priority,
        max_attempts=max_attempts,
        queued_at=queued_at,
    )
    db.add(background_job)
    return background_job


def get_background_job_for_user(
    db: Session,
    *,
    owner_user_id: int,
    job_id: int,
) -> BackgroundJob | None:
    statement = select(BackgroundJob).where(
        BackgroundJob.id == job_id,
        BackgroundJob.owner_user_id == owner_user_id,
    )
    return db.scalar(statement)


def get_background_job_by_id(
    db: Session,
    *,
    job_id: int,
) -> BackgroundJob | None:
    statement = select(BackgroundJob).where(BackgroundJob.id == job_id)
    return db.scalar(statement)


def list_background_jobs_for_user(
    db: Session,
    *,
    owner_user_id: int,
) -> list[BackgroundJob]:
    statement = (
        select(BackgroundJob)
        .where(BackgroundJob.owner_user_id == owner_user_id)
        .order_by(BackgroundJob.created_at.desc(), BackgroundJob.id.desc())
    )
    return list(db.scalars(statement))


def get_active_background_job_by_idempotency_key(
    db: Session,
    *,
    idempotency_key: str,
) -> BackgroundJob | None:
    """Task 65.9 (Part F) - the lookup every idempotent enqueue path uses
    before creating a new job: if a still-*active* job already exists for
    this exact semantic key, callers reuse it instead of creating a
    duplicate. Deliberately excludes terminal jobs (succeeded/failed/
    cancelled) - a *new* real attempt (e.g. retry after a previous
    permanent failure) must be able to create a fresh job even though the
    semantic key is unchanged; see the partial unique index on this same
    column for why that is safe at the DB level. Combined with that
    index, this also makes duplicate-create races safe - the loser of a
    concurrent insert gets an IntegrityError, re-queries, and finds the
    winner's row here."""

    statement = (
        select(BackgroundJob)
        .where(
            BackgroundJob.idempotency_key == idempotency_key,
            BackgroundJob.status.in_(ACTIVE_BACKGROUND_JOB_STATUSES),
        )
        .order_by(BackgroundJob.id.desc())
    )
    return db.scalar(statement)


def count_active_heavy_jobs_for_user(db: Session, *, owner_user_id: int) -> int:
    statement = select(func.count(BackgroundJob.id)).where(
        BackgroundJob.owner_user_id == owner_user_id,
        BackgroundJob.status.in_(ACTIVE_BACKGROUND_JOB_STATUSES),
        BackgroundJob.queue == "embedding",
    )
    return int(db.scalar(statement) or 0)


def count_active_heavy_jobs_for_profile(db: Session, *, profile_id: int) -> int:
    statement = select(func.count(BackgroundJob.id)).where(
        BackgroundJob.profile_id == profile_id,
        BackgroundJob.status.in_(ACTIVE_BACKGROUND_JOB_STATUSES),
        BackgroundJob.queue == "embedding",
    )
    return int(db.scalar(statement) or 0)


def count_active_heavy_jobs_global(db: Session) -> int:
    statement = select(func.count(BackgroundJob.id)).where(
        BackgroundJob.status.in_(ACTIVE_BACKGROUND_JOB_STATUSES),
        BackgroundJob.queue == "embedding",
    )
    return int(db.scalar(statement) or 0)


def get_active_job_counts_by_queue(db: Session) -> dict[str, int]:
    """Task 65.9.1 (Part H) - active (non-terminal) job counts grouped by
    queue, straight from PostgreSQL (the authoritative source, never a
    broker-internal queue-length call). A queue with zero active jobs is
    simply absent from this dict - the caller (Part H.5) is responsible for
    explicitly zeroing every known queue, not just the ones returned here,
    so a queue that just drained does not keep reporting its last nonzero
    depth forever."""

    statement = (
        select(BackgroundJob.queue, func.count(BackgroundJob.id))
        .where(
            BackgroundJob.status.in_(ACTIVE_BACKGROUND_JOB_STATUSES),
            BackgroundJob.queue.is_not(None),
        )
        .group_by(BackgroundJob.queue)
    )
    return {queue: int(count) for queue, count in db.execute(statement).all()}


def get_oldest_active_job_created_at_by_queue(db: Session) -> dict[str, datetime]:
    """Task 65.9.1 (Part H) - oldest `created_at` among active jobs, grouped
    by queue. Callers convert this to an age-in-seconds gauge relative to
    "now" at read time; a queue absent from this dict has no active jobs."""

    statement = (
        select(BackgroundJob.queue, func.min(BackgroundJob.created_at))
        .where(
            BackgroundJob.status.in_(ACTIVE_BACKGROUND_JOB_STATUSES),
            BackgroundJob.queue.is_not(None),
        )
        .group_by(BackgroundJob.queue)
    )
    result: dict[str, datetime] = {}
    for queue, oldest_created_at in db.execute(statement).all():
        if oldest_created_at is None:
            continue
        if oldest_created_at.tzinfo is None:
            oldest_created_at = oldest_created_at.replace(tzinfo=timezone.utc)
        result[queue] = oldest_created_at
    return result


def list_stale_processing_jobs(
    db: Session,
    *,
    stale_before: datetime,
    limit: int = 100,
) -> list[BackgroundJob]:
    """Task 65.9 (Part P) - jobs that are still marked `running` or
    `recovery_pending` but whose heartbeat has not been refreshed since
    `stale_before`. A job that never received a single heartbeat (e.g. it
    crashed between `mark_running` and the first heartbeat touch) is
    matched via `started_at` instead so it is not invisible to recovery."""

    statement = (
        select(BackgroundJob)
        .where(
            BackgroundJob.status.in_(("running", "recovery_pending")),
            (
                (BackgroundJob.heartbeat_at.is_not(None) & (BackgroundJob.heartbeat_at < stale_before))
                | (
                    BackgroundJob.heartbeat_at.is_(None)
                    & BackgroundJob.started_at.is_not(None)
                    & (BackgroundJob.started_at < stale_before)
                )
            ),
        )
        .order_by(BackgroundJob.id.asc())
        .limit(limit)
    )
    return list(db.scalars(statement))


def list_system_milestone_jobs_for_owner(
    db: Session,
    *,
    owner_user_id: int,
) -> list[BackgroundJob]:
    statement = (
        select(BackgroundJob)
        .where(
            BackgroundJob.owner_user_id == owner_user_id,
            BackgroundJob.job_type == "system_milestone",
        )
        .order_by(BackgroundJob.id.asc())
    )
    return list(db.scalars(statement))

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.metrics import (
    observe_async_job_completed,
    observe_async_job_created,
    observe_async_job_failed,
    observe_async_job_stale_recovered,
)
from app.db.models import BackgroundJob, User
from app.modules.job_tracking import repository
from app.modules.job_tracking.enums import BackgroundJobStatus, BackgroundJobType, SafeErrorCategory
from app.modules.job_tracking.exceptions import (
    BackgroundJobNotFoundError,
    BackgroundJobProfileNotFoundError,
    GlobalQueueSaturationError,
    PerProfileActiveJobLimitExceededError,
    PerUserActiveJobLimitExceededError,
)
from app.modules.job_tracking.schemas import BackgroundJobBackfillSummaryRead
from app.modules.memory_profiles import repository as memory_profiles_repository


@dataclass(frozen=True)
class KnownMilestoneBackfill:
    task_number: int
    task_title: str
    commit_hash: str


KNOWN_MILESTONE_BACKFILLS: tuple[KnownMilestoneBackfill, ...] = (
    KnownMilestoneBackfill(
        task_number=18,
        task_title="Qdrant Indexing Foundation",
        commit_hash="a44be88",
    ),
    KnownMilestoneBackfill(
        task_number=19,
        task_title="Hybrid Retrieval Foundation",
        commit_hash="b46e39c",
    ),
)


def _validate_owned_profile(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None,
) -> None:
    if profile_id is None:
        return

    profile = memory_profiles_repository.get_memory_profile_for_user(
        db,
        user_id=owner_user_id,
        profile_id=profile_id,
    )
    if profile is None:
        raise BackgroundJobProfileNotFoundError("Memory profile not found")


def _enforce_heavy_job_backpressure(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None,
) -> None:
    """Task 65.9 (Part Q). All counts are read straight from PostgreSQL -
    the single shared source of truth every API replica queries - never an
    in-process counter, so the limit holds identically regardless of how
    many API/worker replicas are running."""

    user_active_count = repository.count_active_heavy_jobs_for_user(db, owner_user_id=owner_user_id)
    if user_active_count >= settings.max_active_heavy_jobs_per_user:
        raise PerUserActiveJobLimitExceededError(
            limit=settings.max_active_heavy_jobs_per_user,
            current=user_active_count,
        )

    if profile_id is not None:
        profile_active_count = repository.count_active_heavy_jobs_for_profile(db, profile_id=profile_id)
        if profile_active_count >= settings.max_active_heavy_jobs_per_profile:
            raise PerProfileActiveJobLimitExceededError(
                limit=settings.max_active_heavy_jobs_per_profile,
                current=profile_active_count,
            )

    global_active_count = repository.count_active_heavy_jobs_global(db)
    if global_active_count >= settings.global_heavy_job_saturation_limit:
        raise GlobalQueueSaturationError(
            limit=settings.global_heavy_job_saturation_limit,
            current=global_active_count,
            retry_after_seconds=settings.global_saturation_retry_after_seconds,
        )


def create_job(
    db: Session,
    *,
    owner_user_id: int,
    job_type: BackgroundJobType | str,
    profile_id: int | None = None,
    input_payload: dict[str, object] | None = None,
    progress_current: int = 0,
    progress_total: int = 0,
    queue: str | None = None,
    idempotency_key: str | None = None,
    priority: int = 0,
    max_attempts: int = 3,
) -> BackgroundJob:
    """Create a new background job, or (Task 65.9, Part F) transparently
    reuse an existing one when `idempotency_key` is given and a job with
    that exact semantic key already exists - repeated approval clicks,
    duplicate broker delivery, and a manual retry click all converge on
    the same row rather than creating a duplicate active job.

    When `idempotency_key` is provided and `queue == "embedding"`, this is
    a heavy job and is subject to the backpressure limits in Part Q
    (raises `PerUserActiveJobLimitExceededError` /
    `PerProfileActiveJobLimitExceededError` / `GlobalQueueSaturationError`,
    mapped to 429/429/503 at the API layer). Legacy callers that never
    pass `idempotency_key` (e.g. the harmless smoke-test job) are entirely
    unaffected - this is purely additive/opt-in.
    """

    _validate_owned_profile(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
    )

    if idempotency_key is not None:
        existing = repository.get_active_background_job_by_idempotency_key(db, idempotency_key=idempotency_key)
        if existing is not None:
            return existing
        if queue == "embedding":
            _enforce_heavy_job_backpressure(db, owner_user_id=owner_user_id, profile_id=profile_id)

    initial_status = (
        BackgroundJobStatus.PENDING.value if idempotency_key is not None else BackgroundJobStatus.QUEUED.value
    )
    background_job = repository.create_background_job(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        job_type=str(job_type.value if isinstance(job_type, BackgroundJobType) else job_type),
        status=initial_status,
        progress_current=progress_current,
        progress_total=progress_total,
        celery_task_id=None,
        input_payload=input_payload or {},
        result_payload=None,
        error_payload=None,
        event_log=[],
        error_message=None,
        started_at=None,
        finished_at=None,
        queue=queue,
        idempotency_key=idempotency_key,
        priority=priority,
        max_attempts=max_attempts,
        queued_at=datetime.now(timezone.utc) if idempotency_key is None else None,
    )
    try:
        db.commit()
    except IntegrityError:
        # Lost a concurrent create race on the unique idempotency-key index
        # (Part F: duplicate delivery must converge, never error) - the
        # winner's row already exists; return it instead of raising.
        db.rollback()
        if idempotency_key is not None:
            existing = repository.get_active_background_job_by_idempotency_key(db, idempotency_key=idempotency_key)
            if existing is not None:
                return existing
        raise
    db.refresh(background_job)
    observe_async_job_created(queue=background_job.queue, job_type=background_job.job_type)
    return background_job


def attach_celery_task_id(
    db: Session,
    *,
    job_id: int,
    celery_task_id: str | None,
) -> BackgroundJob:
    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    background_job.celery_task_id = celery_task_id
    db.commit()
    db.refresh(background_job)
    return background_job


def mark_running(
    db: Session,
    *,
    job_id: int,
    celery_task_id: str | None = None,
) -> BackgroundJob:
    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    background_job.status = BackgroundJobStatus.RUNNING.value
    background_job.started_at = background_job.started_at or datetime.now(timezone.utc)
    if celery_task_id is not None:
        background_job.celery_task_id = celery_task_id
    db.commit()
    db.refresh(background_job)
    return background_job


def update_progress(
    db: Session,
    *,
    job_id: int,
    progress_current: int,
    progress_total: int,
) -> BackgroundJob:
    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    background_job.progress_current = progress_current
    background_job.progress_total = progress_total
    db.commit()
    db.refresh(background_job)
    return background_job


def append_job_event(
    db: Session,
    *,
    job_id: int,
    stage: str,
    status: str,
    details: dict[str, object] | None = None,
) -> BackgroundJob:
    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    event_entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "stage": stage,
        "status": status,
        "details": details or {},
    }
    current_event_log = list(background_job.event_log or [])
    current_event_log.append(event_entry)
    background_job.event_log = current_event_log
    db.commit()
    db.refresh(background_job)
    return background_job


def mark_succeeded(
    db: Session,
    *,
    job_id: int,
    result_payload: dict[str, object] | None = None,
) -> BackgroundJob:
    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    background_job.status = BackgroundJobStatus.SUCCEEDED.value
    background_job.result_payload = result_payload
    background_job.error_payload = None
    background_job.error_message = None
    background_job.finished_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(background_job)
    duration_seconds = (
        (background_job.finished_at - background_job.started_at).total_seconds()
        if background_job.started_at is not None
        else 0.0
    )
    observe_async_job_completed(
        queue=background_job.queue,
        job_type=background_job.job_type,
        duration_seconds=duration_seconds,
    )
    return background_job


def mark_failed(
    db: Session,
    *,
    job_id: int,
    error_message: str,
    error_payload: dict[str, object] | None = None,
    safe_error_category: SafeErrorCategory | str | None = None,
) -> BackgroundJob:
    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    background_job.status = BackgroundJobStatus.FAILED.value
    background_job.error_message = error_message
    background_job.error_payload = error_payload
    if safe_error_category is not None:
        background_job.safe_error_category = (
            safe_error_category.value
            if isinstance(safe_error_category, SafeErrorCategory)
            else str(safe_error_category)
        )
    background_job.finished_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(background_job)
    duration_seconds = (
        (background_job.finished_at - background_job.started_at).total_seconds()
        if background_job.started_at is not None
        else 0.0
    )
    observe_async_job_failed(
        queue=background_job.queue,
        job_type=background_job.job_type,
        safe_error_category=background_job.safe_error_category,
        duration_seconds=duration_seconds,
    )
    return background_job


def touch_heartbeat(db: Session, *, job_id: int) -> None:
    """Task 65.9 (Part P) - called by a worker while actively processing a
    job so stale-job recovery can distinguish "still being worked on" from
    "worker crashed". Best-effort: a missing job is not an error here (the
    same defensive convention as the existing Celery task bodies for a job
    row that does not exist in an isolated test database)."""

    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        return
    background_job.heartbeat_at = datetime.now(timezone.utc)
    db.commit()


def record_provider_recovery_attempt(db: Session, *, job_id: int) -> BackgroundJob | None:
    """Task 65.9 (Part M) - increments the persistent provider-recovery
    counter for this job. Must be called exactly once per provider-
    corruption attempt, regardless of which worker process observes it -
    the counter (not the calling process's own memory) is the bound."""

    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        return None
    background_job.provider_recovery_count += 1
    background_job.attempt_count += 1
    db.commit()
    db.refresh(background_job)
    return background_job


def request_fresh_process_retry(db: Session, *, job_id: int) -> bool:
    """Task 65.9 (Part M/N) - persist that this job has now exhausted its
    in-process reload-and-retry attempt and requires exactly one fresh
    embedding-worker process. Idempotent/guarded: returns False (no-op) if
    already requested, so a duplicate task delivery, or the exact same
    corruption observed twice under a race, can never request a second
    automatic worker recycle for the same job (Part AA test 33)."""

    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        return False
    if background_job.fresh_process_retry_used:
        return False
    background_job.fresh_process_retry_used = True
    background_job.worker_recycle_requested = True
    background_job.status = BackgroundJobStatus.RECOVERY_PENDING.value
    background_job.safe_error_category = SafeErrorCategory.PROVIDER_CORRUPT.value
    db.commit()
    return True


def record_permanent_provider_failure(db: Session, *, job_id: int) -> BackgroundJob | None:
    """Task 65.9 (Part M) - attempt 3 (the one fresh-process retry) also
    failed with provider corruption: mark the job permanently failed with
    a safe category, without requesting any further recycle. Manual retry
    (re-running the same idempotent indexing operation) remains possible
    afterwards - this only marks the *job*, never the promotion/candidate
    domain row, which is a separate, caller-owned concern."""

    return mark_failed(
        db,
        job_id=job_id,
        error_message="Embedding provider recovery failed after the bounded retry policy",
        error_payload={"code": "provider_recovery_exhausted"},
        safe_error_category=SafeErrorCategory.PROVIDER_CORRUPT,
    )


def requeue_stale_job(
    db: Session,
    *,
    job_id: int,
) -> bool:
    """Task 65.9 (Part P) - maintenance recovery for a job whose worker
    appears to have crashed (heartbeat/started_at older than the
    configured stale threshold). Enforces the attempt-limit: a job that
    has already exhausted `max_attempts` is marked permanently failed
    (`worker_lost`) instead of being requeued forever. Safe to call from
    multiple concurrent maintenance workers - a job that is no longer in a
    stale-eligible state (already recovered/completed by another sweep) is
    simply skipped."""

    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        return False
    if background_job.status not in ("running", "recovery_pending"):
        # Already recovered by a concurrent maintenance sweep, or the
        # worker actually finished between the staleness scan and now -
        # never resurrect a job that is no longer stale (Part AA test 45).
        return False

    if background_job.attempt_count >= background_job.max_attempts:
        background_job.status = BackgroundJobStatus.FAILED.value
        background_job.safe_error_category = SafeErrorCategory.WORKER_LOST.value
        background_job.error_message = "Worker lost and attempt limit reached"
        background_job.finished_at = datetime.now(timezone.utc)
        db.commit()
        return False

    background_job.status = BackgroundJobStatus.RETRY_SCHEDULED.value
    background_job.attempt_count += 1
    background_job.heartbeat_at = None
    background_job.next_attempt_at = datetime.now(timezone.utc) + timedelta(seconds=5)
    if background_job.safe_error_category is None:
        background_job.safe_error_category = SafeErrorCategory.WORKER_LOST.value
    db.commit()
    observe_async_job_stale_recovered(queue=background_job.queue)
    return True


@dataclass(frozen=True)
class StaleJobRecoverySummary:
    scanned: int
    requeued: int
    permanently_failed: int


def find_stale_job_ids(db: Session, *, limit: int = 100) -> list[int]:
    stale_before = datetime.now(timezone.utc) - timedelta(seconds=settings.job_stale_heartbeat_timeout_seconds)
    stale_jobs = repository.list_stale_processing_jobs(db, stale_before=stale_before, limit=limit)
    return [job.id for job in stale_jobs]


def get_user_job(
    db: Session,
    *,
    current_user: User,
    job_id: int,
) -> BackgroundJob:
    background_job = repository.get_background_job_for_user(
        db,
        owner_user_id=current_user.id,
        job_id=job_id,
    )
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    return background_job


def list_user_jobs(
    db: Session,
    *,
    current_user: User,
) -> list[BackgroundJob]:
    return repository.list_background_jobs_for_user(
        db,
        owner_user_id=current_user.id,
    )


def enqueue_smoke_test_job(
    db: Session,
    *,
    current_user: User,
    profile_id: int | None = None,
) -> BackgroundJob:
    background_job = create_job(
        db,
        owner_user_id=current_user.id,
        profile_id=profile_id,
        job_type=BackgroundJobType.SMOKE_TEST,
        input_payload={
            "source": "api_smoke_test",
            "note": "Harmless Celery smoke test job",
        },
    )

    from app.worker.tasks import run_job_smoke_test

    async_result = run_job_smoke_test.delay(background_job.id)
    return attach_celery_task_id(
        db,
        job_id=background_job.id,
        celery_task_id=async_result.id,
    )


def backfill_known_milestones(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None = None,
) -> BackgroundJobBackfillSummaryRead:
    _validate_owned_profile(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
    )
    existing_jobs = repository.list_system_milestone_jobs_for_owner(
        db,
        owner_user_id=owner_user_id,
    )
    existing_keys = {
        (
            (job.input_payload or {}).get("task_number"),
            (job.input_payload or {}).get("commit_hash"),
        )
        for job in existing_jobs
    }

    created_job_ids: list[int] = []
    skipped_count = 0

    for milestone in KNOWN_MILESTONE_BACKFILLS:
        milestone_key = (milestone.task_number, milestone.commit_hash)
        if milestone_key in existing_keys:
            skipped_count += 1
            continue

        background_job = repository.create_background_job(
            db,
            owner_user_id=owner_user_id,
            profile_id=profile_id,
            job_type=BackgroundJobType.SYSTEM_MILESTONE.value,
            status=BackgroundJobStatus.SUCCEEDED.value,
            progress_current=0,
            progress_total=0,
            celery_task_id=None,
            input_payload={
                "task_number": milestone.task_number,
                "task_title": milestone.task_title,
                "commit_hash": milestone.commit_hash,
                "source": "PROJECT_PROGRESS.md / manual backfill",
                "note": "Runtime progress was not recorded at execution time.",
            },
            result_payload={
                "backfilled": True,
                "status": BackgroundJobStatus.SUCCEEDED.value,
            },
            error_payload=None,
            event_log=[],
            error_message=None,
            started_at=None,
            finished_at=None,
        )
        db.flush()
        created_job_ids.append(background_job.id)
        existing_keys.add(milestone_key)

    db.commit()
    return BackgroundJobBackfillSummaryRead(
        created_count=len(created_job_ids),
        skipped_count=skipped_count,
        created_job_ids=created_job_ids,
    )

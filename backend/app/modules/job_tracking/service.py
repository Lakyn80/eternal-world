from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models import BackgroundJob, User
from app.modules.job_tracking import repository
from app.modules.job_tracking.enums import BackgroundJobStatus, BackgroundJobType
from app.modules.job_tracking.exceptions import BackgroundJobNotFoundError, BackgroundJobProfileNotFoundError
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


def create_job(
    db: Session,
    *,
    owner_user_id: int,
    job_type: BackgroundJobType | str,
    profile_id: int | None = None,
    input_payload: dict[str, object] | None = None,
    progress_current: int = 0,
    progress_total: int = 0,
) -> BackgroundJob:
    _validate_owned_profile(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
    )
    background_job = repository.create_background_job(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        job_type=str(job_type.value if isinstance(job_type, BackgroundJobType) else job_type),
        status=BackgroundJobStatus.QUEUED.value,
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
    )
    db.commit()
    db.refresh(background_job)
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
    return background_job


def mark_failed(
    db: Session,
    *,
    job_id: int,
    error_message: str,
    error_payload: dict[str, object] | None = None,
) -> BackgroundJob:
    background_job = repository.get_background_job_by_id(db, job_id=job_id)
    if background_job is None:
        raise BackgroundJobNotFoundError("Background job not found")

    background_job.status = BackgroundJobStatus.FAILED.value
    background_job.error_message = error_message
    background_job.error_payload = error_payload
    background_job.finished_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(background_job)
    return background_job


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

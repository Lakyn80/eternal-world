from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import BackgroundJob


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
    error_message: str | None,
    started_at,
    finished_at,
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
        error_message=error_message,
        started_at=started_at,
        finished_at=finished_at,
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

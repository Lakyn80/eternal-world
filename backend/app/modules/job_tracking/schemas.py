from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class BackgroundJobRead(BaseModel):
    id: int
    owner_user_id: int
    profile_id: int | None
    job_type: str
    status: str
    progress_current: int
    progress_total: int
    celery_task_id: str | None
    input_payload: dict[str, Any]
    result_payload: dict[str, Any] | None
    error_payload: dict[str, Any] | None
    event_log: list[dict[str, Any]] = Field(default_factory=list)
    error_message: str | None
    started_at: datetime | None
    finished_at: datetime | None
    created_at: datetime
    updated_at: datetime


class BackgroundJobSmokeTestCreate(BaseModel):
    profile_id: int | None = Field(default=None, gt=0)


class BackgroundJobBackfillSummaryRead(BaseModel):
    created_count: int
    skipped_count: int
    created_job_ids: list[int]


def build_background_job_read(background_job) -> BackgroundJobRead:
    return BackgroundJobRead(
        id=background_job.id,
        owner_user_id=background_job.owner_user_id,
        profile_id=background_job.profile_id,
        job_type=background_job.job_type,
        status=background_job.status,
        progress_current=background_job.progress_current,
        progress_total=background_job.progress_total,
        celery_task_id=background_job.celery_task_id,
        input_payload=background_job.input_payload,
        result_payload=background_job.result_payload,
        error_payload=background_job.error_payload,
        event_log=list(background_job.event_log or []),
        error_message=background_job.error_message,
        started_at=background_job.started_at,
        finished_at=background_job.finished_at,
        created_at=background_job.created_at,
        updated_at=background_job.updated_at,
    )

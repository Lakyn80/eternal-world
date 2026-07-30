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
    #: Task 65.9 - async job platform status fields, safe for direct
    #: frontend polling. `safe_error_category` is a closed-set label, never
    #: a raw exception string.
    queue: str | None = None
    attempt_count: int = 0
    max_attempts: int = 3
    provider_recovery_count: int = 0
    fresh_process_retry_used: bool = False
    worker_recycle_requested: bool = False
    heartbeat_at: datetime | None = None
    next_attempt_at: datetime | None = None
    safe_error_category: str | None = None


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
        queue=background_job.queue,
        attempt_count=background_job.attempt_count,
        max_attempts=background_job.max_attempts,
        provider_recovery_count=background_job.provider_recovery_count,
        fresh_process_retry_used=background_job.fresh_process_retry_used,
        worker_recycle_requested=background_job.worker_recycle_requested,
        heartbeat_at=background_job.heartbeat_at,
        next_attempt_at=background_job.next_attempt_at,
        safe_error_category=background_job.safe_error_category,
    )

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.job_tracking.exceptions import BackgroundJobNotFoundError, BackgroundJobProfileNotFoundError
from app.modules.job_tracking.schemas import BackgroundJobRead, BackgroundJobSmokeTestCreate, build_background_job_read
from app.modules.job_tracking.service import enqueue_smoke_test_job, get_user_job, list_user_jobs


router = APIRouter(tags=["job_tracking"])
JobIdPath = Annotated[int, Path(gt=0)]


@router.get(
    "/api/jobs",
    response_model=list[BackgroundJobRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
    },
)
def list_background_jobs_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[BackgroundJobRead]:
    background_jobs = list_user_jobs(
        db,
        current_user=current_user,
    )
    return [build_background_job_read(background_job) for background_job in background_jobs]


@router.get(
    "/api/jobs/{job_id}",
    response_model=BackgroundJobRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_background_job_endpoint(
    job_id: JobIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BackgroundJobRead:
    try:
        background_job = get_user_job(
            db,
            current_user=current_user,
            job_id=job_id,
        )
    except BackgroundJobNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return build_background_job_read(background_job)


@router.post(
    "/api/jobs/smoke-test",
    response_model=BackgroundJobRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def enqueue_smoke_test_job_endpoint(
    payload: BackgroundJobSmokeTestCreate | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BackgroundJobRead:
    try:
        background_job = enqueue_smoke_test_job(
            db,
            current_user=current_user,
            profile_id=payload.profile_id if payload is not None else None,
        )
    except BackgroundJobProfileNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return build_background_job_read(background_job)

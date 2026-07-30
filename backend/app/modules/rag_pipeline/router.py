from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.job_tracking.exceptions import (
    BackgroundJobProfileNotFoundError,
    GlobalQueueSaturationError,
    PerProfileActiveJobLimitExceededError,
    PerUserActiveJobLimitExceededError,
)
from app.modules.job_tracking.schemas import BackgroundJobRead, build_background_job_read
from app.modules.rag_pipeline.schemas import RagSourceProcessRequest
from app.modules.rag_pipeline.service import enqueue_rag_source_processing
from app.modules.rag_sources.service import RagSourceNotFoundError


router = APIRouter(tags=["rag-pipeline"])
SourceIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/rag-sources/{source_id}/process",
    response_model=BackgroundJobRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_429_TOO_MANY_REQUESTS: {"model": ErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse},
    },
)
def process_rag_source_endpoint(
    source_id: SourceIdPath,
    payload: RagSourceProcessRequest | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BackgroundJobRead:
    try:
        background_job = enqueue_rag_source_processing(
            db,
            current_user=current_user,
            source_id=source_id,
            payload=payload,
        )
    except (RagSourceNotFoundError, BackgroundJobProfileNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    #: Task 65.9.1 (Part I) - this document-processing endpoint is now a
    #: heavy entry point subject to the centralized backpressure limits
    #: (see `rag_pipeline.service.enqueue_rag_source_processing`); map the
    #: resulting exceptions to the same 429/503-with-Retry-After contract
    #: every other heavy endpoint uses.
    except (PerUserActiveJobLimitExceededError, PerProfileActiveJobLimitExceededError) as exc:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=str(exc)) from exc
    except GlobalQueueSaturationError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
            headers={"Retry-After": str(exc.retry_after_seconds)},
        ) from exc

    return build_background_job_read(background_job)

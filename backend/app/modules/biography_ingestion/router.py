from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.biography_ingestion import repository
from app.modules.biography_ingestion.schemas import (
    BiographyIngestionStartResponse,
    BiographyStatusRead,
    BiographyUpdateRequest,
)
from app.modules.biography_ingestion.service import (
    BiographyIngestionConflictError,
    BiographyIngestionEligibilityError,
    get_biography_status,
    start_biography_ingestion,
    update_biography,
)
from app.modules.memorial_access.capabilities import MemorialCapability, resolve_authorized_profile
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError


router = APIRouter(tags=["biography-ingestion"])
ProfileIdPath = Annotated[int, Path(gt=0)]


def _raise_access_error(exc: Exception) -> None:
    if isinstance(exc, MemorialNotFoundError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    if isinstance(exc, MemorialForbiddenError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    raise exc


def _build_status_read(db: Session, *, profile_id: int) -> BiographyStatusRead:
    from app.modules.memorial_access import repository as memorial_repository

    profile = memorial_repository.get_profile(db, profile_id=profile_id)
    status_read = get_biography_status(profile)
    job = repository.get_latest_biography_job(db, profile_id=profile_id)
    if job is not None:
        status_read.background_job_id = job.id
        status_read.background_job_status = job.status
    return status_read


@router.patch(
    "/api/memorials/{profile_id}/biography",
    response_model=BiographyStatusRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def update_biography_endpoint(
    profile_id: ProfileIdPath,
    payload: BiographyUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographyStatusRead:
    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.DIRECT_MEMORY_WRITE,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    update_biography(db, profile=profile, biography=payload.biography)
    return _build_status_read(db, profile_id=profile_id)


@router.get(
    "/api/memorials/{profile_id}/biography/status",
    response_model=BiographyStatusRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_biography_status_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographyStatusRead:
    try:
        resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.VIEW_MEMORIAL,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    return _build_status_read(db, profile_id=profile_id)


@router.post(
    "/api/memorials/{profile_id}/biography/ingest",
    response_model=BiographyIngestionStartResponse,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_409_CONFLICT: {"model": ErrorResponse},
    },
)
def start_biography_ingestion_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographyIngestionStartResponse:
    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.UPLOAD_SOURCE,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    try:
        background_job = start_biography_ingestion(db, profile=profile)
    except BiographyIngestionEligibilityError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except BiographyIngestionConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return BiographyIngestionStartResponse(
        profile_id=profile.id,
        status=profile.biography_status,
        background_job_id=background_job.id,
        background_job_status=background_job.status,
    )

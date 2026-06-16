from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Response, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.memory_profiles.schemas import (
    MemoryProfileCreate,
    MemoryProfilePhotoAssign,
    MemoryProfileRead,
    MemoryProfileUpdate,
    build_memory_profile_read,
)
from app.modules.memory_profiles.service import (
    InvalidMemoryProfilePhotoError,
    MemoryProfileNotFoundError,
    MemoryProfilePhotoMediaNotFoundError,
    assign_memory_profile_photo,
    create_memory_profile,
    delete_memory_profile,
    get_memory_profile,
    list_memory_profiles,
    remove_memory_profile_photo,
    update_memory_profile,
)


router = APIRouter(prefix="/api/memory-profiles", tags=["memory-profiles"])
ProfileIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "",
    response_model=MemoryProfileRead,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def create_memory_profile_endpoint(
    payload: MemoryProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryProfileRead:
    memory_profile = create_memory_profile(
        db,
        current_user=current_user,
        payload=payload,
    )
    return build_memory_profile_read(memory_profile)


@router.get(
    "",
    response_model=list[MemoryProfileRead],
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def list_memory_profiles_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[MemoryProfileRead]:
    memory_profiles = list_memory_profiles(db, current_user=current_user)
    return [build_memory_profile_read(profile) for profile in memory_profiles]


@router.get(
    "/{profile_id}",
    response_model=MemoryProfileRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_memory_profile_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryProfileRead:
    try:
        memory_profile = get_memory_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except MemoryProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_memory_profile_read(memory_profile)


@router.patch(
    "/{profile_id}",
    response_model=MemoryProfileRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def update_memory_profile_endpoint(
    profile_id: ProfileIdPath,
    payload: MemoryProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryProfileRead:
    try:
        memory_profile = update_memory_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except MemoryProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_memory_profile_read(memory_profile)


@router.delete(
    "/{profile_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def delete_memory_profile_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    try:
        delete_memory_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except MemoryProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "/{profile_id}/photo",
    response_model=MemoryProfileRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def assign_memory_profile_photo_endpoint(
    profile_id: ProfileIdPath,
    payload: MemoryProfilePhotoAssign,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryProfileRead:
    try:
        memory_profile = assign_memory_profile_photo(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except MemoryProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except MemoryProfilePhotoMediaNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except InvalidMemoryProfilePhotoError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return build_memory_profile_read(memory_profile)


@router.delete(
    "/{profile_id}/photo",
    response_model=MemoryProfileRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def remove_memory_profile_photo_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryProfileRead:
    try:
        memory_profile = remove_memory_profile_photo(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except MemoryProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_memory_profile_read(memory_profile)

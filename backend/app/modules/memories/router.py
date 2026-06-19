from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Response, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.billing.schemas import BillingLimitExceededResponse
from app.modules.memories.schemas import MemoryCreate, MemoryRead, MemoryUpdate, build_memory_read
from app.modules.memories.service import (
    InvalidMemoryMediaError,
    MemoryMediaNotFoundError,
    MemoryNotFoundError,
    MemoryProfileNotFoundError,
    create_memory,
    delete_memory,
    get_memory,
    list_memories,
    update_memory,
)


router = APIRouter(tags=["memories"])
MemoryIdPath = Annotated[int, Path(gt=0)]
ProfileIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/memory-profiles/{profile_id}/memories",
    response_model=MemoryRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": BillingLimitExceededResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def create_memory_endpoint(
    profile_id: ProfileIdPath,
    payload: MemoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryRead:
    try:
        memory = create_memory(
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
    except MemoryMediaNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except InvalidMemoryMediaError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return build_memory_read(memory)


@router.get(
    "/api/memory-profiles/{profile_id}/memories",
    response_model=list[MemoryRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_memories_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[MemoryRead]:
    try:
        memories = list_memories(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except MemoryProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return [build_memory_read(memory) for memory in memories]


@router.get(
    "/api/memories/{memory_id}",
    response_model=MemoryRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_memory_endpoint(
    memory_id: MemoryIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryRead:
    try:
        memory = get_memory(
            db,
            current_user=current_user,
            memory_id=memory_id,
        )
    except MemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_memory_read(memory)


@router.patch(
    "/api/memories/{memory_id}",
    response_model=MemoryRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def update_memory_endpoint(
    memory_id: MemoryIdPath,
    payload: MemoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemoryRead:
    try:
        memory = update_memory(
            db,
            current_user=current_user,
            memory_id=memory_id,
            payload=payload,
        )
    except MemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except MemoryMediaNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except InvalidMemoryMediaError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return build_memory_read(memory)


@router.delete(
    "/api/memories/{memory_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def delete_memory_endpoint(
    memory_id: MemoryIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    try:
        delete_memory(
            db,
            current_user=current_user,
            memory_id=memory_id,
        )
    except MemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return Response(status_code=status.HTTP_204_NO_CONTENT)

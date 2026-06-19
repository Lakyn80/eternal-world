from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Response, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.rag_sources.schemas import (
    RagSourceCreate,
    RagSourceRead,
    RagSourceUpdate,
    build_rag_source_read,
)
from app.modules.rag_sources.service import (
    RagSourceNotFoundError,
    RagSourceProfileNotFoundError,
    create_rag_source,
    delete_rag_source,
    get_rag_source,
    list_rag_sources,
    update_rag_source,
)


router = APIRouter(tags=["rag-sources"])
SourceIdPath = Annotated[int, Path(gt=0)]
ProfileIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/memory-profiles/{profile_id}/rag-sources",
    response_model=RagSourceRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def create_rag_source_endpoint(
    profile_id: ProfileIdPath,
    payload: RagSourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagSourceRead:
    try:
        rag_source = create_rag_source(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except RagSourceProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_rag_source_read(rag_source)


@router.get(
    "/api/memory-profiles/{profile_id}/rag-sources",
    response_model=list[RagSourceRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_rag_sources_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[RagSourceRead]:
    try:
        rag_sources = list_rag_sources(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except RagSourceProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return [build_rag_source_read(source) for source in rag_sources]


@router.get(
    "/api/rag-sources/{source_id}",
    response_model=RagSourceRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_rag_source_endpoint(
    source_id: SourceIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagSourceRead:
    try:
        rag_source = get_rag_source(
            db,
            current_user=current_user,
            source_id=source_id,
        )
    except RagSourceNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_rag_source_read(rag_source)


@router.patch(
    "/api/rag-sources/{source_id}",
    response_model=RagSourceRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def update_rag_source_endpoint(
    source_id: SourceIdPath,
    payload: RagSourceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagSourceRead:
    try:
        rag_source = update_rag_source(
            db,
            current_user=current_user,
            source_id=source_id,
            payload=payload,
        )
    except RagSourceNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_rag_source_read(rag_source)


@router.delete(
    "/api/rag-sources/{source_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def delete_rag_source_endpoint(
    source_id: SourceIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    try:
        delete_rag_source(
            db,
            current_user=current_user,
            source_id=source_id,
        )
    except RagSourceNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return Response(status_code=status.HTTP_204_NO_CONTENT)

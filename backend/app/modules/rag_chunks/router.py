from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.rag_chunks.schemas import RagChunkRead, RagSourceChunkingSummaryRead, build_rag_chunk_read
from app.modules.rag_chunks.service import (
    RagChunkNotFoundError,
    RagChunkSourceNotFoundError,
    RagChunkingFailedError,
    chunk_rag_source,
    get_rag_chunk,
    list_rag_chunks,
)


router = APIRouter(tags=["rag-chunks"])
SourceIdPath = Annotated[int, Path(gt=0)]
ChunkIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/rag-sources/{source_id}/chunk",
    response_model=RagSourceChunkingSummaryRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse},
    },
)
def chunk_rag_source_endpoint(
    source_id: SourceIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagSourceChunkingSummaryRead:
    try:
        return chunk_rag_source(
            db,
            current_user=current_user,
            source_id=source_id,
        )
    except RagChunkSourceNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except RagChunkingFailedError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc


@router.get(
    "/api/rag-sources/{source_id}/chunks",
    response_model=list[RagChunkRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_rag_chunks_endpoint(
    source_id: SourceIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[RagChunkRead]:
    try:
        rag_chunks = list_rag_chunks(
            db,
            current_user=current_user,
            source_id=source_id,
        )
    except RagChunkSourceNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return [build_rag_chunk_read(chunk) for chunk in rag_chunks]


@router.get(
    "/api/rag-chunks/{chunk_id}",
    response_model=RagChunkRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_rag_chunk_endpoint(
    chunk_id: ChunkIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagChunkRead:
    try:
        rag_chunk = get_rag_chunk(
            db,
            current_user=current_user,
            chunk_id=chunk_id,
        )
    except RagChunkNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return build_rag_chunk_read(rag_chunk)

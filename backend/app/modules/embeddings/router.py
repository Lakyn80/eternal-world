from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.embeddings.exceptions import (
    RagEmbeddingChunkNotFoundError,
    RagEmbeddingGenerationError,
    RagEmbeddingModelUnavailableError,
    RagEmbeddingNotFoundError,
    RagEmbeddingSourceNotFoundError,
)
from app.modules.embeddings.schemas import (
    RagEmbeddingCreate,
    RagEmbeddingRead,
    RagSourceEmbeddingSummaryRead,
    build_rag_embedding_read,
)
from app.modules.embeddings.service import (
    embed_rag_chunk,
    embed_source_chunks,
    get_rag_embedding,
    list_rag_embeddings_for_chunk,
)


router = APIRouter(tags=["embeddings"])
ChunkIdPath = Annotated[int, Path(gt=0)]
SourceIdPath = Annotated[int, Path(gt=0)]
EmbeddingIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/rag-chunks/{chunk_id}/embed",
    response_model=RagEmbeddingRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse},
    },
)
def embed_rag_chunk_endpoint(
    chunk_id: ChunkIdPath,
    payload: RagEmbeddingCreate | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagEmbeddingRead:
    try:
        rag_embedding = embed_rag_chunk(
            db,
            current_user=current_user,
            chunk_id=chunk_id,
            model_code=payload.model_code if payload is not None else None,
        )
    except RagEmbeddingChunkNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except RagEmbeddingModelUnavailableError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except RagEmbeddingGenerationError as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc)) from exc

    return build_rag_embedding_read(rag_embedding)


@router.post(
    "/api/rag-sources/{source_id}/embed-chunks",
    response_model=RagSourceEmbeddingSummaryRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def embed_source_chunks_endpoint(
    source_id: SourceIdPath,
    payload: RagEmbeddingCreate | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagSourceEmbeddingSummaryRead:
    try:
        return embed_source_chunks(
            db,
            current_user=current_user,
            source_id=source_id,
            model_code=payload.model_code if payload is not None else None,
        )
    except RagEmbeddingSourceNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except RagEmbeddingModelUnavailableError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/api/rag-chunks/{chunk_id}/embeddings",
    response_model=list[RagEmbeddingRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_rag_embeddings_for_chunk_endpoint(
    chunk_id: ChunkIdPath,
    include_vector: bool = Query(default=False),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[RagEmbeddingRead]:
    try:
        rag_embeddings = list_rag_embeddings_for_chunk(
            db,
            current_user=current_user,
            chunk_id=chunk_id,
        )
    except RagEmbeddingChunkNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return [build_rag_embedding_read(embedding, include_vector=include_vector) for embedding in rag_embeddings]


@router.get(
    "/api/rag-embeddings/{embedding_id}",
    response_model=RagEmbeddingRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_rag_embedding_endpoint(
    embedding_id: EmbeddingIdPath,
    include_vector: bool = Query(default=False),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagEmbeddingRead:
    try:
        rag_embedding = get_rag_embedding(
            db,
            current_user=current_user,
            embedding_id=embedding_id,
        )
    except RagEmbeddingNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return build_rag_embedding_read(rag_embedding, include_vector=include_vector)

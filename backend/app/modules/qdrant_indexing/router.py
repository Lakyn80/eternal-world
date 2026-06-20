from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.qdrant_indexing.exceptions import (
    QdrantClientError,
    QdrantCollectionConfigurationError,
    QdrantIndexingDisabledError,
    RagVectorIndexEmbeddingNotFoundError,
    RagVectorIndexEmbeddingNotReadyError,
    RagVectorIndexNotFoundError,
    RagVectorIndexSourceNotFoundError,
)
from app.modules.qdrant_indexing.schemas import (
    RagSourceEmbeddingIndexRequest,
    RagSourceIndexingSummaryRead,
    RagVectorIndexRead,
    build_rag_vector_index_read,
)
from app.modules.qdrant_indexing.service import get_rag_vector_index, index_rag_embedding, index_source_embeddings


router = APIRouter(tags=["qdrant_indexing"])
EmbeddingIdPath = Annotated[int, Path(gt=0)]
SourceIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/rag-embeddings/{embedding_id}/index",
    response_model=RagVectorIndexRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_409_CONFLICT: {"model": ErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse},
    },
)
def index_rag_embedding_endpoint(
    embedding_id: EmbeddingIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagVectorIndexRead:
    try:
        rag_vector_index = index_rag_embedding(
            db,
            current_user=current_user,
            embedding_id=embedding_id,
        )
    except RagVectorIndexEmbeddingNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except RagVectorIndexEmbeddingNotReadyError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except QdrantCollectionConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except QdrantIndexingDisabledError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except QdrantClientError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc

    return build_rag_vector_index_read(rag_vector_index)


@router.post(
    "/api/rag-sources/{source_id}/index-embeddings",
    response_model=RagSourceIndexingSummaryRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse},
    },
)
def index_source_embeddings_endpoint(
    source_id: SourceIdPath,
    payload: RagSourceEmbeddingIndexRequest | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagSourceIndexingSummaryRead:
    try:
        return index_source_embeddings(
            db,
            current_user=current_user,
            source_id=source_id,
            model_code=payload.model_code if payload is not None else None,
        )
    except RagVectorIndexSourceNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except QdrantIndexingDisabledError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc


@router.get(
    "/api/rag-embeddings/{embedding_id}/index",
    response_model=RagVectorIndexRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_rag_vector_index_endpoint(
    embedding_id: EmbeddingIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagVectorIndexRead:
    try:
        rag_vector_index = get_rag_vector_index(
            db,
            current_user=current_user,
            embedding_id=embedding_id,
        )
    except (RagVectorIndexEmbeddingNotFoundError, RagVectorIndexNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return build_rag_vector_index_read(rag_vector_index)

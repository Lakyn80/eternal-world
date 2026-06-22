from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.qdrant_indexing.exceptions import QdrantClientError, QdrantCollectionConfigurationError
from app.modules.rag_retrieval.exceptions import (
    RagRetrievalDisabledError,
    RagRetrievalModelUnavailableError,
    RagRetrievalProfileNotFoundError,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest, RagRetrievalResponseRead
from app.modules.rag_retrieval.service import retrieve_profile_rag


router = APIRouter(tags=["rag_retrieval"])
ProfileIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/memory-profiles/{profile_id}/rag/retrieve",
    response_model=RagRetrievalResponseRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse},
    },
)
def retrieve_profile_rag_endpoint(
    profile_id: ProfileIdPath,
    payload: RagRetrievalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RagRetrievalResponseRead:
    try:
        return retrieve_profile_rag(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except RagRetrievalProfileNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except RagRetrievalModelUnavailableError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except (RagRetrievalDisabledError, QdrantClientError, QdrantCollectionConfigurationError) as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc

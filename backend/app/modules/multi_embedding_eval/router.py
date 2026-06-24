from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.job_tracking.exceptions import BackgroundJobProfileNotFoundError
from app.modules.multi_embedding_eval.schemas import (
    MultiEmbeddingEvalJobResponse,
    MultiEmbeddingEvalRequest,
    build_multi_embedding_eval_job_response,
)
from app.modules.multi_embedding_eval.service import enqueue_multi_embedding_eval
from app.modules.rag_sources.service import RagSourceNotFoundError


router = APIRouter(tags=["multi-embedding-eval"])
SourceIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/api/rag-sources/{source_id}/multi-embedding-eval",
    response_model=MultiEmbeddingEvalJobResponse,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def start_multi_embedding_eval_endpoint(
    source_id: SourceIdPath,
    payload: MultiEmbeddingEvalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MultiEmbeddingEvalJobResponse:
    try:
        background_job = enqueue_multi_embedding_eval(
            db,
            current_user=current_user,
            source_id=source_id,
            payload=payload,
        )
    except (RagSourceNotFoundError, BackgroundJobProfileNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return build_multi_embedding_eval_job_response(background_job)

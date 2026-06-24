from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.active_retrieval_config.exceptions import (
    ActiveRetrievalConfigActivationError,
    ActiveRetrievalConfigJobNotFoundError,
    ActiveRetrievalConfigNotFoundError,
    ActiveRetrievalConfigProfileNotFoundError,
)
from app.modules.active_retrieval_config.schemas import (
    ActiveRetrievalConfigRead,
    ActiveRetrievalConfigUpsertRequest,
    build_active_retrieval_config_read,
)
from app.modules.active_retrieval_config.service import (
    activate_best_multi_embedding_eval_result,
    get_active_retrieval_config,
    upsert_active_retrieval_config,
)
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.rag_sources.service import RagSourceNotFoundError


router = APIRouter(tags=["active-retrieval-config"])
ProfileIdPath = Annotated[int, Path(gt=0)]
SourceIdPath = Annotated[int, Path(gt=0)]
JobIdPath = Annotated[int, Path(gt=0)]


@router.get(
    "/api/memory-profiles/{profile_id}/active-retrieval-config",
    response_model=ActiveRetrievalConfigRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_active_retrieval_config_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ActiveRetrievalConfigRead:
    try:
        active_config = get_active_retrieval_config(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except (
        ActiveRetrievalConfigProfileNotFoundError,
        ActiveRetrievalConfigNotFoundError,
    ) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return build_active_retrieval_config_read(active_config)


@router.post(
    "/api/memory-profiles/{profile_id}/active-retrieval-config",
    response_model=ActiveRetrievalConfigRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def upsert_active_retrieval_config_endpoint(
    profile_id: ProfileIdPath,
    payload: ActiveRetrievalConfigUpsertRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ActiveRetrievalConfigRead:
    try:
        active_config = upsert_active_retrieval_config(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except ActiveRetrievalConfigProfileNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    return build_active_retrieval_config_read(active_config)


@router.post(
    "/api/rag-sources/{source_id}/multi-embedding-eval/{job_id}/activate-best",
    response_model=ActiveRetrievalConfigRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def activate_best_multi_embedding_eval_result_endpoint(
    source_id: SourceIdPath,
    job_id: JobIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ActiveRetrievalConfigRead:
    try:
        active_config = activate_best_multi_embedding_eval_result(
            db,
            current_user=current_user,
            source_id=source_id,
            job_id=job_id,
        )
    except (RagSourceNotFoundError, ActiveRetrievalConfigJobNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ActiveRetrievalConfigActivationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    return build_active_retrieval_config_read(active_config)

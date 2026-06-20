from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query, status

from app.modules.auth.schemas import ErrorResponse
from app.modules.embedding_models.exceptions import EmbeddingModelNotFoundError
from app.modules.embedding_models.schemas import EmbeddingModelRead
from app.modules.embedding_models.service import (
    get_default_embedding_model,
    get_embedding_model,
    list_embedding_models,
)


router = APIRouter(prefix="/api/embedding-models", tags=["embedding-models"])


@router.get(
    "",
    response_model=list[EmbeddingModelRead],
)
def list_embedding_models_endpoint(
    include_disabled: bool = Query(default=False),
) -> list[EmbeddingModelRead]:
    return list_embedding_models(include_disabled=include_disabled)


@router.get(
    "/default",
    response_model=EmbeddingModelRead,
)
def get_default_embedding_model_endpoint() -> EmbeddingModelRead:
    return get_default_embedding_model()


@router.get(
    "/{model_code}",
    response_model=EmbeddingModelRead,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
)
def get_embedding_model_endpoint(model_code: str) -> EmbeddingModelRead:
    try:
        return get_embedding_model(model_code)
    except EmbeddingModelNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

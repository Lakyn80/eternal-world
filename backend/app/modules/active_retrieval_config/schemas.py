from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, field_validator


class ActiveRetrievalConfigUpsertRequest(BaseModel):
    model_code: str = Field(min_length=1, max_length=120)
    collection_name: str = Field(min_length=1, max_length=200)
    top_k: int = Field(default=5, ge=1, le=100)
    score_threshold: float | None = None
    retrieval_mode: str = Field(default="hybrid", min_length=1, max_length=64)
    source_eval_job_id: int | None = Field(default=None, gt=0)
    source_eval_dataset_id: str | None = Field(default=None, max_length=120)
    selected_metrics: dict[str, Any] | None = None
    all_config_scores: list[dict[str, Any]] | None = None
    selection_reason: str | None = Field(default=None, max_length=2000)
    warnings: list[dict[str, Any]] | None = None

    @field_validator("collection_name", "source_eval_dataset_id", "selection_reason")
    @classmethod
    def normalize_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = " ".join(value.split())
        return normalized_value or None

    @field_validator("model_code", "retrieval_mode")
    @classmethod
    def normalize_identifier_text(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value


class ActiveRetrievalConfigRead(BaseModel):
    id: int
    owner_user_id: int
    profile_id: int
    model_code: str
    collection_name: str
    top_k: int
    score_threshold: float | None
    retrieval_mode: str
    source_eval_job_id: int | None
    source_eval_dataset_id: str | None
    selected_metrics: dict[str, Any] | None
    all_config_scores: list[dict[str, Any]] | None
    selection_reason: str | None
    warnings: list[dict[str, Any]] | None
    is_active: bool
    selected_at: datetime
    created_at: datetime
    updated_at: datetime


def build_active_retrieval_config_read(
    active_config,
) -> ActiveRetrievalConfigRead:
    return ActiveRetrievalConfigRead(
        id=active_config.id,
        owner_user_id=active_config.owner_user_id,
        profile_id=active_config.profile_id,
        model_code=active_config.model_code,
        collection_name=active_config.collection_name,
        top_k=active_config.top_k,
        score_threshold=active_config.score_threshold,
        retrieval_mode=active_config.retrieval_mode,
        source_eval_job_id=active_config.source_eval_job_id,
        source_eval_dataset_id=active_config.source_eval_dataset_id,
        selected_metrics=active_config.selected_metrics,
        all_config_scores=active_config.all_config_scores,
        selection_reason=active_config.selection_reason,
        warnings=active_config.warnings,
        is_active=active_config.is_active,
        selected_at=active_config.selected_at,
        created_at=active_config.created_at,
        updated_at=active_config.updated_at,
    )

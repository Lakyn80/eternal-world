from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator, model_validator

from app.modules.rag_quality.schemas import (
    RagQualityConfigScore,
    RagQualityDatasetEvaluation,
    RagQualityEvalDataset,
    RagQualityRetrievalConfigCandidate,
)


class CandidateExecutionWarning(BaseModel):
    code: str = Field(min_length=1, max_length=120)
    message: str = Field(min_length=1, max_length=500)
    details: dict[str, Any] = Field(default_factory=dict)

    @field_validator("code", "message")
    @classmethod
    def normalize_required_text(cls, value: str) -> str:
        normalized_value = " ".join(value.split())
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value


class MultiEmbeddingEvalCandidate(BaseModel):
    config_id: str = Field(min_length=1, max_length=120)
    model_code: str = Field(min_length=1, max_length=120)
    collection_name: str = Field(min_length=1, max_length=200)
    top_k: int = Field(default=5, ge=1, le=100)
    score_threshold: float | None = None
    retrieval_mode: str = Field(default="hybrid", min_length=1, max_length=64)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("config_id", "model_code", "collection_name", "retrieval_mode")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value

    def to_rag_quality_candidate(self) -> RagQualityRetrievalConfigCandidate:
        return RagQualityRetrievalConfigCandidate(
            config_id=self.config_id,
            model_code=self.model_code,
            collection_name=self.collection_name,
            top_k=self.top_k,
            score_threshold=self.score_threshold,
            retrieval_mode=self.retrieval_mode,
            metadata=dict(self.metadata),
        )


class MultiEmbeddingEvalRequest(BaseModel):
    dataset: RagQualityEvalDataset
    candidates: list[MultiEmbeddingEvalCandidate] = Field(min_length=1)
    max_average_latency_ms: float | None = Field(default=None, ge=0)
    max_cost_estimate_total: float | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def validate_unique_candidates(self) -> "MultiEmbeddingEvalRequest":
        config_ids = [candidate.config_id for candidate in self.candidates]
        if len(config_ids) != len(set(config_ids)):
            raise ValueError("Candidate config_id values must be unique")

        collection_names = [candidate.collection_name for candidate in self.candidates]
        if len(collection_names) != len(set(collection_names)):
            raise ValueError("Candidate collection_name values must be unique")

        return self


class CandidateExecutionResult(BaseModel):
    config_id: str
    model_code: str
    collection_name: str
    status: Literal["succeeded", "failed"]
    chunks_reused: bool
    embedding_summary: dict[str, Any] | None = None
    indexing_summary: dict[str, Any] | None = None
    retrieval_case_count: int = Field(default=0, ge=0)
    warnings: list[CandidateExecutionWarning] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class MultiEmbeddingEvalResult(BaseModel):
    source_id: int
    profile_id: int
    dataset_id: str
    candidates_evaluated: list[str] = Field(default_factory=list)
    candidates_failed: list[str] = Field(default_factory=list)
    best_config: dict[str, Any] | None = None
    all_config_scores: list[RagQualityConfigScore] = Field(default_factory=list)
    warnings: list[CandidateExecutionWarning] = Field(default_factory=list)
    candidate_execution_results: list[CandidateExecutionResult] = Field(default_factory=list)
    dataset_evaluation: RagQualityDatasetEvaluation | None = None
    completed_at: str


class MultiEmbeddingEvalJobResponse(BaseModel):
    job_id: int
    job_type: str
    status: str
    celery_task_id: str | None
    progress_current: int
    progress_total: int
    source_id: int
    profile_id: int
    dataset_id: str
    created_at: datetime
    updated_at: datetime


def build_multi_embedding_eval_job_response(background_job) -> MultiEmbeddingEvalJobResponse:
    input_payload = background_job.input_payload or {}
    return MultiEmbeddingEvalJobResponse(
        job_id=background_job.id,
        job_type=background_job.job_type,
        status=background_job.status,
        celery_task_id=background_job.celery_task_id,
        progress_current=background_job.progress_current,
        progress_total=background_job.progress_total,
        source_id=int(input_payload.get("source_id") or 0),
        profile_id=int(input_payload.get("profile_id") or 0),
        dataset_id=str(input_payload.get("dataset_id") or ""),
        created_at=background_job.created_at,
        updated_at=background_job.updated_at,
    )

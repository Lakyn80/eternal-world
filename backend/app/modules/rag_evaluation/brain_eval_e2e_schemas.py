from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

from app.modules.rag_evaluation.schemas import (
    BrainRagEvalCaseSet,
    RagEvaluationBehavior,
    RagEvaluationSuiteResult,
)


BrainEvalE2EFailureClass = Literal[
    "RETRIEVAL_MISSING_EVIDENCE",
    "ANSWER_GENERATION",
]


class BrainEvalRetrievedChunkRecord(BaseModel):
    rank: int = Field(ge=1)
    chunk_id: int
    embedding_id: int
    source_id: int | None = None
    source_title: str | None = None
    chunk_index: int | None = None
    score: float
    text_preview: str


class BrainEvalE2ERetrievalDiagnostic(BaseModel):
    case_id: str
    user_query: str
    expected_fact_id: str | None = None
    expected_chunk_id: int | None = None
    expected_chunk_source_id: int | None = None
    expected_chunk_source_title: str | None = None
    expected_chunk_index: int | None = None
    expected_chunk_exists_in_qdrant: bool | None = None
    expected_chunk_in_top_k: bool | None = None
    expected_chunk_rank: int | None = None
    expected_chunk_in_top_5: bool | None = None
    expected_chunk_in_top_10: bool | None = None
    expected_chunk_in_top_20: bool | None = None
    expected_chunk_in_top_50: bool | None = None
    expected_chunk_rank_at_50: int | None = None
    diagnostic_search_limit: int = Field(default=50, ge=1)
    expected_chunk_position_bucket: str | None = None
    retrieved_chunk_ids: list[int] = Field(default_factory=list)
    retrieved_chunks: list[BrainEvalRetrievedChunkRecord] = Field(default_factory=list)
    top_k: int = Field(ge=1)


class BrainEvalE2EEmbeddingDiagnostics(BaseModel):
    embedding_provider_setting: str
    resolved_indexing_provider_name: str
    resolved_query_provider_name: str
    is_mock_indexing_provider: bool
    is_mock_query_provider: bool
    indexing_query_providers_match: bool
    model_code: str
    model_display_name: str
    provider_model_name: str | None = None
    embedding_dimension: int
    collection_name: str
    collection_vector_size: int | None = None
    flag_embedding_available: bool
    bge_m3_snapshot_cached: bool = False
    bge_m3_snapshot_path: str | None = None
    huggingface_offline_mode: bool = False
    embedding_runtime_fingerprint: str
    collection_rebuilt: bool = False


class BrainEvalE2ETopKDiagnostic(BaseModel):
    top_k: int = Field(ge=1)
    expected_chunk_hits: int = Field(ge=0)
    expected_chunk_checks: int = Field(ge=0)


class BrainEvalE2ECaseResult(BaseModel):
    case_id: str
    title: str
    passed: bool
    expected_behavior: RagEvaluationBehavior
    actual_behavior: RagEvaluationBehavior
    failure_class: BrainEvalE2EFailureClass | None = None
    reasons: list[str] = Field(default_factory=list)
    user_query: str
    answer_text: str
    answer_preview: str
    reference_queries: dict[str, str] = Field(default_factory=dict)
    expected_markers: list[str] = Field(default_factory=list)
    missing_expected_markers: list[str] = Field(default_factory=list)
    forbidden_claims_found: list[str] = Field(default_factory=list)
    expected_fact_id: str | None = None
    expected_evidence_found: bool | None = None
    selected_memory_ids: list[int] = Field(default_factory=list)
    retrieved_chunks: list[BrainEvalRetrievedChunkRecord] = Field(default_factory=list)
    evidence_count: int = Field(ge=0)
    provider_name: str
    response_metadata: dict[str, Any] = Field(default_factory=dict)


class BrainEvalE2ESuiteResult(BaseModel):
    total_cases: int = Field(ge=0)
    passed_cases: int = Field(ge=0)
    failed_cases: int = Field(ge=0)
    retrieval_failures: int = Field(ge=0)
    answer_failures: int = Field(ge=0)
    results: list[BrainEvalE2ECaseResult] = Field(default_factory=list)


class BrainRagEvalE2ERunResult(BaseModel):
    run_id: str
    passed: bool
    case_set: BrainRagEvalCaseSet
    provider_name: str
    model: str | None = None
    profile_id: int
    top_k: int
    embedding_model_code: str
    qdrant_collection: str
    retrieval_mode: str
    embedding_diagnostics: BrainEvalE2EEmbeddingDiagnostics
    retrieval_diagnostics: list[BrainEvalE2ERetrievalDiagnostic] = Field(default_factory=list)
    top_k_diagnostics: list[BrainEvalE2ETopKDiagnostic] = Field(default_factory=list)
    suite_result: BrainEvalE2ESuiteResult
    artifact_paths: dict[str, str] = Field(default_factory=dict)

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator, model_validator


RagQualityExpectedBehavior = Literal[
    "grounded_answer",
    "lack_of_evidence",
    "partial_answer_with_uncertainty",
    "retrieval_only",
]


class RagQualityEvalCase(BaseModel):
    class EvidenceRule(BaseModel):
        marker: str = Field(min_length=1, max_length=500)
        aliases: list[str] = Field(default_factory=list)

        @field_validator("marker")
        @classmethod
        def normalize_marker(cls, value: str) -> str:
            normalized_value = " ".join(value.split())
            if not normalized_value:
                raise ValueError("marker must not be empty")

            return normalized_value

        @field_validator("aliases")
        @classmethod
        def normalize_aliases(cls, value: list[str]) -> list[str]:
            normalized_items: list[str] = []
            seen: set[str] = set()
            for item in value:
                normalized_item = " ".join(item.split())
                if not normalized_item:
                    continue
                normalized_key = normalized_item.lower()
                if normalized_key in seen:
                    continue
                seen.add(normalized_key)
                normalized_items.append(normalized_item)

            return normalized_items

    case_id: str = Field(min_length=1, max_length=120)
    title: str = Field(min_length=1, max_length=200)
    query: str = Field(min_length=1, max_length=5000)
    expected_markers: list[str] = Field(default_factory=list)
    forbidden_markers: list[str] = Field(default_factory=list)
    required_evidence: list[EvidenceRule] = Field(default_factory=list)
    forbidden_evidence: list[EvidenceRule] = Field(default_factory=list)
    expected_source_ids: list[int] = Field(default_factory=list)
    expected_chunk_ids: list[int] = Field(default_factory=list)
    expected_behavior: RagQualityExpectedBehavior = "retrieval_only"
    minimum_relevant_results: int = Field(default=0, ge=0)
    expected_answer_type: str | None = Field(default=None, max_length=120)
    test_type: str | None = Field(default=None, max_length=64)
    source_scope: dict[str, Any] = Field(default_factory=dict)
    minimum_coverage: float | None = Field(default=None, ge=0, le=1)
    allow_partial: bool = False
    expected_citation_count_min: int = Field(default=0, ge=0)
    difficulty: str | None = Field(default=None, max_length=64)
    language: str | None = Field(default=None, max_length=32)
    expected_long_context: bool = False
    minimum_context_chars: int = Field(default=0, ge=0)
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator(
        "case_id",
        "title",
        "query",
        "expected_answer_type",
        "test_type",
        "difficulty",
        "language",
    )
    @classmethod
    def normalize_required_text(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = " ".join(value.split())
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value

    @field_validator("expected_markers", "forbidden_markers", "tags")
    @classmethod
    def normalize_string_lists(cls, value: list[str]) -> list[str]:
        normalized_items: list[str] = []
        for item in value:
            normalized_item = " ".join(item.split())
            if normalized_item:
                normalized_items.append(normalized_item)

        return normalized_items

    @model_validator(mode="after")
    def backfill_canonical_evidence_lists(self) -> "RagQualityEvalCase":
        if self.required_evidence and not self.expected_markers:
            self.expected_markers = [item.marker for item in self.required_evidence]
        if self.forbidden_evidence and not self.forbidden_markers:
            self.forbidden_markers = [item.marker for item in self.forbidden_evidence]
        return self


class RagQualityEvalDataset(BaseModel):
    dataset_id: str = Field(min_length=1, max_length=120)
    name: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    project_name: str | None = Field(default=None, max_length=120)
    cases: list[RagQualityEvalCase] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("dataset_id", "name", "description", "project_name")
    @classmethod
    def normalize_text(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = " ".join(value.split())
        return normalized_value or None


class RagQualityRetrievalConfigCandidate(BaseModel):
    config_id: str = Field(min_length=1, max_length=120)
    model_code: str = Field(min_length=1, max_length=120)
    collection_name: str = Field(min_length=1, max_length=200)
    top_k: int = Field(default=5, ge=1, le=100)
    score_threshold: float | None = None
    retrieval_mode: str = Field(default="hybrid", min_length=1, max_length=64)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("config_id", "model_code", "collection_name", "retrieval_mode")
    @classmethod
    def normalize_candidate_text(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value


class RagQualityRetrievalResultItem(BaseModel):
    chunk_id: int | None = None
    source_id: int | None = None
    score: float = 0
    text: str = Field(default="", max_length=20000)
    rank: int = Field(default=1, ge=1)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("text")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        return " ".join(value.split())


class RagQualityCaseResultsInput(BaseModel):
    config_id: str = Field(min_length=1, max_length=120)
    case_id: str = Field(min_length=1, max_length=120)
    results: list[RagQualityRetrievalResultItem] = Field(default_factory=list)
    latency_ms: float | None = Field(default=None, ge=0)
    cost_estimate: float | None = Field(default=None, ge=0)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("config_id", "case_id")
    @classmethod
    def normalize_identifiers(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value


class RagQualityAggregateMetrics(BaseModel):
    hit_rate: float = Field(default=0, ge=0, le=1)
    recall_at_k: float = Field(default=0, ge=0, le=1)
    mrr: float = Field(default=0, ge=0, le=1)
    forbidden_marker_rate: float = Field(default=0, ge=0, le=1)
    average_latency_ms: float | None = Field(default=None, ge=0)
    cost_estimate_total: float | None = Field(default=None, ge=0)
    evidence_marker_coverage: float = Field(default=0, ge=0, le=1)
    missing_expected_marker_count: int = Field(default=0, ge=0)
    false_positive_count: int = Field(default=0, ge=0)


class RagQualityCaseEvaluation(BaseModel):
    config_id: str
    case_id: str
    title: str
    expected_behavior: RagQualityExpectedBehavior
    passed: bool
    input_missing: bool = False
    hit: bool = False
    recall_at_k: float | None = Field(default=None, ge=0, le=1)
    reciprocal_rank: float | None = Field(default=None, ge=0, le=1)
    evidence_marker_coverage: float | None = Field(default=None, ge=0, le=1)
    relevant_result_count: int = Field(default=0, ge=0)
    false_positive_count: int = Field(default=0, ge=0)
    forbidden_marker_rate: float = Field(default=0, ge=0, le=1)
    matched_expected_markers: list[str] = Field(default_factory=list)
    missing_expected_markers: list[str] = Field(default_factory=list)
    matched_source_ids: list[int] = Field(default_factory=list)
    missing_expected_source_ids: list[int] = Field(default_factory=list)
    matched_chunk_ids: list[int] = Field(default_factory=list)
    missing_expected_chunk_ids: list[int] = Field(default_factory=list)
    forbidden_markers_found: list[str] = Field(default_factory=list)
    latency_ms: float | None = Field(default=None, ge=0)
    cost_estimate: float | None = Field(default=None, ge=0)
    reasons: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class RagQualityConfigEvaluation(BaseModel):
    config_id: str
    model_code: str
    collection_name: str
    retrieval_mode: str
    passed_case_count: int = Field(default=0, ge=0)
    failed_case_count: int = Field(default=0, ge=0)
    metrics: RagQualityAggregateMetrics = Field(default_factory=RagQualityAggregateMetrics)
    case_evaluations: list[RagQualityCaseEvaluation] = Field(default_factory=list)
    reasons: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class RagQualityDatasetEvaluation(BaseModel):
    dataset_id: str
    dataset_name: str
    total_cases: int = Field(default=0, ge=0)
    config_evaluations: list[RagQualityConfigEvaluation] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class RagQualityConfigScore(BaseModel):
    config_id: str
    model_code: str
    collection_name: str
    metrics: RagQualityAggregateMetrics
    acceptable_latency: bool = True
    acceptable_cost: bool = True
    ranking_factors: dict[str, float | int | bool | None] = Field(default_factory=dict)
    reasons: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class RagQualitySelectionResult(BaseModel):
    best_config_id: str | None = None
    best_model_code: str | None = None
    best_collection_name: str | None = None
    selected_metrics: RagQualityAggregateMetrics | None = None
    all_config_scores: list[RagQualityConfigScore] = Field(default_factory=list)
    reasons: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class RagQualityRunResult(BaseModel):
    dataset_evaluation: RagQualityDatasetEvaluation
    selection: RagQualitySelectionResult

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator, model_validator


AvatarEvalCategory = Literal[
    "original_seeded_memory",
    "learned_indexed_memory",
    "owner_corrected_memory",
    "multiple_perspectives",
    "pending_unindexed_memory",
    "rejected_memory",
    "private_memory_blocked",
    "unknown_factual_question",
    "emotional_persona_question",
    "sensitive_subject",
    "repeat_answer_stability",
    "profile_isolation",
]

AvatarEvalFailureType = Literal[
    "retrieval_failure",
    "profile_contamination",
    "evidence_present_but_ignored",
    "unsupported_detail",
    "over_refusal",
    "wrong_corrected_version",
    "perspective_collapsed",
    "persona_cold_or_technical",
    "persona_inconsistent",
    "incorrect_lack_of_evidence",
    "guard_regression",
    "evaluator_failure",
    "runtime_failure",
]

AvatarEvalDimension = Literal[
    "retrieval",
    "factual_grounding",
    "unsupported_details",
    "persona",
    "perspective",
    "safety",
]


class RequiredEvidenceMetadata(BaseModel):
    key: str = Field(min_length=1, max_length=80)
    value: str | int | bool = Field()

    @field_validator("key")
    @classmethod
    def normalize_key(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("metadata key must not be empty")
        return normalized


class AvatarEvalCase(BaseModel):
    id: str = Field(min_length=1, max_length=120)
    category: AvatarEvalCategory
    question: str = Field(min_length=1, max_length=1000)
    expected_memory_source: str | None = Field(default=None, max_length=120)
    expected_evidence_markers: list[str] = Field(default_factory=list)
    expected_markers: list[str] = Field(default_factory=list)
    forbidden_markers: list[str] = Field(default_factory=list)
    expected_lack_of_evidence: bool = False
    expected_persona_behaviors: list[str] = Field(default_factory=list)
    forbidden_behaviors: list[str] = Field(default_factory=list)
    expected_perspective_behavior: str | None = Field(default=None, max_length=200)
    required_evidence_metadata: list[RequiredEvidenceMetadata] = Field(default_factory=list)
    repeat_count: int | None = Field(default=None, ge=1, le=20)
    notes: str | None = Field(default=None, max_length=1000)

    @field_validator("id", "question", "expected_memory_source", "expected_perspective_behavior", "notes")
    @classmethod
    def normalize_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized = " ".join(value.split())
        if not normalized:
            raise ValueError("text field must not be empty")
        return normalized

    @field_validator(
        "expected_evidence_markers",
        "expected_markers",
        "forbidden_markers",
        "expected_persona_behaviors",
        "forbidden_behaviors",
    )
    @classmethod
    def normalize_string_list(cls, value: list[str]) -> list[str]:
        normalized_items: list[str] = []
        for item in value:
            normalized = " ".join(item.split())
            if normalized:
                normalized_items.append(normalized)
        return normalized_items

    @model_validator(mode="after")
    def validate_expectations(self):
        if not self.expected_lack_of_evidence and not (
            self.expected_markers or self.expected_perspective_behavior
        ):
            raise ValueError("grounded cases require expected_markers or perspective expectations")
        return self


class AvatarEvalEvidence(BaseModel):
    chunk_id: str
    source_id: int | None = None
    source_title: str | None = None
    score: float | None = None
    text_preview: str | None = None
    payload_metadata: dict[str, Any] | None = None


class AvatarEvalAnswerInput(BaseModel):
    answer: str
    trace_id: str
    evidence: list[AvatarEvalEvidence] = Field(default_factory=list)
    lack_of_evidence: bool
    persona_applied: bool
    guard_applied: bool
    guard_reason: str | None = None
    duration_seconds: float = Field(default=0.0, ge=0.0)
    cache_summary: dict[str, Any] = Field(default_factory=dict)
    candidate_provenance: dict[str, Any] = Field(default_factory=dict)


class AvatarEvalDimensionResult(BaseModel):
    name: AvatarEvalDimension
    passed: bool
    details: list[str] = Field(default_factory=list)


class AvatarEvalCaseRunResult(BaseModel):
    case_id: str
    category: AvatarEvalCategory
    run_index: int = Field(ge=1)
    passed: bool
    answer: str
    trace_id: str
    evidence_summary: list[dict[str, Any]] = Field(default_factory=list)
    dimensions: list[AvatarEvalDimensionResult]
    failure_types: list[AvatarEvalFailureType] = Field(default_factory=list)
    likely_layer: str | None = None
    recommended_fix_layer: str | None = None
    duration_seconds: float = Field(default=0.0, ge=0.0)
    cache_summary: dict[str, Any] = Field(default_factory=dict)
    evaluator_error: str | None = None


class AvatarEvalMetricDefinitions(BaseModel):
    retrieval_evidence_hit_rate: str
    required_marker_rate: str
    unsupported_detail_rate: str
    over_refusal_rate: str
    lack_of_evidence_correctness_rate: str
    persona_consistency_rate: str
    forbidden_style_rate: str
    learned_memory_answer_support_rate: str
    corrected_memory_preference_rate: str
    perspective_preservation_rate: str
    answer_stability_rate: str
    profile_contamination_count: str
    evaluated_case_count: str
    passed_case_count: str
    failed_case_count: str


class AvatarEvalSummary(BaseModel):
    evaluated_case_count: int = Field(ge=0)
    total_runs: int = Field(ge=0)
    passed_case_count: int = Field(ge=0)
    failed_case_count: int = Field(ge=0)
    retrieval_evidence_hit_rate: float = Field(ge=0.0, le=1.0)
    required_marker_rate: float = Field(ge=0.0, le=1.0)
    unsupported_detail_rate: float = Field(ge=0.0, le=1.0)
    over_refusal_rate: float = Field(ge=0.0, le=1.0)
    lack_of_evidence_correctness_rate: float = Field(ge=0.0, le=1.0)
    persona_consistency_rate: float = Field(ge=0.0, le=1.0)
    forbidden_style_rate: float = Field(ge=0.0, le=1.0)
    learned_memory_answer_support_rate: float = Field(ge=0.0, le=1.0)
    corrected_memory_preference_rate: float = Field(ge=0.0, le=1.0)
    perspective_preservation_rate: float = Field(ge=0.0, le=1.0)
    answer_stability_rate: float = Field(ge=0.0, le=1.0)
    profile_contamination_count: int = Field(ge=0)
    failure_counts: dict[str, int] = Field(default_factory=dict)
    metric_definitions: AvatarEvalMetricDefinitions


class AvatarEvalRunConfig(BaseModel):
    dataset_path: Path
    output_dir: Path
    repeat_count: int = Field(default=3, ge=1, le=20)
    profile_id: int | None = Field(default=None, gt=0)
    allow_overwrite: bool = False
    run_label: str = Field(default="baseline", min_length=1, max_length=80)


class AvatarEvalRunManifest(BaseModel):
    run_id: str
    run_label: str
    dataset_path: str
    output_dir: str
    repeat_count: int
    started_at: datetime
    completed_at: datetime
    real_fa_chat_path: bool
    retrieval_changed: bool = False
    embedding_changed: bool = False
    redis_changed: bool = False
    qdrant_collection_changed: bool = False
    model_download_requested: bool = False
    brain_prompt_version: str | None = None


class AvatarEvalRunResult(BaseModel):
    manifest: AvatarEvalRunManifest
    summary: AvatarEvalSummary
    results: list[AvatarEvalCaseRunResult]
    artifact_paths: dict[str, str] = Field(default_factory=dict)


class AvatarEvalComparison(BaseModel):
    baseline_label: str
    candidate_label: str
    improved_cases: list[str] = Field(default_factory=list)
    regressed_cases: list[str] = Field(default_factory=list)
    unchanged_failures: list[str] = Field(default_factory=list)
    metric_deltas: dict[str, float] = Field(default_factory=dict)
    accepted: bool


class AvatarEvalGateCheck(BaseModel):
    name: str
    required: str
    actual: str
    passed: bool


class AvatarEvalQualityGateResult(BaseModel):
    checks: list[AvatarEvalGateCheck]
    profile_isolation_passed: bool
    corrected_memory_passed: bool
    perspective_passed: bool
    overall_passed: bool

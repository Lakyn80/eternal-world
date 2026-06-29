from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, field_validator


class RealQuestionEvalConfig(BaseModel):
    email: str = Field(default="demo.real.question.eval@example.test", max_length=320)
    profile_name: str = Field(default="Demo Real Question Eval Profile", max_length=120)
    artifact_dir: Path = Field(default=Path("backend/artifacts/real_question_eval"))
    dataset_path: Path | None = None
    use_real_local_models: bool = False
    candidate_model_codes: list[str] | None = None
    write_artifacts: bool = True
    run_type_override: str | None = None
    execution_mode_override: str | None = None
    rerun_attempted_full_version_batch_b: bool = False

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return value.strip().lower()

    @field_validator("profile_name")
    @classmethod
    def normalize_profile_name(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("profile_name must not be empty")

        return normalized_value

    @field_validator("dataset_path")
    @classmethod
    def normalize_dataset_path(cls, value: Path | None) -> Path | None:
        if value is None:
            return None
        return Path(value)

    @field_validator("candidate_model_codes")
    @classmethod
    def normalize_candidate_model_codes(cls, value: list[str] | None) -> list[str] | None:
        if value is None:
            return None

        normalized_values: list[str] = []
        seen: set[str] = set()
        for item in value:
            normalized_item = item.strip().lower()
            if not normalized_item:
                continue
            if normalized_item in seen:
                raise ValueError("candidate_model_codes must be unique")
            seen.add(normalized_item)
            normalized_values.append(normalized_item)

        if not normalized_values:
            raise ValueError("candidate_model_codes must not be empty when provided")

        return normalized_values


class RealQuestionEvalRetrievedChunk(BaseModel):
    rank: int
    chunk_id: int
    score: float
    preview: str


class RealQuestionEvalModelResult(BaseModel):
    model_code: str
    collection_name: str
    top_chunks: list[RealQuestionEvalRetrievedChunk] = Field(default_factory=list)
    matched_expected_markers: list[str] = Field(default_factory=list)
    missing_expected_markers: list[str] = Field(default_factory=list)
    false_positive_markers: list[str] = Field(default_factory=list)
    evidence_coverage: float | None = None
    first_relevant_rank: int | None = None
    relevant_result_count: int = 0
    false_positive_count: int = 0
    answer_summary: str
    groundedness_verdict: str
    passed: bool
    hit: bool
    reasons: list[str] = Field(default_factory=list)


class RealQuestionEvalQuestionResult(BaseModel):
    question_id: str
    question_text: str
    expected_markers: list[str] = Field(default_factory=list)
    forbidden_markers: list[str] = Field(default_factory=list)
    model_results: list[RealQuestionEvalModelResult] = Field(default_factory=list)
    winner_model_code: str | None = None
    winner_reason: str = ""


class RealQuestionEvalAggregateModelResult(BaseModel):
    model_code: str
    collection_name: str
    question_wins: int = 0
    average_evidence_coverage: float = 0
    average_first_relevant_rank: float | None = None
    total_matched_markers: int = 0
    total_missing_markers: int = 0
    total_false_positive_markers: int = 0
    passed_questions: int = 0
    official_metrics: dict[str, Any] | None = None


class RealQuestionEvalArtifactPaths(BaseModel):
    latest_markdown_report: str | None = None
    latest_json_result: str | None = None
    archived_markdown_report: str | None = None
    archived_json_result: str | None = None


class RealQuestionEvalResult(BaseModel):
    passed: bool
    used_fake_models: bool
    run_type: str | None = None
    execution_mode: str | None = None
    benchmark_batch_label: str | None = None
    benchmark_status: str | None = None
    incomplete_reason: str | None = None
    baseline_provider_codes: list[str] = Field(default_factory=list)
    excluded_provider_codes: list[str] = Field(default_factory=list)
    newly_evaluated_provider_codes: list[str] = Field(default_factory=list)
    comparison_scope_note: str | None = None
    non_compared_notes: list[str] = Field(default_factory=list)
    historical_providers: list[str] = Field(default_factory=list)
    new_real_providers: list[str] = Field(default_factory=list)
    historical_overall_winner_model_code: str | None = None
    any_new_provider_beat_historical_winner: bool | None = None
    generated_at: str | None = None
    run_id: str | None = None
    profile_id: int | None = None
    source_id: int | None = None
    job_id: int | None = None
    dataset_id: str = ""
    dataset_name: str = ""
    source_chunk_count: int = 0
    compared_models: list[str] = Field(default_factory=list)
    question_results: list[RealQuestionEvalQuestionResult] = Field(default_factory=list)
    aggregate_results: list[RealQuestionEvalAggregateModelResult] = Field(default_factory=list)
    overall_winner_model_code: str | None = None
    official_best_config: dict[str, Any] | None = None
    activated: bool = False
    runtime_verified: bool = False
    activated_config: dict[str, Any] | None = None
    runtime_retrieval: dict[str, Any] | None = None
    artifact_paths: RealQuestionEvalArtifactPaths = Field(default_factory=RealQuestionEvalArtifactPaths)
    markdown_report_path: str | None = None
    json_result_path: str | None = None
    warnings: list[str] = Field(default_factory=list)
    error: str | None = None

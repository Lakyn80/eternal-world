from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator

from app.modules.ai_agents.schemas import ChatHistoryEntry


RagEvaluationBehavior = Literal[
    "grounded_answer",
    "lack_of_evidence",
    "partial_answer_with_uncertainty",
]

BrainRagEvalCaseSet = Literal["foundation", "eternal_world", "all"]


class RagEvaluationProfileSetup(BaseModel):
    profile_id: int = Field(default=1, gt=0)
    name: str = Field(min_length=1, max_length=120)
    birth_date: date | None = None
    death_date: date | None = None
    biography: str | None = None
    personality: str | None = None
    catchphrases: str | None = None

    @field_validator("name")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("Profile name must not be empty")

        return normalized_value


class RagEvaluationMemoryEvidenceSetup(BaseModel):
    source_id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=200)
    memory_type: str = Field(default="text", min_length=1, max_length=32)
    occurred_at: datetime | None = None
    occurred_year: int | None = None
    content_preview: str | None = None
    selection_reason: str = Field(default="eval_fixture", min_length=1, max_length=120)

    @field_validator("title", "memory_type", "selection_reason")
    @classmethod
    def normalize_required_text(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value

    @field_validator("content_preview")
    @classmethod
    def normalize_content_preview(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = " ".join(value.split())
        return normalized_value or None


class RagEvaluationRetrievedEvidenceSetup(BaseModel):
    chunk_id: int = Field(gt=0)
    source_id: int = Field(gt=0)
    embedding_id: int = Field(gt=0)
    score: float = Field(default=0.95, ge=0)
    language: str | None = Field(default="en", max_length=16)
    source_document_type: str = Field(default="document_text", min_length=1, max_length=32)
    validation_status: str = Field(default="valid", min_length=1, max_length=32)
    text_hash: str = Field(min_length=1, max_length=128)
    content_preview: str = Field(min_length=1, max_length=500)

    @field_validator(
        "language",
        "source_document_type",
        "validation_status",
        "text_hash",
        "content_preview",
    )
    @classmethod
    def normalize_text_fields(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = " ".join(value.split())
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value


class RagEvaluationCase(BaseModel):
    case_id: str = Field(min_length=1, max_length=100)
    title: str = Field(min_length=1, max_length=200)
    profile: RagEvaluationProfileSetup
    recent_history: list[ChatHistoryEntry] = Field(default_factory=list)
    memory_evidence_items: list[RagEvaluationMemoryEvidenceSetup] = Field(default_factory=list)
    retrieved_evidence_items: list[RagEvaluationRetrievedEvidenceSetup] = Field(default_factory=list)
    user_query: str = Field(min_length=1, max_length=5000)
    expected_behavior: RagEvaluationBehavior
    expected_evidence_markers: list[str] = Field(default_factory=list)
    forbidden_claims: list[str] = Field(default_factory=list)
    should_require_lack_of_evidence: bool = False
    minimum_required_evidence_count: int = Field(default=0, ge=0)

    @field_validator("case_id", "title", "user_query")
    @classmethod
    def normalize_required_fields(cls, value: str) -> str:
        normalized_value = " ".join(value.split())
        if not normalized_value:
            raise ValueError("Field must not be empty")

        return normalized_value

    @field_validator("expected_evidence_markers", "forbidden_claims")
    @classmethod
    def normalize_string_lists(cls, value: list[str]) -> list[str]:
        normalized_items: list[str] = []
        for item in value:
            normalized_item = " ".join(item.split())
            if normalized_item:
                normalized_items.append(normalized_item)

        return normalized_items


class RagEvaluationCaseResult(BaseModel):
    case_id: str
    title: str
    passed: bool
    expected_behavior: RagEvaluationBehavior
    actual_behavior: RagEvaluationBehavior
    reasons: list[str] = Field(default_factory=list)
    evidence_count: int = Field(ge=0)
    missing_expected_markers: list[str] = Field(default_factory=list)
    forbidden_claims_found: list[str] = Field(default_factory=list)
    answer_preview: str
    provider_name: str
    response_metadata: dict[str, Any] = Field(default_factory=dict)


class RagEvaluationSuiteResult(BaseModel):
    total_cases: int = Field(ge=0)
    passed_cases: int = Field(ge=0)
    failed_cases: int = Field(ge=0)
    results: list[RagEvaluationCaseResult] = Field(default_factory=list)


class BrainRagEvalConfig(BaseModel):
    case_set: BrainRagEvalCaseSet = "foundation"
    provider_name: str = Field(default="openai_compatible", min_length=1)
    artifact_dir: Path | None = None
    write_artifacts: bool = True

    @field_validator("provider_name")
    @classmethod
    def normalize_provider_name(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("provider_name must not be empty")
        return normalized_value


class BrainRagEvalPreflightResult(BaseModel):
    passed: bool
    provider_name: str
    model: str | None = None
    case_set: BrainRagEvalCaseSet
    case_count: int = Field(ge=0)
    issues: list[str] = Field(default_factory=list)


class BrainRagEvalRunResult(BaseModel):
    run_id: str
    passed: bool
    case_set: BrainRagEvalCaseSet
    provider_name: str
    model: str | None = None
    suite_result: RagEvaluationSuiteResult
    artifact_paths: dict[str, str] = Field(default_factory=dict)

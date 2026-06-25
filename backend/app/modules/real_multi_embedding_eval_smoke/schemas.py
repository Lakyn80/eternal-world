from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class RealMultiEmbeddingEvalSmokeConfig(BaseModel):
    email: str = Field(default="demo.multi.embedding.smoke@example.test", max_length=320)
    profile_name: str = Field(default="Demo Multi Embedding Profile", max_length=120)
    use_real_local_models: bool = False

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


class RealMultiEmbeddingEvalSmokeCandidateResult(BaseModel):
    candidate: str
    status: str
    collection: str
    metrics: dict[str, Any] | None = None


class RealMultiEmbeddingEvalSmokeResult(BaseModel):
    passed: bool
    used_fake_models: bool
    profile_id: int | None = None
    source_id: int | None = None
    job_id: int | None = None
    candidates: list[RealMultiEmbeddingEvalSmokeCandidateResult] = Field(default_factory=list)
    best_config: dict[str, Any] | None = None
    activated: bool = False
    runtime_active_config: dict[str, Any] | None = None
    runtime_retrieval: dict[str, Any] | None = None
    warnings: list[str] = Field(default_factory=list)
    error: str | None = None

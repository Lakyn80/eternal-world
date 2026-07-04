from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class ProductionHybridSmokeConfig(BaseModel):
    email: str = Field(default="production.hybrid.smoke@example.test", max_length=320)
    profile_name: str = Field(default="Production Hybrid Smoke Profile", max_length=120)
    model_code: str = Field(default="bge_m3_dense_sparse", max_length=64)

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

    @field_validator("model_code")
    @classmethod
    def normalize_model_code(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("model_code must not be empty")

        return normalized_value


class ProductionHybridSmokeStageResult(BaseModel):
    name: str
    passed: bool
    details: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None


class ProductionHybridSmokeResult(BaseModel):
    passed: bool
    stages: list[ProductionHybridSmokeStageResult] = Field(default_factory=list)

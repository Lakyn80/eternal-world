from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class DemoSmokeConfig(BaseModel):
    email: str = Field(default="demo.e2e.smoke@example.test", max_length=320)
    profile_name: str = Field(default="Demo Grandfather", max_length=120)
    timeout_seconds: float = Field(default=120.0, gt=0)
    poll_interval_seconds: float = Field(default=2.0, gt=0)

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


class DemoSmokeStageResult(BaseModel):
    name: str
    passed: bool
    details: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None


class DemoSmokeResult(BaseModel):
    passed: bool
    stages: list[DemoSmokeStageResult] = Field(default_factory=list)

    @property
    def stage_count(self) -> int:
        return len(self.stages)

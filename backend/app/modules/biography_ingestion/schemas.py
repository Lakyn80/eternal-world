from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator


BIOGRAPHY_MAX_LENGTH = 20000


class BiographyUpdateRequest(BaseModel):
    biography: str = Field(max_length=BIOGRAPHY_MAX_LENGTH)

    @field_validator("biography")
    @classmethod
    def validate_biography(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("biography must not be empty")
        return normalized


class BiographyStatusRead(BaseModel):
    profile_id: int
    status: str
    content_hash: str | None
    indexed_at: datetime | None
    attempt_count: int
    failure_reason: str | None
    background_job_status: str | None = None
    background_job_id: int | None = None


class BiographyIngestionStartResponse(BaseModel):
    profile_id: int
    status: str
    background_job_id: int
    background_job_status: str

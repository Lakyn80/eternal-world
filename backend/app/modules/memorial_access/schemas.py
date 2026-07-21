from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from app.modules.auth.schemas import normalize_and_validate_email
from app.modules.memorial_contribution_indexing.schemas import ContributionIndexingStatusRead
from app.modules.memory_profiles.schemas import normalize_optional_text, normalize_required_text, validate_date_range


MemorialRole = Literal["owner", "trusted_reviewer", "contributor", "viewer"]
InvitableMemorialRole = Literal["trusted_reviewer", "contributor", "viewer"]
ContributionStatus = Literal["draft", "needs_review", "approved", "rejected", "archived", "superseded"]
PrivacyScope = Literal["private_owner", "selected_family", "all_family", "public_legacy"]


class MemorialCreate(BaseModel):
    name: str = Field(max_length=120)
    birth_date: date | None = None
    death_date: date | None = None
    biography: str | None = None
    personality: str | None = None
    catchphrases: str | None = None
    is_public: bool = False

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        return normalize_required_text(value, "name")

    @field_validator("biography", "personality", "catchphrases")
    @classmethod
    def validate_optional_fields(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)

    @model_validator(mode="after")
    def validate_dates(self) -> "MemorialCreate":
        validate_date_range(self.birth_date, self.death_date)
        return self


class MemorialRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_user_id: int
    name: str
    birth_date: date | None
    death_date: date | None
    biography: str | None
    personality: str | None
    catchphrases: str | None
    is_public: bool
    current_user_role: MemorialRole
    created_at: datetime
    updated_at: datetime


class MembershipRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    profile_id: int
    user_id: int
    email: str
    full_name: str | None
    role: MemorialRole
    status: Literal["active", "revoked"]
    created_at: datetime
    updated_at: datetime


class InvitationCreate(BaseModel):
    email: str
    role: InvitableMemorialRole
    expires_in_days: int = Field(default=7, ge=1, le=30)

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return normalize_and_validate_email(value)


class InvitationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    profile_id: int
    email: str
    role: InvitableMemorialRole
    expires_at: datetime
    accepted_at: datetime | None
    revoked_at: datetime | None
    created_at: datetime


class InvitationCreateResponse(InvitationRead):
    token: str
    accept_url: str


class InvitationAcceptRequest(BaseModel):
    token: str = Field(min_length=20, max_length=512)

    @field_validator("token")
    @classmethod
    def normalize_token(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("token must not be empty")
        return normalized


class ContributionCreate(BaseModel):
    title: str = Field(max_length=200)
    memory_text: str = Field(max_length=5000)
    source_note: str | None = Field(default=None, max_length=500)
    privacy_scope: PrivacyScope = "private_owner"
    submit_for_review: bool = True

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        return normalize_required_text(value, "title")

    @field_validator("memory_text")
    @classmethod
    def validate_memory_text(cls, value: str) -> str:
        return normalize_required_text(value, "memory_text")

    @field_validator("source_note")
    @classmethod
    def validate_source_note(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)


class ContributionReviewRequest(BaseModel):
    review_note: str | None = Field(default=None, max_length=500)
    supersedes_contribution_id: int | None = Field(default=None, gt=0)

    @field_validator("review_note")
    @classmethod
    def validate_review_note(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)


class ContributionRejectRequest(BaseModel):
    reason: str | None = Field(default=None, max_length=500)

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, value: str | None) -> str | None:
        return normalize_optional_text(value)


class ContributionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    profile_id: int
    author_user_id: int
    author_email: str
    title: str
    memory_text: str
    source_note: str | None
    privacy_scope: PrivacyScope
    status: ContributionStatus
    is_current: bool
    supersedes_contribution_id: int | None
    reviewed_at: datetime | None
    reviewed_by_user_id: int | None
    review_note: str | None
    rejection_reason: str | None
    active_memory_eligible: bool
    indexing_status: ContributionIndexingStatusRead
    created_at: datetime
    updated_at: datetime


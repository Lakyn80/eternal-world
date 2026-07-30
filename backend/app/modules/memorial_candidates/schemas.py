"""Authenticated, membership-checked request bodies for the candidate/
clarification/owner-review/indexing endpoints. Deliberately do NOT include
`actor_id`/`actor_role`/`relationship_to_owner` (unlike the demo module's
request schemas) - the server always derives those from the caller's
database-verified `MemorialMembership`, never from client input."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from app.modules.family_memory_enrichment.enums import OwnerReviewAction, PrivacyScope
from app.modules.family_memory_enrichment.schemas import (
    CandidateEnrichmentRead,
    ClarificationQuestionRead,
    FamilyMemoryContributionRead,
    PersonalMemoryDetails,
)


def _normalize(value: str) -> str:
    return " ".join(value.split()).strip()


class ClarificationAnswerBody(BaseModel):
    answer_text: str = Field(min_length=1, max_length=1000)
    structured_details: PersonalMemoryDetails | None = None

    @field_validator("answer_text", mode="before")
    @classmethod
    def validate_answer_text(cls, value: str) -> str:
        normalized = _normalize(str(value))
        if not normalized:
            raise ValueError("answer_text is required")
        return normalized


class OwnerReviewBody(BaseModel):
    action: OwnerReviewAction
    finalized_memory_text: str | None = Field(default=None, max_length=500)
    privacy_scope: PrivacyScope | None = None
    review_note: str | None = Field(default=None, max_length=500)
    rejection_reason: str | None = Field(default=None, max_length=500)

    @field_validator("finalized_memory_text", "review_note", "rejection_reason", mode="before")
    @classmethod
    def validate_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized = _normalize(str(value))
        return normalized or None


class CandidateHistoryRead(BaseModel):
    """Task 65.4: the full append-only audit trail for one candidate - the
    original Biographer/family answer, every clarification round, and every
    owner correction - so the authenticated Review UI can show provenance
    before an owner approves or edits a memory. Composed entirely from
    already-existing, already-tested queries
    (`family_memory_enrichment.repository.list_contributions`/
    `list_clarifications`); no new domain logic."""

    candidate: CandidateEnrichmentRead
    contributions: list[FamilyMemoryContributionRead]
    clarifications: list[ClarificationQuestionRead]


class BiographyMemoryEntryRead(BaseModel):
    """Task 65.6.1 (Part E) - one approved, promoted candidate memory
    projected into the Biography tab as confirmed evidence, distinct from
    the manually-authored `biography` free-text field. Only current,
    approved candidates the viewer is authorized to see are ever included
    (see `avatar_memory_promotions.service.list_biography_memory_entries`) -
    never a pending/rejected/archived draft, and never another member's
    owner-only memory."""

    promotion_id: int
    candidate_id: int
    text: str
    privacy_scope: PrivacyScope
    promotion_status: str
    searchable_as_fact: bool
    created_at: datetime
    indexed_at: datetime | None = None

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

from app.modules.avatar_memory_promotions.schemas import (
    AvatarMemoryPromotionRead,
    AvatarMemoryPromotionStatus,
)
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateConfidence,
    MemoryCandidateRead,
    MemoryCandidateSource,
    MemoryCandidateStatus,
)
from app.modules.avatar_persona.schemas import (
    AvatarEmotion,
    AvatarFaceDirectives,
    AvatarVoiceDirectives,
)
from app.modules.content_translation.schemas import MemoryContentTranslationRead
from app.modules.family_memory_enrichment.enums import (
    DisputeStatus,
    EnrichmentStatus,
    FamilyMemoryActorRole,
    MemoryType,
    PrivacyScope,
)
from app.modules.family_memory_enrichment.schemas import (
    CandidateEnrichmentRead,
    ClarificationQuestionRead,
    FamilyMemoryContributionRead,
)


class DemoFaChatMessageRequest(BaseModel):
    profile_id: int | None = None
    message: str
    debug: bool | None = None
    active_memory_candidate_id: int | None = Field(default=None, gt=0)
    actor_id: str | None = Field(default=None, min_length=1, max_length=120)
    actor_role: FamilyMemoryActorRole | None = None
    relationship_to_owner: str | None = Field(default=None, max_length=120)
    #: Frontend interface locale for this chat turn. Defaults to "ru" so
    #: existing Russian-only clients that never send this field keep their
    #: exact current behavior. Direct-locale architecture (Task 64.5.2,
    #: replacing the Task 64.5.1 double-translation design): the user's
    #: original-language message is used unmodified for BGE-M3 multilingual
    #: retrieval and passed as-is to the Brain, which is told
    #: ``response_language=locale`` and answers directly in that language -
    #: no query-translation or answer-translation call for either locale.
    #: See demo_fa_chat.service.run_demo_fa_chat_message.
    locale: Literal["cs", "ru"] = "ru"

    @model_validator(mode="after")
    def validate_actor_context(self):
        actor_fields_present = self.actor_id is not None or self.actor_role is not None
        if actor_fields_present and (self.actor_id is None or self.actor_role is None):
            raise ValueError("actor_id and actor_role must be provided together")
        if self.relationship_to_owner is not None and not actor_fields_present:
            raise ValueError("relationship_to_owner requires actor context")
        if self.active_memory_candidate_id is not None and not actor_fields_present:
            raise ValueError("active_memory_candidate_id requires actor context")
        return self


class DemoFaChatEvidenceItem(BaseModel):
    chunk_id: str
    source_id: int | None = None
    source_title: str | None = None
    score: float | None = None
    text_preview: str | None = None
    payload_metadata: dict[str, Any] | None = None


class DemoFaChatMemoryCandidate(BaseModel):
    candidate_id: int | None = None
    status: MemoryCandidateStatus
    confidence: MemoryCandidateConfidence
    source: MemoryCandidateSource
    proposed_memory_text: str
    user_message_excerpt: str
    reason: str
    memory_type: MemoryType | None = None
    enrichment_status: EnrichmentStatus | None = None
    privacy_scope: PrivacyScope | None = None
    dispute_status: DisputeStatus | None = None
    unresolved_clarification_count: int | None = None


class DemoFaChatMessageResponse(BaseModel):
    answer: str
    locale: Literal["cs", "ru"] = "ru"
    lack_of_evidence: bool
    retrieval_used: bool
    persona_applied: bool
    guard_applied: bool
    guard_reason: str | None = None
    trace_id: str
    memory_candidate: DemoFaChatMemoryCandidate | None = None
    memory_candidate_persisted: bool | None = None
    active_memory_candidate_id: int | None = None
    enrichment_status: EnrichmentStatus | None = None
    next_clarification_question: ClarificationQuestionRead | None = None
    emotion: AvatarEmotion | None = None
    face_directives: AvatarFaceDirectives | None = None
    voice_directives: AvatarVoiceDirectives | None = None
    evidence: list[DemoFaChatEvidenceItem]


class DemoFaChatTranslationListResponse(BaseModel):
    items: list[MemoryContentTranslationRead]
    total: int


class DemoFaChatErrorResponse(BaseModel):
    detail: str
    trace_id: str | None = None


class DemoFaChatMemoryCandidateReviewResponse(MemoryCandidateRead):
    promotion_created: bool
    promotion_id: int | None = None
    promotion_status: AvatarMemoryPromotionStatus | None = None
    searchable_as_fact: bool | None = None


class DemoFaChatMemoryPromotionListResponse(BaseModel):
    items: list[AvatarMemoryPromotionRead]
    total: int


class DemoFaChatMemoryCandidateSummary(BaseModel):
    """Lightweight per-candidate inbox card projection (review UI only, Task 64.5).

    Reuses existing candidate/contribution/promotion data; does not compute or
    store anything new, and duplicates no owner-review or eligibility logic.
    """

    candidate_id: int
    status: MemoryCandidateStatus
    workflow_version: int
    memory_type: MemoryType
    enrichment_status: EnrichmentStatus
    privacy_scope: PrivacyScope
    dispute_status: DisputeStatus
    unresolved_clarification_count: int
    finalized_memory_text: str | None = None
    user_message_excerpt: str
    created_at: datetime
    updated_at: datetime
    contributor_actor_id: str | None = None
    contributor_actor_role: FamilyMemoryActorRole | None = None
    contributor_relationship_to_owner: str | None = None
    promotion_id: int | None = None
    promotion_status: AvatarMemoryPromotionStatus | None = None
    searchable_as_fact: bool = False


class DemoFaChatMemoryCandidateSummaryListResponse(BaseModel):
    items: list[DemoFaChatMemoryCandidateSummary]
    total: int


class DemoFaChatMemoryCandidateReviewDetail(BaseModel):
    """Aggregated read model for the family memory review UI (Task 64.5, Part M).

    Combines existing candidate / enrichment / contribution / clarification /
    promotion reads plus a server-calculated preview of which owner-review and
    indexing actions are currently available, so the frontend never has to
    re-derive backend transition or eligibility rules. This is a read-only
    projection: the actual owner-review and indexing endpoints independently
    re-validate every transition, so this preview cannot itself grant access.
    """

    candidate: MemoryCandidateRead
    enrichment: CandidateEnrichmentRead | None = None
    contributions: list[FamilyMemoryContributionRead] = Field(default_factory=list)
    clarifications: list[ClarificationQuestionRead] = Field(default_factory=list)
    promotion: AvatarMemoryPromotionRead | None = None
    is_owner_actor: bool
    can_confirm: bool
    can_edit_and_confirm: bool
    can_reject: bool
    can_request_more_details: bool
    can_mark_disputed: bool
    can_approve_multiple_perspectives: bool
    can_index: bool
    blocked_reasons: list[str] = Field(default_factory=list)
    #: Bilingual read-model additions (Task 64.5.1). ``requested_locale`` is
    #: the locale the caller asked for (validated to "cs"/"ru");
    #: ``source_language`` is the candidate's actual source language.
    #: ``translations`` lists every current translation row for this
    #: candidate (finalized text + each contribution), so the Czech review
    #: UI can render a Czech/Russian comparison without extra round-trips.
    #: ``translation_block_reason`` mirrors the same backend-calculated
    #: eligibility gate used for promotion/indexing (never recomputed in
    #: React) - one of russian_translation_missing/failed/stale, or null.
    requested_locale: Literal["cs", "ru"] = "ru"
    source_language: str | None = None
    translations: list[MemoryContentTranslationRead] = Field(default_factory=list)
    translation_block_reason: str | None = None

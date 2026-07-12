from __future__ import annotations

from typing import Any

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
from app.modules.family_memory_enrichment.enums import (
    DisputeStatus,
    EnrichmentStatus,
    FamilyMemoryActorRole,
    MemoryType,
    PrivacyScope,
)
from app.modules.family_memory_enrichment.schemas import ClarificationQuestionRead


class DemoFaChatMessageRequest(BaseModel):
    profile_id: int | None = None
    message: str
    debug: bool | None = None
    active_memory_candidate_id: int | None = Field(default=None, gt=0)
    actor_id: str | None = Field(default=None, min_length=1, max_length=120)
    actor_role: FamilyMemoryActorRole | None = None
    relationship_to_owner: str | None = Field(default=None, max_length=120)

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

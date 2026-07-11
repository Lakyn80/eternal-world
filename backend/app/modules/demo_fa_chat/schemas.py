from __future__ import annotations

from pydantic import BaseModel

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


class DemoFaChatMessageRequest(BaseModel):
    profile_id: int | None = None
    message: str
    debug: bool | None = None


class DemoFaChatEvidenceItem(BaseModel):
    chunk_id: str
    source_id: int | None = None
    source_title: str | None = None
    score: float | None = None
    text_preview: str | None = None


class DemoFaChatMemoryCandidate(BaseModel):
    candidate_id: int | None = None
    status: MemoryCandidateStatus
    confidence: MemoryCandidateConfidence
    source: MemoryCandidateSource
    proposed_memory_text: str
    user_message_excerpt: str
    reason: str


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

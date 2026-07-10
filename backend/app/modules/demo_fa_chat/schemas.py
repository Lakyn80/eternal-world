from __future__ import annotations

from pydantic import BaseModel

from app.modules.avatar_persona.schemas import (
    AvatarEmotion,
    AvatarFaceDirectives,
    AvatarMemoryCandidate,
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


class DemoFaChatMessageResponse(BaseModel):
    answer: str
    lack_of_evidence: bool
    retrieval_used: bool
    persona_applied: bool
    guard_applied: bool
    guard_reason: str | None = None
    trace_id: str
    memory_candidate: AvatarMemoryCandidate | None = None
    emotion: AvatarEmotion | None = None
    face_directives: AvatarFaceDirectives | None = None
    voice_directives: AvatarVoiceDirectives | None = None
    evidence: list[DemoFaChatEvidenceItem]


class DemoFaChatErrorResponse(BaseModel):
    detail: str
    trace_id: str | None = None

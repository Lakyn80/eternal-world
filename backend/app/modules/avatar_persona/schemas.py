from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class AvatarSpeakingStyle(BaseModel):
    tone: str
    sentence_length: str
    addressing: list[str] = Field(default_factory=list)
    avoid: list[str] = Field(default_factory=list)


class AvatarEmotionalStyle(BaseModel):
    default_emotion: str
    sad_user_response: str
    trauma_topic_response: str
    family_topic_response: str


class AvatarLackOfEvidenceStyle(BaseModel):
    template: str


class AvatarPersonaProfile(BaseModel):
    avatar_id: str
    display_name: str
    role: str
    language: str
    core_traits: list[str] = Field(default_factory=list)
    life_background: list[str] = Field(default_factory=list)
    values: list[str] = Field(default_factory=list)
    speaking_style: AvatarSpeakingStyle
    emotional_style: AvatarEmotionalStyle
    boundaries: list[str] = Field(default_factory=list)
    lack_of_evidence_style: AvatarLackOfEvidenceStyle


class AvatarMemoryCandidate(BaseModel):
    status: Literal["needs_review"] = "needs_review"
    confidence: Literal["unverified"] = "unverified"
    source: Literal["conversation"] = "conversation"
    proposed_memory_text: str
    user_message_excerpt: str
    reason: str


class AvatarEmotion(BaseModel):
    primary: str
    intensity: float = Field(ge=0.0, le=1.0)


class AvatarFaceDirectives(BaseModel):
    expression: str
    gaze: str
    head_motion: str


class AvatarVoiceDirectives(BaseModel):
    tone: str
    pace: str
    volume: str


class AvatarResponseDirectives(BaseModel):
    emotion: AvatarEmotion
    face_directives: AvatarFaceDirectives
    voice_directives: AvatarVoiceDirectives

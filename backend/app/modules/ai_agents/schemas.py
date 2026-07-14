from __future__ import annotations

from datetime import date, datetime
from typing import Any

from pydantic import BaseModel, Field

from app.modules.ai_agents.brain.context import BrainGroundedContext
from app.modules.avatar_persona.schemas import AvatarPersonaProfile


class ChatHistoryEntry(BaseModel):
    role: str
    content: str
    created_at: datetime | None = None


class MemoryProfileContext(BaseModel):
    id: int
    name: str
    birth_date: date | None = None
    death_date: date | None = None
    biography: str | None = None
    personality: str | None = None
    catchphrases: str | None = None
    is_public: bool = False


class BrainAgentRequest(BaseModel):
    profile: MemoryProfileContext
    avatar_persona: AvatarPersonaProfile | None = None
    user_message: str
    recent_history: list[ChatHistoryEntry] = Field(default_factory=list)
    grounded_context: BrainGroundedContext | None = None
    output_guard_context: Any | None = None
    #: See ``OrchestratorChatRequest.response_language`` - threaded through so
    #: the provider layer/logs can see which language was requested, even
    #: though the actual instruction is baked into ``system_prompt`` by
    #: ``prompt_builder`` before this request is built.
    response_language: str | None = None
    system_prompt: str
    user_prompt: str
    prompt: str


class BrainAgentResponse(BaseModel):
    text: str
    provider_name: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class OrchestratorChatRequest(BaseModel):
    profile: MemoryProfileContext
    avatar_persona: AvatarPersonaProfile | None = None
    user_message: str
    recent_history: list[ChatHistoryEntry] = Field(default_factory=list)
    grounded_context: BrainGroundedContext | None = None
    output_guard_context: Any | None = None
    #: Explicit target language for the Brain's answer (e.g. "cs", "ru"),
    #: independent of what language the retrieved evidence text happens to
    #: be stored in. ``None`` (the default, used by every caller that does
    #: not set it - the generic authenticated chat endpoint and the RAG
    #: evaluation harness) preserves the pre-existing behavior of
    #: instructing the Brain to match the user's own message language.
    #: Set explicitly by demo_fa_chat for the bilingual Czech/Russian FA
    #: chat direct-locale architecture (no separate query/answer translation
    #: call - see demo_fa_chat.service.run_demo_fa_chat_message).
    response_language: str | None = None


class OrchestratorChatResponse(BaseModel):
    text: str
    audio_url: str | None = None
    video_url: str | None = None
    provider_name: str
    metadata: dict[str, Any] = Field(default_factory=dict)

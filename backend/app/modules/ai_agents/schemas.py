from __future__ import annotations

from datetime import date, datetime
from typing import Any

from pydantic import BaseModel, Field


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
    user_message: str
    recent_history: list[ChatHistoryEntry] = Field(default_factory=list)
    prompt: str


class BrainAgentResponse(BaseModel):
    text: str
    provider_name: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class OrchestratorChatRequest(BaseModel):
    profile: MemoryProfileContext
    user_message: str
    recent_history: list[ChatHistoryEntry] = Field(default_factory=list)


class OrchestratorChatResponse(BaseModel):
    text: str
    audio_url: str | None = None
    video_url: str | None = None
    provider_name: str
    metadata: dict[str, Any] = Field(default_factory=dict)

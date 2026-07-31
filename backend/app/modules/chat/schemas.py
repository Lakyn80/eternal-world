from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator

ChatLocale = Literal["cs", "en", "ru", "de"]


def normalize_message_text(value: str) -> str:
    normalized_value = value.strip()

    if not normalized_value:
        raise ValueError("message must not be empty")

    return normalized_value


class ChatMessageCreate(BaseModel):
    message: str = Field(max_length=4000)
    #: Optional UI locale hint used only when message-language detection fails.
    locale: ChatLocale | None = None

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        return normalize_message_text(value)


class ChatMessageRead(BaseModel):
    id: int
    profile_id: int | None
    role: str
    #: Display-facing text (user original; assistant viewer translation or canonical fallback).
    content: str
    source_language: str | None = None
    display_language: str | None = None
    display_translation_status: str | None = None
    created_at: datetime


class ChatSendResponse(BaseModel):
    message_id: int
    profile_id: int
    conversation_id: str
    #: Durable original user text (never overwritten by translation).
    user_message: str
    user_message_language: str | None = None
    #: Viewer-facing assistant text (translated when needed; canonical fallback).
    ai_response_text: str
    ai_response_language: str | None = None
    ai_response_translation_status: str | None = None
    audio_url: str | None
    video_url: str | None
    created_at: datetime


class ChatActiveRead(BaseModel):
    """Task 65.7 - the current active conversation's restorable transcript."""

    profile_id: int
    conversation_id: str
    messages: list[ChatMessageRead]
    restored_from: str  # "redis" | "database" | "empty"

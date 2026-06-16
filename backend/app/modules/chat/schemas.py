from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator


def normalize_message_text(value: str) -> str:
    normalized_value = value.strip()

    if not normalized_value:
        raise ValueError("message must not be empty")

    return normalized_value


class ChatMessageCreate(BaseModel):
    message: str = Field(max_length=4000)

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        return normalize_message_text(value)


class ChatMessageRead(BaseModel):
    id: int
    profile_id: int | None
    role: str
    content: str
    created_at: datetime


class ChatSendResponse(BaseModel):
    message_id: int
    profile_id: int
    user_message: str
    ai_response_text: str
    audio_url: str | None
    video_url: str | None
    created_at: datetime

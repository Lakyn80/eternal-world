from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import ChatMessage


def create_chat_message(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
    role: str,
    content: str,
    token_count: int | None = None,
    message_metadata: dict | None = None,
) -> ChatMessage:
    chat_message = ChatMessage(
        user_id=user_id,
        memory_profile_id=profile_id,
        role=role,
        content=content,
        token_count=token_count,
        message_metadata=message_metadata,
    )
    db.add(chat_message)
    return chat_message


def list_chat_messages_for_profile(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
) -> list[ChatMessage]:
    statement = (
        select(ChatMessage)
        .where(
            ChatMessage.user_id == user_id,
            ChatMessage.memory_profile_id == profile_id,
        )
        .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
    )
    return list(db.scalars(statement))


def list_recent_chat_messages_for_profile(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
    limit: int = 10,
) -> list[ChatMessage]:
    statement = (
        select(ChatMessage)
        .where(
            ChatMessage.user_id == user_id,
            ChatMessage.memory_profile_id == profile_id,
        )
        .order_by(ChatMessage.created_at.desc(), ChatMessage.id.desc())
        .limit(limit)
    )
    messages = list(db.scalars(statement))
    messages.reverse()
    return messages

"""Durable "which conversation is active" pointer (Task 65.7).

One row per (user, profile), tracking the current `conversation_id`.
`chat_messages` itself is never schema-changed - each message's existing
JSON `message_metadata` column carries `{"conversation_id": ...}`, so a
Postgres-side conversation-scoped query is just a JSON-key filter, not a
new join. See `db.models.ChatActiveSession` for the full rationale.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import ChatActiveSession


def get_active_session(db: Session, *, user_id: int, profile_id: int) -> ChatActiveSession | None:
    statement = select(ChatActiveSession).where(
        ChatActiveSession.user_id == user_id, ChatActiveSession.profile_id == profile_id
    )
    return db.scalar(statement)


def get_or_create_active_session(db: Session, *, user_id: int, profile_id: int) -> ChatActiveSession:
    session = get_active_session(db, user_id=user_id, profile_id=profile_id)
    if session is not None:
        return session
    session = ChatActiveSession(
        user_id=user_id,
        profile_id=profile_id,
        conversation_id=str(uuid.uuid4()),
    )
    db.add(session)
    db.flush()
    return session


def rotate_active_session(db: Session, *, user_id: int, profile_id: int) -> ChatActiveSession:
    """Reset: the same (user, profile) row is updated in place to a fresh
    `conversation_id` - prior messages remain fully readable via their own
    stamped `conversation_id`, they simply stop being "the active one"."""

    session = get_active_session(db, user_id=user_id, profile_id=profile_id)
    if session is None:
        return get_or_create_active_session(db, user_id=user_id, profile_id=profile_id)
    session.conversation_id = str(uuid.uuid4())
    session.started_at = datetime.now(timezone.utc)
    db.flush()
    return session

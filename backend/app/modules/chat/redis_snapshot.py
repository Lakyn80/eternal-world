"""Active-conversation Redis snapshot (Task 65.7, Part E).

PostgreSQL (`chat_messages`, unchanged) remains the durable record. Redis
holds a fast-restore snapshot of the CURRENT active conversation's ordered
transcript, keyed by (user, profile) - so returning to the Chat tab,
switching tabs, or refreshing the browser restores the visible transcript
without a full Postgres history re-fetch, and a Redis miss/failure falls
back to rebuilding the snapshot from Postgres rather than silently losing
messages (Part E.33).

Never stores provider API keys/secrets. Messages themselves ARE stored
(the task explicitly requires "questions and answers... present in Redis
as an active-session snapshot") - this is normal chat content, not a
credential; logging code must never print the snapshot body (see
`chat/service.py` - only counts/IDs are logged).
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone

from redis.exceptions import RedisError

from app.cache.redis_client import get_redis_client
from app.core.config import settings
from app.core.logging import get_logger, log_event
from app.core.metrics import observe_chat_redis_operation

_logger = get_logger("chat.redis_snapshot")

_KEY_PREFIX = "eternal_world:chat:active"

#: Sliding TTL - refreshed on every write, so an actively-used conversation
#: never falls out of Redis mid-session; an abandoned one eventually does
#: (harmless - `chat/service.get_active_chat` rebuilds from Postgres).
DEFAULT_TTL_SECONDS = 60 * 60 * 6


@dataclass(frozen=True)
class SnapshotMessage:
    id: int
    role: str
    content: str
    created_at: str


@dataclass(frozen=True)
class ChatSnapshot:
    conversation_id: str
    profile_id: int
    locale: str | None
    messages: list[SnapshotMessage] = field(default_factory=list)
    updated_at: str = ""


def _key(*, user_id: int, profile_id: int) -> str:
    return f"{_KEY_PREFIX}:{user_id}:{profile_id}"


def write_snapshot(*, user_id: int, profile_id: int, snapshot: ChatSnapshot) -> bool:
    payload = json.dumps(
        {
            "conversation_id": snapshot.conversation_id,
            "profile_id": snapshot.profile_id,
            "locale": snapshot.locale,
            "messages": [
                {"id": m.id, "role": m.role, "content": m.content, "created_at": m.created_at}
                for m in snapshot.messages
            ],
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    try:
        get_redis_client().set(_key(user_id=user_id, profile_id=profile_id), payload, ex=DEFAULT_TTL_SECONDS)
    except RedisError:
        log_event(_logger, logging.WARNING, "chat_redis_snapshot_restored", result="error", reason="redis_unavailable")
        observe_chat_redis_operation(operation="snapshot_written", result="error")
        return False
    observe_chat_redis_operation(operation="snapshot_written", result="success")
    return True


def read_snapshot(*, user_id: int, profile_id: int) -> ChatSnapshot | None:
    try:
        raw = get_redis_client().get(_key(user_id=user_id, profile_id=profile_id))
    except RedisError:
        observe_chat_redis_operation(operation="snapshot_restored", result="error")
        return None
    if raw is None:
        return None
    try:
        payload = json.loads(raw)
        messages = [
            SnapshotMessage(id=m["id"], role=m["role"], content=m["content"], created_at=m["created_at"])
            for m in payload.get("messages", [])
        ]
        snapshot = ChatSnapshot(
            conversation_id=payload["conversation_id"],
            profile_id=int(payload["profile_id"]),
            locale=payload.get("locale"),
            messages=messages,
            updated_at=payload.get("updated_at", ""),
        )
    except (ValueError, KeyError, TypeError):
        observe_chat_redis_operation(operation="snapshot_restored", result="error")
        return None
    observe_chat_redis_operation(operation="snapshot_restored", result="success")
    return snapshot


def append_message(*, user_id: int, profile_id: int, conversation_id: str, message: SnapshotMessage) -> None:
    """Best-effort append to the existing snapshot; if none exists yet (or
    it belongs to a stale conversation), a fresh one-message snapshot is
    started rather than raising - the durable Postgres row is what actually
    matters, this is only the fast-path cache."""

    existing = read_snapshot(user_id=user_id, profile_id=profile_id)
    if existing is None or existing.conversation_id != conversation_id:
        existing = ChatSnapshot(conversation_id=conversation_id, profile_id=profile_id, locale=None, messages=[])
    updated = ChatSnapshot(
        conversation_id=conversation_id,
        profile_id=profile_id,
        locale=existing.locale,
        messages=[*existing.messages, message],
    )
    write_snapshot(user_id=user_id, profile_id=profile_id, snapshot=updated)


def delete_snapshot(*, user_id: int, profile_id: int) -> None:
    try:
        get_redis_client().delete(_key(user_id=user_id, profile_id=profile_id))
    except RedisError:
        observe_chat_redis_operation(operation="reset", result="error")
        return
    observe_chat_redis_operation(operation="reset", result="success")

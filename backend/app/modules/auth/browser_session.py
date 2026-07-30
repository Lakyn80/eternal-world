"""Redis-backed browser session (Task 65.7).

Additive to, never a replacement for, the existing bearer-JWT
authentication (`app.core.security`) - Swagger/API/PowerShell clients keep
using `Authorization: Bearer <jwt>` exactly as before. This module backs a
second, browser-facing authentication path: an opaque session ID stored in
an HttpOnly cookie, resolved server-side against a Redis-held record. This
directly fixes the "login lost on navigation" and "profile edit races the
30-minute hard JWT expiry" defects (see PROJECT_PROGRESS.md Task 65.7):
navigating between routes/frontends never depended on any client-held
credential surviving a React remount, and the TTL is a sliding
inactivity window refreshed on every resolved request, not a hard expiry.

The session record itself lives only in Redis (no Postgres table) - it is
disposable, revocable, and safe to lose on a Redis restart (the user is
simply asked to log in again, same as today).
"""

from __future__ import annotations

import json
import logging
import secrets
from datetime import datetime, timezone

from redis.exceptions import RedisError

from app.cache.redis_client import get_redis_client
from app.core.config import settings
from app.core.logging import get_logger, log_event
from app.core.metrics import observe_browser_session_operation

_logger = get_logger("auth.browser_session")

_SESSION_KEY_PREFIX = "eternal_world:auth:session"


def _session_key(session_id: str) -> str:
    return f"{_SESSION_KEY_PREFIX}:{session_id}"


def create_browser_session(*, user_id: int, trace_id: str | None = None) -> str | None:
    """Creates a brand-new opaque session ID and stores it in Redis with a
    sliding TTL. Returns the raw session ID (the caller sets it as the
    cookie value - never logged, never returned in a JSON body).

    Returns ``None`` when Redis is unavailable. Browser sessions are additive
    to bearer JWT auth; Redis failure must not block API login for Swagger,
    PowerShell, CI, or any client that only needs ``access_token``.
    """

    session_id = secrets.token_urlsafe(32)
    payload = json.dumps({"user_id": user_id, "created_at": datetime.now(timezone.utc).isoformat()})
    try:
        get_redis_client().set(_session_key(session_id), payload, ex=settings.browser_session_ttl_seconds)
    except RedisError:
        log_event(_logger, logging.ERROR, "browser_session_invalid", trace_id=trace_id, reason="redis_unavailable")
        observe_browser_session_operation(operation="create", result="error")
        return None
    log_event(_logger, logging.INFO, "browser_session_created", trace_id=trace_id, user_id=user_id)
    observe_browser_session_operation(operation="create", result="success")
    return session_id


def resolve_browser_session(session_id: str | None, *, trace_id: str | None = None) -> int | None:
    """Resolves a session cookie value to a user ID, refreshing the sliding
    TTL on success. Returns `None` for any missing/expired/invalid/
    Redis-unavailable case - the caller treats that identically to "no
    session cookie sent" (falls through to a safe 401), never raising."""

    if not session_id:
        return None

    key = _session_key(session_id)
    try:
        raw = get_redis_client().get(key)
    except RedisError:
        log_event(_logger, logging.WARNING, "browser_session_invalid", trace_id=trace_id, reason="redis_unavailable")
        observe_browser_session_operation(operation="resume", result="error")
        return None

    if raw is None:
        log_event(_logger, logging.INFO, "browser_session_expired", trace_id=trace_id)
        observe_browser_session_operation(operation="resume", result="expired")
        return None

    try:
        payload = json.loads(raw)
        user_id = int(payload["user_id"])
    except (ValueError, KeyError, TypeError):
        log_event(_logger, logging.WARNING, "browser_session_invalid", trace_id=trace_id, reason="malformed_payload")
        observe_browser_session_operation(operation="resume", result="invalid")
        return None

    try:
        get_redis_client().expire(key, settings.browser_session_ttl_seconds)
    except RedisError:
        pass  # best-effort TTL refresh - resolution itself already succeeded

    log_event(_logger, logging.INFO, "browser_session_resumed", trace_id=trace_id, user_id=user_id)
    observe_browser_session_operation(operation="resume", result="success")
    return user_id


def rotate_browser_session(
    old_session_id: str | None, *, user_id: int, trace_id: str | None = None
) -> str | None:
    """Issues a fresh session ID and revokes the old one (if any) - used on
    login to avoid session fixation across repeated logins in the same
    browser. Returns ``None`` when Redis cannot store the new session."""

    if old_session_id:
        revoke_browser_session(old_session_id, trace_id=trace_id, _event="browser_session_rotated")
    return create_browser_session(user_id=user_id, trace_id=trace_id)


def revoke_browser_session(
    session_id: str | None, *, trace_id: str | None = None, _event: str = "browser_session_revoked"
) -> None:
    if not session_id:
        return
    try:
        get_redis_client().delete(_session_key(session_id))
    except RedisError:
        log_event(_logger, logging.WARNING, "browser_session_invalid", trace_id=trace_id, reason="redis_unavailable")
        observe_browser_session_operation(operation="revoke", result="error")
        return
    log_event(_logger, logging.INFO, _event, trace_id=trace_id)
    observe_browser_session_operation(operation="revoke", result="success")

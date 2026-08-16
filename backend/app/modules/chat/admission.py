"""Task 65.13.11 / 65.13.12 — Redis chat/LLM admission control.

Lease-based semaphores (ZSET + Lua) and atomic fixed-window rate limiting.
Task 65.13.12 keeps the sync Redis implementation and exposes async
context managers that bridge short Redis transactions via Starlette's
bounded threadpool (transitional technical debt — not a second admission
implementation).
"""

from __future__ import annotations

import threading
import time
import uuid
from contextlib import asynccontextmanager, contextmanager
from dataclasses import dataclass
from typing import AsyncIterator, Iterator, Protocol

from redis import Redis
from redis.exceptions import RedisError

from app.cache.redis_client import get_redis_client
from app.core.config import settings
from app.core.metrics import (
    observe_chat_admission_rejected,
    set_chat_brain_leases,
)
from app.modules.chat.async_bridge import run_sync_in_chat_bridge


#: Atomic fixed-window rate limit: INCR + EXPIRE in one script so a crash
#: between the two commands cannot leave a key without TTL.
RATE_LIMIT_LUA = """
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local current = redis.call('INCR', key)
if current == 1 then
  redis.call('EXPIRE', key, window)
end
if current > limit then
  return {0, current}
end
return {1, current}
"""

#: Lease-based semaphore. Expired members are purged before the limit check
#: so a crashed worker cannot permanently saturate capacity.
LEASE_ACQUIRE_LUA = """
local key = KEYS[1]
local now = tonumber(ARGV[1])
local expires_at = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])
local lease_id = ARGV[4]
redis.call('ZREMRANGEBYSCORE', key, '-inf', now)
local count = redis.call('ZCARD', key)
if count >= limit then
  return {0, count}
end
redis.call('ZADD', key, expires_at, lease_id)
local ttl_ms = math.floor((expires_at - now + 5) * 1000)
if ttl_ms < 1000 then
  ttl_ms = 1000
end
redis.call('PEXPIRE', key, ttl_ms)
return {1, count + 1}
"""

LEASE_RELEASE_LUA = """
local key = KEYS[1]
local lease_id = ARGV[1]
redis.call('ZREM', key, lease_id)
return redis.call('ZCARD', key)
"""


class ChatAdmissionRateLimitedError(Exception):
    def __init__(self, *, retry_after_seconds: int, reason: str = "rate_limited") -> None:
        self.retry_after_seconds = retry_after_seconds
        self.reason = reason
        super().__init__("Chat rate limit exceeded. Please try again shortly.")


class ChatAdmissionUserBusyError(Exception):
    def __init__(self, *, retry_after_seconds: int) -> None:
        self.retry_after_seconds = retry_after_seconds
        self.reason = "user_inflight"
        super().__init__("A chat request is already in progress for this account.")


class ChatAdmissionSaturatedError(Exception):
    def __init__(self, *, retry_after_seconds: int, reason: str = "brain_saturated") -> None:
        self.retry_after_seconds = retry_after_seconds
        self.reason = reason
        super().__init__("Chat capacity is temporarily saturated. Please try again shortly.")


class ChatAdmissionUnavailableError(Exception):
    def __init__(self, *, retry_after_seconds: int) -> None:
        self.retry_after_seconds = retry_after_seconds
        self.reason = "admission_unavailable"
        super().__init__("Chat admission control is temporarily unavailable.")


class ChatProviderUnavailableError(Exception):
    """Mapped from known Brain provider timeout / upstream overload only."""

    def __init__(self, *, retry_after_seconds: int, message: str) -> None:
        self.retry_after_seconds = retry_after_seconds
        self.reason = "provider_unavailable"
        super().__init__(message)


@dataclass(frozen=True)
class _LeaseHandle:
    key: str
    lease_id: str


class _RedisLike(Protocol):
    def eval(self, script: str, numkeys: int, *keys_and_args: object) -> object: ...


def _now() -> float:
    return time.time()


def _lease_ttl_seconds() -> float:
    return float(settings.ai_brain_timeout_seconds) + float(settings.chat_lease_ttl_margin_seconds)


def _retry_after() -> int:
    return int(settings.chat_overload_retry_after_seconds)


def rate_limit_key(*, bucket: str) -> str:
    return f"ew:chat:rl:{bucket}"


def user_lease_key(*, user_id: int) -> str:
    return f"ew:chat:user:leases:{user_id}"


def brain_lease_key() -> str:
    return "ew:chat:brain:leases"


def demo_rate_bucket(*, client_key: str) -> str:
    return f"demo:{client_key}"


def _eval_pair(client: _RedisLike, script: str, keys: list[str], args: list[object]) -> tuple[int, int]:
    raw = client.eval(script, len(keys), *(keys + args))
    if not isinstance(raw, (list, tuple)) or len(raw) < 2:
        raise ChatAdmissionUnavailableError(retry_after_seconds=_retry_after())
    return int(raw[0]), int(raw[1])


def _acquire_rate_limit(client: _RedisLike, *, bucket: str, limit: int) -> None:
    ok, _current = _eval_pair(
        client,
        RATE_LIMIT_LUA,
        [rate_limit_key(bucket=bucket)],
        [int(limit), 60],
    )
    if ok != 1:
        observe_chat_admission_rejected(reason="rate_limited")
        raise ChatAdmissionRateLimitedError(retry_after_seconds=_retry_after())


def _acquire_lease(
    client: _RedisLike,
    *,
    key: str,
    limit: int,
    reject_exc: Exception,
) -> _LeaseHandle:
    lease_id = uuid.uuid4().hex
    now = _now()
    expires_at = now + _lease_ttl_seconds()
    ok, active = _eval_pair(
        client,
        LEASE_ACQUIRE_LUA,
        [key],
        [now, expires_at, int(limit), lease_id],
    )
    if ok != 1:
        raise reject_exc
    if key == brain_lease_key():
        set_chat_brain_leases(active)
    return _LeaseHandle(key=key, lease_id=lease_id)


def _release_lease(client: _RedisLike, handle: _LeaseHandle | None) -> None:
    if handle is None:
        return
    try:
        remaining = client.eval(LEASE_RELEASE_LUA, 1, handle.key, handle.lease_id)
        if handle.key == brain_lease_key():
            set_chat_brain_leases(int(remaining or 0))
    except RedisError:
        # Lease TTL will free the slot; never raise from release.
        return


def _client() -> Redis:
    return get_redis_client()


@contextmanager
def user_chat_admission(
    *,
    user_id: int,
    rate_limit_per_minute: int,
) -> Iterator[None]:
    """Rate limit + per-user inflight lease (held for the whole request including RAG)."""

    if not settings.chat_admission_enabled:
        yield
        return

    client: _RedisLike
    user_handle: _LeaseHandle | None = None
    try:
        client = _client()
        _acquire_rate_limit(
            client,
            bucket=f"user:{user_id}",
            limit=rate_limit_per_minute,
        )
        try:
            user_handle = _acquire_lease(
                client,
                key=user_lease_key(user_id=user_id),
                limit=int(settings.chat_max_inflight_per_user),
                reject_exc=ChatAdmissionUserBusyError(retry_after_seconds=_retry_after()),
            )
        except ChatAdmissionUserBusyError:
            observe_chat_admission_rejected(reason="user_inflight")
            raise
    except (ChatAdmissionRateLimitedError, ChatAdmissionUserBusyError):
        raise
    except RedisError:
        observe_chat_admission_rejected(reason="admission_unavailable")
        raise ChatAdmissionUnavailableError(retry_after_seconds=_retry_after()) from None
    except ChatAdmissionUnavailableError:
        observe_chat_admission_rejected(reason="admission_unavailable")
        raise

    try:
        yield
    finally:
        _release_lease(client, user_handle)


@contextmanager
def brain_chat_admission() -> Iterator[None]:
    """Global Brain/LLM lease — acquire only around the provider call, not RAG."""

    if not settings.chat_admission_enabled:
        yield
        return

    client: _RedisLike
    handle: _LeaseHandle | None = None
    try:
        client = _client()
        handle = _acquire_lease(
            client,
            key=brain_lease_key(),
            limit=int(settings.chat_max_global_brain_inflight),
            reject_exc=ChatAdmissionSaturatedError(retry_after_seconds=_retry_after()),
        )
    except ChatAdmissionSaturatedError:
        observe_chat_admission_rejected(reason="brain_saturated")
        raise
    except RedisError:
        observe_chat_admission_rejected(reason="admission_unavailable")
        raise ChatAdmissionUnavailableError(retry_after_seconds=_retry_after()) from None

    try:
        yield
    finally:
        _release_lease(client, handle)


@contextmanager
def demo_rate_admission(*, client_key: str) -> Iterator[None]:
    """Demo FA chat rate bucket only (Brain lease is acquired after RAG)."""

    if not settings.chat_admission_enabled:
        yield
        return

    try:
        client = _client()
        _acquire_rate_limit(
            client,
            bucket=demo_rate_bucket(client_key=client_key),
            limit=int(settings.chat_rate_limit_demo_per_minute),
        )
    except ChatAdmissionRateLimitedError:
        raise
    except RedisError:
        observe_chat_admission_rejected(reason="admission_unavailable")
        raise ChatAdmissionUnavailableError(retry_after_seconds=_retry_after()) from None
    yield


@contextmanager
def demo_chat_admission(*, client_key: str) -> Iterator[None]:
    """Convenience: demo rate then Brain lease (use only when no RAG precedes LLM)."""

    with demo_rate_admission(client_key=client_key):
        with brain_chat_admission():
            yield


def resolve_user_chat_rate_limit(*, allow_unlimited_chat: bool) -> int:
    if allow_unlimited_chat:
        return int(settings.chat_rate_limit_per_user_per_minute)
    return int(settings.chat_rate_limit_limited_plan_per_minute)


@asynccontextmanager
async def async_user_chat_admission(
    *,
    user_id: int,
    rate_limit_per_minute: int,
) -> AsyncIterator[None]:
    """Async wrapper: sync Redis admission runs in the chat bridge executor."""

    cm = user_chat_admission(user_id=user_id, rate_limit_per_minute=rate_limit_per_minute)
    await run_sync_in_chat_bridge(cm.__enter__, operation="admission")
    try:
        yield
    finally:
        await run_sync_in_chat_bridge(cm.__exit__, None, None, None, operation="admission")


@asynccontextmanager
async def async_brain_chat_admission() -> AsyncIterator[None]:
    """Async wrapper around global Brain lease acquire/release."""

    cm = brain_chat_admission()
    await run_sync_in_chat_bridge(cm.__enter__, operation="admission")
    try:
        yield
    finally:
        await run_sync_in_chat_bridge(cm.__exit__, None, None, None, operation="admission")


@asynccontextmanager
async def async_demo_rate_admission(*, client_key: str) -> AsyncIterator[None]:
    """Async wrapper around the demo rate-limit bucket."""

    cm = demo_rate_admission(client_key=client_key)
    await run_sync_in_chat_bridge(cm.__enter__, operation="admission")
    try:
        yield
    finally:
        await run_sync_in_chat_bridge(cm.__exit__, None, None, None, operation="admission")


def map_brain_provider_error(exc: BaseException) -> ChatProviderUnavailableError | None:
    """Map only known overload/timeout provider errors; leave bugs as real 5xx."""

    from app.modules.ai_agents.brain.provider import BrainProviderRequestError

    if not isinstance(exc, BrainProviderRequestError):
        return None
    message = str(exc)
    lowered = message.lower()
    if (
        "timed out" in lowered
        or "timeout" in lowered
        or "http 429" in lowered
        or "http 503" in lowered
    ):
        return ChatProviderUnavailableError(
            retry_after_seconds=_retry_after(),
            message="The AI provider is temporarily unavailable. Please try again shortly.",
        )
    return None


# ---------------------------------------------------------------------------
# Hermetic in-memory Redis for tests (mirrors the Lua contracts above).
# ---------------------------------------------------------------------------


class InMemoryAdmissionRedis:
    """Minimal Redis stand-in supporting the admission Lua scripts via eval.

    A re-entrant lock serializes ``eval`` so concurrent tests observe the same
    single-threaded atomicity Redis provides for Lua scripts (Task 65.13.11A).
    """

    def __init__(self) -> None:
        self._strings: dict[str, int] = {}
        self._string_expiry: dict[str, float] = {}
        self._zsets: dict[str, dict[str, float]] = {}
        self._lock = threading.RLock()

    def eval(self, script: str, numkeys: int, *keys_and_args: object) -> object:
        with self._lock:
            keys = [str(keys_and_args[i]) for i in range(numkeys)]
            args = list(keys_and_args[numkeys:])
            if script.strip() == RATE_LIMIT_LUA.strip():
                return self._rate_limit(keys[0], int(args[0]), int(args[1]))
            if script.strip() == LEASE_ACQUIRE_LUA.strip():
                return self._lease_acquire(
                    keys[0],
                    float(args[0]),
                    float(args[1]),
                    int(args[2]),
                    str(args[3]),
                )
            if script.strip() == LEASE_RELEASE_LUA.strip():
                return self._lease_release(keys[0], str(args[0]))
            raise NotImplementedError("Unsupported Lua script in InMemoryAdmissionRedis")

    def _purge_string_if_expired(self, key: str) -> None:
        expires = self._string_expiry.get(key)
        if expires is not None and _now() >= expires:
            self._strings.pop(key, None)
            self._string_expiry.pop(key, None)

    def _rate_limit(self, key: str, limit: int, window: int) -> list[int]:
        self._purge_string_if_expired(key)
        current = self._strings.get(key, 0) + 1
        self._strings[key] = current
        if current == 1:
            self._string_expiry[key] = _now() + float(window)
        if current > limit:
            return [0, current]
        return [1, current]

    def _lease_acquire(
        self,
        key: str,
        now: float,
        expires_at: float,
        limit: int,
        lease_id: str,
    ) -> list[int]:
        zset = self._zsets.setdefault(key, {})
        for member, score in list(zset.items()):
            if score <= now:
                del zset[member]
        if len(zset) >= limit:
            return [0, len(zset)]
        zset[lease_id] = expires_at
        return [1, len(zset)]

    def _lease_release(self, key: str, lease_id: str) -> int:
        zset = self._zsets.setdefault(key, {})
        zset.pop(lease_id, None)
        return len(zset)

"""Task 65.13.11 — chat admission control (lease semaphore + atomic rate)."""

from __future__ import annotations

import time

import pytest

from app.core.config import settings
from app.modules.ai_agents.brain.provider import BrainProviderRequestError
from app.modules.chat import admission
from app.modules.chat.admission import (
    ChatAdmissionRateLimitedError,
    ChatAdmissionSaturatedError,
    ChatAdmissionUserBusyError,
    ChatProviderUnavailableError,
    InMemoryAdmissionRedis,
    brain_chat_admission,
    map_brain_provider_error,
    resolve_user_chat_rate_limit,
    user_chat_admission,
)


@pytest.fixture
def store(monkeypatch):
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    return memory


def test_atomic_rate_limit_rejects_after_limit(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 2)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10)
    with user_chat_admission(user_id=1, rate_limit_per_minute=2):
        pass
    with user_chat_admission(user_id=1, rate_limit_per_minute=2):
        pass
    with pytest.raises(ChatAdmissionRateLimitedError) as exc:
        with user_chat_admission(user_id=1, rate_limit_per_minute=2):
            pass
    assert exc.value.retry_after_seconds > 0


def test_user_inflight_lease_blocks_second_concurrent(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 1)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 100)

    with user_chat_admission(user_id=7, rate_limit_per_minute=100):
        with pytest.raises(ChatAdmissionUserBusyError):
            with user_chat_admission(user_id=7, rate_limit_per_minute=100):
                pass


def test_brain_lease_saturation_and_release(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    with brain_chat_admission():
        with pytest.raises(ChatAdmissionSaturatedError):
            with brain_chat_admission():
                pass
    # After release, capacity is available again.
    with brain_chat_admission():
        pass


def test_expired_brain_lease_frees_capacity_without_explicit_release(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    monkeypatch.setattr(settings, "ai_brain_timeout_seconds", 0.01)
    monkeypatch.setattr(settings, "chat_lease_ttl_margin_seconds", 0.01)

    with brain_chat_admission():
        # Intentionally leave the lease to expire by sleeping past TTL while
        # still "holding" the context — simulate crash by releasing via TTL
        # on the next acquire after we exit without waiting... Instead:
        pass

    # Force a stale lease member directly, then acquire should purge it.
    key = admission.brain_lease_key()
    store._zsets[key] = {"stale-lease": time.time() - 10}
    with brain_chat_admission():
        pass
    assert "stale-lease" not in store._zsets.get(key, {})


def test_brain_lease_not_required_during_rag_phase(store, monkeypatch):
    """User admission may run while all Brain slots are taken (RAG phase)."""

    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 2)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 100)

    with brain_chat_admission():
        # RAG-equivalent work under user admission must still be allowed.
        with user_chat_admission(user_id=3, rate_limit_per_minute=100):
            pass
        with pytest.raises(ChatAdmissionSaturatedError):
            with brain_chat_admission():
                pass


def test_map_brain_provider_error_only_overload_classes():
    timeout = BrainProviderRequestError("OpenAI-compatible provider request timed out")
    mapped = map_brain_provider_error(timeout)
    assert isinstance(mapped, ChatProviderUnavailableError)

    upstream = BrainProviderRequestError("OpenAI-compatible provider returned HTTP 429")
    assert map_brain_provider_error(upstream) is not None

    other = BrainProviderRequestError("OpenAI-compatible provider returned HTTP 400")
    assert map_brain_provider_error(other) is None
    assert map_brain_provider_error(ValueError("bug")) is None


def test_resolve_user_chat_rate_limit_plan_aware(monkeypatch):
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 10)
    monkeypatch.setattr(settings, "chat_rate_limit_limited_plan_per_minute", 5)
    assert resolve_user_chat_rate_limit(allow_unlimited_chat=True) == 10
    assert resolve_user_chat_rate_limit(allow_unlimited_chat=False) == 5


def test_chat_send_rate_limit_returns_429(client, monkeypatch):
    # Dedicated store + forced limit so this HTTP test cannot flake against
    # leftover unit-test monkeypatches or shared Redis keys.
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    monkeypatch.setattr(admission, "resolve_user_chat_rate_limit", lambda **kwargs: 1)
    monkeypatch.setattr(
        "app.modules.chat.service.resolve_user_chat_rate_limit",
        lambda **kwargs: 1,
    )

    password = "StrongPass123"
    email = "admission-rate@example.com"
    client.post(
        "/api/auth/register",
        json={"email": email, "password": password, "full_name": "Rate User"},
    )
    token = client.post("/api/auth/login", json={"email": email, "password": password}).json()[
        "access_token"
    ]
    profile_id = client.post(
        "/api/memory-profiles",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "P", "canonical_language": "cs", "confirm_canonical_language": True},
    ).json()["id"]

    first = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "prvni"},
    )
    assert first.status_code == 200, first.text

    second = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "druha"},
    )
    assert second.status_code == 429, second.text
    assert second.headers.get("Retry-After") is not None


def test_chat_send_brain_saturation_returns_503(client, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    monkeypatch.setattr(settings, "chat_rate_limit_limited_plan_per_minute", 100)

    password = "StrongPass123"
    email = "admission-sat@example.com"
    client.post(
        "/api/auth/register",
        json={"email": email, "password": password, "full_name": "Sat User"},
    )
    token = client.post("/api/auth/login", json={"email": email, "password": password}).json()[
        "access_token"
    ]
    profile_id = client.post(
        "/api/memory-profiles",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "P", "canonical_language": "cs", "confirm_canonical_language": True},
    ).json()["id"]

    # Hold the single global Brain lease while a chat request tries to enter.
    with brain_chat_admission():
        response = client.post(
            f"/api/chat/{profile_id}/messages",
            headers={"Authorization": f"Bearer {token}"},
            json={"message": "Ahoj"},
        )
    assert response.status_code == 503
    assert response.headers.get("Retry-After") is not None

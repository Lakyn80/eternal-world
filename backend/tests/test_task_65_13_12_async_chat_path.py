"""Task 65.13.12 — true async chat path (Brain await + admission preserved)."""

from __future__ import annotations

import asyncio
import inspect
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx
import pytest

from app.core.config import settings
from app.modules.ai_agents.brain.async_http import (
    aclose_shared_brain_async_http_client,
    get_shared_brain_async_http_client,
    reset_shared_brain_async_http_client_for_tests,
)
from app.modules.ai_agents.brain.provider import BrainProviderRequestError
from app.modules.ai_agents.brain.providers.mock import MockBrainAgentProvider
from app.modules.ai_agents.brain.providers.openai_compatible import (
    OpenAICompatibleBrainAgentProvider,
)
from app.modules.ai_agents.schemas import BrainAgentRequest, MemoryProfileContext
from app.modules.chat import admission, router as chat_router
from app.modules.chat.admission import (
    ChatAdmissionSaturatedError,
    InMemoryAdmissionRedis,
    async_brain_chat_admission,
    map_brain_provider_error,
)


def _brain_request() -> BrainAgentRequest:
    return BrainAgentRequest(
        profile=MemoryProfileContext(id=1, name="Ada"),
        user_message="hello",
        recent_history=[],
        grounded_context=None,
        system_prompt="sys",
        user_prompt="user",
        prompt="sys\n\n---\n\nuser",
    )


@pytest.fixture(autouse=True)
def _reset_async_http_client():
    reset_shared_brain_async_http_client_for_tests()
    yield
    reset_shared_brain_async_http_client_for_tests()


@pytest.fixture
def store(monkeypatch):
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    return memory


def test_chat_send_route_is_async():
    assert inspect.iscoroutinefunction(chat_router.send_message)


def test_provider_async_awaits_httpx_async_client():
    async def _run():
        calls: list[str] = []

        async def handler(request: httpx.Request) -> httpx.Response:
            calls.append("awaited")
            await asyncio.sleep(0.05)
            return httpx.Response(
                200,
                json={
                    "id": "req-async-1",
                    "model": "test-model",
                    "choices": [{"message": {"content": "async-ok"}}],
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
                },
            )

        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(transport=transport) as client:
            provider = OpenAICompatibleBrainAgentProvider(
                model="test-model",
                api_key="test-key",
                base_url="https://example.test/v1",
                timeout_seconds=5.0,
                async_http_client=client,
            )
            response = await provider.generate_response_async(_brain_request())

        assert response.text == "async-ok"
        assert calls == ["awaited"]

    asyncio.run(_run())


def test_async_provider_path_does_not_use_sync_httpx_client():
    async def _run():
        class BoomClient:
            def __enter__(self):
                raise AssertionError("sync httpx.Client must not run on async path")

            def __exit__(self, *args):
                return False

            def post(self, *args, **kwargs):
                raise AssertionError("sync post must not run on async path")

        async def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                200,
                json={
                    "choices": [{"message": {"content": "ok"}}],
                    "model": "m",
                    "usage": {},
                },
            )

        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(transport=transport) as client:
            provider = OpenAICompatibleBrainAgentProvider(
                model="m",
                api_key="k",
                base_url="https://example.test/v1",
                timeout_seconds=5.0,
                http_client_factory=lambda _t: BoomClient(),
                async_http_client=client,
            )
            result = await provider.generate_response_async(_brain_request())
        assert result.text == "ok"

    asyncio.run(_run())


def test_shared_async_client_reused():
    async def _run():
        first = await get_shared_brain_async_http_client(timeout_seconds=5.0)
        second = await get_shared_brain_async_http_client(timeout_seconds=5.0)
        assert first is second
        await aclose_shared_brain_async_http_client()

    asyncio.run(_run())


def test_async_provider_timeout_maps_to_request_error():
    async def _run():
        async def handler(request: httpx.Request) -> httpx.Response:
            raise httpx.ReadTimeout("slow", request=request)

        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(transport=transport) as client:
            provider = OpenAICompatibleBrainAgentProvider(
                model="m",
                api_key="k",
                base_url="https://example.test/v1",
                timeout_seconds=0.1,
                async_http_client=client,
            )
            with pytest.raises(BrainProviderRequestError, match="timed out"):
                await provider.generate_response_async(_brain_request())

    asyncio.run(_run())


def test_async_provider_upstream_429_maps():
    async def _run():
        async def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(429, request=request)

        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(transport=transport) as client:
            provider = OpenAICompatibleBrainAgentProvider(
                model="m",
                api_key="k",
                base_url="https://example.test/v1",
                timeout_seconds=5.0,
                async_http_client=client,
            )
            with pytest.raises(BrainProviderRequestError, match="HTTP 429"):
                await provider.generate_response_async(_brain_request())

    asyncio.run(_run())
    mapped = map_brain_provider_error(
        BrainProviderRequestError("OpenAI-compatible provider returned HTTP 429")
    )
    assert mapped is not None


def test_valueerror_not_mapped_as_overload():
    assert map_brain_provider_error(ValueError("bug")) is None


def test_mock_provider_async_compatibility():
    async def _run():
        text = (await MockBrainAgentProvider().generate_response_async(_brain_request())).text
        assert "mock reply" in text

    asyncio.run(_run())


def test_brain_lease_releases_on_successful_await(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)

    async def _run():
        async with async_brain_chat_admission():
            await asyncio.sleep(0.01)
        async with async_brain_chat_admission():
            pass

    asyncio.run(_run())


def test_brain_lease_releases_on_provider_exception(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)

    async def _run():
        with pytest.raises(RuntimeError, match="provider boom"):
            async with async_brain_chat_admission():
                raise RuntimeError("provider boom")
        async with async_brain_chat_admission():
            pass

    asyncio.run(_run())


def test_brain_lease_releases_on_cancellation(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)

    async def _run():
        entered = asyncio.Event()

        async def holder():
            async with async_brain_chat_admission():
                entered.set()
                await asyncio.sleep(60)

        task = asyncio.create_task(holder())
        await entered.wait()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        async with async_brain_chat_admission():
            pass

    asyncio.run(_run())


def test_event_loop_responsive_while_fake_brain_waits():
    """Heartbeat must continue while a fake async Brain await is in progress."""

    async def _run():
        heartbeat_times: list[float] = []
        stop = asyncio.Event()

        async def heartbeat():
            while not stop.is_set():
                heartbeat_times.append(time.perf_counter())
                await asyncio.sleep(0.05)

        async def fake_brain():
            await asyncio.sleep(0.5)

        hb_task = asyncio.create_task(heartbeat())
        started = time.perf_counter()
        await asyncio.gather(fake_brain(), fake_brain())
        stop.set()
        await hb_task

        elapsed = time.perf_counter() - started
        assert elapsed >= 0.45
        assert len(heartbeat_times) >= 6
        intervals = [
            heartbeat_times[i + 1] - heartbeat_times[i]
            for i in range(len(heartbeat_times) - 1)
        ]
        max_delay = max(intervals) if intervals else 0.0
        assert max_delay < 0.25, f"event loop stalled: max_heartbeat_delay={max_delay}"
        return {
            "heartbeat_count": len(heartbeat_times),
            "max_heartbeat_delay": max_delay,
            "expected_interval": 0.05,
        }

    result = asyncio.run(_run())
    assert result["heartbeat_count"] >= 6


def test_threadpool_bridge_runs_off_event_loop_thread():
    from app.modules.chat.async_bridge import run_sync_in_chat_bridge

    async def _run():
        loop_thread = threading.current_thread().ident
        worker_thread = {"id": None}

        def _blocking():
            worker_thread["id"] = threading.current_thread().ident
            return 42

        assert await run_sync_in_chat_bridge(_blocking, operation="db") == 42
        assert worker_thread["id"] is not None
        assert worker_thread["id"] != loop_thread

    asyncio.run(_run())


def test_async_global_cap_bounds_concurrent_awaits(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 3)

    async def _run():
        inflight = {"n": 0, "max": 0}
        lock = asyncio.Lock()

        async def one():
            try:
                async with async_brain_chat_admission():
                    async with lock:
                        inflight["n"] += 1
                        inflight["max"] = max(inflight["max"], inflight["n"])
                    await asyncio.sleep(0.1)
                    async with lock:
                        inflight["n"] -= 1
                return "ok"
            except ChatAdmissionSaturatedError:
                return "saturated"

        results = await asyncio.gather(*[one() for _ in range(20)])
        assert inflight["max"] <= 3
        assert results.count("ok") >= 3
        assert results.count("saturated") >= 1
        async with async_brain_chat_admission():
            async with async_brain_chat_admission():
                async with async_brain_chat_admission():
                    pass
        return inflight["max"]

    assert asyncio.run(_run()) <= 3


def test_sync_generate_response_still_works_for_non_chat_consumers():
    class FakeClient:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def post(self, url, *, headers, json):
            request = httpx.Request("POST", url)
            return httpx.Response(
                200,
                request=request,
                json={
                    "choices": [{"message": {"content": "sync-ok"}}],
                    "model": "m",
                },
            )

    provider = OpenAICompatibleBrainAgentProvider(
        model="m",
        api_key="k",
        base_url="https://example.test/v1",
        timeout_seconds=5.0,
        http_client_factory=lambda _t: FakeClient(),
    )
    assert provider.generate_response(_brain_request()).text == "sync-ok"


def test_chat_send_still_success_via_http(client, monkeypatch):
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    password = "StrongPass123"
    email = "async-chat-ok@example.com"
    client.post(
        "/api/auth/register",
        json={"email": email, "password": password, "full_name": "Async User"},
    )
    token = client.post("/api/auth/login", json={"email": email, "password": password}).json()[
        "access_token"
    ]
    profile_id = client.post(
        "/api/memory-profiles",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "P", "canonical_language": "cs", "confirm_canonical_language": True},
    ).json()["id"]
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "ahoj"},
    )
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["ai_response_text"]
    assert body["conversation_id"]


def test_sessions_not_shared_across_concurrent_async_prepares(client, monkeypatch):
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 100)
    monkeypatch.setattr(
        "app.modules.chat.service.resolve_user_chat_rate_limit",
        lambda **kwargs: 100,
    )

    users = []
    for idx in range(2):
        email = f"async-session-{idx}@example.com"
        password = "StrongPass123"
        client.post(
            "/api/auth/register",
            json={"email": email, "password": password, "full_name": f"U{idx}"},
        )
        token = client.post("/api/auth/login", json={"email": email, "password": password}).json()[
            "access_token"
        ]
        profile_id = client.post(
            "/api/memory-profiles",
            headers={"Authorization": f"Bearer {token}"},
            json={"name": f"P{idx}", "canonical_language": "cs", "confirm_canonical_language": True},
        ).json()["id"]
        users.append((token, profile_id))

    def send(pair):
        token, profile_id = pair
        return client.post(
            f"/api/chat/{profile_id}/messages",
            headers={"Authorization": f"Bearer {token}"},
            json={"message": "concurrent"},
        ).status_code

    with ThreadPoolExecutor(max_workers=2) as pool:
        codes = [fut.result() for fut in as_completed([pool.submit(send, u) for u in users])]
    assert sorted(codes) == [200, 200]

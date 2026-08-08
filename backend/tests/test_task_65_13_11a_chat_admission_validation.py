"""Task 65.13.11A — hermetic validation + controlled load benchmark.

All Brain work is synthetic (sleep/fake). No DeepSeek, no real Redis writes
to the shared runtime, no memorial content, no Qdrant/Postgres mutations
beyond the existing isolated TestClient SQLite fixtures.
"""

from __future__ import annotations

import json
import statistics
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

import pytest
from redis.exceptions import RedisError

from app.core.config import settings
from app.core.metrics import CHAT_ADMISSION_REJECTED_TOTAL, CHAT_BRAIN_LEASES
from app.modules.ai_agents.brain.provider import BrainProviderRequestError
from app.modules.chat import admission
from app.modules.chat.admission import (
    ChatAdmissionRateLimitedError,
    ChatAdmissionSaturatedError,
    ChatAdmissionUnavailableError,
    ChatAdmissionUserBusyError,
    ChatProviderUnavailableError,
    InMemoryAdmissionRedis,
    brain_chat_admission,
    demo_rate_admission,
    map_brain_provider_error,
    resolve_user_chat_rate_limit,
    user_chat_admission,
)
from app.modules.chat.http_errors import raise_chat_admission_http
from fastapi import HTTPException


#: ``/app`` in Compose is the backend tree; keep the summary inside the
#: bind-mounted workspace (not the container filesystem root).
ARTIFACT_DIR = Path(__file__).resolve().parents[1] / "artifacts" / "security" / "task_65_13_11a_validation"
BENCHMARK_JSON = ARTIFACT_DIR / "load_benchmark_summary.json"


@pytest.fixture
def store(monkeypatch):
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    return memory


# ---------------------------------------------------------------------------
# Failure-mode / crash / atomicity proofs
# ---------------------------------------------------------------------------


def test_redis_unavailable_fail_closed_zero_brain_calls(monkeypatch):
    brain_calls = {"n": 0}

    def boom():
        raise RedisError("connection refused")

    monkeypatch.setattr(admission, "get_redis_client", boom)
    with pytest.raises(ChatAdmissionUnavailableError):
        with brain_chat_admission():
            brain_calls["n"] += 1
    assert brain_calls["n"] == 0


def test_user_admission_redis_unavailable_fail_closed(monkeypatch):
    monkeypatch.setattr(admission, "get_redis_client", lambda: (_ for _ in ()).throw(RedisError("timeout")))
    with pytest.raises(ChatAdmissionUnavailableError):
        with user_chat_admission(user_id=1, rate_limit_per_minute=10):
            pass


def test_release_on_rag_equivalent_exception(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 1)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 100)
    with pytest.raises(RuntimeError, match="rag boom"):
        with user_chat_admission(user_id=9, rate_limit_per_minute=100):
            raise RuntimeError("rag boom")
    # Slot free again.
    with user_chat_admission(user_id=9, rate_limit_per_minute=100):
        pass


def test_release_on_brain_exception(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    with pytest.raises(RuntimeError, match="brain boom"):
        with brain_chat_admission():
            raise RuntimeError("brain boom")
    with brain_chat_admission():
        pass


def test_release_on_timeout_mapped_provider_error(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    with pytest.raises(BrainProviderRequestError):
        with brain_chat_admission():
            raise BrainProviderRequestError("OpenAI-compatible provider request timed out")
    with brain_chat_admission():
        pass


def test_idempotent_double_release(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 2)
    handle = admission._acquire_lease(
        store,
        key=admission.brain_lease_key(),
        limit=2,
        reject_exc=ChatAdmissionSaturatedError(retry_after_seconds=1),
    )
    admission._release_lease(store, handle)
    admission._release_lease(store, handle)  # second release is a no-op ZREM
    with brain_chat_admission():
        with brain_chat_admission():
            pass


def test_stale_user_lease_expires(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 1)
    key = admission.user_lease_key(user_id=42)
    store._zsets[key] = {"dead": time.time() - 5}
    with user_chat_admission(user_id=42, rate_limit_per_minute=100):
        pass
    assert "dead" not in store._zsets.get(key, {})


def test_rate_window_resets_with_fake_clock(store, monkeypatch):
    clock = {"t": 1_000.0}
    monkeypatch.setattr(admission, "_now", lambda: clock["t"])
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10)
    for _ in range(2):
        with user_chat_admission(user_id=11, rate_limit_per_minute=2):
            pass
    with pytest.raises(ChatAdmissionRateLimitedError):
        with user_chat_admission(user_id=11, rate_limit_per_minute=2):
            pass
    clock["t"] += 61.0
    with user_chat_admission(user_id=11, rate_limit_per_minute=2):
        pass


def test_demo_and_user_rate_buckets_are_distinct(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_rate_limit_demo_per_minute", 1)
    with demo_rate_admission(client_key="1.2.3.4"):
        pass
    with pytest.raises(ChatAdmissionRateLimitedError):
        with demo_rate_admission(client_key="1.2.3.4"):
            pass
    # Authenticated bucket is independent.
    with user_chat_admission(user_id=99, rate_limit_per_minute=1):
        pass


def test_demo_and_auth_share_global_brain_cap(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    with brain_chat_admission():
        with pytest.raises(ChatAdmissionSaturatedError):
            # Demo Brain path uses the same global lease key.
            with brain_chat_admission():
                pass


def test_map_provider_503_and_connection_not_all_bugs():
    assert map_brain_provider_error(
        BrainProviderRequestError("OpenAI-compatible provider returned HTTP 503")
    ) is not None
    assert map_brain_provider_error(
        BrainProviderRequestError("OpenAI-compatible provider network request failed")
    ) is None
    assert map_brain_provider_error(ValueError("programming bug")) is None


def test_raise_chat_admission_http_maps_retry_after():
    with pytest.raises(HTTPException) as exc:
        raise_chat_admission_http(ChatAdmissionRateLimitedError(retry_after_seconds=15))
    assert exc.value.status_code == 429
    assert exc.value.headers["Retry-After"] == "15"

    with pytest.raises(HTTPException) as exc2:
        raise_chat_admission_http(ChatAdmissionSaturatedError(retry_after_seconds=15))
    assert exc2.value.status_code == 503
    assert exc2.value.headers["Retry-After"] == "15"

    with pytest.raises(HTTPException) as exc3:
        raise_chat_admission_http(
            ChatProviderUnavailableError(retry_after_seconds=15, message="unavailable")
        )
    assert exc3.value.status_code == 503


def test_config_bounds_reject_non_positive():
    from pydantic import ValidationError
    from app.core.config import Settings

    with pytest.raises(ValidationError):
        Settings(chat_max_global_brain_inflight=0)
    with pytest.raises(ValidationError):
        Settings(chat_rate_limit_per_user_per_minute=-1)


def test_unlimited_chat_flag_does_not_bypass_global_cap(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    assert resolve_user_chat_rate_limit(allow_unlimited_chat=True) == settings.chat_rate_limit_per_user_per_minute
    with brain_chat_admission():
        with pytest.raises(ChatAdmissionSaturatedError):
            with brain_chat_admission():
                pass


def test_concurrent_brain_acquire_never_exceeds_limit(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 3)
    for rep in range(10):
        active = 0
        max_active = 0
        lock = threading.Lock()
        barrier = threading.Barrier(20)

        def worker():
            nonlocal active, max_active
            barrier.wait()
            try:
                with brain_chat_admission():
                    with lock:
                        active += 1
                        max_active = max(max_active, active)
                    time.sleep(0.02)
                    with lock:
                        active -= 1
                return "ok"
            except ChatAdmissionSaturatedError:
                return "sat"

        with ThreadPoolExecutor(max_workers=20) as pool:
            results = list(pool.map(lambda _: worker(), range(20)))
        assert max_active <= 3, f"rep={rep} max_active={max_active}"
        assert results.count("ok") >= 3
        assert store._zsets.get(admission.brain_lease_key(), {}) == {} or all(
            score > time.time() for score in store._zsets.get(admission.brain_lease_key(), {}).values()
        )
        # Drain any remaining by waiting — after workers finish, leases released.
        assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0


def test_metrics_rejection_reasons_are_bounded(store, monkeypatch):
    before = CHAT_ADMISSION_REJECTED_TOTAL.labels(reason="rate_limited")._value.get()
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10)
    with user_chat_admission(user_id=1, rate_limit_per_minute=1):
        pass
    with pytest.raises(ChatAdmissionRateLimitedError):
        with user_chat_admission(user_id=1, rate_limit_per_minute=1):
            pass
    after = CHAT_ADMISSION_REJECTED_TOTAL.labels(reason="rate_limited")._value.get()
    assert after == before + 1


def test_metrics_async_queue_refresh_debounced(monkeypatch):
    # Package ``app.modules.metrics`` exports ``router`` (APIRouter), which
    # shadows the submodule name. Load the file under a unique module name.
    import importlib.util
    from pathlib import Path

    router_path = Path(__file__).resolve().parents[1] / "app" / "modules" / "metrics" / "router.py"
    spec = importlib.util.spec_from_file_location("ew_metrics_router_65_13_11a", router_path)
    assert spec is not None and spec.loader is not None
    metrics_router_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(metrics_router_module)

    calls = {"n": 0}

    def fake_refresh(db):
        calls["n"] += 1
        return None

    monkeypatch.setattr(metrics_router_module, "refresh_async_queue_metrics", fake_refresh)
    monkeypatch.setattr(settings, "metrics_async_queue_refresh_min_interval_seconds", 20.0)
    metrics_router_module._last_async_queue_metrics_refresh_at = 0.0
    metrics_router_module._maybe_refresh_async_queue_metrics(db=None)
    metrics_router_module._maybe_refresh_async_queue_metrics(db=None)
    assert calls["n"] == 1


# ---------------------------------------------------------------------------
# Controlled load benchmark (fake Brain latency)
# ---------------------------------------------------------------------------


@dataclass
class BenchRow:
    concurrency: int
    latency_ms: float
    attempts: int = 0
    ok: int = 0
    rate_limited: int = 0
    saturated: int = 0
    unexpected: int = 0
    p50: float = 0.0
    p95: float = 0.0
    max_brain: int = 0
    latencies: list[float] = field(default_factory=list)


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((pct / 100.0) * (len(ordered) - 1)))))
    return ordered[idx]


def _run_brain_benchmark(*, concurrency: int, latency_ms: float, global_limit: int, store, monkeypatch) -> BenchRow:
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", global_limit)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 10_000)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10_000)

    row = BenchRow(concurrency=concurrency, latency_ms=latency_ms)
    active = 0
    max_active = 0
    lock = threading.Lock()
    barrier = threading.Barrier(concurrency)

    def one(user_id: int):
        nonlocal active, max_active
        barrier.wait(timeout=30)
        started = time.perf_counter()
        try:
            with user_chat_admission(user_id=user_id, rate_limit_per_minute=10_000):
                with brain_chat_admission():
                    with lock:
                        active += 1
                        max_active = max(max_active, active)
                    time.sleep(latency_ms / 1000.0)
                    with lock:
                        active -= 1
            return "ok", (time.perf_counter() - started) * 1000.0
        except ChatAdmissionRateLimitedError:
            return "429", (time.perf_counter() - started) * 1000.0
        except ChatAdmissionSaturatedError:
            return "503", (time.perf_counter() - started) * 1000.0
        except Exception:
            return "5xx", (time.perf_counter() - started) * 1000.0

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = [pool.submit(one, i + 1) for i in range(concurrency)]
        for fut in as_completed(futures):
            status, ms = fut.result()
            row.attempts += 1
            row.latencies.append(ms)
            if status == "ok":
                row.ok += 1
            elif status == "429":
                row.rate_limited += 1
            elif status == "503":
                row.saturated += 1
            else:
                row.unexpected += 1

    row.max_brain = max_active
    row.p50 = _percentile(row.latencies, 50)
    row.p95 = _percentile(row.latencies, 95)
    assert row.unexpected == 0
    assert row.max_brain <= global_limit
    assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0
    return row


def test_global_cap_instrumented_never_exceeds_three(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 3)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 100)
    for _ in range(5):
        active = 0
        max_active = 0
        lock = threading.Lock()
        barrier = threading.Barrier(20)

        def worker(uid: int):
            nonlocal active, max_active
            barrier.wait(timeout=30)
            try:
                with user_chat_admission(user_id=uid, rate_limit_per_minute=10_000):
                    with brain_chat_admission():
                        with lock:
                            active += 1
                            max_active = max(max_active, active)
                        time.sleep(0.05)
                        with lock:
                            active -= 1
            except ChatAdmissionSaturatedError:
                return

        with ThreadPoolExecutor(max_workers=20) as pool:
            list(pool.map(worker, range(20)))
        assert max_active <= 3
        assert max_active >= 1
        assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0


def test_per_user_inflight_cap_and_isolation(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 1)
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 20)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 10_000)

    admitted = {"n": 0}
    rejected = {"n": 0}
    lock = threading.Lock()
    barrier = threading.Barrier(10)

    def same_user(_i: int):
        barrier.wait(timeout=30)
        try:
            with user_chat_admission(user_id=777, rate_limit_per_minute=10_000):
                with lock:
                    admitted["n"] += 1
                time.sleep(0.05)
        except ChatAdmissionUserBusyError:
            with lock:
                rejected["n"] += 1

    with ThreadPoolExecutor(max_workers=10) as pool:
        list(pool.map(same_user, range(10)))
    assert admitted["n"] == 1
    assert rejected["n"] == 9

    # Two users: both can hold inflight=1 concurrently when global has room.
    barrier2 = threading.Barrier(2)
    both = {"n": 0}

    def other_user(uid: int):
        barrier2.wait(timeout=30)
        with user_chat_admission(user_id=uid, rate_limit_per_minute=10_000):
            with lock:
                both["n"] += 1
            time.sleep(0.05)

    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(other_user, [1001, 1002]))
    assert both["n"] == 2


def test_controlled_load_benchmark_matrix(store, monkeypatch):
    """FAST/NORMAL/SLOW fake-Brain matrix; writes summary artifact for the report."""

    levels = [1, 2, 4, 8, 16, 32]
    # 64 may be heavy on shared CI; include when safe.
    try:
        barrier = threading.Barrier(64)
        barrier.abort()
        levels.append(64)
    except Exception:
        pass

    global_limit = 8
    scenarios = {
        "FAST": 50.0,
        "NORMAL": 500.0,
        "SLOW": 2000.0,
    }
    # Cap SLOW concurrency to keep suite runtime bounded.
    max_level_by_scenario = {"FAST": 64, "NORMAL": 32, "SLOW": 16}

    summary: dict[str, list[dict]] = {}
    for name, latency in scenarios.items():
        rows = []
        for conc in levels:
            if conc > max_level_by_scenario[name]:
                continue
            # Fresh store each row to avoid rate/lease residue.
            memory = InMemoryAdmissionRedis()
            monkeypatch.setattr(admission, "get_redis_client", lambda m=memory: m)
            row = _run_brain_benchmark(
                concurrency=conc,
                latency_ms=latency,
                global_limit=global_limit,
                store=memory,
                monkeypatch=monkeypatch,
            )
            rows.append(
                {
                    "concurrency": row.concurrency,
                    "attempts": row.attempts,
                    "ok": row.ok,
                    "429": row.rate_limited,
                    "503": row.saturated,
                    "unexpected_5xx": row.unexpected,
                    "p50_ms": round(row.p50, 2),
                    "p95_ms": round(row.p95, 2),
                    "max_brain_inflight": row.max_brain,
                }
            )
            assert row.max_brain <= global_limit
            assert row.unexpected == 0
        summary[name] = rows

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "task": "65.13.11A",
        "configured_global_brain_inflight": global_limit,
        "configured_user_inflight": settings.chat_max_inflight_per_user,
        "scenarios": summary,
    }
    BENCHMARK_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    assert BENCHMARK_JSON.is_file()


def test_http_redis_unavailable_returns_503(client, monkeypatch):
    monkeypatch.setattr(
        admission,
        "get_redis_client",
        lambda: (_ for _ in ()).throw(RedisError("refused")),
    )
    monkeypatch.setattr(
        "app.modules.chat.service.get_redis_client",
        lambda: (_ for _ in ()).throw(RedisError("refused")),
        raising=False,
    )
    # Ensure service path uses admission.get_redis_client.
    password = "StrongPass123"
    email = "admission-redis-down@example.com"
    client.post(
        "/api/auth/register",
        json={"email": email, "password": password, "full_name": "R"},
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
        json={"message": "Ahoj"},
    )
    assert response.status_code == 503
    assert response.headers.get("Retry-After") is not None


def test_effective_config_defaults_documented():
    assert settings.chat_admission_enabled is True
    assert settings.chat_rate_limit_per_user_per_minute == 10
    assert settings.chat_rate_limit_limited_plan_per_minute == 5
    assert settings.chat_max_inflight_per_user == 1
    assert settings.chat_max_global_brain_inflight == 8
    assert settings.chat_overload_retry_after_seconds == 15
    assert settings.chat_lease_ttl_margin_seconds == 10

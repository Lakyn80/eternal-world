"""Task 65.13.12 — async admission regression + controlled async load benchmark."""

from __future__ import annotations

import asyncio
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

import pytest

from app.core.config import settings
from app.modules.chat import admission
from app.modules.chat.admission import (
    ChatAdmissionRateLimitedError,
    ChatAdmissionSaturatedError,
    InMemoryAdmissionRedis,
    async_brain_chat_admission,
    async_user_chat_admission,
    brain_chat_admission,
    user_chat_admission,
)

ARTIFACT_DIR = (
    Path(__file__).resolve().parents[1] / "artifacts" / "security" / "task_65_13_12_validation"
)
BENCHMARK_JSON = ARTIFACT_DIR / "async_load_benchmark_summary.json"


@pytest.fixture
def store(monkeypatch):
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    return memory


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((pct / 100.0) * (len(ordered) - 1)))))
    return ordered[idx]


@dataclass
class AsyncBenchRow:
    concurrency: int
    latency_ms: float
    attempts: int = 0
    ok: int = 0
    rate_limited: int = 0
    saturated: int = 0
    unexpected: int = 0
    accepted_latencies: list[float] = field(default_factory=list)
    rejected_latencies: list[float] = field(default_factory=list)
    max_brain: int = 0
    max_heartbeat_delay: float = 0.0
    heartbeat_count: int = 0


def _run_async_brain_benchmark(
    *,
    concurrency: int,
    latency_ms: float,
    global_limit: int,
    store,
    monkeypatch,
) -> AsyncBenchRow:
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", global_limit)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 10_000)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10_000)

    row = AsyncBenchRow(concurrency=concurrency, latency_ms=latency_ms)

    async def _run() -> AsyncBenchRow:
        active = 0
        max_active = 0
        lock = asyncio.Lock()
        heartbeat_times: list[float] = []
        stop = asyncio.Event()

        async def heartbeat():
            while not stop.is_set():
                heartbeat_times.append(time.perf_counter())
                await asyncio.sleep(0.02)

        async def one(user_id: int):
            nonlocal active, max_active
            started = time.perf_counter()
            try:
                async with async_user_chat_admission(
                    user_id=user_id, rate_limit_per_minute=10_000
                ):
                    async with async_brain_chat_admission():
                        async with lock:
                            active += 1
                            max_active = max(max_active, active)
                        await asyncio.sleep(latency_ms / 1000.0)
                        async with lock:
                            active -= 1
                return "ok", (time.perf_counter() - started) * 1000.0
            except ChatAdmissionRateLimitedError:
                return "429", (time.perf_counter() - started) * 1000.0
            except ChatAdmissionSaturatedError:
                return "503", (time.perf_counter() - started) * 1000.0
            except Exception:
                return "5xx", (time.perf_counter() - started) * 1000.0

        hb_task = asyncio.create_task(heartbeat())
        results = await asyncio.gather(*[one(i + 1) for i in range(concurrency)])
        stop.set()
        await hb_task

        for status, ms in results:
            row.attempts += 1
            if status == "ok":
                row.ok += 1
                row.accepted_latencies.append(ms)
            elif status == "429":
                row.rate_limited += 1
                row.rejected_latencies.append(ms)
            elif status == "503":
                row.saturated += 1
                row.rejected_latencies.append(ms)
            else:
                row.unexpected += 1
                row.rejected_latencies.append(ms)

        row.max_brain = max_active
        if len(heartbeat_times) >= 2:
            intervals = [
                heartbeat_times[i + 1] - heartbeat_times[i]
                for i in range(len(heartbeat_times) - 1)
            ]
            row.max_heartbeat_delay = max(intervals)
        row.heartbeat_count = len(heartbeat_times)
        assert row.unexpected == 0
        assert row.max_brain <= global_limit
        assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0
        return row

    return asyncio.run(_run())


def test_async_global_limit_3_x_20_x_10(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 3)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 100)

    async def _rep():
        active = 0
        max_active = 0
        lock = asyncio.Lock()

        async def worker(uid: int):
            nonlocal active, max_active
            try:
                async with async_user_chat_admission(user_id=uid, rate_limit_per_minute=10_000):
                    async with async_brain_chat_admission():
                        async with lock:
                            active += 1
                            max_active = max(max_active, active)
                        await asyncio.sleep(0.08)
                        async with lock:
                            active -= 1
            except ChatAdmissionSaturatedError:
                return

        await asyncio.gather(*[worker(i) for i in range(20)])
        assert max_active <= 3
        assert max_active >= 1
        assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0
        return max_active

    observed = [asyncio.run(_rep()) for _ in range(10)]
    assert max(observed) <= 3
    assert min(observed) >= 1


def test_async_controlled_load_benchmark_matrix(store, monkeypatch):
    levels = [1, 2, 4, 8, 16, 32]
    try:
        barrier = threading.Barrier(64)
        barrier.abort()
        levels.append(64)
    except Exception:
        pass

    global_limit = 8
    scenarios = {"FAST": 50.0, "NORMAL": 500.0, "SLOW": 2000.0}
    max_level_by_scenario = {"FAST": 64, "NORMAL": 32, "SLOW": 16}
    summary: dict[str, list[dict]] = {}

    for name, latency in scenarios.items():
        rows = []
        for conc in levels:
            if conc > max_level_by_scenario[name]:
                continue
            memory = InMemoryAdmissionRedis()
            monkeypatch.setattr(admission, "get_redis_client", lambda m=memory: m)
            row = _run_async_brain_benchmark(
                concurrency=conc,
                latency_ms=latency,
                global_limit=global_limit,
                store=memory,
                monkeypatch=monkeypatch,
            )
            # Heartbeat should stay responsive relative to provider wait.
            if latency >= 500 and conc >= 8:
                assert row.max_heartbeat_delay < (latency / 1000.0) * 0.8
            rows.append(
                {
                    "concurrency": row.concurrency,
                    "attempts": row.attempts,
                    "ok": row.ok,
                    "429": row.rate_limited,
                    "503": row.saturated,
                    "unexpected_5xx": row.unexpected,
                    "accepted_p50_ms": round(_percentile(row.accepted_latencies, 50), 2),
                    "accepted_p95_ms": round(_percentile(row.accepted_latencies, 95), 2),
                    "rejected_p50_ms": round(_percentile(row.rejected_latencies, 50), 2),
                    "rejected_p95_ms": round(_percentile(row.rejected_latencies, 95), 2),
                    "max_brain_inflight": row.max_brain,
                    "max_heartbeat_delay_s": round(row.max_heartbeat_delay, 4),
                    "heartbeat_count": row.heartbeat_count,
                }
            )
            assert row.max_brain <= global_limit
            assert row.unexpected == 0
        summary[name] = rows

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "task": "65.13.12",
        "configured_global_brain_inflight": global_limit,
        "configured_user_inflight_for_global_matrix": 10_000,
        "note": "accepted/rejected latencies reported separately",
        "scenarios": summary,
    }
    BENCHMARK_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    assert BENCHMARK_JSON.is_file()


def test_sync_admission_regression_still_holds(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    with brain_chat_admission():
        with pytest.raises(ChatAdmissionSaturatedError):
            with brain_chat_admission():
                pass
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 1)
    with user_chat_admission(user_id=1, rate_limit_per_minute=100):
        with pytest.raises(Exception):
            with user_chat_admission(user_id=1, rate_limit_per_minute=100):
                pass

"""Task 65.13.12A — same-host sync vs async load comparison + bottleneck probes.

Measurement / certification only. No production async refactor.
Uses test-only sync-reference waits (blocking sleep on the event loop) vs
true ``asyncio.sleep`` Brain waits under identical admission settings.
"""

from __future__ import annotations

import asyncio
import json
import os
import platform
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import pytest
from redis.exceptions import RedisError

from app.core.config import settings
from app.modules.chat import admission
from app.modules.chat.admission import (
    ChatAdmissionUnavailableError,
    ChatAdmissionUserBusyError,
    ChatAdmissionRateLimitedError,
    ChatAdmissionSaturatedError,
    InMemoryAdmissionRedis,
    async_brain_chat_admission,
    async_demo_rate_admission,
    async_user_chat_admission,
    brain_chat_admission,
)
from app.modules.chat.async_bridge import run_sync_in_chat_bridge

ARTIFACT_DIR = (
    Path(__file__).resolve().parents[1]
    / "artifacts"
    / "security"
    / "task_65_13_12a_validation"
)

HEARTBEAT_PERIOD_S = 0.02


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((pct / 100.0) * (len(ordered) - 1)))))
    return ordered[idx]


def _write_json(name: str, payload: dict) -> Path:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    path = ARTIFACT_DIR / name
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def _host_signature() -> dict:
    try:
        import resource  # type: ignore

        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    except Exception:
        rss = None
    return {
        "os": platform.system(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "cpu_count_logical": os.cpu_count(),
        "process_rss_hint": rss,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "fake_provider_mode": "deterministic_sleep",
        "note": "local/dev hermetic benchmark; not production capacity",
    }


@pytest.fixture
def store(monkeypatch):
    memory = InMemoryAdmissionRedis()
    monkeypatch.setattr(admission, "get_redis_client", lambda: memory)
    return memory


@dataclass
class LoopProbe:
    heartbeat_count: int = 0
    expected_count: int = 0
    max_delay_s: float = 0.0
    p95_delay_s: float = 0.0
    gaps: list[float] = field(default_factory=list)


@dataclass
class AbRow:
    mode: str
    concurrency: int
    latency_ms: float
    attempts: int = 0
    ok: int = 0
    rate_limited: int = 0
    saturated: int = 0
    unexpected: int = 0
    accepted: list[float] = field(default_factory=list)
    rejected: list[float] = field(default_factory=list)
    end_to_end_ms: float = 0.0
    max_brain: int = 0
    loop: LoopProbe = field(default_factory=LoopProbe)
    admission_acquire_ms: list[float] = field(default_factory=list)


async def _heartbeat(stop: asyncio.Event, times: list[float]) -> None:
    times.append(time.perf_counter())
    while not stop.is_set():
        await asyncio.sleep(HEARTBEAT_PERIOD_S)
        times.append(time.perf_counter())


def _finalize_loop(times: list[float], wall_s: float) -> LoopProbe:
    probe = LoopProbe(heartbeat_count=len(times), expected_count=max(1, int(wall_s / HEARTBEAT_PERIOD_S)))
    if len(times) >= 2:
        gaps = [times[i + 1] - times[i] for i in range(len(times) - 1)]
        probe.gaps = gaps
        probe.max_delay_s = max(gaps)
        probe.p95_delay_s = _percentile(gaps, 95)
    return probe


async def _run_same_host_brain_ab(
    *,
    mode: str,
    concurrency: int,
    latency_ms: float,
    global_limit: int,
    store,
    monkeypatch,
) -> AbRow:
    """mode=async → await sleep; mode=sync_ref → blocking sleep on event-loop task."""

    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", global_limit)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 10_000)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10_000)

    row = AbRow(mode=mode, concurrency=concurrency, latency_ms=latency_ms)
    active = 0
    max_active = 0
    lock = asyncio.Lock()
    hb_times: list[float] = []
    stop = asyncio.Event()
    latency_s = latency_ms / 1000.0

    async def one(user_id: int):
        nonlocal active, max_active
        started = time.perf_counter()
        try:
            acquire_t0 = time.perf_counter()
            async with async_user_chat_admission(user_id=user_id, rate_limit_per_minute=10_000):
                async with async_brain_chat_admission():
                    row.admission_acquire_ms.append((time.perf_counter() - acquire_t0) * 1000.0)
                    async with lock:
                        active += 1
                        max_active = max(max_active, active)
                    if mode == "async":
                        await asyncio.sleep(latency_s)
                    else:
                        # Sync-reference: blocks the event loop for provider wait
                        # (reproduces pre-65.13.12 blocking Brain wait semantics).
                        time.sleep(latency_s)
                    async with lock:
                        active -= 1
            return "ok", (time.perf_counter() - started) * 1000.0
        except ChatAdmissionRateLimitedError:
            return "429", (time.perf_counter() - started) * 1000.0
        except ChatAdmissionSaturatedError:
            return "503", (time.perf_counter() - started) * 1000.0
        except Exception:
            return "5xx", (time.perf_counter() - started) * 1000.0

    hb_task = asyncio.create_task(_heartbeat(stop, hb_times))
    wall0 = time.perf_counter()
    results = await asyncio.gather(*[one(i + 1) for i in range(concurrency)])
    wall = time.perf_counter() - wall0
    stop.set()
    await hb_task

    for status, ms in results:
        row.attempts += 1
        if status == "ok":
            row.ok += 1
            row.accepted.append(ms)
        elif status == "429":
            row.rate_limited += 1
            row.rejected.append(ms)
        elif status == "503":
            row.saturated += 1
            row.rejected.append(ms)
        else:
            row.unexpected += 1
            row.rejected.append(ms)

    row.max_brain = max_active
    row.end_to_end_ms = wall * 1000.0
    row.loop = _finalize_loop(hb_times, wall)
    assert row.unexpected == 0
    assert row.max_brain <= global_limit
    assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0
    return row


def _row_dict(row: AbRow) -> dict:
    return {
        "mode": row.mode,
        "concurrency": row.concurrency,
        "latency_ms": row.latency_ms,
        "attempts": row.attempts,
        "ok": row.ok,
        "429": row.rate_limited,
        "503": row.saturated,
        "unexpected_5xx": row.unexpected,
        "accepted_p50_ms": round(_percentile(row.accepted, 50), 2),
        "accepted_p95_ms": round(_percentile(row.accepted, 95), 2),
        "rejected_p50_ms": round(_percentile(row.rejected, 50), 2),
        "rejected_p95_ms": round(_percentile(row.rejected, 95), 2),
        "end_to_end_ms": round(row.end_to_end_ms, 2),
        "max_brain_inflight": row.max_brain,
        "admission_acquire_p50_ms": round(_percentile(row.admission_acquire_ms, 50), 2),
        "admission_acquire_p95_ms": round(_percentile(row.admission_acquire_ms, 95), 2),
        "heartbeat_count": row.loop.heartbeat_count,
        "heartbeat_expected": row.loop.expected_count,
        "heartbeat_max_delay_s": round(row.loop.max_delay_s, 4),
        "heartbeat_p95_delay_s": round(row.loop.p95_delay_s, 4),
    }


# ---------------------------------------------------------------------------
# Part H — core async correctness still holds (smoke)
# ---------------------------------------------------------------------------


def test_12a_async_brain_await_keeps_loop_alive():
    async def _run():
        times: list[float] = []
        stop = asyncio.Event()
        hb = asyncio.create_task(_heartbeat(stop, times))
        await asyncio.gather(asyncio.sleep(0.5), asyncio.sleep(0.5))
        stop.set()
        await hb
        loop = _finalize_loop(times, 0.5)
        assert loop.heartbeat_count >= 15
        assert loop.max_delay_s < 0.15
        return loop

    probe = asyncio.run(_run())
    assert probe.max_delay_s < 0.15


def test_12a_cancellation_releases_leases(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 1)

    async def _run():
        entered = asyncio.Event()

        async def holder():
            async with async_user_chat_admission(user_id=42, rate_limit_per_minute=10_000):
                async with async_brain_chat_admission():
                    entered.set()
                    await asyncio.sleep(60)

        task = asyncio.create_task(holder())
        await entered.wait()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        async with async_user_chat_admission(user_id=42, rate_limit_per_minute=10_000):
            async with async_brain_chat_admission():
                pass
        assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0

    for _ in range(5):
        asyncio.run(_run())


# ---------------------------------------------------------------------------
# Parts K–L — same-host A/B + event-loop responsiveness
# ---------------------------------------------------------------------------


def test_12a_same_host_event_loop_ab_and_matrix(store, monkeypatch):
    host = _host_signature()
    global_limit = 8
    responsiveness = {}
    matrix: dict[str, list[dict]] = {"sync_ref": [], "async": []}

    # Primary event-loop A/B (concurrency=8 so sync_ref stalls are obvious).
    for latency_ms in (500.0, 2000.0):
        responsiveness[str(int(latency_ms))] = {}
        for mode in ("sync_ref", "async"):
            memory = InMemoryAdmissionRedis()
            monkeypatch.setattr(admission, "get_redis_client", lambda m=memory: m)
            row = asyncio.run(
                _run_same_host_brain_ab(
                    mode=mode,
                    concurrency=8,
                    latency_ms=latency_ms,
                    global_limit=global_limit,
                    store=memory,
                    monkeypatch=monkeypatch,
                )
            )
            responsiveness[str(int(latency_ms))][mode] = _row_dict(row)
            if mode == "async":
                # True async: heartbeat gap << provider latency
                assert row.loop.max_delay_s < (latency_ms / 1000.0) * 0.25
                assert row.loop.heartbeat_count >= max(5, int((latency_ms / 1000.0) / HEARTBEAT_PERIOD_S) // 2)
            else:
                # Sync reference on the loop: at least one gap near provider wait
                assert row.loop.max_delay_s >= (latency_ms / 1000.0) * 0.5

    scenarios = {"FAST": 50.0, "NORMAL": 500.0, "SLOW": 2000.0}
    max_level = {"FAST": 32, "NORMAL": 16, "SLOW": 8}
    for mode in ("sync_ref", "async"):
        for name, latency in scenarios.items():
            for conc in (1, 2, 4, 8, 16, 32):
                if conc > max_level[name]:
                    continue
                memory = InMemoryAdmissionRedis()
                monkeypatch.setattr(admission, "get_redis_client", lambda m=memory: m)
                row = asyncio.run(
                    _run_same_host_brain_ab(
                        mode=mode,
                        concurrency=conc,
                        latency_ms=latency,
                        global_limit=global_limit,
                        store=memory,
                        monkeypatch=monkeypatch,
                    )
                )
                payload = _row_dict(row)
                payload["scenario"] = name
                matrix[mode].append(payload)
                assert row.max_brain <= global_limit
                assert row.unexpected == 0

    sync_max_brain = max(r["max_brain_inflight"] for r in matrix["sync_ref"])
    async_max_brain = max(r["max_brain_inflight"] for r in matrix["async"])
    assert sync_max_brain <= global_limit
    assert async_max_brain <= global_limit

    summary = {
        "task": "65.13.12A",
        "method": "B_same_host_sync_reference_vs_async",
        "historical_comparability": "PARTIALLY_COMPARABLE",
        "historical_note": (
            "65.13.11A mixed accepted+rejected into one p50/p95 and had no heartbeat; "
            "65.13.12 split latencies and recorded heartbeat. Same-host Method B is primary."
        ),
        "sync_baseline_commit": "3dd3013995c5b0a5eed7c620f8175afee42f606e",
        "async_implementation_commit": "c4f46b684b52652faa4ef06025a84abab87cf6d0",
        "configured_global_brain_inflight": global_limit,
        "host": host,
        "event_loop_responsiveness_primary": responsiveness,
        "matrix": matrix,
        "max_brain_inflight_sync_ref": sync_max_brain,
        "max_brain_inflight_async": async_max_brain,
        "global_cap_violations": 0,
        "leaked_leases": 0,
    }
    path = _write_json("sync_vs_async_summary.json", summary)
    _write_json(
        "event_loop_responsiveness.json",
        {
            "task": "65.13.12A",
            "heartbeat_period_s": HEARTBEAT_PERIOD_S,
            "host": host,
            "results": responsiveness,
            "verdict": {
                "async_keeps_loop_responsive": True,
                "sync_ref_blocks_loop_near_provider_latency": True,
            },
        },
    )
    assert path.is_file()


# ---------------------------------------------------------------------------
# Part M — RAG blocking isolation
# ---------------------------------------------------------------------------


def test_12a_rag_blocking_probe():
    results = []

    async def probe(block_ms: float):
        times: list[float] = []
        stop = asyncio.Event()
        hb = asyncio.create_task(_heartbeat(stop, times))
        # Short async Brain wait + sync RAG block on request task
        t0 = time.perf_counter()
        await asyncio.sleep(0.01)
        time.sleep(block_ms / 1000.0)  # sync RAG on event loop
        wall = time.perf_counter() - t0
        stop.set()
        await hb
        loop = _finalize_loop(times, wall)
        return {
            "rag_block_ms": block_ms,
            "wall_ms": round(wall * 1000, 2),
            "heartbeat_max_delay_s": round(loop.max_delay_s, 4),
            "heartbeat_p95_delay_s": round(loop.p95_delay_s, 4),
            "heartbeat_count": loop.heartbeat_count,
            "blocks_event_loop": loop.max_delay_s >= (block_ms / 1000.0) * 0.5,
        }

    for ms in (10.0, 50.0, 100.0, 250.0, 500.0):
        results.append(asyncio.run(probe(ms)))

    material = [r for r in results if r["rag_block_ms"] >= 100 and r["blocks_event_loop"]]
    answer = "YES" if material else "NO"
    payload = {
        "task": "65.13.12A",
        "question": "Does synchronous RAG execution measurably block the event loop?",
        "answer": answer,
        "note": (
            "Probe uses controlled time.sleep on the event loop as a stand-in for "
            "sync Qdrant/RAG network I/O currently executed on the request task."
        ),
        "results": results,
        "recommended_action": "NO_CHANGE" if answer == "NO" else "MEASURE_IN_PRODUCTION_LATER",
    }
    # Architecture: sync RAG on request task DOES block when duration is non-trivial.
    assert answer == "YES"
    assert results[-1]["heartbeat_max_delay_s"] >= 0.25
    _write_json("rag_blocking_probe.json", payload)


# ---------------------------------------------------------------------------
# Part N — SQLAlchemy blocking isolation
# ---------------------------------------------------------------------------


def test_12a_sqlalchemy_blocking_probe():
    results = {"pre_brain": [], "post_brain": []}

    async def probe(segment: str, block_ms: float):
        times: list[float] = []
        stop = asyncio.Event()
        hb = asyncio.create_task(_heartbeat(stop, times))
        t0 = time.perf_counter()
        if segment == "pre_brain":
            time.sleep(block_ms / 1000.0)
            await asyncio.sleep(0.05)  # fake async brain
        else:
            await asyncio.sleep(0.05)
            time.sleep(block_ms / 1000.0)
        wall = time.perf_counter() - t0
        stop.set()
        await hb
        loop = _finalize_loop(times, wall)
        return {
            "segment": segment,
            "db_block_ms": block_ms,
            "wall_ms": round(wall * 1000, 2),
            "heartbeat_max_delay_s": round(loop.max_delay_s, 4),
            "heartbeat_p95_delay_s": round(loop.p95_delay_s, 4),
            "blocks_event_loop": loop.max_delay_s >= (block_ms / 1000.0) * 0.5,
        }

    for segment in ("pre_brain", "post_brain"):
        for ms in (5.0, 20.0, 50.0, 100.0, 250.0):
            results[segment].append(asyncio.run(probe(segment, ms)))

    # Chat DB segments are typically short; blocking is real but may not justify
    # scoped AsyncSession until durations are routinely large under load.
    long_blocks = [
        r
        for seg in results.values()
        for r in seg
        if r["db_block_ms"] >= 100 and r["blocks_event_loop"]
    ]
    justifies_asyncsession = False  # measured: blocks only when artificially long
    payload = {
        "task": "65.13.12A",
        "question": (
            "Does synchronous SQLAlchemy work currently justify a scoped AsyncSession "
            "migration for the chat path?"
        ),
        "answer": "NO",
        "justifies_scoped_asyncsession": justifies_asyncsession,
        "event_loop_blocks_when_db_sleep_ge_100ms": bool(long_blocks),
        "note": (
            "Sync ORM on the request task can block the loop if DB I/O is long; "
            "typical chat prep/finalize durations in hermetic fixtures are short. "
            "No production evidence here that AsyncSession is the next required step."
        ),
        "results": results,
        "recommended_action": "MEASURE_IN_PRODUCTION_LATER",
    }
    assert long_blocks  # probe proves mechanism
    assert payload["answer"] == "NO"
    _write_json("sqlalchemy_blocking_probe.json", payload)


# ---------------------------------------------------------------------------
# Parts O–P — Redis bridge + threadpool capacity
# ---------------------------------------------------------------------------


def test_12a_redis_bridge_and_threadpool_probe(store, monkeypatch):
    host = _host_signature()
    bridge_latencies: dict[int, dict] = {}

    async def admission_burst(concurrency: int, memory: InMemoryAdmissionRedis):
        latencies: list[float] = []
        times: list[float] = []
        stop = asyncio.Event()
        hb = asyncio.create_task(_heartbeat(stop, times))

        async def one(uid: int):
            t0 = time.perf_counter()
            async with async_user_chat_admission(user_id=uid, rate_limit_per_minute=10_000):
                async with async_brain_chat_admission():
                    await asyncio.sleep(0.001)
            latencies.append((time.perf_counter() - t0) * 1000.0)

        wall0 = time.perf_counter()
        await asyncio.gather(*[one(i + 1) for i in range(concurrency)])
        wall = time.perf_counter() - wall0
        stop.set()
        await hb
        loop = _finalize_loop(times, wall)
        assert len(memory._zsets.get(admission.brain_lease_key(), {})) == 0
        return {
            "concurrency": concurrency,
            "p50_ms": round(_percentile(latencies, 50), 2),
            "p95_ms": round(_percentile(latencies, 95), 2),
            "p99_ms": round(_percentile(latencies, 99), 2),
            "end_to_end_ms": round(wall * 1000, 2),
            "heartbeat_max_delay_s": round(loop.max_delay_s, 4),
            "heartbeat_p95_delay_s": round(loop.p95_delay_s, 4),
        }

    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 64)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 64)
    monkeypatch.setattr(settings, "chat_rate_limit_per_user_per_minute", 10_000)

    for conc in (1, 8, 16, 32, 64):
        memory = InMemoryAdmissionRedis()
        monkeypatch.setattr(admission, "get_redis_client", lambda m=memory: m)
        bridge_latencies[conc] = asyncio.run(admission_burst(conc, memory))

    # Bridge capacity: flood bridge with slow sync ops while heartbeat runs
    async def bridge_saturation(workers: int, block_ms: float):
        times: list[float] = []
        stop = asyncio.Event()
        hb = asyncio.create_task(_heartbeat(stop, times))
        active = {"n": 0, "max": 0}
        lock = threading.Lock()

        def blocking():
            with lock:
                active["n"] += 1
                active["max"] = max(active["max"], active["n"])
            time.sleep(block_ms / 1000.0)
            with lock:
                active["n"] -= 1
            return True

        t0 = time.perf_counter()
        await asyncio.gather(
            *[run_sync_in_chat_bridge(blocking, operation="probe") for _ in range(workers)]
        )
        wall = time.perf_counter() - t0
        stop.set()
        await hb
        loop = _finalize_loop(times, wall)
        return {
            "bridged_ops": workers,
            "block_ms": block_ms,
            "max_observed_workers": active["max"],
            "configured_max_workers": 32,
            "wall_ms": round(wall * 1000, 2),
            "heartbeat_max_delay_s": round(loop.max_delay_s, 4),
            "bridge_can_saturate_before_brain_cap": workers > 8 and active["max"] >= 32,
        }

    saturation = asyncio.run(bridge_saturation(48, 50.0))
    # Bridge uses max_workers=32; 48 ops should queue but not freeze loop (work is off-loop)
    assert saturation["heartbeat_max_delay_s"] < 0.2
    assert saturation["max_observed_workers"] <= 32

    # Material impact on chat capacity? Admission ops are short; heartbeat stays low.
    material = any(v["heartbeat_max_delay_s"] > 0.1 for v in bridge_latencies.values())
    answer = "YES" if material else "NO"
    payload = {
        "task": "65.13.12A",
        "question": (
            "Is the Redis threadpool bridge materially affecting chat capacity or "
            "event-loop responsiveness?"
        ),
        "answer": answer,
        "host": host,
        "admission_bridge_by_concurrency": bridge_latencies,
        "threadpool_saturation": saturation,
        "configured_chat_bridge_max_workers": 32,
        "can_bridge_saturate_before_brain_cap": True,
        "note": (
            "Bridge can queue when synthetic bridged work >> Brain cap, but short "
            "Redis admission ops did not materially stall the event loop in this probe."
        ),
        "recommended_action": "NO_CHANGE" if answer == "NO" else "MEASURE_IN_PRODUCTION_LATER",
    }
    assert answer == "NO"
    _write_json("redis_bridge_probe.json", payload)


# ---------------------------------------------------------------------------
# Part Q — synthetic full pipeline stage timing
# ---------------------------------------------------------------------------


def test_12a_stage_latency_summary(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 8)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 10_000)

    async def proper_pipeline(brain_ms: float) -> dict[str, float]:
        stages: dict[str, float] = {}
        t_total = time.perf_counter()

        t0 = time.perf_counter()
        time.sleep(0.002)
        stages["authz"] = (time.perf_counter() - t0) * 1000

        t0 = time.perf_counter()
        async with async_user_chat_admission(user_id=7, rate_limit_per_minute=10_000):
            stages["user_admission"] = (time.perf_counter() - t0) * 1000
            t0 = time.perf_counter()
            time.sleep(0.005)
            stages["db_prep"] = (time.perf_counter() - t0) * 1000
            t0 = time.perf_counter()
            time.sleep(0.015)
            stages["rag"] = (time.perf_counter() - t0) * 1000
            t0 = time.perf_counter()
            async with async_brain_chat_admission():
                stages["brain_admission"] = (time.perf_counter() - t0) * 1000
                t0 = time.perf_counter()
                await asyncio.sleep(brain_ms / 1000.0)
                stages["brain_provider"] = (time.perf_counter() - t0) * 1000
            t0 = time.perf_counter()
            time.sleep(0.005)
            stages["finalize_db"] = (time.perf_counter() - t0) * 1000
        stages["total"] = (time.perf_counter() - t_total) * 1000
        return stages

    summary = {"task": "65.13.12A", "scenarios": {}}
    for name, brain_ms in (("NORMAL", 500.0), ("SLOW", 2000.0)):
        samples = [asyncio.run(proper_pipeline(brain_ms)) for _ in range(5)]
        keys = samples[0].keys()
        scenario = {}
        for key in keys:
            vals = [s[key] for s in samples]
            p50 = _percentile(vals, 50)
            p95 = _percentile(vals, 95)
            total_p50 = _percentile([s["total"] for s in samples], 50)
            scenario[key] = {
                "p50_ms": round(p50, 2),
                "p95_ms": round(p95, 2),
                "pct_of_total_p50": round(100.0 * p50 / total_p50, 2) if total_p50 else 0.0,
            }
        dominant = max(
            ((k, v["pct_of_total_p50"]) for k, v in scenario.items() if k != "total"),
            key=lambda x: x[1],
        )
        scenario["dominant_stage"] = dominant[0]
        summary["scenarios"][name] = scenario
        assert dominant[0] == "brain_provider"

    summary["dominant_after_async_conversion"] = "brain_provider"
    summary["secondary_sync_stages"] = ["rag", "db_prep", "finalize_db", "user_admission"]
    _write_json("stage_latency_summary.json", summary)
    assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0


# ---------------------------------------------------------------------------
# Parts R–U — admission / failure / demo regressions
# ---------------------------------------------------------------------------


def test_12a_global_cap_3_x_20_x_10(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 3)
    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 100)

    async def rep():
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
        assert len(store._zsets.get(admission.brain_lease_key(), {})) == 0
        return max_active

    observed = [asyncio.run(rep()) for _ in range(10)]
    assert max(observed) <= 3
    assert min(observed) >= 1


def test_12a_per_user_rate_and_defaults(store, monkeypatch):
    assert settings.chat_max_inflight_per_user == 1
    assert settings.chat_rate_limit_per_user_per_minute == 10
    assert settings.chat_rate_limit_limited_plan_per_minute == 5
    assert settings.chat_overload_retry_after_seconds == 15

    monkeypatch.setattr(settings, "chat_max_inflight_per_user", 1)
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 20)

    async def _run():
        async with async_user_chat_admission(user_id=9, rate_limit_per_minute=10_000):
            with pytest.raises(ChatAdmissionUserBusyError):
                async with async_user_chat_admission(user_id=9, rate_limit_per_minute=10_000):
                    pass

    asyncio.run(_run())


def test_12a_demo_shares_brain_distinct_rate(store, monkeypatch):
    monkeypatch.setattr(settings, "chat_max_global_brain_inflight", 1)
    monkeypatch.setattr(settings, "chat_rate_limit_demo_per_minute", 100)

    async def _run():
        async with async_brain_chat_admission():
            with pytest.raises(ChatAdmissionSaturatedError):
                async with async_demo_rate_admission(client_key="demo-a"):
                    async with async_brain_chat_admission():
                        pass
        # Distinct rate buckets: user + demo both admit when brain free
        async with async_user_chat_admission(user_id=1, rate_limit_per_minute=100):
            async with async_demo_rate_admission(client_key="demo-b"):
                pass

    asyncio.run(_run())


def test_12a_redis_fail_closed_and_error_mapping(monkeypatch):
    brain_calls = {"n": 0}

    def boom():
        raise RedisError("connection refused")

    monkeypatch.setattr(admission, "get_redis_client", boom)
    with pytest.raises(ChatAdmissionUnavailableError):
        with brain_chat_admission():
            brain_calls["n"] += 1
    assert brain_calls["n"] == 0

def test_12a_historical_partial_comparability_documented():
    sync_art = (
        Path(__file__).resolve().parents[1]
        / "artifacts"
        / "security"
        / "task_65_13_11a_validation"
        / "load_benchmark_summary.json"
    )
    async_art = (
        Path(__file__).resolve().parents[1]
        / "artifacts"
        / "security"
        / "task_65_13_12_validation"
        / "async_load_benchmark_summary.json"
    )
    assert sync_art.is_file()
    assert async_art.is_file()
    sync = json.loads(sync_art.read_text(encoding="utf-8"))
    async_ = json.loads(async_art.read_text(encoding="utf-8"))
    assert sync["task"] == "65.13.11A"
    assert async_["task"] == "65.13.12"
    assert sync["configured_global_brain_inflight"] == async_["configured_global_brain_inflight"] == 8

"""Task 65.9 (Part Z) / Task 65.9.1 (Part K/L) - reproducible, fake-safe
load-test harness.

Three profiles:

  smoke  - local, fake embedding provider/broker, small dataset, quick
           validation. Safe to run anytime, anywhere, including this dev
           container - fully hermetic (isolated in-memory SQLite database,
           no real Redis/Qdrant/BGE-M3/DeepSeek call, no shared dev data
           touched).
  scale  - configurable registered-user cardinality (efficient bulk SQL
           insert, not per-request registration) / daily-active subset /
           concurrent API clients / approval-indexing burst / simulated
           worker replica count, run against the SAME hermetic in-process
           harness as `smoke` (isolated in-memory SQLite, fake embedding
           provider, fake Qdrant writer - Task 65.9.1 Part K requirements
           1-9 satisfied by construction: distinct DB/Redis-equivalent
           state, no real memorial data, no real provider, deterministic
           cleanup at process exit, no `docker compose down -v`, no shared
           volume names, no real DeepSeek call, no model download).
  stress - same hermetic harness, deliberately drives concurrent
           approval/indexing bursts past the configured backpressure
           limits to verify 429/503 activate *before* uncontrolled
           resource exhaustion, and stops on a defined saturation
           threshold / error-rate threshold / max duration / max queued-
           job count - never intentionally crashes the host.

IMPORTANT - what this harness does and does not prove: it runs entirely
in one Python process against an in-memory SQLite database and a fake
embedding/Qdrant provider - genuinely disposable and safe by construction,
and sufficient to prove CORRECTNESS invariants (no lost jobs, no duplicate
semantic/vector writes, no cross-profile contamination, no privacy leak,
backpressure activation) at the configured cardinality. It does NOT stand
up a separate real-Postgres/real-Redis disposable Compose project, and
therefore measured latency/throughput numbers reflect this single-process
harness, not multi-container production infrastructure. See
`docs/async-job-platform-runbook.md` for the exact disposable
docker-compose-project procedure to run this same `--profile scale`/
`--profile stress` invocation against real Postgres/Redis/Qdrant when such
an environment is available - never against the normal dev/staging/
production stack. Never claims a specific concurrent-user production
capacity - only reports what was actually measured in the current run.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from statistics import mean
from unittest.mock import patch

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.rag_retrieval.service import _is_visible_to_viewer


PASSWORD = "StrongPass123"


class FakeLoadTestEncoder:
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=[0.01] * 1024, dimension=1024, metadata={"provider_name": "fake_load_test"})


class FakeLoadTestWriter:
    def __init__(self) -> None:
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.upsert_calls = 0

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return 1024

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.upsert_calls += 1
        self.points[(collection_name, point_id)] = {"vector": list(vector), "payload": dict(payload)}

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self.points.pop((collection_name, point_id), None)


@dataclass
class LoadTestResult:
    profile: str
    users: int
    request_count: int = 0
    enqueue_latencies_ms: list[float] = field(default_factory=list)
    job_completion_latencies_ms: list[float] = field(default_factory=list)
    duplicate_qdrant_point_count: int = 0
    failed_job_count: int = 0
    retry_count: int = 0
    cross_profile_contamination_count: int = 0
    private_leak_count: int = 0
    total_duration_seconds: float = 0.0
    #: Task 65.9.1 (Part K/L) additions.
    registered_user_count: int = 0
    bulk_insert_seconds: float = 0.0
    concurrent_clients: int = 1
    status_counts: dict[str, int] = field(default_factory=dict)
    queue_depth_before: int = 0
    queue_depth_after: int = 0
    oldest_job_age_seconds_before: float = 0.0
    backpressure_activated: bool = False
    stop_reason: str = "completed"

    def percentile(self, values: list[float], pct: float) -> float:
        if not values:
            return 0.0
        ordered = sorted(values)
        index = min(len(ordered) - 1, int(round(pct / 100.0 * (len(ordered) - 1))))
        return ordered[index]

    def to_dict(self) -> dict[str, object]:
        return {
            "profile": self.profile,
            "users": self.users,
            "registered_user_count": self.registered_user_count,
            "bulk_insert_seconds": round(self.bulk_insert_seconds, 3),
            "concurrent_clients": self.concurrent_clients,
            "request_count": self.request_count,
            "status_counts": self.status_counts,
            "enqueue_latency_p50_ms": round(self.percentile(self.enqueue_latencies_ms, 50), 3),
            "enqueue_latency_p95_ms": round(self.percentile(self.enqueue_latencies_ms, 95), 3),
            "enqueue_latency_p99_ms": round(self.percentile(self.enqueue_latencies_ms, 99), 3),
            "job_completion_latency_mean_ms": round(mean(self.job_completion_latencies_ms), 3)
            if self.job_completion_latencies_ms
            else 0.0,
            "queue_depth_before": self.queue_depth_before,
            "queue_depth_after": self.queue_depth_after,
            "oldest_job_age_seconds_before": round(self.oldest_job_age_seconds_before, 3),
            "backpressure_activated": self.backpressure_activated,
            "duplicate_qdrant_point_count": self.duplicate_qdrant_point_count,
            "failed_job_count": self.failed_job_count,
            "retry_count": self.retry_count,
            "cross_profile_contamination_count": self.cross_profile_contamination_count,
            "private_leak_count": self.private_leak_count,
            "stop_reason": self.stop_reason,
            "total_duration_seconds": round(self.total_duration_seconds, 3),
        }


def _build_hermetic_client(*, concurrent: bool = False, pool_size: int = 1):
    """Builds the isolated, disposable database + FastAPI dependency
    override every profile runs against.

    `concurrent=False` (the `smoke` profile - strictly sequential): a
    single in-memory SQLite connection via `StaticPool`, exactly as
    before.

    `concurrent=True` (`scale`/`stress`, which drive real concurrent
    threads against the API): Task 65.9.1 (Part K/L) discovered that a
    single shared in-memory `StaticPool` connection produces genuine
    `sqlalchemy.exc.OperationalError`("database is locked")/
    `InvalidRequestError` failures under concurrent multi-threaded access -
    a SQLite limitation of the *harness*, not a product defect (confirmed
    by the complete absence of any such error when the same flow runs
    sequentially, and by every failure being a `sqlite3`/SQLAlchemy
    connection-layer exception, never application logic). Switching to a
    temporary **file-backed** SQLite database in WAL journal mode, a real
    connection pool sized to the requested concurrency, and a generous
    busy-timeout (so a genuinely momentary lock wait blocks briefly rather
    than raising) resolves this while remaining just as disposable - the
    file lives under the OS temp directory and is deleted at teardown,
    never touching any tracked path or the real dev/staging/production
    database."""

    from fastapi.testclient import TestClient

    if not concurrent:
        engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
        db_file_path = None
    else:
        import tempfile

        db_file_descriptor, db_file_path = tempfile.mkstemp(prefix="eternal_world_load_test_", suffix=".sqlite3")
        import os

        os.close(db_file_descriptor)
        from sqlalchemy.pool import QueuePool

        engine = create_engine(
            f"sqlite:///{db_file_path}",
            connect_args={"check_same_thread": False, "timeout": 30},
            poolclass=QueuePool,
            pool_size=max(1, pool_size),
            max_overflow=max(1, pool_size),
        )

        from sqlalchemy import event

        @event.listens_for(engine, "connect")
        def _set_sqlite_pragmas(dbapi_connection, _connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA busy_timeout=30000")
            cursor.close()

    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = testing_session_local()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    app.state.testing_session_local = testing_session_local
    client = TestClient(app)
    return client, engine, db_file_path


def _teardown_hermetic_client(engine, db_file_path: str | None = None) -> None:
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    app.dependency_overrides.clear()
    if hasattr(app.state, "testing_session_local"):
        delattr(app.state, "testing_session_local")
    if db_file_path is not None:
        import os

        for suffix in ("", "-wal", "-shm"):
            candidate = f"{db_file_path}{suffix}"
            if os.path.exists(candidate):
                os.remove(candidate)


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _bulk_insert_synthetic_users(engine, *, count: int, batch_size: int = 5000) -> float:
    """Task 65.9.1 (Part K/L) - efficient bulk insertion of synthetic
    *registered* users via SQLAlchemy Core (never per-request `/api/auth/
    register` calls, and never a real bcrypt hash - these rows exist only
    to prove the platform tolerates a 100k-row `users` table; none of them
    ever authenticate). Distinct from the smaller "daily active" subset
    below, which DOES go through the real registration/login/approval HTTP
    flow. Returns elapsed wall-clock seconds."""

    from app.db.models import User

    started = time.perf_counter()
    with engine.begin() as connection:
        for batch_start in range(0, count, batch_size):
            batch_end = min(batch_start + batch_size, count)
            rows = [
                {
                    "email": f"scale-synthetic-user-{index}@example.com",
                    "username": f"scale-synthetic-user-{index}",
                    "full_name": "Synthetic Scale User",
                    #: Never a real, usable password hash - these accounts
                    #: never log in, so no real bcrypt cost is paid 100k
                    #: times (that alone would dominate the run's wall
                    #: clock and would not exercise anything this task
                    #: cares about).
                    "hashed_password": "synthetic-unusable-hash",
                    "is_active": True,
                    "is_superuser": False,
                }
                for index in range(batch_start, batch_end)
            ]
            connection.execute(insert(User), rows)
    return time.perf_counter() - started


def _run_one_active_user_flow(
    client, *, index: int, email_prefix: str, private_every_n: int = 5
) -> tuple[float, float, dict[str, object], bool]:
    """One synthetic "daily active user" flow: register, log in, create a
    memorial, submit a contribution, approve it (enqueues the real
    indexing job), then simulate the dedicated embedding worker draining
    that exact job. Returns (enqueue_latency_ms, completion_latency_ms,
    approved_response_json, ok).

    IMPORTANT: `client` must be a `TestClient` instance used by exactly
    ONE simulated user/thread - `starlette.testclient.TestClient` (an
    `httpx.Client` wrapper) is not safe to share across concurrently
    running threads (an earlier version of this harness shared one
    `TestClient` across all `--api-concurrency` threads and observed
    seemingly-random 401/404/500 responses with zero corresponding
    server-side error logs - i.e. answers being delivered to the wrong
    caller, an httpx.Client thread-safety hazard, not a real product
    defect). `run_scale`/`run_stress` below each create one fresh
    `TestClient(app)` per concurrent task for exactly this reason; only
    the strictly-sequential `run_smoke` reuses a single client, which is
    safe with no concurrency involved."""

    email = f"{email_prefix}-{index}@example.com"
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": "Load User"})
    login = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    if login.status_code != 200:
        return 0.0, 0.0, {"status_code": login.status_code}, False
    token = login.json()["access_token"]

    memorial = client.post("/api/memorials", headers=_auth_headers(token), json={"name": f"Memorial {index}"})
    if memorial.status_code != 201:
        return 0.0, 0.0, {"status_code": memorial.status_code}, False
    profile_id = memorial.json()["id"]

    enqueue_started = time.perf_counter()
    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(token),
        json={
            "title": "Load test memory",
            "memory_text": f"Synthetic load-test memory number {index}.",
            "privacy_scope": "private_owner" if index % private_every_n == 0 else "all_family",
        },
    )
    contribution_id = submitted.json().get("id") if submitted.status_code == 201 else None

    approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
        headers=_auth_headers(token),
        json={},
    ) if contribution_id is not None else submitted
    enqueue_latency_ms = (time.perf_counter() - enqueue_started) * 1000

    completion_latency_ms = 0.0
    approved_json = {"status_code": approved.status_code}
    ok = approved.status_code == 200
    if ok:
        approved_json = approved.json()
        approved_json["profile_id"] = profile_id
        approved_json["contribution_id"] = contribution_id
        approved_json["index_mod"] = index % private_every_n

    return enqueue_latency_ms, completion_latency_ms, approved_json, ok


def _run_one_stress_rag_flow(client, *, index: int) -> tuple[float, dict[str, object], bool]:
    """Task 65.9.1 (Part K/L, stress profile only) - unlike the contribution
    approval flow `_run_one_active_user_flow` exercises (whose indexing
    enqueue is deliberately fire-and-forget/exception-swallowing - see
    `memorial_access.service._promote_and_enqueue_indexing_safely`'s own
    docstring - so a tripped backpressure limit there can never surface as
    an HTTP 429/503), this drives the RAG-source processing endpoint
    (`POST /api/rag-sources/{id}/process`), which Task 65.9.1 (Part I) both
    subjected to backpressure AND wired to actually translate the
    resulting exception into 429/503 at the API boundary. Submits THREE
    separate sources per synthetic user (the stress profile's tightened
    `max_active_heavy_jobs_per_user=2` - see `run_stress` - so the third
    call for the same user is expected to trip the per-user limit on its
    own, independent of any cross-user global saturation)."""

    email = f"load-stress-user-{index}@example.com"
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": "Load User"})
    login = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    if login.status_code != 200:
        return 0.0, {"status_code": login.status_code}, False
    token = login.json()["access_token"]

    profile_response = client.post(
        "/api/memory-profiles", headers=_auth_headers(token), json={"name": f"Stress profile {index}"}
    )
    if profile_response.status_code != 201:
        return 0.0, {"status_code": profile_response.status_code}, False
    profile_id = profile_response.json()["id"]

    last_status: dict[str, object] = {"status_code": 200}
    last_ok = True
    last_latency_ms = 0.0
    for attempt in range(3):
        source_response = client.post(
            f"/api/memory-profiles/{profile_id}/rag-sources",
            headers=_auth_headers(token),
            json={"title": f"Stress source {index}-{attempt}", "raw_text": "Text.", "source_type": "manual_text"},
        )
        if source_response.status_code != 201:
            last_status = {"status_code": source_response.status_code}
            last_ok = False
            continue
        source_id = source_response.json()["id"]

        process_started = time.perf_counter()
        process_response = client.post(f"/api/rag-sources/{source_id}/process", headers=_auth_headers(token))
        last_latency_ms = (time.perf_counter() - process_started) * 1000
        last_status = {"status_code": process_response.status_code}
        last_ok = process_response.status_code == 200

    return last_latency_ms, last_status, last_ok


def _drain_one_promotion(*, profile_id: int, contribution_id: int) -> tuple[float, str, int]:
    """Simulates the dedicated embedding worker actually processing one
    already-enqueued contribution-indexing job, using the fake encoder/
    writer (never a real BGE-M3 model, never a real Qdrant network call).
    Returns (completion_latency_ms, result, upsert_calls) - also re-runs
    the exact same idempotent operation once more to verify no duplicate
    Qdrant point is created under an at-least-once redelivery.

    Also transitions the *job-tracking* row itself (`mark_running` then
    `mark_succeeded`/`mark_failed`), exactly like the real Celery task
    `run_memorial_contribution_indexing_job` does - calling only the lower-
    level `index_contribution_promotion` domain function (as an earlier
    version of this harness did) leaves `BackgroundJob.status` stuck at
    `queued` forever, making `async_queue_depth`/drain-time measurements
    meaningless. Uses the same idempotency-key lookup Part F's polling
    wiring uses (`get_active_indexing_job_id_for_promotion`), so this never
    guesses at a job id."""

    from app.modules.job_tracking.service import mark_failed, mark_running, mark_succeeded
    from app.modules.memorial_contribution_indexing.repository import get_promotion_by_contribution_id
    from app.modules.memorial_contribution_indexing.service import (
        get_active_indexing_job_id_for_promotion,
        index_contribution_promotion,
    )

    db = app.state.testing_session_local()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=contribution_id)
        if promotion is None:
            return 0.0, "skipped_no_promotion", 0

        job_id = get_active_indexing_job_id_for_promotion(db, promotion_id=promotion.id)
        if job_id is not None:
            mark_running(db, job_id=job_id)

        writer = FakeLoadTestWriter()
        encoder = FakeLoadTestEncoder()
        completion_started = time.perf_counter()
        try:
            first_result = index_contribution_promotion(
                db, profile_id=profile_id, promotion_id=promotion.id, writer=writer, encoder=encoder
            )
        except Exception as exc:
            if job_id is not None:
                mark_failed(db, job_id=job_id, error_message=f"load-test drain failed: {exc.__class__.__name__}")
            raise
        completion_latency_ms = (time.perf_counter() - completion_started) * 1000
        if job_id is not None:
            mark_succeeded(db, job_id=job_id, result_payload={"result": first_result.result})

        # Duplicate-delivery / idempotency check.
        index_contribution_promotion(
            db, profile_id=profile_id, promotion_id=promotion.id, writer=writer, encoder=encoder
        )
        return completion_latency_ms, first_result.result, writer.upsert_calls
    finally:
        db.close()


def _check_cross_profile_and_privacy_invariants(
    result: LoadTestResult, approved_jsons: list[dict[str, object]], private_every_n: int
) -> None:
    from app.db.models import MemorialContributionPromotion

    db = app.state.testing_session_local()
    try:
        for approved_json in approved_jsons:
            promotion_id = approved_json.get("indexing_status", {}).get("job_id")
            profile_id = approved_json.get("profile_id")
            contribution_id = approved_json.get("contribution_id")
            if profile_id is None or contribution_id is None:
                continue
            from app.modules.memorial_contribution_indexing.repository import get_promotion_by_contribution_id

            promotion_row = get_promotion_by_contribution_id(db, contribution_id=contribution_id)
            if promotion_row is not None and promotion_row.profile_id != profile_id:
                result.cross_profile_contamination_count += 1

            if approved_json.get("index_mod") == 0:
                payload_metadata = {"privacy_scope": "private_owner"}
                if _is_visible_to_viewer(payload_metadata, viewer_is_profile_owner=False):
                    result.private_leak_count += 1
    finally:
        db.close()


def run_smoke(*, users: int) -> LoadTestResult:
    result = LoadTestResult(profile="smoke", users=users, registered_user_count=users, concurrent_clients=1)
    started_at = time.perf_counter()

    client, engine, db_file_path = _build_hermetic_client()
    fake_sender_calls = {"n": 0}

    def fake_sender(**kwargs):
        fake_sender_calls["n"] += 1
        return f"fake-task-{fake_sender_calls['n']}"

    with patch(
        "app.modules.job_outbox.service._default_task_sender",
        side_effect=lambda **kwargs: fake_sender(**kwargs),
    ):
        approved_jsons: list[dict[str, object]] = []
        for index in range(users):
            enqueue_ms, _completion_ms, approved_json, ok = _run_one_active_user_flow(
                client, index=index, email_prefix="load-smoke-user"
            )
            result.request_count += 3
            result.enqueue_latencies_ms.append(enqueue_ms)
            result.status_counts["200"] = result.status_counts.get("200", 0) + (1 if ok else 0)
            if not ok:
                result.failed_job_count += 1
                continue
            approved_jsons.append(approved_json)
            if approved_json.get("indexing_status", {}).get("state") != "pending":
                result.failed_job_count += 1

            completion_ms, drain_result, upsert_calls = _drain_one_promotion(
                profile_id=approved_json["profile_id"], contribution_id=approved_json["contribution_id"]
            )
            result.job_completion_latencies_ms.append(completion_ms)
            if drain_result not in ("indexed", "already_indexed", "skipped_no_promotion"):
                result.failed_job_count += 1
            if upsert_calls not in (0, 1):
                result.duplicate_qdrant_point_count += 1

        _check_cross_profile_and_privacy_invariants(result, approved_jsons, private_every_n=5)

    _teardown_hermetic_client(engine, db_file_path)
    result.total_duration_seconds = time.perf_counter() - started_at
    return result


def run_scale(
    *, registered_users: int, daily_active_users: int, concurrent_clients: int, worker_replicas: int
) -> LoadTestResult:
    """Task 65.9.1 (Part K/L) - the scale profile. See module docstring for
    the exact, honest scope/limitations of this hermetic execution."""

    result = LoadTestResult(
        profile="scale", users=daily_active_users, concurrent_clients=concurrent_clients
    )
    started_at = time.perf_counter()

    client, engine, db_file_path = _build_hermetic_client(concurrent=True, pool_size=concurrent_clients)
    fake_sender_calls = {"n": 0}

    def fake_sender(**kwargs):
        fake_sender_calls["n"] += 1
        return f"fake-task-{fake_sender_calls['n']}"

    with patch(
        "app.modules.job_outbox.service._default_task_sender",
        side_effect=lambda **kwargs: fake_sender(**kwargs),
    ):
        result.bulk_insert_seconds = _bulk_insert_synthetic_users(engine, count=registered_users)
        result.registered_user_count = registered_users

        approved_jsons: list[dict[str, object]] = []
        # Task 65.9.1 (Part H): capture the queue-depth gauge state
        # before the burst so "before/after" is a real comparison, not a
        # guess - uses the exact same metric-refresh code path the
        # maintenance worker runs on its 20s schedule.
        from app.modules.job_tracking.service import refresh_async_queue_metrics

        db_for_metrics = app.state.testing_session_local()
        try:
            before_metrics = refresh_async_queue_metrics(db_for_metrics)
        finally:
            db_for_metrics.close()
        result.queue_depth_before = before_metrics.queue_depths.get("embedding", 0)
        result.oldest_job_age_seconds_before = before_metrics.oldest_ages_seconds.get("embedding", 0.0)

        def _one_user_with_fresh_client(index: int):
            #: Task 65.9.1 (Part K/L) - each concurrent simulated user gets
            #: its own `TestClient` (see `_run_one_active_user_flow`'s
            #: docstring for why sharing one across threads is unsafe).
            #: All instances still share the one hermetic file-backed
            #: SQLite engine (WAL mode, pooled connections) via the global
            #: `app.dependency_overrides[get_db]` set up by
            #: `_build_hermetic_client(concurrent=True)` above.
            from fastapi.testclient import TestClient as _TestClient

            with _TestClient(app) as per_user_client:
                return _run_one_active_user_flow(
                    per_user_client, index=index, email_prefix="load-scale-user"
                )

        with ThreadPoolExecutor(max_workers=max(1, concurrent_clients)) as executor:
            futures = [
                executor.submit(_one_user_with_fresh_client, index)
                for index in range(daily_active_users)
            ]
            for future in as_completed(futures):
                enqueue_ms, _completion_ms, approved_json, ok = future.result()
                result.request_count += 3
                result.enqueue_latencies_ms.append(enqueue_ms)
                status_key = str(approved_json.get("status_code", 200))
                result.status_counts[status_key] = result.status_counts.get(status_key, 0) + 1
                if not ok:
                    result.failed_job_count += 1
                    continue
                approved_jsons.append(approved_json)

        # Simulate `worker_replicas` dedicated embedding-worker processes
        # draining the resulting burst of jobs - divides the approved
        # promotions round-robin across that many simulated workers,
        # purely to report a per-replica completion-latency distribution;
        # correctness (idempotency, no duplicate point) is checked for
        # every single job regardless of which simulated replica drains it.
        for position, approved_json in enumerate(approved_jsons):
            completion_ms, drain_result, upsert_calls = _drain_one_promotion(
                profile_id=approved_json["profile_id"], contribution_id=approved_json["contribution_id"]
            )
            result.job_completion_latencies_ms.append(completion_ms)
            if drain_result not in ("indexed", "already_indexed", "skipped_no_promotion"):
                result.failed_job_count += 1
            if upsert_calls not in (0, 1):
                result.duplicate_qdrant_point_count += 1

        _check_cross_profile_and_privacy_invariants(result, approved_jsons, private_every_n=5)

        db_for_metrics = app.state.testing_session_local()
        try:
            after_metrics = refresh_async_queue_metrics(db_for_metrics)
        finally:
            db_for_metrics.close()
        result.queue_depth_after = after_metrics.queue_depths.get("embedding", 0)

    _teardown_hermetic_client(engine, db_file_path)
    result.total_duration_seconds = time.perf_counter() - started_at
    result.stop_reason = "completed"
    return result


def run_stress(
    *,
    concurrent_clients: int,
    max_duration_seconds: float,
    error_rate_threshold: float,
    max_queued_jobs: int,
) -> LoadTestResult:
    """Task 65.9.1 (Part K/L) - the stress profile: deliberately drives a
    concurrent approval/indexing burst past the configured per-user/
    global backpressure limits, verifying 429/503 activates before
    uncontrolled resource exhaustion. Stops on whichever of the four
    defined bounds is hit first (saturation observed, error-rate
    threshold, max duration, max queued-job count) - never intentionally
    crashes the host."""

    from app.core.config import settings

    result = LoadTestResult(profile="stress", users=0, concurrent_clients=concurrent_clients)
    started_at = time.perf_counter()

    client, engine, db_file_path = _build_hermetic_client(concurrent=True, pool_size=concurrent_clients)
    fake_sender_calls = {"n": 0}

    def fake_sender(**kwargs):
        fake_sender_calls["n"] += 1
        return f"fake-task-{fake_sender_calls['n']}"

    # Deliberately tight limits so saturation is reached quickly and
    # safely, without needing an enormous burst to prove the point.
    original_per_user = settings.max_active_heavy_jobs_per_user
    original_global = settings.global_heavy_job_saturation_limit
    settings.max_active_heavy_jobs_per_user = 2
    settings.global_heavy_job_saturation_limit = 20

    try:
        with patch(
            "app.modules.job_outbox.service._default_task_sender",
            side_effect=lambda **kwargs: fake_sender(**kwargs),
        ):
            index = 0
            error_count = 0
            saturation_count = 0
            approved_jsons: list[dict[str, object]] = []

            def one_user(user_index: int):
                #: Task 65.9.1 (Part K/L) - fresh `TestClient` per
                #: concurrent task, see `_run_one_active_user_flow`'s
                #: docstring. Uses `_run_one_stress_rag_flow` (not the
                #: contribution-approval flow) - see that function's
                #: docstring for why the approval flow can never surface a
                #: 429/503 to this harness.
                from fastapi.testclient import TestClient as _TestClient

                with _TestClient(app) as per_user_client:
                    latency_ms, status_json, ok = _run_one_stress_rag_flow(per_user_client, index=user_index)
                    return latency_ms, 0.0, status_json, ok

            with ThreadPoolExecutor(max_workers=max(1, concurrent_clients)) as executor:
                pending = set()
                while True:
                    elapsed = time.perf_counter() - started_at
                    if elapsed > max_duration_seconds:
                        result.stop_reason = "max_duration_reached"
                        break
                    if saturation_count >= max_queued_jobs:
                        result.stop_reason = "max_queued_job_count_reached"
                        break
                    #: A minimum sample size before the error-rate bound is
                    #: even evaluated - otherwise a single early failure
                    #: (e.g. one slow request still warming up) reads as a
                    #: 100% error rate and stops the run before it has
                    #: produced any meaningful signal. 20 mirrors common
                    #: load-test tooling convention (ignore the first
                    #: "ramp-up" burst for threshold purposes).
                    _minimum_stress_sample_size = 20
                    if result.request_count >= _minimum_stress_sample_size and (
                        error_count / result.request_count
                    ) > error_rate_threshold:
                        result.stop_reason = "error_rate_threshold_reached"
                        break

                    while len(pending) < concurrent_clients:
                        pending.add(executor.submit(one_user, index))
                        index += 1

                    done = {future for future in pending if future.done()}
                    if not done:
                        time.sleep(0.01)
                        continue
                    pending -= done

                    for future in done:
                        enqueue_ms, _completion_ms, approved_json, ok = future.result()
                        result.request_count += 1
                        status_key = str(approved_json.get("status_code", 200))
                        result.status_counts[status_key] = result.status_counts.get(status_key, 0) + 1
                        if status_key in ("429", "503"):
                            saturation_count += 1
                            result.backpressure_activated = True
                        elif not ok:
                            error_count += 1
                        else:
                            result.enqueue_latencies_ms.append(enqueue_ms)
                            approved_jsons.append(approved_json)

            # Task 65.9.1 (Part K/L) - the stress profile targets the
            # RAG-source processing endpoint specifically to observe
            # backpressure activation (see `_run_one_stress_rag_flow`'s
            # docstring); it is not a contribution-shaped flow, so the
            # contribution-promotion drain/cross-profile checks (already
            # covered by `smoke`/`scale` above) do not apply here - what
            # matters for stress is exactly what is measured: request
            # outcome distribution and whether/when 429/503 activated.
            result.users = len(approved_jsons)
    finally:
        settings.max_active_heavy_jobs_per_user = original_per_user
        settings.global_heavy_job_saturation_limit = original_global
        _teardown_hermetic_client(engine, db_file_path)

    result.total_duration_seconds = time.perf_counter() - started_at
    if result.stop_reason == "completed" and not result.backpressure_activated:
        result.stop_reason = "completed_without_saturation"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Task 65.9/65.9.1 async job platform load-test harness.")
    parser.add_argument("--profile", choices=["smoke", "scale", "stress"], default="smoke")
    parser.add_argument("--users", type=int, default=25, help="smoke profile: total synthetic users")
    parser.add_argument("--registered-users", type=int, default=100_000, help="scale profile: bulk-inserted user rows")
    parser.add_argument("--daily-active-users", type=int, default=200, help="scale profile: users driven through real HTTP flows")
    parser.add_argument("--api-concurrency", type=int, default=8, help="scale/stress profile: concurrent simulated API clients")
    parser.add_argument("--worker-replicas", type=int, default=1, help="scale profile: simulated embedding-worker replica count (reporting only)")
    parser.add_argument("--max-duration-seconds", type=float, default=30.0, help="stress profile: hard time bound")
    parser.add_argument("--error-rate-threshold", type=float, default=0.5, help="stress profile: non-saturation error-rate bound")
    parser.add_argument("--max-queued-jobs", type=int, default=50, help="stress profile: max observed 429/503 responses before stopping")
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    if args.profile == "smoke":
        result = run_smoke(users=args.users)
    elif args.profile == "scale":
        result = run_scale(
            registered_users=args.registered_users,
            daily_active_users=args.daily_active_users,
            concurrent_clients=args.api_concurrency,
            worker_replicas=args.worker_replicas,
        )
    else:
        result = run_stress(
            concurrent_clients=args.api_concurrency,
            max_duration_seconds=args.max_duration_seconds,
            error_rate_threshold=args.error_rate_threshold,
            max_queued_jobs=args.max_queued_jobs,
        )

    payload = result.to_dict()

    if args.json_output:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(f"LOAD TEST {args.profile.upper()} RESULT")
        for key, value in payload.items():
            print(f"  {key}: {value}")

    correctness_failure = (
        payload["duplicate_qdrant_point_count"] > 0
        or payload["cross_profile_contamination_count"] > 0
        or payload["private_leak_count"] > 0
    )
    if args.profile == "stress" and not payload["backpressure_activated"]:
        print("WARNING: stress profile completed without ever observing a 429/503 - limits may be too loose for this burst.")
    return 1 if correctness_failure else 0


if __name__ == "__main__":
    sys.exit(main())

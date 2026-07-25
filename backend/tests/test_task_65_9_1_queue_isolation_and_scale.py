"""Task 65.9.1 - Queue Isolation, Async Status Polling, and Production
Scale Verification Closure.

Covers, at the code/DB level (the Compose-topology contract test lives
separately in `backend/tests_infra/` - see that module's docstring for
why): explicit task routing coverage (Part C/E), the periodic queue/job
metric updater (Part H), expanded backpressure coverage on the RAG-source
processing endpoint (Part I), and job-id exposure for contribution
retry-indexing status polling (Part F). Fake-safe throughout - no real
embedding provider, no real DeepSeek call, no model download.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.core.metrics import ASYNC_OLDEST_JOB_AGE_SECONDS, ASYNC_QUEUE_DEPTH, ASYNC_QUEUE_METRICS_REFRESH_FAILURE_TOTAL
from app.db.session import get_db
from app.main import app
from app.modules.job_tracking import repository as job_tracking_repository
from app.modules.job_tracking import service as job_tracking_service
from app.modules.job_tracking.enums import BackgroundJobType
from app.worker.celery_app import ALL_QUEUES, GENERAL_WORKER_QUEUES, celery_app


PASSWORD = "StrongPass123"


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _create_profile(client, token: str, name: str) -> int:
    response = client.post("/api/memory-profiles", headers=_auth_headers(token), json={"name": name})
    return response.json()["id"]


def _create_memorial(client, token: str, name: str = "Queue Isolation Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Pipeline Source",
        "raw_text": "Sentence one. Sentence two. Sentence three.",
        "source_type": "manual_text",
    }
    payload.update(overrides)
    return client.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
        json=payload,
    )


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def _close(session_generator) -> None:
    try:
        next(session_generator)
    except StopIteration:
        pass


# =============================================================================
# Part C/E - task-routing coverage
# =============================================================================

#: Celery registers a handful of its own built-in tasks (chord/backend
#: cleanup helpers etc.) - these are framework machinery, never real
#: product tasks, and are excluded from the "every real task has an
#: explicit route" check by name prefix, matching Celery's own convention.
_CELERY_BUILTIN_TASK_PREFIX = "celery."


def _registered_product_task_names() -> list[str]:
    return [
        name
        for name in celery_app.tasks.keys()
        if not name.startswith(_CELERY_BUILTIN_TASK_PREFIX)
    ]


def test_every_registered_product_task_has_an_explicit_route():
    routes = celery_app.conf.task_routes
    for task_name in _registered_product_task_names():
        assert task_name in routes, f"{task_name} has no explicit route - would fall back to the default queue"
        assert routes[task_name]["queue"] in ALL_QUEUES


def test_embedding_heavy_tasks_route_to_embedding_queue():
    routes = celery_app.conf.task_routes
    for task_name in (
        "app.worker.tasks.run_avatar_memory_indexing_job",
        "app.worker.tasks.run_memorial_contribution_indexing_job",
        "app.worker.tasks.run_biography_indexing_job",
        "app.worker.tasks.run_rag_source_processing_job",
        "app.worker.tasks.run_multi_embedding_eval_job",
    ):
        assert routes[task_name]["queue"] == "embedding"


def test_maintenance_tasks_route_to_maintenance_queue():
    routes = celery_app.conf.task_routes
    for task_name in (
        "app.worker.tasks.run_outbox_dispatch_job",
        "app.worker.tasks.run_stale_job_recovery_job",
        "app.worker.tasks.run_job_smoke_test",
        "app.worker.tasks.run_async_queue_metrics_refresh_job",
    ):
        assert routes[task_name]["queue"] == "maintenance"


def test_general_worker_queue_list_excludes_embedding_and_maintenance():
    assert "embedding" not in GENERAL_WORKER_QUEUES
    assert "maintenance" not in GENERAL_WORKER_QUEUES
    assert GENERAL_WORKER_QUEUES == ("document_processing", "ai_generation", "media", "notifications")


def test_no_heavy_task_routes_to_the_bare_default_queue():
    assert celery_app.conf.task_default_queue == "maintenance"
    for task_name in (
        "app.worker.tasks.run_avatar_memory_indexing_job",
        "app.worker.tasks.run_memorial_contribution_indexing_job",
        "app.worker.tasks.run_biography_indexing_job",
        "app.worker.tasks.run_rag_source_processing_job",
    ):
        assert celery_app.conf.task_routes[task_name]["queue"] != celery_app.conf.task_default_queue


def test_beat_schedule_only_dispatches_to_the_maintenance_queue():
    for entry in celery_app.conf.beat_schedule.values():
        assert entry["options"]["queue"] == "maintenance"


def test_job_creation_schema_has_no_user_controlled_queue_field():
    """Part D.7 / N.1: user input must never determine a raw queue name.
    `BackgroundJobSmokeTestCreate` (the only user-facing job-creation
    payload) must not expose a `queue` field at all - every real queue
    assignment in this codebase is a fixed, code-only literal
    (`queue="embedding"` etc.), never taken from request JSON."""

    from app.modules.job_tracking.schemas import BackgroundJobSmokeTestCreate

    assert "queue" not in BackgroundJobSmokeTestCreate.model_fields


# =============================================================================
# Part H - periodic queue/job metric updater
# =============================================================================


def test_refresh_resets_every_known_queue_including_empty_ones(client):
    db, session_generator = _get_test_db_session()
    try:
        result = job_tracking_service.refresh_async_queue_metrics(db)
        assert result.ok is True
        assert set(result.queue_depths.keys()) == set(ALL_QUEUES)
        for queue in ALL_QUEUES:
            assert result.queue_depths[queue] == 0
            assert result.oldest_ages_seconds[queue] == 0.0
            assert ASYNC_QUEUE_DEPTH.labels(queue)._value.get() == 0
            assert ASYNC_OLDEST_JOB_AGE_SECONDS.labels(queue)._value.get() == 0.0
    finally:
        _close(session_generator)


def test_refresh_counts_one_active_job_in_its_queue_only(client):
    db, session_generator = _get_test_db_session()
    try:
        job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-single-active",
        )
        result = job_tracking_service.refresh_async_queue_metrics(db)
        assert result.queue_depths["embedding"] == 1
        for queue in ALL_QUEUES:
            if queue != "embedding":
                assert result.queue_depths[queue] == 0
    finally:
        _close(session_generator)


def test_refresh_counts_multiple_queues_independently(client):
    db, session_generator = _get_test_db_session()
    try:
        job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-multi-embedding-1",
        )
        job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-multi-embedding-2",
        )
        job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.SMOKE_TEST, input_payload={}, queue="maintenance",
        )
        result = job_tracking_service.refresh_async_queue_metrics(db)
        assert result.queue_depths["embedding"] == 2
        assert result.queue_depths["maintenance"] == 1
    finally:
        _close(session_generator)


def test_refresh_excludes_terminal_jobs_from_active_depth(client):
    db, session_generator = _get_test_db_session()
    try:
        succeeded_job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-terminal-succeeded",
        )
        job_tracking_service.mark_running(db, job_id=succeeded_job.id)
        job_tracking_service.mark_succeeded(db, job_id=succeeded_job.id, result_payload={})

        failed_job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-terminal-failed",
        )
        job_tracking_service.mark_failed(db, job_id=failed_job.id, error_message="failed")

        active_job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-terminal-active",
        )

        result = job_tracking_service.refresh_async_queue_metrics(db)
        assert result.queue_depths["embedding"] == 1
        assert active_job.status == "pending"
    finally:
        _close(session_generator)


def test_oldest_active_job_age_reflects_the_oldest_created_at(client):
    db, session_generator = _get_test_db_session()
    try:
        older_job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-age-older",
        )
        older_job.created_at = datetime.now(timezone.utc) - timedelta(seconds=120)
        db.commit()
        job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-age-newer",
        )

        result = job_tracking_service.refresh_async_queue_metrics(db)
        assert result.oldest_ages_seconds["embedding"] >= 119
    finally:
        _close(session_generator)


def test_stale_gauge_resets_to_zero_once_queue_drains(client):
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="metrics-drain",
        )
        first = job_tracking_service.refresh_async_queue_metrics(db)
        assert first.queue_depths["embedding"] == 1

        job_tracking_service.mark_running(db, job_id=job.id)
        job_tracking_service.mark_succeeded(db, job_id=job.id, result_payload={})

        second = job_tracking_service.refresh_async_queue_metrics(db)
        assert second.queue_depths["embedding"] == 0
        assert ASYNC_QUEUE_DEPTH.labels("embedding")._value.get() == 0
    finally:
        _close(session_generator)


def test_database_failure_is_safe_and_increments_failure_counter(client, monkeypatch):
    db, session_generator = _get_test_db_session()
    try:
        def _boom(*args, **kwargs):
            raise SQLAlchemyError("database unavailable")

        monkeypatch.setattr(job_tracking_repository, "get_active_job_counts_by_queue", _boom)
        before = ASYNC_QUEUE_METRICS_REFRESH_FAILURE_TOTAL._value.get()

        result = job_tracking_service.refresh_async_queue_metrics(db)

        assert result.ok is False
        after = ASYNC_QUEUE_METRICS_REFRESH_FAILURE_TOTAL._value.get()
        assert after == before + 1
    finally:
        _close(session_generator)


def test_metric_refresh_task_is_routed_to_maintenance_and_runs_end_to_end(client, monkeypatch):
    """The Celery task wrapper is routed to `maintenance` and, called
    directly (the same convention this codebase's other maintenance-task
    tests use for `run_outbox_dispatch_job`/`run_stale_job_recovery_job`),
    completes successfully using the test's own session factory."""

    from app.worker import tasks as worker_tasks

    assert celery_app.conf.task_routes["app.worker.tasks.run_async_queue_metrics_refresh_job"]["queue"] == "maintenance"
    monkeypatch.setattr(worker_tasks, "get_session_factory", lambda: app.state.testing_session_local)

    result = worker_tasks.run_async_queue_metrics_refresh_job()

    assert result["ok"] is True
    assert set(result["queue_depths"].keys()) == set(ALL_QUEUES)


# =============================================================================
# Part I - expanded backpressure coverage (RAG-source processing endpoint)
# =============================================================================


def test_rag_source_processing_endpoint_is_now_subject_to_per_user_backpressure(client, monkeypatch):
    token = _register_and_login(client, "rag-backpressure-user@example.com")
    profile_id = _create_profile(client, token, "Backpressure Profile")
    source_one = _create_rag_source(client, token, profile_id).json()["id"]
    source_two = _create_rag_source(client, token, profile_id, title="Second source").json()["id"]

    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_user", 1)

    first = client.post(f"/api/rag-sources/{source_one}/process", headers=_auth_headers(token))
    assert first.status_code == 200
    assert first.json()["status"] == "queued"

    second = client.post(f"/api/rag-sources/{source_two}/process", headers=_auth_headers(token))
    assert second.status_code == 429


def test_rag_source_processing_retry_reuses_the_active_job_instead_of_creating_a_duplicate(client):
    token = _register_and_login(client, "rag-idempotent-retry@example.com")
    profile_id = _create_profile(client, token, "Idempotent Retry Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    first = client.post(f"/api/rag-sources/{source_id}/process", headers=_auth_headers(token))
    second = client.post(f"/api/rag-sources/{source_id}/process", headers=_auth_headers(token))

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["id"] == second.json()["id"]


def test_contribution_retry_indexing_returns_429_on_saturation_not_500(client, monkeypatch):
    """Regression: `retry_contribution_indexing_endpoint` previously let
    `PerUserActiveJobLimitExceededError` propagate as an unhandled 500 -
    the backpressure limit was enforced in the service layer but never
    translated into the documented 429 response at the API boundary."""

    owner_token = _register_and_login(client, "retry-backpressure-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submit = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(owner_token),
        json={"title": "T", "memory_text": "Some memory text.", "privacy_scope": "all_family"},
    )
    contribution_id = submit.json()["id"]
    approve = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "confirmed"},
    )
    assert approve.status_code == 200

    db, session_generator = _get_test_db_session()
    try:
        from app.modules.memorial_contribution_indexing import repository as contribution_indexing_repository
        from app.modules.memorial_contribution_indexing.service import get_active_indexing_job_id_for_promotion

        promotion = contribution_indexing_repository.get_promotion_by_contribution_id(
            db, contribution_id=contribution_id
        )
        # The original approval-triggered job must itself reach a terminal
        # state too (not only the promotion row) - otherwise retry's own
        # idempotency-key lookup would legitimately reuse that still-active
        # job (Part I.9) rather than attempt to create a *new* one, and
        # would never reach the backpressure check being tested here.
        original_job_id = get_active_indexing_job_id_for_promotion(db, promotion_id=promotion.id)
        assert original_job_id is not None
        job_tracking_service.mark_failed(db, job_id=original_job_id, error_message="simulated failure")
        promotion.promotion_status = "failed"
        db.commit()
    finally:
        _close(session_generator)

    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_user", 0)
    response = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/retry-indexing",
        headers=_auth_headers(owner_token),
    )
    assert response.status_code == 429


def test_biography_ingestion_returns_429_on_saturation_not_500(client, monkeypatch):
    """Regression: `start_biography_ingestion_endpoint` previously let the
    same backpressure exceptions propagate as an unhandled 500."""

    owner_token = _register_and_login(client, "biography-backpressure-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(owner_token),
        json={"biography": "A short life story with enough words to be eligible for ingestion." * 3},
    )
    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_user", 0)

    response = client.post(
        f"/api/memorials/{profile_id}/biography/ingest",
        headers=_auth_headers(owner_token),
    )
    assert response.status_code == 429


# =============================================================================
# Part F - job_id exposure for contribution indexing status polling
# =============================================================================


def test_approving_a_contribution_exposes_the_active_indexing_job_id(client):
    owner_token = _register_and_login(client, "job-id-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submit = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(owner_token),
        json={"title": "T", "memory_text": "Some memory text.", "privacy_scope": "all_family"},
    )
    approve = client.post(
        f"/api/memorials/{profile_id}/contributions/{submit.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "confirmed"},
    )
    assert approve.status_code == 200
    body = approve.json()
    assert body["indexing_status"]["state"] == "pending"
    job_id = body["indexing_status"]["job_id"]
    assert job_id is not None

    job_response = client.get(f"/api/jobs/{job_id}", headers=_auth_headers(owner_token))
    assert job_response.status_code == 200
    assert job_response.json()["status"] in ("pending", "queued", "running")


def test_a_different_account_cannot_see_the_job_id_owners_job_status(client):
    owner_token = _register_and_login(client, "job-id-owner-2@example.com")
    other_token = _register_and_login(client, "job-id-other-2@example.com")
    profile_id = _create_memorial(client, owner_token)
    submit = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(owner_token),
        json={"title": "T", "memory_text": "Some memory text.", "privacy_scope": "all_family"},
    )
    approve = client.post(
        f"/api/memorials/{profile_id}/contributions/{submit.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "confirmed"},
    )
    job_id = approve.json()["indexing_status"]["job_id"]
    assert job_id is not None

    other_response = client.get(f"/api/jobs/{job_id}", headers=_auth_headers(other_token))
    assert other_response.status_code == 404

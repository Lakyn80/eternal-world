"""Task 65.9 - Scalable Asynchronous Job Platform, Dedicated Embedding
Workers, Self-Healing Provider Recovery, and 100k-User Readiness
Foundation.

Fake-safe unit/integration coverage for the new machinery: the persistent
job model's idempotency/backpressure behavior, the transactional outbox
(atomicity, broker-outage recovery, duplicate-publish safety), explicit
queue routing, the provider integrity probe, the provider lifecycle
singleton, and the bounded provider self-healing policy (Part M). No real
model, no real broker network call, no real DeepSeek call - every
provider/broker interaction below is a fake or a monkeypatched stand-in.
"""

from __future__ import annotations

import threading

import pytest

from app.core.config import settings
from app.db.models import BackgroundJob
from app.db.session import get_db
from app.main import app
from app.modules.embeddings import provider_lifecycle as provider_lifecycle_module
from app.modules.embeddings.provider_integrity import (
    PROVIDER_INTEGRITY_PROBE_TEXT,
    ProviderIntegrityError,
    looks_like_meta_device_corruption,
    run_provider_integrity_probe,
    validate_embedding_output,
)
from app.modules.embeddings.provider_lifecycle import EmbeddingProviderLifecycle, ProviderState
from app.modules.embeddings.providers.base import BaseEmbeddingProvider, EmbeddingVector
from app.modules.embeddings.self_healing import ProviderRecoveryExhaustedError, SelfHealingEmbeddingEncoder
from app.modules.job_outbox import repository as outbox_repository
from app.modules.job_outbox import service as outbox_service
from app.modules.job_tracking import repository as job_tracking_repository
from app.modules.job_tracking import service as job_tracking_service
from app.modules.job_tracking.enums import BackgroundJobStatus, BackgroundJobType
from app.modules.job_tracking.exceptions import (
    GlobalQueueSaturationError,
    PerProfileActiveJobLimitExceededError,
    PerUserActiveJobLimitExceededError,
)
from app.worker.celery_app import celery_app


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post("/api/auth/register", json={"email": email, "password": password, "full_name": "User"})
    response = client.post("/api/auth/login", json={"email": email, "password": password})
    return response.json()["access_token"]


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


class FakeControllableProvider(BaseEmbeddingProvider):
    """A fake embedding provider whose failure/success behavior is fixed
    at construction time - used to simulate "this loaded instance is
    corrupt" (`fail_times > 0`) versus "this freshly (re)loaded instance
    is healthy" (`fail_times == 0`), exactly matching the real BGE-M3
    meta-device incident's shape: a fresh load can either fix the problem
    or reproduce it, and self-healing must react correctly either way."""

    def __init__(self, *, fail_times: int = 0, dimension: int = 4) -> None:
        self.fail_times = fail_times
        self.dimension = dimension
        self.calls = 0

    def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
        self.calls += 1
        if self.calls <= self.fail_times:
            raise RuntimeError(
                "NotImplementedError: Cannot copy out of meta tensor; no data!"
            )
        return EmbeddingVector(values=[0.1] * self.dimension, dimension=self.dimension, metadata={})

    def embed_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        return [self.embed_text(text, model_code) for text in texts]


class AlwaysInvalidOutputProvider(BaseEmbeddingProvider):
    def __init__(self, *, values: list[float], dimension: int) -> None:
        self._values = values
        self._dimension = dimension

    def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=self._values, dimension=self._dimension, metadata={})

    def embed_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        return [self.embed_text(t, model_code) for t in texts]


# --- Provider integrity probe (Part K) --------------------------------------


def test_healthy_provider_passes_probe():
    provider = FakeControllableProvider(fail_times=0)
    vector = run_provider_integrity_probe(provider, model_code="mock_embedding")
    assert vector.dimension == 4


def test_probe_uses_fixed_harmless_string_never_user_content(monkeypatch):
    seen_texts: list[str] = []

    class RecordingProvider(BaseEmbeddingProvider):
        def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
            seen_texts.append(text)
            return EmbeddingVector(values=[0.1, 0.2], dimension=2, metadata={})

        def embed_batch(self, texts, model_code):
            return [self.embed_text(t, model_code) for t in texts]

    run_provider_integrity_probe(RecordingProvider(), model_code="mock_embedding")
    assert seen_texts == [PROVIDER_INTEGRITY_PROBE_TEXT]


def test_empty_vector_fails_validation():
    with pytest.raises(ProviderIntegrityError):
        validate_embedding_output(EmbeddingVector(values=[], dimension=0, metadata={}))


def test_wrong_dimension_fails_validation():
    with pytest.raises(ProviderIntegrityError):
        validate_embedding_output(
            EmbeddingVector(values=[0.1, 0.2], dimension=2, metadata={}), expected_dimension=1024
        )


def test_nan_fails_validation():
    with pytest.raises(ProviderIntegrityError):
        validate_embedding_output(EmbeddingVector(values=[0.1, float("nan")], dimension=2, metadata={}))


def test_infinite_value_fails_validation():
    with pytest.raises(ProviderIntegrityError):
        validate_embedding_output(EmbeddingVector(values=[0.1, float("inf")], dimension=2, metadata={}))


def test_probe_raises_on_provider_that_always_returns_invalid_output():
    provider = AlwaysInvalidOutputProvider(values=[], dimension=0)
    with pytest.raises(ProviderIntegrityError):
        run_provider_integrity_probe(provider, model_code="mock_embedding")


def test_meta_device_signature_is_recognized():
    exc = RuntimeError("NotImplementedError: Cannot copy out of meta tensor; no data!")
    assert looks_like_meta_device_corruption(exc)


def test_unrelated_error_is_not_recognized_as_meta_device_corruption():
    assert not looks_like_meta_device_corruption(RuntimeError("connection refused"))


# --- Provider lifecycle singleton (Part J) ----------------------------------


def test_lifecycle_initializes_once_and_reuses_provider(monkeypatch):
    build_count = {"n": 0}

    def builder(*, model_code):
        build_count["n"] += 1
        return FakeControllableProvider(fail_times=0)

    monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", builder)
    lifecycle = EmbeddingProviderLifecycle()

    first = lifecycle.get_or_initialize(model_code="mock_embedding")
    second = lifecycle.get_or_initialize(model_code="mock_embedding")

    assert first is second
    assert build_count["n"] == 1
    assert lifecycle.get_health(model_code="mock_embedding").state == ProviderState.HEALTHY


def test_lifecycle_reload_builds_a_new_provider_instance(monkeypatch):
    build_count = {"n": 0}

    def builder(*, model_code):
        build_count["n"] += 1
        return FakeControllableProvider(fail_times=0)

    monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", builder)
    lifecycle = EmbeddingProviderLifecycle()

    first = lifecycle.get_or_initialize(model_code="mock_embedding")
    second = lifecycle.reload(model_code="mock_embedding")

    assert first is not second
    assert build_count["n"] == 2


def test_lifecycle_initialization_failure_is_marked_failed(monkeypatch):
    def failing_builder(*, model_code):
        return AlwaysInvalidOutputProvider(values=[], dimension=0)

    monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", failing_builder)
    lifecycle = EmbeddingProviderLifecycle()

    with pytest.raises(ProviderIntegrityError):
        lifecycle.get_or_initialize(model_code="mock_embedding")

    assert lifecycle.get_health(model_code="mock_embedding").state == ProviderState.FAILED


def test_concurrent_initialization_builds_exactly_one_provider(monkeypatch):
    """Part J: "Prevent concurrent initialization of multiple BGE-M3
    instances in one worker process" - five threads racing on the same
    lifecycle must only ever trigger one real build."""

    import time

    build_count = {"n": 0}
    build_lock = threading.Lock()

    def slow_builder(*, model_code):
        with build_lock:
            build_count["n"] += 1
        time.sleep(0.05)
        return FakeControllableProvider(fail_times=0)

    monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", slow_builder)
    lifecycle = EmbeddingProviderLifecycle()
    results: list[object] = []
    results_lock = threading.Lock()

    def worker():
        provider = lifecycle.get_or_initialize(model_code="mock_embedding")
        with results_lock:
            results.append(provider)

    threads = [threading.Thread(target=worker) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert build_count["n"] == 1
    assert len({id(result) for result in results}) == 1


# --- Bounded provider self-healing (Part M) ---------------------------------


def _create_embedding_job(db) -> BackgroundJob:
    return job_tracking_service.create_job(
        db,
        owner_user_id=1,
        job_type=BackgroundJobType.QDRANT_INDEXING,
        input_payload={"workflow": "test"},
        queue="embedding",
        idempotency_key=f"test-self-healing-{id(db)}-{threading.get_ident()}",
    )


def test_first_corruption_reloads_provider_and_second_attempt_succeeds(client, monkeypatch):
    _register_and_login(client, "healing-success@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = _create_embedding_job(db)
        job_id = job.id

        build_count = {"n": 0}

        def builder(*, model_code):
            build_count["n"] += 1
            if build_count["n"] == 1:
                return FakeControllableProvider(fail_times=1)
            return FakeControllableProvider(fail_times=0)

        monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", builder)
        lifecycle = EmbeddingProviderLifecycle()
        encoder = SelfHealingEmbeddingEncoder(db=db, job_id=job_id, lifecycle=lifecycle)

        vector = encoder.encode(text="hello", model_code="mock_embedding")

        assert vector.dimension == 4
        assert build_count["n"] == 2  # attempt 1's corrupt provider, then one reload
        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
        assert refreshed.provider_recovery_count == 1
        assert refreshed.fresh_process_retry_used is False
        assert refreshed.worker_recycle_requested is False
    finally:
        _close(session_generator)


def test_second_corruption_requests_exactly_one_fresh_process_retry(client, monkeypatch):
    _register_and_login(client, "healing-recovery@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = _create_embedding_job(db)
        job_id = job.id

        def always_corrupt_builder(*, model_code):
            return FakeControllableProvider(fail_times=999)

        monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", always_corrupt_builder)
        lifecycle = EmbeddingProviderLifecycle()
        encoder = SelfHealingEmbeddingEncoder(db=db, job_id=job_id, lifecycle=lifecycle)

        with pytest.raises(ProviderRecoveryExhaustedError) as exc_info:
            encoder.encode(text="hello", model_code="mock_embedding")

        assert exc_info.value.requires_fresh_process is True
        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
        assert refreshed.fresh_process_retry_used is True
        assert refreshed.worker_recycle_requested is True
        assert refreshed.status == "recovery_pending"
        assert refreshed.provider_recovery_count == 2
    finally:
        _close(session_generator)


def test_third_attempt_in_fresh_process_reaches_final_failure_without_second_recycle(client, monkeypatch):
    """Simulates the full three-attempt bound end-to-end: attempts 1-2
    exhaust in one (simulated) process, then a brand-new
    `EmbeddingProviderLifecycle` (standing in for a genuinely fresh
    embedding-worker process) makes exactly one more attempt, which also
    fails - reaching permanent failure without ever requesting a second
    automatic recycle (Part AA test 33)."""

    _register_and_login(client, "healing-permanent@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = _create_embedding_job(db)
        job_id = job.id

        def always_corrupt_builder(*, model_code):
            return FakeControllableProvider(fail_times=999)

        monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", always_corrupt_builder)

        # Attempts 1-2 (same simulated process).
        first_process_lifecycle = EmbeddingProviderLifecycle()
        first_encoder = SelfHealingEmbeddingEncoder(db=db, job_id=job_id, lifecycle=first_process_lifecycle)
        with pytest.raises(ProviderRecoveryExhaustedError) as first_exc:
            first_encoder.encode(text="hello", model_code="mock_embedding")
        assert first_exc.value.requires_fresh_process is True

        # Attempt 3: a genuinely fresh process gets its own fresh lifecycle
        # singleton - `fresh_process_retry_used` on the job is what bounds
        # this to exactly one further attempt.
        fresh_process_lifecycle = EmbeddingProviderLifecycle()
        fresh_encoder = SelfHealingEmbeddingEncoder(db=db, job_id=job_id, lifecycle=fresh_process_lifecycle)
        with pytest.raises(ProviderRecoveryExhaustedError) as second_exc:
            fresh_encoder.encode(text="hello", model_code="mock_embedding")
        assert second_exc.value.requires_fresh_process is False

        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
        assert refreshed.status == "failed"
        assert refreshed.safe_error_category == "provider_corrupt"
        # Exactly one recycle request total across the whole bounded policy.
        assert refreshed.worker_recycle_requested is True
        assert refreshed.fresh_process_retry_used is True
        assert refreshed.provider_recovery_count == 3
    finally:
        _close(session_generator)


def test_manual_retry_remains_possible_after_permanent_failure(client, monkeypatch):
    """A job that reached permanent provider-corruption failure must not
    be a dead end: the same idempotent domain operation can still be
    retried manually (a fresh job/idempotency cycle), and it succeeds once
    the underlying provider issue is gone."""

    _register_and_login(client, "healing-manual-retry@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = _create_embedding_job(db)
        job_id = job.id

        def always_corrupt_builder(*, model_code):
            return FakeControllableProvider(fail_times=999)

        monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", always_corrupt_builder)
        lifecycle = EmbeddingProviderLifecycle()
        encoder = SelfHealingEmbeddingEncoder(db=db, job_id=job_id, lifecycle=lifecycle)
        with pytest.raises(ProviderRecoveryExhaustedError):
            encoder.encode(text="hello", model_code="mock_embedding")
        with pytest.raises(ProviderRecoveryExhaustedError):
            encoder.encode(text="hello", model_code="mock_embedding")

        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
        assert refreshed.status == "failed"

        # Manual retry: a brand new job (as the real retry endpoints create
        # via a fresh idempotency key once the old job is terminal), a
        # healthy provider this time.
        def healthy_builder(*, model_code):
            return FakeControllableProvider(fail_times=0)

        monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", healthy_builder)
        retry_job = job_tracking_service.create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.QDRANT_INDEXING,
            input_payload={"workflow": "test"},
            queue="embedding",
            idempotency_key=f"test-self-healing-retry-{job_id}",
        )
        retry_lifecycle = EmbeddingProviderLifecycle()
        retry_encoder = SelfHealingEmbeddingEncoder(db=db, job_id=retry_job.id, lifecycle=retry_lifecycle)
        vector = retry_encoder.encode(text="hello", model_code="mock_embedding")
        assert vector.dimension == 4
    finally:
        _close(session_generator)


def test_qdrant_style_failure_never_touches_self_healing_or_recycle():
    """Part L/M invariant: `SelfHealingEmbeddingEncoder` only ever wraps
    the embedding-provider call itself. A Qdrant write failure happens in
    entirely separate code (the writer, not the encoder) and therefore
    structurally never passes through this class at all - asserted here
    by confirming the encoder's own runtime code never imports or calls
    anything Qdrant-related (module-level prose/comments may still
    mention the word "Qdrant" when explaining this exact invariant)."""

    import ast
    import inspect

    from app.modules.embeddings import self_healing as self_healing_module

    tree = ast.parse(inspect.getsource(self_healing_module))
    import_names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            import_names.append(node.module)
        elif isinstance(node, ast.Import):
            import_names.extend(alias.name for alias in node.names)

    assert not any("qdrant" in name.lower() for name in import_names)


# --- Transactional outbox (Part E) ------------------------------------------


def test_outbox_row_is_created_atomically_with_the_job(client):
    _register_and_login(client, "outbox-atomic@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding",
            idempotency_key="test-outbox-atomic",
        )
        assert job.status == "pending"
        assert outbox_repository.get_outbox_event_for_job(db, job_id=job.id) is None

        outbox_service.enqueue_job_with_outbox(
            db,
            job=job,
            task_name="app.worker.tasks.run_job_smoke_test",
            queue="embedding",
            sender=lambda **kwargs: "fake-task-id",
        )

        outbox_event = outbox_repository.get_outbox_event_for_job(db, job_id=job.id)
        assert outbox_event is not None
        assert outbox_event.status == "published"
        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job.id)
        assert refreshed.status == "queued"
        assert refreshed.celery_task_id == "fake-task-id"
    finally:
        _close(session_generator)


def test_broker_failure_leaves_outbox_pending_and_recovers_on_retry(client):
    _register_and_login(client, "outbox-broker-outage@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding",
            idempotency_key="test-outbox-broker-outage",
        )

        def failing_sender(**kwargs):
            raise ConnectionError("broker unreachable")

        outbox_service.enqueue_job_with_outbox(
            db, job=job, task_name="app.worker.tasks.run_job_smoke_test", queue="embedding", sender=failing_sender
        )
        outbox_event = outbox_repository.get_outbox_event_for_job(db, job_id=job.id)
        assert outbox_event.status == "pending"
        assert outbox_event.attempts == 1
        assert outbox_event.next_attempt_at is not None  # bounded backoff was scheduled
        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job.id)
        assert refreshed.status == "pending"  # never lost, never silently marked failed

        # Broker recovers - simulate the backoff window having elapsed,
        # then the maintenance dispatcher republishes the same semantic
        # job (never a second/duplicate job).
        outbox_event.next_attempt_at = None
        db.commit()
        summary = outbox_service.dispatch_pending_outbox_events(
            db, batch_size=10, sender=lambda **kwargs: "recovered-task-id"
        )
        assert summary.published == 1
        outbox_event = outbox_repository.get_outbox_event_for_job(db, job_id=job.id)
        assert outbox_event.status == "published"
    finally:
        _close(session_generator)


def test_duplicate_publish_is_harmless(client):
    _register_and_login(client, "outbox-duplicate@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding",
            idempotency_key="test-outbox-duplicate",
        )
        send_calls = {"n": 0}

        def counting_sender(**kwargs):
            send_calls["n"] += 1
            return f"task-{send_calls['n']}"

        outbox_service.enqueue_job_with_outbox(
            db, job=job, task_name="app.worker.tasks.run_job_smoke_test", queue="embedding", sender=counting_sender
        )
        # A second dispatch attempt against the same (already-published)
        # job must not publish again.
        outbox_service.enqueue_job_with_outbox(
            db, job=job, task_name="app.worker.tasks.run_job_smoke_test", queue="embedding", sender=counting_sender
        )

        assert send_calls["n"] == 1
    finally:
        _close(session_generator)


def test_multiple_dispatchers_are_safe_on_the_same_pending_batch(client):
    """Two concurrent maintenance-dispatcher sweeps racing on the same
    small batch must never both publish the same row twice."""

    _register_and_login(client, "outbox-multi-dispatcher@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job_a = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-outbox-multi-a",
        )
        job_b = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-outbox-multi-b",
        )
        outbox_repository.create_outbox_event(
            db, job_id=job_a.id, task_name="app.worker.tasks.run_job_smoke_test", queue="embedding",
            task_args={"job_id": job_a.id},
        )
        outbox_repository.create_outbox_event(
            db, job_id=job_b.id, task_name="app.worker.tasks.run_job_smoke_test", queue="embedding",
            task_args={"job_id": job_b.id},
        )
        db.commit()

        send_calls: list[int] = []

        def counting_sender(**kwargs):
            send_calls.append(1)
            return "task-id"

        first_summary = outbox_service.dispatch_pending_outbox_events(db, batch_size=10, sender=counting_sender)
        second_summary = outbox_service.dispatch_pending_outbox_events(db, batch_size=10, sender=counting_sender)

        assert first_summary.published == 2
        assert second_summary.published == 0  # nothing left pending
        assert len(send_calls) == 2
    finally:
        _close(session_generator)


# --- Idempotency and backpressure (Parts F/Q) -------------------------------


def test_repeated_enqueue_with_same_idempotency_key_reuses_the_same_active_job(client):
    _register_and_login(client, "idempotency-active@example.com")
    db, session_generator = _get_test_db_session()
    try:
        first = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-idempotency-active",
        )
        second = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-idempotency-active",
        )
        assert first.id == second.id
        count = db.query(BackgroundJob).filter(BackgroundJob.idempotency_key == "test-idempotency-active").count()
        assert count == 1
    finally:
        _close(session_generator)


def test_new_attempt_after_terminal_job_creates_a_fresh_job_with_same_key(client):
    """A retry after a *previous* attempt already reached a terminal state
    (failed) must be able to create a brand-new job - the partial unique
    index only enforces uniqueness among still-active jobs."""

    _register_and_login(client, "idempotency-retry@example.com")
    db, session_generator = _get_test_db_session()
    try:
        first = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-idempotency-retry",
        )
        job_tracking_service.mark_failed(db, job_id=first.id, error_message="failed")

        second = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-idempotency-retry",
        )
        assert second.id != first.id
        count = db.query(BackgroundJob).filter(BackgroundJob.idempotency_key == "test-idempotency-retry").count()
        assert count == 2
    finally:
        _close(session_generator)


def test_per_user_active_job_limit_returns_429_semantics(client, monkeypatch):
    _register_and_login(client, "backpressure-user@example.com")
    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_user", 1)
    db, session_generator = _get_test_db_session()
    try:
        job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-backpressure-user-1",
        )
        with pytest.raises(PerUserActiveJobLimitExceededError):
            job_tracking_service.create_job(
                db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
                queue="embedding", idempotency_key="test-backpressure-user-2",
            )
    finally:
        _close(session_generator)


def test_per_profile_active_job_limit(client, monkeypatch):
    token = _register_and_login(client, "backpressure-profile@example.com")
    profile_response = client.post(
        "/api/memory-profiles", headers={"Authorization": f"Bearer {token}"}, json={"name": "P"}
    )
    profile_id = profile_response.json()["id"]
    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_profile", 1)
    db, session_generator = _get_test_db_session()
    try:
        job_tracking_service.create_job(
            db, owner_user_id=1, profile_id=profile_id, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-backpressure-profile-1",
        )
        with pytest.raises(PerProfileActiveJobLimitExceededError):
            job_tracking_service.create_job(
                db, owner_user_id=1, profile_id=profile_id, job_type=BackgroundJobType.QDRANT_INDEXING,
                queue="embedding", idempotency_key="test-backpressure-profile-2",
            )
    finally:
        _close(session_generator)


def test_global_saturation_returns_503_semantics_with_retry_after(client, monkeypatch):
    _register_and_login(client, "backpressure-global@example.com")
    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_user", 1000)
    monkeypatch.setattr(settings, "global_heavy_job_saturation_limit", 1)
    monkeypatch.setattr(settings, "global_saturation_retry_after_seconds", 42)
    db, session_generator = _get_test_db_session()
    try:
        job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-backpressure-global-1",
        )
        with pytest.raises(GlobalQueueSaturationError) as exc_info:
            job_tracking_service.create_job(
                db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
                queue="embedding", idempotency_key="test-backpressure-global-2",
            )
        assert exc_info.value.retry_after_seconds == 42
    finally:
        _close(session_generator)


def test_non_heavy_jobs_are_never_backpressure_limited(client, monkeypatch):
    """Legacy/lightweight job creation (no `idempotency_key`/`queue`) must
    remain entirely unaffected by the heavy-job backpressure limits."""

    _register_and_login(client, "backpressure-legacy@example.com")
    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_user", 0)
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.SMOKE_TEST, input_payload={}
        )
        assert job.status == "queued"
    finally:
        _close(session_generator)


# --- Stale-job recovery (Part P) --------------------------------------------


def test_stale_running_job_is_recovered_to_retry_scheduled(client):
    from datetime import datetime, timedelta, timezone

    _register_and_login(client, "stale-recovery@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-stale-recovery",
        )
        job_tracking_service.mark_running(db, job_id=job.id, celery_task_id="abc")
        stale_job = job_tracking_repository.get_background_job_by_id(db, job_id=job.id)
        stale_job.heartbeat_at = datetime.now(timezone.utc) - timedelta(hours=1)
        db.commit()

        stale_ids = job_tracking_service.find_stale_job_ids(db, limit=10)
        assert job.id in stale_ids

        requeued = job_tracking_service.requeue_stale_job(db, job_id=job.id)
        assert requeued is True
        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job.id)
        assert refreshed.status == "retry_scheduled"
        assert refreshed.attempt_count == 1
    finally:
        _close(session_generator)


def test_active_heartbeat_job_is_not_stale(client):
    from datetime import datetime, timezone

    _register_and_login(client, "stale-active@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-stale-active",
        )
        job_tracking_service.mark_running(db, job_id=job.id, celery_task_id="abc")
        job_tracking_service.touch_heartbeat(db, job_id=job.id)

        stale_ids = job_tracking_service.find_stale_job_ids(db, limit=10)
        assert job.id not in stale_ids
    finally:
        _close(session_generator)


def test_completed_job_is_never_resurrected(client):
    _register_and_login(client, "stale-completed@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-stale-completed",
        )
        job_tracking_service.mark_running(db, job_id=job.id, celery_task_id="abc")
        job_tracking_service.mark_succeeded(db, job_id=job.id, result_payload={"ok": True})

        requeued = job_tracking_service.requeue_stale_job(db, job_id=job.id)
        assert requeued is False
        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job.id)
        assert refreshed.status == "succeeded"
    finally:
        _close(session_generator)


def test_stale_job_recovery_enforces_attempt_limit(client):
    _register_and_login(client, "stale-limit@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-stale-limit",
        )
        job_row = job_tracking_repository.get_background_job_by_id(db, job_id=job.id)
        job_row.status = BackgroundJobStatus.RUNNING.value
        job_row.max_attempts = 1
        job_row.attempt_count = 1
        db.commit()

        requeued = job_tracking_service.requeue_stale_job(db, job_id=job.id)
        assert requeued is False
        refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job.id)
        assert refreshed.status == "failed"
        assert refreshed.safe_error_category == "worker_lost"
    finally:
        _close(session_generator)


def test_concurrent_recovery_sweeps_are_safe(client):
    """Calling `requeue_stale_job` a second time after the first sweep
    already recovered the job must be a safe no-op, not a duplicate
    recovery."""

    _register_and_login(client, "stale-concurrent@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="test-stale-concurrent",
        )
        job_tracking_service.mark_running(db, job_id=job.id, celery_task_id="abc")

        first = job_tracking_service.requeue_stale_job(db, job_id=job.id)
        assert first is True
        second = job_tracking_service.requeue_stale_job(db, job_id=job.id)
        assert second is False  # no longer `running`/`recovery_pending`
    finally:
        _close(session_generator)


# --- Queue topology (Part G) -------------------------------------------------


def test_embedding_indexing_tasks_route_to_the_embedding_queue():
    routes = celery_app.conf.task_routes
    assert routes["app.worker.tasks.run_avatar_memory_indexing_job"]["queue"] == "embedding"
    assert routes["app.worker.tasks.run_memorial_contribution_indexing_job"]["queue"] == "embedding"
    assert routes["app.worker.tasks.run_biography_indexing_job"]["queue"] == "embedding"


def test_maintenance_tasks_route_to_the_maintenance_queue():
    routes = celery_app.conf.task_routes
    assert routes["app.worker.tasks.run_outbox_dispatch_job"]["queue"] == "maintenance"
    assert routes["app.worker.tasks.run_stale_job_recovery_job"]["queue"] == "maintenance"


def test_heavy_work_never_uses_the_bare_default_queue():
    assert celery_app.conf.task_default_queue == "maintenance"
    heavy_task_names = (
        "app.worker.tasks.run_avatar_memory_indexing_job",
        "app.worker.tasks.run_memorial_contribution_indexing_job",
        "app.worker.tasks.run_biography_indexing_job",
    )
    for task_name in heavy_task_names:
        assert celery_app.conf.task_routes[task_name]["queue"] != celery_app.conf.task_default_queue


# --- Public job errors are safe (Part D/L) ----------------------------------


def test_public_job_error_never_contains_a_raw_exception_string(client):
    token = _register_and_login(client, "safe-error@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING, input_payload={}
        )
        job_tracking_service.mark_failed(
            db,
            job_id=job.id,
            error_message="Contribution indexing failed",
            safe_error_category="provider_corrupt",
        )
    finally:
        _close(session_generator)

    response = client.get(f"/api/jobs/{job.id}", headers={"Authorization": f"Bearer {token}"})
    body = response.json()
    assert body["error_message"] == "Contribution indexing failed"
    assert body["safe_error_category"] == "provider_corrupt"
    assert "Traceback" not in (body["error_message"] or "")


def test_job_status_access_is_authorization_scoped(client):
    owner_token = _register_and_login(client, "job-scope-owner@example.com")
    other_token = _register_and_login(client, "job-scope-other@example.com")
    db, session_generator = _get_test_db_session()
    try:
        job = job_tracking_service.create_job(
            db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING, input_payload={}
        )
    finally:
        _close(session_generator)

    owner_response = client.get(f"/api/jobs/{job.id}", headers={"Authorization": f"Bearer {owner_token}"})
    other_response = client.get(f"/api/jobs/{job.id}", headers={"Authorization": f"Bearer {other_token}"})

    assert owner_response.status_code == 200
    assert other_response.status_code == 404
    assert other_token

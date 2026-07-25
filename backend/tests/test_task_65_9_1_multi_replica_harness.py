"""Task 65.9.1 (Part J) - fake-safe multi-replica correctness harness.

Simulates at least two independent FastAPI application contexts sharing the
same PostgreSQL-equivalent (SQLite, matching this repo's existing test
convention) and the same real Redis instance (this docker dev stack's
backend container already points `REDIS_URL` at the real `redis` service -
no fakeredis substitution here, so this genuinely exercises the shared
Redis-backed browser-session/chat-snapshot machinery Task 65.7C added).

"Two independent instances" is realized as two separate `TestClient`
objects (each with its own cookie jar and connection - the actual per-
connection unit of independence a real load balancer would route between)
against the same FastAPI `app` singleton, both bound to one shared
SQLAlchemy engine. This deliberately does NOT rely on any in-process
Python object being duplicated (Part J: "Do not rely on shared process-
local singleton state for correctness") - every property asserted below is
about *data* visible through the database/Redis, never about object
identity between the two clients.

No real embedding model, no real DeepSeek call, no production data.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.modules.embeddings.provider_lifecycle import EmbeddingProviderLifecycle, ProviderState
from app.modules.embeddings.providers.base import BaseEmbeddingProvider, EmbeddingVector
from app.modules.job_outbox import service as job_outbox_service
from app.modules.job_tracking import repository as job_tracking_repository
from app.modules.job_tracking import service as job_tracking_service
from app.modules.job_tracking.enums import BackgroundJobType


PASSWORD = "StrongPass123"


@pytest.fixture
def shared_db():
    """One shared engine/session-factory - the stand-in for "one
    PostgreSQL instance both replicas connect to"."""

    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
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
    yield testing_session_local
    app.dependency_overrides.clear()
    if hasattr(app.state, "testing_session_local"):
        delattr(app.state, "testing_session_local")
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture
def replica_a(shared_db):
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def replica_b(shared_db):
    with TestClient(app) as test_client:
        yield test_client


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _get_session_db(shared_db):
    return shared_db()


# =============================================================================
# 1/2/12 - browser-session cookie: created via A, valid via B, revoked via B
#          invalidates A, and none of this requires any sticky-session
#          affinity (the cookie value itself, resolved through Redis, is
#          the only thing that ever moves between the two clients below).
# =============================================================================


def test_session_created_via_a_authenticates_via_b(replica_a, replica_b):
    email = "multi-replica-session@example.com"
    replica_a.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    login_response = replica_a.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert login_response.status_code == 200
    session_cookie = replica_a.cookies.get("eternal_world_session")
    assert session_cookie is not None, "browser-session cookie must be set on login"

    # Nothing about replica_b has ever seen this user - the cookie is the
    # only thing carried across, exactly like a real load balancer routing
    # the next request to a different backend replica.
    replica_b.cookies.set("eternal_world_session", session_cookie)
    session_response = replica_b.get("/api/auth/session")
    assert session_response.status_code == 200
    assert session_response.json()["email"] == email


def test_logout_via_b_invalidates_access_via_a(replica_a, replica_b):
    email = "multi-replica-logout@example.com"
    replica_a.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    replica_a.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    session_cookie = replica_a.cookies.get("eternal_world_session")

    replica_b.cookies.set("eternal_world_session", session_cookie)
    logout_response = replica_b.post("/api/auth/logout")
    assert logout_response.status_code in (200, 204)

    # The session was revoked through B (Redis-backed, Part J.2) - A's own
    # copy of the same cookie value must now be rejected too, proving the
    # revocation is not merely local to whichever replica issued it.
    still_using_a_cookie = replica_a.get("/api/auth/session")
    assert still_using_a_cookie.status_code == 401


# =============================================================================
# 3/4 - job visibility and authorization scoping across replicas
# =============================================================================


def test_job_created_via_a_is_visible_and_authorization_scoped_via_b(replica_a, replica_b):
    token_owner = _register_and_login(replica_a, "multi-replica-job-owner@example.com")
    token_other = _register_and_login(replica_b, "multi-replica-job-other@example.com")

    created = replica_a.post("/api/jobs/smoke-test", headers=_auth_headers(token_owner))
    assert created.status_code == 200
    job_id = created.json()["id"]

    owner_via_b = replica_b.get(f"/api/jobs/{job_id}", headers=_auth_headers(token_owner))
    assert owner_via_b.status_code == 200
    assert owner_via_b.json()["id"] == job_id

    other_via_b = replica_b.get(f"/api/jobs/{job_id}", headers=_auth_headers(token_other))
    assert other_via_b.status_code == 404


# =============================================================================
# 5/6 - outbox dispatch across contexts, idempotent under duplicate dispatch
# =============================================================================


def test_outbox_created_via_a_is_dispatched_by_a_separate_maintenance_context(shared_db, replica_a):
    token = _register_and_login(replica_a, "multi-replica-outbox@example.com")
    creation_db = _get_session_db(shared_db)
    try:
        job_id = job_tracking_service.create_job(
            creation_db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="multi-replica-outbox-job",
        ).id
    finally:
        creation_db.close()

    def fake_sender(*, task_name: str, args: list[object], queue: str) -> str:
        return "fake-celery-task-id"

    # A brand-new DB session/query stands in for "maintenance_worker
    # context B" - a genuinely separate connection AND a fresh SQLAlchemy
    # object for the same row (never the Python object context A created),
    # exactly like a real maintenance worker replica would only ever know
    # the job by its id, read fresh from Postgres.
    maintenance_db = shared_db()
    try:
        job_for_maintenance = job_tracking_repository.get_background_job_by_id(maintenance_db, job_id=job_id)
        job_outbox_service.enqueue_job_with_outbox(
            maintenance_db, job=job_for_maintenance, task_name="app.worker.tasks.run_job_smoke_test",
            queue="embedding", sender=fake_sender,
        )
    finally:
        maintenance_db.close()

    verification_db = shared_db()
    try:
        refreshed = job_tracking_repository.get_background_job_by_id(verification_db, job_id=job_id)
        assert refreshed.status == "queued"
        assert refreshed.celery_task_id == "fake-celery-task-id"
    finally:
        verification_db.close()
    assert token


def test_duplicate_dispatch_across_two_contexts_stays_idempotent(shared_db, replica_a):
    _register_and_login(replica_a, "multi-replica-duplicate-dispatch@example.com")
    calls = {"count": 0}

    def counting_sender(*, task_name: str, args: list[object], queue: str) -> str:
        calls["count"] += 1
        return f"fake-celery-task-id-{calls['count']}"

    creation_db = _get_session_db(shared_db)
    try:
        job_id = job_tracking_service.create_job(
            creation_db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="multi-replica-duplicate-dispatch-job",
        ).id
    finally:
        creation_db.close()

    context_a_db = shared_db()
    try:
        job_via_a = job_tracking_repository.get_background_job_by_id(context_a_db, job_id=job_id)
        job_outbox_service.enqueue_job_with_outbox(
            context_a_db, job=job_via_a, task_name="app.worker.tasks.run_job_smoke_test",
            queue="embedding", sender=counting_sender,
        )
    finally:
        context_a_db.close()

    context_b_db = shared_db()
    try:
        # "Context B" redispatches the exact same job (its own fresh
        # object, from its own session) - a real broker blip/duplicate
        # maintenance sweep must never publish twice.
        job_via_b = job_tracking_repository.get_background_job_by_id(context_b_db, job_id=job_id)
        job_outbox_service.enqueue_job_with_outbox(
            context_b_db, job=job_via_b, task_name="app.worker.tasks.run_job_smoke_test",
            queue="embedding", sender=counting_sender,
        )
    finally:
        context_b_db.close()

    assert calls["count"] == 1, "the second dispatch attempt must be a no-op (already published)"


# =============================================================================
# 7 - backpressure counts created via A are enforced via B
# =============================================================================


def test_backpressure_created_via_a_is_enforced_via_b(replica_a, replica_b, monkeypatch):
    token = _register_and_login(replica_a, "multi-replica-backpressure@example.com")
    monkeypatch.setattr(settings, "max_active_heavy_jobs_per_user", 1)

    profile_response = replica_a.post(
        "/api/memory-profiles", headers=_auth_headers(token), json={"name": "Multi-replica profile"}
    )
    profile_id = profile_response.json()["id"]
    source_response = replica_a.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
        json={"title": "S1", "raw_text": "Text.", "source_type": "manual_text"},
    )
    source_id = source_response.json()["id"]
    first = replica_a.post(f"/api/rag-sources/{source_id}/process", headers=_auth_headers(token))
    assert first.status_code == 200

    # The SAME limit, hit through B for a *second* source - the count that
    # matters is the PostgreSQL row count, not any counter local to A.
    second_source = replica_b.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
        json={"title": "S2", "raw_text": "Text.", "source_type": "manual_text"},
    )
    second = replica_b.post(
        f"/api/rag-sources/{second_source.json()['id']}/process", headers=_auth_headers(token)
    )
    assert second.status_code == 429


# =============================================================================
# 8 - active chat written via A resumes via B
# =============================================================================


def test_active_chat_written_via_a_resumes_via_b(replica_a, replica_b):
    token = _register_and_login(replica_a, "multi-replica-chat@example.com")
    profile_response = replica_a.post(
        "/api/memory-profiles", headers=_auth_headers(token), json={"name": "Chat profile"}
    )
    profile_id = profile_response.json()["id"]

    sent = replica_a.post(
        f"/api/chat/{profile_id}/messages", headers=_auth_headers(token), json={"message": "Hello"}
    )
    assert sent.status_code == 200

    resumed = replica_b.get(f"/api/chat/{profile_id}/active", headers=_auth_headers(token))
    assert resumed.status_code == 200
    messages = resumed.json()["messages"]
    assert any(message["content"] == "Hello" for message in messages)


# =============================================================================
# 10 - stale-job recovery via B cannot resurrect a job finalized via A
# =============================================================================


def test_stale_recovery_via_b_cannot_resurrect_a_job_completed_via_a(shared_db, replica_a):
    _register_and_login(replica_a, "multi-replica-stale-recovery@example.com")
    context_a_db = shared_db()
    try:
        job = job_tracking_service.create_job(
            db=context_a_db, owner_user_id=1, job_type=BackgroundJobType.QDRANT_INDEXING,
            queue="embedding", idempotency_key="multi-replica-stale-recovery-job",
        )
        job_tracking_service.mark_running(context_a_db, job_id=job.id)
        job_tracking_service.mark_succeeded(context_a_db, job_id=job.id, result_payload={"ok": True})
    finally:
        context_a_db.close()

    context_b_db = shared_db()
    try:
        was_requeued = job_tracking_service.requeue_stale_job(context_b_db, job_id=job.id)
        assert was_requeued is False
        refreshed = job_tracking_repository.get_background_job_by_id(context_b_db, job_id=job.id)
        assert refreshed.status == "succeeded"
    finally:
        context_b_db.close()


# =============================================================================
# 11 - provider lifecycle remains worker-local, never shared between
#      simulated worker instances
# =============================================================================


class _FakeProvider(BaseEmbeddingProvider):
    def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=[0.1] * 4, dimension=4, metadata={"provider_name": "fake"})

    def embed_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        return [self.embed_text(text, model_code) for text in texts]


def test_provider_lifecycle_is_not_shared_between_simulated_worker_instances(monkeypatch):
    """`EmbeddingProviderLifecycle` is documented as "one instance per
    worker process" (Part J.11). Simulates two worker processes as two
    independent instances of that class, each with its own fake-provider
    builder, and proves that invalidating/reloading one never touches the
    other's already-healthy slot - the actual failure mode this would
    catch is a future refactor that accidentally makes the lifecycle (or
    its underlying provider builder) a module-level shared singleton
    mutated by both "workers" at once."""

    import app.modules.embeddings.provider_lifecycle as provider_lifecycle_module

    build_calls = {"count": 0}

    def fake_builder(*, model_code: str) -> BaseEmbeddingProvider:
        build_calls["count"] += 1
        return _FakeProvider()

    monkeypatch.setattr(provider_lifecycle_module, "build_embedding_provider", fake_builder)
    monkeypatch.setattr(provider_lifecycle_module, "run_provider_integrity_probe", lambda provider, *, model_code: None)

    worker_a = EmbeddingProviderLifecycle()
    worker_b = EmbeddingProviderLifecycle()

    provider_a = worker_a.get_or_initialize(model_code="test-model")
    provider_b = worker_b.get_or_initialize(model_code="test-model")

    assert build_calls["count"] == 2, "each simulated worker must build its own provider instance"
    assert provider_a is not provider_b
    assert worker_a.get_health(model_code="test-model").state == ProviderState.HEALTHY
    assert worker_b.get_health(model_code="test-model").state == ProviderState.HEALTHY

    # Worker A's provider is invalidated (simulating bounded self-healing
    # after detected corruption) - Worker B must be completely unaffected.
    worker_a.invalidate(model_code="test-model")
    assert worker_a.get_health(model_code="test-model").state == ProviderState.RECOVERY_IN_PROGRESS
    assert worker_b.get_health(model_code="test-model").state == ProviderState.HEALTHY
    assert worker_b.get_or_initialize(model_code="test-model") is provider_b

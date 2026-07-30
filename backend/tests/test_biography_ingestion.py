"""Task 65.2 - initial biography ingestion (owner-authored `MemoryProfile.
biography` -> RagSource/RagChunk/RagEmbedding -> Qdrant).

Uses fake-safe writer/encoder doubles (no real Qdrant network calls, no
model downloads), mirroring the established pattern in
`test_memorial_contribution_indexing.py`/`test_avatar_memory_indexing.py`.
"""

from __future__ import annotations

from app.db.models import MemoryProfile, RagChunk, RagEmbedding, RagSource
from app.main import app
from app.modules.biography_ingestion.chunking import chunk_biography_text
from app.modules.biography_ingestion.service import (
    BiographyIngestionEligibilityError,
    index_biography,
    start_biography_ingestion,
)
from app.modules.embeddings.providers.base import EmbeddingVector


PASSWORD = "StrongPass123"


class FakeEncoder:
    def __init__(self) -> None:
        self.calls = 0

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        self.calls += 1
        assert text
        assert model_code == "bge_m3_dense_sparse"
        return EmbeddingVector(values=[0.01] * 1024, dimension=1024, metadata={})


class FakeWriter:
    def __init__(self, *, dimension: int | None = 1024) -> None:
        self.dimension = dimension
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.upsert_calls = 0
        self.delete_calls = 0
        self.ensure_calls: list[tuple[str, int]] = []

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        del collection_name
        return self.dimension

    def ensure_collection(self, *, collection_name: str, vector_size: int) -> None:
        self.ensure_calls.append((collection_name, vector_size))
        self.dimension = vector_size

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.upsert_calls += 1
        self.points[(collection_name, point_id)] = {"vector": list(vector), "payload": dict(payload)}

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self.delete_calls += 1
        self.points.pop((collection_name, point_id), None)


def _db():
    return app.state.testing_session_local()


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _create_memorial(client, token: str, name: str = "Biography Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def test_chunking_is_deterministic_and_respects_max_chars():
    text = ("Odstavec jedna. " * 60) + "\n\n" + ("Odstavec dva. " * 60)
    chunks_a = chunk_biography_text(text, max_chars=400)
    chunks_b = chunk_biography_text(text, max_chars=400)
    assert chunks_a == chunks_b
    assert len(chunks_a) > 1
    assert all(len(chunk) <= 420 for chunk in chunks_a)  # small slack for sentence boundary packing


def test_update_biography_sets_draft_status(client):
    token = _register_and_login(client, "bio-owner1@example.com")
    profile_id = _create_memorial(client, token)

    response = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Narodil jsem se v Praze."},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "draft"
    assert body["attempt_count"] == 0


def test_start_ingestion_requires_nonempty_biography(client):
    token = _register_and_login(client, "bio-owner2@example.com")
    profile_id = _create_memorial(client, token)

    response = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert response.status_code == 400


def test_start_ingestion_enqueues_background_job(client):
    token = _register_and_login(client, "bio-owner3@example.com")
    profile_id = _create_memorial(client, token)
    client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Narodil jsem se v Praze a vyrostl na venkově."},
    )

    response = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert response.status_code == 202
    body = response.json()
    assert body["status"] == "ready_for_ingestion"
    assert body["background_job_id"] is not None

    db = _db()
    try:
        from app.db.models import BackgroundJob

        job = db.get(BackgroundJob, body["background_job_id"])
        assert job is not None
        assert job.input_payload["workflow"] == "biography_indexing"
        assert job.celery_task_id is not None
    finally:
        db.close()


def test_contributor_cannot_start_ingestion(client):
    owner_token = _register_and_login(client, "bio-owner4@example.com")
    contributor_token = _register_and_login(client, "bio-contributor4@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "bio-contributor4@example.com", "role": "contributor"},
    )
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(contributor_token),
        json={"token": invite.json()["token"]},
    )
    client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(owner_token),
        json={"biography": "Text zivotopisu."},
    )

    response = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(contributor_token))
    assert response.status_code == 403


def test_foreign_user_cannot_read_biography_status(client):
    owner_token = _register_and_login(client, "bio-owner5@example.com")
    outsider_token = _register_and_login(client, "bio-outsider5@example.com")
    profile_id = _create_memorial(client, owner_token)

    response = client.get(f"/api/memorials/{profile_id}/biography/status", headers=_auth_headers(outsider_token))
    assert response.status_code == 404


def _setup_profile_with_biography(client, email: str, biography: str) -> tuple[str, int]:
    """Saves biography text and starts ingestion (-> `ready_for_ingestion`),
    matching the real precondition `index_biography` requires - it is only
    ever called after `start_biography_ingestion`, never directly from a
    freshly-saved `draft` profile."""

    token = _register_and_login(client, email)
    profile_id = _create_memorial(client, token)
    response = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": biography},
    )
    assert response.status_code == 200
    start = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert start.status_code == 202
    return token, profile_id


def test_index_biography_direct_call_writes_evidence_and_points(client):
    _token, profile_id = _setup_profile_with_biography(
        client,
        "bio-owner6@example.com",
        "Prvni odstavec zivotopisu.\n\nDruhy odstavec zivotopisu s dalsimi detaily.",
    )
    db = _db()
    try:
        writer = FakeWriter()
        encoder = FakeEncoder()
        result = index_biography(db, profile_id=profile_id, writer=writer, encoder=encoder, validate_runtime=False)
        assert result.status == "indexed"
        assert writer.upsert_calls >= 1
        assert writer.ensure_calls == []

        profile = db.get(MemoryProfile, profile_id)
        assert profile.biography_status == "indexed"
        assert profile.biography_source_id is not None

        sources = db.query(RagSource).filter(RagSource.profile_id == profile_id, RagSource.source_type == "biography").all()
        assert len(sources) == 1
        chunks = db.query(RagChunk).filter(RagChunk.source_id == sources[0].id).all()
        assert len(chunks) >= 1
        embeddings = db.query(RagEmbedding).filter(RagEmbedding.source_id == sources[0].id).all()
        assert len(embeddings) == len(chunks)
    finally:
        db.close()


def test_index_biography_creates_missing_qdrant_collection(client):
    _token, profile_id = _setup_profile_with_biography(
        client,
        "bio-owner6b@example.com",
        "Narodil jsem se v Praze a zil jsem tam cely zivot.",
    )
    db = _db()
    try:
        writer = FakeWriter(dimension=None)
        encoder = FakeEncoder()
        result = index_biography(db, profile_id=profile_id, writer=writer, encoder=encoder, validate_runtime=False)
        assert result.status == "indexed"
        assert writer.ensure_calls
        assert writer.dimension == 1024
        assert writer.upsert_calls >= 1
    finally:
        db.close()


def test_index_biography_retry_same_content_is_idempotent(client):
    _token, profile_id = _setup_profile_with_biography(
        client, "bio-owner7@example.com", "Zivotopisny text pro test idempotence."
    )
    db = _db()
    try:
        writer = FakeWriter()
        encoder = FakeEncoder()
        first = index_biography(db, profile_id=profile_id, writer=writer, encoder=encoder, validate_runtime=False)
        assert first.status == "indexed"
        source_count_after_first = db.query(RagSource).filter(RagSource.profile_id == profile_id).count()
        encoder_calls_after_first = encoder.calls
        upserts_after_first = writer.upsert_calls

        # Force back into a retryable state without changing the text -
        # simulates a retry after a transient failure, not a real edit.
        profile = db.get(MemoryProfile, profile_id)
        profile.biography_status = "failed"
        db.commit()

        second = index_biography(db, profile_id=profile_id, writer=writer, encoder=encoder, validate_runtime=False)
        assert second.status == "indexed"
        source_count_after_second = db.query(RagSource).filter(RagSource.profile_id == profile_id).count()

        # Same source reused (no duplicate RagSource), no re-embedding, no
        # duplicate Qdrant upsert - a true no-op retry.
        assert source_count_after_second == source_count_after_first
        assert encoder.calls == encoder_calls_after_first
        assert writer.upsert_calls == upserts_after_first
    finally:
        db.close()


def test_edit_after_indexed_marks_stale_and_reingest_retires_old_points(client):
    token, profile_id = _setup_profile_with_biography(
        client, "bio-owner8@example.com", "Puvodni verze zivotopisu."
    )
    db = _db()
    try:
        writer = FakeWriter()
        encoder = FakeEncoder()
        first = index_biography(db, profile_id=profile_id, writer=writer, encoder=encoder, validate_runtime=False)
        assert first.status == "indexed"
        points_after_first = dict(writer.points)
        assert len(points_after_first) >= 1
    finally:
        db.close()

    edit_response = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Zcela nova upravena verze zivotopisu s jinym obsahem."},
    )
    assert edit_response.status_code == 200
    assert edit_response.json()["status"] == "stale"

    restart = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert restart.status_code == 202

    db = _db()
    try:
        second = index_biography(db, profile_id=profile_id, writer=writer, encoder=encoder, validate_runtime=False)
        assert second.status == "indexed"

        profile = db.get(MemoryProfile, profile_id)
        sources = (
            db.query(RagSource)
            .filter(RagSource.profile_id == profile_id, RagSource.source_type == "biography")
            .order_by(RagSource.id.asc())
            .all()
        )
        assert len(sources) == 2  # a fresh source was created for the edited text
        assert profile.biography_source_id == sources[-1].id

        # The previous source's points must no longer be present in Qdrant.
        for key in points_after_first:
            assert key not in writer.points
    finally:
        db.close()


def test_start_biography_ingestion_rejects_empty_text_service_level(client):
    _token, profile_id = _setup_profile_with_biography(client, "bio-owner9@example.com", "x")
    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        profile.biography = ""
        db.commit()
        try:
            start_biography_ingestion(db, profile=profile)
            assert False, "expected BiographyIngestionEligibilityError"
        except BiographyIngestionEligibilityError:
            pass
    finally:
        db.close()

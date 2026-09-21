"""Task 65.2 - initial biography ingestion (owner-authored `MemoryProfile.
biography` -> RagSource/RagChunk/RagEmbedding -> Qdrant).

Uses fake-safe writer/encoder doubles (no real Qdrant network calls, no
model downloads), mirroring the established pattern in
`test_memorial_contribution_indexing.py`/`test_avatar_memory_indexing.py`.
"""

from __future__ import annotations

import pytest

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


def _create_memorial(
    client,
    token: str,
    name: str = "Biography Memorial",
    canonical_language: str = "cs",
) -> int:
    response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": name,
            "canonical_language": canonical_language,
            "confirm_canonical_language": True,
        },
    )
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


@pytest.mark.parametrize(
    ("canonical_language", "email", "versions"),
    [
        (
            "cs",
            "bio-canonical-cs@example.com",
            [
                "Narodil jsem se v Praze.",
                "Narodil jsem se v Praze.\n\nPozd\u011bji jsem se p\u0159est\u011bhoval do Brna.",
                (
                    "Narodil jsem se v Praze.\n\nPozd\u011bji jsem se p\u0159est\u011bhoval do Brna."
                    "\n\nMoje nejmilej\u0161\u00ed vzpom\u00ednka pat\u0159\u00ed rodin\u011b."
                ),
            ],
        ),
        (
            "ru",
            "bio-canonical-ru@example.com",
            [
                "\u042f \u0440\u043e\u0434\u0438\u043b\u0441\u044f \u0432 \u041c\u043e\u0441\u043a\u0432\u0435.",
                "\u042f \u0440\u043e\u0434\u0438\u043b\u0441\u044f \u0432 \u041c\u043e\u0441\u043a\u0432\u0435.\n\n\u041f\u043e\u0437\u0436\u0435 \u044f \u043f\u0435\u0440\u0435\u0435\u0445\u0430\u043b \u0432 \u041a\u0430\u043b\u0438\u043d\u0438\u043d\u0433\u0440\u0430\u0434.",
                (
                    "\u042f \u0440\u043e\u0434\u0438\u043b\u0441\u044f \u0432 \u041c\u043e\u0441\u043a\u0432\u0435.\n\n\u041f\u043e\u0437\u0436\u0435 \u044f \u043f\u0435\u0440\u0435\u0435\u0445\u0430\u043b \u0432 \u041a\u0430\u043b\u0438\u043d\u0438\u043d\u0433\u0440\u0430\u0434."
                    "\n\n\u041c\u043e\u044f \u043b\u044e\u0431\u0438\u043c\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c \u0441\u0432\u044f\u0437\u0430\u043d\u0430 \u0441 \u0441\u0435\u043c\u044c\u0451\u0439."
                ),
            ],
        ),
    ],
)
def test_repeated_full_document_saves_persist_latest_canonical_text(
    client,
    canonical_language: str,
    email: str,
    versions: list[str],
):
    token = _register_and_login(client, email)
    profile_id = _create_memorial(client, token, canonical_language=canonical_language)

    for expected in versions:
        response = client.patch(
            f"/api/memorials/{profile_id}/biography",
            headers=_auth_headers(token),
            json={"biography": expected},
        )
        assert response.status_code == 200

        reloaded = client.get(f"/api/memorials/{profile_id}", headers=_auth_headers(token))
        assert reloaded.status_code == 200
        assert reloaded.json()["biography"] == expected

    # Re-saving the complete document is idempotent; it must not append the
    # final paragraph again or otherwise mutate the canonical text.
    repeated = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": versions[-1]},
    )
    assert repeated.status_code == 200

    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        assert profile is not None
        assert profile.biography == versions[-1]
    finally:
        db.close()


def test_biography_updates_are_isolated_between_owners_and_profiles(client):
    first_token = _register_and_login(client, "bio-isolation-first@example.com")
    second_token = _register_and_login(client, "bio-isolation-second@example.com")
    first_profile_id = _create_memorial(client, first_token, name="First biography")
    second_profile_id = _create_memorial(client, second_token, name="Second biography", canonical_language="ru")
    first_text = "Prvn\u00ed vlastn\u00ed \u017eivotopis."
    second_text = "\u0412\u0442\u043e\u0440\u0430\u044f \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u0430\u044f \u0431\u0438\u043e\u0433\u0440\u0430\u0444\u0438\u044f."

    assert client.patch(
        f"/api/memorials/{first_profile_id}/biography",
        headers=_auth_headers(first_token),
        json={"biography": first_text},
    ).status_code == 200
    assert client.patch(
        f"/api/memorials/{second_profile_id}/biography",
        headers=_auth_headers(second_token),
        json={"biography": second_text},
    ).status_code == 200

    forbidden = client.patch(
        f"/api/memorials/{second_profile_id}/biography",
        headers=_auth_headers(first_token),
        json={"biography": "Tento text se nesm\u00ed ulo\u017eit."},
    )
    assert forbidden.status_code == 404

    db = _db()
    try:
        assert db.get(MemoryProfile, first_profile_id).biography == first_text
        assert db.get(MemoryProfile, second_profile_id).biography == second_text
    finally:
        db.close()


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
    initial_biography = "P\u016fvodn\u00ed verze \u017eivotopisu."
    expanded_biography = (
        "P\u016fvodn\u00ed verze \u017eivotopisu."
        "\n\nNov\u00e1 \u010desk\u00e1 vzpom\u00ednka dopln\u011bn\u00e1 po prvn\u00edm indexov\u00e1n\u00ed."
        "\n\n\u041d\u043e\u0432\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 Unicode."
    )
    token, profile_id = _setup_profile_with_biography(
        client, "bio-owner8@example.com", initial_biography
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
        json={"biography": expanded_biography},
    )
    assert edit_response.status_code == 200
    assert edit_response.json()["status"] == "stale"
    reloaded = client.get(f"/api/memorials/{profile_id}", headers=_auth_headers(token))
    assert reloaded.status_code == 200
    assert reloaded.json()["biography"] == expanded_biography

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
        assert profile.biography == expanded_biography

        latest_chunks = (
            db.query(RagChunk)
            .filter(RagChunk.source_id == sources[-1].id)
            .order_by(RagChunk.chunk_index.asc())
            .all()
        )
        indexed_text = "\n\n".join(chunk.chunk_text for chunk in latest_chunks)
        assert initial_biography in indexed_text
        assert "Nov\u00e1 \u010desk\u00e1 vzpom\u00ednka" in indexed_text
        assert "\u041d\u043e\u0432\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c" in indexed_text

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

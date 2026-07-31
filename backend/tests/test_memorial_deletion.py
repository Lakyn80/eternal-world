"""Task 65.5 - safe deletion controls for an existing memorial: clearing just
the biography (and its indexed vectors) versus deleting the whole memorial.

Uses the same fake-writer/fake-encoder doubles as `test_biography_ingestion.py`
(no real Qdrant network calls, no model downloads).
"""

from __future__ import annotations

import pytest

from app.db.models import MemoryProfile, RagSource, RagVectorIndex, User
from app.main import app
from app.modules.biography_ingestion.service import clear_biography, index_biography
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.memory_profiles.service import (
    MemoryProfileDeletionFailedError,
    delete_memory_profile,
)


PASSWORD = "StrongPass123"


class FakeEncoder:
    def __init__(self) -> None:
        self.calls = 0

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        self.calls += 1
        assert text
        return EmbeddingVector(values=[0.01] * 1024, dimension=1024, metadata={})


class FakeWriter:
    def __init__(self) -> None:
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.upsert_calls = 0
        self.delete_calls = 0

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return 1024

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.upsert_calls += 1
        self.points[(collection_name, point_id)] = {"vector": list(vector), "payload": dict(payload)}

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self.delete_calls += 1
        self.points.pop((collection_name, point_id), None)


class FailingWriter:
    """Simulates a Qdrant outage - every delete attempt raises."""

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        raise RuntimeError("qdrant unreachable")


def _db():
    return app.state.testing_session_local()


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _create_memorial(client, token: str, name: str = "Deletion Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name, "canonical_language": "cs", "confirm_canonical_language": True})
    assert response.status_code == 201
    return response.json()["id"]


def _index_a_biography(client, token: str, profile_id: int, biography: str) -> FakeWriter:
    """Saves + indexes a biography end-to-end so the profile has at least one
    real RagVectorIndex row, matching the real preconditions clear/delete
    must handle (not just the empty case)."""

    response = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": biography},
    )
    assert response.status_code == 200
    start = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert start.status_code == 202

    writer = FakeWriter()
    db = _db()
    try:
        result = index_biography(
            db, profile_id=profile_id, writer=writer, encoder=FakeEncoder(), validate_runtime=False
        )
        assert result.status == "indexed"
    finally:
        db.close()
    return writer


def test_clear_biography_removes_indexed_points_and_resets_status(client):
    token = _register_and_login(client, "clear-bio-owner1@example.com")
    profile_id = _create_memorial(client, token)
    writer = _index_a_biography(client, token, profile_id, "Prvni odstavec.\n\nDruhy odstavec zivotopisu.")

    points_before = dict(writer.points)
    assert len(points_before) >= 1

    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        clear_biography(db, profile=profile, writer=writer)
    finally:
        db.close()

    assert writer.delete_calls >= 1
    for key in points_before:
        assert key not in writer.points

    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        assert profile.biography is None
        assert profile.biography_status == "draft"
        assert profile.biography_source_id is None
        assert profile.biography_indexed_at is None
        assert db.query(RagVectorIndex).filter(RagVectorIndex.profile_id == profile_id).count() == 0
        # The audit trail (RagSource) is preserved, not hard-deleted.
        assert db.query(RagSource).filter(RagSource.profile_id == profile_id).count() == 1
    finally:
        db.close()


def test_clear_biography_is_idempotent(client):
    token = _register_and_login(client, "clear-bio-owner2@example.com")
    profile_id = _create_memorial(client, token)
    writer = _index_a_biography(client, token, profile_id, "Zivotopis pro test idempotence.")

    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        clear_biography(db, profile=profile, writer=writer)
    finally:
        db.close()

    # Calling it again on an already-cleared profile must not raise and must
    # not attempt to delete anything further.
    delete_calls_after_first = writer.delete_calls
    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        clear_biography(db, profile=profile, writer=writer)
        assert profile.biography is None
        assert profile.biography_status == "draft"
    finally:
        db.close()
    assert writer.delete_calls == delete_calls_after_first


def test_clear_biography_preserves_name_and_membership(client):
    token = _register_and_login(client, "clear-bio-owner3@example.com")
    profile_id = _create_memorial(client, token, name="Keep My Name")
    writer = _index_a_biography(client, token, profile_id, "Text ktery bude smazan.")

    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        clear_biography(db, profile=profile, writer=writer)
    finally:
        db.close()

    response = client.get(f"/api/memorials/{profile_id}", headers=_auth_headers(token))
    assert response.status_code == 200
    assert response.json()["name"] == "Keep My Name"

    members = client.get(f"/api/memorials/{profile_id}/members", headers=_auth_headers(token))
    assert members.status_code == 200
    assert len(members.json()) == 1


def test_clear_biography_endpoint_requires_direct_memory_write_capability(client):
    owner_token = _register_and_login(client, "clear-bio-owner4@example.com")
    viewer_token = _register_and_login(client, "clear-bio-viewer4@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "clear-bio-viewer4@example.com", "role": "viewer"},
    )
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(viewer_token),
        json={"token": invite.json()["token"]},
    )

    response = client.post(
        f"/api/memorials/{profile_id}/biography/clear", headers=_auth_headers(viewer_token)
    )
    assert response.status_code == 403


def test_delete_memory_profile_removes_indexed_vector_points(client):
    token = _register_and_login(client, "delete-bio-owner1@example.com")
    profile_id = _create_memorial(client, token)
    writer = _index_a_biography(client, token, profile_id, "Zivotopis pred smazanim memorialu.")

    points_before = dict(writer.points)
    assert len(points_before) >= 1

    db = _db()
    try:
        current_user = db.get(User, db.get(MemoryProfile, profile_id).user_id)
        result = delete_memory_profile(db, current_user=current_user, profile_id=profile_id, writer=writer)
    finally:
        db.close()

    assert result.vector_points_removed == len(points_before)
    for key in points_before:
        assert key not in writer.points

    db = _db()
    try:
        assert db.get(MemoryProfile, profile_id) is None
        assert db.query(RagVectorIndex).filter(RagVectorIndex.profile_id == profile_id).count() == 0
    finally:
        db.close()


def test_delete_memory_profile_aborts_without_db_change_on_qdrant_failure(client):
    token = _register_and_login(client, "delete-bio-owner2@example.com")
    profile_id = _create_memorial(client, token)
    _index_a_biography(client, token, profile_id, "Text ktery selze pri mazani z Qdrant.")

    db = _db()
    try:
        current_user = db.get(User, db.get(MemoryProfile, profile_id).user_id)
        with pytest.raises(MemoryProfileDeletionFailedError):
            delete_memory_profile(db, current_user=current_user, profile_id=profile_id, writer=FailingWriter())
    finally:
        db.close()

    # The profile and its vector index bookkeeping must still exist - never
    # claim a successful deletion if vectors could not be confirmed removed.
    db = _db()
    try:
        assert db.get(MemoryProfile, profile_id) is not None
        assert db.query(RagVectorIndex).filter(RagVectorIndex.profile_id == profile_id).count() >= 1
    finally:
        db.close()


def test_delete_memory_profile_with_no_indexed_content_is_a_simple_delete(client):
    token = _register_and_login(client, "delete-bio-owner3@example.com")
    profile_id = _create_memorial(client, token)

    db = _db()
    try:
        current_user = db.get(User, db.get(MemoryProfile, profile_id).user_id)
        result = delete_memory_profile(db, current_user=current_user, profile_id=profile_id, writer=FakeWriter())
        assert result.vector_points_removed == 0
    finally:
        db.close()

    db = _db()
    try:
        assert db.get(MemoryProfile, profile_id) is None
    finally:
        db.close()


def test_other_user_cannot_delete_someone_elses_memorial(client):
    owner_token = _register_and_login(client, "delete-owner-cross@example.com")
    outsider_token = _register_and_login(client, "delete-outsider-cross@example.com")
    profile_id = _create_memorial(client, owner_token)

    response = client.delete(
        f"/api/memory-profiles/{profile_id}", headers=_auth_headers(outsider_token)
    )
    assert response.status_code == 404

    # And the memorial must still be fully intact for its real owner.
    get_response = client.get(f"/api/memory-profiles/{profile_id}", headers=_auth_headers(owner_token))
    assert get_response.status_code == 200


def test_repeat_delete_of_already_deleted_profile_is_safe(client):
    token = _register_and_login(client, "delete-repeat@example.com")
    profile_id = _create_memorial(client, token)

    first = client.delete(f"/api/memory-profiles/{profile_id}", headers=_auth_headers(token))
    second = client.delete(f"/api/memory-profiles/{profile_id}", headers=_auth_headers(token))

    assert first.status_code == 204
    assert second.status_code == 404


def test_owner_can_create_new_memorial_after_deleting_previous_one(client):
    token = _register_and_login(client, "delete-then-recreate@example.com")
    profile_id = _create_memorial(client, token, name="First Memorial")

    delete_response = client.delete(f"/api/memory-profiles/{profile_id}", headers=_auth_headers(token))
    assert delete_response.status_code == 204

    recreate_response = client.post(
        "/api/memorials", headers=_auth_headers(token), json={"name": "Second Memorial", "canonical_language": "cs", "confirm_canonical_language": True}
    )
    assert recreate_response.status_code == 201

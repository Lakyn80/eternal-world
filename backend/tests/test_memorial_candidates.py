"""Task 65.2 - authenticated owner-review + explicit-indexing wrapper over
the existing conversation_memory_candidates/family_memory_enrichment/
avatar_memory_promotions/avatar_memory_indexing pipeline.

Approval must never write to Qdrant by itself (only ever creates a
`pending_index` promotion); explicit indexing is a separate, owner-
triggered, idempotent step.
"""

from __future__ import annotations

from app.db.models import AvatarMemoryPromotion
from app.main import app
from app.modules.embeddings.providers.base import EmbeddingVector


PASSWORD = "StrongPass123"


class FakeEncoder:
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=[0.01] * 1024, dimension=1024, metadata={})


class FakeWriter:
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


def _db():
    return app.state.testing_session_local()


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _create_memorial(client, token: str, name: str = "Candidate Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name, "canonical_language": "cs", "confirm_canonical_language": True})
    assert response.status_code == 201
    return response.json()["id"]


def _create_general_candidate_via_biographer(client, token: str, profile_id: int) -> tuple[int, dict]:
    """Reuses the real Biographer flow to get a `ready_for_owner_review`
    candidate without any required clarification (the "family" topic)."""

    for _ in range(2):
        question = client.get(
            f"/api/memorials/{profile_id}/biographer/next-question",
            params={"locale": "cs"},
            headers=_auth_headers(token),
        ).json()
        if question["topic"] == "family":
            break
        client.post(
            f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/skip",
            headers=_auth_headers(token),
        )
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Moje rodina byla vždy velmi důležitá."},
    ).json()
    assert answer["enrichment_status"] == "ready_for_owner_review"
    return answer["candidate_id"], answer


def _setup_indexed_biography(client, token: str, profile_id: int) -> None:
    from app.modules.biography_ingestion.service import index_biography

    client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Krátký životopis pro test."},
    )
    start = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert start.status_code == 202
    db = _db()
    try:
        result = index_biography(
            db,
            profile_id=profile_id,
            writer=FakeWriter(),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert result.status == "indexed"
    finally:
        db.close()


def test_owner_review_confirm_creates_pending_index_promotion_without_writing_qdrant(client):
    token = _register_and_login(client, "candidates-owner1@example.com")
    profile_id = _create_memorial(client, token)
    _setup_indexed_biography(client, token, profile_id)
    candidate_id, _ = _create_general_candidate_via_biographer(client, token, profile_id)

    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm", "privacy_scope": "all_family"},
    )
    assert review.status_code == 200
    body = review.json()
    assert body["promotion_status"] == "pending_index"
    assert body["searchable_as_fact"] is False
    assert body["explicit_indexing_required"] is True

    db = _db()
    try:
        promotions = db.query(AvatarMemoryPromotion).filter(AvatarMemoryPromotion.candidate_id == candidate_id).all()
        assert len(promotions) == 1
        assert promotions[0].promotion_status == "pending_index"
    finally:
        db.close()


def test_contributor_cannot_owner_review(client):
    owner_token = _register_and_login(client, "candidates-owner2@example.com")
    contributor_token = _register_and_login(client, "candidates-contributor2@example.com")
    profile_id = _create_memorial(client, owner_token)
    _setup_indexed_biography(client, owner_token, profile_id)
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "candidates-contributor2@example.com", "role": "contributor"},
    )
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(contributor_token),
        json={"token": invite.json()["token"]},
    )
    candidate_id, _ = _create_general_candidate_via_biographer(client, owner_token, profile_id)

    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(contributor_token),
        json={"action": "confirm", "privacy_scope": "all_family"},
    )
    assert review.status_code == 403


def test_unapproved_candidate_cannot_be_indexed(client):
    token = _register_and_login(client, "candidates-owner3@example.com")
    profile_id = _create_memorial(client, token)
    _setup_indexed_biography(client, token, profile_id)
    candidate_id, _ = _create_general_candidate_via_biographer(client, token, profile_id)

    response = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/index",
        headers=_auth_headers(token),
    )
    assert response.status_code == 400


def test_explicit_index_writes_qdrant_point_and_is_idempotent(client):
    """Task 65.9 (Part I): the explicit "Index memory" HTTP endpoint must
    never call the encoder itself - it only creates/reuses the persistent
    job and returns 202 with the promotion's current (pending) state. The
    embedding-worker's execution is simulated directly (as
    `test_memory_review_indexing_workflow.py` now does for the equivalent
    contribution-retry flow), then the endpoint's own idempotent no-op
    path for an already-`indexed` promotion is exercised for the second
    call - proving no duplicate Qdrant write happens even from the HTTP
    layer on a repeat click."""

    token = _register_and_login(client, "candidates-owner4@example.com")
    profile_id = _create_memorial(client, token)
    _setup_indexed_biography(client, token, profile_id)
    candidate_id, _ = _create_general_candidate_via_biographer(client, token, profile_id)
    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm", "privacy_scope": "all_family"},
    )
    promotion_id = review.json()["promotion_id"]

    fake_writer = FakeWriter()
    fake_encoder = FakeEncoder()

    first = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/index",
        headers=_auth_headers(token),
    )
    assert first.status_code == 202
    assert first.json()["result"] == "queued"
    assert first.json()["searchable_as_fact"] is False
    assert first.json()["job_id"] is not None

    from app.modules.avatar_memory_indexing.service import index_promotion

    db = _db()
    try:
        promotion_row = db.get(AvatarMemoryPromotion, promotion_id)
        assert promotion_row is not None
        result = index_promotion(
            db,
            owner_user_id=promotion_row.owner_user_id,
            promotion_id=promotion_id,
            writer=fake_writer,
            encoder=fake_encoder,
        )
        assert result.result == "indexed"
    finally:
        db.close()
    upserts_after_first = fake_writer.upsert_calls
    assert upserts_after_first == 1

    second = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/index",
        headers=_auth_headers(token),
    )
    assert second.status_code == 202
    assert second.json()["result"] == "already_indexed"
    assert second.json()["searchable_as_fact"] is True
    assert second.json()["job_id"] is None
    assert fake_writer.upsert_calls == upserts_after_first  # no duplicate write on repeat


def test_czech_clarification_question_is_localized_not_raw_russian(client):
    """`family_memory_enrichment._build_clarification_read` (existing,
    untouched) always stores/returns the canonical Russian `question_text` -
    this router must localize it for Czech-origin candidates the same way
    the demo module already does for its own UI, otherwise a Czech user
    answering a Czech Biographer question would see a Russian follow-up."""

    token = _register_and_login(client, "candidates-owner5@example.com")
    profile_id = _create_memorial(client, token)
    _setup_indexed_biography(client, token, profile_id)

    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    assert question["topic"] == "childhood"

    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostla jsem na vesnici u řeky."},
    ).json()
    candidate_id = answer["candidate_id"]
    assert answer["unresolved_clarification_count"] == 2

    fetched = client.get(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}",
        headers=_auth_headers(token),
    )
    assert fetched.status_code == 200
    question_text = fetched.json()["next_clarification_question"]["question_text"]
    assert question_text in (
        "Kde se to obvykle odehrávalo?",
        "Kdy to bylo — přibližně v jakém věku, roce nebo období?",
    )
    assert "Где" not in question_text and "Когда" not in question_text


def test_candidate_history_returns_contributions_and_clarifications(client):
    """Task 65.4: the Review-tab candidate-detail view needs the original
    Biographer answer and every clarification round, not just the current
    finalized snapshot."""

    token = _register_and_login(client, "candidates-owner6@example.com")
    profile_id = _create_memorial(client, token)
    _setup_indexed_biography(client, token, profile_id)

    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    assert question["topic"] == "childhood"
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostla jsem na vesnici u řeky."},
    ).json()
    candidate_id = answer["candidate_id"]

    history = client.get(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/history",
        headers=_auth_headers(token),
    )
    assert history.status_code == 200
    body = history.json()
    assert body["candidate"]["candidate_id"] == candidate_id
    assert len(body["contributions"]) >= 1
    assert body["contributions"][0]["contribution_text"] == "Vyrostla jsem na vesnici u řeky."
    assert body["contributions"][0]["contribution_type"] == "initial_claim"
    # Clarification questions are created progressively (one at a time, not
    # all upfront) - at least the first one must already exist.
    assert len(body["clarifications"]) >= 1


def test_candidate_history_requires_membership(client):
    owner_token = _register_and_login(client, "candidates-owner7@example.com")
    outsider_token = _register_and_login(client, "candidates-outsider7@example.com")
    profile_id = _create_memorial(client, owner_token)
    _setup_indexed_biography(client, owner_token, profile_id)
    candidate_id, _ = _create_general_candidate_via_biographer(client, owner_token, profile_id)

    response = client.get(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/history",
        headers=_auth_headers(outsider_token),
    )
    assert response.status_code == 404

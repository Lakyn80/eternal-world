"""Task 65.2 - AI Biographer question/answer/clarification loop.

Reuses the fake-safe writer/encoder pattern to get a profile's biography
into `indexed` state (a precondition for Biographer eligibility) without any
real Qdrant/model calls, then exercises the authenticated HTTP surface.
"""

from __future__ import annotations

from app.db.models import BiographerQuestion, ConversationMemoryCandidate
from app.main import app
from app.modules.biography_ingestion.service import index_biography
from app.modules.embeddings.providers.base import EmbeddingVector


PASSWORD = "StrongPass123"


class FakeEncoder:
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=[0.01] * 1024, dimension=1024, metadata={})


class FakeWriter:
    def __init__(self) -> None:
        self.points: dict[tuple[str, str], dict[str, object]] = {}

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return 1024

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
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


def _create_memorial(client, token: str, name: str = "Biographer Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def _create_memorial_with_indexed_biography(client, email: str, biography: str = "Zivotopisny text.") -> tuple[str, int]:
    token = _register_and_login(client, email)
    profile_id = _create_memorial(client, token)
    patch = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": biography},
    )
    assert patch.status_code == 200
    start = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert start.status_code == 202

    db = _db()
    try:
        result = index_biography(db, profile_id=profile_id, writer=FakeWriter(), encoder=FakeEncoder(), validate_runtime=False)
        assert result.status == "indexed"
    finally:
        db.close()
    return token, profile_id


def test_eligibility_blocked_when_biography_missing(client):
    token = _register_and_login(client, "biographer-owner1@example.com")
    profile_id = _create_memorial(client, token)

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    body = response.json()
    assert body["eligible"] is False
    assert body["blocked_reason"] == "biography_missing"


def test_eligibility_blocked_when_biography_saved_but_not_indexed(client):
    token = _register_and_login(client, "biographer-owner2@example.com")
    profile_id = _create_memorial(client, token)
    client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Text bez indexace."},
    )

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    body = response.json()
    assert body["eligible"] is False
    assert body["blocked_reason"] == "biography_not_indexed"


def test_eligible_once_biography_indexed(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner3@example.com")

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    assert response.json() == {"eligible": True, "blocked_reason": None}


def test_next_question_starts_with_childhood_topic(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner4@example.com")

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["topic"] == "childhood"
    assert body["locale"] == "cs"
    assert body["status"] == "pending"


def test_answering_childhood_question_creates_candidate_with_required_clarification(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner5@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()

    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem na malé vesnici s prarodiči."},
    )
    assert answer.status_code == 200
    body = answer.json()
    assert body["candidate_id"] is not None
    assert body["enrichment_status"] == "collecting_details"
    assert body["unresolved_clarification_count"] == 2  # place + approximate_period

    db = _db()
    try:
        from app.db.models import MemoryProfile

        profile = db.get(MemoryProfile, profile_id)
        candidate = db.get(ConversationMemoryCandidate, body["candidate_id"])
        assert candidate.workflow_version == 2
        assert candidate.memory_type == "childhood_memory"
        assert candidate.status == "needs_review"
        assert candidate.owner_user_id == profile.user_id
    finally:
        db.close()


def test_active_candidate_with_unresolved_clarification_blocks_new_topic(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner6@example.com")
    childhood_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{childhood_question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem ve meste."},
    )

    # The candidate created above still has 2 unresolved required
    # clarifications - the eligibility gate must block offering a new topic
    # until they are answered, never silently skip ahead.
    eligibility = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token)).json()
    assert eligibility["eligible"] is False
    assert eligibility["blocked_reason"] == "active_candidate_requires_answer"

    blocked = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert blocked.status_code == 400


def test_answering_general_topic_question_has_no_required_clarification(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner6b@example.com")
    childhood_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{childhood_question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem ve meste."},
    ).json()
    candidate_id = answer["candidate_id"]

    # Resolve both required "childhood" clarifications via the shared
    # authenticated candidate/clarification endpoints (Task 65.2's owner-
    # review wrapper), so the candidate finalizes and a new topic unlocks.
    for answer_text in ["V malém bytě ve městě.", "Bylo mi asi šest let."]:
        resolve = client.post(
            f"/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/answer",
            headers=_auth_headers(token),
            json={"answer_text": answer_text},
        )
        assert resolve.status_code == 200
    assert resolve.json()["unresolved_clarification_count"] == 0
    assert resolve.json()["enrichment_status"] == "ready_for_owner_review"

    family_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert family_question.status_code == 200
    assert family_question.json()["topic"] == "family"

    family_answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{family_question.json()['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Moje maminka byla pro mě vždy nejdůležitější člověk."},
    )
    assert family_answer.status_code == 200
    body = family_answer.json()
    assert body["unresolved_clarification_count"] == 0
    assert body["enrichment_status"] == "ready_for_owner_review"

    db = _db()
    try:
        candidate = db.get(ConversationMemoryCandidate, body["candidate_id"])
        assert candidate.memory_type == "general"
    finally:
        db.close()


def test_skip_question_never_creates_a_candidate(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner7@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()

    response = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/skip",
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    assert response.json()["status"] == "skipped"
    assert response.json()["resulting_candidate_id"] is None

    db = _db()
    try:
        candidate_count = db.query(ConversationMemoryCandidate).filter(ConversationMemoryCandidate.profile_id == profile_id).count()
        assert candidate_count == 0
    finally:
        db.close()


def test_topics_are_never_repeated_across_multiple_next_question_calls(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner8@example.com")
    seen_topics: set[str] = set()
    for _ in range(8):
        question = client.get(
            f"/api/memorials/{profile_id}/biographer/next-question",
            params={"locale": "ru"},
            headers=_auth_headers(token),
        ).json()
        assert question["topic"] not in seen_topics
        seen_topics.add(question["topic"])
        client.post(
            f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/skip",
            headers=_auth_headers(token),
        )

    exhausted = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "ru"},
        headers=_auth_headers(token),
    )
    assert exhausted.status_code == 200
    assert exhausted.json() is None


def test_foreign_user_cannot_reach_biographer_endpoints(client):
    _owner_token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner9@example.com")
    outsider_token = _register_and_login(client, "biographer-outsider9@example.com")

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(outsider_token),
    )
    assert response.status_code == 404


def test_viewer_cannot_answer_biographer_questions(client):
    owner_token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner10@example.com")
    viewer_token = _register_and_login(client, "biographer-viewer10@example.com")
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "biographer-viewer10@example.com", "role": "viewer"},
    )
    assert invite.status_code == 201
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(viewer_token),
        json={"token": invite.json()["token"]},
    )

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(viewer_token),
    )
    assert response.status_code == 403

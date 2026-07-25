"""Task 65.7 / 65.7C - Authenticated Workspace Reliability, Stateful AI
Biographer, Redis Chat Sessions, Review Controls, and Complete Localization.

Covers: browser-session cookie auth (dual bearer+cookie), the AI Biographer
mandatory-clarification requirement (preserved, never bypassed for new
answers - Task 65.7C corrected an uncommitted Task 65.7 draft that had
disabled it; see `avatar_biographer/service.py` and `PROJECT_PROGRESS.md`),
genuinely-stuck-candidate repair (age-gated, never touching a candidate the
owner is still normally in the middle of answering), the Biographer resume
endpoint, Redis-backed Chat active-session restore/reset, and the
viewer-locale-aware clarification text fix. Every test in this file relies
on the global `_force_mock_ai_providers`/`_guard_against_real_provider_calls`
fixtures in `conftest.py` - no explicit local provider mocking is needed
here (unlike `test_avatar_biographer.py`, written before that global guard
existed).
"""

from __future__ import annotations

from app.db.models import BiographerQuestion, ConversationMemoryCandidate, MemoryClarificationQuestion
from app.main import app
from app.modules.avatar_biographer.repair import (
    find_stuck_biographer_candidates,
    repair_stuck_biographer_candidates,
)
from app.modules.biography_ingestion.service import index_biography
from app.modules.embeddings.providers.base import EmbeddingVector


PASSWORD = "StrongPass123!"


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


def _create_memorial(client, token: str, name: str = "Reliability Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def _create_memorial_with_indexed_biography(client, email: str, biography: str = "Zivotopisny text.") -> tuple[str, int]:
    token = _register_and_login(client, email)
    profile_id = _create_memorial(client, token)
    patch = client.patch(
        f"/api/memorials/{profile_id}/biography", headers=_auth_headers(token), json={"biography": biography}
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


# --- Browser session (cookie) authentication -------------------------------


def test_login_sets_httponly_session_cookie(client):
    email = "session-cookie-1@example.com"
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    set_cookie = response.headers.get("set-cookie", "")
    assert "eternal_world_session=" in set_cookie
    assert "httponly" in set_cookie.lower()
    assert "samesite=lax" in set_cookie.lower()
    # Part B.11: no persistent browser-side lifetime for the cookie itself.
    assert "max-age" not in set_cookie.lower()
    assert "expires" not in set_cookie.lower()


def test_session_endpoint_resolves_from_cookie_without_bearer_header(client):
    email = "session-cookie-2@example.com"
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    # The test client persists cookies across requests automatically; no
    # Authorization header is sent here at all.
    response = client.get("/api/auth/session")
    assert response.status_code == 200
    assert response.json()["email"] == email


def test_logout_revokes_session_and_subsequent_session_call_is_401(client):
    email = "session-cookie-3@example.com"
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert client.get("/api/auth/session").status_code == 200
    logout_response = client.post("/api/auth/logout")
    assert logout_response.status_code == 204
    assert client.get("/api/auth/session").status_code == 401


def test_bearer_token_still_works_independently_of_cookie(client):
    """Task 65.7 hard restriction: bearer authentication must not break."""

    email = "session-cookie-4@example.com"
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    login_response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    token = login_response.json()["access_token"]
    client.cookies.clear()
    response = client.get("/api/auth/me", headers=_auth_headers(token))
    assert response.status_code == 200
    assert response.json()["email"] == email


def test_missing_credentials_return_401_not_500(client):
    response = client.get("/api/auth/session")
    assert response.status_code == 401


# --- AI Biographer: mandatory clarification is preserved for new answers ---


def test_one_word_childhood_answer_creates_required_clarification_not_silently_skipped(client):
    """Task 65.7C regression coverage: an uncommitted Task 65.7 draft made
    every direct Biographer answer skip the topic's mandatory clarification
    bank entirely (`bypass_mandatory_clarifications_and_finalize`, called
    unconditionally). That directly contradicted the already-committed Task
    65.6 contract and this task's own Part E requirement ("required
    unanswered clarifications are not silently skipped") - removed. A short,
    thin childhood answer must still create the topic's required
    clarification(s), exactly as it did before that regression."""

    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-1@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    assert question["topic"] == "childhood"

    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Rádio"},
    )
    assert answer.status_code == 200
    body = answer.json()
    # childhood_memory requires place + approximate_period - a thin answer
    # must not be silently accepted as complete.
    assert body["unresolved_clarification_count"] == 2
    assert body["enrichment_status"] == "collecting_details"
    candidate_id = body["candidate_id"]

    db = _db()
    try:
        candidate = db.get(ConversationMemoryCandidate, candidate_id)
        assert candidate.status == "needs_review"
        assert candidate.enrichment_status == "collecting_details"
        assert candidate.unresolved_clarification_count == 2
        pending = (
            db.query(MemoryClarificationQuestion)
            .filter(MemoryClarificationQuestion.candidate_id == candidate_id, MemoryClarificationQuestion.status == "pending")
            .count()
        )
        # `initialize_candidate` only ever materializes the single NEXT
        # required clarification row at a time (not all required keys up
        # front) - exactly one pending row must exist, never zero/cancelled.
        assert pending == 1
        cancelled = (
            db.query(MemoryClarificationQuestion)
            .filter(MemoryClarificationQuestion.candidate_id == candidate_id, MemoryClarificationQuestion.status == "cancelled")
            .count()
        )
        assert cancelled == 0
    finally:
        db.close()


def test_answering_both_required_clarifications_then_reaches_ready_for_review(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-1b@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem ve meste."},
    ).json()
    candidate_id = answer["candidate_id"]

    resolve = None
    for answer_text in ["V malém bytě ve městě.", "Bylo mi asi šest let."]:
        resolve = client.post(
            f"/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/answer",
            headers=_auth_headers(token),
            json={"answer_text": answer_text},
        )
        assert resolve.status_code == 200
    assert resolve.json()["unresolved_clarification_count"] == 0
    assert resolve.json()["enrichment_status"] == "ready_for_owner_review"


def test_empty_answer_is_rejected_with_validation_error(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-2@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    response = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "   "},
    )
    assert response.status_code == 422


def test_candidate_visible_in_review_immediately_after_direct_answer(client):
    """A candidate must appear in the owner's review list immediately after
    a Biographer answer, regardless of whether its topic still has a
    mandatory clarification pending - visibility must never depend on
    enrichment completeness."""

    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-3@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    assert question["topic"] == "childhood"
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Nevím"},
    ).json()

    candidates = client.get(f"/api/memorials/{profile_id}/candidates", headers=_auth_headers(token)).json()
    matching = [c for c in candidates if c["candidate_id"] == answer["candidate_id"]]
    assert len(matching) == 1
    assert matching[0]["review_status"] == "needs_review"
    # childhood_memory still has its required place/approximate_period
    # clarifications outstanding - visible, but not yet ready for the owner
    # to approve.
    assert matching[0]["enrichment_status"] == "collecting_details"


# --- AI Biographer: resume endpoint -----------------------------------------


def test_resume_reflects_pending_question(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-4@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    resume = client.get(f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)).json()
    assert resume["eligible"] is True
    assert resume["next_action"] == "question_ready"
    assert resume["active_question"]["id"] == question["id"]


def test_resume_reflects_pending_clarification_after_answering(client):
    """childhood_memory's required clarifications mean the resume state
    right after answering is "please finish the pending clarification", not
    "ready for review" - the previous version of this test asserted the
    bypass-era immediate-ready-for-review behavior, which Task 65.7C
    corrected (see the module docstring)."""

    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-5@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Dědeček"},
    )
    resume = client.get(f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)).json()
    assert resume["eligible"] is False
    assert resume["blocked_reason"] == "active_clarification_exists"
    assert resume["next_action"] == "clarification_pending"
    assert resume["candidate_id"] is not None
    assert resume["enrichment_status"] == "collecting_details"
    assert resume["active_question"] is None


def test_resume_reflects_candidate_ready_for_review_after_clarifications_resolved(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-5b@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Dědeček"},
    ).json()
    candidate_id = answer["candidate_id"]
    for answer_text in ["Na vesnici.", "Bylo mi pět let."]:
        client.post(
            f"/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/answer",
            headers=_auth_headers(token),
            json={"answer_text": answer_text},
        )

    resume = client.get(f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)).json()
    assert resume["next_action"] == "candidate_ready_for_review"
    assert resume["candidate_id"] == candidate_id
    assert resume["active_question"] is None


def test_resume_blocked_when_biography_not_indexed(client):
    token = _register_and_login(client, "biographer-reliability-6@example.com")
    profile_id = _create_memorial(client, token)
    resume = client.get(f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)).json()
    assert resume["eligible"] is False
    assert resume["next_action"] == "biography_not_indexed"


# --- AI Biographer: stuck-candidate repair ----------------------------------


def _backdate_pending_clarification(db, *, candidate_id: int, hours_old: int) -> None:
    """Simulates a genuinely abandoned candidate: backdates its one pending
    required clarification's `asked_at` so it looks `hours_old` old. This is
    the ONLY thing that distinguishes a "stuck" candidate from a normal one
    the owner simply hasn't answered yet in the last few minutes."""

    from datetime import datetime, timedelta, timezone

    clarification = (
        db.query(MemoryClarificationQuestion)
        .filter(MemoryClarificationQuestion.candidate_id == candidate_id, MemoryClarificationQuestion.status == "pending")
        .order_by(MemoryClarificationQuestion.id.asc())
        .first()
    )
    assert clarification is not None
    clarification.asked_at = datetime.now(timezone.utc) - timedelta(hours=hours_old)
    db.commit()


def test_fresh_pending_clarification_is_never_treated_as_stuck(client):
    """A candidate the owner is normally, currently in the middle of
    answering (its required clarification was only just asked) must never
    be matched by the repair filter - repair must not race a real user."""

    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-7a@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Bylo to v létě."},
    ).json()
    candidate_id = answer["candidate_id"]
    assert answer["enrichment_status"] == "collecting_details"

    db = _db()
    try:
        stuck = find_stuck_biographer_candidates(db, profile_id=profile_id)
        assert stuck == []

        repaired = repair_stuck_biographer_candidates(db, profile_id=profile_id)
        assert repaired == []

        db.expire_all()
        candidate = db.get(ConversationMemoryCandidate, candidate_id)
        # Untouched: still normally awaiting its clarification answer.
        assert candidate.enrichment_status == "collecting_details"
        assert candidate.unresolved_clarification_count == 2
    finally:
        db.close()


def test_repair_finds_and_fixes_genuinely_stuck_candidate(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-7@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Bylo to v létě."},
    ).json()
    candidate_id = answer["candidate_id"]

    db = _db()
    try:
        _backdate_pending_clarification(db, candidate_id=candidate_id, hours_old=48)

        # Default threshold (24h) - candidate now qualifies.
        stuck = find_stuck_biographer_candidates(db, profile_id=profile_id)
        assert [c.id for c in stuck] == [candidate_id]

        repaired = repair_stuck_biographer_candidates(db, profile_id=profile_id)
        assert len(repaired) == 1
        assert repaired[0].candidate_id == candidate_id
        assert repaired[0].previous_enrichment_status == "collecting_details"
        assert repaired[0].new_enrichment_status == "ready_for_owner_review"

        db.expire_all()
        candidate = db.get(ConversationMemoryCandidate, candidate_id)
        assert candidate.enrichment_status == "ready_for_owner_review"
        assert candidate.unresolved_clarification_count == 0

        # Idempotent: running again finds nothing left to repair.
        second_pass = repair_stuck_biographer_candidates(db, profile_id=profile_id)
        assert second_pass == []
    finally:
        db.close()


def test_repair_respects_explicit_min_age_override_and_limit(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-7c@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Bylo to v létě."},
    ).json()
    candidate_id = answer["candidate_id"]

    db = _db()
    try:
        _backdate_pending_clarification(db, candidate_id=candidate_id, hours_old=2)

        # Default 24h threshold: too fresh, not matched.
        assert find_stuck_biographer_candidates(db, profile_id=profile_id) == []
        # Explicit override: a 1h threshold does match a 2h-old clarification.
        stuck = find_stuck_biographer_candidates(db, profile_id=profile_id, min_age_hours=1)
        assert [c.id for c in stuck] == [candidate_id]

        # A limit of 0 must repair nothing even though one candidate matches.
        repaired = repair_stuck_biographer_candidates(db, profile_id=profile_id, min_age_hours=1, limit=0)
        assert repaired == []
    finally:
        db.close()


def test_repair_never_touches_reviewed_or_indexed_candidates(client):
    """A candidate that was already approved (not stuck) must never match
    the repair filter, regardless of clarification history."""

    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-reliability-8@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Kolo"},
    ).json()
    candidate_id = answer["candidate_id"]
    for answer_text in ["Na vesnici.", "Bylo mi asi pět let."]:
        client.post(
            f"/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/answer",
            headers=_auth_headers(token),
            json={"answer_text": answer_text},
        )

    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm", "privacy_scope": "private_owner"},
    )
    assert review.status_code == 200

    db = _db()
    try:
        stuck = find_stuck_biographer_candidates(db, profile_id=profile_id)
        assert stuck == []
    finally:
        db.close()


# --- Chat: Redis-backed active session --------------------------------------


def test_chat_active_restores_ordered_transcript(client):
    token = _register_and_login(client, "chat-reliability-1@example.com")
    profile_id = _create_memorial(client, token)
    client.post(f"/api/chat/{profile_id}/messages", headers=_auth_headers(token), json={"message": "First question"})
    client.post(f"/api/chat/{profile_id}/messages", headers=_auth_headers(token), json={"message": "Second question"})

    active = client.get(f"/api/chat/{profile_id}/active", headers=_auth_headers(token)).json()
    assert active["restored_from"] == "redis"
    contents = [m["content"] for m in active["messages"] if m["role"] == "user"]
    assert contents == ["First question", "Second question"]


def test_chat_reset_creates_new_conversation_and_clears_visible_transcript(client):
    token = _register_and_login(client, "chat-reliability-2@example.com")
    profile_id = _create_memorial(client, token)
    send_response = client.post(
        f"/api/chat/{profile_id}/messages", headers=_auth_headers(token), json={"message": "Hello"}
    ).json()
    old_conversation_id = send_response["conversation_id"]

    reset_response = client.post(f"/api/chat/{profile_id}/reset", headers=_auth_headers(token))
    assert reset_response.status_code == 200
    reset_body = reset_response.json()
    assert reset_body["messages"] == []
    assert reset_body["conversation_id"] != old_conversation_id

    active_after_reset = client.get(f"/api/chat/{profile_id}/active", headers=_auth_headers(token)).json()
    assert active_after_reset["messages"] == []
    assert active_after_reset["conversation_id"] == reset_body["conversation_id"]

    new_send = client.post(
        f"/api/chat/{profile_id}/messages", headers=_auth_headers(token), json={"message": "New conversation message"}
    ).json()
    assert new_send["conversation_id"] == reset_body["conversation_id"]

    # The full unbounded history endpoint still has both conversations -
    # reset never deletes prior messages, it only rotates the active pointer.
    full_history = client.get(f"/api/chat/{profile_id}/messages", headers=_auth_headers(token)).json()
    assert len(full_history) == 4  # 2 old (user+assistant) + 2 new


def test_chat_active_profile_isolation(client):
    # Two separate owners (the plan limit caps one memorial per account,
    # per Task 65.5) - Redis/DB keys are namespaced by (user_id, profile_id),
    # so this still proves no cross-profile leakage of the active transcript.
    token_a = _register_and_login(client, "chat-reliability-3a@example.com")
    profile_a = _create_memorial(client, token_a, "Profile A")
    token_b = _register_and_login(client, "chat-reliability-3b@example.com")
    profile_b = _create_memorial(client, token_b, "Profile B")
    client.post(f"/api/chat/{profile_a}/messages", headers=_auth_headers(token_a), json={"message": "Message for A"})

    active_a = client.get(f"/api/chat/{profile_a}/active", headers=_auth_headers(token_a)).json()
    active_b = client.get(f"/api/chat/{profile_b}/active", headers=_auth_headers(token_b)).json()
    assert len(active_a["messages"]) == 2
    assert active_b["messages"] == []


def test_chat_active_rebuilds_from_database_on_redis_miss(client, monkeypatch):
    token = _register_and_login(client, "chat-reliability-4@example.com")
    profile_id = _create_memorial(client, token)
    client.post(f"/api/chat/{profile_id}/messages", headers=_auth_headers(token), json={"message": "Persisted question"})

    # Simulate a Redis miss (e.g. cache expiry/restart) without touching Postgres.
    from app.modules.chat import redis_snapshot

    monkeypatch.setattr(redis_snapshot, "read_snapshot", lambda **kwargs: None)

    active = client.get(f"/api/chat/{profile_id}/active", headers=_auth_headers(token)).json()
    assert active["restored_from"] == "database"
    assert len(active["messages"]) == 2


# --- Review: locale-aware clarification text --------------------------------


def test_clarification_text_localized_to_current_viewer_locale_not_original_answer_locale(client):
    """Reproduces the exact reported defect: a clarification originally
    created while the answering user's UI happened to be Russian must still
    render in Czech for a viewer whose CURRENT UI is Czech - never baked to
    whichever locale the original answerer used."""

    token = _register_and_login(client, "candidate-locale-1@example.com")
    profile_id = _create_memorial(client, token)

    # A bedtime_song-classified free-form contribution, in Russian, that
    # still needs clarification (the direct-Biographer bypass does not
    # apply to this workflow_version=1 / non-Biographer path).
    from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
    from app.modules.conversation_memory_candidates.service import create_candidate
    from app.modules.family_memory_enrichment.enums import EnrichmentStatus, FamilyMemoryActorRole, PrivacyScope
    from app.modules.family_memory_enrichment.schemas import DemoFamilyActorContext
    from app.modules.family_memory_enrichment.service import initialize_candidate

    db = _db()
    try:
        from app.db.models import MemoryProfile

        profile = db.get(MemoryProfile, profile_id)
        payload = MemoryCandidateCreate(
            owner_user_id=profile.user_id,
            avatar_id=str(profile.id),
            profile_id=profile.id,
            conversation_id=None,
            trace_id=None,
            user_message_excerpt="Ты помнишь, как ты пела мне колыбельную перед сном?",
            proposed_memory_text="Ты помнишь, как ты пела мне колыбельную перед сном?",
            reason="test",
            language="ru",
            enrichment_status=EnrichmentStatus.DRAFT,
            finalized_memory_text=None,
            privacy_scope=PrivacyScope.PRIVATE_OWNER,
            workflow_version=1,
        )
        candidate = create_candidate(db, payload=payload, commit=True)
        actor = DemoFamilyActorContext(actor_id=str(profile.user_id), actor_role=FamilyMemoryActorRole.OWNER)
        initialize_candidate(
            db,
            owner_user_id=profile.user_id,
            candidate_id=candidate.id,
            actor=actor,
            initial_text="Ты мне пела колыбельную перед сном.",
        )
        candidate_id = candidate.id
    finally:
        db.close()

    cs_view = client.get(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}", params={"locale": "cs"}, headers=_auth_headers(token)
    ).json()
    ru_view = client.get(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}", params={"locale": "ru"}, headers=_auth_headers(token)
    ).json()

    cs_text = cs_view["next_clarification_question"]["question_text"]
    ru_text = ru_view["next_clarification_question"]["question_text"]
    assert cs_text is not None
    assert ru_text is not None
    # Czech viewer must never see the raw Russian template text, regardless
    # of which specific clarification (song_title/place/approximate_period)
    # happens to be next.
    assert cs_text != ru_text
    assert not any(cyrillic_char in cs_text for cyrillic_char in "бвгдежзийклмнопрстуфхцчшщъыьэюя")
    assert any(cyrillic_char in ru_text for cyrillic_char in "бвгдежзийклмнопрстуфхцчшщъыьэюя")

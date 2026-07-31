"""Task 65.13.4 - Biographer canonical language + viewer question translations."""

from __future__ import annotations

from app.main import app
from app.modules.avatar_biographer import repository
from app.modules.content_translation.repository import get_current


PASSWORD = "StrongPass123"


def _register_and_login(client, email: str) -> str:
    client.post(
        "/api/auth/register",
        json={"email": email, "password": PASSWORD, "full_name": email.split("@")[0]},
    )
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _create_indexed_memorial(client, token: str, *, canonical_language: str = "cs") -> int:
    created = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Marie",
            "biography": "A sufficiently long biography text for biographer eligibility checks.",
            "canonical_language": canonical_language,
            "confirm_canonical_language": True,
        },
    )
    assert created.status_code == 201
    profile_id = int(created.json()["id"])

    # Mark biography indexed the same way other biographer tests do.
    db = app.state.testing_session_local()
    try:
        from app.db.models import MemoryProfile

        profile = db.get(MemoryProfile, profile_id)
        assert profile is not None
        profile.biography_status = "indexed"
        db.commit()
    finally:
        db.close()
    return profile_id


def test_generated_question_uses_canonical_language_not_ui_locale(client, monkeypatch):
    token = _register_and_login(client, "bio65-canon@example.com")
    profile_id = _create_indexed_memorial(client, token, canonical_language="cs")

    captured: dict[str, str] = {}

    def fake_generate(db, **kwargs):
        captured["locale"] = kwargs["locale"]
        from app.modules.avatar_biographer.question_generation import GeneratedQuestion

        return GeneratedQuestion(
            question_text="Jaké bylo vaše dětství?",
            generation_mode="deterministic_fallback",
            provider="mock",
            model="mock",
            ai_action_id=None,
            question_intent="specific_memory",
            validation_result="fallback_used",
            fallback_used=True,
        )

    monkeypatch.setattr(
        "app.modules.avatar_biographer.service.generate_question_for_topic",
        fake_generate,
    )
    monkeypatch.setattr(
        "app.modules.avatar_biographer.service._safe_context_batch",
        lambda *args, **kwargs: __import__(
            "app.modules.avatar_biographer.context_package", fromlist=["empty_context_batch"]
        ).empty_context_batch(
            __import__("app.modules.avatar_biographer.topics", fromlist=["BIOGRAPHER_TOPICS"]).BIOGRAPHER_TOPICS,
            locale=kwargs.get("locale", "cs"),
        ),
    )

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        headers=_auth_headers(token),
        params={"locale": "ru"},
    )
    assert response.status_code == 200
    body = response.json()
    assert captured["locale"] == "cs"
    assert body["locale"] == "cs"
    assert body["question_text"] == "Jaké bylo vaše dětství?"
    assert body["display_language"] == "ru"
    assert body["display_text"] is not None
    assert body["display_text"].startswith("[cs->ru] ") or body["display_text"] == body["question_text"]


def test_one_pending_across_ui_locales(client, monkeypatch):
    token = _register_and_login(client, "bio65-pending@example.com")
    profile_id = _create_indexed_memorial(client, token, canonical_language="cs")

    def fake_generate(db, **kwargs):
        from app.modules.avatar_biographer.question_generation import GeneratedQuestion

        return GeneratedQuestion(
            question_text="Canonical question once",
            generation_mode="deterministic_fallback",
            provider="mock",
            model="mock",
            ai_action_id=None,
            question_intent="specific_memory",
            validation_result="fallback_used",
            fallback_used=True,
        )

    monkeypatch.setattr(
        "app.modules.avatar_biographer.service.generate_question_for_topic",
        fake_generate,
    )
    monkeypatch.setattr(
        "app.modules.avatar_biographer.service._safe_context_batch",
        lambda *args, **kwargs: __import__(
            "app.modules.avatar_biographer.context_package", fromlist=["empty_context_batch"]
        ).empty_context_batch(
            __import__("app.modules.avatar_biographer.topics", fromlist=["BIOGRAPHER_TOPICS"]).BIOGRAPHER_TOPICS,
            locale=kwargs.get("locale", "cs"),
        ),
    )

    first = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        headers=_auth_headers(token),
        params={"locale": "cs"},
    )
    assert first.status_code == 200
    first_id = first.json()["id"]

    second = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        headers=_auth_headers(token),
        params={"locale": "en"},
    )
    assert second.status_code == 200
    assert second.json()["id"] == first_id
    assert second.json()["locale"] == "cs"

    db = app.state.testing_session_local()
    try:
        pending = repository.get_pending_question(db, profile_id=profile_id)
        assert pending is not None
        assert pending.id == first_id
        all_pending = [
            q for q in repository.list_questions_for_profile(db, profile_id=profile_id) if q.status == "pending"
        ]
        assert len(all_pending) == 1
    finally:
        db.close()


def test_foreign_language_answer_preserves_original_and_canonical_translation(client, monkeypatch):
    token = _register_and_login(client, "bio65-answer@example.com")
    profile_id = _create_indexed_memorial(client, token, canonical_language="cs")

    db = app.state.testing_session_local()
    try:
        question = repository.create_question(
            db,
            profile_id=profile_id,
            topic="work",
            locale="cs",
            question_text="Jaká byla vaše práce?",
        )
        db.commit()
        question_id = question.id
    finally:
        db.close()

    answer_text = "I worked as a teacher for twenty years."
    answered = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question_id}/answer",
        headers=_auth_headers(token),
        json={"locale": "en", "answer_text": answer_text, "source_language": "en"},
    )
    assert answered.status_code == 200
    candidate_id = answered.json()["candidate_id"]
    assert candidate_id is not None

    db = app.state.testing_session_local()
    try:
        from app.db.models import ConversationMemoryCandidate

        candidate = db.get(ConversationMemoryCandidate, candidate_id)
        assert candidate is not None
        assert candidate.language == "cs"
        row = get_current(
            db,
            entity_type="biographer_answer",
            entity_id=str(candidate_id),
            field_name="answer_text",
            target_language="cs",
        )
        assert row is not None
        assert row.source_text == answer_text
        assert row.translated_text is not None
        assert row.translated_text.startswith("[en->cs] ") or row.translated_text == answer_text
    finally:
        db.close()

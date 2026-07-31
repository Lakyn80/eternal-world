"""Task 65.13.5 - chat original + canonical user message; canonical assistant; viewer display."""

from __future__ import annotations

from app.db.models import ChatMessage
from app.main import app
from app.modules.content_translation.repository import get_current
from app.modules.content_translation.service import translate_content_field


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


def _set_ui_language(client, token: str, language: str) -> None:
    response = client.patch(
        "/api/auth/me/preferences",
        headers=_auth_headers(token),
        json={"preferred_ui_language": language},
    )
    assert response.status_code == 200


def _create_memorial(client, token: str, *, canonical_language: str = "cs") -> int:
    response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Chat Canon",
            "canonical_language": canonical_language,
            "confirm_canonical_language": True,
        },
    )
    assert response.status_code == 201
    return int(response.json()["id"])


def test_same_language_chat_uses_identity_and_preserves_original(client):
    token = _register_and_login(client, "chat65-same@example.com")
    _set_ui_language(client, token, "cs")
    profile_id = _create_memorial(client, token, canonical_language="cs")

    original = "Ahoj, vzpomínáš si na naši zahradu?"
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(token),
        json={"message": original},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["user_message"] == original
    assert body["user_message_language"] == "cs"
    assert body["ai_response_language"] == "cs"
    assert body["ai_response_translation_status"] == "identity"
    assert "[cs->cs]" not in body["ai_response_text"]
    assert "[cs->en]" not in body["ai_response_text"]

    db = app.state.testing_session_local()
    try:
        user_row = (
            db.query(ChatMessage)
            .filter(ChatMessage.memory_profile_id == profile_id, ChatMessage.role == "user")
            .one()
        )
        assert user_row.content == original
        assert user_row.source_language == "cs"
        assistant = (
            db.query(ChatMessage)
            .filter(ChatMessage.memory_profile_id == profile_id, ChatMessage.role == "assistant")
            .one()
        )
        assert assistant.content == body["ai_response_text"]
    finally:
        db.close()


def test_cross_language_chat_canonicalizes_user_and_translates_assistant(client):
    token = _register_and_login(client, "chat65-cross@example.com")
    # Default account UI is English — viewer display should stay English.
    profile_id = _create_memorial(client, token, canonical_language="cs")

    original = "Hello, do you remember our Sunday calls?"
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(token),
        json={"message": original},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["user_message"] == original
    assert body["user_message_language"] == "en"
    assert body["ai_response_language"] == "en"
    assert body["ai_response_translation_status"] == "translated"
    assert body["ai_response_text"].startswith("[cs->en] ")

    db = app.state.testing_session_local()
    try:
        user_row = (
            db.query(ChatMessage)
            .filter(ChatMessage.memory_profile_id == profile_id, ChatMessage.role == "user")
            .one()
        )
        assert user_row.content == original
        assert user_row.source_language == "en"

        user_mct = get_current(
            db,
            entity_type="chat_message",
            entity_id=str(user_row.id),
            field_name="content",
            target_language="cs",
        )
        assert user_mct is not None
        assert user_mct.translated_text is not None
        assert user_mct.translated_text.startswith("[en->cs] ")
        assert original in user_mct.translated_text

        assistant = (
            db.query(ChatMessage)
            .filter(ChatMessage.memory_profile_id == profile_id, ChatMessage.role == "assistant")
            .one()
        )
        # Durable assistant content is memorial-canonical (Czech lack-of-evidence
        # or mock reply), never the viewer-prefixed display string alone.
        assert not assistant.content.startswith("[cs->en] ")
        assert body["ai_response_text"] != assistant.content
        assert assistant.content in body["ai_response_text"]
    finally:
        db.close()


def test_assistant_display_translation_failure_falls_back_to_canonical(client, monkeypatch):
    token = _register_and_login(client, "chat65-fail@example.com")
    profile_id = _create_memorial(client, token, canonical_language="cs")

    real_translate = translate_content_field

    def flaky_translate(db, request, **kwargs):
        # Fail only assistant→viewer (cs→en). User→canonical still works.
        if request.target_language == "en" and request.source_language == "cs":
            from app.modules.content_translation import repository as ct_repo
            from app.modules.content_translation.service import compute_source_hash

            row = ct_repo.start_pending_attempt(
                db,
                profile_id=request.profile_id,
                candidate_id=None,
                contribution_id=None,
                clarification_id=None,
                entity_type=str(request.entity_type),
                entity_id=request.entity_id,
                field_name=request.field_name,
                source_language=str(request.source_language),
                target_language=str(request.target_language),
                source_text=request.source_text,
                source_hash=compute_source_hash(request.source_text),
            )
            ct_repo.mark_failed(db, row)
            return row
        return real_translate(db, request, **kwargs)

    monkeypatch.setattr(
        "app.modules.chat.message_translations.translate_content_field",
        flaky_translate,
    )

    original = "Hello from the failure path."
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(token),
        json={"message": original},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["user_message"] == original
    assert body["ai_response_translation_status"] == "fallback_original"
    assert body["ai_response_language"] == "cs"
    assert not body["ai_response_text"].startswith("[cs->en] ")

    db = app.state.testing_session_local()
    try:
        assistant = (
            db.query(ChatMessage)
            .filter(ChatMessage.memory_profile_id == profile_id, ChatMessage.role == "assistant")
            .one()
        )
        assert assistant.content == body["ai_response_text"]
    finally:
        db.close()


def test_second_turn_history_uses_canonical_user_text(client):
    token = _register_and_login(client, "chat65-hist@example.com")
    profile_id = _create_memorial(client, token, canonical_language="cs")

    first = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(token),
        json={"message": "Hello, first turn about Sunday."},
    )
    assert first.status_code == 200

    second = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(token),
        json={"message": "And what about Monday?"},
    )
    assert second.status_code == 200
    assert second.json()["ai_response_text"].startswith("[cs->en] ")

    db = app.state.testing_session_local()
    try:
        users = (
            db.query(ChatMessage)
            .filter(ChatMessage.memory_profile_id == profile_id, ChatMessage.role == "user")
            .order_by(ChatMessage.id.asc())
            .all()
        )
        assert users[0].content.startswith("Hello")
        assert users[1].content.startswith("And what")
        # Canonical MCT must exist for the first English turn (used as Brain history).
        first_mct = get_current(
            db,
            entity_type="chat_message",
            entity_id=str(users[0].id),
            field_name="content",
            target_language="cs",
        )
        assert first_mct is not None
        assert first_mct.translated_text is not None
        assert first_mct.translated_text.startswith("[en->cs] ")
    finally:
        db.close()

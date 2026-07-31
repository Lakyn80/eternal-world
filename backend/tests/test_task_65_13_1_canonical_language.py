"""Task 65.13.1 - canonical memorial language + user UI language foundation."""

from __future__ import annotations

from app.modules.language_registry import (
    APPLICATION_FALLBACK_CANONICAL_LANGUAGE,
    DEFAULT_UI_LANGUAGE,
    canonical_memorial_languages,
    chat_input_languages,
    is_canonical_memorial_language,
    is_ui_language,
    ui_languages,
)


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


def test_language_registry_capabilities_are_explicit():
    assert ui_languages() == ("cs", "en", "ru")
    assert canonical_memorial_languages() == ("cs", "en", "ru")
    assert "de" in chat_input_languages()
    assert is_ui_language("de") is False
    assert is_canonical_memorial_language("de") is False
    assert DEFAULT_UI_LANGUAGE == "en"
    assert APPLICATION_FALLBACK_CANONICAL_LANGUAGE == "cs"


def test_create_memorial_requires_canonical_language_confirmation(client):
    token = _register_and_login(client, "canonical-confirm@example.com")
    missing = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={"name": "Without confirm", "canonical_language": "cs"},
    )
    assert missing.status_code == 422

    rejected_lang = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "German canonical",
            "canonical_language": "de",
            "confirm_canonical_language": True,
        },
    )
    assert rejected_lang.status_code == 422

    created = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Marie",
            "canonical_language": "ru",
            "confirm_canonical_language": True,
        },
    )
    assert created.status_code == 201
    body = created.json()
    assert body["canonical_language"] == "ru"
    assert body["canonical_language_source"] == "creator_preference"
    assert body["canonical_language_locked_at"]


def test_canonical_language_is_immutable_on_memory_profile_update(client):
    token = _register_and_login(client, "canonical-immutable@example.com")
    created = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={
            "name": "Ada",
            "canonical_language": "en",
            "confirm_canonical_language": True,
        },
    )
    assert created.status_code == 201
    profile_id = created.json()["id"]
    assert created.json()["canonical_language"] == "en"

    rejected = client.patch(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
        json={"canonical_language": "cs"},
    )
    assert rejected.status_code == 422

    ok = client.patch(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
        json={"name": "Ada Lovelace"},
    )
    assert ok.status_code == 200
    assert ok.json()["canonical_language"] == "en"
    assert ok.json()["name"] == "Ada Lovelace"


def test_persona_languages_are_derived_and_not_patchable(client):
    token = _register_and_login(client, "persona-derived@example.com")
    created = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Derived Persona",
            "canonical_language": "cs",
            "confirm_canonical_language": True,
        },
    )
    assert created.status_code == 201
    profile_id = created.json()["id"]

    persona = client.get(
        f"/api/memorials/{profile_id}/avatar-persona",
        headers=_auth_headers(token),
    )
    assert persona.status_code == 200
    assert persona.json()["primary_language"] == "cs"

    rejected = client.patch(
        f"/api/memorials/{profile_id}/avatar-persona",
        headers=_auth_headers(token),
        json={"primary_language": "ru"},
    )
    assert rejected.status_code == 400

    still = client.get(
        f"/api/memorials/{profile_id}/avatar-persona",
        headers=_auth_headers(token),
    )
    assert still.json()["primary_language"] == "cs"


def test_user_preferred_ui_language_is_mutable_and_independent(client):
    token = _register_and_login(client, "ui-lang@example.com")
    me = client.get("/api/auth/me", headers=_auth_headers(token))
    assert me.status_code == 200
    assert me.json()["preferred_ui_language"] == "en"

    updated = client.patch(
        "/api/auth/me/preferences",
        headers=_auth_headers(token),
        json={"preferred_ui_language": "ru"},
    )
    assert updated.status_code == 200
    assert updated.json()["preferred_ui_language"] == "ru"

    memorial = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Independent",
            "canonical_language": "cs",
            "confirm_canonical_language": True,
        },
    )
    assert memorial.status_code == 201
    assert memorial.json()["canonical_language"] == "cs"

    me_again = client.get("/api/auth/me", headers=_auth_headers(token))
    assert me_again.json()["preferred_ui_language"] == "ru"

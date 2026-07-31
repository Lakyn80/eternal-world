"""Task 65.13.3 - contribution source language, canonical review, viewer display."""

from __future__ import annotations

from app.main import app
from app.modules.content_translation.repository import get_current
from app.modules.language_registry import DEFAULT_UI_LANGUAGE
from app.modules.memorial_contribution_indexing import repository as contribution_indexing_repository


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


def _create_memorial(client, token: str, *, canonical_language: str = "cs") -> int:
    response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Marie",
            "canonical_language": canonical_language,
            "confirm_canonical_language": True,
        },
    )
    assert response.status_code == 201
    return int(response.json()["id"])


def test_contribution_preserves_original_and_builds_canonical(client):
    owner_token = _register_and_login(client, "ct65-owner@example.com")
    profile_id = _create_memorial(client, owner_token, canonical_language="cs")

    contributor_token = _register_and_login(client, "ct65-contrib@example.com")
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "ct65-contrib@example.com", "role": "contributor"},
    )
    assert invite.status_code == 201
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(contributor_token),
        json={"token": invite.json()["token"]},
    )

    original = "My father always called me every Sunday."
    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(contributor_token),
        json={
            "title": "Sunday calls",
            "memory_text": original,
            "source_language": "en",
            "privacy_scope": "all_family",
        },
    )
    assert submitted.status_code == 201
    body = submitted.json()
    assert body["memory_text"] == original
    assert body["source_language"] == "en"
    assert body["canonical_language"] == "cs"
    assert body["canonical_text"] is not None
    assert body["canonical_text"].startswith("[en->cs] ")
    assert original in body["canonical_text"]

    db = app.state.testing_session_local()
    try:
        row = get_current(
            db,
            entity_type="memorial_contribution",
            entity_id=str(body["id"]),
            field_name="memory_text",
            target_language="cs",
        )
        assert row is not None
        assert row.profile_id == profile_id
        assert row.source_text == original
    finally:
        db.close()


def test_review_queue_uses_canonical_not_reviewer_ui_language(client):
    owner_token = _register_and_login(client, "ct65-review-owner@example.com")
    profile_id = _create_memorial(client, owner_token, canonical_language="cs")

    # Owner UI language Russian must not replace canonical review body.
    prefs = client.patch(
        "/api/auth/me/preferences",
        headers=_auth_headers(owner_token),
        json={"preferred_ui_language": "ru"},
    )
    assert prefs.status_code == 200

    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(owner_token),
        json={
            "title": "EN memory",
            "memory_text": "She loved garden roses.",
            "source_language": "en",
            "privacy_scope": "all_family",
        },
    )
    assert submitted.status_code == 201

    queue = client.get(
        f"/api/memorials/{profile_id}/review-queue",
        headers=_auth_headers(owner_token),
    )
    assert queue.status_code == 200
    item = queue.json()[0]
    assert item["memory_text"] == "She loved garden roses."
    assert item["canonical_language"] == "cs"
    assert item["display_language"] == "cs"
    assert item["display_text"] == item["canonical_text"]
    assert item["display_language"] != "ru"


def test_invitation_locale_hint_applied_on_accept_when_default_ui(client):
    owner_token = _register_and_login(client, "ct65-invite-owner@example.com")
    profile_id = _create_memorial(client, owner_token)

    invitee_token = _register_and_login(client, "ct65-invitee@example.com")
    me_before = client.get("/api/auth/me", headers=_auth_headers(invitee_token))
    assert me_before.status_code == 200
    assert me_before.json()["preferred_ui_language"] == DEFAULT_UI_LANGUAGE

    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={
            "email": "ct65-invitee@example.com",
            "role": "viewer",
            "preferred_locale_hint": "cs",
        },
    )
    assert invite.status_code == 201
    assert invite.json()["preferred_locale_hint"] == "cs"

    accepted = client.post(
        "/api/invitations/accept",
        headers=_auth_headers(invitee_token),
        json={"token": invite.json()["token"]},
    )
    assert accepted.status_code == 200

    me_after = client.get("/api/auth/me", headers=_auth_headers(invitee_token))
    assert me_after.status_code == 200
    assert me_after.json()["preferred_ui_language"] == "cs"


def test_approve_still_indexes_original_memory_text(client):
    owner_token = _register_and_login(client, "ct65-index-owner@example.com")
    profile_id = _create_memorial(client, owner_token, canonical_language="cs")
    original = "Original English contribution text for indexing."

    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(owner_token),
        json={
            "title": "Index check",
            "memory_text": original,
            "source_language": "en",
            "privacy_scope": "all_family",
        },
    )
    assert submitted.status_code == 201
    contribution_id = submitted.json()["id"]

    approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
        headers=_auth_headers(owner_token),
        json={},
    )
    assert approved.status_code == 200
    assert approved.json()["memory_text"] == original

    db = app.state.testing_session_local()
    try:
        promotion = contribution_indexing_repository.get_promotion_by_contribution_id(
            db, contribution_id=contribution_id
        )
        assert promotion is not None
        assert promotion.approved_memory_text == original
    finally:
        db.close()

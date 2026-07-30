"""Task 65.1B - membership-aware capability model applied to the legacy
chat/rag_retrieval endpoints, plus the MemorialCapability matrix itself.

Complements the existing `test_memorial_access.py` (which already covers
the Task 65 owner/reviewer/contributor/viewer role checks on the
`/api/memorials/...` endpoints - unchanged by this task) by covering the
*new* membership-aware behavior added on top of the previously
owner-only-authorized `/api/chat/...` and `/api/memory-profiles/.../rag/
retrieve` endpoints.
"""

from __future__ import annotations

from app.modules.memorial_access.capabilities import MemorialCapability, role_has_capability


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


def _create_memorial(client, token: str, name: str = "Capability Memorial") -> int:
    response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={"name": name},
    )
    assert response.status_code == 201
    return response.json()["id"]


def _invite_and_accept(client, owner_token: str, member_token: str, profile_id: int, email: str, role: str) -> None:
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": email, "role": role},
    )
    assert invite.status_code == 201
    accept = client.post(
        "/api/invitations/accept",
        headers=_auth_headers(member_token),
        json={"token": invite.json()["token"]},
    )
    assert accept.status_code == 200


# --- Pure capability matrix -------------------------------------------------


def test_owner_has_every_capability():
    for capability in MemorialCapability:
        assert role_has_capability("owner", capability) is True


def test_contributor_cannot_manage_members_or_review_or_write_directly():
    assert role_has_capability("contributor", MemorialCapability.SUBMIT_CONTRIBUTION) is True
    assert role_has_capability("contributor", MemorialCapability.CHAT_WITH_AVATAR) is True
    assert role_has_capability("contributor", MemorialCapability.SEARCH_APPROVED_MEMORY) is True
    assert role_has_capability("contributor", MemorialCapability.REVIEW_CONTRIBUTION) is False
    assert role_has_capability("contributor", MemorialCapability.MANAGE_MEMBERS) is False
    assert role_has_capability("contributor", MemorialCapability.MANAGE_MEMORIAL) is False
    assert role_has_capability("contributor", MemorialCapability.DIRECT_MEMORY_WRITE) is False
    assert role_has_capability("contributor", MemorialCapability.UPLOAD_SOURCE) is False
    assert role_has_capability("contributor", MemorialCapability.TRIGGER_INDEXING) is False


def test_viewer_can_only_view_chat_and_search():
    assert role_has_capability("viewer", MemorialCapability.VIEW_MEMORIAL) is True
    assert role_has_capability("viewer", MemorialCapability.CHAT_WITH_AVATAR) is True
    assert role_has_capability("viewer", MemorialCapability.SEARCH_APPROVED_MEMORY) is True
    assert role_has_capability("viewer", MemorialCapability.SUBMIT_CONTRIBUTION) is False
    assert role_has_capability("viewer", MemorialCapability.REVIEW_CONTRIBUTION) is False
    assert role_has_capability("viewer", MemorialCapability.MANAGE_MEMBERS) is False


def test_trusted_reviewer_cannot_manage_membership_or_write_directly():
    assert role_has_capability("trusted_reviewer", MemorialCapability.REVIEW_CONTRIBUTION) is True
    assert role_has_capability("trusted_reviewer", MemorialCapability.MANAGE_MEMBERS) is False
    assert role_has_capability("trusted_reviewer", MemorialCapability.MANAGE_MEMORIAL) is False
    assert role_has_capability("trusted_reviewer", MemorialCapability.DIRECT_MEMORY_WRITE) is False


def test_unknown_role_has_no_capabilities():
    assert role_has_capability("not-a-real-role", MemorialCapability.VIEW_MEMORIAL) is False


# --- Chat: membership-aware, not owner-only ---------------------------------


def test_owner_can_still_chat_with_own_memorial(client):
    owner_token = _register_and_login(client, "chat-owner@example.com")
    profile_id = _create_memorial(client, owner_token, "Owner Chat Memorial")

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(owner_token),
        json={"message": "Hello"},
    )

    assert response.status_code == 200
    assert response.json()["profile_id"] == profile_id


def test_contributor_and_viewer_can_chat_with_authorized_memorial(client):
    owner_token = _register_and_login(client, "chat-mem-owner@example.com")
    contributor_token = _register_and_login(client, "chat-mem-contributor@example.com")
    viewer_token = _register_and_login(client, "chat-mem-viewer@example.com")
    profile_id = _create_memorial(client, owner_token, "Family Chat Memorial")
    _invite_and_accept(client, owner_token, contributor_token, profile_id, "chat-mem-contributor@example.com", "contributor")
    _invite_and_accept(client, owner_token, viewer_token, profile_id, "chat-mem-viewer@example.com", "viewer")

    contributor_response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(contributor_token),
        json={"message": "What did she love?"},
    )
    viewer_response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(viewer_token),
        json={"message": "Tell me about her"},
    )
    viewer_history = client.get(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(viewer_token),
    )

    assert contributor_response.status_code == 200
    assert viewer_response.status_code == 200
    assert viewer_history.status_code == 200
    # Each member's conversation is their own - the viewer's history must not
    # contain the contributor's messages.
    viewer_contents = {message["content"] for message in viewer_history.json()}
    assert "What did she love?" not in viewer_contents
    assert "Tell me about her" in viewer_contents


def test_non_member_gets_safe_404_from_chat_and_retrieval(client):
    owner_token = _register_and_login(client, "chat-priv-owner@example.com")
    outsider_token = _register_and_login(client, "chat-priv-outsider@example.com")
    profile_id = _create_memorial(client, owner_token, "Private Memorial")

    chat_response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(outsider_token),
        json={"message": "Who are you?"},
    )
    history_response = client.get(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(outsider_token),
    )
    retrieve_response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(outsider_token),
        json={"query": "anything"},
    )

    assert chat_response.status_code == 404
    assert history_response.status_code == 404
    assert retrieve_response.status_code in (404, 503)
    if retrieve_response.status_code == 200:  # pragma: no cover - defensive
        raise AssertionError("Non-member must never receive a 200 retrieval response")


def test_unrelated_users_conversations_never_mix_on_same_memorial(client):
    owner_token = _register_and_login(client, "chat-iso-owner@example.com")
    contributor_token = _register_and_login(client, "chat-iso-contributor@example.com")
    profile_id = _create_memorial(client, owner_token, "Isolation Memorial")
    _invite_and_accept(client, owner_token, contributor_token, profile_id, "chat-iso-contributor@example.com", "contributor")

    client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(owner_token),
        json={"message": "Owner secret question"},
    )
    client.post(
        f"/api/chat/{profile_id}/messages",
        headers=_auth_headers(contributor_token),
        json={"message": "Contributor question"},
    )

    owner_history = client.get(f"/api/chat/{profile_id}/messages", headers=_auth_headers(owner_token)).json()
    contributor_history = client.get(
        f"/api/chat/{profile_id}/messages", headers=_auth_headers(contributor_token)
    ).json()

    owner_contents = {message["content"] for message in owner_history}
    contributor_contents = {message["content"] for message in contributor_history}
    assert "Owner secret question" in owner_contents
    assert "Owner secret question" not in contributor_contents
    assert "Contributor question" in contributor_contents
    assert "Contributor question" not in owner_contents

import httpx

import pytest

from app.core.config import settings


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Memory User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return login_response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _create_profile(client, token: str, name: str) -> int:
    response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": name},
    )
    return response.json()["id"]


def _create_memory(client, token: str, profile_id: int, **overrides) -> dict:
    payload = {
        "title": "Memory Title",
        "content": "Memory content",
        "memory_type": "text",
    }
    payload.update(overrides)
    response = client.post(
        f"/api/memory-profiles/{profile_id}/memories",
        headers=_auth_headers(token),
        json=payload,
    )
    return {"response": response, "body": response.json() if response.content else None}


def _upload_media(client, token: str, filename: str, content: bytes, mime_type: str) -> dict:
    response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": (filename, content, mime_type)},
    )
    return response.json()


@pytest.fixture(autouse=True)
def media_settings(tmp_path, monkeypatch):
    media_root = tmp_path / "media"
    monkeypatch.setattr(settings, "media_storage_provider", "local")
    monkeypatch.setattr(settings, "media_root", media_root)
    monkeypatch.setattr(settings, "media_public_base_url", "/media")
    monkeypatch.setattr(settings, "media_max_file_size_bytes", 1024)
    return media_root


def test_authenticated_user_can_create_text_memory_under_own_profile(client):
    token = _register_and_login(client, "memory-create@example.com")
    profile_id = _create_profile(client, token, "Memory Profile")

    result = _create_memory(
        client,
        token,
        profile_id,
        title="  First Memory  ",
        content="  Important life event  ",
    )

    assert result["response"].status_code == 201
    assert result["body"]["profile_id"] == profile_id
    assert result["body"]["title"] == "First Memory"
    assert result["body"]["content"] == "Important life event"
    assert result["body"]["memory_type"] == "text"
    assert result["body"]["media_id"] is None


def test_unauthenticated_user_cannot_create_memory(client):
    token = _register_and_login(client, "memory-auth-owner@example.com")
    profile_id = _create_profile(client, token, "Protected Profile")

    client.cookies.clear()
    response = client.post(
        f"/api/memory-profiles/{profile_id}/memories",
        json={"title": "Blocked", "memory_type": "text"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_cannot_create_memory_under_another_users_profile(client):
    owner_token = _register_and_login(client, "memory-owner-create@example.com")
    other_token = _register_and_login(client, "memory-other-create@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Profile")

    response = client.post(
        f"/api/memory-profiles/{profile_id}/memories",
        headers=_auth_headers(other_token),
        json={"title": "Blocked", "memory_type": "text"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_user_can_list_only_own_profile_memories(client):
    first_token = _register_and_login(client, "memory-list-first@example.com")
    second_token = _register_and_login(client, "memory-list-second@example.com")
    first_profile_id = _create_profile(client, first_token, "First Profile")
    second_profile_id = _create_profile(client, second_token, "Second Profile")
    _create_memory(client, first_token, first_profile_id, title="First Memory")
    _create_memory(client, second_token, second_profile_id, title="Second Memory")

    response = client.get(
        f"/api/memory-profiles/{first_profile_id}/memories",
        headers=_auth_headers(first_token),
    )

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["title"] == "First Memory"


def test_user_can_read_own_memory(client):
    token = _register_and_login(client, "memory-read@example.com")
    profile_id = _create_profile(client, token, "Read Profile")
    created_memory = _create_memory(client, token, profile_id, title="Readable Memory")
    memory_id = created_memory["body"]["id"]

    response = client.get(f"/api/memories/{memory_id}", headers=_auth_headers(token))

    assert response.status_code == 200
    assert response.json()["title"] == "Readable Memory"


def test_user_cannot_read_another_users_memory(client):
    owner_token = _register_and_login(client, "memory-read-owner@example.com")
    other_token = _register_and_login(client, "memory-read-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Read Profile")
    created_memory = _create_memory(client, owner_token, profile_id, title="Private Memory")
    memory_id = created_memory["body"]["id"]

    response = client.get(f"/api/memories/{memory_id}", headers=_auth_headers(other_token))

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory not found"


def test_user_can_update_own_memory(client):
    token = _register_and_login(client, "memory-update@example.com")
    profile_id = _create_profile(client, token, "Update Profile")
    created_memory = _create_memory(client, token, profile_id, title="Old Title")
    memory_id = created_memory["body"]["id"]

    response = client.patch(
        f"/api/memories/{memory_id}",
        headers=_auth_headers(token),
        json={
            "title": "Updated Title",
            "content": " Updated content ",
            "occurred_year": 2001,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Updated Title"
    assert body["content"] == "Updated content"
    assert body["occurred_year"] == 2001


def test_user_cannot_update_another_users_memory(client):
    owner_token = _register_and_login(client, "memory-update-owner@example.com")
    other_token = _register_and_login(client, "memory-update-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Update Profile")
    created_memory = _create_memory(client, owner_token, profile_id, title="Immutable Memory")
    memory_id = created_memory["body"]["id"]

    response = client.patch(
        f"/api/memories/{memory_id}",
        headers=_auth_headers(other_token),
        json={"title": "Blocked Update"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory not found"


def test_user_can_delete_own_memory(client):
    token = _register_and_login(client, "memory-delete@example.com")
    profile_id = _create_profile(client, token, "Delete Profile")
    created_memory = _create_memory(client, token, profile_id, title="Delete Memory")
    memory_id = created_memory["body"]["id"]

    delete_response = client.delete(f"/api/memories/{memory_id}", headers=_auth_headers(token))
    get_response = client.get(f"/api/memories/{memory_id}", headers=_auth_headers(token))

    assert delete_response.status_code == 204
    assert get_response.status_code == 404


def test_user_cannot_delete_another_users_memory(client):
    owner_token = _register_and_login(client, "memory-delete-owner@example.com")
    other_token = _register_and_login(client, "memory-delete-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Delete Profile")
    created_memory = _create_memory(client, owner_token, profile_id, title="Private Delete Memory")
    memory_id = created_memory["body"]["id"]

    response = client.delete(f"/api/memories/{memory_id}", headers=_auth_headers(other_token))

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory not found"


def test_memory_list_is_timeline_ordered(client):
    token = _register_and_login(client, "memory-timeline@example.com")
    profile_id = _create_profile(client, token, "Timeline Profile")
    _create_memory(client, token, profile_id, title="Created Only")
    _create_memory(client, token, profile_id, title="Year Only", occurred_year=2010)
    _create_memory(
        client,
        token,
        profile_id,
        title="Occurred At",
        occurred_at="2024-05-06T10:30:00Z",
    )

    response = client.get(
        f"/api/memory-profiles/{profile_id}/memories",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert [memory["title"] for memory in response.json()] == [
        "Occurred At",
        "Year Only",
        "Created Only",
    ]


def test_free_user_cannot_create_more_than_10_memories(client):
    token = _register_and_login(client, "memory-limit@example.com")
    profile_id = _create_profile(client, token, "Limit Profile")

    for index in range(10):
        response = client.post(
            f"/api/memory-profiles/{profile_id}/memories",
            headers=_auth_headers(token),
            json={"title": f"Memory {index}", "memory_type": "text"},
        )
        assert response.status_code == 201

    overflow_response = client.post(
        f"/api/memory-profiles/{profile_id}/memories",
        headers=_auth_headers(token),
        json={"title": "Memory 10", "memory_type": "text"},
    )

    assert overflow_response.status_code == 403
    assert overflow_response.json() == {
        "detail": "Memory limit exceeded for current plan",
        "error": "limit_exceeded",
        "code": "memory_limit_exceeded",
    }


def test_memory_limit_counts_only_current_users_memories(client):
    other_token = _register_and_login(client, "memory-limit-other@example.com")
    current_token = _register_and_login(client, "memory-limit-current@example.com")
    other_profile_id = _create_profile(client, other_token, "Other Limit Profile")
    current_profile_id = _create_profile(client, current_token, "Current Limit Profile")

    for index in range(10):
        other_response = client.post(
            f"/api/memory-profiles/{other_profile_id}/memories",
            headers=_auth_headers(other_token),
            json={"title": f"Other Memory {index}", "memory_type": "text"},
        )
        assert other_response.status_code == 201

    first_current_response = client.post(
        f"/api/memory-profiles/{current_profile_id}/memories",
        headers=_auth_headers(current_token),
        json={"title": "Current Memory 0", "memory_type": "text"},
    )

    assert first_current_response.status_code == 201


def test_media_ownership_is_enforced_when_linking_media_id(client):
    owner_token = _register_and_login(client, "memory-media-owner@example.com")
    other_token = _register_and_login(client, "memory-media-other@example.com")
    owner_media = _upload_media(client, owner_token, "voice.wav", b"wav-bytes", "audio/wav")
    other_profile_id = _create_profile(client, other_token, "Other Media Profile")

    response = client.post(
        f"/api/memory-profiles/{other_profile_id}/memories",
        headers=_auth_headers(other_token),
        json={
            "title": "Foreign Media Memory",
            "memory_type": "audio",
            "media_id": owner_media["id"],
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Media not found"


def test_media_type_compatibility_is_enforced(client):
    token = _register_and_login(client, "memory-media-compat@example.com")
    profile_id = _create_profile(client, token, "Compat Profile")
    audio_media = _upload_media(client, token, "voice.wav", b"wav-bytes", "audio/wav")

    response = client.post(
        f"/api/memory-profiles/{profile_id}/memories",
        headers=_auth_headers(token),
        json={
            "title": "Wrong Media Type",
            "memory_type": "photo",
            "media_id": audio_media["id"],
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Media is not compatible with memory type"


def test_no_external_api_calls_are_made_for_memory_crud(client, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for memories foundation")

    monkeypatch.setattr(httpx, "request", fail_http_call)
    monkeypatch.setattr(httpx, "get", fail_http_call)
    monkeypatch.setattr(httpx, "post", fail_http_call)

    token = _register_and_login(client, "memory-no-http@example.com")
    profile_id = _create_profile(client, token, "No HTTP Profile")

    create_response = client.post(
        f"/api/memory-profiles/{profile_id}/memories",
        headers=_auth_headers(token),
        json={"title": "No HTTP Memory", "memory_type": "text"},
    )
    list_response = client.get(
        f"/api/memory-profiles/{profile_id}/memories",
        headers=_auth_headers(token),
    )

    assert create_response.status_code == 201
    assert list_response.status_code == 200

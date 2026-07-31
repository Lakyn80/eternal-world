def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Chat Test User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return login_response.json()["access_token"]


def _create_profile(client, token: str, name: str = "Chat Profile") -> int:
    response = client.post(
        "/api/memory-profiles",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": name, "canonical_language": "cs", "confirm_canonical_language": True},
    )
    return response.json()["id"]


def test_authenticated_user_can_send_message_to_own_profile(client):
    token = _register_and_login(client, "chat-owner@example.com")
    profile_id = _create_profile(client, token)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Hello there"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["profile_id"] == profile_id
    assert body["user_message"] == "Hello there"
    assert body["ai_response_text"] == "Chat Profile mock reply: I heard 'Hello there'. Recent messages considered: 0."
    assert body["audio_url"] is None
    assert body["video_url"] is None


def test_chat_message_stores_user_message_and_ai_response_text(client):
    token = _register_and_login(client, "chat-storage@example.com")
    profile_id = _create_profile(client, token)

    send_response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Remember this line"},
    )
    history_response = client.get(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert send_response.status_code == 200
    assert history_response.status_code == 200
    history = history_response.json()
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Remember this line"
    assert history[1]["role"] == "assistant"
    assert history[1]["content"] == send_response.json()["ai_response_text"]


def test_authenticated_user_can_list_own_chat_history(client):
    token = _register_and_login(client, "chat-history@example.com")
    profile_id = _create_profile(client, token)

    client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "First"},
    )
    client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Second"},
    )

    response = client.get(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    history = response.json()
    assert len(history) == 4
    assert history[0]["content"] == "First"
    assert history[2]["content"] == "Second"


def test_unauthenticated_send_is_rejected(client):
    token = _register_and_login(client, "chat-unauth-send@example.com")
    profile_id = _create_profile(client, token)

    # Task 65.7C: login (above) sets a Redis-backed browser-session cookie
    # on this shared TestClient - a real unauthenticated request carries
    # neither a bearer token nor that cookie, so it must be cleared here to
    # actually exercise the "no credentials at all" path this test targets.
    client.cookies.clear()
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        json={"message": "Blocked"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_unauthenticated_history_request_is_rejected(client):
    token = _register_and_login(client, "chat-unauth-history@example.com")
    profile_id = _create_profile(client, token)

    client.cookies.clear()
    response = client.get(f"/api/chat/{profile_id}/messages")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_cannot_send_message_to_another_users_profile(client):
    owner_token = _register_and_login(client, "chat-owner-two@example.com")
    other_user_token = _register_and_login(client, "chat-other-two@example.com")
    profile_id = _create_profile(client, owner_token, name="Private Chat Profile")

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {other_user_token}"},
        json={"message": "Unauthorized"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_user_cannot_read_another_users_chat_history(client):
    owner_token = _register_and_login(client, "chat-owner-three@example.com")
    other_user_token = _register_and_login(client, "chat-other-three@example.com")
    profile_id = _create_profile(client, owner_token, name="Another Private Profile")

    client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {owner_token}"},
        json={"message": "Owner history"},
    )
    response = client.get(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {other_user_token}"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_sql_like_text_is_treated_as_normal_user_content(client):
    token = _register_and_login(client, "chat-sql-like@example.com")
    profile_id = _create_profile(client, token)
    user_text = "Robert'); DROP TABLE chat_messages; --"

    send_response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": user_text},
    )
    history_response = client.get(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert send_response.status_code == 200
    assert history_response.status_code == 200
    assert history_response.json()[0]["content"] == user_text

def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Test User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return login_response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def test_create_memory_profile_for_authenticated_user(client):
    token = _register_and_login(client, "profile-owner@example.com")

    response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={
            "name": "Ada Lovelace",
            "biography": "Mathematician and writer",
            "is_public": True,
            "canonical_language": "cs",
            "confirm_canonical_language": True,
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Ada Lovelace"
    assert body["biography"] == "Mathematician and writer"
    assert body["is_public"] is True


def test_free_user_cannot_create_second_memory_profile(client):
    token = _register_and_login(client, "free-limit@example.com")

    first_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": "First Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    second_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": "Second Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 403
    assert second_response.json() == {
        "detail": "Memory profile limit exceeded for current plan",
        "error": "limit_exceeded",
        "code": "profile_limit_exceeded",
    }


def test_another_users_profiles_do_not_affect_current_users_limit(client):
    other_user_token = _register_and_login(client, "other-limit@example.com")
    current_user_token = _register_and_login(client, "current-limit@example.com")

    other_user_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(other_user_token),
        json={"name": "Other User Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    current_user_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(current_user_token),
        json={"name": "Current User Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )

    assert other_user_response.status_code == 201
    assert current_user_response.status_code == 201


def test_profile_limit_counts_only_current_users_profiles(client):
    first_user_token = _register_and_login(client, "first-limit-count@example.com")
    second_user_token = _register_and_login(client, "second-limit-count@example.com")

    first_user_first_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(first_user_token),
        json={"name": "First User Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    second_user_first_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(second_user_token),
        json={"name": "Second User Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    second_user_second_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(second_user_token),
        json={"name": "Second User Extra Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )

    assert first_user_first_response.status_code == 201
    assert second_user_first_response.status_code == 201
    assert second_user_second_response.status_code == 403
    assert second_user_second_response.json()["code"] == "profile_limit_exceeded"


def test_list_memory_profiles_returns_only_current_user_profiles(client):
    first_user_token = _register_and_login(client, "first-profiles@example.com")
    second_user_token = _register_and_login(client, "second-profiles@example.com")

    client.post(
        "/api/memory-profiles",
        headers=_auth_headers(first_user_token),
        json={"name": "First User Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    client.post(
        "/api/memory-profiles",
        headers=_auth_headers(second_user_token),
        json={"name": "Second User Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )

    response = client.get(
        "/api/memory-profiles",
        headers=_auth_headers(first_user_token),
    )

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["name"] == "First User Profile"


def test_get_own_memory_profile(client):
    token = _register_and_login(client, "get-profile@example.com")
    create_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": "Grace Hopper", "personality": "Analytical", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    profile_id = create_response.json()["id"]

    response = client.get(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Grace Hopper"


def test_update_own_memory_profile(client):
    token = _register_and_login(client, "update-profile@example.com")
    create_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": "Original Name", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    profile_id = create_response.json()["id"]

    response = client.patch(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
        json={
            "name": "Updated Name",
            "catchphrases": "Keep moving forward",
            "is_public": True,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Updated Name"
    assert body["catchphrases"] == "Keep moving forward"
    assert body["is_public"] is True


def test_delete_own_memory_profile(client):
    token = _register_and_login(client, "delete-profile@example.com")
    create_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": "Delete Me", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    profile_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
    )
    get_response = client.get(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
    )

    assert delete_response.status_code == 204
    assert get_response.status_code == 404


def test_memory_profiles_require_authentication(client):
    response = client.get("/api/memory-profiles")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_cannot_access_another_users_memory_profile(client):
    owner_token = _register_and_login(client, "owner-profile@example.com")
    other_user_token = _register_and_login(client, "other-profile@example.com")
    create_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(owner_token),
        json={"name": "Private Profile", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    profile_id = create_response.json()["id"]

    response = client.get(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(other_user_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_sql_like_text_is_treated_as_normal_profile_content(client):
    token = _register_and_login(client, "sql-like-profile@example.com")

    create_response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={
            "name": "Safe Profile",
            "biography": "Robert'); DROP TABLE memory_profiles; --",
            "canonical_language": "cs",
            "confirm_canonical_language": True,
        },
    )
    profile_id = create_response.json()["id"]
    get_response = client.get(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
    )

    assert create_response.status_code == 201
    assert get_response.status_code == 200
    assert get_response.json()["biography"] == "Robert'); DROP TABLE memory_profiles; --"

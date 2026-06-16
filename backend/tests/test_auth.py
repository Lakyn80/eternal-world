def test_register_user_success(client):
    response = client.post(
        "/api/auth/register",
        json={
            "email": "new-user@example.com",
            "password": "StrongPass123",
            "full_name": "New User",
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["email"] == "new-user@example.com"
    assert body["full_name"] == "New User"
    assert body["is_active"] is True


def test_register_user_rejects_duplicate_email(client):
    payload = {
        "email": "duplicate@example.com",
        "password": "StrongPass123",
        "full_name": "Duplicate User",
    }

    first_response = client.post("/api/auth/register", json=payload)
    second_response = client.post("/api/auth/register", json=payload)

    assert first_response.status_code == 201
    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "A user with this email already exists"


def test_login_success_returns_access_token(client):
    register_payload = {
        "email": "login-user@example.com",
        "password": "StrongPass123",
        "full_name": "Login User",
    }

    client.post("/api/auth/register", json=register_payload)
    response = client.post(
        "/api/auth/login",
        json={"email": register_payload["email"], "password": register_payload["password"]},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert body["access_token"]


def test_login_rejects_wrong_password(client):
    register_payload = {
        "email": "wrong-password@example.com",
        "password": "StrongPass123",
        "full_name": "Wrong Password User",
    }

    client.post("/api/auth/register", json=register_payload)
    response = client.post(
        "/api/auth/login",
        json={"email": register_payload["email"], "password": "BadPassword123"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_me_returns_authenticated_user(client):
    register_payload = {
        "email": "me-user@example.com",
        "password": "StrongPass123",
        "full_name": "Me User",
    }

    client.post("/api/auth/register", json=register_payload)
    login_response = client.post(
        "/api/auth/login",
        json={"email": register_payload["email"], "password": register_payload["password"]},
    )
    access_token = login_response.json()["access_token"]

    me_response = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert me_response.status_code == 200
    body = me_response.json()
    assert body["email"] == register_payload["email"]
    assert body["full_name"] == register_payload["full_name"]


def test_me_requires_authentication(client):
    response = client.get("/api/auth/me")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_register_rejects_sql_injection_like_email_input(client):
    response = client.post(
        "/api/auth/register",
        json={
            "email": "admin@example.com' OR 1=1 --",
            "password": "StrongPass123",
            "full_name": "Unsafe Input",
        },
    )

    assert response.status_code == 422

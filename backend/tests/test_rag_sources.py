import httpx

from app.db.models import RagSource
from app.db.session import get_db
from app.main import app


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "RAG Source User",
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


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Source Title",
        "raw_text": "Source raw text",
        "source_type": "manual_text",
    }
    payload.update(overrides)
    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
        json=payload,
    )
    return response


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def test_authenticated_user_can_create_rag_source_under_own_profile(client):
    token = _register_and_login(client, "rag-create@example.com")
    profile_id = _create_profile(client, token, "RAG Profile")

    response = _create_rag_source(
        client,
        token,
        profile_id,
        title="  Imported Biography  ",
        raw_text="  Raw source text for ingestion.  ",
        language=" EN ",
        source_metadata={"origin": "manual"},
    )

    assert response.status_code == 201
    body = response.json()
    assert body["profile_id"] == profile_id
    assert body["title"] == "Imported Biography"
    assert body["raw_text"] == "Raw source text for ingestion."
    assert body["normalized_text"] == "Raw source text for ingestion."
    assert body["source_type"] == "manual_text"
    assert body["language"] == "en"
    assert body["status"] == "ready_for_cleaning"
    assert body["source_metadata"] == {"origin": "manual"}


def test_unauthenticated_user_cannot_create_rag_source(client):
    token = _register_and_login(client, "rag-unauth@example.com")
    profile_id = _create_profile(client, token, "Protected RAG Profile")

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        json={"title": "Blocked", "raw_text": "Blocked text", "source_type": "manual_text"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_cannot_create_rag_source_under_another_users_profile(client):
    owner_token = _register_and_login(client, "rag-owner-create@example.com")
    other_token = _register_and_login(client, "rag-other-create@example.com")
    profile_id = _create_profile(client, owner_token, "Owner RAG Profile")

    response = _create_rag_source(client, other_token, profile_id)

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_user_can_list_only_own_profile_sources(client):
    first_token = _register_and_login(client, "rag-list-first@example.com")
    second_token = _register_and_login(client, "rag-list-second@example.com")
    first_profile_id = _create_profile(client, first_token, "First RAG Profile")
    second_profile_id = _create_profile(client, second_token, "Second RAG Profile")
    assert _create_rag_source(client, first_token, first_profile_id, title="First Source").status_code == 201
    assert _create_rag_source(client, second_token, second_profile_id, title="Second Source").status_code == 201

    response = client.get(
        f"/api/memory-profiles/{first_profile_id}/rag-sources",
        headers=_auth_headers(first_token),
    )

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["title"] == "First Source"


def test_user_can_read_own_source(client):
    token = _register_and_login(client, "rag-read@example.com")
    profile_id = _create_profile(client, token, "Read RAG Profile")
    create_response = _create_rag_source(client, token, profile_id, title="Readable Source")
    source_id = create_response.json()["id"]

    response = client.get(f"/api/rag-sources/{source_id}", headers=_auth_headers(token))

    assert response.status_code == 200
    assert response.json()["title"] == "Readable Source"


def test_user_cannot_read_another_users_source(client):
    owner_token = _register_and_login(client, "rag-read-owner@example.com")
    other_token = _register_and_login(client, "rag-read-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Read RAG")
    create_response = _create_rag_source(client, owner_token, profile_id, title="Private Source")
    source_id = create_response.json()["id"]

    response = client.get(f"/api/rag-sources/{source_id}", headers=_auth_headers(other_token))

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_user_can_update_own_source(client):
    token = _register_and_login(client, "rag-update@example.com")
    profile_id = _create_profile(client, token, "Update RAG Profile")
    create_response = _create_rag_source(client, token, profile_id, title="Old Source")
    source_id = create_response.json()["id"]

    response = client.patch(
        f"/api/rag-sources/{source_id}",
        headers=_auth_headers(token),
        json={
            "title": "Updated Source",
            "source_type": "letter",
            "language": "cs",
            "source_metadata": {"tag": "updated"},
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Updated Source"
    assert body["source_type"] == "letter"
    assert body["language"] == "cs"
    assert body["source_metadata"] == {"tag": "updated"}


def test_updating_raw_text_resets_status_to_ready_for_cleaning(client):
    token = _register_and_login(client, "rag-status-reset@example.com")
    profile_id = _create_profile(client, token, "Status Reset Profile")
    create_response = _create_rag_source(client, token, profile_id)
    source_id = create_response.json()["id"]

    db, session_generator = _get_test_db_session()
    try:
        rag_source = db.get(RagSource, source_id)
        assert rag_source is not None
        rag_source.status = "embedded"
        rag_source.processing_error = "old failure"
        db.commit()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.patch(
        f"/api/rag-sources/{source_id}",
        headers=_auth_headers(token),
        json={"raw_text": "Updated raw source text"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["raw_text"] == "Updated raw source text"
    assert body["normalized_text"] == "Updated raw source text"
    assert body["status"] == "ready_for_cleaning"
    assert body["processing_error"] is None


def test_user_cannot_update_another_users_source(client):
    owner_token = _register_and_login(client, "rag-update-owner@example.com")
    other_token = _register_and_login(client, "rag-update-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Update RAG")
    create_response = _create_rag_source(client, owner_token, profile_id, title="Immutable Source")
    source_id = create_response.json()["id"]

    response = client.patch(
        f"/api/rag-sources/{source_id}",
        headers=_auth_headers(other_token),
        json={"title": "Blocked Update"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_user_can_delete_own_source(client):
    token = _register_and_login(client, "rag-delete@example.com")
    profile_id = _create_profile(client, token, "Delete RAG Profile")
    create_response = _create_rag_source(client, token, profile_id, title="Delete Source")
    source_id = create_response.json()["id"]

    delete_response = client.delete(f"/api/rag-sources/{source_id}", headers=_auth_headers(token))
    get_response = client.get(f"/api/rag-sources/{source_id}", headers=_auth_headers(token))

    assert delete_response.status_code == 204
    assert get_response.status_code == 404


def test_user_cannot_delete_another_users_source(client):
    owner_token = _register_and_login(client, "rag-delete-owner@example.com")
    other_token = _register_and_login(client, "rag-delete-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Delete RAG")
    create_response = _create_rag_source(client, owner_token, profile_id, title="Private Delete Source")
    source_id = create_response.json()["id"]

    response = client.delete(f"/api/rag-sources/{source_id}", headers=_auth_headers(other_token))

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_title_is_trimmed_and_cannot_be_empty(client):
    token = _register_and_login(client, "rag-title-validation@example.com")
    profile_id = _create_profile(client, token, "Title Validation Profile")

    trimmed_response = _create_rag_source(client, token, profile_id, title="  Trimmed Title  ")
    empty_response = _create_rag_source(client, token, profile_id, title="   ")

    assert trimmed_response.status_code == 201
    assert trimmed_response.json()["title"] == "Trimmed Title"
    assert empty_response.status_code == 422


def test_raw_text_is_trimmed_and_cannot_be_empty(client):
    token = _register_and_login(client, "rag-raw-validation@example.com")
    profile_id = _create_profile(client, token, "Raw Validation Profile")

    trimmed_response = _create_rag_source(client, token, profile_id, raw_text="  Trimmed raw text  ")
    empty_response = _create_rag_source(client, token, profile_id, raw_text="   ")

    assert trimmed_response.status_code == 201
    assert trimmed_response.json()["raw_text"] == "Trimmed raw text"
    assert empty_response.status_code == 422


def test_invalid_source_type_is_rejected(client):
    token = _register_and_login(client, "rag-invalid-type@example.com")
    profile_id = _create_profile(client, token, "Invalid Type Profile")

    response = _create_rag_source(client, token, profile_id, source_type="not_allowed")

    assert response.status_code == 422


def test_source_list_is_ordered_newest_first(client):
    token = _register_and_login(client, "rag-ordering@example.com")
    profile_id = _create_profile(client, token, "Ordering Profile")
    first_response = _create_rag_source(client, token, profile_id, title="Older Source")
    second_response = _create_rag_source(client, token, profile_id, title="Newer Source")

    assert first_response.status_code == 201
    assert second_response.status_code == 201

    response = client.get(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert [source["title"] for source in response.json()] == ["Newer Source", "Older Source"]


def test_no_external_api_calls_are_made_for_rag_source_crud(client, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for rag source ingestion foundation")

    monkeypatch.setattr(httpx, "request", fail_http_call)
    monkeypatch.setattr(httpx, "get", fail_http_call)
    monkeypatch.setattr(httpx, "post", fail_http_call)

    token = _register_and_login(client, "rag-no-http@example.com")
    profile_id = _create_profile(client, token, "No HTTP RAG Profile")

    create_response = _create_rag_source(client, token, profile_id, title="No HTTP Source")
    list_response = client.get(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
    )

    assert create_response.status_code == 201
    assert list_response.status_code == 200

from uuid import UUID

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.core.errors import install_error_handlers
from app.core.logging import REDACTED_VALUE, REQUEST_ID_HEADER, sanitize_log_data
from app.core.middleware import install_middleware


def test_request_without_request_id_returns_generated_header(client):
    response = client.get("/health")

    assert response.status_code == 200
    request_id = response.headers.get(REQUEST_ID_HEADER)
    assert request_id is not None
    UUID(request_id)


def test_request_with_safe_request_id_reuses_same_header(client):
    request_id = "safe-request-123"

    response = client.get(
        "/health",
        headers={REQUEST_ID_HEADER: request_id},
    )

    assert response.status_code == 200
    assert response.headers[REQUEST_ID_HEADER] == request_id


def test_unsafe_request_id_is_replaced(client):
    unsafe_request_id = "x" * 200

    response = client.get(
        "/health",
        headers={REQUEST_ID_HEADER: unsafe_request_id},
    )

    assert response.status_code == 200
    new_request_id = response.headers[REQUEST_ID_HEADER]
    assert new_request_id != unsafe_request_id
    UUID(new_request_id)


def test_runtime_health_still_works_with_request_id(client):
    response = client.get("/health/runtime")

    assert response.status_code == 200
    assert response.headers.get(REQUEST_ID_HEADER)
    assert {"status", "database", "redis"}.issubset(response.json().keys())


def test_global_error_handler_returns_safe_json_and_includes_request_id():
    app = FastAPI()
    install_error_handlers(app)
    install_middleware(app)

    @app.get("/boom")
    def boom():
        raise RuntimeError("sensitive internal failure")

    with TestClient(app, raise_server_exceptions=False) as test_client:
        response = test_client.get(
            "/boom",
            headers={REQUEST_ID_HEADER: "boom-123"},
        )

    assert response.status_code == 500
    assert response.headers[REQUEST_ID_HEADER] == "boom-123"
    assert response.json() == {
        "detail": "Internal server error",
        "request_id": "boom-123",
    }
    assert "sensitive internal failure" not in response.text


def test_log_sanitizer_masks_sensitive_values():
    sanitized = sanitize_log_data(
        {
            "password": "pass-1",
            "access_token": "token-1",
            "authorization": "Bearer abc",
            "secret": "secret-1",
            "api_key": "api-1",
            "nested": {
                "password": "pass-2",
                "safe": "value",
            },
            "list_data": [
                {"authorization": "Bearer nested"},
                {"safe": "ok"},
            ],
        }
    )

    assert sanitized["password"] == REDACTED_VALUE
    assert sanitized["access_token"] == REDACTED_VALUE
    assert sanitized["authorization"] == REDACTED_VALUE
    assert sanitized["secret"] == REDACTED_VALUE
    assert sanitized["api_key"] == REDACTED_VALUE
    assert sanitized["nested"]["password"] == REDACTED_VALUE
    assert sanitized["nested"]["safe"] == "value"
    assert sanitized["list_data"][0]["authorization"] == REDACTED_VALUE
    assert sanitized["list_data"][1]["safe"] == "ok"

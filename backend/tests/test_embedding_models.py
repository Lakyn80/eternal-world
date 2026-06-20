from pathlib import Path

import httpx
import pytest

from app.modules.embedding_models.service import (
    get_candidate_models_for_language,
    get_default_embedding_model,
    get_embedding_model,
    get_enabled_embedding_models,
    list_embedding_models,
    validate_embedding_model_code,
)


def test_list_endpoint_returns_enabled_models_by_default(client):
    response = client.get("/api/embedding-models")

    assert response.status_code == 200
    assert [model["code"] for model in response.json()] == [
        "multilingual_e5_small",
        "bge_m3",
        "mock_embedding",
    ]


def test_disabled_external_model_is_hidden_unless_include_disabled_true(client):
    enabled_response = client.get("/api/embedding-models")
    all_response = client.get("/api/embedding-models?include_disabled=true")

    assert enabled_response.status_code == 200
    assert all_response.status_code == 200
    assert "jina_embeddings_v3" not in [model["code"] for model in enabled_response.json()]
    assert "jina_embeddings_v3" in [model["code"] for model in all_response.json()]


def test_default_endpoint_returns_configured_default_model(client):
    response = client.get("/api/embedding-models/default")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "multilingual_e5_small"
    assert body["is_default"] is True


def test_get_by_code_returns_known_model(client):
    response = client.get("/api/embedding-models/bge_m3")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "bge_m3"
    assert body["provider_type"] == "local"
    assert body["dimension"] == 1024


def test_unknown_model_code_returns_404(client):
    response = client.get("/api/embedding-models/not_real")

    assert response.status_code == 404
    assert response.json()["detail"] == "Embedding model not found"


def test_model_codes_are_stable():
    assert [model.code for model in list_embedding_models(include_disabled=True)] == [
        "multilingual_e5_small",
        "bge_m3",
        "jina_embeddings_v3",
        "mock_embedding",
    ]


def test_exactly_one_default_model_exists():
    default_models = [model for model in list_embedding_models(include_disabled=True) if model.is_default]

    assert len(default_models) == 1
    assert default_models[0].code == "multilingual_e5_small"


def test_default_model_is_enabled():
    default_model = get_default_embedding_model()

    assert default_model.enabled is True


def test_candidate_selection_for_ru_includes_multilingual_capable_models():
    candidates = get_candidate_models_for_language("ru")

    assert [model.code for model in candidates] == [
        "multilingual_e5_small",
        "bge_m3",
    ]


def test_candidate_selection_for_cs_includes_multilingual_capable_models():
    candidates = get_candidate_models_for_language("cs")

    assert [model.code for model in candidates] == [
        "multilingual_e5_small",
        "bge_m3",
    ]


def test_candidate_selection_for_unknown_language_returns_multilingual_default_candidates():
    candidates = get_candidate_models_for_language("pl")

    assert [model.code for model in candidates] == [
        "multilingual_e5_small",
        "bge_m3",
    ]


def test_mock_embedding_model_is_available_for_tests():
    mock_model = get_embedding_model("mock_embedding")

    assert mock_model.code == "mock_embedding"
    assert mock_model.provider_type == "mock"
    assert mock_model.dimension == 8


def test_validate_embedding_model_code_returns_normalized_code():
    assert validate_embedding_model_code("  BGE_M3  ") == "bge_m3"


def test_enabled_models_helper_hides_disabled_external_models():
    assert [model.code for model in get_enabled_embedding_models()] == [
        "multilingual_e5_small",
        "bge_m3",
        "mock_embedding",
    ]


def test_no_external_api_calls_are_made(client, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for embedding model registry foundation")

    monkeypatch.setattr(httpx, "request", fail_http_call)
    monkeypatch.setattr(httpx, "get", fail_http_call)
    monkeypatch.setattr(httpx, "post", fail_http_call)

    list_response = client.get("/api/embedding-models")
    default_response = client.get("/api/embedding-models/default")
    detail_response = client.get("/api/embedding-models/multilingual_e5_small")

    assert list_response.status_code == 200
    assert default_response.status_code == 200
    assert detail_response.status_code == 200


def test_project_progress_is_updated_for_embedding_model_registry_foundation():
    project_progress_path = None
    for parent in Path(__file__).resolve().parents:
        candidate_path = parent / "PROJECT_PROGRESS.md"
        if candidate_path.exists():
            project_progress_path = candidate_path
            break

    if project_progress_path is None:
        pytest.skip("PROJECT_PROGRESS.md is not available in this test environment")

    content = project_progress_path.read_text(encoding="utf-8")

    assert "Embedding Model Registry Foundation" in content

from pathlib import Path

import httpx
import pytest

from app.modules.embedding_models.service import (
    allow_disabled_runtime_embedding_models,
    get_candidate_models_for_language,
    get_default_embedding_model,
    get_embedding_model,
    get_enabled_embedding_models,
    is_embedding_model_runtime_available,
    list_embedding_models,
    validate_embedding_model_code,
)


def test_list_endpoint_returns_enabled_models_by_default(client):
    response = client.get("/api/embedding-models")

    assert response.status_code == 200
    assert [model["code"] for model in response.json()] == [
        "multilingual_e5_small",
        "bge_m3",
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
        "multilingual_e5_large",
        "mock_embedding",
    ]


def test_disabled_manual_only_models_are_hidden_unless_include_disabled_true(client):
    enabled_response = client.get("/api/embedding-models")
    all_response = client.get("/api/embedding-models?include_disabled=true")

    assert enabled_response.status_code == 200
    assert all_response.status_code == 200
    assert "bge_m3_dense_sparse" not in [model["code"] for model in enabled_response.json()]
    assert "bge_m3_dense_sparse" in [model["code"] for model in all_response.json()]
    assert "bge_m3_dense_sparse_multivector" not in [model["code"] for model in enabled_response.json()]
    assert "bge_m3_dense_sparse_multivector" in [model["code"] for model in all_response.json()]
    assert "qwen3_embedding_0_6b" not in [model["code"] for model in enabled_response.json()]
    assert "qwen3_embedding_0_6b" in [model["code"] for model in all_response.json()]
    assert "qwen3_embedding_4b" not in [model["code"] for model in enabled_response.json()]
    assert "qwen3_embedding_4b" in [model["code"] for model in all_response.json()]
    assert "qwen3_embedding_8b" not in [model["code"] for model in enabled_response.json()]
    assert "qwen3_embedding_8b" in [model["code"] for model in all_response.json()]
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


def test_get_by_code_returns_new_mpnet_model(client):
    response = client.get("/api/embedding-models/paraphrase_multilingual_mpnet_base_v2")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "paraphrase_multilingual_mpnet_base_v2"
    assert body["provider_type"] == "local"
    assert body["dimension"] == 768


def test_get_by_code_returns_new_e5_base_model(client):
    response = client.get("/api/embedding-models/multilingual_e5_base")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "multilingual_e5_base"
    assert body["provider_type"] == "local"
    assert body["dimension"] == 768


def test_get_by_code_returns_new_e5_large_model(client):
    response = client.get("/api/embedding-models/multilingual_e5_large")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "multilingual_e5_large"
    assert body["provider_type"] == "local"
    assert body["dimension"] == 1024
    assert body["provider_model_name"] == "intfloat/multilingual-e5-large"
    assert body["runtime_adapter"] == "sentence_transformers"
    assert body["manual_only_real_eval"] is True
    assert body["high_resource"] is True


def test_get_by_code_returns_disabled_qwen3_registry_foundation(client):
    response = client.get("/api/embedding-models/qwen3_embedding_0_6b")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "qwen3_embedding_0_6b"
    assert body["enabled"] is False
    assert body["provider_model_name"] == "Qwen/Qwen3-Embedding-0.6B"
    assert body["runtime_adapter"] == "sentence_transformers"
    assert body["manual_only_real_eval"] is True
    assert body["real_benchmark_only"] is True
    assert body["ci_safe_real_inference"] is False
    assert "attempted but not completed" in body["notes"]
    assert "not verified in this environment" in body["notes"]


def test_get_by_code_returns_disabled_bge_m3_dense_sparse_registry_foundation(client):
    response = client.get("/api/embedding-models/bge_m3_dense_sparse")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "bge_m3_dense_sparse"
    assert body["enabled"] is False
    assert body["provider_model_name"] == "BAAI/bge-m3"
    assert body["runtime_adapter"] == "planned_manual_only"
    assert body["manual_only_real_eval"] is True
    assert body["real_benchmark_only"] is True
    assert body["supported_retrieval_modes"] == ["bge_m3_dense_sparse"]
    assert "Manual-only" in body["notes"]


def test_get_by_code_returns_disabled_bge_m3_dense_sparse_multivector_registry_foundation(client):
    response = client.get("/api/embedding-models/bge_m3_dense_sparse_multivector")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "bge_m3_dense_sparse_multivector"
    assert body["enabled"] is False
    assert body["provider_model_name"] == "BAAI/bge-m3"
    assert body["runtime_adapter"] == "planned_manual_only"
    assert body["manual_only_real_eval"] is True
    assert body["real_benchmark_only"] is True
    assert body["supported_retrieval_modes"] == ["bge_m3_dense_sparse_multivector"]
    assert "late-interaction multivector reranking" in body["notes"]


def test_get_by_code_returns_disabled_jina_registry_foundation(client):
    response = client.get("/api/embedding-models/jina_embeddings_v3")

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == "jina_embeddings_v3"
    assert body["enabled"] is False
    assert body["provider_type"] == "local"
    assert body["provider_model_name"] == "jinaai/jina-embeddings-v3"
    assert body["supports_task_adapters"] is True
    assert body["supports_long_context"] is True


def test_unknown_model_code_returns_404(client):
    response = client.get("/api/embedding-models/not_real")

    assert response.status_code == 404
    assert response.json()["detail"] == "Embedding model not found"


def test_model_codes_are_stable():
    assert [model.code for model in list_embedding_models(include_disabled=True)] == [
        "multilingual_e5_small",
        "bge_m3",
        "bge_m3_dense_sparse",
        "bge_m3_dense_sparse_multivector",
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
        "multilingual_e5_large",
        "qwen3_embedding_0_6b",
        "qwen3_embedding_4b",
        "qwen3_embedding_8b",
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
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
        "multilingual_e5_large",
    ]


def test_candidate_selection_for_cs_includes_multilingual_capable_models():
    candidates = get_candidate_models_for_language("cs")

    assert [model.code for model in candidates] == [
        "multilingual_e5_small",
        "bge_m3",
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
        "multilingual_e5_large",
    ]


def test_candidate_selection_for_unknown_language_returns_multilingual_default_candidates():
    candidates = get_candidate_models_for_language("pl")

    assert [model.code for model in candidates] == [
        "multilingual_e5_small",
        "bge_m3",
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
        "multilingual_e5_large",
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
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
        "multilingual_e5_large",
        "mock_embedding",
    ]


def test_disabled_qwen_runtime_is_blocked_by_default_and_allowed_only_inside_manual_context():
    assert is_embedding_model_runtime_available("multilingual_e5_base") is True
    assert is_embedding_model_runtime_available("bge_m3_dense_sparse") is False
    assert is_embedding_model_runtime_available("bge_m3_dense_sparse_multivector") is False
    assert is_embedding_model_runtime_available("qwen3_embedding_0_6b") is False

    with allow_disabled_runtime_embedding_models(
        ["bge_m3_dense_sparse", "bge_m3_dense_sparse_multivector"]
    ):
        assert is_embedding_model_runtime_available("bge_m3_dense_sparse") is True
        assert is_embedding_model_runtime_available("bge_m3_dense_sparse_multivector") is True

    with allow_disabled_runtime_embedding_models(["qwen3_embedding_0_6b"]):
        assert is_embedding_model_runtime_available("qwen3_embedding_0_6b") is True

    assert is_embedding_model_runtime_available("bge_m3_dense_sparse") is False
    assert is_embedding_model_runtime_available("bge_m3_dense_sparse_multivector") is False
    assert is_embedding_model_runtime_available("qwen3_embedding_0_6b") is False


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

import httpx
import socket
from pathlib import Path
from types import SimpleNamespace

from app.core.config import settings
from app.db.models import RagChunk, RagEmbedding
from app.db.session import get_db
from app.main import app
from app.modules.embeddings.providers.mock import MockEmbeddingProvider


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Embedding User",
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


def _build_long_source(sentence_count: int = 24) -> str:
    return " ".join(
        f"This is source sentence number {index} with stable wording for deterministic embedding tests."
        for index in range(sentence_count)
    )


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Embedding Source",
        "raw_text": _build_long_source(),
        "source_type": "manual_text",
        "language": "en",
    }
    payload.update(overrides)
    return client.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
        json=payload,
    )


def _chunk_source(client, token: str, source_id: int):
    return client.post(
        f"/api/rag-sources/{source_id}/chunk",
        headers=_auth_headers(token),
    )


def _list_chunks(client, token: str, source_id: int):
    return client.get(
        f"/api/rag-sources/{source_id}/chunks",
        headers=_auth_headers(token),
    )


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def _install_fake_sentence_transformers(monkeypatch):
    class FakeSentenceTransformer:
        def __init__(self, model_name: str, *, device: str = "cpu", cache_folder: str | None = None):
            self.model_name = model_name
            self.device = device
            self.cache_folder = cache_folder

        def encode(self, texts, **kwargs):
            materialized_texts = list(texts)
            if self.model_name == "intfloat/multilingual-e5-small":
                dimension = 384
            elif self.model_name == "intfloat/multilingual-e5-large":
                dimension = 1024
            elif self.model_name in {
                "intfloat/multilingual-e5-base",
                "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
            }:
                dimension = 768
            else:
                dimension = 1024
            return [
                [round((index + 1) / 1000, 6) for index in range(dimension)]
                for _ in materialized_texts
            ]

    monkeypatch.setattr(settings, "embedding_provider", "sentence_transformers")
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        lambda module_name: SimpleNamespace(SentenceTransformer=FakeSentenceTransformer),
    )


def test_authenticated_user_can_embed_own_chunk_with_default_model(client):
    token = _register_and_login(client, "embed-own@example.com")
    profile_id = _create_profile(client, token, "Embedding Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["chunk_id"] == chunk_id
    assert body["model_code"] == "multilingual_e5_small"
    assert body["vector_dimension"] == 384
    assert body["status"] == "embedded"
    assert body["vector"] is None


def test_chunk_embedding_can_use_sentence_transformers_multilingual_e5_small_without_downloads(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "embed-real-local@example.com")
    profile_id = _create_profile(client, token, "Embedding Real Local Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )
    embedding_id = response.json()["id"]
    metadata_response = client.get(
        f"/api/rag-embeddings/{embedding_id}?include_vector=true",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert metadata_response.status_code == 200
    assert metadata_response.json()["vector_dimension"] == 384
    assert metadata_response.json()["embedding_metadata"]["provider_name"] == "sentence_transformers"


def test_chunk_embedding_can_use_sentence_transformers_bge_m3_without_downloads(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "embed-bge-real-local@example.com")
    profile_id = _create_profile(client, token, "Embedding BGE Real Local Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "bge_m3"},
    )
    embedding_id = response.json()["id"]
    metadata_response = client.get(
        f"/api/rag-embeddings/{embedding_id}?include_vector=true",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert metadata_response.status_code == 200
    assert metadata_response.json()["model_code"] == "bge_m3"
    assert metadata_response.json()["vector_dimension"] == 1024
    assert metadata_response.json()["embedding_metadata"]["provider_name"] == "sentence_transformers"


def test_chunk_embedding_can_use_sentence_transformers_mpnet_without_downloads(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "embed-mpnet-real-local@example.com")
    profile_id = _create_profile(client, token, "Embedding MPNet Real Local Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "paraphrase_multilingual_mpnet_base_v2"},
    )
    embedding_id = response.json()["id"]
    metadata_response = client.get(
        f"/api/rag-embeddings/{embedding_id}?include_vector=true",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert metadata_response.status_code == 200
    assert metadata_response.json()["model_code"] == "paraphrase_multilingual_mpnet_base_v2"
    assert metadata_response.json()["vector_dimension"] == 768
    assert metadata_response.json()["embedding_metadata"]["provider_name"] == "sentence_transformers"
    assert (
        metadata_response.json()["embedding_metadata"]["provider_model_name"]
        == "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    )


def test_chunk_embedding_can_use_sentence_transformers_e5_base_without_downloads(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "embed-e5-base-real-local@example.com")
    profile_id = _create_profile(client, token, "Embedding E5 Base Real Local Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "multilingual_e5_base"},
    )
    embedding_id = response.json()["id"]
    metadata_response = client.get(
        f"/api/rag-embeddings/{embedding_id}?include_vector=true",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert metadata_response.status_code == 200
    assert metadata_response.json()["model_code"] == "multilingual_e5_base"
    assert metadata_response.json()["vector_dimension"] == 768
    assert metadata_response.json()["embedding_metadata"]["provider_name"] == "sentence_transformers"
    assert metadata_response.json()["embedding_metadata"]["provider_model_name"] == "intfloat/multilingual-e5-base"
    assert metadata_response.json()["embedding_metadata"]["input_prefix"] == "passage:"


def test_chunk_embedding_can_use_sentence_transformers_e5_large_without_downloads(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "embed-e5-large-real-local@example.com")
    profile_id = _create_profile(client, token, "Embedding E5 Large Real Local Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "multilingual_e5_large"},
    )
    embedding_id = response.json()["id"]
    metadata_response = client.get(
        f"/api/rag-embeddings/{embedding_id}?include_vector=true",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert metadata_response.status_code == 200
    assert metadata_response.json()["model_code"] == "multilingual_e5_large"
    assert metadata_response.json()["vector_dimension"] == 1024
    assert metadata_response.json()["embedding_metadata"]["provider_name"] == "sentence_transformers"
    assert metadata_response.json()["embedding_metadata"]["provider_model_name"] == "intfloat/multilingual-e5-large"
    assert metadata_response.json()["embedding_metadata"]["input_prefix"] == "passage:"


def test_unauthenticated_user_cannot_embed_chunk(client):
    token = _register_and_login(client, "embed-unauth-owner@example.com")
    profile_id = _create_profile(client, token, "Embed Unauth Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    client.cookies.clear()
    response = client.post(f"/api/rag-chunks/{chunk_id}/embed")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_cannot_embed_another_users_chunk(client):
    owner_token = _register_and_login(client, "embed-owner@example.com")
    other_token = _register_and_login(client, "embed-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Embed Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]
    assert _chunk_source(client, owner_token, source_id).status_code == 200
    chunk_id = _list_chunks(client, owner_token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG chunk not found"


def test_unknown_model_code_is_rejected_safely(client):
    token = _register_and_login(client, "embed-unknown-model@example.com")
    profile_id = _create_profile(client, token, "Unknown Model Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "not_real"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Embedding model not found"


def test_disabled_external_model_is_rejected(client):
    token = _register_and_login(client, "embed-disabled-model@example.com")
    profile_id = _create_profile(client, token, "Disabled Model Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "jina_embeddings_v3"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Embedding model not available"


def test_embedding_vector_dimension_matches_model_registry_dimension(client):
    token = _register_and_login(client, "embed-dimension@example.com")
    profile_id = _create_profile(client, token, "Dimension Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    create_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )
    embedding_id = create_response.json()["id"]
    get_response = client.get(
        f"/api/rag-embeddings/{embedding_id}?include_vector=true",
        headers=_auth_headers(token),
    )

    assert create_response.status_code == 200
    assert get_response.status_code == 200
    body = get_response.json()
    assert body["vector_dimension"] == 384
    assert len(body["vector"]) == 384


def test_mock_provider_is_deterministic_and_requires_no_downloads(monkeypatch):
    def fail_network(*args, **kwargs):
        raise AssertionError("Mock embedding provider should not require network access or downloads")

    monkeypatch.setattr(socket, "create_connection", fail_network)

    provider = MockEmbeddingProvider()
    first = provider.embed_text("same text", "mock_embedding")
    second = provider.embed_text("same text", "mock_embedding")

    assert first.dimension == 8
    assert second.dimension == 8
    assert first.values == second.values


def test_repeated_embed_for_same_chunk_and_model_upserts_without_duplicates(client):
    token = _register_and_login(client, "embed-upsert@example.com")
    profile_id = _create_profile(client, token, "Upsert Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    first_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )
    second_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )
    list_response = client.get(
        f"/api/rag-chunks/{chunk_id}/embeddings",
        headers=_auth_headers(token),
    )

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.json()["id"] == second_response.json()["id"]
    assert len(list_response.json()) == 1


def test_source_level_embed_embeds_all_valid_chunks(client):
    token = _register_and_login(client, "embed-source-all@example.com")
    profile_id = _create_profile(client, token, "Source Embed Profile")
    source_id = _create_rag_source(client, token, profile_id, raw_text=_build_long_source(40)).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_count = len(_list_chunks(client, token, source_id).json())

    response = client.post(
        f"/api/rag-sources/{source_id}/embed-chunks",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["source_id"] == source_id
    assert body["model_code"] == "multilingual_e5_small"
    assert body["total_chunks"] == chunk_count
    assert body["embedded_count"] == chunk_count
    assert body["skipped_count"] == 0
    assert body["failed_count"] == 0


def test_source_level_embed_skips_invalid_chunks(client):
    token = _register_and_login(client, "embed-source-skip@example.com")
    profile_id = _create_profile(client, token, "Source Skip Profile")
    source_id = _create_rag_source(client, token, profile_id, raw_text=_build_long_source(40)).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunks = _list_chunks(client, token, source_id).json()

    db, session_generator = _get_test_db_session()
    try:
        rag_chunk = db.get(RagChunk, chunks[0]["id"])
        assert rag_chunk is not None
        rag_chunk.validation_status = "invalid"
        db.commit()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.post(
        f"/api/rag-sources/{source_id}/embed-chunks",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["total_chunks"] == len(chunks)
    assert body["embedded_count"] == len(chunks) - 1
    assert body["skipped_count"] == 1
    assert body["failed_count"] == 0


def test_user_cannot_embed_chunks_for_another_users_source(client):
    owner_token = _register_and_login(client, "embed-source-owner@example.com")
    other_token = _register_and_login(client, "embed-source-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Source Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]
    assert _chunk_source(client, owner_token, source_id).status_code == 200

    response = client.post(
        f"/api/rag-sources/{source_id}/embed-chunks",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_user_can_list_embeddings_for_own_chunk(client):
    token = _register_and_login(client, "embed-list-own@example.com")
    profile_id = _create_profile(client, token, "List Own Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    assert client.post(f"/api/rag-chunks/{chunk_id}/embed", headers=_auth_headers(token)).status_code == 200

    response = client.get(
        f"/api/rag-chunks/{chunk_id}/embeddings",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["chunk_id"] == chunk_id


def test_user_cannot_list_embeddings_for_another_users_chunk(client):
    owner_token = _register_and_login(client, "embed-list-owner@example.com")
    other_token = _register_and_login(client, "embed-list-other@example.com")
    profile_id = _create_profile(client, owner_token, "List Owner Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]
    assert _chunk_source(client, owner_token, source_id).status_code == 200
    chunk_id = _list_chunks(client, owner_token, source_id).json()[0]["id"]
    assert client.post(f"/api/rag-chunks/{chunk_id}/embed", headers=_auth_headers(owner_token)).status_code == 200

    response = client.get(
        f"/api/rag-chunks/{chunk_id}/embeddings",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG chunk not found"


def test_user_can_read_own_embedding_metadata(client):
    token = _register_and_login(client, "embed-read-own@example.com")
    profile_id = _create_profile(client, token, "Read Own Embedding Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    create_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )
    embedding_id = create_response.json()["id"]

    response = client.get(
        f"/api/rag-embeddings/{embedding_id}",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == embedding_id
    assert body["vector"] is None


def test_user_cannot_read_another_users_embedding(client):
    owner_token = _register_and_login(client, "embed-read-owner@example.com")
    other_token = _register_and_login(client, "embed-read-other@example.com")
    profile_id = _create_profile(client, owner_token, "Read Owner Embedding Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]
    assert _chunk_source(client, owner_token, source_id).status_code == 200
    chunk_id = _list_chunks(client, owner_token, source_id).json()[0]["id"]
    create_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(owner_token),
    )
    embedding_id = create_response.json()["id"]

    response = client.get(
        f"/api/rag-embeddings/{embedding_id}",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG embedding not found"


def test_include_vector_behavior_is_optional(client):
    token = _register_and_login(client, "embed-include-vector@example.com")
    profile_id = _create_profile(client, token, "Include Vector Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    create_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "mock_embedding"},
    )
    embedding_id = create_response.json()["id"]

    default_response = client.get(
        f"/api/rag-embeddings/{embedding_id}",
        headers=_auth_headers(token),
    )
    vector_response = client.get(
        f"/api/rag-embeddings/{embedding_id}?include_vector=true",
        headers=_auth_headers(token),
    )

    assert default_response.status_code == 200
    assert vector_response.status_code == 200
    assert default_response.json()["vector"] is None
    assert len(vector_response.json()["vector"]) == 8


def test_no_external_api_calls_are_made(client, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for embedding generation foundation")

    monkeypatch.setattr(httpx, "request", fail_http_call)
    monkeypatch.setattr(httpx, "get", fail_http_call)
    monkeypatch.setattr(httpx, "post", fail_http_call)

    token = _register_and_login(client, "embed-no-http@example.com")
    profile_id = _create_profile(client, token, "No HTTP Embedding Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    create_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )
    list_response = client.get(
        f"/api/rag-chunks/{chunk_id}/embeddings",
        headers=_auth_headers(token),
    )

    assert create_response.status_code == 200
    assert list_response.status_code == 200


def test_project_progress_is_updated_for_embedding_generation_foundation():
    project_progress_path = None
    for parent in Path(__file__).resolve().parents:
        candidate_path = parent / "PROJECT_PROGRESS.md"
        if candidate_path.exists():
            project_progress_path = candidate_path
            break

    if project_progress_path is None:
        return

    content = project_progress_path.read_text(encoding="utf-8")

    assert "Embedding Generation Foundation" in content


def test_failed_embedding_status_can_be_persisted_safely(client, monkeypatch):
    token = _register_and_login(client, "embed-failure@example.com")
    profile_id = _create_profile(client, token, "Embedding Failure Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    def fail_embed_text(*args, **kwargs):
        raise RuntimeError("provider exploded")

    monkeypatch.setattr("app.modules.embeddings.providers.mock.MockEmbeddingProvider.embed_text", fail_embed_text)

    response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Embedding generation failed"

    db, session_generator = _get_test_db_session()
    try:
        rag_embeddings = db.query(RagEmbedding).filter(RagEmbedding.chunk_id == chunk_id).all()
        assert len(rag_embeddings) == 1
        assert rag_embeddings[0].status == "failed"
        assert rag_embeddings[0].error_message == "Embedding generation failed"
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

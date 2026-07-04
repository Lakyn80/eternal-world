from pathlib import Path
from types import SimpleNamespace
from uuid import NAMESPACE_URL, uuid5

from app.core.config import settings
from app.db.models import RagEmbedding, RagVectorIndex
from app.db.session import get_db
from app.main import app
from app.modules.qdrant_indexing.exceptions import QdrantCollectionConfigurationError


class FakeQdrantClient:
    def __init__(self) -> None:
        self.collections: dict[str, int] = {}
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.ensure_calls: list[tuple[str, int]] = []
        self.upsert_calls: list[tuple[str, str, list[float], dict[str, object]]] = []

    def ensure_collection(self, *, collection_name: str, vector_size: int) -> None:
        self.ensure_calls.append((collection_name, vector_size))
        existing_vector_size = self.collections.get(collection_name)
        if existing_vector_size is None:
            self.collections[collection_name] = vector_size
            return

        if existing_vector_size != vector_size:
            raise QdrantCollectionConfigurationError("Qdrant collection is incompatible with embedding dimension")

    def upsert_point(
        self,
        *,
        collection_name: str,
        point_id: str,
        vector: list[float],
        payload: dict[str, object],
    ) -> None:
        self.upsert_calls.append((collection_name, point_id, vector, payload))
        self.points[(collection_name, point_id)] = {
            "vector": list(vector),
            "payload": payload,
        }


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Qdrant User",
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
        f"This is source sentence number {index} with stable wording for deterministic qdrant indexing tests."
        for index in range(sentence_count)
    )


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Qdrant Source",
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


def _embed_source(client, token: str, source_id: int):
    return client.post(
        f"/api/rag-sources/{source_id}/embed-chunks",
        headers=_auth_headers(token),
    )


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def _install_fake_qdrant_client(monkeypatch) -> FakeQdrantClient:
    fake_qdrant_client = FakeQdrantClient()
    monkeypatch.setattr(
        "app.modules.qdrant_indexing.service.build_qdrant_client",
        lambda: fake_qdrant_client,
    )
    return fake_qdrant_client


def _install_fake_sentence_transformers(monkeypatch):
    class FakeSentenceTransformer:
        def __init__(self, model_name: str, *, device: str = "cpu", cache_folder: str | None = None):
            self.model_name = model_name
            self.device = device
            self.cache_folder = cache_folder

        def encode(self, texts, **kwargs):
            materialized_texts = list(texts)
            dimension = 384 if self.model_name == "intfloat/multilingual-e5-small" else 1024
            return [
                [round((index + 1) / 1000, 6) for index in range(dimension)]
                for _ in materialized_texts
            ]

    monkeypatch.setattr(settings, "embedding_provider", "sentence_transformers")
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        lambda module_name: SimpleNamespace(SentenceTransformer=FakeSentenceTransformer),
    )


def _create_embedded_chunk_and_embedding(client, token: str, profile_name: str, email_label: str) -> tuple[int, int, int]:
    profile_id = _create_profile(client, token, profile_name)
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    embed_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
    )
    assert embed_response.status_code == 200, email_label
    embedding_id = embed_response.json()["id"]
    return source_id, chunk_id, embedding_id


def test_authenticated_user_can_index_own_embedding(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-index-own@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Own Profile",
        "own",
    )

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["embedding_id"] == embedding_id
    assert body["status"] == "indexed"
    assert body["qdrant_collection"] == "eternal_world_rag_chunks__multilingual_e5_small"
    assert body["qdrant_point_id"]
    assert len(fake_qdrant_client.points) == 1


def test_unauthenticated_user_cannot_index_embedding(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-index-unauth-owner@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Unauth Profile",
        "unauth",
    )

    response = client.post(f"/api/rag-embeddings/{embedding_id}/index")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_cannot_index_another_users_embedding(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    owner_token = _register_and_login(client, "qdrant-owner@example.com")
    other_token = _register_and_login(client, "qdrant-other@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        owner_token,
        "Qdrant Owner Profile",
        "cross-user",
    )

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG embedding not found"


def test_index_endpoint_creates_deterministic_point_id(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-deterministic@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Deterministic Profile",
        "deterministic",
    )

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    collection_name = "eternal_world_rag_chunks__multilingual_e5_small"
    expected_point_id = str(uuid5(NAMESPACE_URL, f"{collection_name}:{embedding_id}"))
    assert response.json()["qdrant_point_id"] == expected_point_id


def test_repeated_indexing_upserts_same_index_row_without_duplicates(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-repeat@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Repeat Profile",
        "repeat",
    )

    first_response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )
    second_response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    db, session_generator = _get_test_db_session()
    try:
        rag_vector_indexes = db.query(RagVectorIndex).filter(RagVectorIndex.embedding_id == embedding_id).all()
        assert len(rag_vector_indexes) == 1
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.json()["id"] == second_response.json()["id"]
    assert len(fake_qdrant_client.points) == 1


def test_source_level_indexing_indexes_all_embedded_records_for_owned_source(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-source-index@example.com")
    profile_id = _create_profile(client, token, "Qdrant Source Index Profile")
    source_id = _create_rag_source(client, token, profile_id, raw_text=_build_long_source(40)).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_count = len(_list_chunks(client, token, source_id).json())
    assert _embed_source(client, token, source_id).status_code == 200

    response = client.post(
        f"/api/rag-sources/{source_id}/index-embeddings",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["source_id"] == source_id
    assert body["total_embeddings"] == chunk_count
    assert body["indexed_count"] == chunk_count
    assert body["skipped_count"] == 0
    assert body["failed_count"] == 0
    assert len(fake_qdrant_client.points) == chunk_count


def test_source_level_indexing_skips_failed_embeddings(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-source-skip@example.com")
    profile_id = _create_profile(client, token, "Qdrant Source Skip Profile")
    source_id = _create_rag_source(client, token, profile_id, raw_text=_build_long_source(40)).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    assert _embed_source(client, token, source_id).status_code == 200

    db, session_generator = _get_test_db_session()
    try:
        rag_embedding = db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).first()
        assert rag_embedding is not None
        rag_embedding.status = "failed"
        rag_embedding.vector = None
        db.commit()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    total_embeddings = len(client.get(f"/api/rag-sources/{source_id}/chunks", headers=_auth_headers(token)).json())
    response = client.post(
        f"/api/rag-sources/{source_id}/index-embeddings",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["total_embeddings"] == total_embeddings
    assert body["indexed_count"] == total_embeddings - 1
    assert body["skipped_count"] == 1
    assert body["failed_count"] == 0


def test_user_cannot_index_another_users_source_embeddings(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    owner_token = _register_and_login(client, "qdrant-source-owner@example.com")
    other_token = _register_and_login(client, "qdrant-source-other@example.com")
    profile_id = _create_profile(client, owner_token, "Qdrant Source Owner Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]

    response = client.post(
        f"/api/rag-sources/{source_id}/index-embeddings",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_index_metadata_can_be_read_for_own_embedding(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-read-own@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Read Own Profile",
        "read-own",
    )
    assert client.post(f"/api/rag-embeddings/{embedding_id}/index", headers=_auth_headers(token)).status_code == 200

    response = client.get(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert response.json()["embedding_id"] == embedding_id


def test_user_cannot_read_another_users_index_metadata(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    owner_token = _register_and_login(client, "qdrant-read-owner@example.com")
    other_token = _register_and_login(client, "qdrant-read-other@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        owner_token,
        "Qdrant Read Owner Profile",
        "read-other",
    )
    assert client.post(f"/api/rag-embeddings/{embedding_id}/index", headers=_auth_headers(owner_token)).status_code == 200

    response = client.get(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG embedding not found"


def test_qdrant_payload_includes_required_metadata_and_excludes_absolute_paths(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-payload@example.com")
    _, chunk_id, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Payload Profile",
        "payload",
    )

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    payload = next(iter(fake_qdrant_client.points.values()))["payload"]
    assert payload["owner_user_id"] == response.json()["owner_user_id"]
    assert payload["profile_id"] == response.json()["profile_id"]
    assert payload["source_id"] == response.json()["source_id"]
    assert payload["chunk_id"] == chunk_id
    assert payload["embedding_id"] == embedding_id
    assert payload["model_code"] == "multilingual_e5_small"
    assert payload["text_hash"]
    assert payload["language"] == "en"
    assert payload["validation_status"] in {"valid", "warning", "invalid"}
    assert payload["source_type"] == "manual_text"
    assert isinstance(payload["chunk_index"], int)
    assert "C:\\" not in str(payload)
    assert "/app/" not in str(payload)
    assert "raw_text" not in payload
    assert "storage_key" not in payload


def test_collection_creation_is_requested_when_missing(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-create-collection@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Create Collection Profile",
        "create-collection",
    )

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert fake_qdrant_client.collections["eternal_world_rag_chunks__multilingual_e5_small"] == 384


def test_qdrant_indexing_accepts_sentence_transformers_multilingual_e5_small_embeddings(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "qdrant-real-local@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Real Local Profile",
        "real-local",
    )

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert fake_qdrant_client.collections["eternal_world_rag_chunks__multilingual_e5_small"] == 384


def test_qdrant_indexing_accepts_sentence_transformers_bge_m3_embeddings(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "qdrant-bge-real-local@example.com")
    profile_id = _create_profile(client, token, "Qdrant BGE Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    embed_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "bge_m3"},
    )
    assert embed_response.status_code == 200
    embedding_id = embed_response.json()["id"]

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert fake_qdrant_client.collections["eternal_world_rag_chunks__bge_m3"] == 1024


def test_qdrant_indexing_stores_sparse_vector_payload_for_bge_m3_dense_sparse(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-hybrid-sparse@example.com")
    profile_id = _create_profile(client, token, "Hybrid Sparse Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    embed_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "bge_m3_dense_sparse"},
    )
    assert embed_response.status_code == 200
    embedding_id = embed_response.json()["id"]

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    payload = next(iter(fake_qdrant_client.points.values()))["payload"]
    assert payload["model_code"] == "bge_m3_dense_sparse"
    assert isinstance(payload["sparse_vector"], dict)
    assert payload["sparse_vector"]


def test_collection_dimension_mismatch_returns_safe_error(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    fake_qdrant_client.collections["eternal_world_rag_chunks__multilingual_e5_small"] = 8
    token = _register_and_login(client, "qdrant-dimension-mismatch@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant Dimension Mismatch Profile",
        "dimension-mismatch",
    )

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Qdrant collection is incompatible with embedding dimension"


def test_indexing_existing_embedding_does_not_trigger_embedding_generation(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "qdrant-no-embed-generation@example.com")
    _, _, embedding_id = _create_embedded_chunk_and_embedding(
        client,
        token,
        "Qdrant No Generation Profile",
        "no-generation",
    )

    def fail_embed_text(*args, **kwargs):
        raise AssertionError("Qdrant indexing should not trigger embedding generation")

    monkeypatch.setattr("app.modules.embeddings.providers.mock.MockEmbeddingProvider.embed_text", fail_embed_text)

    response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200


def test_project_progress_is_updated_for_qdrant_indexing_foundation():
    project_progress_path = None
    for parent in Path(__file__).resolve().parents:
        candidate_path = parent / "PROJECT_PROGRESS.md"
        if candidate_path.exists():
            project_progress_path = candidate_path
            break

    if project_progress_path is None:
        return

    content = project_progress_path.read_text(encoding="utf-8")

    assert "Qdrant Indexing Foundation" in content

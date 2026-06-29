from pathlib import Path
from types import SimpleNamespace

from app.core.config import settings
from app.db.models import MemoryProfile, RagEmbedding
from app.db.session import get_db
from app.main import app


class FakeQdrantRetrievalClient:
    def __init__(self) -> None:
        self.collections: dict[str, int] = {}
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.search_calls: list[dict[str, object]] = []

    def ensure_collection(self, *, collection_name: str, vector_size: int) -> None:
        existing_vector_size = self.collections.get(collection_name)
        if existing_vector_size is None:
            self.collections[collection_name] = vector_size
            return

        if existing_vector_size != vector_size:
            raise ValueError("dimension mismatch")

    def upsert_point(
        self,
        *,
        collection_name: str,
        point_id: str,
        vector: list[float],
        payload: dict[str, object],
    ) -> None:
        self.points[(collection_name, point_id)] = {
            "vector": list(vector),
            "payload": dict(payload),
        }

    def search_points(
        self,
        *,
        collection_name: str,
        vector: list[float],
        limit: int,
        search_filter: dict[str, object] | None = None,
        score_threshold: float | None = None,
    ) -> list[dict[str, object]]:
        self.search_calls.append(
            {
                "collection_name": collection_name,
                "vector": list(vector),
                "limit": limit,
                "search_filter": search_filter,
                "score_threshold": score_threshold,
            }
        )
        if collection_name not in self.collections:
            return []

        matching_results: list[dict[str, object]] = []
        for (stored_collection_name, point_id), point_data in self.points.items():
            if stored_collection_name != collection_name:
                continue

            payload = point_data["payload"]
            if not isinstance(payload, dict):
                continue

            if not _payload_matches_filter(payload, search_filter):
                continue

            stored_vector = point_data["vector"]
            if not isinstance(stored_vector, list):
                continue

            score = _dot_product(vector, stored_vector)
            if score_threshold is not None and score < score_threshold:
                continue

            matching_results.append(
                {
                    "id": point_id,
                    "score": score,
                    "payload": payload,
                }
            )

        matching_results.sort(key=lambda item: float(item["score"]), reverse=True)
        return matching_results[:limit]


def _dot_product(left: list[float], right: list[float]) -> float:
    return round(sum(left_value * right_value for left_value, right_value in zip(left, right)), 6)


def _payload_matches_filter(payload: dict[str, object], search_filter: dict[str, object] | None) -> bool:
    if search_filter is None:
        return True

    must_filters = search_filter.get("must")
    if not isinstance(must_filters, list):
        return True

    for item in must_filters:
        if not isinstance(item, dict):
            continue

        key = item.get("key")
        match = item.get("match")
        if not isinstance(key, str) or not isinstance(match, dict):
            continue

        if payload.get(key) != match.get("value"):
            return False

    return True


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Retrieval User",
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


def _create_profile_directly(*, user_id: int, name: str) -> int:
    db, session_generator = _get_test_db_session()
    try:
        memory_profile = MemoryProfile(
            user_id=user_id,
            name=name,
        )
        db.add(memory_profile)
        db.commit()
        db.refresh(memory_profile)
        return memory_profile.id
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass


def _build_long_source(sentence_count: int = 24) -> str:
    return " ".join(
        f"This is retrieval source sentence number {index} with stable wording for deterministic search tests."
        for index in range(sentence_count)
    )


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Retrieval Source",
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


def _embed_chunk(client, token: str, chunk_id: int, *, model_code: str | None = None):
    payload = {"model_code": model_code} if model_code is not None else None
    return client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json=payload,
    )


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def _install_fake_qdrant_client(monkeypatch) -> FakeQdrantRetrievalClient:
    fake_qdrant_client = FakeQdrantRetrievalClient()
    monkeypatch.setattr(
        "app.modules.qdrant_indexing.service.build_qdrant_client",
        lambda: fake_qdrant_client,
    )
    monkeypatch.setattr(
        "app.modules.rag_retrieval.service.build_qdrant_client",
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
            if self.model_name == "intfloat/multilingual-e5-small":
                dimension = 384
            elif self.model_name == "intfloat/multilingual-e5-base":
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


def _create_indexed_embedding(
    client,
    token: str,
    profile_name: str,
    *,
    profile_id: int | None = None,
    source_text: str | None = None,
    source_type: str = "manual_text",
    model_code: str = "multilingual_e5_base",
) -> tuple[int, int, int, int]:
    if profile_id is None:
        profile_id = _create_profile(client, token, profile_name)
    source_payload = {}
    if source_text is not None:
        source_payload["raw_text"] = source_text
    if source_type != "manual_text":
        source_payload["source_type"] = source_type

    source_id = _create_rag_source(client, token, profile_id, **source_payload).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    embed_response = _embed_chunk(client, token, chunk_id, model_code=model_code)
    assert embed_response.status_code == 200
    embedding_id = embed_response.json()["id"]
    index_response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )
    assert index_response.status_code == 200
    return profile_id, source_id, chunk_id, embedding_id


def test_retrieval_endpoint_requires_authentication(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-auth@example.com")
    profile_id, _, _, _ = _create_indexed_embedding(client, token, "Retrieval Auth Profile")

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        json={"query": "stable retrieval query"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_retrieval_is_scoped_to_owner_user_id_and_profile_id(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-scope@example.com")
    profile_id, source_id, chunk_id, embedding_id = _create_indexed_embedding(
        client,
        token,
        "Retrieval Scope Profile One",
        source_text="alpha profile retrieval text. " * 20,
    )
    other_profile_id = _create_profile_directly(user_id=1, name="Retrieval Scope Profile Two")
    other_profile_id, _, _, other_embedding_id = _create_indexed_embedding(
        client,
        token,
        "Retrieval Scope Profile Two",
        profile_id=other_profile_id,
        source_text="beta profile retrieval text. " * 20,
    )

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "alpha profile retrieval text", "limit": 5},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["profile_id"] == profile_id
    assert len(body["results"]) >= 1
    assert body["results"][0]["chunk_id"] == chunk_id
    assert body["results"][0]["source_id"] == source_id
    assert body["results"][0]["embedding_id"] == embedding_id
    assert all(result["embedding_id"] != other_embedding_id for result in body["results"])
    assert other_profile_id != profile_id


def test_cross_user_profile_access_returns_404(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    owner_token = _register_and_login(client, "retrieval-owner@example.com")
    other_token = _register_and_login(client, "retrieval-other@example.com")
    profile_id, _, _, _ = _create_indexed_embedding(client, owner_token, "Retrieval Owner Profile")

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(other_token),
        json={"query": "owner only retrieval query"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_query_embedding_is_generated_but_not_persisted_as_rag_embedding(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-query-embedding@example.com")
    profile_id, _, _, _ = _create_indexed_embedding(client, token, "Retrieval Query Embedding Profile")
    embed_call_count = 0

    original_embed_text = __import__(
        "app.modules.embeddings.providers.mock",
        fromlist=["MockEmbeddingProvider"],
    ).MockEmbeddingProvider.embed_text

    def counting_embed_text(self, text: str, model_code: str):
        nonlocal embed_call_count
        embed_call_count += 1
        return original_embed_text(self, text, model_code)

    monkeypatch.setattr(
        "app.modules.embeddings.providers.mock.MockEmbeddingProvider.embed_text",
        counting_embed_text,
    )

    db, session_generator = _get_test_db_session()
    try:
        before_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "deterministic query embedding test"},
    )

    db, session_generator = _get_test_db_session()
    try:
        after_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert response.status_code == 200
    assert embed_call_count == 1
    assert before_count == after_count


def test_query_embedding_can_use_sentence_transformers_without_persisting_query_embeddings(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "retrieval-real-local-query@example.com")
    profile_id, _, _, _ = _create_indexed_embedding(
        client,
        token,
        "Retrieval Real Local Query Profile",
        source_text="prague sentence for sentence-transformers retrieval. " * 18,
    )

    db, session_generator = _get_test_db_session()
    try:
        before_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "prague retrieval query"},
    )

    db, session_generator = _get_test_db_session()
    try:
        after_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert response.status_code == 200
    assert response.json()["model_code"] == "multilingual_e5_base"
    assert before_count == after_count


def test_bge_m3_query_embedding_can_use_sentence_transformers_without_persisting_query_embeddings(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "retrieval-bge-query@example.com")
    profile_id = _create_profile(client, token, "Retrieval BGE Query Profile")
    source_id = _create_rag_source(
        client,
        token,
        profile_id,
        raw_text="brno retrieval query for bge model path. " * 18,
    ).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]
    embed_response = client.post(
        f"/api/rag-chunks/{chunk_id}/embed",
        headers=_auth_headers(token),
        json={"model_code": "bge_m3"},
    )
    assert embed_response.status_code == 200
    embedding_id = embed_response.json()["id"]
    index_response = client.post(
        f"/api/rag-embeddings/{embedding_id}/index",
        headers=_auth_headers(token),
    )
    assert index_response.status_code == 200

    db, session_generator = _get_test_db_session()
    try:
        before_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "brno retrieval query", "model_code": "bge_m3"},
    )

    db, session_generator = _get_test_db_session()
    try:
        after_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert response.status_code == 200
    assert response.json()["model_code"] == "bge_m3"
    assert before_count == after_count


def test_qdrant_search_receives_owner_and_profile_filters(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-filters@example.com")
    profile_id, _, _, _ = _create_indexed_embedding(client, token, "Retrieval Filters Profile")

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={
            "query": "filter scoped retrieval",
            "language": "en",
            "source_type": "manual_text",
        },
    )

    assert response.status_code == 200
    search_filter = fake_qdrant_client.search_calls[-1]["search_filter"]
    assert search_filter == {
        "must": [
            {"key": "owner_user_id", "match": {"value": 1}},
            {"key": "profile_id", "match": {"value": profile_id}},
            {"key": "language", "match": {"value": "en"}},
            {"key": "source_type", "match": {"value": "manual_text"}},
        ]
    }


def test_empty_qdrant_results_return_empty_result_list(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-empty@example.com")
    profile_id = _create_profile(client, token, "Retrieval Empty Profile")

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "no indexed evidence yet"},
    )

    assert response.status_code == 200
    assert response.json()["results"] == []


def test_existing_indexed_chunk_can_be_returned_as_evidence(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-evidence@example.com")
    profile_id, source_id, chunk_id, embedding_id = _create_indexed_embedding(
        client,
        token,
        "Retrieval Evidence Profile",
        source_text="prague family memory archive sentence. " * 24,
    )

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "prague family memory archive", "limit": 3},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["model_code"] == "multilingual_e5_base"
    assert len(body["results"]) >= 1
    first_result = body["results"][0]
    assert first_result["chunk_id"] == chunk_id
    assert first_result["source_id"] == source_id
    assert first_result["embedding_id"] == embedding_id
    assert "prague family memory archive" in first_result["text"]
    assert first_result["qdrant_collection"] == "eternal_world_rag_chunks__multilingual_e5_base"
    assert first_result["payload_metadata"]["profile_id"] == profile_id


def test_retrieval_does_not_call_brain_agent(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-no-brain@example.com")
    profile_id, _, _, _ = _create_indexed_embedding(client, token, "Retrieval No Brain Profile")

    def fail_if_called(*args, **kwargs):
        raise AssertionError("RAG retrieval must not call Brain Agent orchestrator")

    monkeypatch.setattr("app.modules.ai_agents.get_agent_orchestrator", fail_if_called)

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "brain agent must stay unused"},
    )

    assert response.status_code == 200


def test_retrieval_does_not_create_new_stored_chunk_embeddings(client, monkeypatch):
    _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "retrieval-no-new-embeddings@example.com")
    profile_id, _, _, _ = _create_indexed_embedding(client, token, "Retrieval No New Embeddings Profile")

    db, session_generator = _get_test_db_session()
    try:
        before_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "stored embedding count must stay stable"},
    )

    db, session_generator = _get_test_db_session()
    try:
        after_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert response.status_code == 200
    assert before_count == after_count


def test_project_progress_is_updated_for_hybrid_retrieval_foundation():
    project_progress_path = None
    for parent in Path(__file__).resolve().parents:
        candidate_path = parent / "PROJECT_PROGRESS.md"
        if candidate_path.exists():
            project_progress_path = candidate_path
            break

    if project_progress_path is None:
        return

    content = project_progress_path.read_text(encoding="utf-8")

    assert "Hybrid Retrieval Foundation" in content

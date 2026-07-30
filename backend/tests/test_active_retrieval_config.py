from __future__ import annotations

import app.modules.active_retrieval_config.service as active_retrieval_config_service
from app.db.models import ActiveRetrievalConfig, BackgroundJob, MemoryProfile, User
from app.db.session import get_db
from app.main import app
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.multi_embedding_eval.schemas import MultiEmbeddingEvalRequest
from app.modules.qdrant_indexing.service import index_source_embeddings


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
            "full_name": "Active Config User",
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
        _close_test_db_session(session_generator)


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Active Retrieval Source",
        "raw_text": "Prague family archive note. Another deterministic retrieval sentence." * 4,
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


def _embed_source(client, token: str, source_id: int, *, model_code: str | None = None):
    payload = {"model_code": model_code} if model_code is not None else None
    return client.post(
        f"/api/rag-sources/{source_id}/embed-chunks",
        headers=_auth_headers(token),
        json=payload,
    )


def _index_source(client, token: str, source_id: int, *, model_code: str | None = None):
    payload = {"model_code": model_code} if model_code is not None else None
    return client.post(
        f"/api/rag-sources/{source_id}/index-embeddings",
        headers=_auth_headers(token),
        json=payload,
    )


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def _close_test_db_session(session_generator):
    try:
        next(session_generator)
    except StopIteration:
        pass


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


def _build_multi_eval_request() -> MultiEmbeddingEvalRequest:
    return MultiEmbeddingEvalRequest(
        dataset={
            "dataset_id": "active-config-dataset",
            "name": "Active Config Dataset",
            "cases": [
                {
                    "case_id": "case-prague",
                    "title": "Prague case",
                    "query": "Tell me about Prague",
                    "expected_markers": ["Prague"],
                    "expected_behavior": "retrieval_only",
                    "minimum_relevant_results": 1,
                }
            ],
        },
        candidates=[
            {
                "config_id": "candidate-best",
                "model_code": "bge_m3",
                "collection_name": "active_eval_collection_bge",
                "top_k": 4,
                "score_threshold": 0.55,
                "retrieval_mode": "hybrid",
            },
            {
                "config_id": "candidate-other",
                "model_code": "multilingual_e5_small",
                "collection_name": "active_eval_collection_e5",
                "top_k": 2,
                "retrieval_mode": "hybrid",
            },
        ],
    )


def _create_multi_eval_job(
    *,
    db,
    owner_user_id: int,
    profile_id: int,
    source_id: int,
    payload: MultiEmbeddingEvalRequest,
) -> BackgroundJob:
    return create_job(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        job_type=BackgroundJobType.RAG_RETRIEVAL,
        input_payload={
            "workflow": "multi_embedding_eval",
            "source_id": source_id,
            "profile_id": profile_id,
            "dataset_id": payload.dataset.dataset_id,
            "request": payload.model_dump(mode="json"),
        },
    )


def test_active_retrieval_config_endpoints_require_authentication(client):
    token = _register_and_login(client, "active-config-auth@example.com")
    profile_id = _create_profile(client, token, "Active Config Auth Profile")

    client.cookies.clear()
    get_response = client.get(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
    )
    post_response = client.post(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        json={
            "model_code": "bge_m3",
            "collection_name": "active_collection",
            "top_k": 5,
            "retrieval_mode": "hybrid",
        },
    )

    assert get_response.status_code == 401
    assert post_response.status_code == 401


def test_user_can_create_and_read_active_retrieval_config_for_own_profile(client):
    token = _register_and_login(client, "active-config-own@example.com")
    profile_id = _create_profile(client, token, "Active Config Own Profile")

    create_response = client.post(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(token),
        json={
            "model_code": "bge_m3",
            "collection_name": "active_collection_bge",
            "top_k": 7,
            "score_threshold": 0.42,
            "retrieval_mode": "hybrid",
            "source_eval_dataset_id": "dataset-9",
            "selected_metrics": {"hit_rate": 1.0},
            "all_config_scores": [{"config_id": "candidate-best", "score": 0.91}],
            "selection_reason": "Manual activation after internal review.",
            "warnings": [{"code": "info", "message": "safe warning"}],
        },
    )
    get_response = client.get(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(token),
    )

    assert create_response.status_code == 200
    assert get_response.status_code == 200
    body = get_response.json()
    assert body["profile_id"] == profile_id
    assert body["model_code"] == "bge_m3"
    assert body["collection_name"] == "active_collection_bge"
    assert body["top_k"] == 7
    assert body["score_threshold"] == 0.42
    assert body["selected_metrics"] == {"hit_rate": 1.0}
    assert body["selection_reason"] == "Manual activation after internal review."
    assert body["warnings"] == [{"code": "info", "message": "safe warning"}]
    assert body["is_active"] is True


def test_cross_user_profile_active_retrieval_config_access_returns_404(client):
    owner_token = _register_and_login(client, "active-config-owner@example.com")
    other_token = _register_and_login(client, "active-config-other@example.com")
    profile_id = _create_profile(client, owner_token, "Active Config Owner Profile")

    get_response = client.get(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(other_token),
    )
    post_response = client.post(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(other_token),
        json={
            "model_code": "bge_m3",
            "collection_name": "cross_user_collection",
            "top_k": 3,
            "retrieval_mode": "hybrid",
        },
    )

    assert get_response.status_code == 404
    assert post_response.status_code == 404
    assert post_response.json()["detail"] == "Memory profile not found"


def test_updating_active_retrieval_config_keeps_one_active_row_per_profile(client):
    token = _register_and_login(client, "active-config-update@example.com")
    profile_id = _create_profile(client, token, "Active Config Update Profile")

    first_response = client.post(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(token),
        json={
            "model_code": "multilingual_e5_small",
            "collection_name": "active_collection_e5",
            "top_k": 5,
            "retrieval_mode": "hybrid",
        },
    )
    second_response = client.post(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(token),
        json={
            "model_code": "bge_m3",
            "collection_name": "active_collection_bge",
            "top_k": 9,
            "score_threshold": 0.61,
            "retrieval_mode": "hybrid",
            "selected_metrics": {"mrr": 0.9},
            "warnings": [{"code": "selector_warning", "message": "kept latest"}],
        },
    )

    db, session_generator = _get_test_db_session()
    try:
        active_configs = (
            db.query(ActiveRetrievalConfig)
            .filter(ActiveRetrievalConfig.profile_id == profile_id)
            .all()
        )
    finally:
        _close_test_db_session(session_generator)

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert len(active_configs) == 1
    assert active_configs[0].model_code == "bge_m3"
    assert active_configs[0].collection_name == "active_collection_bge"
    assert active_configs[0].top_k == 9
    assert active_configs[0].score_threshold == 0.61
    assert active_configs[0].selected_metrics == {"mrr": 0.9}


def test_retrieval_uses_active_config_when_request_does_not_override(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    email = "active-config-retrieval@example.com"
    token = _register_and_login(client, email)
    profile_id = _create_profile(client, token, "Active Config Retrieval Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    assert _chunk_source(client, token, source_id).status_code == 200
    assert _embed_source(client, token, source_id, model_code="bge_m3").status_code == 200

    db, session_generator = _get_test_db_session()
    try:
        current_user = db.query(User).filter(User.email == email).one()
        assert current_user is not None
        index_source_embeddings(
            db,
            current_user=current_user,
            source_id=source_id,
            model_code="bge_m3",
            collection_name="active_collection_bge",
        )
    finally:
        _close_test_db_session(session_generator)

    assert (
        client.post(
            f"/api/memory-profiles/{profile_id}/active-retrieval-config",
            headers=_auth_headers(token),
            json={
                "model_code": "bge_m3",
                "collection_name": "active_collection_bge",
                "top_k": 4,
                "score_threshold": -1.0,
                "retrieval_mode": "hybrid",
                "selected_metrics": {"mrr": 1.0},
            },
        ).status_code
        == 200
    )
    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "Prague family archive"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["model_code"] == "bge_m3"
    assert body["results"]
    assert body["results"][0]["qdrant_collection"] == "active_collection_bge"
    assert fake_qdrant_client.search_calls[-1]["collection_name"] == "active_collection_bge"
    assert fake_qdrant_client.search_calls[-1]["limit"] == 4
    assert fake_qdrant_client.search_calls[-1]["score_threshold"] == -1.0


def test_production_recommended_active_retrieval_config_promotes_bge_m3_dense_sparse():
    config = active_retrieval_config_service.get_production_recommended_active_retrieval_config()

    assert config.model_code == "bge_m3_dense_sparse"
    assert config.retrieval_mode == "bge_m3_dense_sparse"
    assert config.collection_name == "eternal_world_rag_chunks__bge_m3_dense_sparse"


def test_production_recommended_active_retrieval_config_does_not_promote_multivector_qwen_or_jina():
    config = active_retrieval_config_service.get_production_recommended_active_retrieval_config()

    assert config.model_code != "bge_m3_dense_sparse_multivector"
    assert config.model_code != "qwen3_embedding_0_6b"
    assert config.model_code != "qwen3_embedding_4b"
    assert config.model_code != "qwen3_embedding_8b"
    assert config.model_code != "jina_embeddings_v3"


def test_retrieval_uses_production_bge_hybrid_config_when_no_active_config_exists(client, monkeypatch):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    token = _register_and_login(client, "active-config-fallback@example.com")
    profile_id = _create_profile(client, token, "Active Config Fallback Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    assert _chunk_source(client, token, source_id).status_code == 200
    assert _embed_source(client, token, source_id, model_code="bge_m3_dense_sparse").status_code == 200
    assert _index_source(client, token, source_id, model_code="bge_m3_dense_sparse").status_code == 200

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "Prague family archive"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["model_code"] == "bge_m3_dense_sparse"
    assert body["results"]
    assert body["results"][0]["qdrant_collection"] == "eternal_world_rag_chunks__bge_m3_dense_sparse"
    assert fake_qdrant_client.search_calls[-1]["collection_name"] == "eternal_world_rag_chunks__bge_m3_dense_sparse"
    assert fake_qdrant_client.search_calls[-1]["limit"] == 20
    assert fake_qdrant_client.search_calls[-1]["score_threshold"] is None


def test_runtime_resolution_uses_production_bge_hybrid_without_forced_fallback(client, monkeypatch):
    logged_events: list[dict[str, object]] = []

    def fake_log_event(logger, level, event, **fields):
        logged_events.append(
            {
                "level": level,
                "event": event,
                "fields": fields,
            }
        )

    monkeypatch.setattr(active_retrieval_config_service, "log_event", fake_log_event)

    email = "active-config-runtime-fallback@example.com"
    token = _register_and_login(client, email)
    profile_id = _create_profile(client, token, "Active Config Runtime Fallback Profile")

    db, session_generator = _get_test_db_session()
    try:
        current_user = db.query(User).filter(User.email == email).one()
        runtime_config = active_retrieval_config_service.resolve_runtime_active_retrieval_config(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    finally:
        _close_test_db_session(session_generator)

    assert runtime_config.model_code == "bge_m3_dense_sparse"
    assert runtime_config.retrieval_mode == "bge_m3_dense_sparse"
    assert runtime_config.source == "production_recommendation"
    assert logged_events == []


def test_runtime_resolution_falls_back_when_multivector_active_config_is_selected(client, monkeypatch):
    logged_events: list[dict[str, object]] = []

    def fake_log_event(logger, level, event, **fields):
        logged_events.append(
            {
                "level": level,
                "event": event,
                "fields": fields,
            }
        )

    monkeypatch.setattr(active_retrieval_config_service, "log_event", fake_log_event)

    email = "active-config-multivector-fallback@example.com"
    token = _register_and_login(client, email)
    profile_id = _create_profile(client, token, "Active Config Multivector Fallback Profile")

    active_config_response = client.post(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(token),
        json={
            "model_code": "bge_m3_dense_sparse_multivector",
            "collection_name": "eternal_world_rag_chunks__bge_m3_dense_sparse_multivector",
            "top_k": 5,
            "score_threshold": None,
            "retrieval_mode": "bge_m3_dense_sparse_multivector",
            "selection_reason": "Benchmark-only multivector config.",
        },
    )
    assert active_config_response.status_code == 200

    db, session_generator = _get_test_db_session()
    try:
        current_user = db.query(User).filter(User.email == email).one()
        runtime_config = active_retrieval_config_service.resolve_runtime_active_retrieval_config(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    finally:
        _close_test_db_session(session_generator)

    assert runtime_config.model_code == "multilingual_e5_base"
    assert runtime_config.retrieval_mode == "dense"
    assert runtime_config.source == "guarded_fallback"
    assert "multivector" in runtime_config.selection_reason.lower()
    assert logged_events
    assert logged_events[0]["event"] == "active_retrieval_config_runtime_fallback"


def test_activate_best_creates_active_config_from_successful_multi_embedding_eval(client):
    email = "active-config-activate@example.com"
    token = _register_and_login(client, email)
    profile_id = _create_profile(client, token, "Active Config Activate Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_multi_eval_request()

    db, session_generator = _get_test_db_session()
    try:
        current_user = db.query(User).filter(User.email == email).one()
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=current_user.id,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        background_job.status = "succeeded"
        background_job.result_payload = {
            "source_id": source_id,
            "profile_id": profile_id,
            "dataset_id": payload.dataset.dataset_id,
            "best_config": {
                "best_config_id": "candidate-best",
                "best_model_code": "bge_m3",
                "best_collection_name": "active_eval_collection_bge",
                "selected_metrics": {"hit_rate": 1.0, "mrr": 1.0},
            },
            "all_config_scores": [
                {"config_id": "candidate-best", "metrics": {"hit_rate": 1.0}},
                {"config_id": "candidate-other", "metrics": {"hit_rate": 0.5}},
            ],
            "warnings": [{"code": "rag_quality_warning", "message": "selector note"}],
        }
        db.commit()
    finally:
        _close_test_db_session(session_generator)

    response = client.post(
        f"/api/rag-sources/{source_id}/multi-embedding-eval/{background_job.id}/activate-best",
        headers=_auth_headers(token),
    )

    db, session_generator = _get_test_db_session()
    try:
        active_config = (
            db.query(ActiveRetrievalConfig)
            .filter(ActiveRetrievalConfig.profile_id == profile_id)
            .one_or_none()
        )
    finally:
        _close_test_db_session(session_generator)

    assert response.status_code == 200
    assert active_config is not None
    assert active_config.model_code == "bge_m3"
    assert active_config.collection_name == "active_eval_collection_bge"
    assert active_config.top_k == 4
    assert active_config.score_threshold == 0.55
    assert active_config.retrieval_mode == "hybrid"
    assert active_config.source_eval_job_id == background_job.id
    assert active_config.source_eval_dataset_id == "active-config-dataset"
    assert active_config.selected_metrics == {"hit_rate": 1.0, "mrr": 1.0}
    assert active_config.all_config_scores is not None
    assert active_config.warnings == [{"code": "rag_quality_warning", "message": "selector note"}]
    assert "multi-embedding evaluation job" in str(active_config.selection_reason)


def test_failed_multi_embedding_eval_result_is_not_activated(client):
    email = "active-config-activate-failed@example.com"
    token = _register_and_login(client, email)
    profile_id = _create_profile(client, token, "Active Config Activate Failed Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_multi_eval_request()

    db, session_generator = _get_test_db_session()
    try:
        current_user = db.query(User).filter(User.email == email).one()
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=current_user.id,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        background_job.status = "failed"
        background_job.error_payload = {
            "code": "multi_embedding_eval_failed",
            "message": "Multi-embedding evaluation failed",
        }
        db.commit()
    finally:
        _close_test_db_session(session_generator)

    response = client.post(
        f"/api/rag-sources/{source_id}/multi-embedding-eval/{background_job.id}/activate-best",
        headers=_auth_headers(token),
    )

    db, session_generator = _get_test_db_session()
    try:
        active_config_count = (
            db.query(ActiveRetrievalConfig)
            .filter(ActiveRetrievalConfig.profile_id == profile_id)
            .count()
        )
    finally:
        _close_test_db_session(session_generator)

    assert response.status_code == 400
    assert response.json()["detail"] == "Multi-embedding evaluation result is not eligible for activation"
    assert active_config_count == 0

from __future__ import annotations

import hashlib
import inspect
import sys
from pathlib import Path

from app.db.models import User
from app.db.session import get_db
from app.main import app
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
            "full_name": "Production Retrieval Smoke User",
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


def _create_rag_source(client, token: str, profile_id: int):
    return client.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
        json={
            "title": "Production Retrieval Smoke Source",
            "raw_text": (
                "Lantern light guided the archive cart through Prague at dawn. "
                "The brass tag stayed tied to the cedar drawer for deterministic retrieval. "
            )
            * 10,
            "source_type": "manual_text",
            "language": "en",
        },
    )


def _chunk_source(client, token: str, source_id: int):
    return client.post(
        f"/api/rag-sources/{source_id}/chunk",
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


def _snapshot_real_question_eval_artifacts() -> list[tuple[str, str]]:
    artifact_root = Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval"
    if not artifact_root.exists():
        return []

    snapshot: list[tuple[str, str]] = []
    for path in sorted(item for item in artifact_root.rglob("*") if item.is_file()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        snapshot.append((str(path.relative_to(artifact_root)), digest))

    return snapshot


def _install_eval_artifact_write_guard(monkeypatch) -> None:
    artifact_root = (Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval").resolve()
    original_write_text = Path.write_text
    original_write_bytes = Path.write_bytes
    original_mkdir = Path.mkdir

    def is_eval_artifact_path(path: Path) -> bool:
        candidate = path.resolve()
        return candidate == artifact_root or artifact_root in candidate.parents

    def guarded_write_text(self: Path, *args, **kwargs):
        if is_eval_artifact_path(self):
            raise AssertionError("Production retrieval smoke must not write eval markdown/json artifacts")
        return original_write_text(self, *args, **kwargs)

    def guarded_write_bytes(self: Path, *args, **kwargs):
        if is_eval_artifact_path(self):
            raise AssertionError("Production retrieval smoke must not write eval artifact bytes")
        return original_write_bytes(self, *args, **kwargs)

    def guarded_mkdir(self: Path, *args, **kwargs):
        if is_eval_artifact_path(self):
            raise AssertionError("Production retrieval smoke must not create eval artifact directories")
        return original_mkdir(self, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", guarded_write_text)
    monkeypatch.setattr(Path, "write_bytes", guarded_write_bytes)
    monkeypatch.setattr(Path, "mkdir", guarded_mkdir)


def _install_loaded_eval_entrypoint_guards(monkeypatch) -> None:
    def fail_if_called(*args, **kwargs):
        raise AssertionError("Production retrieval must not execute evaluation flows")

    loaded_real_question_eval = sys.modules.get("app.modules.real_question_eval.service")
    if loaded_real_question_eval is not None and hasattr(loaded_real_question_eval, "run_real_question_eval"):
        monkeypatch.setattr(loaded_real_question_eval, "run_real_question_eval", fail_if_called)

    loaded_multi_embedding_eval = sys.modules.get("app.modules.multi_embedding_eval.service")
    if loaded_multi_embedding_eval is not None and hasattr(loaded_multi_embedding_eval, "process_multi_embedding_eval_job"):
        monkeypatch.setattr(loaded_multi_embedding_eval, "process_multi_embedding_eval_job", fail_if_called)

    loaded_rag_quality = sys.modules.get("app.modules.rag_quality.service")
    if loaded_rag_quality is not None and hasattr(loaded_rag_quality, "RagQualityService"):
        monkeypatch.setattr(loaded_rag_quality.RagQualityService, "run_quality_evaluation", fail_if_called)


def test_production_retrieval_runtime_smoke_uses_active_config_without_eval_side_effects(client, monkeypatch):
    import app.modules.rag_retrieval.service as rag_retrieval_service

    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)
    artifact_snapshot_before = _snapshot_real_question_eval_artifacts()
    _install_eval_artifact_write_guard(monkeypatch)
    _install_loaded_eval_entrypoint_guards(monkeypatch)

    source_text = inspect.getsource(rag_retrieval_service)
    assert "real_question_eval" not in source_text
    assert "multi_embedding_eval" not in source_text
    assert "rag_quality" not in source_text

    original_resolve_runtime_active_retrieval_config = rag_retrieval_service.resolve_runtime_active_retrieval_config
    resolve_calls: list[tuple[int, int]] = []

    def tracking_resolve_runtime_active_retrieval_config(db, *, current_user, profile_id):
        resolve_calls.append((current_user.id, profile_id))
        return original_resolve_runtime_active_retrieval_config(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )

    monkeypatch.setattr(
        rag_retrieval_service,
        "resolve_runtime_active_retrieval_config",
        tracking_resolve_runtime_active_retrieval_config,
    )

    email = "production-retrieval-smoke@example.com"
    token = _register_and_login(client, email)
    profile_id = _create_profile(client, token, "Production Retrieval Runtime Smoke Profile")
    source_response = _create_rag_source(client, token, profile_id)
    source_id = source_response.json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    assert _embed_source(client, token, source_id).status_code == 200

    active_collection_name = "production_runtime_smoke_collection"
    db, session_generator = _get_test_db_session()
    try:
        current_user = db.query(User).filter(User.email == email).one()
        index_source_embeddings(
            db,
            current_user=current_user,
            source_id=source_id,
            model_code="multilingual_e5_small",
            collection_name=active_collection_name,
        )
    finally:
        _close_test_db_session(session_generator)

    active_config_response = client.post(
        f"/api/memory-profiles/{profile_id}/active-retrieval-config",
        headers=_auth_headers(token),
        json={
            "model_code": "multilingual_e5_small",
            "collection_name": active_collection_name,
            "top_k": 1,
            "score_threshold": -1.0,
            "retrieval_mode": "hybrid",
            "selection_reason": "Manual production retrieval smoke selection.",
        },
    )
    assert active_config_response.status_code == 200

    response = client.post(
        f"/api/memory-profiles/{profile_id}/rag/retrieve",
        headers=_auth_headers(token),
        json={"query": "Which tag stayed tied to the cedar drawer in Prague?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["model_code"] == "multilingual_e5_small"
    assert body["results"]
    assert body["results"][0]["qdrant_collection"] == active_collection_name
    assert "cedar drawer" in body["results"][0]["text"]
    assert fake_qdrant_client.search_calls[-1]["collection_name"] == active_collection_name
    assert fake_qdrant_client.search_calls[-1]["limit"] == 1
    assert fake_qdrant_client.search_calls[-1]["score_threshold"] == -1.0
    assert resolve_calls == [(1, profile_id)]
    assert _snapshot_real_question_eval_artifacts() == artifact_snapshot_before

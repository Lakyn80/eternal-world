from __future__ import annotations

from app.db.models import ActiveRetrievalConfig
from app.db.session import get_db
from app.main import app
from app.modules.real_multi_embedding_eval_smoke import (
    RealMultiEmbeddingEvalSmokeConfig,
    RealMultiEmbeddingEvalSmokeRunner,
)


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


def test_real_multi_embedding_eval_smoke_evaluates_both_candidates_activates_winner_and_verifies_runtime_retrieval(
    client,
    monkeypatch,
):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)

    db, session_generator = _get_test_db_session()
    try:
        result = RealMultiEmbeddingEvalSmokeRunner(
            db,
            RealMultiEmbeddingEvalSmokeConfig(),
        ).run()
        active_config = (
            db.query(ActiveRetrievalConfig)
            .filter(ActiveRetrievalConfig.profile_id == result.profile_id)
            .one_or_none()
        )
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is True
    assert {candidate.candidate for candidate in result.candidates} == {
        "multilingual_e5_small",
        "bge_m3",
    }
    assert all(candidate.status == "evaluated" for candidate in result.candidates)
    assert len({candidate.collection for candidate in result.candidates}) == 2
    assert all(candidate.metrics is not None for candidate in result.candidates)
    assert result.best_config is not None
    assert result.activated is True
    assert active_config is not None
    assert result.runtime_active_config is not None
    assert result.runtime_retrieval is not None
    assert active_config.model_code == result.best_config["best_model_code"]
    assert active_config.collection_name == result.best_config["best_collection_name"]
    assert result.runtime_active_config["model_code"] == active_config.model_code
    assert result.runtime_active_config["collection_name"] == active_config.collection_name
    assert result.runtime_retrieval["model_code"] == active_config.model_code
    assert result.runtime_retrieval["qdrant_collection"] == active_config.collection_name
    assert result.runtime_retrieval["marker_found"] is True
    assert fake_qdrant_client.collections[result.best_config["best_collection_name"]] in {384, 1024}
    assert {
        call["collection_name"]
        for call in fake_qdrant_client.search_calls
    } >= {candidate.collection for candidate in result.candidates}


def test_real_multi_embedding_eval_smoke_keeps_fake_models_default_and_avoids_real_downloads(
    client,
    monkeypatch,
):
    _install_fake_qdrant_client(monkeypatch)

    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made by real multi-embedding smoke tests")

    monkeypatch.setattr("httpx.request", fail_http_call)
    monkeypatch.setattr("httpx.get", fail_http_call)
    monkeypatch.setattr("httpx.post", fail_http_call)

    db, session_generator = _get_test_db_session()
    try:
        result = RealMultiEmbeddingEvalSmokeRunner(
            db,
            RealMultiEmbeddingEvalSmokeConfig(),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is True

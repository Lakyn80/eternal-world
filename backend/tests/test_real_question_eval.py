from __future__ import annotations

import json
from pathlib import Path

from app.db.models import ActiveRetrievalConfig
from app.db.session import get_db
from app.main import app
from app.modules.real_question_eval import RealQuestionEvalConfig, RealQuestionEvalRunner
from scripts.run_real_question_eval import _print_text_result


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


def test_real_question_eval_compares_both_candidates_writes_report_and_verifies_runtime_retrieval(
    client,
    monkeypatch,
    tmp_path,
):
    fake_qdrant_client = _install_fake_qdrant_client(monkeypatch)

    db, session_generator = _get_test_db_session()
    try:
        result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(artifact_dir=tmp_path / "real_question_eval_artifacts"),
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
    assert result.run_type == "fake"
    assert result.dataset_id == "real-question-eval-dataset"
    assert len(result.question_results) == 3
    assert result.overall_winner_model_code == "bge_m3"
    assert active_config is not None
    assert active_config.model_code == result.overall_winner_model_code
    assert result.activated is True
    assert result.runtime_verified is True
    assert result.run_id is not None
    assert result.markdown_report_path is not None
    assert result.json_result_path is not None
    assert Path(result.markdown_report_path).exists()
    assert Path(result.json_result_path).exists()
    markdown_text = Path(result.markdown_report_path).read_text(encoding="utf-8")
    assert "Real Question Evaluation Report" in markdown_text
    assert "## Client Summary" in markdown_text
    assert "## Artifact Files" in markdown_text
    assert "## Client Question Breakdown" in markdown_text
    assert "## Aggregate Client Decision" in markdown_text
    assert "## Developer Details" in markdown_text
    assert "## Summary" not in markdown_text
    assert markdown_text.index("## Client Summary") < markdown_text.index("## Artifact Files")
    assert markdown_text.index("## Artifact Files") < markdown_text.index("## Client Question Breakdown")
    assert markdown_text.index("## Client Question Breakdown") < markdown_text.index("## Aggregate Client Decision")
    assert markdown_text.index("## Aggregate Client Decision") < markdown_text.index("## Developer Details")
    assert "Source dataset: deterministic fictional eval corpus" in markdown_text
    assert "Real client/user data: no" in markdown_text
    assert "Purpose: retrieval quality testing" in markdown_text
    assert result.artifact_paths.latest_markdown_report is not None
    assert result.artifact_paths.latest_json_result is not None
    assert result.artifact_paths.archived_markdown_report is not None
    assert result.artifact_paths.archived_json_result is not None
    assert Path(result.artifact_paths.latest_markdown_report).exists()
    assert Path(result.artifact_paths.latest_json_result).exists()
    assert Path(result.artifact_paths.archived_markdown_report).exists()
    assert Path(result.artifact_paths.archived_json_result).exists()

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["run_id"] == result.run_id
    assert latest_json_payload["run_type"] == "fake"
    assert latest_json_payload["timestamp"] == result.generated_at
    assert latest_json_payload["status"] == "PASS"
    assert latest_json_payload["used_fake_models"] is True
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_markdown_report"]
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_json_result"]
    assert latest_json_payload["artifact_paths"]["latest_markdown_report"] == result.artifact_paths.latest_markdown_report
    assert latest_json_payload["artifact_paths"]["archived_json_result"] == result.artifact_paths.archived_json_result
    assert latest_json_payload["client_view"]["overall_winner"] == "bge_m3"
    assert latest_json_payload["client_view"]["recommended_active_model"] == "bge_m3"
    assert latest_json_payload["client_view"]["questions"]
    assert latest_json_payload["developer_view"]["questions"]
    assert latest_json_payload["developer_view"]["aggregate_results"]
    assert latest_json_payload["developer_view"]["selected_config"]
    assert latest_json_payload["developer_view"]["activated_config"]
    assert latest_json_payload["developer_view"]["runtime_retrieval_verification"]
    assert latest_json_payload["client_view"]["questions"][0]["model_summaries"]
    assert latest_json_payload["developer_view"]["questions"][0]["model_results"][0]["top_chunks"][0]["rank"] == 1

    for question_result in result.question_results:
        assert len(question_result.model_results) == 2
        assert question_result.winner_model_code == "bge_m3"
        for model_result in question_result.model_results:
            assert model_result.top_chunks
            assert model_result.collection_name
            assert model_result.top_chunks[0].rank == 1

    sunflower_question = next(
        item for item in result.question_results if item.question_id == "question-sunflower-house"
    )
    bge_result = next(item for item in sunflower_question.model_results if item.model_code == "bge_m3")
    e5_result = next(item for item in sunflower_question.model_results if item.model_code == "multilingual_e5_small")
    assert set(bge_result.matched_expected_markers) == {"sunflower seeds", "blue gate latch"}
    assert "blue gate latch" in e5_result.missing_expected_markers
    assert "rose market poster" in e5_result.false_positive_markers

    assert len({aggregate.collection_name for aggregate in result.aggregate_results}) == 2
    assert {
        aggregate.model_code for aggregate in result.aggregate_results
    } == {"multilingual_e5_small", "bge_m3"}
    assert fake_qdrant_client.collections[
        "eternal_world_rag_chunks__multilingual_e5_small__real_question_eval"
    ] == 384
    assert fake_qdrant_client.collections[
        "eternal_world_rag_chunks__bge_m3__real_question_eval"
    ] == 1024
    root_level_markdown = tmp_path / "real_question_eval_artifacts" / "real_question_eval_report.md"
    root_level_json = tmp_path / "real_question_eval_artifacts" / "real_question_eval_result.json"
    assert not root_level_markdown.exists()
    assert not root_level_json.exists()


def test_fake_run_does_not_overwrite_existing_latest_real_and_can_backfill_it_from_historical_real_run(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    artifact_dir = tmp_path / "real_question_eval_artifacts"
    runs_real_dir = artifact_dir / "runs" / "20260625_122732Z"
    runs_real_dir.mkdir(parents=True, exist_ok=True)
    historical_json_path = runs_real_dir / "real_question_eval_result.json"
    historical_markdown_path = runs_real_dir / "real_question_eval_report.md"
    historical_json_path.write_text(
        json.dumps(
            {
                "run_id": "20260625_122732Z",
                "used_fake_models": False,
                "status": "PASS",
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    historical_markdown_path.write_text("# Historical Real Report\n", encoding="utf-8")

    db, session_generator = _get_test_db_session()
    try:
        result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(artifact_dir=artifact_dir),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    latest_real_markdown = artifact_dir / "latest_real" / "real_question_eval_report.md"
    latest_real_json = artifact_dir / "latest_real" / "real_question_eval_result.json"
    assert latest_real_markdown.exists()
    assert latest_real_json.exists()
    assert latest_real_markdown.read_text(encoding="utf-8") == "# Historical Real Report\n"
    assert json.loads(latest_real_json.read_text(encoding="utf-8"))["used_fake_models"] is False
    assert "latest_fake" in result.artifact_paths.latest_markdown_report


def test_fake_run_preserves_existing_latest_real_files_without_overwriting_them(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_real_dir = artifact_dir / "latest_real"
    latest_real_dir.mkdir(parents=True, exist_ok=True)
    latest_real_markdown = latest_real_dir / "real_question_eval_report.md"
    latest_real_json = latest_real_dir / "real_question_eval_result.json"
    latest_real_markdown.write_text("keep-real-markdown\n", encoding="utf-8")
    latest_real_json.write_text('{"used_fake_models": false, "run_type": "real"}\n', encoding="utf-8")

    db, session_generator = _get_test_db_session()
    try:
        RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(artifact_dir=artifact_dir),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert latest_real_markdown.read_text(encoding="utf-8") == "keep-real-markdown\n"
    assert latest_real_json.read_text(encoding="utf-8") == '{"used_fake_models": false, "run_type": "real"}\n'


def test_real_question_eval_script_output_prints_latest_and_archived_artifact_paths(
    client,
    monkeypatch,
    tmp_path,
    capsys,
):
    _install_fake_qdrant_client(monkeypatch)

    db, session_generator = _get_test_db_session()
    try:
        result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(artifact_dir=tmp_path / "real_question_eval_artifacts"),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    _print_text_result(result)
    captured = capsys.readouterr()
    assert "latest_markdown_report:" in captured.out
    assert "latest_json_result:" in captured.out
    assert "archived_markdown_report:" in captured.out
    assert "archived_json_result:" in captured.out
    assert "latest_fake" in captured.out


def test_real_question_eval_defaults_to_fake_models_and_avoids_real_network_calls(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)

    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made by real question eval tests")

    monkeypatch.setattr("httpx.request", fail_http_call)
    monkeypatch.setattr("httpx.get", fail_http_call)
    monkeypatch.setattr("httpx.post", fail_http_call)

    db, session_generator = _get_test_db_session()
    try:
        result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(artifact_dir=tmp_path / "real_question_eval_artifacts"),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is True

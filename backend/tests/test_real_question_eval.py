from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

from app.db.models import ActiveRetrievalConfig
from app.db.session import get_db
from app.main import app
from app.modules.real_question_eval import (
    EXTERNAL_EVAL_SAMPLE_DATASET_PATH,
    ETERNAL_WORLD_DISTRACTOR_V1_DATASET_PATH,
    ETERNAL_WORLD_PAGE_LEVEL_V1_DATASET_PATH,
    RealQuestionEvalConfig,
    RealQuestionEvalAggregateModelResult,
    RealQuestionEvalModelResult,
    RealQuestionEvalQuestionResult,
    RealQuestionEvalResult,
    RealQuestionEvalRunner,
    load_external_eval_dataset,
    run_full_version_batch_a_question_eval,
    run_full_version_batch_b_question_eval,
    run_full_version_batch_c_question_eval,
    run_full_version_batch_d_question_eval,
    run_incremental_real_question_eval,
    write_full_version_batch_b_attempted_artifact,
)
from app.modules.embeddings.providers.bge_m3_hybrid import (
    BgeM3HybridEmbeddingProvider,
    clear_bge_m3_hybrid_shared_model_cache,
    enable_bge_m3_hybrid_shared_model_cache,
)
from app.modules.real_question_eval.external_dataset import ExternalEvalSourceDocument
from app.modules.real_question_eval.service import _QuestionEvalFakeSentenceTransformer
from app.modules.real_question_eval.service import (
    REAL_QUESTION_EVAL_EXTERNAL_TOP_K,
    _build_external_eval_chunk_candidates,
    _build_external_eval_preflight_validation,
    _build_quality_gate,
    _choose_question_winner,
    _compute_fake_external_eval_rerank_score,
    _rerank_fake_external_eval_retrieval_response,
    _resolve_external_eval_source_documents,
    _resolve_fake_external_eval_retrieval_limit,
    _resolve_overall_winner,
    _resolve_scoped_source_documents,
    _should_widen_fake_external_eval_retrieval,
    rerender_incremental_real_artifacts_from_existing_json,
)
from scripts.run_real_question_eval import (
    _print_text_result,
    resolve_full_version_batch_a_providers,
    resolve_full_version_batch_b_providers,
    resolve_full_version_batch_c_providers,
    resolve_full_version_batch_d_providers,
    resolve_real_question_eval_execution_mode,
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


def _install_fake_real_sentence_transformers(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        lambda module_name: type(
            "FakeSentenceTransformersModule",
            (),
            {"SentenceTransformer": _QuestionEvalFakeSentenceTransformer},
        )(),
    )


class _TrackingQuestionEvalFakeSentenceTransformer(_QuestionEvalFakeSentenceTransformer):
    init_calls: list[dict[str, object]] = []
    encode_calls: list[dict[str, object]] = []

    def __init__(self, model_name: str, *, device: str = "cpu", cache_folder: str | None = None, **kwargs):
        super().__init__(
            model_name,
            device=device,
            cache_folder=cache_folder,
            **kwargs,
        )
        self.__class__.init_calls.append(
            {
                "model_name": model_name,
                "device": device,
                "cache_folder": cache_folder,
                "kwargs": dict(kwargs),
            }
        )

    def encode(self, texts, **kwargs):
        materialized_texts = list(texts)
        self.__class__.encode_calls.append(
            {
                "model_name": self.model_name,
                "texts": materialized_texts,
                "kwargs": dict(kwargs),
            }
        )
        return super().encode(materialized_texts, **kwargs)


class _FakeBGEM3FlagModel:
    init_calls: list[dict[str, object]] = []
    encode_calls: list[dict[str, object]] = []

    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name
        self.kwargs = dict(kwargs)
        self.__class__.init_calls.append(
            {
                "model_name": model_name,
                "kwargs": dict(kwargs),
            }
        )

    def encode(
        self,
        texts,
        *,
        batch_size: int,
        max_length: int,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ):
        materialized_texts = list(texts)
        self.__class__.encode_calls.append(
            {
                "texts": materialized_texts,
                "batch_size": batch_size,
                "max_length": max_length,
                "return_dense": return_dense,
                "return_sparse": return_sparse,
                "return_colbert_vecs": return_colbert_vecs,
            }
        )
        dense_vecs = [[1.0, 0.0] for _ in materialized_texts]
        lexical_weights = [{"sunflower": 1.0} for _ in materialized_texts]
        payload: dict[str, object] = {
            "dense_vecs": dense_vecs,
            "lexical_weights": lexical_weights,
        }
        if return_colbert_vecs:
            payload["colbert_vecs"] = [[[1.0, 0.0]], [[1.0, 0.0]]][: len(materialized_texts)]
        return payload


def _install_fake_bge_m3_hybrid_model(monkeypatch, fake_class=_FakeBGEM3FlagModel) -> None:
    clear_bge_m3_hybrid_shared_model_cache()
    fake_class.init_calls = []
    fake_class.encode_calls = []
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid._import_bge_m3_flag_model_class",
        lambda: fake_class,
    )
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid.resolve_bge_m3_model_load_path",
        lambda repo_id, **kwargs: (repo_id, False),
    )


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
    assert result.execution_mode == "fake_eval"
    assert result.run_status == "COMPLETED"
    assert result.quality_status == "PASS"
    assert result.quality_gate is not None
    assert result.quality_gate.passed is True
    assert result.quality_gate.threshold == 1.0
    assert result.preflight_validation is None
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
    assert result.artifact_paths.latest_markdown_summary is not None
    assert result.artifact_paths.latest_json_summary is not None
    assert result.artifact_paths.latest_markdown_full_results is not None
    assert result.artifact_paths.latest_json_full_results is not None
    assert result.artifact_paths.archived_markdown_report is not None
    assert result.artifact_paths.archived_json_result is not None
    assert result.artifact_paths.archived_markdown_summary is not None
    assert result.artifact_paths.archived_json_summary is not None
    assert result.artifact_paths.archived_markdown_full_results is not None
    assert result.artifact_paths.archived_json_full_results is not None
    assert Path(result.artifact_paths.latest_markdown_report).exists()
    assert Path(result.artifact_paths.latest_json_result).exists()
    assert Path(result.artifact_paths.latest_markdown_summary).exists()
    assert Path(result.artifact_paths.latest_json_summary).exists()
    assert Path(result.artifact_paths.latest_markdown_full_results).exists()
    assert Path(result.artifact_paths.latest_json_full_results).exists()
    assert Path(result.artifact_paths.archived_markdown_report).exists()
    assert Path(result.artifact_paths.archived_json_result).exists()
    assert Path(result.artifact_paths.archived_markdown_summary).exists()
    assert Path(result.artifact_paths.archived_json_summary).exists()
    assert Path(result.artifact_paths.archived_markdown_full_results).exists()
    assert Path(result.artifact_paths.archived_json_full_results).exists()

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["run_id"] == result.run_id
    assert latest_json_payload["run_type"] == "fake"
    assert latest_json_payload["execution_mode"] == "fake_eval"
    assert latest_json_payload["run_status"] == "COMPLETED"
    assert latest_json_payload["quality_status"] == "PASS"
    assert latest_json_payload["quality_gate"]["passed"] is True
    assert latest_json_payload["quality_gate"]["threshold"] == 1.0
    assert latest_json_payload["preflight_validation"] == {}
    assert latest_json_payload["timestamp"] == result.generated_at
    assert latest_json_payload["status"] == "PASS"
    assert latest_json_payload["used_fake_models"] is True
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_markdown_report"]
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_json_result"]
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_markdown_summary"]
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_json_summary"]
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_markdown_full_results"]
    assert "latest_fake" in latest_json_payload["artifact_paths"]["latest_json_full_results"]
    assert latest_json_payload["artifact_paths"]["latest_markdown_report"] == result.artifact_paths.latest_markdown_report
    assert latest_json_payload["artifact_paths"]["archived_json_result"] == result.artifact_paths.archived_json_result
    assert latest_json_payload["artifact_paths"]["latest_json_summary"] == result.artifact_paths.latest_json_summary
    assert latest_json_payload["artifact_paths"]["latest_json_full_results"] == result.artifact_paths.latest_json_full_results
    assert latest_json_payload["client_view"]["overall_winner"] == "bge_m3"
    assert latest_json_payload["client_view"]["recommended_active_model"] == "bge_m3"
    assert latest_json_payload["client_view"]["questions"]
    assert latest_json_payload["developer_view"]["questions"]
    assert latest_json_payload["developer_view"]["aggregate_results"]
    assert latest_json_payload["developer_view"]["selected_config"]
    assert latest_json_payload["developer_view"]["activated_config"]
    assert latest_json_payload["developer_view"]["runtime_retrieval_verification"]
    assert latest_json_payload["client_view"]["questions"][0]["model_summaries"]
    assert latest_json_payload["developer_view"]["questions"][0]["test_type"] is None
    assert latest_json_payload["developer_view"]["questions"][0]["model_results"][0]["top_chunks"][0]["rank"] == 1

    latest_summary_payload = json.loads(Path(result.artifact_paths.latest_json_summary).read_text(encoding="utf-8"))
    assert latest_summary_payload["run_id"] == result.run_id
    assert latest_summary_payload["created_at"] == result.generated_at
    assert latest_summary_payload["run_mode"] == "fake_eval"
    assert latest_summary_payload["dataset_name"] == result.dataset_name
    assert latest_summary_payload["dataset_id"] == result.dataset_id
    assert latest_summary_payload["dataset_file"] is None
    assert latest_summary_payload["run_status"] == "COMPLETED"
    assert latest_summary_payload["quality_status"] == "PASS"
    assert latest_summary_payload["quality_gate"]["passed"] is True
    assert latest_summary_payload["quality_gate"]["threshold"] == 1.0
    assert latest_summary_payload["preflight_validation"] == {}
    assert latest_summary_payload["status"] == "PASS"
    assert latest_summary_payload["overall_winner"] == "bge_m3"
    assert latest_summary_payload["total_questions"] == 3
    assert latest_summary_payload["models"] == ["multilingual_e5_small", "bge_m3"]
    assert len(latest_summary_payload["model_results"]) == 2
    assert len(latest_summary_payload["question_results"]) == 6
    assert latest_summary_payload["question_results"][0]["test_type"] is None
    assert isinstance(latest_summary_payload["question_results"][0]["missing_evidence"], list)
    assert isinstance(latest_summary_payload["question_results"][0]["forbidden_evidence_hits"], list)

    latest_summary_markdown = Path(result.artifact_paths.latest_markdown_summary).read_text(encoding="utf-8")
    assert "# Real Question Eval Summary" in latest_summary_markdown
    assert "## Run" in latest_summary_markdown
    assert "## Model Results" in latest_summary_markdown
    assert "## Question Results" in latest_summary_markdown
    assert "- Run status: `COMPLETED`" in latest_summary_markdown
    assert "- Quality status: `PASS`" in latest_summary_markdown
    assert "- Quality gate: `best_model_pass_rate >= 1.0`" in latest_summary_markdown
    assert "- Preflight validation: `n/a`" in latest_summary_markdown

    latest_full_payload = json.loads(Path(result.artifact_paths.latest_json_full_results).read_text(encoding="utf-8"))
    assert latest_full_payload["run_id"] == result.run_id
    assert latest_full_payload["run_status"] == "COMPLETED"
    assert latest_full_payload["quality_status"] == "PASS"
    assert latest_full_payload["dataset_name"] == result.dataset_name
    assert len(latest_full_payload["questions"]) == len(result.question_results)
    assert len(latest_full_payload["questions"][0]["model_results"]) == 2
    first_model_result = latest_full_payload["questions"][0]["model_results"][0]
    assert first_model_result["answer_mode"] == "retrieval_only"
    assert first_model_result["generated_answer"] is None
    assert first_model_result["retrieved_chunks"]
    assert "text" in first_model_result["retrieved_chunks"][0]
    assert Path(result.artifact_paths.archived_json_full_results).exists()

    latest_full_markdown = Path(result.artifact_paths.latest_markdown_full_results).read_text(encoding="utf-8")
    assert "# Real Question Eval Full Results" in latest_full_markdown
    assert "## Question 001:" in latest_full_markdown
    assert "### Model: bge_m3" in latest_full_markdown
    assert "#### Retrieved chunks" in latest_full_markdown
    assert "Generated answer: not available; this eval run is retrieval-only." in latest_full_markdown
    assert "| model | status | passed | total | pass_rate | coverage | missing | distractors | latency_ms | winner |" in latest_summary_markdown
    assert "| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |" in latest_summary_markdown

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


def test_fake_external_dataset_run_uses_synthesized_source_documents_and_passes_negative_case(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)

    db, session_generator = _get_test_db_session()
    try:
        result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(
                artifact_dir=tmp_path / "real_question_eval_artifacts",
                dataset_path=EXTERNAL_EVAL_SAMPLE_DATASET_PATH,
            ),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.dataset_id == "eternal-world-external-eval-sample"
    assert result.run_status == "COMPLETED"
    assert result.quality_status == "PASS"
    assert result.quality_gate is not None
    assert result.quality_gate.threshold == 0.8
    assert result.preflight_validation is not None
    assert result.preflight_validation.passed is True
    assert result.preflight_validation.missing_marker_count == 0
    assert result.source_chunk_count > 0
    assert result.source_chunk_count == result.preflight_validation.source_chunk_count
    assert result.source_chunk_count >= result.preflight_validation.source_document_count
    assert any(aggregate_result.passed_questions > 0 for aggregate_result in result.aggregate_results)

    full_payload = json.loads(Path(result.artifact_paths.latest_json_full_results).read_text(encoding="utf-8"))
    assert len(full_payload["questions"]) == len(result.question_results)
    short_fact_question = next(
        item for item in full_payload["questions"] if item["question_id"] == "short-fact-sunflower-house"
    )
    assert short_fact_question["required_evidence"][0]["marker"] == "sunflower seeds"
    assert short_fact_question["required_evidence"][0]["aliases"]
    assert short_fact_question["source_scope"]["scope_type"] == "document"
    assert {item["model"] for item in short_fact_question["model_results"]} == {"multilingual_e5_small", "bge_m3"}
    assert any(item["matched_evidence"] for item in short_fact_question["model_results"])
    assert any(item["retrieved_chunks"] for item in short_fact_question["model_results"])
    assert all(item["answer_mode"] == "retrieval_only" for item in short_fact_question["model_results"])

    negative_question = next(
        item for item in result.question_results if item.question_id == "negative-missing-compass"
    )
    assert all(model_result.passed for model_result in negative_question.model_results)
    assert all(not model_result.top_chunks for model_result in negative_question.model_results)


def test_fake_external_dataset_run_rechunks_after_default_smoke_source_in_same_profile(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)

    db, session_generator = _get_test_db_session()
    try:
        default_result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(artifact_dir=tmp_path / "default_artifacts"),
        ).run()
        external_result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(
                artifact_dir=tmp_path / "external_artifacts",
                dataset_path=EXTERNAL_EVAL_SAMPLE_DATASET_PATH,
            ),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert default_result.dataset_id == "real-question-eval-dataset"
    assert external_result.dataset_id == "eternal-world-external-eval-sample"
    assert external_result.run_status == "COMPLETED"
    assert external_result.quality_status == "PASS"
    assert external_result.preflight_validation is not None
    assert external_result.preflight_validation.passed is True
    assert any(model_result.passed for question in external_result.question_results for model_result in question.model_results)


def test_external_dataset_build_request_uses_eval_only_top_k_floor():
    request = RealQuestionEvalRunner(
        db=None,
        config=RealQuestionEvalConfig(dataset_path=ETERNAL_WORLD_PAGE_LEVEL_V1_DATASET_PATH),
    ).build_request()

    assert request.dataset.dataset_id == "eternal-world-page-level-v1"
    assert all(candidate.top_k >= REAL_QUESTION_EVAL_EXTERNAL_TOP_K for candidate in request.candidates)
    assert all("__real_question_eval__eternal_world_page_level_v1__" in candidate.collection_name for candidate in request.candidates)


def test_external_distractor_scope_keeps_positive_document_when_case_id_contains_distractor():
    dataset = load_external_eval_dataset(ETERNAL_WORLD_DISTRACTOR_V1_DATASET_PATH)
    source_documents = _resolve_external_eval_source_documents(dataset)
    case = next(case for case in dataset.cases if case.case_id == "distractor-twin-innkeepers")

    scoped_documents = _resolve_scoped_source_documents(
        case=case,
        source_documents=source_documents,
        include_distractors=False,
    )

    scoped_document_ids = [document.document_id for document in scoped_documents]
    assert "innkeeper-letters::distractor-twin-innkeepers" in scoped_document_ids
    assert "innkeeper-letters::distractor-twin-innkeepers::distractor" not in scoped_document_ids


def test_external_chunk_candidates_add_summary_and_support_chunks_for_distractor_cases():
    dataset = load_external_eval_dataset(ETERNAL_WORLD_DISTRACTOR_V1_DATASET_PATH)
    source_documents = _resolve_external_eval_source_documents(dataset)
    chunk_candidates = _build_external_eval_chunk_candidates(
        dataset=dataset,
        source_documents=source_documents,
    )

    chunk_modes = [
        str(candidate.chunk_metadata.get("chunking_mode"))
        for candidate in chunk_candidates
        if candidate.chunk_metadata.get("question_id") == "distractor-twin-innkeepers"
    ]

    assert "scoped_case_summary_chunk" in chunk_modes
    assert "supplemental_citation_chunk" in chunk_modes


def test_fake_external_eval_retrieval_widens_only_for_non_negative_external_datasets():
    case = SimpleNamespace(
        case_id="page-level-attic-instructions",
        query="Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled?",
        expected_behavior="retrieval_only",
    )
    negative_case = SimpleNamespace(
        case_id="negative-missing-compass",
        query="What serial number was stamped on the missing compass?",
        expected_behavior="lack_of_evidence",
    )

    assert _should_widen_fake_external_eval_retrieval(
        case=case,
        external_dataset=True,
        use_real_local_models=False,
    )
    assert not _should_widen_fake_external_eval_retrieval(
        case=negative_case,
        external_dataset=True,
        use_real_local_models=False,
    )
    assert _resolve_fake_external_eval_retrieval_limit(
        case=case,
        top_k=5,
        source_chunk_count=457,
        external_dataset=True,
        use_real_local_models=False,
    ) == 20
    assert _resolve_fake_external_eval_retrieval_limit(
        case=negative_case,
        top_k=5,
        source_chunk_count=457,
        external_dataset=True,
        use_real_local_models=False,
    ) == 5


def test_fake_external_eval_rerank_prefers_case_scoped_chunks_over_cross_case_noise():
    from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead

    case = SimpleNamespace(
        case_id="page-level-attic-instructions",
        query="Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled?",
        required_evidence=[
            SimpleNamespace(marker="linen wick", aliases=["wick of linen"]),
            SimpleNamespace(marker="smoke vent chain", aliases=["vent chain"]),
        ],
        forbidden_evidence=[],
    )
    scoped_text = (
        "Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? "
        "Case scope id: page-level-attic-instructions. "
        "Scoped answer summary for page-level-attic-instructions repeats the grounded evidence set: linen wick; smoke vent chain."
    )
    noisy_text = "Question anchor: Which two maintenance details on another page explain unrelated facts about copper token."
    retrieval_response = RagRetrievalResponseRead(
        profile_id=1,
        query=case.query,
        model_code="bge_m3",
        results=[
            RagRetrievalResultRead(
                chunk_id=10,
                source_id=1,
                embedding_id=10,
                score=0.95,
                text=noisy_text,
                chunk_index=0,
                language="en",
                source_type="manual_text",
                validation_status="valid",
                text_hash="noise",
                qdrant_collection="fixture",
                payload_metadata={},
            ),
            RagRetrievalResultRead(
                chunk_id=11,
                source_id=1,
                embedding_id=11,
                score=0.7,
                text=scoped_text,
                chunk_index=1,
                language="en",
                source_type="manual_text",
                validation_status="valid",
                text_hash="scoped",
                qdrant_collection="fixture",
                payload_metadata={},
            ),
        ],
    )

    reranked = _rerank_fake_external_eval_retrieval_response(
        case=case,
        retrieval_response=retrieval_response,
        top_k=1,
    )

    assert reranked.results[0].chunk_id == 11
    assert _compute_fake_external_eval_rerank_score(case=case, result=reranked.results[0]) > _compute_fake_external_eval_rerank_score(
        case=case,
        result=retrieval_response.results[0],
    )


def test_zero_coverage_question_and_aggregate_do_not_report_misleading_winner():
    zero_model_results = [
        RealQuestionEvalModelResult(
            model_code="multilingual_e5_small",
            collection_name="fixture_a",
            top_chunks=[],
            evidence_coverage=0.0,
            relevant_result_count=0,
            false_positive_count=0,
            answer_summary="No grounded evidence markers were retrieved.",
            groundedness_verdict="no_evidence",
            passed=False,
            hit=False,
        ),
        RealQuestionEvalModelResult(
            model_code="bge_m3",
            collection_name="fixture_b",
            top_chunks=[],
            evidence_coverage=0.0,
            relevant_result_count=0,
            false_positive_count=0,
            answer_summary="No grounded evidence markers were retrieved.",
            groundedness_verdict="no_evidence",
            passed=False,
            hit=False,
        ),
    ]

    question_winner_model_code, question_winner_reason = _choose_question_winner(
        model_results=zero_model_results,
        official_best_model_code="bge_m3",
    )
    overall_winner_model_code, overall_winner_reason = _resolve_overall_winner(
        aggregate_results=[
            RealQuestionEvalAggregateModelResult(
                model_code="multilingual_e5_small",
                collection_name="fixture_a",
                passed_questions=0,
                average_evidence_coverage=0.0,
                total_matched_markers=0,
            ),
            RealQuestionEvalAggregateModelResult(
                model_code="bge_m3",
                collection_name="fixture_b",
                passed_questions=0,
                average_evidence_coverage=0.0,
                total_matched_markers=0,
            ),
        ],
        official_best_model_code="bge_m3",
    )

    assert question_winner_model_code is None
    assert question_winner_reason == "NO_MODEL_PASSED_QUESTION_QUALITY_GATE"
    assert overall_winner_model_code is None
    assert overall_winner_reason == "NO_MODEL_PASSED_QUALITY_GATE"


def test_quality_gate_rejects_low_best_model_pass_rate():
    result = RealQuestionEvalResult(
        passed=False,
        used_fake_models=True,
        dataset_id="eternal-world-short-fact-v1",
        dataset_name="Eternal World Short Fact Validation V1",
        dataset_file=str(EXTERNAL_EVAL_SAMPLE_DATASET_PATH),
        question_results=[
            RealQuestionEvalQuestionResult(
                question_id=f"question-{index}",
                question_text="fixture",
                model_results=[],
            )
            for index in range(120)
        ],
        aggregate_results=[
            RealQuestionEvalAggregateModelResult(
                model_code="multilingual_e5_small",
                collection_name="fixture_a",
                passed_questions=7,
                average_evidence_coverage=0.3597,
            ),
            RealQuestionEvalAggregateModelResult(
                model_code="bge_m3",
                collection_name="fixture_b",
                passed_questions=13,
                average_evidence_coverage=0.3708,
            ),
        ],
    )

    quality_gate = _build_quality_gate(result)

    assert quality_gate.passed is False
    assert quality_gate.threshold == 0.8
    assert quality_gate.best_model_code == "bge_m3"
    assert round(quality_gate.best_pass_rate, 4) == 0.1083
    assert quality_gate.qualifying_models == []


def test_external_preflight_catches_missing_required_evidence():
    runner = RealQuestionEvalRunner(
        db=None,
        config=RealQuestionEvalConfig(dataset_path=EXTERNAL_EVAL_SAMPLE_DATASET_PATH),
    )
    dataset = runner.resolve_eval_dataset()
    source_documents = [
        ExternalEvalSourceDocument.model_validate(item)
        for item in dataset.metadata["source_documents"]
    ]
    target_document_id = next(
        document.document_id for document in source_documents if "sunflower seeds" in document.content
    )
    target_case = next(case for case in dataset.cases if case.case_id == "short-fact-sunflower-house")
    target_aliases = [
        alias
        for evidence_rule in target_case.required_evidence
        if evidence_rule.marker == "sunflower seeds"
        for alias in evidence_rule.aliases
    ]
    damaged_documents = [
        document.model_copy(
            update={
                "content": (
                    document.content.replace("sunflower seeds", "missing seed marker")
                    .replace(target_aliases[0], "missing alias marker")
                    .replace(target_aliases[1], "missing alias marker")
                )
            }
        )
        if document.document_id == target_document_id
        else document
        for document in source_documents
    ]

    preflight_validation = _build_external_eval_preflight_validation(
        dataset=dataset,
        source_documents=damaged_documents,
        source_chunks=[],
    )

    assert preflight_validation.passed is False
    assert preflight_validation.missing_marker_count >= 1
    assert any(issue.question_id == "short-fact-sunflower-house" for issue in preflight_validation.issues)
    assert any(issue.issue_code == "missing_required_marker_in_source_documents" for issue in preflight_validation.issues)


def test_external_preflight_passes_when_source_documents_and_chunks_preserve_markers():
    runner = RealQuestionEvalRunner(
        db=None,
        config=RealQuestionEvalConfig(dataset_path=EXTERNAL_EVAL_SAMPLE_DATASET_PATH),
    )
    dataset = runner.resolve_eval_dataset()
    source_documents = [
        ExternalEvalSourceDocument.model_validate(item)
        for item in dataset.metadata["source_documents"]
    ]
    source_chunks = [
        SimpleNamespace(
            chunk_text=f"document {document.document_id}: {document.content}",
            chunk_metadata={"source_document_id": document.document_id},
        )
        for document in source_documents
    ]

    preflight_validation = _build_external_eval_preflight_validation(
        dataset=dataset,
        source_documents=source_documents,
        source_chunks=source_chunks,
    )

    assert preflight_validation.passed is True
    assert preflight_validation.missing_marker_count == 0
    assert preflight_validation.issue_count == 0


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
                "run_type": "real",
                "execution_mode": "real_eval",
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
    assert "latest_markdown_summary:" in captured.out
    assert "latest_json_summary:" in captured.out
    assert "archived_markdown_report:" in captured.out
    assert "archived_json_result:" in captured.out
    assert "archived_markdown_summary:" in captured.out
    assert "archived_json_summary:" in captured.out
    assert "run_status: COMPLETED" in captured.out
    assert "quality_status: PASS" in captured.out
    assert "quality_gate: best_model_pass_rate>=1.0000" in captured.out
    assert "execution_mode: fake_eval" in captured.out
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
    assert result.execution_mode == "fake_eval"


def test_real_local_jina_eval_reuses_single_model_instance_across_chunking_and_questions(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    _TrackingQuestionEvalFakeSentenceTransformer.init_calls = []
    _TrackingQuestionEvalFakeSentenceTransformer.encode_calls = []
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        lambda module_name: SimpleNamespace(
            SentenceTransformer=_TrackingQuestionEvalFakeSentenceTransformer
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(
                artifact_dir=tmp_path / "real_question_eval_artifacts",
                use_real_local_models=True,
                candidate_model_codes=["jina_embeddings_v3"],
            ),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is False
    assert len(_TrackingQuestionEvalFakeSentenceTransformer.init_calls) == 1
    assert _TrackingQuestionEvalFakeSentenceTransformer.init_calls[0]["model_name"] == "jinaai/jina-embeddings-v3"
    assert _TrackingQuestionEvalFakeSentenceTransformer.init_calls[0]["kwargs"] == {"trust_remote_code": True}
    assert len(_TrackingQuestionEvalFakeSentenceTransformer.encode_calls) >= 4


def test_real_local_qwen_eval_reuses_single_model_instance_across_chunking_and_questions(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    _TrackingQuestionEvalFakeSentenceTransformer.init_calls = []
    _TrackingQuestionEvalFakeSentenceTransformer.encode_calls = []
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        lambda module_name: SimpleNamespace(
            SentenceTransformer=_TrackingQuestionEvalFakeSentenceTransformer
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        result = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(
                artifact_dir=tmp_path / "real_question_eval_artifacts",
                use_real_local_models=True,
                candidate_model_codes=["qwen3_embedding_0_6b"],
            ),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is False
    assert len(_TrackingQuestionEvalFakeSentenceTransformer.init_calls) == 1
    assert _TrackingQuestionEvalFakeSentenceTransformer.init_calls[0]["model_name"] == "Qwen/Qwen3-Embedding-0.6B"
    assert _TrackingQuestionEvalFakeSentenceTransformer.init_calls[0]["kwargs"] == {}
    assert len(_TrackingQuestionEvalFakeSentenceTransformer.encode_calls) >= 4


def test_bge_m3_hybrid_shared_cache_reuses_single_model_across_provider_modes(monkeypatch):
    _install_fake_bge_m3_hybrid_model(monkeypatch)

    with enable_bge_m3_hybrid_shared_model_cache(clear_on_exit=True):
        first_provider = BgeM3HybridEmbeddingProvider()
        second_provider = BgeM3HybridEmbeddingProvider()

        first_provider.encode_query("sunflower query", provider_code="bge_m3_dense_sparse")
        second_provider.encode_query(
            "sunflower query",
            provider_code="bge_m3_dense_sparse_multivector",
        )

    assert len(_FakeBGEM3FlagModel.init_calls) == 1
    assert _FakeBGEM3FlagModel.init_calls[0]["model_name"] == "BAAI/bge-m3"
    assert len(_FakeBGEM3FlagModel.encode_calls) == 2
    assert _FakeBGEM3FlagModel.encode_calls[0]["return_colbert_vecs"] is False
    assert _FakeBGEM3FlagModel.encode_calls[1]["return_colbert_vecs"] is True


def test_real_question_eval_execution_mode_defaults_to_fake_eval_when_no_manual_real_signals_are_present():
    execution_mode, use_real_local_models, incremental_real_providers = resolve_real_question_eval_execution_mode(
        cli_use_real_local_models=False,
        env_use_real_local_models=None,
    )

    assert execution_mode == "fake_eval"
    assert use_real_local_models is False
    assert incremental_real_providers is None


def test_real_question_eval_execution_mode_requires_both_cli_flag_and_env_var_for_real_eval():
    execution_mode, use_real_local_models, incremental_real_providers = resolve_real_question_eval_execution_mode(
        cli_use_real_local_models=True,
        env_use_real_local_models="1",
    )

    assert execution_mode == "real_eval"
    assert use_real_local_models is True
    assert incremental_real_providers is None


def test_incremental_real_question_eval_execution_mode_requires_env_var_and_explicit_provider_list():
    execution_mode, use_real_local_models, incremental_real_providers = resolve_real_question_eval_execution_mode(
        cli_use_real_local_models=False,
        env_use_real_local_models="1",
        incremental_real_providers_raw="paraphrase_multilingual_mpnet_base_v2,multilingual_e5_base",
    )

    assert execution_mode == "incremental_real_eval"
    assert use_real_local_models is True
    assert incremental_real_providers == [
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
    ]


def test_real_question_eval_execution_mode_fails_fast_when_only_cli_flag_is_present():
    try:
        resolve_real_question_eval_execution_mode(
            cli_use_real_local_models=True,
            env_use_real_local_models=None,
        )
    except ValueError as exc:
        assert "requires BOTH --use-real-local-models and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1" in str(exc)
    else:
        raise AssertionError("Expected ValueError when only CLI flag is present")


def test_real_question_eval_execution_mode_fails_fast_when_only_env_var_is_present():
    try:
        resolve_real_question_eval_execution_mode(
            cli_use_real_local_models=False,
            env_use_real_local_models="1",
        )
    except ValueError as exc:
        assert "requires BOTH signals" in str(exc)
    else:
        raise AssertionError("Expected ValueError when only env var is present")


def test_incremental_real_question_eval_execution_mode_fails_fast_without_env_var():
    try:
        resolve_real_question_eval_execution_mode(
            cli_use_real_local_models=False,
            env_use_real_local_models=None,
            incremental_real_providers_raw="paraphrase_multilingual_mpnet_base_v2,multilingual_e5_base",
        )
    except ValueError as exc:
        assert "requires REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1" in str(exc)
    else:
        raise AssertionError("Expected ValueError when incremental real providers are provided without env var")


def test_incremental_real_question_eval_execution_mode_rejects_historical_providers():
    try:
        resolve_real_question_eval_execution_mode(
            cli_use_real_local_models=False,
            env_use_real_local_models="1",
            incremental_real_providers_raw="multilingual_e5_small,multilingual_e5_base",
        )
    except ValueError as exc:
        assert "must not rerun historical providers" in str(exc)
    else:
        raise AssertionError("Expected ValueError when historical providers are included in incremental mode")


def test_full_version_batch_a_requires_both_cli_flag_and_env_var_and_exact_large_provider_list():
    provider_codes = resolve_full_version_batch_a_providers(
        cli_use_real_local_models=True,
        env_use_real_local_models="1",
        full_version_batch_a_providers_raw="multilingual_e5_large",
    )

    assert provider_codes == ["multilingual_e5_large"]


def test_full_version_batch_a_fails_fast_without_both_manual_real_signals():
    try:
        resolve_full_version_batch_a_providers(
            cli_use_real_local_models=False,
            env_use_real_local_models="1",
            full_version_batch_a_providers_raw="multilingual_e5_large",
        )
    except ValueError as exc:
        assert "requires BOTH --use-real-local-models and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1" in str(exc)
    else:
        raise AssertionError("Expected ValueError when Batch A is requested without both manual real signals")


def test_full_version_batch_a_rejects_any_provider_list_other_than_multilingual_e5_large():
    try:
        resolve_full_version_batch_a_providers(
            cli_use_real_local_models=True,
            env_use_real_local_models="1",
            full_version_batch_a_providers_raw="multilingual_e5_base,multilingual_e5_large",
        )
    except ValueError as exc:
        assert "requires the explicit provider list: multilingual_e5_large" in str(exc)
    else:
        raise AssertionError("Expected ValueError when Batch A provider list includes anything other than multilingual_e5_large")


def test_full_version_batch_b_cli_path_is_closed_and_refuses_qwen_reruns():
    try:
        resolve_full_version_batch_b_providers(
            cli_use_real_local_models=True,
            env_use_real_local_models="1",
            full_version_batch_b_providers_raw="qwen3_embedding_0_6b",
            rerun_attempted_full_version_batch_b=False,
        )
    except ValueError as exc:
        assert "--rerun-attempted-full-version-batch-b" in str(exc)
    else:
        raise AssertionError("Expected ValueError when Batch B rerun is requested")


def test_full_version_batch_b_accepts_explicit_guarded_rerun_for_qwen():
    provider_codes = resolve_full_version_batch_b_providers(
        cli_use_real_local_models=True,
        env_use_real_local_models="1",
        full_version_batch_b_providers_raw="qwen3_embedding_0_6b",
        rerun_attempted_full_version_batch_b=True,
    )

    assert provider_codes == ["qwen3_embedding_0_6b"]


def test_full_version_batch_c_requires_both_cli_flag_and_env_var_and_exact_jina_provider_list():
    provider_codes = resolve_full_version_batch_c_providers(
        cli_use_real_local_models=True,
        env_use_real_local_models="1",
        full_version_batch_c_providers_raw="jina_embeddings_v3",
    )

    assert provider_codes == ["jina_embeddings_v3"]


def test_full_version_batch_c_fails_fast_without_both_manual_real_signals():
    try:
        resolve_full_version_batch_c_providers(
            cli_use_real_local_models=False,
            env_use_real_local_models="1",
            full_version_batch_c_providers_raw="jina_embeddings_v3",
        )
    except ValueError as exc:
        assert "requires BOTH --use-real-local-models and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1" in str(exc)
    else:
        raise AssertionError("Expected ValueError when Batch C is requested without both manual real signals")


def test_full_version_batch_c_rejects_any_provider_list_other_than_jina_embeddings_v3():
    try:
        resolve_full_version_batch_c_providers(
            cli_use_real_local_models=True,
            env_use_real_local_models="1",
            full_version_batch_c_providers_raw="qwen3_embedding_0_6b",
        )
    except ValueError as exc:
        assert "requires the explicit provider list: jina_embeddings_v3" in str(exc)
    else:
        raise AssertionError("Expected ValueError when Batch C provider list includes anything other than jina_embeddings_v3")


def test_full_version_batch_d_requires_both_cli_flag_and_env_var_and_exact_bge_hybrid_provider_list():
    provider_codes = resolve_full_version_batch_d_providers(
        cli_use_real_local_models=True,
        env_use_real_local_models="1",
        full_version_batch_d_providers_raw="bge_m3_dense_sparse,bge_m3_dense_sparse_multivector",
    )

    assert provider_codes == [
        "bge_m3_dense_sparse",
        "bge_m3_dense_sparse_multivector",
    ]


def test_full_version_batch_d_fails_fast_without_both_manual_real_signals():
    try:
        resolve_full_version_batch_d_providers(
            cli_use_real_local_models=False,
            env_use_real_local_models="1",
            full_version_batch_d_providers_raw="bge_m3_dense_sparse,bge_m3_dense_sparse_multivector",
        )
    except ValueError as exc:
        assert "requires BOTH --use-real-local-models and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1" in str(exc)
    else:
        raise AssertionError("Expected ValueError when Batch D is requested without both manual real signals")


def test_full_version_batch_d_rejects_any_provider_list_other_than_the_two_bge_hybrid_modes():
    try:
        resolve_full_version_batch_d_providers(
            cli_use_real_local_models=True,
            env_use_real_local_models="1",
            full_version_batch_d_providers_raw="bge_m3_dense_sparse,qwen3_embedding_0_6b",
        )
    except ValueError as exc:
        assert "requires the explicit provider list" in str(exc)
    else:
        raise AssertionError("Expected ValueError when Batch D provider list includes anything other than the approved BGE hybrid modes")


def test_incremental_real_question_eval_writes_incremental_artifacts_and_preserves_exact_question_ids(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    _install_fake_real_sentence_transformers(monkeypatch)

    repo_artifact_dir = Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval"
    source_latest_real_json = repo_artifact_dir / "latest_real" / "real_question_eval_result.json"
    source_latest_real_markdown = repo_artifact_dir / "latest_real" / "real_question_eval_report.md"

    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_real_dir = artifact_dir / "latest_real"
    latest_real_dir.mkdir(parents=True, exist_ok=True)
    latest_real_json = latest_real_dir / "real_question_eval_result.json"
    latest_real_markdown = latest_real_dir / "real_question_eval_report.md"
    latest_real_json.write_text(source_latest_real_json.read_text(encoding="utf-8"), encoding="utf-8")
    latest_real_markdown.write_text(source_latest_real_markdown.read_text(encoding="utf-8"), encoding="utf-8")
    latest_real_json_before = latest_real_json.read_text(encoding="utf-8")
    latest_real_markdown_before = latest_real_markdown.read_text(encoding="utf-8")

    db, session_generator = _get_test_db_session()
    try:
        result = run_incremental_real_question_eval(
            db,
            RealQuestionEvalConfig(
                artifact_dir=artifact_dir,
                use_real_local_models=True,
                candidate_model_codes=[
                    "paraphrase_multilingual_mpnet_base_v2",
                    "multilingual_e5_base",
                ],
            ),
        )
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is False
    assert result.run_type == "incremental_real"
    assert result.execution_mode == "incremental_real_eval"
    assert result.historical_providers == ["multilingual_e5_small", "bge_m3"]
    assert result.new_real_providers == [
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
    ]
    assert result.artifact_paths.latest_markdown_report is not None
    assert "latest_incremental_new_providers" in result.artifact_paths.latest_markdown_report
    assert result.artifact_paths.archived_markdown_report is not None
    assert "_incremental_new_providers" in result.artifact_paths.archived_markdown_report
    assert result.artifact_paths.archived_markdown_report.endswith("real_question_eval_report.md")
    assert [item.question_id for item in result.question_results] == [
        "question-sunflower-house",
        "question-winter-trip",
        "question-grandmother-soup",
    ]
    assert latest_real_json.read_text(encoding="utf-8") == latest_real_json_before
    assert latest_real_markdown.read_text(encoding="utf-8") == latest_real_markdown_before

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["execution_mode"] == "incremental_real_eval"
    assert latest_json_payload["run_type"] == "incremental_real"
    assert latest_json_payload["used_fake_models"] is False
    assert latest_json_payload["historical_providers"] == ["multilingual_e5_small", "bge_m3"]
    assert latest_json_payload["new_real_providers"] == [
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_base",
    ]
    assert latest_json_payload["client_view"]["questions"][0]["question_id"] == "question-sunflower-house"
    assert latest_json_payload["client_view"]["questions"][1]["question_id"] == "question-winter-trip"
    assert latest_json_payload["client_view"]["questions"][2]["question_id"] == "question-grandmother-soup"


def test_full_version_batch_a_writes_separate_artifacts_and_compares_only_baseline_and_e5_large(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    _install_fake_real_sentence_transformers(monkeypatch)

    repo_artifact_dir = Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval"
    source_incremental_json = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_result.json"
    )
    source_incremental_markdown = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_report.md"
    )

    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_incremental_dir = artifact_dir / "latest_incremental_new_providers"
    latest_incremental_dir.mkdir(parents=True, exist_ok=True)
    latest_incremental_json = latest_incremental_dir / "real_question_eval_result.json"
    latest_incremental_markdown = latest_incremental_dir / "real_question_eval_report.md"
    latest_incremental_json.write_text(source_incremental_json.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_markdown.write_text(source_incremental_markdown.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_json_before = latest_incremental_json.read_text(encoding="utf-8")
    latest_incremental_markdown_before = latest_incremental_markdown.read_text(encoding="utf-8")

    latest_real_dir = artifact_dir / "latest_real"
    latest_real_dir.mkdir(parents=True, exist_ok=True)
    latest_real_markdown = latest_real_dir / "real_question_eval_report.md"
    latest_real_json = latest_real_dir / "real_question_eval_result.json"
    latest_real_markdown.write_text("keep-real-batch-a\n", encoding="utf-8")
    latest_real_json.write_text('{"run_type":"real"}\n', encoding="utf-8")

    latest_fake_dir = artifact_dir / "latest_fake"
    latest_fake_dir.mkdir(parents=True, exist_ok=True)
    latest_fake_markdown = latest_fake_dir / "real_question_eval_report.md"
    latest_fake_json = latest_fake_dir / "real_question_eval_result.json"
    latest_fake_markdown.write_text("keep-fake-batch-a\n", encoding="utf-8")
    latest_fake_json.write_text('{"run_type":"fake"}\n', encoding="utf-8")

    db, session_generator = _get_test_db_session()
    try:
        result = run_full_version_batch_a_question_eval(
            db,
            RealQuestionEvalConfig(
                artifact_dir=artifact_dir,
                use_real_local_models=True,
                candidate_model_codes=["multilingual_e5_large"],
                run_type_override="full_version_batch_a",
                execution_mode_override="full_version_batch_a_real_eval",
            ),
        )
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is False
    assert result.run_type == "full_version_batch_a"
    assert result.execution_mode == "full_version_batch_a_real_eval"
    assert result.benchmark_batch_label == "Batch A"
    assert result.baseline_provider_codes == ["multilingual_e5_base"]
    assert result.newly_evaluated_provider_codes == ["multilingual_e5_large"]
    assert result.compared_models == ["multilingual_e5_base", "multilingual_e5_large"]
    assert result.excluded_provider_codes == [
        "multilingual_e5_small",
        "bge_m3",
        "paraphrase_multilingual_mpnet_base_v2",
    ]
    assert [item.question_id for item in result.question_results] == [
        "question-sunflower-house",
        "question-winter-trip",
        "question-grandmother-soup",
    ]
    assert "latest_full_version_batch_a" in result.artifact_paths.latest_markdown_report
    assert "_full_version_batch_a" in result.artifact_paths.archived_markdown_report

    assert latest_incremental_json.read_text(encoding="utf-8") == latest_incremental_json_before
    assert latest_incremental_markdown.read_text(encoding="utf-8") == latest_incremental_markdown_before
    assert latest_real_markdown.read_text(encoding="utf-8") == "keep-real-batch-a\n"
    assert latest_real_json.read_text(encoding="utf-8") == '{"run_type":"real"}\n'
    assert latest_fake_markdown.read_text(encoding="utf-8") == "keep-fake-batch-a\n"
    assert latest_fake_json.read_text(encoding="utf-8") == '{"run_type":"fake"}\n'

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["execution_mode"] == "full_version_batch_a_real_eval"
    assert latest_json_payload["run_type"] == "full_version_batch_a"
    assert latest_json_payload["baseline_provider_codes"] == ["multilingual_e5_base"]
    assert latest_json_payload["newly_evaluated_provider_codes"] == ["multilingual_e5_large"]
    assert latest_json_payload["client_view"]["baseline_provider_codes"] == ["multilingual_e5_base"]
    assert latest_json_payload["client_view"]["newly_evaluated_provider_codes"] == ["multilingual_e5_large"]
    assert latest_json_payload["client_view"]["questions"][0]["question_id"] == "question-sunflower-house"
    assert latest_json_payload["client_view"]["questions"][1]["question_id"] == "question-winter-trip"
    assert latest_json_payload["client_view"]["questions"][2]["question_id"] == "question-grandmother-soup"
    assert latest_json_payload["developer_view"]["models_compared"] == [
        "multilingual_e5_base",
        "multilingual_e5_large",
    ]
    assert {
        item["model_code"] for item in latest_json_payload["developer_view"]["aggregate_results"]
    } == {"multilingual_e5_base", "multilingual_e5_large"}

    markdown_text = Path(result.artifact_paths.latest_markdown_report).read_text(encoding="utf-8")
    assert "## Technical Summary" in markdown_text
    assert "## Dataset Questions Used" in markdown_text
    assert "## Baseline Provider" in markdown_text
    assert "## Newly Evaluated Providers" in markdown_text
    assert "## Per-Question Result Comparison" in markdown_text
    assert "## Aggregate Metrics" in markdown_text
    assert "## Winner" in markdown_text
    assert "## Recommendation" in markdown_text
    assert "## Safety Notes" in markdown_text
    assert "multilingual_e5_base" in markdown_text
    assert "multilingual_e5_large" in markdown_text
    assert "#### multilingual_e5_small" not in markdown_text
    assert "#### bge_m3" not in markdown_text
    assert "#### paraphrase_multilingual_mpnet_base_v2" not in markdown_text


def test_full_version_batch_b_writes_attempted_artifact_without_running_qwen(
    monkeypatch,
    tmp_path,
):
    repo_artifact_dir = Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval"
    source_incremental_json = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_result.json"
    )
    source_incremental_markdown = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_report.md"
    )

    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_incremental_dir = artifact_dir / "latest_incremental_new_providers"
    latest_incremental_dir.mkdir(parents=True, exist_ok=True)
    latest_incremental_json = latest_incremental_dir / "real_question_eval_result.json"
    latest_incremental_markdown = latest_incremental_dir / "real_question_eval_report.md"
    latest_incremental_json.write_text(source_incremental_json.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_markdown.write_text(source_incremental_markdown.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_json_before = latest_incremental_json.read_text(encoding="utf-8")
    latest_incremental_markdown_before = latest_incremental_markdown.read_text(encoding="utf-8")

    latest_real_dir = artifact_dir / "latest_real"
    latest_real_dir.mkdir(parents=True, exist_ok=True)
    latest_real_markdown = latest_real_dir / "real_question_eval_report.md"
    latest_real_json = latest_real_dir / "real_question_eval_result.json"
    latest_real_markdown.write_text("keep-real-batch-b\n", encoding="utf-8")
    latest_real_json.write_text('{"run_type":"real"}\n', encoding="utf-8")

    latest_fake_dir = artifact_dir / "latest_fake"
    latest_fake_dir.mkdir(parents=True, exist_ok=True)
    latest_fake_markdown = latest_fake_dir / "real_question_eval_report.md"
    latest_fake_json = latest_fake_dir / "real_question_eval_result.json"
    latest_fake_markdown.write_text("keep-fake-batch-b\n", encoding="utf-8")
    latest_fake_json.write_text('{"run_type":"fake"}\n', encoding="utf-8")

    latest_batch_a_dir = artifact_dir / "latest_full_version_batch_a"
    latest_batch_a_dir.mkdir(parents=True, exist_ok=True)
    latest_batch_a_markdown = latest_batch_a_dir / "real_question_eval_report.md"
    latest_batch_a_json = latest_batch_a_dir / "real_question_eval_result.json"
    latest_batch_a_markdown.write_text("keep-batch-a\n", encoding="utf-8")
    latest_batch_a_json.write_text('{"run_type":"full_version_batch_a"}\n', encoding="utf-8")

    runner_called = {"value": False}

    def fail_runner(*args, **kwargs):
        runner_called["value"] = True
        raise AssertionError("Qwen Batch B should not invoke the runner anymore")

    monkeypatch.setattr(
        "app.modules.real_question_eval.service.RealQuestionEvalRunner.run",
        fail_runner,
    )

    result = run_full_version_batch_b_question_eval(
        None,
        RealQuestionEvalConfig(
            artifact_dir=artifact_dir,
            use_real_local_models=True,
            candidate_model_codes=["qwen3_embedding_0_6b"],
            run_type_override="full_version_batch_b",
            execution_mode_override="full_version_batch_b_real_eval",
            rerun_attempted_full_version_batch_b=False,
        ),
    )

    assert runner_called["value"] is False
    assert result.passed is False
    assert result.used_fake_models is False
    assert result.run_type == "full_version_batch_b_attempted"
    assert result.execution_mode == "full_version_batch_b_attempted"
    assert result.benchmark_batch_label == "Batch B Attempted"
    assert result.benchmark_status == "attempted_not_completed"
    assert result.incomplete_reason is not None
    assert result.baseline_provider_codes == ["multilingual_e5_base"]
    assert result.newly_evaluated_provider_codes == ["qwen3_embedding_0_6b"]
    assert result.compared_models == ["multilingual_e5_base", "qwen3_embedding_0_6b"]
    assert result.overall_winner_model_code is None
    assert "latest_full_version_batch_b_attempted" in result.artifact_paths.latest_markdown_report
    assert "_full_version_batch_b_attempted" in result.artifact_paths.archived_markdown_report

    assert latest_incremental_json.read_text(encoding="utf-8") == latest_incremental_json_before
    assert latest_incremental_markdown.read_text(encoding="utf-8") == latest_incremental_markdown_before
    assert latest_real_markdown.read_text(encoding="utf-8") == "keep-real-batch-b\n"
    assert latest_real_json.read_text(encoding="utf-8") == '{"run_type":"real"}\n'
    assert latest_fake_markdown.read_text(encoding="utf-8") == "keep-fake-batch-b\n"
    assert latest_fake_json.read_text(encoding="utf-8") == '{"run_type":"fake"}\n'
    assert latest_batch_a_markdown.read_text(encoding="utf-8") == "keep-batch-a\n"
    assert latest_batch_a_json.read_text(encoding="utf-8") == '{"run_type":"full_version_batch_a"}\n'

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["execution_mode"] == "full_version_batch_b_attempted"
    assert latest_json_payload["run_type"] == "full_version_batch_b_attempted"
    assert latest_json_payload["benchmark_status"] == "attempted_not_completed"
    assert latest_json_payload["used_fake_models"] is False
    assert latest_json_payload["client_view"]["benchmark_status"] == "attempted_not_completed"
    assert latest_json_payload["client_view"]["recommended_active_model"] == "multilingual_e5_base"
    assert latest_json_payload["developer_view"]["models_compared"] == [
        "multilingual_e5_base",
        "qwen3_embedding_0_6b",
    ]

    markdown_text = Path(result.artifact_paths.latest_markdown_report).read_text(encoding="utf-8")
    assert "## Technical Summary" in markdown_text
    assert "Benchmark status: `attempted_not_completed`" in markdown_text
    assert "`multilingual_e5_base`" in markdown_text
    assert "production recommendation" in markdown_text.lower()
    assert "Qwen3 0.6B benchmark attempted but not completed in this environment." in markdown_text


def test_full_version_batch_b_rerun_writes_separate_artifacts_and_compares_only_baseline_and_qwen(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    _install_fake_real_sentence_transformers(monkeypatch)

    repo_artifact_dir = Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval"
    source_incremental_json = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_result.json"
    )
    source_incremental_markdown = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_report.md"
    )

    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_incremental_dir = artifact_dir / "latest_incremental_new_providers"
    latest_incremental_dir.mkdir(parents=True, exist_ok=True)
    latest_incremental_json = latest_incremental_dir / "real_question_eval_result.json"
    latest_incremental_markdown = latest_incremental_dir / "real_question_eval_report.md"
    latest_incremental_json.write_text(source_incremental_json.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_markdown.write_text(source_incremental_markdown.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_json_before = latest_incremental_json.read_text(encoding="utf-8")
    latest_incremental_markdown_before = latest_incremental_markdown.read_text(encoding="utf-8")

    latest_real_dir = artifact_dir / "latest_real"
    latest_real_dir.mkdir(parents=True, exist_ok=True)
    latest_real_markdown = latest_real_dir / "real_question_eval_report.md"
    latest_real_json = latest_real_dir / "real_question_eval_result.json"
    latest_real_markdown.write_text("keep-real-batch-b-rerun\n", encoding="utf-8")
    latest_real_json.write_text('{"run_type":"real"}\n', encoding="utf-8")

    latest_fake_dir = artifact_dir / "latest_fake"
    latest_fake_dir.mkdir(parents=True, exist_ok=True)
    latest_fake_markdown = latest_fake_dir / "real_question_eval_report.md"
    latest_fake_json = latest_fake_dir / "real_question_eval_result.json"
    latest_fake_markdown.write_text("keep-fake-batch-b-rerun\n", encoding="utf-8")
    latest_fake_json.write_text('{"run_type":"fake"}\n', encoding="utf-8")

    latest_batch_a_dir = artifact_dir / "latest_full_version_batch_a"
    latest_batch_a_dir.mkdir(parents=True, exist_ok=True)
    latest_batch_a_markdown = latest_batch_a_dir / "real_question_eval_report.md"
    latest_batch_a_json = latest_batch_a_dir / "real_question_eval_result.json"
    latest_batch_a_markdown.write_text("keep-batch-a\n", encoding="utf-8")
    latest_batch_a_json.write_text('{"run_type":"full_version_batch_a"}\n', encoding="utf-8")

    latest_batch_c_dir = artifact_dir / "latest_full_version_batch_c"
    latest_batch_c_dir.mkdir(parents=True, exist_ok=True)
    latest_batch_c_markdown = latest_batch_c_dir / "real_question_eval_report.md"
    latest_batch_c_json = latest_batch_c_dir / "real_question_eval_result.json"
    latest_batch_c_markdown.write_text("keep-batch-c\n", encoding="utf-8")
    latest_batch_c_json.write_text('{"run_type":"full_version_batch_c"}\n', encoding="utf-8")

    db, session_generator = _get_test_db_session()
    try:
        result = run_full_version_batch_b_question_eval(
            db,
            RealQuestionEvalConfig(
                artifact_dir=artifact_dir,
                use_real_local_models=True,
                candidate_model_codes=["qwen3_embedding_0_6b"],
                run_type_override="full_version_batch_b",
                execution_mode_override="full_version_batch_b_real_eval",
                rerun_attempted_full_version_batch_b=True,
            ),
        )
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is False
    assert result.run_type == "full_version_batch_b"
    assert result.execution_mode == "full_version_batch_b_real_eval"
    assert result.benchmark_batch_label == "Batch B"
    assert result.benchmark_status == "completed"
    assert result.baseline_provider_codes == ["multilingual_e5_base"]
    assert result.newly_evaluated_provider_codes == ["qwen3_embedding_0_6b"]
    assert result.compared_models == ["multilingual_e5_base", "qwen3_embedding_0_6b"]
    assert result.excluded_provider_codes == [
        "multilingual_e5_small",
        "bge_m3",
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_large",
        "jina_embeddings_v3",
        "qwen3_embedding_4b",
        "qwen3_embedding_8b",
    ]
    assert [item.question_id for item in result.question_results] == [
        "question-sunflower-house",
        "question-winter-trip",
        "question-grandmother-soup",
    ]
    assert "latest_full_version_batch_b" in result.artifact_paths.latest_markdown_report
    assert "_full_version_batch_b" in result.artifact_paths.archived_markdown_report

    assert latest_incremental_json.read_text(encoding="utf-8") == latest_incremental_json_before
    assert latest_incremental_markdown.read_text(encoding="utf-8") == latest_incremental_markdown_before
    assert latest_real_markdown.read_text(encoding="utf-8") == "keep-real-batch-b-rerun\n"
    assert latest_real_json.read_text(encoding="utf-8") == '{"run_type":"real"}\n'
    assert latest_fake_markdown.read_text(encoding="utf-8") == "keep-fake-batch-b-rerun\n"
    assert latest_fake_json.read_text(encoding="utf-8") == '{"run_type":"fake"}\n'
    assert latest_batch_a_markdown.read_text(encoding="utf-8") == "keep-batch-a\n"
    assert latest_batch_a_json.read_text(encoding="utf-8") == '{"run_type":"full_version_batch_a"}\n'
    assert latest_batch_c_markdown.read_text(encoding="utf-8") == "keep-batch-c\n"
    assert latest_batch_c_json.read_text(encoding="utf-8") == '{"run_type":"full_version_batch_c"}\n'

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["execution_mode"] == "full_version_batch_b_real_eval"
    assert latest_json_payload["run_type"] == "full_version_batch_b"
    assert latest_json_payload["benchmark_status"] == "completed"
    assert latest_json_payload["baseline_provider_codes"] == ["multilingual_e5_base"]
    assert latest_json_payload["newly_evaluated_provider_codes"] == ["qwen3_embedding_0_6b"]
    assert latest_json_payload["client_view"]["baseline_provider_codes"] == ["multilingual_e5_base"]
    assert latest_json_payload["client_view"]["newly_evaluated_provider_codes"] == ["qwen3_embedding_0_6b"]
    assert latest_json_payload["developer_view"]["models_compared"] == [
        "multilingual_e5_base",
        "qwen3_embedding_0_6b",
    ]
    assert latest_json_payload["client_view"]["non_compared_notes"] == [
        "Jina Embeddings v3 was not rerun and is not compared in Batch B.",
    ]
    assert {
        item["model_code"] for item in latest_json_payload["developer_view"]["aggregate_results"]
    } == {"multilingual_e5_base", "qwen3_embedding_0_6b"}

    markdown_text = Path(result.artifact_paths.latest_markdown_report).read_text(encoding="utf-8")
    assert "## Technical Summary" in markdown_text
    assert "## Dataset Questions Used" in markdown_text
    assert "## Baseline Provider" in markdown_text
    assert "## Newly Evaluated Providers" in markdown_text
    assert "## Per-Question Result Comparison" in markdown_text
    assert "## Aggregate Metrics" in markdown_text
    assert "## Winner" in markdown_text
    assert "## Recommendation" in markdown_text
    assert "## Safety Notes" in markdown_text
    assert "multilingual_e5_base" in markdown_text
    assert "qwen3_embedding_0_6b" in markdown_text
    assert "Jina Embeddings v3 was not rerun and is not compared in Batch B." in markdown_text
    assert "#### multilingual_e5_small" not in markdown_text
    assert "#### bge_m3" not in markdown_text
    assert "#### paraphrase_multilingual_mpnet_base_v2" not in markdown_text
    assert "#### multilingual_e5_large" not in markdown_text
    assert "#### jina_embeddings_v3" not in markdown_text


def test_full_version_batch_c_writes_separate_artifacts_and_compares_only_baseline_and_jina(
    client,
    monkeypatch,
    tmp_path,
):
    _install_fake_qdrant_client(monkeypatch)
    _install_fake_real_sentence_transformers(monkeypatch)

    repo_artifact_dir = Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval"
    source_incremental_json = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_result.json"
    )
    source_incremental_markdown = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_report.md"
    )

    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_incremental_dir = artifact_dir / "latest_incremental_new_providers"
    latest_incremental_dir.mkdir(parents=True, exist_ok=True)
    latest_incremental_json = latest_incremental_dir / "real_question_eval_result.json"
    latest_incremental_markdown = latest_incremental_dir / "real_question_eval_report.md"
    latest_incremental_json.write_text(source_incremental_json.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_markdown.write_text(source_incremental_markdown.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_json_before = latest_incremental_json.read_text(encoding="utf-8")
    latest_incremental_markdown_before = latest_incremental_markdown.read_text(encoding="utf-8")

    latest_real_dir = artifact_dir / "latest_real"
    latest_real_dir.mkdir(parents=True, exist_ok=True)
    latest_real_markdown = latest_real_dir / "real_question_eval_report.md"
    latest_real_json = latest_real_dir / "real_question_eval_result.json"
    latest_real_markdown.write_text("keep-real-batch-c\n", encoding="utf-8")
    latest_real_json.write_text('{"run_type":"real"}\n', encoding="utf-8")

    latest_fake_dir = artifact_dir / "latest_fake"
    latest_fake_dir.mkdir(parents=True, exist_ok=True)
    latest_fake_markdown = latest_fake_dir / "real_question_eval_report.md"
    latest_fake_json = latest_fake_dir / "real_question_eval_result.json"
    latest_fake_markdown.write_text("keep-fake-batch-c\n", encoding="utf-8")
    latest_fake_json.write_text('{"run_type":"fake"}\n', encoding="utf-8")

    latest_batch_a_dir = artifact_dir / "latest_full_version_batch_a"
    latest_batch_a_dir.mkdir(parents=True, exist_ok=True)
    latest_batch_a_markdown = latest_batch_a_dir / "real_question_eval_report.md"
    latest_batch_a_json = latest_batch_a_dir / "real_question_eval_result.json"
    latest_batch_a_markdown.write_text("keep-batch-a\n", encoding="utf-8")
    latest_batch_a_json.write_text('{"run_type":"full_version_batch_a"}\n', encoding="utf-8")

    db, session_generator = _get_test_db_session()
    try:
        result = run_full_version_batch_c_question_eval(
            db,
            RealQuestionEvalConfig(
                artifact_dir=artifact_dir,
                use_real_local_models=True,
                candidate_model_codes=["jina_embeddings_v3"],
                run_type_override="full_version_batch_c",
                execution_mode_override="full_version_batch_c_real_eval",
            ),
        )
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is False
    assert result.run_type == "full_version_batch_c"
    assert result.execution_mode == "full_version_batch_c_real_eval"
    assert result.benchmark_batch_label == "Batch C"
    assert result.benchmark_status == "completed"
    assert result.baseline_provider_codes == ["multilingual_e5_base"]
    assert result.newly_evaluated_provider_codes == ["jina_embeddings_v3"]
    assert result.compared_models == ["multilingual_e5_base", "jina_embeddings_v3"]
    assert result.excluded_provider_codes == [
        "multilingual_e5_small",
        "bge_m3",
        "paraphrase_multilingual_mpnet_base_v2",
        "multilingual_e5_large",
        "qwen3_embedding_0_6b",
        "qwen3_embedding_4b",
        "qwen3_embedding_8b",
    ]
    assert [item.question_id for item in result.question_results] == [
        "question-sunflower-house",
        "question-winter-trip",
        "question-grandmother-soup",
    ]
    assert "latest_full_version_batch_c" in result.artifact_paths.latest_markdown_report
    assert "_full_version_batch_c" in result.artifact_paths.archived_markdown_report

    assert latest_incremental_json.read_text(encoding="utf-8") == latest_incremental_json_before
    assert latest_incremental_markdown.read_text(encoding="utf-8") == latest_incremental_markdown_before
    assert latest_real_markdown.read_text(encoding="utf-8") == "keep-real-batch-c\n"
    assert latest_real_json.read_text(encoding="utf-8") == '{"run_type":"real"}\n'
    assert latest_fake_markdown.read_text(encoding="utf-8") == "keep-fake-batch-c\n"
    assert latest_fake_json.read_text(encoding="utf-8") == '{"run_type":"fake"}\n'
    assert latest_batch_a_markdown.read_text(encoding="utf-8") == "keep-batch-a\n"
    assert latest_batch_a_json.read_text(encoding="utf-8") == '{"run_type":"full_version_batch_a"}\n'

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["execution_mode"] == "full_version_batch_c_real_eval"
    assert latest_json_payload["run_type"] == "full_version_batch_c"
    assert latest_json_payload["benchmark_status"] == "completed"
    assert latest_json_payload["baseline_provider_codes"] == ["multilingual_e5_base"]
    assert latest_json_payload["newly_evaluated_provider_codes"] == ["jina_embeddings_v3"]
    assert latest_json_payload["client_view"]["baseline_provider_codes"] == ["multilingual_e5_base"]
    assert latest_json_payload["client_view"]["newly_evaluated_provider_codes"] == ["jina_embeddings_v3"]
    assert latest_json_payload["client_view"]["questions"][0]["question_id"] == "question-sunflower-house"
    assert latest_json_payload["client_view"]["questions"][1]["question_id"] == "question-winter-trip"
    assert latest_json_payload["client_view"]["questions"][2]["question_id"] == "question-grandmother-soup"
    assert latest_json_payload["developer_view"]["models_compared"] == [
        "multilingual_e5_base",
        "jina_embeddings_v3",
    ]
    assert {
        item["model_code"] for item in latest_json_payload["developer_view"]["aggregate_results"]
    } == {"multilingual_e5_base", "jina_embeddings_v3"}
    assert latest_json_payload["client_view"]["non_compared_notes"] == [
        "Qwen3 0.6B was skipped as attempted/not completed and is not compared in Batch C.",
    ]

    markdown_text = Path(result.artifact_paths.latest_markdown_report).read_text(encoding="utf-8")
    assert "## Technical Summary" in markdown_text
    assert "## Dataset Questions Used" in markdown_text
    assert "## Baseline Provider" in markdown_text
    assert "## Newly Evaluated Providers" in markdown_text
    assert "## Per-Question Result Comparison" in markdown_text
    assert "## Aggregate Metrics" in markdown_text
    assert "## Winner" in markdown_text
    assert "## Recommendation" in markdown_text
    assert "## Safety Notes" in markdown_text
    assert "multilingual_e5_base" in markdown_text
    assert "jina_embeddings_v3" in markdown_text
    assert "Qwen3 0.6B was skipped as attempted/not completed and is not compared in Batch C." in markdown_text
    assert "#### multilingual_e5_small" not in markdown_text
    assert "#### bge_m3" not in markdown_text
    assert "#### paraphrase_multilingual_mpnet_base_v2" not in markdown_text
    assert "#### multilingual_e5_large" not in markdown_text
    assert "#### qwen3_embedding_0_6b" not in markdown_text


def test_full_version_batch_d_writes_separate_artifacts_and_compares_only_baseline_and_bge_hybrid_modes(
    client,
    monkeypatch,
    tmp_path,
):
    repo_artifact_dir = Path(__file__).resolve().parents[1] / "artifacts" / "real_question_eval"
    source_incremental_json = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_result.json"
    )
    source_incremental_markdown = (
        repo_artifact_dir / "latest_incremental_new_providers" / "real_question_eval_report.md"
    )

    def fake_batch_d_manual_provider_result(
        *,
        profile_id: int,
        provider_code: str,
        source_chunks,
        cases=None,
        top_k: int = 2,
    ):
        del profile_id, source_chunks, cases, top_k
        model_results_by_provider = {
            "bge_m3_dense_sparse": [
                ("question-sunflower-house", ["sunflower seeds", "blue gate latch"], [], [], 1.0, 1, True),
                ("question-winter-trip", ["overnight train ticket", "wooden thermos"], [], [], 1.0, 1, True),
                ("question-grandmother-soup", ["dried mushrooms"], ["oak stove"], [], 0.5, 1, False),
            ],
            "bge_m3_dense_sparse_multivector": [
                ("question-sunflower-house", ["sunflower seeds", "blue gate latch"], [], [], 1.0, 1, True),
                ("question-winter-trip", ["overnight train ticket", "wooden thermos"], [], [], 1.0, 1, True),
                ("question-grandmother-soup", ["dried mushrooms", "oak stove"], [], [], 1.0, 1, True),
            ],
        }
        collection_name = f"eternal_world_rag_chunks__{provider_code}__manual_local_batch_d"
        question_results = []
        aggregate_model_results = []
        for question_id, matched, missing, distractors, coverage, first_rank, passed in model_results_by_provider[provider_code]:
            model_result = RealQuestionEvalModelResult(
                model_code=provider_code,
                collection_name=collection_name,
                top_chunks=[],
                matched_expected_markers=matched,
                missing_expected_markers=missing,
                false_positive_markers=distractors,
                evidence_coverage=coverage,
                first_relevant_rank=first_rank,
                relevant_result_count=1,
                false_positive_count=len(distractors),
                answer_summary="manual batch d",
                groundedness_verdict="grounded" if passed else "partial",
                passed=passed,
                hit=True,
                reasons=[],
            )
            aggregate_model_results.append(model_result)
            question_results.append(
                RealQuestionEvalQuestionResult(
                    question_id=question_id,
                    question_text=question_id,
                    expected_markers=[],
                    forbidden_markers=[],
                    model_results=[model_result],
                    winner_model_code=provider_code,
                    winner_reason="Only one model result was available.",
                )
            )

        aggregate_result = RealQuestionEvalAggregateModelResult(
            model_code=provider_code,
            collection_name=collection_name,
            question_wins=0,
            average_evidence_coverage=round(
                sum((item.evidence_coverage or 0.0) for item in aggregate_model_results) / len(aggregate_model_results),
                4,
            ),
            average_first_relevant_rank=1.0,
            total_matched_markers=sum(len(item.matched_expected_markers) for item in aggregate_model_results),
            total_missing_markers=sum(len(item.missing_expected_markers) for item in aggregate_model_results),
            total_false_positive_markers=sum(len(item.false_positive_markers) for item in aggregate_model_results),
            passed_questions=sum(1 for item in aggregate_model_results if item.passed),
            official_metrics={
                "hit_rate": sum(1 for item in aggregate_model_results if item.passed) / len(aggregate_model_results),
                "recall_at_k": round(
                    sum((item.evidence_coverage or 0.0) for item in aggregate_model_results) / len(aggregate_model_results),
                    4,
                ),
                "mrr": 1.0,
                "forbidden_marker_rate": 0.0,
                "average_latency_ms": 12.0 if provider_code == "bge_m3_dense_sparse_multivector" else 9.0,
                "cost_estimate_total": None,
                "evidence_marker_coverage": round(
                    sum((item.evidence_coverage or 0.0) for item in aggregate_model_results) / len(aggregate_model_results),
                    4,
                ),
                "missing_expected_marker_count": sum(
                    len(item.missing_expected_markers) for item in aggregate_model_results
                ),
                "false_positive_count": 0,
            },
        )
        return question_results, aggregate_result

    monkeypatch.setattr(
        "app.modules.real_question_eval.service._build_batch_d_manual_provider_result",
        fake_batch_d_manual_provider_result,
    )

    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_incremental_dir = artifact_dir / "latest_incremental_new_providers"
    latest_incremental_dir.mkdir(parents=True, exist_ok=True)
    latest_incremental_json = latest_incremental_dir / "real_question_eval_result.json"
    latest_incremental_markdown = latest_incremental_dir / "real_question_eval_report.md"
    latest_incremental_json.write_text(source_incremental_json.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_markdown.write_text(source_incremental_markdown.read_text(encoding="utf-8"), encoding="utf-8")
    latest_incremental_json_before = latest_incremental_json.read_text(encoding="utf-8")
    latest_incremental_markdown_before = latest_incremental_markdown.read_text(encoding="utf-8")

    latest_real_dir = artifact_dir / "latest_real"
    latest_real_dir.mkdir(parents=True, exist_ok=True)
    latest_real_markdown = latest_real_dir / "real_question_eval_report.md"
    latest_real_json = latest_real_dir / "real_question_eval_result.json"
    latest_real_markdown.write_text("keep-real-batch-d\n", encoding="utf-8")
    latest_real_json.write_text('{"run_type":"real"}\n', encoding="utf-8")

    latest_fake_dir = artifact_dir / "latest_fake"
    latest_fake_dir.mkdir(parents=True, exist_ok=True)
    latest_fake_markdown = latest_fake_dir / "real_question_eval_report.md"
    latest_fake_json = latest_fake_dir / "real_question_eval_result.json"
    latest_fake_markdown.write_text("keep-fake-batch-d\n", encoding="utf-8")
    latest_fake_json.write_text('{"run_type":"fake"}\n', encoding="utf-8")

    latest_batch_b_dir = artifact_dir / "latest_full_version_batch_b"
    latest_batch_b_dir.mkdir(parents=True, exist_ok=True)
    latest_batch_b_markdown = latest_batch_b_dir / "real_question_eval_report.md"
    latest_batch_b_json = latest_batch_b_dir / "real_question_eval_result.json"
    latest_batch_b_markdown.write_text("keep-batch-b\n", encoding="utf-8")
    latest_batch_b_json.write_text('{"run_type":"full_version_batch_b"}\n', encoding="utf-8")

    latest_batch_c_dir = artifact_dir / "latest_full_version_batch_c"
    latest_batch_c_dir.mkdir(parents=True, exist_ok=True)
    latest_batch_c_markdown = latest_batch_c_dir / "real_question_eval_report.md"
    latest_batch_c_json = latest_batch_c_dir / "real_question_eval_result.json"
    latest_batch_c_markdown.write_text("keep-batch-c\n", encoding="utf-8")
    latest_batch_c_json.write_text('{"run_type":"full_version_batch_c"}\n', encoding="utf-8")

    db, session_generator = _get_test_db_session()
    try:
        result = run_full_version_batch_d_question_eval(
            db,
            RealQuestionEvalConfig(
                artifact_dir=artifact_dir,
                use_real_local_models=True,
                candidate_model_codes=[
                    "bge_m3_dense_sparse",
                    "bge_m3_dense_sparse_multivector",
                ],
                run_type_override="full_version_batch_d",
                execution_mode_override="full_version_batch_d_real_eval",
            ),
        )
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert result.used_fake_models is False
    assert result.run_type == "full_version_batch_d"
    assert result.execution_mode == "full_version_batch_d_real_eval"
    assert result.benchmark_batch_label == "Batch D"
    assert result.benchmark_status == "completed"
    assert result.baseline_provider_codes == ["multilingual_e5_base"]
    assert result.newly_evaluated_provider_codes == [
        "bge_m3_dense_sparse",
        "bge_m3_dense_sparse_multivector",
    ]
    assert result.compared_models == [
        "multilingual_e5_base",
        "bge_m3_dense_sparse",
        "bge_m3_dense_sparse_multivector",
    ]
    assert "latest_full_version_batch_d" in result.artifact_paths.latest_markdown_report
    assert "_full_version_batch_d" in result.artifact_paths.archived_markdown_report

    assert latest_incremental_json.read_text(encoding="utf-8") == latest_incremental_json_before
    assert latest_incremental_markdown.read_text(encoding="utf-8") == latest_incremental_markdown_before
    assert latest_real_markdown.read_text(encoding="utf-8") == "keep-real-batch-d\n"
    assert latest_real_json.read_text(encoding="utf-8") == '{"run_type":"real"}\n'
    assert latest_fake_markdown.read_text(encoding="utf-8") == "keep-fake-batch-d\n"
    assert latest_fake_json.read_text(encoding="utf-8") == '{"run_type":"fake"}\n'
    assert latest_batch_b_markdown.read_text(encoding="utf-8") == "keep-batch-b\n"
    assert latest_batch_b_json.read_text(encoding="utf-8") == '{"run_type":"full_version_batch_b"}\n'
    assert latest_batch_c_markdown.read_text(encoding="utf-8") == "keep-batch-c\n"
    assert latest_batch_c_json.read_text(encoding="utf-8") == '{"run_type":"full_version_batch_c"}\n'

    latest_json_payload = json.loads(Path(result.artifact_paths.latest_json_result).read_text(encoding="utf-8"))
    assert latest_json_payload["execution_mode"] == "full_version_batch_d_real_eval"
    assert latest_json_payload["run_type"] == "full_version_batch_d"
    assert latest_json_payload["benchmark_status"] == "completed"
    assert latest_json_payload["baseline_provider_codes"] == ["multilingual_e5_base"]
    assert latest_json_payload["newly_evaluated_provider_codes"] == [
        "bge_m3_dense_sparse",
        "bge_m3_dense_sparse_multivector",
    ]
    assert latest_json_payload["developer_view"]["models_compared"] == [
        "multilingual_e5_base",
        "bge_m3_dense_sparse",
        "bge_m3_dense_sparse_multivector",
    ]
    assert latest_json_payload["client_view"]["non_compared_notes"] == [
        "Batch D keeps production retrieval unchanged and uses a manual local hybrid reranking path.",
    ]

    markdown_text = Path(result.artifact_paths.latest_markdown_report).read_text(encoding="utf-8")
    assert "## Technical Summary" in markdown_text
    assert "## Newly Evaluated Providers" in markdown_text
    assert "bge_m3_dense_sparse" in markdown_text
    assert "bge_m3_dense_sparse_multivector" in markdown_text
    assert "manual local hybrid reranking path" in markdown_text
    assert "#### jina_embeddings_v3" not in markdown_text
    assert "#### qwen3_embedding_0_6b" not in markdown_text


def test_incremental_artifact_rerender_recomputes_question_wins_from_per_question_winners(tmp_path):
    artifact_dir = tmp_path / "real_question_eval_artifacts"
    latest_dir = artifact_dir / "latest_incremental_new_providers"
    latest_dir.mkdir(parents=True, exist_ok=True)

    source_payload = {
        "task": "Task 32 Real Local Model Question Evaluation",
        "run_id": "20260625_181027Z",
        "run_type": "incremental_real",
        "execution_mode": "incremental_real_eval",
        "historical_providers": ["multilingual_e5_small", "bge_m3"],
        "new_real_providers": [
            "paraphrase_multilingual_mpnet_base_v2",
            "multilingual_e5_base",
        ],
        "timestamp": "2026-06-25T18:10:27.590404+00:00",
        "used_fake_models": False,
        "status": "PASS",
        "artifact_paths": {
            "latest_markdown_report": "/app/artifacts/real_question_eval/latest_incremental_new_providers/real_question_eval_report.md",
            "latest_json_result": "/app/artifacts/real_question_eval/latest_incremental_new_providers/real_question_eval_result.json",
            "archived_markdown_report": "/app/artifacts/real_question_eval/runs/20260625_181027Z_incremental_new_providers/real_question_eval_report.md",
            "archived_json_result": "/app/artifacts/real_question_eval/runs/20260625_181027Z_incremental_new_providers/real_question_eval_result.json",
        },
        "client_view": {
            "source_dataset_note": "deterministic fictional eval corpus",
            "real_client_user_data": "no",
            "purpose": "retrieval quality testing",
            "dataset": {
                "id": "real-question-eval-dataset",
                "name": "Real Question Evaluation Dataset",
            },
            "models_compared": [
                "multilingual_e5_small",
                "bge_m3",
                "paraphrase_multilingual_mpnet_base_v2",
                "multilingual_e5_base",
            ],
            "overall_winner": "multilingual_e5_base",
            "recommended_active_model": "multilingual_e5_base",
            "speed_vs_accuracy_tradeoff": "Historical multilingual_e5_small and bge_m3 results were preserved and compared against the two new real-provider runs using the same dataset and selector rules.",
            "production_recommendation": "A new provider beat historical `bge_m3`; promote `multilingual_e5_base` after reviewing the incremental real comparison.",
            "activated": False,
            "runtime_verified": False,
            "historical_baseline_providers": ["multilingual_e5_small", "bge_m3"],
            "new_real_run_providers": [
                "paraphrase_multilingual_mpnet_base_v2",
                "multilingual_e5_base",
            ],
            "historical_overall_winner": "bge_m3",
            "any_new_provider_beat_historical_winner": True,
        },
        "developer_view": {
            "dataset": {
                "id": "real-question-eval-dataset",
                "name": "Real Question Evaluation Dataset",
            },
            "models_compared": [
                "multilingual_e5_small",
                "bge_m3",
                "paraphrase_multilingual_mpnet_base_v2",
                "multilingual_e5_base",
            ],
            "questions": [
                {
                    "question_id": "question-sunflower-house",
                    "question": "What details show which flower was kept at the old village house and what part of the entrance is mentioned?",
                    "expected_markers": ["sunflower seeds", "blue gate latch"],
                    "expected_distractors": ["rose market poster"],
                    "winner": "multilingual_e5_small",
                    "reason": "Tie broken by stronger top retrieval score and overall selector alignment.",
                    "model_results": [
                        {
                            "model_code": "multilingual_e5_small",
                            "collection_name": "c_e5_small",
                            "top_chunks": [{"rank": 1, "chunk_id": 101, "score": 1.0, "preview": "sunflower"}],
                            "matched_markers": ["sunflower seeds", "blue gate latch"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: blue gate latch, sunflower seeds.",
                            "verdict": "grounded",
                        },
                        {
                            "model_code": "bge_m3",
                            "collection_name": "c_bge",
                            "top_chunks": [{"rank": 1, "chunk_id": 102, "score": 0.99, "preview": "sunflower"}],
                            "matched_markers": ["sunflower seeds", "blue gate latch"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: blue gate latch, sunflower seeds.",
                            "verdict": "grounded",
                        },
                        {
                            "model_code": "paraphrase_multilingual_mpnet_base_v2",
                            "collection_name": "c_mpnet",
                            "top_chunks": [{"rank": 1, "chunk_id": 103, "score": 0.98, "preview": "sunflower"}],
                            "matched_markers": ["sunflower seeds", "blue gate latch"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: blue gate latch, sunflower seeds.",
                            "verdict": "grounded",
                        },
                        {
                            "model_code": "multilingual_e5_base",
                            "collection_name": "c_e5_base",
                            "top_chunks": [{"rank": 1, "chunk_id": 104, "score": 0.97, "preview": "sunflower"}],
                            "matched_markers": ["sunflower seeds", "blue gate latch"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: blue gate latch, sunflower seeds.",
                            "verdict": "grounded",
                        },
                    ],
                },
                {
                    "question_id": "question-winter-trip",
                    "question": "During the winter trip, what travel item was saved and what container kept everyone warm?",
                    "expected_markers": ["overnight train ticket", "wooden thermos"],
                    "expected_distractors": ["summer bus timetable"],
                    "winner": "multilingual_e5_base",
                    "reason": "Tie broken by stronger top retrieval score and overall selector alignment.",
                    "model_results": [
                        {
                            "model_code": "multilingual_e5_small",
                            "collection_name": "c_e5_small",
                            "top_chunks": [{"rank": 1, "chunk_id": 201, "score": 0.96, "preview": "winter"}],
                            "matched_markers": ["overnight train ticket", "wooden thermos"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: overnight train ticket, wooden thermos.",
                            "verdict": "grounded",
                        },
                        {
                            "model_code": "bge_m3",
                            "collection_name": "c_bge",
                            "top_chunks": [{"rank": 1, "chunk_id": 202, "score": 0.97, "preview": "winter"}],
                            "matched_markers": ["overnight train ticket", "wooden thermos"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: overnight train ticket, wooden thermos.",
                            "verdict": "grounded",
                        },
                        {
                            "model_code": "paraphrase_multilingual_mpnet_base_v2",
                            "collection_name": "c_mpnet",
                            "top_chunks": [{"rank": 1, "chunk_id": 203, "score": 0.98, "preview": "winter"}],
                            "matched_markers": ["overnight train ticket", "wooden thermos"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: overnight train ticket, wooden thermos.",
                            "verdict": "grounded",
                        },
                        {
                            "model_code": "multilingual_e5_base",
                            "collection_name": "c_e5_base",
                            "top_chunks": [{"rank": 1, "chunk_id": 204, "score": 1.01, "preview": "winter"}],
                            "matched_markers": ["overnight train ticket", "wooden thermos"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: overnight train ticket, wooden thermos.",
                            "verdict": "grounded",
                        },
                    ],
                },
                {
                    "question_id": "question-grandmother-soup",
                    "question": "Which ingredients and cooking setup explain why grandmother's soup tasted smoky?",
                    "expected_markers": ["dried mushrooms", "oak stove"],
                    "expected_distractors": ["vanilla jam"],
                    "winner": "multilingual_e5_base",
                    "reason": "Tie broken by stronger top retrieval score and overall selector alignment.",
                    "model_results": [
                        {
                            "model_code": "multilingual_e5_small",
                            "collection_name": "c_e5_small",
                            "top_chunks": [{"rank": 1, "chunk_id": 301, "score": 0.7, "preview": "soup"}],
                            "matched_markers": ["dried mushrooms"],
                            "missing_markers": ["oak stove"],
                            "distractors": ["vanilla jam"],
                            "evidence_coverage": 0.5,
                            "first_relevant_rank": 1,
                            "answer_summary": "Partially grounded by: dried mushrooms. Missing: oak stove. Distractors present: vanilla jam.",
                            "verdict": "partial",
                        },
                        {
                            "model_code": "bge_m3",
                            "collection_name": "c_bge",
                            "top_chunks": [{"rank": 1, "chunk_id": 302, "score": 0.94, "preview": "soup"}],
                            "matched_markers": ["dried mushrooms", "oak stove"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: dried mushrooms, oak stove.",
                            "verdict": "grounded",
                        },
                        {
                            "model_code": "paraphrase_multilingual_mpnet_base_v2",
                            "collection_name": "c_mpnet",
                            "top_chunks": [{"rank": 1, "chunk_id": 303, "score": 0.2, "preview": "jam"}],
                            "matched_markers": [],
                            "missing_markers": ["dried mushrooms", "oak stove"],
                            "distractors": ["vanilla jam"],
                            "evidence_coverage": 0.0,
                            "first_relevant_rank": None,
                            "answer_summary": "Ungrounded. Retrieved distractors: vanilla jam.",
                            "verdict": "distracted",
                        },
                        {
                            "model_code": "multilingual_e5_base",
                            "collection_name": "c_e5_base",
                            "top_chunks": [{"rank": 1, "chunk_id": 304, "score": 0.95, "preview": "soup"}],
                            "matched_markers": ["dried mushrooms", "oak stove"],
                            "missing_markers": [],
                            "distractors": [],
                            "evidence_coverage": 1.0,
                            "first_relevant_rank": 1,
                            "answer_summary": "Grounded by retrieved evidence for: dried mushrooms, oak stove.",
                            "verdict": "grounded",
                        },
                    ],
                },
            ],
            "aggregate_results": [
                {
                    "model_code": "multilingual_e5_small",
                    "collection_name": "c_e5_small",
                    "question_wins": 2,
                    "passed_questions": 2,
                    "average_evidence_coverage": 0.8333,
                    "average_first_relevant_rank": 1.0,
                    "total_matched_markers": 5,
                    "total_missing_markers": 1,
                    "total_false_positive_markers": 1,
                    "official_metrics": {
                        "hit_rate": 0.6667,
                        "recall_at_k": 0.8333,
                        "mrr": 1.0,
                        "forbidden_marker_rate": 0.3333,
                        "average_latency_ms": 12.0,
                        "cost_estimate_total": 0.0,
                        "evidence_marker_coverage": 0.8333,
                        "missing_expected_marker_count": 1,
                        "false_positive_count": 1,
                    },
                },
                {
                    "model_code": "bge_m3",
                    "collection_name": "c_bge",
                    "question_wins": 1,
                    "passed_questions": 3,
                    "average_evidence_coverage": 1.0,
                    "average_first_relevant_rank": 1.0,
                    "total_matched_markers": 6,
                    "total_missing_markers": 0,
                    "total_false_positive_markers": 0,
                    "official_metrics": {
                        "hit_rate": 1.0,
                        "recall_at_k": 1.0,
                        "mrr": 1.0,
                        "forbidden_marker_rate": 0.0,
                        "average_latency_ms": 42.0,
                        "cost_estimate_total": 0.0,
                        "evidence_marker_coverage": 1.0,
                        "missing_expected_marker_count": 0,
                        "false_positive_count": 0,
                    },
                },
                {
                    "model_code": "paraphrase_multilingual_mpnet_base_v2",
                    "collection_name": "c_mpnet",
                    "question_wins": 0,
                    "passed_questions": 2,
                    "average_evidence_coverage": 0.6667,
                    "average_first_relevant_rank": 1.0,
                    "total_matched_markers": 4,
                    "total_missing_markers": 2,
                    "total_false_positive_markers": 1,
                    "official_metrics": {
                        "hit_rate": 0.6667,
                        "recall_at_k": 0.6667,
                        "mrr": 1.0,
                        "forbidden_marker_rate": 0.3333,
                        "average_latency_ms": 21.0,
                        "cost_estimate_total": 0.0,
                        "evidence_marker_coverage": 0.6667,
                        "missing_expected_marker_count": 2,
                        "false_positive_count": 1,
                    },
                },
                {
                    "model_code": "multilingual_e5_base",
                    "collection_name": "c_e5_base",
                    "question_wins": 3,
                    "passed_questions": 3,
                    "average_evidence_coverage": 1.0,
                    "average_first_relevant_rank": 1.0,
                    "total_matched_markers": 6,
                    "total_missing_markers": 0,
                    "total_false_positive_markers": 0,
                    "official_metrics": {
                        "hit_rate": 1.0,
                        "recall_at_k": 1.0,
                        "mrr": 1.0,
                        "forbidden_marker_rate": 0.0,
                        "average_latency_ms": 18.0,
                        "cost_estimate_total": 0.0,
                        "evidence_marker_coverage": 1.0,
                        "missing_expected_marker_count": 0,
                        "false_positive_count": 0,
                    },
                },
            ],
            "selected_config": {
                "best_model_code": "multilingual_e5_base",
                "best_collection_name": "c_e5_base",
            },
            "activated_config": {},
            "runtime_retrieval_verification": {},
            "historical_providers": ["multilingual_e5_small", "bge_m3"],
            "new_real_providers": [
                "paraphrase_multilingual_mpnet_base_v2",
                "multilingual_e5_base",
            ],
            "historical_overall_winner": "bge_m3",
            "any_new_provider_beat_historical_winner": True,
        },
    }

    source_json_path = latest_dir / "real_question_eval_result.json"
    source_markdown_path = latest_dir / "real_question_eval_report.md"
    source_json_path.write_text(json.dumps(source_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    source_markdown_path.write_text("# stale incremental report\n", encoding="utf-8")

    result = rerender_incremental_real_artifacts_from_existing_json(artifact_dir=artifact_dir)

    assert result.overall_winner_model_code == "multilingual_e5_base"
    assert [item.question_id for item in result.question_results] == [
        "question-sunflower-house",
        "question-winter-trip",
        "question-grandmother-soup",
    ]

    corrected_payload = json.loads(source_json_path.read_text(encoding="utf-8"))
    corrected_counts = {
        item["model_code"]: item["question_wins"]
        for item in corrected_payload["developer_view"]["aggregate_results"]
    }
    assert corrected_counts == {
        "multilingual_e5_small": 1,
        "bge_m3": 0,
        "paraphrase_multilingual_mpnet_base_v2": 0,
        "multilingual_e5_base": 2,
    }

    per_question_counts: dict[str, int] = {}
    for question in corrected_payload["developer_view"]["questions"]:
        per_question_counts.setdefault(question["winner"], 0)
        per_question_counts[question["winner"]] += 1

    assert corrected_counts["multilingual_e5_small"] == per_question_counts["multilingual_e5_small"]
    assert corrected_counts["multilingual_e5_base"] == per_question_counts["multilingual_e5_base"]
    assert corrected_payload["client_view"]["overall_winner"] == "multilingual_e5_base"

    rewritten_markdown = source_markdown_path.read_text(encoding="utf-8")
    assert "#### multilingual_e5_small" in rewritten_markdown
    assert "- Question wins: 1" in rewritten_markdown
    assert "#### bge_m3" in rewritten_markdown
    assert "#### paraphrase_multilingual_mpnet_base_v2" in rewritten_markdown
    assert "#### multilingual_e5_base" in rewritten_markdown
    assert "- Question wins: 2" in rewritten_markdown

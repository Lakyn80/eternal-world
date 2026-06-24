from __future__ import annotations

from app.db.models import RagEmbedding
from app.db.session import get_db
from app.main import app
from app.modules.rag_quality.schemas import (
    RagQualityCaseResultsInput,
    RagQualityEvalCase,
    RagQualityEvalDataset,
    RagQualityRetrievalConfigCandidate,
    RagQualityRetrievalResultItem,
)
from app.modules.rag_quality.service import RagQualityService
from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead


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


def _build_dataset() -> RagQualityEvalDataset:
    return RagQualityEvalDataset(
        dataset_id="universal-quality-dataset",
        name="Universal Quality Dataset",
        description="Reusable retrieval quality dataset.",
        project_name="generic-rag",
        cases=[
            RagQualityEvalCase(
                case_id="case-grounded",
                title="Grounded city fact",
                query="Which city is mentioned?",
                expected_markers=["Brno", "station"],
                expected_source_ids=[10],
                expected_chunk_ids=[100],
                expected_behavior="retrieval_only",
                minimum_relevant_results=1,
                tags=["grounded"],
                metadata={"priority": "high"},
            ),
            RagQualityEvalCase(
                case_id="case-no-evidence",
                title="Unknown fact should not retrieve support",
                query="What is the secret code word?",
                forbidden_markers=["secret code word"],
                expected_behavior="lack_of_evidence",
                metadata={"priority": "safety"},
            ),
        ],
        metadata={"owner": "tests"},
    )


def _build_candidates() -> tuple[RagQualityRetrievalConfigCandidate, RagQualityRetrievalConfigCandidate]:
    return (
        RagQualityRetrievalConfigCandidate(
            config_id="config-safe",
            model_code="multilingual_e5_small",
            collection_name="eternal_world_rag_chunks__multilingual_e5_small",
            top_k=5,
            retrieval_mode="hybrid",
        ),
        RagQualityRetrievalConfigCandidate(
            config_id="config-risky",
            model_code="bge_m3",
            collection_name="eternal_world_rag_chunks__bge_m3",
            top_k=5,
            retrieval_mode="hybrid",
        ),
    )


def test_eval_case_schema_supports_expected_markers_forbidden_markers_behavior_and_metadata():
    case = _build_dataset().cases[0]

    assert case.expected_markers == ["Brno", "station"]
    assert case.expected_source_ids == [10]
    assert case.expected_chunk_ids == [100]
    assert case.expected_behavior == "retrieval_only"
    assert case.metadata == {"priority": "high"}


def test_dataset_can_contain_multiple_cases():
    dataset = _build_dataset()

    assert dataset.dataset_id == "universal-quality-dataset"
    assert len(dataset.cases) == 2
    assert [case.case_id for case in dataset.cases] == [
        "case-grounded",
        "case-no-evidence",
    ]


def test_candidate_retrieval_configs_can_represent_multiple_models_and_collections():
    safe_candidate, risky_candidate = _build_candidates()

    assert safe_candidate.model_code == "multilingual_e5_small"
    assert safe_candidate.collection_name.endswith("__multilingual_e5_small")
    assert risky_candidate.model_code == "bge_m3"
    assert risky_candidate.collection_name.endswith("__bge_m3")


def test_hit_rate_recall_and_mrr_are_computed_correctly():
    dataset = RagQualityEvalDataset(
        dataset_id="metrics-dataset",
        name="Metrics Dataset",
        cases=[
            RagQualityEvalCase(
                case_id="metrics-case",
                title="Metrics Case",
                query="Tell me about Brno",
                expected_markers=["Brno", "teacher"],
                expected_behavior="retrieval_only",
            )
        ],
    )
    candidate = _build_candidates()[0]
    service = RagQualityService()

    evaluation = service.evaluate_config_results(
        dataset=dataset,
        candidate=candidate,
        case_results_inputs=[
            RagQualityCaseResultsInput(
                config_id=candidate.config_id,
                case_id="metrics-case",
                results=[
                    RagQualityRetrievalResultItem(
                        chunk_id=1,
                        source_id=1,
                        score=0.9,
                        text="Brno is the city in the archive.",
                        rank=1,
                    ),
                    RagQualityRetrievalResultItem(
                        chunk_id=2,
                        source_id=2,
                        score=0.8,
                        text="This result is unrelated.",
                        rank=2,
                    ),
                ],
                latency_ms=100,
                cost_estimate=0.01,
            )
        ],
    )

    case_evaluation = evaluation.case_evaluations[0]
    assert case_evaluation.hit is True
    assert case_evaluation.recall_at_k == 0.5
    assert case_evaluation.reciprocal_rank == 1.0
    assert evaluation.metrics.hit_rate == 1.0
    assert evaluation.metrics.recall_at_k == 0.5
    assert evaluation.metrics.mrr == 1.0


def test_forbidden_marker_detection_and_missing_expected_markers_work():
    dataset = _build_dataset()
    candidate = _build_candidates()[0]
    service = RagQualityService()

    evaluation = service.evaluate_config_results(
        dataset=dataset,
        candidate=candidate,
        case_results_inputs=[
            RagQualityCaseResultsInput(
                config_id=candidate.config_id,
                case_id="case-grounded",
                results=[
                    RagQualityRetrievalResultItem(
                        chunk_id=999,
                        source_id=999,
                        score=0.7,
                        text="Brno is mentioned but the platform detail is missing.",
                        rank=1,
                    )
                ],
            ),
            RagQualityCaseResultsInput(
                config_id=candidate.config_id,
                case_id="case-no-evidence",
                results=[
                    RagQualityRetrievalResultItem(
                        score=0.5,
                        text="The secret code word is sunflower.",
                        rank=1,
                    )
                ],
            ),
        ],
    )

    grounded_case = evaluation.case_evaluations[0]
    no_evidence_case = evaluation.case_evaluations[1]
    assert grounded_case.missing_expected_markers == ["station"]
    assert grounded_case.missing_expected_source_ids == [10]
    assert grounded_case.missing_expected_chunk_ids == [100]
    assert no_evidence_case.forbidden_markers_found == ["secret code word"]
    assert evaluation.metrics.forbidden_marker_rate == 0.5


def test_latency_and_cost_metrics_are_aggregated_when_provided():
    dataset = _build_dataset()
    candidate = _build_candidates()[0]
    service = RagQualityService()

    evaluation = service.evaluate_config_results(
        dataset=dataset,
        candidate=candidate,
        case_results_inputs=[
            RagQualityCaseResultsInput(
                config_id=candidate.config_id,
                case_id="case-grounded",
                results=[
                    RagQualityRetrievalResultItem(
                        chunk_id=100,
                        source_id=10,
                        score=0.95,
                        text="Brno station archive note.",
                        rank=1,
                    )
                ],
                latency_ms=120,
                cost_estimate=0.03,
            ),
            RagQualityCaseResultsInput(
                config_id=candidate.config_id,
                case_id="case-no-evidence",
                results=[],
                latency_ms=180,
                cost_estimate=0.02,
            ),
        ],
    )

    assert evaluation.metrics.average_latency_ms == 150
    assert evaluation.metrics.cost_estimate_total == 0.05


def test_selector_chooses_best_config_by_quality_metrics():
    dataset = _build_dataset()
    safe_candidate, risky_candidate = _build_candidates()
    service = RagQualityService()

    run_result = service.run_quality_evaluation(
        dataset=dataset,
        candidates=[safe_candidate, risky_candidate],
        case_results_inputs=[
            RagQualityCaseResultsInput(
                config_id=safe_candidate.config_id,
                case_id="case-grounded",
                results=[
                    RagQualityRetrievalResultItem(
                        chunk_id=100,
                        source_id=10,
                        score=0.95,
                        text="Brno station archive note.",
                        rank=1,
                    )
                ],
                latency_ms=120,
                cost_estimate=0.01,
            ),
            RagQualityCaseResultsInput(
                config_id=safe_candidate.config_id,
                case_id="case-no-evidence",
                results=[],
                latency_ms=100,
                cost_estimate=0.01,
            ),
                RagQualityCaseResultsInput(
                    config_id=risky_candidate.config_id,
                    case_id="safety-case",
                    results=[
                    RagQualityRetrievalResultItem(
                        chunk_id=100,
                        source_id=10,
                        score=0.99,
                        text="Brno archive note only.",
                        rank=1,
                    )
                ],
                latency_ms=80,
                cost_estimate=0.02,
            ),
            RagQualityCaseResultsInput(
                config_id=risky_candidate.config_id,
                case_id="case-no-evidence",
                results=[
                    RagQualityRetrievalResultItem(
                        score=0.4,
                        text="secret code word appears here.",
                        rank=1,
                    )
                ],
                latency_ms=80,
                cost_estimate=0.02,
            ),
        ],
    )

    assert run_result.selection.best_config_id == safe_candidate.config_id
    assert run_result.selection.best_model_code == safe_candidate.model_code
    assert run_result.selection.selected_metrics is not None


def test_selector_does_not_choose_high_forbidden_rate_config_when_safer_close_quality_exists():
    dataset = RagQualityEvalDataset(
        dataset_id="safety-dataset",
        name="Safety Dataset",
        cases=[
            RagQualityEvalCase(
                case_id="safety-case",
                title="Safety-sensitive retrieval case",
                query="Which city is mentioned?",
                expected_markers=["Brno", "station"],
                forbidden_markers=["fabricated"],
                expected_behavior="retrieval_only",
                minimum_relevant_results=1,
            )
        ],
    )
    safe_candidate, risky_candidate = _build_candidates()
    service = RagQualityService()

    risky_evaluation = service.evaluate_config_results(
        dataset=dataset,
        candidate=risky_candidate,
        case_results_inputs=[
            RagQualityCaseResultsInput(
                config_id=risky_candidate.config_id,
                case_id="safety-case",
                results=[
                    RagQualityRetrievalResultItem(
                        chunk_id=100,
                        source_id=10,
                        score=0.98,
                        text="Brno station archive note with fabricated detail.",
                        rank=1,
                    )
                ],
                latency_ms=50,
                cost_estimate=0.01,
            ),
        ],
    )
    safe_evaluation = service.evaluate_config_results(
        dataset=dataset,
        candidate=safe_candidate,
        case_results_inputs=[
                RagQualityCaseResultsInput(
                    config_id=safe_candidate.config_id,
                    case_id="safety-case",
                    results=[
                    RagQualityRetrievalResultItem(
                        chunk_id=100,
                        source_id=10,
                        score=0.97,
                        text="Brno station archive note.",
                        rank=1,
                    )
                ],
                latency_ms=60,
                cost_estimate=0.01,
            ),
        ],
    )

    selection = service.select_best_config(
        config_evaluations=[risky_evaluation, safe_evaluation],
    )

    assert selection.best_config_id == safe_candidate.config_id
    assert any("safety override" in reason.lower() for reason in selection.reasons)


def test_evaluator_returns_structured_reasons_and_warnings():
    dataset = _build_dataset()
    candidate = _build_candidates()[0]
    service = RagQualityService()

    evaluation = service.evaluate_config_results(
        dataset=dataset,
        candidate=candidate,
        case_results_inputs=[
            RagQualityCaseResultsInput(
                config_id=candidate.config_id,
                case_id="case-grounded",
                results=[],
            )
        ],
    )

    assert evaluation.reasons
    assert evaluation.warnings
    assert evaluation.case_evaluations[0].reasons
    assert evaluation.case_evaluations[0].warnings


def test_evaluator_works_with_generic_retrieval_result_data_and_adapter():
    dataset = _build_dataset()
    candidate = _build_candidates()[0]
    service = RagQualityService()
    retrieval_response = RagRetrievalResponseRead(
        profile_id=1,
        query="Which city is mentioned?",
        model_code="multilingual_e5_small",
        results=[
            RagRetrievalResultRead(
                chunk_id=100,
                source_id=10,
                embedding_id=15,
                score=0.91,
                text="Brno station archive note.",
                chunk_index=0,
                language="en",
                source_type="manual_text",
                validation_status="valid",
                text_hash="hash-100",
                qdrant_collection="eternal_world_rag_chunks__multilingual_e5_small",
                payload_metadata={"profile_id": 1},
            )
        ],
    )

    adapted_input = service.adapt_rag_retrieval_response(
        case_id="case-grounded",
        candidate=candidate,
        retrieval_response=retrieval_response,
        latency_ms=111,
        cost_estimate=0.02,
    )
    case_evaluation = service.evaluate_case_results(
        case=dataset.cases[0],
        case_results=adapted_input,
    )

    assert adapted_input.results[0].metadata["embedding_id"] == 15
    assert case_evaluation.hit is True
    assert case_evaluation.matched_expected_markers == ["Brno", "station"]


def test_rag_quality_does_not_call_real_external_apis(monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made by rag_quality tests")

    monkeypatch.setattr("httpx.request", fail_http_call)
    monkeypatch.setattr("httpx.get", fail_http_call)
    monkeypatch.setattr("httpx.post", fail_http_call)

    dataset = _build_dataset()
    candidate = _build_candidates()[0]
    service = RagQualityService()
    evaluation = service.evaluate_config_results(
        dataset=dataset,
        candidate=candidate,
        case_results_inputs=[
            RagQualityCaseResultsInput(
                config_id=candidate.config_id,
                case_id="case-no-evidence",
                results=[],
            )
        ],
    )

    assert evaluation.config_id == candidate.config_id


def test_rag_quality_does_not_create_stored_query_embeddings(client):
    dataset = _build_dataset()
    candidate = _build_candidates()[0]
    service = RagQualityService()
    db, session_generator = _get_test_db_session()
    try:
        before_count = db.query(RagEmbedding).count()
        service.evaluate_config_results(
            dataset=dataset,
            candidate=candidate,
            case_results_inputs=[
                RagQualityCaseResultsInput(
                    config_id=candidate.config_id,
                    case_id="case-grounded",
                    results=[],
                )
            ],
        )
        after_count = db.query(RagEmbedding).count()
    finally:
        _close_test_db_session(session_generator)

    assert before_count == after_count

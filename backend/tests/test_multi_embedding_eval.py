from __future__ import annotations

from types import SimpleNamespace

import pytest

from app.core.config import settings
from app.db.models import BackgroundJob, RagChunk, RagEmbedding
from app.db.session import get_db
from app.main import app
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.embeddings.exceptions import RagEmbeddingModelUnavailableError
from app.modules.embeddings.schemas import RagSourceEmbeddingSummaryRead
from app.modules.job_tracking.enums import BackgroundJobStatus, BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.multi_embedding_eval.exceptions import MultiEmbeddingEvalAllCandidatesFailedError
from app.modules.multi_embedding_eval.schemas import MultiEmbeddingEvalRequest
from app.modules.multi_embedding_eval.service import (
    MAJOR_STEPS_PER_CANDIDATE,
    WORKFLOW_NAME,
    process_multi_embedding_eval_job,
)
from app.modules.qdrant_indexing.schemas import RagSourceIndexingSummaryRead
from app.modules.rag_quality.schemas import (
    RagQualityCaseResultsInput,
    RagQualityEvalCase,
    RagQualityEvalDataset,
    RagQualityRetrievalConfigCandidate,
    RagQualityRetrievalResultItem,
    RagQualityRunResult,
    RagQualitySelectionResult,
)
from app.modules.rag_quality.service import RagQualityService
from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Multi Eval User",
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


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Multi Eval Source",
        "raw_text": "Brno station archive note. Another sentence for chunking.",
        "source_type": "manual_text",
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
            elif self.model_name == "sentence-transformers/paraphrase-multilingual-mpnet-base-v2":
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


def _build_dataset() -> RagQualityEvalDataset:
    return RagQualityEvalDataset(
        dataset_id="multi-embedding-dataset",
        name="Multi Embedding Dataset",
        cases=[
            RagQualityEvalCase(
                case_id="case-brno",
                title="Expected archive fact",
                query="Which city is mentioned?",
                expected_markers=["Brno"],
                expected_behavior="retrieval_only",
                minimum_relevant_results=1,
            )
        ],
    )


def _build_request_model() -> MultiEmbeddingEvalRequest:
    return MultiEmbeddingEvalRequest(
        dataset=_build_dataset(),
        candidates=[
            {
                "config_id": "candidate-mock",
                "model_code": "mock_embedding",
                "collection_name": "eternal_world_rag_chunks__mock_embedding",
                "top_k": 3,
                "retrieval_mode": "hybrid",
            },
            {
                "config_id": "candidate-bge",
                "model_code": "bge_m3",
                "collection_name": "eternal_world_rag_chunks__bge_m3",
                "top_k": 3,
                "retrieval_mode": "hybrid",
            },
        ],
    )


def _build_request_json() -> dict[str, object]:
    return _build_request_model().model_dump(mode="json")


def _build_retrieval_response(*, model_code: str, collection_name: str) -> RagRetrievalResponseRead:
    return RagRetrievalResponseRead(
        profile_id=1,
        query="Which city is mentioned?",
        model_code=model_code,
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
                qdrant_collection=collection_name,
                payload_metadata={"profile_id": 1},
            )
        ],
    )


def _create_multi_eval_job(*, db, owner_user_id: int, profile_id: int, source_id: int, payload: MultiEmbeddingEvalRequest):
    return create_job(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        job_type=BackgroundJobType.RAG_RETRIEVAL,
        input_payload={
            "workflow": WORKFLOW_NAME,
            "source_id": source_id,
            "profile_id": profile_id,
            "dataset_id": payload.dataset.dataset_id,
            "request": payload.model_dump(mode="json"),
        },
        progress_current=0,
        progress_total=len(payload.candidates) * MAJOR_STEPS_PER_CANDIDATE,
    )


def test_multi_embedding_eval_endpoint_requires_authentication(client):
    token = _register_and_login(client, "multi-eval-auth@example.com")
    profile_id = _create_profile(client, token, "Multi Eval Auth Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    response = client.post(
        f"/api/rag-sources/{source_id}/multi-embedding-eval",
        json=_build_request_json(),
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_can_start_multi_embedding_eval_only_for_own_source_and_job_is_created(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-owner@example.com")
    profile_id = _create_profile(client, token, "Multi Eval Owner Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    monkeypatch.setattr(
        "app.worker.tasks.run_multi_embedding_eval_job.delay",
        lambda job_id: SimpleNamespace(id="celery-multi-eval-job"),
    )

    response = client.post(
        f"/api/rag-sources/{source_id}/multi-embedding-eval",
        headers=_auth_headers(token),
        json=_build_request_json(),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["job_type"] == BackgroundJobType.RAG_RETRIEVAL.value
    assert body["status"] == BackgroundJobStatus.QUEUED.value
    assert body["source_id"] == source_id
    assert body["profile_id"] == profile_id
    assert body["dataset_id"] == "multi-embedding-dataset"
    assert body["celery_task_id"] == "celery-multi-eval-job"

    db, session_generator = _get_test_db_session()
    try:
        background_job = db.get(BackgroundJob, body["job_id"])
    finally:
        _close_test_db_session(session_generator)

    assert background_job is not None
    assert background_job.input_payload["workflow"] == WORKFLOW_NAME


def test_cross_user_source_access_returns_404(client):
    owner_token = _register_and_login(client, "multi-eval-cross-owner@example.com")
    other_token = _register_and_login(client, "multi-eval-cross-other@example.com")
    profile_id = _create_profile(client, owner_token, "Multi Eval Cross Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]

    response = client.post(
        f"/api/rag-sources/{source_id}/multi-embedding-eval",
        headers=_auth_headers(other_token),
        json=_build_request_json(),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_each_candidate_uses_its_own_model_code_and_collection_name(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-candidates@example.com")
    profile_id = _create_profile(client, token, "Candidate Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()
    index_calls: list[tuple[str | None, str | None]] = []
    retrieval_calls: list[tuple[str | None, str | None]] = []

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.embed_source_chunks",
        lambda db, *, current_user, source_id, model_code=None: RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code=str(model_code),
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )

    def fake_index_source_embeddings(db, *, current_user, source_id, model_code=None, collection_name=None):
        index_calls.append((model_code, collection_name))
        return RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        )

    def fake_retrieve_profile_rag_for_collection(db, *, current_user, profile_id, payload, collection_name=None):
        retrieval_calls.append((payload.model_code, collection_name))
        return _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        )

    monkeypatch.setattr("app.modules.multi_embedding_eval.service.index_source_embeddings", fake_index_source_embeddings)
    monkeypatch.setattr("app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection", fake_retrieve_profile_rag_for_collection)

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        result = process_multi_embedding_eval_job(db, job_id=background_job.id, celery_task_id="celery-multi-success")
        db.refresh(background_job)
    finally:
        _close_test_db_session(session_generator)

    assert result["status"] == "succeeded"
    assert background_job.status == BackgroundJobStatus.SUCCEEDED.value
    assert index_calls == [
        ("mock_embedding", "eternal_world_rag_chunks__mock_embedding"),
        ("bge_m3", "eternal_world_rag_chunks__bge_m3"),
    ]
    assert retrieval_calls == index_calls
    assert len({collection_name for _, collection_name in index_calls}) == 2


def test_candidate_execution_reuses_existing_chunks(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-existing-chunks@example.com")
    profile_id = _create_profile(client, token, "Existing Chunks Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    payload = _build_request_model()

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.chunk_rag_source",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("Existing chunks should be reused")),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.embed_source_chunks",
        lambda db, *, current_user, source_id, model_code=None: RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code=str(model_code),
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        existing_chunk_ids = [
            chunk.id
            for chunk in db.query(RagChunk).filter(RagChunk.source_id == source_id).all()
        ]
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        process_multi_embedding_eval_job(db, job_id=background_job.id)
        remaining_chunk_ids = [
            chunk.id
            for chunk in db.query(RagChunk).filter(RagChunk.source_id == source_id).all()
        ]
    finally:
        _close_test_db_session(session_generator)

    assert remaining_chunk_ids == existing_chunk_ids


def test_candidate_execution_uses_existing_embedding_and_qdrant_services(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-service-spies@example.com")
    profile_id = _create_profile(client, token, "Service Spies Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()
    calls: list[str] = []

    def fake_embed_source_chunks(db, *, current_user, source_id, model_code=None):
        calls.append(f"embed:{model_code}")
        return RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code=str(model_code),
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        )

    def fake_index_source_embeddings(db, *, current_user, source_id, model_code=None, collection_name=None):
        calls.append(f"index:{model_code}:{collection_name}")
        return RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        )

    monkeypatch.setattr("app.modules.multi_embedding_eval.service.embed_source_chunks", fake_embed_source_chunks)
    monkeypatch.setattr("app.modules.multi_embedding_eval.service.index_source_embeddings", fake_index_source_embeddings)
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        process_multi_embedding_eval_job(db, job_id=background_job.id)
    finally:
        _close_test_db_session(session_generator)

    assert calls == [
        "embed:mock_embedding",
        "index:mock_embedding:eternal_world_rag_chunks__mock_embedding",
        "embed:bge_m3",
        "index:bge_m3:eternal_world_rag_chunks__bge_m3",
    ]


def test_retrieval_results_are_converted_to_generic_rag_quality_data_and_selector_is_used(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-rag-quality@example.com")
    profile_id = _create_profile(client, token, "Rag Quality Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()
    original_adapt = RagQualityService.adapt_rag_retrieval_response
    original_run = RagQualityService.run_quality_evaluation
    captured = {"adapt": 0, "run": 0}

    def capture_adapt(self, *, case_id, candidate, retrieval_response, latency_ms=None, cost_estimate=None, metadata=None):
        captured["adapt"] += 1
        return original_adapt(
            self,
            case_id=case_id,
            candidate=candidate,
            retrieval_response=retrieval_response,
            latency_ms=latency_ms,
            cost_estimate=cost_estimate,
            metadata=metadata,
        )

    def capture_run(self, *, dataset, candidates, case_results_inputs, max_average_latency_ms=None, max_cost_estimate_total=None):
        captured["run"] += 1
        assert all(isinstance(item, RagQualityCaseResultsInput) for item in case_results_inputs)
        return original_run(
            self,
            dataset=dataset,
            candidates=candidates,
            case_results_inputs=case_results_inputs,
            max_average_latency_ms=max_average_latency_ms,
            max_cost_estimate_total=max_cost_estimate_total,
        )

    monkeypatch.setattr(RagQualityService, "adapt_rag_retrieval_response", capture_adapt)
    monkeypatch.setattr(RagQualityService, "run_quality_evaluation", capture_run)
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.embed_source_chunks",
        lambda db, *, current_user, source_id, model_code=None: RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code=str(model_code),
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        process_multi_embedding_eval_job(db, job_id=background_job.id)
    finally:
        _close_test_db_session(session_generator)

    assert captured["adapt"] == len(payload.candidates) * len(payload.dataset.cases)
    assert captured["run"] == 1


def test_one_failed_candidate_produces_partial_success_when_another_candidate_succeeds(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-partial-success@example.com")
    profile_id = _create_profile(client, token, "Partial Success Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()

    def fake_embed_source_chunks(db, *, current_user, source_id, model_code=None):
        if model_code == "mock_embedding":
            raise RagEmbeddingModelUnavailableError("Embedding model not available")
        return RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code=str(model_code),
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        )

    monkeypatch.setattr("app.modules.multi_embedding_eval.service.embed_source_chunks", fake_embed_source_chunks)
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        result = process_multi_embedding_eval_job(db, job_id=background_job.id)
        db.refresh(background_job)
    finally:
        _close_test_db_session(session_generator)

    assert result["status"] == "succeeded"
    assert background_job.status == BackgroundJobStatus.SUCCEEDED.value
    assert background_job.result_payload["candidates_failed"] == ["candidate-mock"]
    assert background_job.result_payload["candidates_evaluated"] == ["candidate-bge"]
    assert background_job.result_payload["warnings"]


def test_all_failed_candidates_mark_job_failed(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-all-failed@example.com")
    profile_id = _create_profile(client, token, "All Failed Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.embed_source_chunks",
        lambda *args, **kwargs: (_ for _ in ()).throw(RagEmbeddingModelUnavailableError("Embedding model not available")),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        with pytest.raises(MultiEmbeddingEvalAllCandidatesFailedError):
            process_multi_embedding_eval_job(db, job_id=background_job.id)
        db.refresh(background_job)
    finally:
        _close_test_db_session(session_generator)

    assert background_job.status == BackgroundJobStatus.FAILED.value
    assert background_job.error_payload["code"] == "multi_embedding_eval_all_candidates_failed"
    assert background_job.error_payload["step"] == "rag_quality_evaluated"


def test_result_payload_includes_best_config_and_all_config_scores(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-result-payload@example.com")
    profile_id = _create_profile(client, token, "Result Payload Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.embed_source_chunks",
        lambda db, *, current_user, source_id, model_code=None: RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code=str(model_code),
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        process_multi_embedding_eval_job(db, job_id=background_job.id)
        db.refresh(background_job)
    finally:
        _close_test_db_session(session_generator)

    assert background_job.result_payload["best_config"]["best_config_id"] is not None
    assert background_job.result_payload["all_config_scores"]


def test_multi_embedding_eval_does_not_call_brain_agent(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-no-brain@example.com")
    profile_id = _create_profile(client, token, "No Brain Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()

    monkeypatch.setattr(
        BrainAgentService,
        "generate_chat_response",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("Brain Agent should not be called")),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.embed_source_chunks",
        lambda db, *, current_user, source_id, model_code=None: RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code=str(model_code),
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        process_multi_embedding_eval_job(db, job_id=background_job.id)
    finally:
        _close_test_db_session(session_generator)


def test_multi_embedding_eval_does_not_create_stored_query_embeddings(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-no-query-embeddings@example.com")
    profile_id = _create_profile(client, token, "No Query Embeddings Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = MultiEmbeddingEvalRequest(
        dataset=_build_dataset(),
        candidates=[
            {
                "config_id": "candidate-mock",
                "model_code": "mock_embedding",
                "collection_name": "eternal_world_rag_chunks__mock_embedding",
            }
        ],
    )

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id, RagEmbedding.model_code == model_code).count(),
            indexed_count=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id, RagEmbedding.model_code == model_code).count(),
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        embeddings_before = db.query(RagEmbedding).count()
        process_multi_embedding_eval_job(db, job_id=background_job.id)
        chunk_count = db.query(RagChunk).filter(RagChunk.source_id == source_id).count()
        source_embedding_count = db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count()
        embeddings_after = db.query(RagEmbedding).count()
    finally:
        _close_test_db_session(session_generator)

    assert embeddings_before == 0
    assert chunk_count > 0
    assert source_embedding_count == chunk_count
    assert embeddings_after == source_embedding_count


def test_multi_embedding_eval_does_not_call_real_external_apis(client, monkeypatch):
    token = _register_and_login(client, "multi-eval-no-external@example.com")
    profile_id = _create_profile(client, token, "No External Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = _build_request_model()

    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made by multi_embedding_eval tests")

    monkeypatch.setattr("httpx.request", fail_http_call)
    monkeypatch.setattr("httpx.get", fail_http_call)
    monkeypatch.setattr("httpx.post", fail_http_call)
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        process_multi_embedding_eval_job(db, job_id=background_job.id)
    finally:
        _close_test_db_session(session_generator)


def test_multi_embedding_eval_can_include_multilingual_e5_small_candidate(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "multi-eval-e5@example.com")
    profile_id = _create_profile(client, token, "Multi Eval E5 Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    payload = MultiEmbeddingEvalRequest(
        dataset=_build_dataset(),
        candidates=[
            {
                "config_id": "candidate-e5",
                "model_code": "multilingual_e5_small",
                "collection_name": "eternal_world_rag_chunks__multilingual_e5_small_eval",
                "top_k": 3,
                "retrieval_mode": "hybrid",
            }
        ],
    )

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        result = process_multi_embedding_eval_job(db, job_id=background_job.id)
    finally:
        _close_test_db_session(session_generator)

    assert result["status"] == "succeeded"
    assert result["result_payload"]["best_config"]["best_model_code"] == "multilingual_e5_small"


def test_multi_embedding_eval_can_include_bge_m3_candidate_using_fake_sentence_transformers(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "multi-eval-bge@example.com")
    profile_id = _create_profile(client, token, "Multi Eval BGE Profile")
    source_id = _create_rag_source(
        client,
        token,
        profile_id,
        raw_text="Brno archive memory sentence. Another Brno sentence for evaluation chunking.",
    ).json()["id"]
    payload = MultiEmbeddingEvalRequest(
        dataset=_build_dataset(),
        candidates=[
            {
                "config_id": "candidate-bge",
                "model_code": "bge_m3",
                "collection_name": "eternal_world_rag_chunks__bge_m3_eval",
                "top_k": 3,
                "retrieval_mode": "hybrid",
            }
        ],
    )

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=db.query(RagEmbedding).filter(
                RagEmbedding.source_id == source_id,
                RagEmbedding.model_code == model_code,
            ).count(),
            indexed_count=db.query(RagEmbedding).filter(
                RagEmbedding.source_id == source_id,
                RagEmbedding.model_code == model_code,
            ).count(),
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        result = process_multi_embedding_eval_job(db, job_id=background_job.id)
        chunk_count = db.query(RagChunk).filter(RagChunk.source_id == source_id).count()
        bge_embeddings = db.query(RagEmbedding).filter(
            RagEmbedding.source_id == source_id,
            RagEmbedding.model_code == "bge_m3",
        ).all()
    finally:
        _close_test_db_session(session_generator)

    assert result["status"] == "succeeded"
    assert result["result_payload"]["best_config"]["best_model_code"] == "bge_m3"
    assert chunk_count > 0
    assert len(bge_embeddings) == chunk_count
    assert all(embedding.vector_dimension == 1024 for embedding in bge_embeddings)


def test_multi_embedding_eval_can_include_mpnet_candidate_using_fake_sentence_transformers(client, monkeypatch):
    _install_fake_sentence_transformers(monkeypatch)
    token = _register_and_login(client, "multi-eval-mpnet@example.com")
    profile_id = _create_profile(client, token, "Multi Eval MPNet Profile")
    source_id = _create_rag_source(
        client,
        token,
        profile_id,
        raw_text="Prague archive memory sentence. Another Prague sentence for evaluation chunking.",
    ).json()["id"]
    payload = MultiEmbeddingEvalRequest(
        dataset=_build_dataset(),
        candidates=[
            {
                "config_id": "candidate-mpnet",
                "model_code": "paraphrase_multilingual_mpnet_base_v2",
                "collection_name": "eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2_eval",
                "top_k": 3,
                "retrieval_mode": "hybrid",
            }
        ],
    )

    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None, collection_name=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=db.query(RagEmbedding).filter(
                RagEmbedding.source_id == source_id,
                RagEmbedding.model_code == model_code,
            ).count(),
            indexed_count=db.query(RagEmbedding).filter(
                RagEmbedding.source_id == source_id,
                RagEmbedding.model_code == model_code,
            ).count(),
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.multi_embedding_eval.service.retrieve_profile_rag_for_collection",
        lambda db, *, current_user, profile_id, payload, collection_name=None: _build_retrieval_response(
            model_code=str(payload.model_code),
            collection_name=str(collection_name),
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_multi_eval_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            payload=payload,
        )
        result = process_multi_embedding_eval_job(db, job_id=background_job.id)
        chunk_count = db.query(RagChunk).filter(RagChunk.source_id == source_id).count()
        mpnet_embeddings = db.query(RagEmbedding).filter(
            RagEmbedding.source_id == source_id,
            RagEmbedding.model_code == "paraphrase_multilingual_mpnet_base_v2",
        ).all()
    finally:
        _close_test_db_session(session_generator)

    assert result["status"] == "succeeded"
    assert result["result_payload"]["best_config"]["best_model_code"] == "paraphrase_multilingual_mpnet_base_v2"
    assert chunk_count > 0
    assert len(mpnet_embeddings) == chunk_count
    assert all(embedding.vector_dimension == 768 for embedding in mpnet_embeddings)

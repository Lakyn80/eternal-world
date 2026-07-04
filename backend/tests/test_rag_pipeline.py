from __future__ import annotations

from types import SimpleNamespace

import pytest

from app.db.models import RagChunk, RagEmbedding
from app.db.session import get_db
from app.main import app
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.embeddings.schemas import RagSourceEmbeddingSummaryRead
from app.modules.job_tracking.enums import BackgroundJobStatus, BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.qdrant_indexing.schemas import RagSourceIndexingSummaryRead
from app.modules.rag_chunks.schemas import RagSourceChunkingSummaryRead
from app.modules.rag_chunks.service import RagChunkingFailedError
from app.modules.rag_pipeline.service import PIPELINE_PROGRESS_TOTAL, process_rag_source_job
from app.worker.celery_app import celery_app


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "RAG Pipeline User",
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
        "title": "Pipeline Source",
        "raw_text": "Sentence one. Sentence two. Sentence three.",
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


def _create_pipeline_job(*, db, owner_user_id: int, profile_id: int, source_id: int, model_code: str | None = None):
    return create_job(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        job_type=BackgroundJobType.RAG_SOURCE_INGESTION,
        input_payload={
            "source_id": source_id,
            "profile_id": profile_id,
            "model_code": model_code,
            "pipeline": ["chunking", "embedding_generation", "qdrant_indexing"],
        },
        progress_current=0,
        progress_total=PIPELINE_PROGRESS_TOTAL,
    )


def test_processing_endpoint_requires_authentication(client):
    token = _register_and_login(client, "rag-pipeline-auth@example.com")
    profile_id = _create_profile(client, token, "Pipeline Auth Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    response = client.post(f"/api/rag-sources/{source_id}/process")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_can_start_processing_only_own_source(client, monkeypatch):
    owner_token = _register_and_login(client, "rag-pipeline-owner@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Pipeline Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]

    monkeypatch.setattr(
        "app.worker.tasks.run_rag_source_processing_job.delay",
        lambda job_id: SimpleNamespace(id="celery-rag-pipeline-owned"),
    )

    response = client.post(
        f"/api/rag-sources/{source_id}/process",
        headers=_auth_headers(owner_token),
        json={"model_code": "mock-embedding-small"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["job_type"] == BackgroundJobType.RAG_SOURCE_INGESTION.value
    assert body["status"] == BackgroundJobStatus.QUEUED.value
    assert body["profile_id"] == profile_id
    assert body["input_payload"]["source_id"] == source_id
    assert body["input_payload"]["model_code"] == "mock-embedding-small"


def test_cross_user_source_processing_returns_404(client):
    owner_token = _register_and_login(client, "rag-pipeline-cross-owner@example.com")
    other_token = _register_and_login(client, "rag-pipeline-cross-other@example.com")
    profile_id = _create_profile(client, owner_token, "Cross User Pipeline Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]

    response = client.post(
        f"/api/rag-sources/{source_id}/process",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_starting_processing_creates_background_job_in_queued_state_and_stores_celery_task_id(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-queued@example.com")
    profile_id = _create_profile(client, token, "Queued Pipeline Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    monkeypatch.setattr(
        "app.worker.tasks.run_rag_source_processing_job.delay",
        lambda job_id: SimpleNamespace(id="celery-rag-pipeline-queued"),
    )

    response = client.post(
        f"/api/rag-sources/{source_id}/process",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == BackgroundJobStatus.QUEUED.value
    assert body["progress_current"] == 0
    assert body["progress_total"] == PIPELINE_PROGRESS_TOTAL
    assert body["celery_task_id"] == "celery-rag-pipeline-queued"


def test_pipeline_marks_job_running_updates_progress_and_succeeds(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-success@example.com")
    profile_id = _create_profile(client, token, "Pipeline Success Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    progress_updates: list[tuple[int, int]] = []
    used_steps = {"chunking": 0, "embedding": 0, "indexing": 0}

    def fake_chunk_rag_source(db, *, current_user, source_id):
        used_steps["chunking"] += 1
        return RagSourceChunkingSummaryRead(
            source_id=source_id,
            profile_id=profile_id,
            owner_user_id=current_user.id,
            source_status="chunked",
            chunk_count=3,
            valid_count=3,
            warning_count=0,
            invalid_count=0,
            source_validation_errors=[],
            processing_error=None,
            normalized_text_updated=False,
        )

    def fake_embed_source_chunks(db, *, current_user, source_id, model_code=None):
        used_steps["embedding"] += 1
        return RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code="mock-embedding-small",
            total_chunks=3,
            embedded_count=3,
            skipped_count=0,
            failed_count=0,
        )

    def fake_index_source_embeddings(db, *, current_user, source_id, model_code=None):
        used_steps["indexing"] += 1
        return RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=3,
            indexed_count=3,
            skipped_count=0,
            failed_count=0,
        )

    from app.modules.job_tracking import service as job_tracking_service

    def capture_update_progress(db, *, job_id, progress_current, progress_total):
        progress_updates.append((progress_current, progress_total))
        return job_tracking_service.update_progress(
            db,
            job_id=job_id,
            progress_current=progress_current,
            progress_total=progress_total,
        )

    monkeypatch.setattr("app.modules.rag_pipeline.service.chunk_rag_source", fake_chunk_rag_source)
    monkeypatch.setattr("app.modules.rag_pipeline.service.embed_source_chunks", fake_embed_source_chunks)
    monkeypatch.setattr("app.modules.rag_pipeline.service.index_source_embeddings", fake_index_source_embeddings)
    monkeypatch.setattr("app.modules.rag_pipeline.service.update_progress", capture_update_progress)

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_pipeline_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
            model_code="mock-embedding-small",
        )

        result = process_rag_source_job(
            db,
            job_id=background_job.id,
            celery_task_id="celery-rag-pipeline-success",
        )
        db.refresh(background_job)
    finally:
        _close_test_db_session(session_generator)

    assert result["status"] == "succeeded"
    assert background_job.status == BackgroundJobStatus.SUCCEEDED.value
    assert background_job.celery_task_id == "celery-rag-pipeline-success"
    assert background_job.progress_current == 4
    assert background_job.progress_total == PIPELINE_PROGRESS_TOTAL
    assert background_job.started_at is not None
    assert background_job.finished_at is not None
    assert progress_updates == [(1, 4), (2, 4), (3, 4), (4, 4)]
    assert used_steps == {"chunking": 1, "embedding": 1, "indexing": 1}
    assert background_job.result_payload["source_id"] == source_id
    assert background_job.result_payload["profile_id"] == profile_id
    assert background_job.result_payload["chunks_total"] == 3
    assert background_job.result_payload["embeddings_created"] == 3
    assert background_job.result_payload["embeddings_indexed"] == 3
    assert background_job.result_payload["qdrant_collection"] == "eternal_world_rag_chunks__mock-embedding-small"
    assert len(background_job.event_log) >= 5
    event_stages = [entry["stage"] for entry in background_job.event_log]
    assert "source_validation" in event_stages
    assert "chunking" in event_stages
    assert "embedding_generation" in event_stages
    assert "qdrant_indexing" in event_stages
    assert "job_completed" in event_stages


def test_failed_pipeline_marks_job_failed_with_structured_error_payload(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-fail@example.com")
    profile_id = _create_profile(client, token, "Pipeline Fail Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.chunk_rag_source",
        lambda db, *, current_user, source_id: (_ for _ in ()).throw(RagChunkingFailedError("Chunking failed")),
    )
    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.embed_source_chunks",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("Embedding step should not run")),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_pipeline_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
        )
        with pytest.raises(RagChunkingFailedError):
            process_rag_source_job(
                db,
                job_id=background_job.id,
                celery_task_id="celery-rag-pipeline-fail",
            )
        db.refresh(background_job)
    finally:
        _close_test_db_session(session_generator)

    assert background_job.status == BackgroundJobStatus.FAILED.value
    assert background_job.error_message == "Chunking failed"
    assert any(entry["status"] == "failed" for entry in background_job.event_log)
    assert background_job.error_payload == {
        "code": "rag_chunking_failed",
        "message": "Chunking failed",
        "step": "chunking",
        "details": {
            "job_id": background_job.id,
            "source_id": source_id,
            "exception_type": "RagChunkingFailedError",
        },
    }
    assert background_job.progress_current == 1
    assert background_job.progress_total == PIPELINE_PROGRESS_TOTAL


def test_pipeline_uses_existing_chunking_embedding_and_indexing_services(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-spies@example.com")
    profile_id = _create_profile(client, token, "Pipeline Spies Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    calls: list[str] = []

    def fake_chunk_rag_source(db, *, current_user, source_id):
        calls.append("chunk")
        return RagSourceChunkingSummaryRead(
            source_id=source_id,
            profile_id=profile_id,
            owner_user_id=current_user.id,
            source_status="chunked",
            chunk_count=2,
            valid_count=2,
            warning_count=0,
            invalid_count=0,
            source_validation_errors=[],
            processing_error=None,
            normalized_text_updated=False,
        )

    def fake_embed_source_chunks(db, *, current_user, source_id, model_code=None):
        calls.append("embed")
        return RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code="mock-embedding-small",
            total_chunks=2,
            embedded_count=2,
            skipped_count=0,
            failed_count=0,
        )

    def fake_index_source_embeddings(db, *, current_user, source_id, model_code=None):
        calls.append("index")
        return RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=2,
            indexed_count=2,
            skipped_count=0,
            failed_count=0,
        )

    monkeypatch.setattr("app.modules.rag_pipeline.service.chunk_rag_source", fake_chunk_rag_source)
    monkeypatch.setattr("app.modules.rag_pipeline.service.embed_source_chunks", fake_embed_source_chunks)
    monkeypatch.setattr("app.modules.rag_pipeline.service.index_source_embeddings", fake_index_source_embeddings)

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_pipeline_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
        )
        process_rag_source_job(db, job_id=background_job.id)
    finally:
        _close_test_db_session(session_generator)

    assert calls == ["chunk", "embed", "index"]


def test_pipeline_does_not_call_brain_agent_or_rag_retrieval(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-no-brain@example.com")
    profile_id = _create_profile(client, token, "Pipeline No Brain Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    monkeypatch.setattr(
        "app.modules.rag_retrieval.service.retrieve_profile_rag",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("RAG retrieval should not be called")),
    )
    monkeypatch.setattr(
        BrainAgentService,
        "generate_chat_response",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("Brain Agent should not be called")),
    )
    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.chunk_rag_source",
        lambda db, *, current_user, source_id: RagSourceChunkingSummaryRead(
            source_id=source_id,
            profile_id=profile_id,
            owner_user_id=current_user.id,
            source_status="chunked",
            chunk_count=1,
            valid_count=1,
            warning_count=0,
            invalid_count=0,
            source_validation_errors=[],
            processing_error=None,
            normalized_text_updated=False,
        ),
    )
    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.embed_source_chunks",
        lambda db, *, current_user, source_id, model_code=None: RagSourceEmbeddingSummaryRead(
            source_id=source_id,
            model_code="mock-embedding-small",
            total_chunks=1,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )
    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=1,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_pipeline_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
        )
        process_rag_source_job(db, job_id=background_job.id)
    finally:
        _close_test_db_session(session_generator)


def test_pipeline_does_not_create_stored_query_embeddings(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-no-query-embeddings@example.com")
    profile_id = _create_profile(client, token, "No Query Embeddings Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count(),
            indexed_count=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count(),
            skipped_count=0,
            failed_count=0,
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        background_job = _create_pipeline_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
        )
        embeddings_before = db.query(RagEmbedding).count()

        process_rag_source_job(db, job_id=background_job.id)

        chunk_count = db.query(RagChunk).filter(RagChunk.source_id == source_id).count()
        source_embedding_count = db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count()
        embeddings_after = db.query(RagEmbedding).count()
    finally:
        _close_test_db_session(session_generator)

    assert embeddings_before == 0
    assert chunk_count > 0
    assert source_embedding_count == chunk_count
    assert embeddings_after == source_embedding_count


def test_pipeline_reuses_existing_chunks_on_rerun_without_rechunking(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-existing-chunks@example.com")
    profile_id = _create_profile(client, token, "Existing Chunks Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200

    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.chunk_rag_source",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("Existing chunks should be reused")),
    )
    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count(),
            indexed_count=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count(),
            skipped_count=0,
            failed_count=0,
        ),
    )

    db, session_generator = _get_test_db_session()
    try:
        existing_chunk_ids = [
            row.id
            for row in db.query(RagChunk)
            .filter(RagChunk.source_id == source_id)
            .order_by(RagChunk.id.asc())
            .all()
        ]
        background_job = _create_pipeline_job(
            db=db,
            owner_user_id=1,
            profile_id=profile_id,
            source_id=source_id,
        )

        process_rag_source_job(db, job_id=background_job.id)

        remaining_chunk_ids = [
            row.id
            for row in db.query(RagChunk)
            .filter(RagChunk.source_id == source_id)
            .order_by(RagChunk.id.asc())
            .all()
        ]
        db.refresh(background_job)
    finally:
        _close_test_db_session(session_generator)

    assert remaining_chunk_ids == existing_chunk_ids
    assert background_job.status == BackgroundJobStatus.SUCCEEDED.value
    assert background_job.result_payload["chunks_total"] == len(existing_chunk_ids)


def test_processing_endpoint_runs_in_eager_mode_and_job_is_visible_via_job_tracking(client, monkeypatch):
    token = _register_and_login(client, "rag-pipeline-eager@example.com")
    profile_id = _create_profile(client, token, "Pipeline Eager Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    monkeypatch.setattr("app.worker.tasks.get_session_factory", lambda: app.state.testing_session_local)
    monkeypatch.setattr(celery_app.conf, "task_always_eager", True)
    monkeypatch.setattr(celery_app.conf, "task_eager_propagates", True)
    monkeypatch.setattr(
        "app.modules.rag_pipeline.service.index_source_embeddings",
        lambda db, *, current_user, source_id, model_code=None: RagSourceIndexingSummaryRead(
            source_id=source_id,
            model_code=model_code,
            total_embeddings=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count(),
            indexed_count=db.query(RagEmbedding).filter(RagEmbedding.source_id == source_id).count(),
            skipped_count=0,
            failed_count=0,
        ),
    )

    response = client.post(
        f"/api/rag-sources/{source_id}/process",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == BackgroundJobStatus.SUCCEEDED.value
    assert body["job_type"] == BackgroundJobType.RAG_SOURCE_INGESTION.value
    assert body["progress_current"] == 4
    assert body["progress_total"] == PIPELINE_PROGRESS_TOTAL
    assert body["result_payload"]["source_id"] == source_id

    job_response = client.get(f"/api/jobs/{body['id']}", headers=_auth_headers(token))
    assert job_response.status_code == 200
    assert job_response.json()["id"] == body["id"]

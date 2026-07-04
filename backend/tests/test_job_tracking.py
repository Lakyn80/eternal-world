from pathlib import Path

from app.db.base import Base
from app.db.models import BackgroundJob
from app.db.session import get_db
from app.main import app
from app.modules.job_tracking.enums import BackgroundJobStatus, BackgroundJobType
from app.modules.job_tracking.service import (
    append_job_event,
    backfill_known_milestones,
    create_job,
    mark_failed,
    mark_running,
    mark_succeeded,
    update_progress,
)
from app.worker.celery_app import celery_app


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Job User",
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


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def test_background_job_model_is_included_in_sqlalchemy_metadata():
    assert BackgroundJob.__tablename__ == "background_jobs"
    assert "background_jobs" in Base.metadata.tables


def test_auth_is_required_for_job_endpoints(client):
    list_response = client.get("/api/jobs")
    get_response = client.get("/api/jobs/1")
    smoke_response = client.post("/api/jobs/smoke-test")

    assert list_response.status_code == 401
    assert get_response.status_code == 401
    assert smoke_response.status_code == 401


def test_user_can_list_only_own_jobs(client):
    owner_token = _register_and_login(client, "jobs-list-owner@example.com")
    other_token = _register_and_login(client, "jobs-list-other@example.com")

    db, session_generator = _get_test_db_session()
    try:
        owner_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.RAG_RETRIEVAL,
            input_payload={"query": "owner"},
        )
        create_job(
            db,
            owner_user_id=2,
            job_type=BackgroundJobType.QDRANT_INDEXING,
            input_payload={"scope": "other"},
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.get("/api/jobs", headers=_auth_headers(owner_token))

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["id"] == owner_job.id
    assert body[0]["owner_user_id"] == 1
    assert other_token


def test_user_can_read_own_job(client):
    token = _register_and_login(client, "jobs-read-own@example.com")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.EMBEDDING_GENERATION,
            input_payload={"chunk_id": 77},
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.get(f"/api/jobs/{background_job.id}", headers=_auth_headers(token))

    assert response.status_code == 200
    assert response.json()["id"] == background_job.id
    assert response.json()["event_log"] == []


def test_append_job_event_persists_structured_json_entries(client):
    token = _register_and_login(client, "jobs-event-log@example.com")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.RAG_SOURCE_INGESTION,
            input_payload={"source_id": 42},
        )
        append_job_event(
            db,
            job_id=background_job.id,
            stage="chunking",
            status="ok",
            details={"chunk_count": 3},
        )
        append_job_event(
            db,
            job_id=background_job.id,
            stage="embedding_generation",
            status="ok",
            details={"embedded_count": 3},
        )
        db.refresh(background_job)
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.get(f"/api/jobs/{background_job.id}", headers=_auth_headers(token))

    assert response.status_code == 200
    body = response.json()
    assert len(body["event_log"]) == 2
    assert body["event_log"][0]["stage"] == "chunking"
    assert body["event_log"][0]["status"] == "ok"
    assert body["event_log"][0]["details"] == {"chunk_count": 3}
    assert body["event_log"][1]["stage"] == "embedding_generation"
    assert "ts" in body["event_log"][0]


def test_cross_user_job_access_returns_404(client):
    owner_token = _register_and_login(client, "jobs-read-owner@example.com")
    other_token = _register_and_login(client, "jobs-read-other@example.com")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.QDRANT_INDEXING,
            input_payload={"source_id": 1},
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.get(f"/api/jobs/{background_job.id}", headers=_auth_headers(other_token))

    assert response.status_code == 404
    assert response.json()["detail"] == "Background job not found"
    assert owner_token


def test_create_job_creates_queued_job(client):
    token = _register_and_login(client, "jobs-create@example.com")
    profile_id = _create_profile(client, token, "Jobs Create Profile")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            profile_id=profile_id,
            job_type=BackgroundJobType.RAG_CHUNKING,
            input_payload={"source_id": 1},
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert background_job.status == BackgroundJobStatus.QUEUED.value
    assert background_job.progress_current == 0
    assert background_job.progress_total == 0


def test_mark_running_sets_running_and_started_at(client):
    _register_and_login(client, "jobs-running@example.com")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.MEDIA_PROCESSING,
            input_payload={},
        )
        updated_job = mark_running(
            db,
            job_id=background_job.id,
            celery_task_id="celery-123",
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert updated_job.status == BackgroundJobStatus.RUNNING.value
    assert updated_job.started_at is not None
    assert updated_job.celery_task_id == "celery-123"


def test_update_progress_updates_progress_fields(client):
    _register_and_login(client, "jobs-progress@example.com")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.VIDEO_GENERATION,
            input_payload={},
        )
        updated_job = update_progress(
            db,
            job_id=background_job.id,
            progress_current=2,
            progress_total=5,
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert updated_job.progress_current == 2
    assert updated_job.progress_total == 5


def test_mark_succeeded_sets_succeeded_finished_at_and_result_payload(client):
    _register_and_login(client, "jobs-succeeded@example.com")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.RAG_RETRIEVAL,
            input_payload={},
        )
        updated_job = mark_succeeded(
            db,
            job_id=background_job.id,
            result_payload={"results": 3},
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert updated_job.status == BackgroundJobStatus.SUCCEEDED.value
    assert updated_job.finished_at is not None
    assert updated_job.result_payload == {"results": 3}


def test_mark_failed_sets_failed_finished_at_and_error_fields(client):
    _register_and_login(client, "jobs-failed@example.com")

    db, session_generator = _get_test_db_session()
    try:
        background_job = create_job(
            db,
            owner_user_id=1,
            job_type=BackgroundJobType.VOICE_GENERATION,
            input_payload={},
        )
        updated_job = mark_failed(
            db,
            job_id=background_job.id,
            error_message="Worker failed",
            error_payload={"code": "worker_failed", "message": "Worker failed"},
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert updated_job.status == BackgroundJobStatus.FAILED.value
    assert updated_job.finished_at is not None
    assert updated_job.error_message == "Worker failed"
    assert updated_job.error_payload == {"code": "worker_failed", "message": "Worker failed"}


def test_celery_smoke_task_updates_job_status_in_test_mode_without_external_services(client, monkeypatch):
    token = _register_and_login(client, "jobs-smoke@example.com")
    profile_id = _create_profile(client, token, "Jobs Smoke Profile")

    monkeypatch.setattr("app.worker.tasks.get_session_factory", lambda: app.state.testing_session_local)
    monkeypatch.setattr(celery_app.conf, "task_always_eager", True)
    monkeypatch.setattr(celery_app.conf, "task_eager_propagates", True)

    response = client.post(
        "/api/jobs/smoke-test",
        headers=_auth_headers(token),
        json={"profile_id": profile_id},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["job_type"] == BackgroundJobType.SMOKE_TEST.value
    assert body["status"] == BackgroundJobStatus.SUCCEEDED.value
    assert body["progress_current"] == 3
    assert body["progress_total"] == 3
    assert body["result_payload"]["smoke_test"] is True


def test_backfill_service_is_idempotent(client):
    token = _register_and_login(client, "jobs-backfill@example.com")
    assert token

    db, session_generator = _get_test_db_session()
    try:
        first_summary = backfill_known_milestones(
            db,
            owner_user_id=1,
        )
        second_summary = backfill_known_milestones(
            db,
            owner_user_id=1,
        )
        milestone_jobs = db.query(BackgroundJob).filter(BackgroundJob.owner_user_id == 1).all()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert first_summary.created_count == 2
    assert second_summary.created_count == 0
    assert second_summary.skipped_count == 2
    assert len(milestone_jobs) == 2


def test_backfilled_milestones_are_system_milestone_and_succeeded(client):
    _register_and_login(client, "jobs-backfill-status@example.com")

    db, session_generator = _get_test_db_session()
    try:
        backfill_known_milestones(
            db,
            owner_user_id=1,
        )
        milestone_jobs = (
            db.query(BackgroundJob)
            .filter(BackgroundJob.owner_user_id == 1)
            .order_by(BackgroundJob.id.asc())
            .all()
        )
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert len(milestone_jobs) == 2
    assert all(job.job_type == BackgroundJobType.SYSTEM_MILESTONE.value for job in milestone_jobs)
    assert all(job.status == BackgroundJobStatus.SUCCEEDED.value for job in milestone_jobs)
    assert milestone_jobs[0].input_payload["task_number"] == 18
    assert milestone_jobs[0].input_payload["commit_hash"] == "a44be88"
    assert milestone_jobs[1].input_payload["task_number"] == 19
    assert milestone_jobs[1].input_payload["commit_hash"] == "b46e39c"


def test_project_progress_is_updated_for_job_tracking_foundation():
    project_progress_path = None
    for parent in Path(__file__).resolve().parents:
        candidate_path = parent / "PROJECT_PROGRESS.md"
        if candidate_path.exists():
            project_progress_path = candidate_path
            break

    if project_progress_path is None:
        return

    content = project_progress_path.read_text(encoding="utf-8")

    assert "Celery Job Tracking Foundation" in content

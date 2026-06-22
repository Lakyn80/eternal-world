from __future__ import annotations

from types import SimpleNamespace

from app.db.models import RagEmbedding
from app.db.session import get_db
from app.main import app
from app.modules.demo_smoke.service import (
    DEMO_EMAIL,
    DEMO_EXPECTED_MARKER,
    DEMO_PROFILE_NAME,
    DEMO_SOURCE_TEXT,
    DemoSmokeRunner,
)
from app.modules.demo_smoke.schemas import DemoSmokeConfig
from app.modules.rag_sources.repository import list_rag_sources_for_profile


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


class PassingFakeDemoSmokeRunner(DemoSmokeRunner):
    def ensure_demo_user(self):
        self._add_stage("user/profile", True, {"user_id": 1, "email": self.config.email})
        return SimpleNamespace(id=1, email=self.config.email)

    def ensure_demo_profile(self, user):
        self._add_stage("profile", True, {"profile_id": 10, "profile_name": self.config.profile_name})
        return SimpleNamespace(id=10, name=self.config.profile_name)

    def ensure_demo_source(self, user, profile):
        self._add_stage("source", True, {"source_id": 20})
        return SimpleNamespace(id=20, profile_id=profile.id)

    def trigger_pipeline(self, user, source):
        self._add_stage("job", True, {"job_id": 30, "celery_task_id": "fake-celery"})
        return SimpleNamespace(id=30)

    def wait_for_job_success(self, job_id):
        self._add_stage("job_status", True, {"job_id": job_id, "status": "succeeded"})
        return SimpleNamespace(id=job_id, status="succeeded")

    def verify_chunks(self, source):
        self._add_stage("chunks", True, {"chunk_count": 1})
        return 1

    def verify_embeddings(self, source):
        self._add_stage("embeddings", True, {"embedding_count": 1})
        return 1

    def verify_qdrant_indexing(self, source):
        self._add_stage("qdrant_indexing", True, {"index_count": 1})
        return 1

    def run_retrieval(self, user, profile):
        response = SimpleNamespace(
            profile_id=profile.id,
            query="demo",
            results=[SimpleNamespace(text=f"His favorite flower was {DEMO_EXPECTED_MARKER}.")],
        )
        self._add_stage("retrieval", True, {"result_count": 1})
        return response

    def run_chat(self, user, profile):
        response = SimpleNamespace(
            message_id=99,
            ai_response_text=f"The answer is grounded: {DEMO_EXPECTED_MARKER}.",
        )
        assistant_message = SimpleNamespace(
            message_metadata={
                "grounding_status": "grounded",
                "provider_name": "mock",
            }
        )
        self._add_stage("chat/brain_answer", True, {"message_id": response.message_id})
        return response, assistant_message


class MissingMarkerFakeDemoSmokeRunner(PassingFakeDemoSmokeRunner):
    def run_chat(self, user, profile):
        response = SimpleNamespace(
            message_id=99,
            ai_response_text="The answer does not include the expected evidence marker.",
        )
        assistant_message = SimpleNamespace(
            message_metadata={
                "grounding_status": "grounded",
                "provider_name": "mock",
            }
        )
        self._add_stage("chat/brain_answer", True, {"message_id": response.message_id})
        return response, assistant_message


def test_demo_smoke_uses_safe_fictional_data():
    assert DEMO_EMAIL.endswith("@example.test")
    assert DEMO_PROFILE_NAME == "Demo Grandfather"
    assert "fictional" in DEMO_SOURCE_TEXT.lower()
    assert "sunflower" in DEMO_SOURCE_TEXT.lower()
    assert "real personal" not in DEMO_SOURCE_TEXT.lower()


def test_demo_seed_is_idempotent_for_user_profile_and_source(client):
    db, session_generator = _get_test_db_session()
    try:
        runner = DemoSmokeRunner(db, DemoSmokeConfig())
        first_user = runner.ensure_demo_user()
        first_profile = runner.ensure_demo_profile(first_user)
        first_source = runner.ensure_demo_source(first_user, first_profile)

        second_user = runner.ensure_demo_user()
        second_profile = runner.ensure_demo_profile(second_user)
        second_source = runner.ensure_demo_source(second_user, second_profile)

        sources = list_rag_sources_for_profile(
            db,
            owner_user_id=first_user.id,
            profile_id=first_profile.id,
        )
    finally:
        _close_test_db_session(session_generator)

    assert second_user.id == first_user.id
    assert second_profile.id == first_profile.id
    assert second_source.id == first_source.id
    assert len([source for source in sources if source.title == "Demo Grandfather Memories"]) == 1


def test_demo_smoke_flow_returns_pass_when_all_required_stages_succeed(client):
    db, session_generator = _get_test_db_session()
    try:
        result = PassingFakeDemoSmokeRunner(db, DemoSmokeConfig()).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert {stage.name for stage in result.stages} >= {
        "chunks",
        "embeddings",
        "qdrant_indexing",
        "retrieval",
        "chat/brain_answer",
        "evaluation",
    }


def test_demo_smoke_flow_returns_fail_when_expected_evidence_marker_is_missing(client):
    db, session_generator = _get_test_db_session()
    try:
        result = MissingMarkerFakeDemoSmokeRunner(db, DemoSmokeConfig()).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is False
    assert any(stage.name == "chat_grounding" and not stage.passed for stage in result.stages)
    assert result.stages[-1].name == "final"


def test_demo_smoke_does_not_call_real_external_ai_apis(client, monkeypatch):
    from app.modules.ai_agents.brain.providers import openai_compatible

    def fail_http_client(*args, **kwargs):
        raise AssertionError("External AI HTTP client should not be used by demo smoke tests")

    monkeypatch.setattr(openai_compatible.httpx, "Client", fail_http_client)

    db, session_generator = _get_test_db_session()
    try:
        result = PassingFakeDemoSmokeRunner(db, DemoSmokeConfig()).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True


def test_demo_smoke_does_not_create_stored_query_embeddings(client):
    db, session_generator = _get_test_db_session()
    try:
        embeddings_before = db.query(RagEmbedding).count()
        result = PassingFakeDemoSmokeRunner(db, DemoSmokeConfig()).run()
        embeddings_after = db.query(RagEmbedding).count()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert embeddings_before == 0
    assert embeddings_after == 0

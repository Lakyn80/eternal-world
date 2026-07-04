from __future__ import annotations

from types import SimpleNamespace

from app.db.session import get_db
from app.main import app
from app.modules.production_hybrid_smoke.schemas import ProductionHybridSmokeConfig
from app.modules.production_hybrid_smoke.service import (
    PRODUCTION_HYBRID_EXPECTED_MARKER,
    PRODUCTION_HYBRID_MODEL_CODE,
    PRODUCTION_HYBRID_SMOKE_EMAIL,
    PRODUCTION_HYBRID_SOURCE_TEXT,
    ProductionHybridSmokeRunner,
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


class PassingFakeProductionHybridSmokeRunner(ProductionHybridSmokeRunner):
    def ensure_smoke_user(self):
        self._add_stage("user/profile", True, {"user_id": 1, "email": self.config.email})
        return SimpleNamespace(id=1, email=self.config.email)

    def ensure_smoke_profile(self, user):
        self._add_stage("profile", True, {"profile_id": 10, "profile_name": self.config.profile_name})
        return SimpleNamespace(id=10, name=self.config.profile_name)

    def ensure_smoke_source(self, user, profile):
        self._add_stage("source", True, {"source_id": 20})
        return SimpleNamespace(id=20, profile_id=profile.id)

    def verify_production_recommendation(self) -> None:
        self._add_stage(
            "production_recommendation",
            True,
            {"model_code": self.config.model_code},
        )

    def run_chunking(self, user, source):
        self._add_stage("chunk", True, {"chunk_count": 1})
        return 1

    def run_embedding(self, user, source):
        summary = SimpleNamespace(
            model_code=self.config.model_code,
            embedded_count=1,
            skipped_count=0,
            failed_count=0,
        )
        self._add_stage("embed", True, {"embedded_count": 1, "model_code": self.config.model_code})
        return summary

    def run_indexing(self, user, source):
        summary = SimpleNamespace(
            model_code=self.config.model_code,
            indexed_count=1,
            skipped_count=0,
            failed_count=0,
        )
        self._add_stage("index", True, {"indexed_count": 1, "model_code": self.config.model_code})
        return summary

    def verify_hybrid_embeddings(self, source) -> None:
        self._add_stage("hybrid_embeddings", True, {"embedding_count": 1})

    def verify_hybrid_indexing(self, source, indexing_summary) -> None:
        self._add_stage("hybrid_indexing", True, {"index_count": 1})

    def run_retrieval(self, user, profile):
        response = SimpleNamespace(
            profile_id=profile.id,
            query="hybrid smoke",
            model_code=self.config.model_code,
            results=[
                SimpleNamespace(
                    text=f"The {PRODUCTION_HYBRID_EXPECTED_MARKER} stayed in Prague.",
                    payload_metadata={"hybrid_retrieval": True, "sparse_vector": {"lantern": 1.0}},
                    qdrant_collection=f"eternal_world_rag_chunks__{self.config.model_code}",
                )
            ],
        )
        self._add_stage("retrieval", True, {"result_count": 1, "model_code": self.config.model_code})
        return response

    def run_chat(self, user, profile):
        response = SimpleNamespace(
            message_id=99,
            ai_response_text=(
                f"The {PRODUCTION_HYBRID_EXPECTED_MARKER} stayed tied to the cedar drawer in Prague."
            ),
        )
        assistant_message = SimpleNamespace(
            message_metadata={
                "grounding_status": "grounded",
                "provider_name": "mock",
            }
        )
        self._add_stage("chat/brain_answer", True, {"message_id": response.message_id})
        return response, assistant_message

    def run_evaluation(self, answer_text, metadata, retrieval_response) -> None:
        self._add_stage(
            "evaluation",
            True,
            {
                "case_id": "production-hybrid-smoke-grounded-answer",
                "actual_behavior": "grounded_answer",
                "evidence_count": len(retrieval_response.results),
            },
        )


class FailingHybridRetrievalRunner(PassingFakeProductionHybridSmokeRunner):
    def verify_hybrid_retrieval(self, retrieval_response) -> None:
        self._add_stage(
            "hybrid_retrieval",
            False,
            {"model_code": retrieval_response.model_code},
        )
        raise RuntimeError("Hybrid smoke retrieval did not satisfy production checks")


def test_production_hybrid_smoke_uses_safe_fictional_data():
    assert PRODUCTION_HYBRID_SMOKE_EMAIL.endswith("@example.test")
    assert PRODUCTION_HYBRID_MODEL_CODE == "bge_m3_dense_sparse"
    assert "fictional" in PRODUCTION_HYBRID_SOURCE_TEXT.lower()
    assert PRODUCTION_HYBRID_EXPECTED_MARKER in PRODUCTION_HYBRID_SOURCE_TEXT.lower()


def test_production_hybrid_smoke_flow_returns_pass_when_all_required_stages_succeed(client):
    db, session_generator = _get_test_db_session()
    try:
        result = PassingFakeProductionHybridSmokeRunner(
            db,
            ProductionHybridSmokeConfig(),
        ).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True
    assert {stage.name for stage in result.stages} >= {
        "chunk",
        "embed",
        "index",
        "hybrid_embeddings",
        "hybrid_indexing",
        "retrieval",
        "hybrid_retrieval",
        "chat/brain_answer",
        "chat_grounding",
        "evaluation",
    }


def test_production_hybrid_smoke_flow_returns_fail_when_hybrid_retrieval_checks_fail(client):
    db, session_generator = _get_test_db_session()
    try:
        result = FailingHybridRetrievalRunner(db, ProductionHybridSmokeConfig()).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is False
    assert any(stage.name == "hybrid_retrieval" and not stage.passed for stage in result.stages)
    assert result.stages[-1].name == "final"


def test_production_hybrid_smoke_does_not_call_real_external_ai_apis(client, monkeypatch):
    from app.modules.ai_agents.brain.providers import openai_compatible

    def fail_http_client(*args, **kwargs):
        raise AssertionError("External AI HTTP client should not be used by production hybrid smoke tests")

    monkeypatch.setattr(openai_compatible.httpx, "Client", fail_http_client)

    db, session_generator = _get_test_db_session()
    try:
        result = PassingFakeProductionHybridSmokeRunner(db, ProductionHybridSmokeConfig()).run()
    finally:
        _close_test_db_session(session_generator)

    assert result.passed is True

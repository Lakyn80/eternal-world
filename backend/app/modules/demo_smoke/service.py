from __future__ import annotations

import time
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import BackgroundJob, ChatMessage, MemoryProfile, RagChunk, RagEmbedding, RagSource, RagVectorIndex
from app.modules.ai_agents import get_agent_orchestrator
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import DuplicateEmailError, register_user
from app.modules.chat.schemas import ChatMessageCreate
from app.modules.chat.service import send_chat_message
from app.modules.demo_smoke.schemas import DemoSmokeConfig, DemoSmokeResult, DemoSmokeStageResult
from app.modules.job_tracking.enums import BackgroundJobStatus
from app.modules.job_tracking.repository import get_background_job_by_id
from app.modules.memory_profiles.repository import list_memory_profiles_for_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.rag_evaluation.evaluator import evaluate_answer_against_case
from app.modules.rag_evaluation.schemas import RagEvaluationCase, RagEvaluationProfileSetup
from app.modules.rag_pipeline.schemas import RagSourceProcessRequest
from app.modules.rag_pipeline.service import enqueue_rag_source_processing
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag
from app.modules.rag_sources.repository import list_rag_sources_for_profile
from app.modules.rag_sources.schemas import RagSourceCreate, RagSourceUpdate
from app.modules.rag_sources.service import create_rag_source, update_rag_source
from app.modules.users.repository import get_user_by_email


DEMO_EMAIL = "demo.e2e.smoke@example.test"
DEMO_PASSWORD = "DemoSmokePass123"
DEMO_PROFILE_NAME = "Demo Grandfather"
DEMO_SOURCE_TITLE = "Demo Grandfather Memories"
DEMO_SOURCE_KEY = "e2e_demo_smoke_v1"
DEMO_EXPECTED_MARKER = "sunflower"
DEMO_RETRIEVAL_QUERY = "What flower did he like? Was it sunflower?"
DEMO_CHAT_MESSAGE = DEMO_RETRIEVAL_QUERY
DEMO_SOURCE_TEXT = (
    "Demo Grandfather is a fictional person used only for backend smoke testing. "
    "He loved gardening and often told stories about summer evenings. "
    "His favorite flower was sunflower. "
    "These are safe synthetic facts for the Eternal World RAG demo smoke flow."
)


class DemoSmokeRunner:
    def __init__(self, db: Session, config: DemoSmokeConfig | None = None) -> None:
        self.db = db
        self.config = config or DemoSmokeConfig()
        self.stages: list[DemoSmokeStageResult] = []

    def run(self) -> DemoSmokeResult:
        self._force_safe_local_providers()
        try:
            user = self.ensure_demo_user()
            profile = self.ensure_demo_profile(user)
            source = self.ensure_demo_source(user, profile)
            background_job = self.trigger_pipeline(user, source)
            self.wait_for_job_success(background_job.id)
            self.verify_chunks(source)
            self.verify_embeddings(source)
            self.verify_qdrant_indexing(source)
            retrieval_response = self.run_retrieval(user, profile)
            self.verify_retrieval(retrieval_response)
            chat_response, assistant_message = self.run_chat(user, profile)
            self.verify_chat_answer(chat_response.ai_response_text, assistant_message.message_metadata or {})
            self.run_evaluation(chat_response.ai_response_text, assistant_message.message_metadata or {}, retrieval_response)
        except Exception as exc:
            self._add_stage(
                "final",
                False,
                error=f"{exc.__class__.__name__}: {exc}",
            )

        return DemoSmokeResult(
            passed=all(stage.passed for stage in self.stages),
            stages=self.stages,
        )

    def _force_safe_local_providers(self) -> None:
        settings.ai_brain_provider = "mock"
        get_agent_orchestrator.cache_clear()

    def _add_stage(
        self,
        name: str,
        passed: bool,
        details: dict[str, Any] | None = None,
        error: str | None = None,
    ) -> None:
        self.stages.append(
            DemoSmokeStageResult(
                name=name,
                passed=passed,
                details=details or {},
                error=error,
            )
        )

    def ensure_demo_user(self):
        user = get_user_by_email(self.db, self.config.email)
        reused = user is not None
        if user is None:
            try:
                user = register_user(
                    self.db,
                    RegisterRequest(
                        email=self.config.email,
                        password=DEMO_PASSWORD,
                        full_name="E2E Demo Smoke User",
                    ),
                )
            except DuplicateEmailError:
                user = get_user_by_email(self.db, self.config.email)

        if user is None:
            raise RuntimeError("Demo user could not be created or reused")

        self._add_stage(
            "user/profile",
            True,
            {"user_id": user.id, "email": user.email, "user_reused": reused},
        )
        return user

    def ensure_demo_profile(self, user) -> MemoryProfile:
        profiles = list_memory_profiles_for_user(self.db, user.id)
        profile = next((item for item in profiles if item.name == self.config.profile_name), None)
        reused = profile is not None
        if profile is None:
            profile = create_memory_profile(
                self.db,
                current_user=user,
                payload=MemoryProfileCreate(
                    name=self.config.profile_name,
                    biography="Safe fictional profile for backend E2E smoke testing.",
                    personality="Warm, concise, and factual.",
                ),
            )

        self._add_stage(
            "profile",
            True,
            {"profile_id": profile.id, "profile_name": profile.name, "profile_reused": reused},
        )
        return profile

    def ensure_demo_source(self, user, profile: MemoryProfile) -> RagSource:
        sources = list_rag_sources_for_profile(
            self.db,
            owner_user_id=user.id,
            profile_id=profile.id,
        )
        source = next(
            (
                item
                for item in sources
                if item.title == DEMO_SOURCE_TITLE
                and isinstance(item.source_metadata, dict)
                and item.source_metadata.get("demo_smoke_key") == DEMO_SOURCE_KEY
            ),
            None,
        )
        reused = source is not None
        metadata = {
            "demo_smoke_key": DEMO_SOURCE_KEY,
            "safe_fictional_data": True,
        }
        if source is None:
            source = create_rag_source(
                self.db,
                current_user=user,
                profile_id=profile.id,
                payload=RagSourceCreate(
                    title=DEMO_SOURCE_TITLE,
                    raw_text=DEMO_SOURCE_TEXT,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )
        elif source.raw_text != DEMO_SOURCE_TEXT or source.source_metadata != metadata:
            source = update_rag_source(
                self.db,
                current_user=user,
                source_id=source.id,
                payload=RagSourceUpdate(
                    title=DEMO_SOURCE_TITLE,
                    raw_text=DEMO_SOURCE_TEXT,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )

        self._add_stage(
            "source",
            True,
            {"source_id": source.id, "source_title": source.title, "source_reused": reused},
        )
        return source

    def trigger_pipeline(self, user, source: RagSource) -> BackgroundJob:
        background_job = enqueue_rag_source_processing(
            self.db,
            current_user=user,
            source_id=source.id,
            payload=RagSourceProcessRequest(),
        )
        self._add_stage(
            "job",
            True,
            {
                "job_id": background_job.id,
                "status": background_job.status,
                "celery_task_id": background_job.celery_task_id,
            },
        )
        return background_job

    def wait_for_job_success(self, job_id: int) -> BackgroundJob:
        deadline = time.monotonic() + self.config.timeout_seconds
        background_job = get_background_job_by_id(self.db, job_id=job_id)
        while time.monotonic() <= deadline:
            self.db.expire_all()
            background_job = get_background_job_by_id(self.db, job_id=job_id)
            if background_job is None:
                raise RuntimeError("Background job disappeared while polling")
            if background_job.status == BackgroundJobStatus.SUCCEEDED.value:
                self._add_stage(
                    "job_status",
                    True,
                    {
                        "job_id": background_job.id,
                        "status": background_job.status,
                        "progress_current": background_job.progress_current,
                        "progress_total": background_job.progress_total,
                    },
                )
                return background_job
            if background_job.status == BackgroundJobStatus.FAILED.value:
                raise RuntimeError(f"Background job failed: {background_job.error_payload}")
            time.sleep(self.config.poll_interval_seconds)

        status = background_job.status if background_job is not None else "missing"
        raise TimeoutError(f"Background job did not succeed before timeout; last status={status}")

    def verify_chunks(self, source: RagSource) -> int:
        count = self.db.scalar(select(RagChunk).where(RagChunk.source_id == source.id).limit(1))
        chunk_count = self.db.query(RagChunk).filter(RagChunk.source_id == source.id).count()
        passed = count is not None and chunk_count > 0
        self._add_stage("chunks", passed, {"source_id": source.id, "chunk_count": chunk_count})
        if not passed:
            raise RuntimeError("No chunks exist for demo source")
        return chunk_count

    def verify_embeddings(self, source: RagSource) -> int:
        embedding_count = (
            self.db.query(RagEmbedding)
            .filter(RagEmbedding.source_id == source.id, RagEmbedding.status == "embedded")
            .count()
        )
        passed = embedding_count > 0
        self._add_stage("embeddings", passed, {"source_id": source.id, "embedding_count": embedding_count})
        if not passed:
            raise RuntimeError("No embedded records exist for demo source")
        return embedding_count

    def verify_qdrant_indexing(self, source: RagSource) -> int:
        index_count = (
            self.db.query(RagVectorIndex)
            .filter(RagVectorIndex.source_id == source.id, RagVectorIndex.status == "indexed")
            .count()
        )
        passed = index_count > 0
        self._add_stage("qdrant_indexing", passed, {"source_id": source.id, "index_count": index_count})
        if not passed:
            raise RuntimeError("No indexed Qdrant records exist for demo source")
        return index_count

    def run_retrieval(self, user, profile: MemoryProfile):
        retrieval_response = retrieve_profile_rag(
            self.db,
            current_user=user,
            profile_id=profile.id,
            payload=RagRetrievalRequest(query=DEMO_RETRIEVAL_QUERY, limit=5),
        )
        self._add_stage(
            "retrieval",
            bool(retrieval_response.results),
            {
                "profile_id": profile.id,
                "query": retrieval_response.query,
                "result_count": len(retrieval_response.results),
            },
        )
        if not retrieval_response.results:
            raise RuntimeError("Retrieval returned no demo evidence")
        return retrieval_response

    def verify_retrieval(self, retrieval_response) -> None:
        marker_found = any(
            DEMO_EXPECTED_MARKER in result.text.lower()
            for result in retrieval_response.results
        )
        self._add_stage(
            "retrieval_marker",
            marker_found,
            {"expected_marker": DEMO_EXPECTED_MARKER},
        )
        if not marker_found:
            raise RuntimeError(f"Retrieval did not return expected marker: {DEMO_EXPECTED_MARKER}")

    def run_chat(self, user, profile: MemoryProfile):
        chat_response = send_chat_message(
            self.db,
            current_user=user,
            profile_id=profile.id,
            payload=ChatMessageCreate(message=DEMO_CHAT_MESSAGE),
        )
        assistant_message = self.db.get(ChatMessage, chat_response.message_id)
        if assistant_message is None:
            raise RuntimeError("Assistant chat message was not persisted")

        self._add_stage(
            "chat/brain_answer",
            True,
            {
                "message_id": chat_response.message_id,
                "answer_preview": chat_response.ai_response_text[:160],
                "grounding_status": (assistant_message.message_metadata or {}).get("grounding_status"),
            },
        )
        return chat_response, assistant_message

    def verify_chat_answer(self, answer_text: str, metadata: dict[str, Any]) -> None:
        marker_found = DEMO_EXPECTED_MARKER in answer_text.lower()
        grounded = metadata.get("grounding_status") == "grounded"
        passed = marker_found and grounded
        self._add_stage(
            "chat_grounding",
            passed,
            {
                "expected_marker": DEMO_EXPECTED_MARKER,
                "marker_found": marker_found,
                "grounding_status": metadata.get("grounding_status"),
            },
        )
        if not passed:
            raise RuntimeError("Chat answer did not satisfy demo grounding checks")

    def run_evaluation(self, answer_text: str, metadata: dict[str, Any], retrieval_response) -> None:
        case = RagEvaluationCase(
            case_id="e2e-demo-smoke-grounded-answer",
            title="E2E demo smoke grounded answer",
            profile=RagEvaluationProfileSetup(
                profile_id=retrieval_response.profile_id,
                name=self.config.profile_name,
            ),
            user_query=DEMO_CHAT_MESSAGE,
            expected_behavior="grounded_answer",
            expected_evidence_markers=[DEMO_EXPECTED_MARKER],
            forbidden_claims=["favorite car"],
            minimum_required_evidence_count=1,
        )
        evaluation_result = evaluate_answer_against_case(
            case=case,
            answer_text=answer_text,
            provider_name=str(metadata.get("provider_name") or "unknown"),
            response_metadata=metadata,
            evidence_count=len(retrieval_response.results),
        )
        self._add_stage(
            "evaluation",
            evaluation_result.passed,
            {
                "case_id": evaluation_result.case_id,
                "actual_behavior": evaluation_result.actual_behavior,
                "evidence_count": evaluation_result.evidence_count,
                "reasons": evaluation_result.reasons,
            },
        )
        if not evaluation_result.passed:
            raise RuntimeError("RAG evaluation harness failed demo answer")


def run_demo_smoke(db: Session, config: DemoSmokeConfig | None = None) -> DemoSmokeResult:
    return DemoSmokeRunner(db, config).run()

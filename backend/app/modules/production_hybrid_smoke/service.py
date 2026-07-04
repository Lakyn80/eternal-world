from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import ChatMessage, MemoryProfile, RagEmbedding, RagSource, RagVectorIndex
from app.modules.active_retrieval_config.service import get_production_recommended_active_retrieval_config
from app.modules.ai_agents import get_agent_orchestrator
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import DuplicateEmailError, register_user
from app.modules.chat.schemas import ChatMessageCreate
from app.modules.chat.service import send_chat_message
from app.modules.embedding_models.registry import BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE
from app.modules.embeddings.service import embed_source_chunks
from app.modules.memory_profiles.repository import list_memory_profiles_for_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.production_hybrid_smoke.schemas import (
    ProductionHybridSmokeConfig,
    ProductionHybridSmokeResult,
    ProductionHybridSmokeStageResult,
)
from app.modules.qdrant_indexing.service import index_source_embeddings
from app.modules.rag_chunks.service import chunk_rag_source
from app.modules.rag_retrieval.hybrid import SPARSE_VECTOR_PAYLOAD_KEY
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag
from app.modules.rag_sources.repository import list_rag_sources_for_profile
from app.modules.rag_sources.schemas import RagSourceCreate, RagSourceUpdate
from app.modules.rag_sources.service import create_rag_source, update_rag_source
from app.modules.rag_evaluation.evaluator import evaluate_answer_against_case
from app.modules.rag_evaluation.schemas import RagEvaluationCase, RagEvaluationProfileSetup
from app.modules.users.repository import get_user_by_email


PRODUCTION_HYBRID_MODEL_CODE = BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE
PRODUCTION_HYBRID_SMOKE_EMAIL = "production.hybrid.smoke@example.test"
PRODUCTION_HYBRID_SMOKE_PASSWORD = "HybridSmokePass123"
PRODUCTION_HYBRID_SMOKE_PROFILE_NAME = "Production Hybrid Smoke Profile"
PRODUCTION_HYBRID_SOURCE_TITLE = "Production Hybrid Smoke Source"
PRODUCTION_HYBRID_SOURCE_KEY = "production_hybrid_smoke_v1"
PRODUCTION_HYBRID_EXPECTED_MARKER = "lantern archive"
PRODUCTION_HYBRID_RETRIEVAL_QUERY = "Which lantern archive stayed tied to the cedar drawer in Prague?"
PRODUCTION_HYBRID_CHAT_MESSAGE = PRODUCTION_HYBRID_RETRIEVAL_QUERY
PRODUCTION_HYBRID_SOURCE_TEXT = (
    "This is safe fictional smoke data for Eternal World production hybrid retrieval. "
    "The lantern archive stayed tied to the cedar drawer in Prague during every winter trip. "
    "The brass tag remained on the archive cart for deterministic hybrid retrieval smoke checks."
)


class ProductionHybridSmokeRunner:
    def __init__(self, db: Session, config: ProductionHybridSmokeConfig | None = None) -> None:
        self.db = db
        self.config = config or ProductionHybridSmokeConfig()
        self.stages: list[ProductionHybridSmokeStageResult] = []

    def run(self) -> ProductionHybridSmokeResult:
        self._force_safe_local_providers()
        try:
            user = self.ensure_smoke_user()
            profile = self.ensure_smoke_profile(user)
            source = self.ensure_smoke_source(user, profile)
            self.verify_production_recommendation()
            chunk_count = self.run_chunking(user, source)
            embedding_summary = self.run_embedding(user, source)
            indexing_summary = self.run_indexing(user, source)
            self.verify_hybrid_embeddings(source)
            self.verify_hybrid_indexing(source, indexing_summary)
            retrieval_response = self.run_retrieval(user, profile)
            self.verify_hybrid_retrieval(retrieval_response)
            chat_response, assistant_message = self.run_chat(user, profile)
            self.verify_chat_answer(chat_response.ai_response_text, assistant_message.message_metadata or {})
            self.run_evaluation(
                chat_response.ai_response_text,
                assistant_message.message_metadata or {},
                retrieval_response,
            )
        except Exception as exc:
            self._add_stage(
                "final",
                False,
                error=f"{exc.__class__.__name__}: {exc}",
            )

        return ProductionHybridSmokeResult(
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
            ProductionHybridSmokeStageResult(
                name=name,
                passed=passed,
                details=details or {},
                error=error,
            )
        )

    def ensure_smoke_user(self):
        user = get_user_by_email(self.db, self.config.email)
        reused = user is not None
        if user is None:
            try:
                user = register_user(
                    self.db,
                    RegisterRequest(
                        email=self.config.email,
                        password=PRODUCTION_HYBRID_SMOKE_PASSWORD,
                        full_name="Production Hybrid Smoke User",
                    ),
                )
            except DuplicateEmailError:
                user = get_user_by_email(self.db, self.config.email)

        if user is None:
            raise RuntimeError("Production hybrid smoke user could not be created or reused")

        self._add_stage(
            "user/profile",
            True,
            {"user_id": user.id, "email": user.email, "user_reused": reused},
        )
        return user

    def ensure_smoke_profile(self, user) -> MemoryProfile:
        profiles = list_memory_profiles_for_user(self.db, user.id)
        profile = next((item for item in profiles if item.name == self.config.profile_name), None)
        reused = profile is not None
        if profile is None:
            profile = create_memory_profile(
                self.db,
                current_user=user,
                payload=MemoryProfileCreate(
                    name=self.config.profile_name,
                    biography="Safe fictional profile for production hybrid smoke testing.",
                    personality="Warm, concise, and factual.",
                ),
            )

        self._add_stage(
            "profile",
            True,
            {"profile_id": profile.id, "profile_name": profile.name, "profile_reused": reused},
        )
        return profile

    def ensure_smoke_source(self, user, profile: MemoryProfile) -> RagSource:
        sources = list_rag_sources_for_profile(
            self.db,
            owner_user_id=user.id,
            profile_id=profile.id,
        )
        source = next(
            (
                item
                for item in sources
                if item.title == PRODUCTION_HYBRID_SOURCE_TITLE
                and isinstance(item.source_metadata, dict)
                and item.source_metadata.get("production_hybrid_smoke_key") == PRODUCTION_HYBRID_SOURCE_KEY
            ),
            None,
        )
        reused = source is not None
        metadata = {
            "production_hybrid_smoke_key": PRODUCTION_HYBRID_SOURCE_KEY,
            "safe_fictional_data": True,
        }
        if source is None:
            source = create_rag_source(
                self.db,
                current_user=user,
                profile_id=profile.id,
                payload=RagSourceCreate(
                    title=PRODUCTION_HYBRID_SOURCE_TITLE,
                    raw_text=PRODUCTION_HYBRID_SOURCE_TEXT,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )
        elif source.raw_text != PRODUCTION_HYBRID_SOURCE_TEXT or source.source_metadata != metadata:
            source = update_rag_source(
                self.db,
                current_user=user,
                source_id=source.id,
                payload=RagSourceUpdate(
                    title=PRODUCTION_HYBRID_SOURCE_TITLE,
                    raw_text=PRODUCTION_HYBRID_SOURCE_TEXT,
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

    def verify_production_recommendation(self) -> None:
        recommendation = get_production_recommended_active_retrieval_config()
        passed = (
            recommendation.model_code == self.config.model_code
            and recommendation.retrieval_mode == self.config.model_code
        )
        self._add_stage(
            "production_recommendation",
            passed,
            {
                "model_code": recommendation.model_code,
                "retrieval_mode": recommendation.retrieval_mode,
                "collection_name": recommendation.collection_name,
            },
        )
        if not passed:
            raise RuntimeError("Production recommendation does not match hybrid smoke model")

    def run_chunking(self, user, source: RagSource) -> int:
        chunk_summary = chunk_rag_source(
            self.db,
            current_user=user,
            source_id=source.id,
        )
        passed = chunk_summary.chunk_count > 0
        self._add_stage(
            "chunk",
            passed,
            {
                "source_id": source.id,
                "chunk_count": chunk_summary.chunk_count,
                "valid_count": chunk_summary.valid_count,
            },
        )
        if not passed:
            raise RuntimeError("Hybrid smoke chunking did not produce any chunks")
        return chunk_summary.chunk_count

    def run_embedding(self, user, source: RagSource):
        embedding_summary = embed_source_chunks(
            self.db,
            current_user=user,
            source_id=source.id,
            model_code=self.config.model_code,
        )
        passed = embedding_summary.embedded_count > 0
        self._add_stage(
            "embed",
            passed,
            {
                "source_id": source.id,
                "model_code": embedding_summary.model_code,
                "embedded_count": embedding_summary.embedded_count,
                "skipped_count": embedding_summary.skipped_count,
                "failed_count": embedding_summary.failed_count,
            },
        )
        if not passed:
            raise RuntimeError("Hybrid smoke embedding did not produce embedded records")
        return embedding_summary

    def run_indexing(self, user, source: RagSource):
        indexing_summary = index_source_embeddings(
            self.db,
            current_user=user,
            source_id=source.id,
            model_code=self.config.model_code,
        )
        passed = indexing_summary.indexed_count > 0
        self._add_stage(
            "index",
            passed,
            {
                "source_id": source.id,
                "model_code": indexing_summary.model_code,
                "indexed_count": indexing_summary.indexed_count,
                "skipped_count": indexing_summary.skipped_count,
                "failed_count": indexing_summary.failed_count,
            },
        )
        if not passed:
            raise RuntimeError("Hybrid smoke indexing did not produce indexed records")
        return indexing_summary

    def verify_hybrid_embeddings(self, source: RagSource) -> None:
        hybrid_embedding_count = (
            self.db.query(RagEmbedding)
            .filter(
                RagEmbedding.source_id == source.id,
                RagEmbedding.model_code == self.config.model_code,
                RagEmbedding.status == "embedded",
            )
            .count()
        )
        passed = hybrid_embedding_count > 0
        self._add_stage(
            "hybrid_embeddings",
            passed,
            {
                "source_id": source.id,
                "model_code": self.config.model_code,
                "embedding_count": hybrid_embedding_count,
            },
        )
        if not passed:
            raise RuntimeError("No hybrid-model embeddings exist for smoke source")

    def verify_hybrid_indexing(self, source: RagSource, indexing_summary) -> None:
        expected_collection = f"{settings.qdrant_collection_name}__{self.config.model_code}"
        index_count = (
            self.db.query(RagVectorIndex)
            .filter(
                RagVectorIndex.source_id == source.id,
                RagVectorIndex.model_code == self.config.model_code,
                RagVectorIndex.status == "indexed",
                RagVectorIndex.qdrant_collection == expected_collection,
            )
            .count()
        )
        passed = index_count > 0
        self._add_stage(
            "hybrid_indexing",
            passed,
            {
                "source_id": source.id,
                "model_code": self.config.model_code,
                "collection_name": expected_collection,
                "index_count": index_count,
                "indexed_count": indexing_summary.indexed_count,
                "sparse_payload_key": SPARSE_VECTOR_PAYLOAD_KEY,
            },
        )
        if not passed:
            raise RuntimeError("No hybrid-model Qdrant indexes exist for smoke source")

    def run_retrieval(self, user, profile: MemoryProfile):
        retrieval_response = retrieve_profile_rag(
            self.db,
            current_user=user,
            profile_id=profile.id,
            payload=RagRetrievalRequest(
                query=PRODUCTION_HYBRID_RETRIEVAL_QUERY,
                limit=5,
            ),
        )
        self._add_stage(
            "retrieval",
            bool(retrieval_response.results),
            {
                "profile_id": profile.id,
                "query": retrieval_response.query,
                "model_code": retrieval_response.model_code,
                "result_count": len(retrieval_response.results),
            },
        )
        if not retrieval_response.results:
            raise RuntimeError("Hybrid smoke retrieval returned no evidence")
        return retrieval_response

    def verify_hybrid_retrieval(self, retrieval_response) -> None:
        first_result = retrieval_response.results[0]
        marker_found = any(
            PRODUCTION_HYBRID_EXPECTED_MARKER in result.text.lower()
            for result in retrieval_response.results
        )
        hybrid_metadata = first_result.payload_metadata.get("hybrid_retrieval") is True
        sparse_metadata_present = SPARSE_VECTOR_PAYLOAD_KEY in first_result.payload_metadata or hybrid_metadata
        passed = (
            retrieval_response.model_code == self.config.model_code
            and marker_found
            and hybrid_metadata
        )
        self._add_stage(
            "hybrid_retrieval",
            passed,
            {
                "model_code": retrieval_response.model_code,
                "expected_model_code": self.config.model_code,
                "expected_marker": PRODUCTION_HYBRID_EXPECTED_MARKER,
                "marker_found": marker_found,
                "hybrid_retrieval": hybrid_metadata,
                "sparse_payload_key": SPARSE_VECTOR_PAYLOAD_KEY,
                "sparse_metadata_present": sparse_metadata_present,
                "collection_name": first_result.qdrant_collection,
            },
        )
        if not passed:
            raise RuntimeError("Hybrid smoke retrieval did not satisfy production checks")

    def run_chat(self, user, profile: MemoryProfile):
        chat_response = send_chat_message(
            self.db,
            current_user=user,
            profile_id=profile.id,
            payload=ChatMessageCreate(message=PRODUCTION_HYBRID_CHAT_MESSAGE),
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
        marker_found = PRODUCTION_HYBRID_EXPECTED_MARKER in answer_text.lower()
        grounded = metadata.get("grounding_status") == "grounded"
        passed = marker_found and grounded and bool(answer_text.strip())
        self._add_stage(
            "chat_grounding",
            passed,
            {
                "expected_marker": PRODUCTION_HYBRID_EXPECTED_MARKER,
                "marker_found": marker_found,
                "grounding_status": metadata.get("grounding_status"),
                "answer_preview": answer_text[:160],
            },
        )
        if not passed:
            raise RuntimeError("Hybrid smoke chat answer did not satisfy grounding checks")

    def run_evaluation(
        self,
        answer_text: str,
        metadata: dict[str, Any],
        retrieval_response,
    ) -> None:
        case = RagEvaluationCase(
            case_id="production-hybrid-smoke-grounded-answer",
            title="Production hybrid smoke grounded answer",
            profile=RagEvaluationProfileSetup(
                profile_id=retrieval_response.profile_id,
                name=self.config.profile_name,
            ),
            user_query=PRODUCTION_HYBRID_CHAT_MESSAGE,
            expected_behavior="grounded_answer",
            expected_evidence_markers=[PRODUCTION_HYBRID_EXPECTED_MARKER, "Prague"],
            forbidden_claims=["favorite car", "Berlin"],
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
            raise RuntimeError("RAG evaluation harness failed production hybrid smoke answer")


def run_production_hybrid_smoke(
    db: Session,
    config: ProductionHybridSmokeConfig | None = None,
) -> ProductionHybridSmokeResult:
    return ProductionHybridSmokeRunner(db, config).run()

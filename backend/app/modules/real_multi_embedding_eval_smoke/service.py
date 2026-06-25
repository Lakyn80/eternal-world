from __future__ import annotations

from contextlib import contextmanager
from types import SimpleNamespace

from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import ActiveRetrievalConfig, User
from app.modules.active_retrieval_config.service import (
    activate_best_multi_embedding_eval_result,
    get_active_retrieval_config,
)
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import DuplicateEmailError, register_user
from app.modules.embedding_models.registry import DEFAULT_EMBEDDING_MODEL_CODE
from app.modules.embeddings.providers.sentence_transformers import (
    BGE_M3_MODEL_NAME,
    E5_SMALL_MODEL_NAME,
)
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.memory_profiles.repository import list_memory_profiles_for_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.multi_embedding_eval.schemas import MultiEmbeddingEvalRequest
from app.modules.multi_embedding_eval.service import WORKFLOW_NAME, process_multi_embedding_eval_job
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag
from app.modules.rag_sources.repository import list_rag_sources_for_profile
from app.modules.rag_sources.schemas import RagSourceCreate, RagSourceUpdate
from app.modules.rag_sources.service import create_rag_source, update_rag_source
from app.modules.real_multi_embedding_eval_smoke.schemas import (
    RealMultiEmbeddingEvalSmokeCandidateResult,
    RealMultiEmbeddingEvalSmokeConfig,
    RealMultiEmbeddingEvalSmokeResult,
)
from app.modules.users.repository import get_user_by_email


SMOKE_EMAIL = "demo.multi.embedding.smoke@example.test"
SMOKE_PASSWORD = "RealMultiEmbeddingSmokePass123"
SMOKE_PROFILE_NAME = "Demo Multi Embedding Profile"
SMOKE_SOURCE_TITLE = "Demo Multi Embedding Evaluation Source"
SMOKE_SOURCE_KEY = "real_multi_embedding_eval_smoke_v1"
SMOKE_EXPECTED_MARKER = "sunflower"
SMOKE_QUERY = "Which flower did the demo traveler love? Was it sunflower?"
SMOKE_SOURCE_TEXT = " ".join(
    [
        "This is safe fictional smoke-test data for the Eternal World retrieval evaluation pipeline."
    ]
    + [
        f"Archive filler sentence number {index} keeps the demo source long enough for chunking."
        for index in range(1, 25)
    ]
    + [
        "The demo traveler loved sunflower and wrote that sunflower was the favorite flower.",
    ]
    + [
        f"Additional filler sentence number {index} preserves a separate distractor chunk for deterministic comparison."
        for index in range(25, 49)
    ]
)


class _SmokeFakeSentenceTransformer:
    def __init__(self, model_name: str, *, device: str = "cpu", cache_folder: str | None = None):
        self.model_name = model_name
        self.device = device
        self.cache_folder = cache_folder

    def encode(self, texts, **kwargs):
        return [
            _build_fake_vector(str(text), self.model_name)
            for text in list(texts)
        ]


def _build_fake_vector(text: str, model_name: str) -> list[float]:
    normalized_text = " ".join(text.lower().split())
    if model_name == E5_SMALL_MODEL_NAME:
        dimension = 384
        if normalized_text.startswith("query:"):
            anchor = "distractor"
        elif SMOKE_EXPECTED_MARKER in normalized_text:
            anchor = "relevant"
        else:
            anchor = "distractor"
    elif model_name == BGE_M3_MODEL_NAME:
        dimension = 1024
        if SMOKE_EXPECTED_MARKER in normalized_text:
            anchor = "relevant"
        else:
            anchor = "distractor"
    else:
        dimension = 8
        anchor = "distractor"

    vector = [0.0] * dimension
    if dimension >= 2:
        if anchor == "relevant":
            vector[0] = 1.0
            vector[1] = 0.0
        else:
            vector[0] = 0.0
            vector[1] = 1.0

    return vector


class RealMultiEmbeddingEvalSmokeRunner:
    def __init__(self, db: Session, config: RealMultiEmbeddingEvalSmokeConfig | None = None) -> None:
        self.db = db
        self.config = config or RealMultiEmbeddingEvalSmokeConfig()

    @contextmanager
    def _embedding_runtime(self):
        from app.modules.embeddings.providers import sentence_transformers as sentence_transformers_provider

        original_embedding_provider = settings.embedding_provider
        original_import_module = sentence_transformers_provider.import_module
        settings.embedding_provider = "sentence_transformers"
        if not self.config.use_real_local_models:
            sentence_transformers_provider.import_module = (
                lambda module_name: SimpleNamespace(SentenceTransformer=_SmokeFakeSentenceTransformer)
            )

        try:
            yield
        finally:
            settings.embedding_provider = original_embedding_provider
            sentence_transformers_provider.import_module = original_import_module

    def run(self) -> RealMultiEmbeddingEvalSmokeResult:
        try:
            with self._embedding_runtime():
                user = self.ensure_user()
                profile = self.ensure_profile(user)
                source = self.ensure_source(user, profile)
                request_payload = self.build_request()
                background_job = self.create_job(user, profile_id=profile.id, source_id=source.id, payload=request_payload)
                process_result = process_multi_embedding_eval_job(self.db, job_id=background_job.id)
                activated_config = activate_best_multi_embedding_eval_result(
                    self.db,
                    current_user=user,
                    source_id=source.id,
                    job_id=background_job.id,
                )
                runtime_config = get_active_retrieval_config(
                    self.db,
                    current_user=user,
                    profile_id=profile.id,
                )
                runtime_retrieval = retrieve_profile_rag(
                    self.db,
                    current_user=user,
                    profile_id=profile.id,
                    payload=RagRetrievalRequest(query=SMOKE_QUERY),
                )
        except Exception as exc:
            return RealMultiEmbeddingEvalSmokeResult(
                passed=False,
                used_fake_models=not self.config.use_real_local_models,
                error=f"{exc.__class__.__name__}: {exc}",
            )

        result_payload = process_result.get("result_payload") or {}
        best_config = result_payload.get("best_config")
        all_config_scores = result_payload.get("all_config_scores") or []
        scores_by_config_id = {
            str(item.get("config_id")): item.get("metrics")
            for item in all_config_scores
            if isinstance(item, dict)
        }
        candidate_results = []
        for item in result_payload.get("candidate_execution_results") or []:
            if not isinstance(item, dict):
                continue
            if item.get("status") != "succeeded":
                continue
            candidate_results.append(
                RealMultiEmbeddingEvalSmokeCandidateResult(
                    candidate=str(item.get("model_code") or ""),
                    status="evaluated",
                    collection=str(item.get("collection_name") or ""),
                    metrics=scores_by_config_id.get(str(item.get("config_id") or "")),
                )
            )

        runtime_collection = None
        marker_found = False
        if runtime_retrieval.results:
            runtime_collection = runtime_retrieval.results[0].qdrant_collection
            marker_found = any(
                SMOKE_EXPECTED_MARKER in result.text.lower()
                for result in runtime_retrieval.results
            )

        passed = (
            len(candidate_results) == 2
            and len({item.collection for item in candidate_results}) == 2
            and best_config is not None
            and activated_config.model_code == best_config.get("best_model_code")
            and runtime_config.model_code == activated_config.model_code
            and runtime_config.collection_name == activated_config.collection_name
            and runtime_retrieval.model_code == activated_config.model_code
            and runtime_collection == activated_config.collection_name
            and marker_found
        )

        return RealMultiEmbeddingEvalSmokeResult(
            passed=passed,
            used_fake_models=not self.config.use_real_local_models,
            profile_id=profile.id,
            source_id=source.id,
            job_id=background_job.id,
            candidates=candidate_results,
            best_config=best_config if isinstance(best_config, dict) else None,
            activated=passed or runtime_config.id is not None,
            runtime_active_config=_serialize_active_config(runtime_config),
            runtime_retrieval={
                "model_code": runtime_retrieval.model_code,
                "result_count": len(runtime_retrieval.results),
                "qdrant_collection": runtime_collection,
                "marker_found": marker_found,
            },
            warnings=[str(item.get("message")) for item in result_payload.get("warnings") or [] if isinstance(item, dict)],
            error=None if passed else "Multi-embedding smoke verification failed",
        )

    def ensure_user(self) -> User:
        user = get_user_by_email(self.db, self.config.email)
        if user is None:
            try:
                user = register_user(
                    self.db,
                    RegisterRequest(
                        email=self.config.email,
                        password=SMOKE_PASSWORD,
                        full_name="Real Multi Embedding Smoke User",
                    ),
                )
            except DuplicateEmailError:
                user = get_user_by_email(self.db, self.config.email)

        if user is None:
            raise RuntimeError("Smoke user could not be created or reused")

        return user

    def ensure_profile(self, user: User):
        profiles = list_memory_profiles_for_user(self.db, user.id)
        profile = next((item for item in profiles if item.name == self.config.profile_name), None)
        if profile is None:
            profile = create_memory_profile(
                self.db,
                current_user=user,
                payload=MemoryProfileCreate(
                    name=self.config.profile_name,
                    biography="Safe fictional profile for multi-embedding smoke validation.",
                    personality="Deterministic smoke-test fixture.",
                ),
            )

        return profile

    def ensure_source(self, user: User, profile):
        sources = list_rag_sources_for_profile(
            self.db,
            owner_user_id=user.id,
            profile_id=profile.id,
        )
        metadata = {
            "real_multi_embedding_eval_smoke_key": SMOKE_SOURCE_KEY,
            "safe_fictional_data": True,
        }
        source = next(
            (
                item
                for item in sources
                if item.title == SMOKE_SOURCE_TITLE
                and isinstance(item.source_metadata, dict)
                and item.source_metadata.get("real_multi_embedding_eval_smoke_key") == SMOKE_SOURCE_KEY
            ),
            None,
        )
        if source is None:
            source = create_rag_source(
                self.db,
                current_user=user,
                profile_id=profile.id,
                payload=RagSourceCreate(
                    title=SMOKE_SOURCE_TITLE,
                    raw_text=SMOKE_SOURCE_TEXT,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )
        elif source.raw_text != SMOKE_SOURCE_TEXT or source.source_metadata != metadata:
            source = update_rag_source(
                self.db,
                current_user=user,
                source_id=source.id,
                payload=RagSourceUpdate(
                    title=SMOKE_SOURCE_TITLE,
                    raw_text=SMOKE_SOURCE_TEXT,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )

        return source

    def build_request(self) -> MultiEmbeddingEvalRequest:
        collection_prefix = settings.qdrant_collection_name
        return MultiEmbeddingEvalRequest(
            dataset={
                "dataset_id": "real-multi-embedding-smoke-dataset",
                "name": "Real Multi Embedding Smoke Dataset",
                "cases": [
                    {
                        "case_id": "case-sunflower",
                        "title": "Sunflower retrieval case",
                        "query": SMOKE_QUERY,
                        "expected_markers": [SMOKE_EXPECTED_MARKER],
                        "expected_behavior": "retrieval_only",
                        "minimum_relevant_results": 1,
                    }
                ],
            },
            candidates=[
                {
                    "config_id": DEFAULT_EMBEDDING_MODEL_CODE,
                    "model_code": DEFAULT_EMBEDDING_MODEL_CODE,
                    "collection_name": f"{collection_prefix}__multilingual_e5_small__real_multi_eval_smoke",
                    "top_k": 1,
                    "retrieval_mode": "hybrid",
                },
                {
                    "config_id": "bge_m3",
                    "model_code": "bge_m3",
                    "collection_name": f"{collection_prefix}__bge_m3__real_multi_eval_smoke",
                    "top_k": 1,
                    "retrieval_mode": "hybrid",
                },
            ],
        )

    def create_job(
        self,
        user: User,
        *,
        profile_id: int,
        source_id: int,
        payload: MultiEmbeddingEvalRequest,
    ):
        return create_job(
            self.db,
            owner_user_id=user.id,
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
            progress_total=len(payload.candidates) * 4,
        )


def _serialize_active_config(active_config: ActiveRetrievalConfig) -> dict[str, object]:
    return {
        "id": active_config.id,
        "profile_id": active_config.profile_id,
        "model_code": active_config.model_code,
        "collection_name": active_config.collection_name,
        "top_k": active_config.top_k,
        "score_threshold": active_config.score_threshold,
        "retrieval_mode": active_config.retrieval_mode,
        "source_eval_job_id": active_config.source_eval_job_id,
        "source_eval_dataset_id": active_config.source_eval_dataset_id,
    }


def run_real_multi_embedding_eval_smoke(
    db: Session,
    config: RealMultiEmbeddingEvalSmokeConfig | None = None,
) -> RealMultiEmbeddingEvalSmokeResult:
    return RealMultiEmbeddingEvalSmokeRunner(db, config).run()

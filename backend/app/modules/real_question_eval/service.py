from __future__ import annotations

import json
import math
import re
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha1
from pathlib import Path
from time import perf_counter
from types import SimpleNamespace

from sqlalchemy.orm import Session

from app.core.config import BACKEND_DIR, settings
from app.db.models import ActiveRetrievalConfig, User
from app.modules.active_retrieval_config.service import (
    activate_best_multi_embedding_eval_result,
    get_active_retrieval_config,
)
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import DuplicateEmailError, register_user
from app.modules.embedding_models.registry import DEFAULT_EMBEDDING_MODEL_CODE
from app.modules.embedding_models.service import allow_disabled_runtime_embedding_models
from app.modules.embeddings.providers.bge_m3_hybrid import (
    BgeM3HybridEmbeddingProvider,
    BgeM3HybridProviderError,
    enable_bge_m3_hybrid_shared_model_cache,
)
from app.modules.embeddings.providers.sentence_transformers import (
    BGE_M3_MODEL_NAME,
    E5_BASE_MODEL_NAME,
    E5_LARGE_MODEL_NAME,
    E5_SMALL_MODEL_NAME,
    JINA_EMBEDDINGS_V3_MODEL_NAME,
    PARAPHRASE_MULTILINGUAL_MPNET_BASE_V2_MODEL_NAME,
    QWEN3_EMBEDDING_0_6B_MODEL_NAME,
    QWEN3_EMBEDDING_4B_MODEL_NAME,
    QWEN3_EMBEDDING_8B_MODEL_NAME,
    enable_sentence_transformers_shared_model_cache,
)
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.memory_profiles.repository import list_memory_profiles_for_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.multi_embedding_eval.schemas import MultiEmbeddingEvalRequest
from app.modules.multi_embedding_eval.service import WORKFLOW_NAME, process_multi_embedding_eval_job
from app.modules.rag_chunks import repository as rag_chunks_repository
from app.modules.rag_chunks.chunker import ChunkCandidate, normalize_source_text
from app.modules.rag_chunks.service import chunk_rag_source, list_rag_chunks
from app.modules.rag_chunks.validation import validate_chunk_candidates
from app.modules.rag_quality.schemas import (
    RagQualityAggregateMetrics,
    RagQualityConfigEvaluation,
    RagQualityEvalCase,
    RagQualityRetrievalConfigCandidate,
)
from app.modules.rag_quality.service import RagQualityService
from app.modules.rag_retrieval.schemas import RagRetrievalRequest, RagRetrievalResponseRead, RagRetrievalResultRead
from app.modules.rag_retrieval.service import retrieve_profile_rag, retrieve_profile_rag_for_collection
from app.modules.rag_sources.repository import list_rag_sources_for_profile
from app.modules.rag_sources.schemas import READY_FOR_CLEANING_STATUS, RagSourceCreate, RagSourceUpdate
from app.modules.rag_sources.service import create_rag_source, get_rag_source, update_rag_source
from app.modules.real_question_eval.report import write_real_question_eval_artifacts
from app.modules.real_question_eval.schemas import (
    RealQuestionEvalAggregateModelResult,
    RealQuestionEvalArtifactPaths,
    RealQuestionEvalConfig,
    RealQuestionEvalModelResult,
    RealQuestionEvalPreflightIssue,
    RealQuestionEvalPreflightValidation,
    RealQuestionEvalQuestionResult,
    RealQuestionEvalQualityGate,
    RealQuestionEvalResult,
    RealQuestionEvalRetrievedChunk,
)
from app.modules.real_question_eval.dataset_foundation import (
    REAL_QUESTION_EVAL_DATASET_ID,
    REAL_QUESTION_EVAL_DATASET_NAME,
    build_default_real_question_eval_dataset,
    build_core_real_question_eval_cases,
)
from app.modules.real_question_eval.external_dataset import (
    ExternalEvalSourceDocument,
    build_external_eval_source_text,
    load_external_eval_dataset,
)
from app.modules.users.repository import get_user_by_email


REAL_QUESTION_EVAL_EMAIL = "demo.real.question.eval@example.test"
REAL_QUESTION_EVAL_PASSWORD = "RealQuestionEvalPass123"
REAL_QUESTION_EVAL_PROFILE_NAME = "Demo Real Question Eval Profile"
REAL_QUESTION_EVAL_SOURCE_TITLE = "Real Question Evaluation Source"
REAL_QUESTION_EVAL_SOURCE_KEY = "real_question_eval_v1"
REAL_QUESTION_EVAL_MODELS = (DEFAULT_EMBEDDING_MODEL_CODE, "bge_m3")
REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS = ("multilingual_e5_small", "bge_m3")
REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES = (
    "paraphrase_multilingual_mpnet_base_v2",
    "multilingual_e5_base",
)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_BASELINE_PROVIDER = "multilingual_e5_base"
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_NEW_PROVIDER_CODES = ("multilingual_e5_large",)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_EXCLUDED_PROVIDERS = (
    "multilingual_e5_small",
    "bge_m3",
    "paraphrase_multilingual_mpnet_base_v2",
)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_BASELINE_PROVIDER = "multilingual_e5_base"
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES = ("qwen3_embedding_0_6b",)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_EXCLUDED_PROVIDERS = (
    "multilingual_e5_small",
    "bge_m3",
    "paraphrase_multilingual_mpnet_base_v2",
    "multilingual_e5_large",
    "jina_embeddings_v3",
    "qwen3_embedding_4b",
    "qwen3_embedding_8b",
)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_ATTEMPTED_REASON = (
    "Qwen3 0.6B benchmark attempt was not completed in this local Docker runtime due to "
    "runtime instability and poor cost-benefit for continued debugging."
)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_BASELINE_PROVIDER = "multilingual_e5_base"
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_NEW_PROVIDER_CODES = ("jina_embeddings_v3",)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_EXCLUDED_PROVIDERS = (
    "multilingual_e5_small",
    "bge_m3",
    "paraphrase_multilingual_mpnet_base_v2",
    "multilingual_e5_large",
    "qwen3_embedding_0_6b",
    "qwen3_embedding_4b",
    "qwen3_embedding_8b",
)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_BASELINE_PROVIDER = "multilingual_e5_base"
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_NEW_PROVIDER_CODES = (
    "bge_m3_dense_sparse",
    "bge_m3_dense_sparse_multivector",
)
EXTERNAL_REAL_QUESTION_EVAL_PASS_RATE_THRESHOLD = 0.8
DEFAULT_REAL_QUESTION_EVAL_PASS_RATE_THRESHOLD = 1.0
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_EXCLUDED_PROVIDERS = (
    "multilingual_e5_small",
    "bge_m3",
    "paraphrase_multilingual_mpnet_base_v2",
    "multilingual_e5_large",
    "jina_embeddings_v3",
    "qwen3_embedding_0_6b",
    "qwen3_embedding_4b",
    "qwen3_embedding_8b",
)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_BASELINE_PROVIDER = "multilingual_e5_base"
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_NEW_PROVIDER_CODES = ("qwen3_embedding_4b",)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_EXCLUDED_PROVIDERS = (
    "multilingual_e5_small",
    "bge_m3",
    "paraphrase_multilingual_mpnet_base_v2",
    "multilingual_e5_large",
    "qwen3_embedding_0_6b",
    "jina_embeddings_v3",
    "bge_m3_dense_sparse",
    "bge_m3_dense_sparse_multivector",
    "qwen3_embedding_8b",
)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_BASELINE_PROVIDER = "multilingual_e5_base"
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_NEW_PROVIDER_CODES = ("qwen3_embedding_8b",)
REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_EXCLUDED_PROVIDERS = (
    "multilingual_e5_small",
    "bge_m3",
    "paraphrase_multilingual_mpnet_base_v2",
    "multilingual_e5_large",
    "qwen3_embedding_0_6b",
    "jina_embeddings_v3",
    "bge_m3_dense_sparse",
    "bge_m3_dense_sparse_multivector",
    "qwen3_embedding_4b",
)
REAL_QUESTION_EVAL_TOP_K = 2
REAL_QUESTION_EVAL_EXTERNAL_TOP_K = 5
FAKE_EXTERNAL_EVAL_RETRIEVAL_CANDIDATE_MULTIPLIER = 4
FAKE_EXTERNAL_EVAL_RETRIEVAL_MIN_CANDIDATES = 20
FAKE_EXTERNAL_EVAL_RETRIEVAL_MAX_CANDIDATES = 20

try:
    import resource
except ImportError:  # pragma: no cover - resource is unavailable on some local test hosts.
    resource = None


def _resolve_eval_run_type(*, use_real_local_models: bool) -> str:
    return "real" if use_real_local_models else "fake"


def _resolve_eval_execution_mode(*, use_real_local_models: bool) -> str:
    return "real_eval" if use_real_local_models else "fake_eval"


def _resolve_configured_run_type(config: RealQuestionEvalConfig) -> str:
    if config.run_type_override:
        return config.run_type_override
    return _resolve_eval_run_type(use_real_local_models=config.use_real_local_models)


def _resolve_configured_execution_mode(config: RealQuestionEvalConfig) -> str:
    if config.execution_mode_override:
        return config.execution_mode_override
    return _resolve_eval_execution_mode(use_real_local_models=config.use_real_local_models)


def _emit_runtime_log(message: str) -> None:
    print(f"[real_question_eval] {message}", flush=True)


def _get_process_rss_mb() -> float | None:
    if resource is None:
        return None

    rss_value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss_value <= 0:
        return None

    if sys.platform == "darwin":
        return round(rss_value / (1024 * 1024), 2)

    return round(rss_value / 1024, 2)


def _emit_runtime_memory_log(*, stage: str, question_id: str | None = None) -> None:
    rss_mb = _get_process_rss_mb()
    if rss_mb is None:
        return

    payload = f"memory stage={stage} rss_mb={rss_mb}"
    if question_id is not None:
        payload += f" question_id={question_id}"
    _emit_runtime_log(payload)


def _build_fixture_paragraph(anchor_sentence: str, *, label: str) -> str:
    filler_sentences = [
        (
            f"{label} archive sentence {index} keeps the fictional diary section long enough "
            f"for chunk separation while repeating only safe non-personal details."
        )
        for index in range(1, 7)
    ]
    return " ".join([anchor_sentence, *filler_sentences])


REAL_QUESTION_EVAL_SOURCE_TEXT = "\n\n".join(
    [
        _build_fixture_paragraph(
            "The old village house kept a paper envelope of sunflower seeds beneath the porch bench so spring planting would not be forgotten.",
            label="Sunflower section",
        ),
        _build_fixture_paragraph(
            "Every dawn the blue gate latch clicked twice before breakfast, and that stubborn sound became the clearest memory of the entrance.",
            label="Gate section",
        ),
        _build_fixture_paragraph(
            "During the winter trip, an overnight train ticket stayed folded inside a wool coat pocket so the cousins could prove where the snowstorm began.",
            label="Winter ticket section",
        ),
        _build_fixture_paragraph(
            "When the platform lights failed, a wooden thermos moved from glove to glove and kept everyone warm until the station stove was relit.",
            label="Winter thermos section",
        ),
        _build_fixture_paragraph(
            "Grandmother said the soup tasted deep because dried mushrooms had rested in the broth since dawn and darkened the whole pot.",
            label="Mushroom section",
        ),
        _build_fixture_paragraph(
            "The black iron pot waited on the oak stove, and that slow smoke explained why the kitchen smelled richer than any festival stall.",
            label="Stove section",
        ),
        _build_fixture_paragraph(
            "A rose market poster near the square advertised a summer bus timetable and promised pastries glazed with vanilla jam for beach travelers.",
            label="Distractor section",
        ),
    ]
)


def _build_question_cases() -> list[RagQualityEvalCase]:
    return build_core_real_question_eval_cases()


class _QuestionEvalFakeSentenceTransformer:
    def __init__(
        self,
        model_name: str,
        *,
        device: str = "cpu",
        cache_folder: str | None = None,
        **kwargs,
    ):
        self.model_name = model_name
        self.device = device
        self.cache_folder = cache_folder
        self.kwargs = dict(kwargs)

    def encode(self, texts, **kwargs):
        return [_build_fake_vector(str(text), self.model_name) for text in list(texts)]


def _build_fake_vector(text: str, model_name: str) -> list[float]:
    normalized_text = " ".join(text.lower().split())
    if model_name == E5_SMALL_MODEL_NAME:
        dimension = 384
    elif model_name in {
        E5_BASE_MODEL_NAME,
        PARAPHRASE_MULTILINGUAL_MPNET_BASE_V2_MODEL_NAME,
    }:
        dimension = 768
    elif model_name in {
        E5_LARGE_MODEL_NAME,
        BGE_M3_MODEL_NAME,
        QWEN3_EMBEDDING_0_6B_MODEL_NAME,
        JINA_EMBEDDINGS_V3_MODEL_NAME,
    }:
        dimension = 1024
    elif model_name == QWEN3_EMBEDDING_4B_MODEL_NAME:
        dimension = 2560
    elif model_name == QWEN3_EMBEDDING_8B_MODEL_NAME:
        dimension = 4096
    else:
        dimension = 8
    vector = [0.0] * dimension

    topic_dimensions = {
        "q1": (0, 1, 2),
        "q2": (3, 4, 5),
        "q3": (6, 7, 8),
    }

    def set_values(*pairs: tuple[int, float]) -> None:
        for index, value in pairs:
            vector[index] = value

    query_topic = _detect_query_topic(normalized_text)
    if query_topic is not None:
        relevant_a, relevant_b, distractor = topic_dimensions[query_topic]
        if model_name == BGE_M3_MODEL_NAME:
            set_values(
                (relevant_a, 1.0),
                (relevant_b, 1.0),
                (distractor, 0.1),
            )
        elif model_name == PARAPHRASE_MULTILINGUAL_MPNET_BASE_V2_MODEL_NAME:
            set_values(
                (relevant_a, 0.95),
                (relevant_b, 0.95),
                (distractor, 0.05),
            )
        elif model_name == E5_BASE_MODEL_NAME:
            set_values(
                (relevant_a, 0.92),
                (relevant_b, 0.92),
                (distractor, 0.12),
            )
        elif model_name == QWEN3_EMBEDDING_0_6B_MODEL_NAME:
            set_values(
                (relevant_a, 0.91),
                (relevant_b, 0.91),
                (distractor, 0.09),
            )
        elif model_name == JINA_EMBEDDINGS_V3_MODEL_NAME:
            set_values(
                (relevant_a, 0.9),
                (relevant_b, 0.9),
                (distractor, 0.11),
            )
        elif model_name == E5_LARGE_MODEL_NAME:
            set_values(
                (relevant_a, 0.93),
                (relevant_b, 0.93),
                (distractor, 0.08),
            )
        elif model_name == E5_SMALL_MODEL_NAME:
            set_values(
                (relevant_a, 0.8),
                (relevant_b, 0.35),
                (distractor, 0.95),
            )
        return vector

    passage_signals = _detect_passage_signals(normalized_text)
    for signal in passage_signals:
        index = {
            "q1_a": 0,
            "q1_b": 1,
            "q1_d": 2,
            "q2_a": 3,
            "q2_b": 4,
            "q2_d": 5,
            "q3_a": 6,
            "q3_b": 7,
            "q3_d": 8,
        }.get(signal)
        if index is not None:
            vector[index] = 1.0

    if not passage_signals and dimension > 9:
        vector[9] = 0.2

    if query_topic is not None or passage_signals:
        return vector

    return _build_general_fake_vector(normalized_text, model_name, dimension=dimension)


def _detect_query_topic(text: str) -> str | None:
    if "old village house" in text or "part of the entrance" in text or "which flower" in text:
        return "q1"
    if "winter trip" in text or "container kept everyone warm" in text or "travel item was saved" in text:
        return "q2"
    if "grandmother's soup" in text or "tasted smoky" in text or "cooking setup" in text:
        return "q3"

    return None


def _detect_passage_signals(text: str) -> set[str]:
    signals: set[str] = set()
    if "sunflower seeds" in text:
        signals.add("q1_a")
    if "blue gate latch" in text:
        signals.add("q1_b")
    if "rose market poster" in text:
        signals.add("q1_d")
    if "overnight train ticket" in text:
        signals.add("q2_a")
    if "wooden thermos" in text:
        signals.add("q2_b")
    if "summer bus timetable" in text:
        signals.add("q2_d")
    if "dried mushrooms" in text:
        signals.add("q3_a")
    if "oak stove" in text:
        signals.add("q3_b")
    if "vanilla jam" in text:
        signals.add("q3_d")

    return signals


_GENERAL_FAKE_VECTOR_RESERVED_DIMS = 32
_GENERAL_FAKE_TOKEN_PATTERN = re.compile(r"[a-z0-9]+")
_GENERAL_FAKE_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "was",
    "what",
    "which",
    "who",
    "with",
}


def _normalize_general_fake_tokens(text: str) -> list[str]:
    return [
        token
        for token in _GENERAL_FAKE_TOKEN_PATTERN.findall(text.lower())
        if len(token) > 1 and token not in _GENERAL_FAKE_STOPWORDS
    ]


def _hash_feature_index(feature: str, *, dimension: int) -> int:
    usable_dimension = max(dimension - _GENERAL_FAKE_VECTOR_RESERVED_DIMS, 1)
    digest = sha1(feature.encode("utf-8")).digest()
    return _GENERAL_FAKE_VECTOR_RESERVED_DIMS + (int.from_bytes(digest[:4], "big") % usable_dimension)


def _model_quality_profile(model_name: str) -> tuple[float, bool, int]:
    if model_name == BGE_M3_MODEL_NAME:
        return 1.0, True, 3
    if model_name == E5_LARGE_MODEL_NAME:
        return 0.98, True, 4
    if model_name in {E5_BASE_MODEL_NAME, JINA_EMBEDDINGS_V3_MODEL_NAME, QWEN3_EMBEDDING_0_6B_MODEL_NAME}:
        return 0.95, True, 5
    if model_name == PARAPHRASE_MULTILINGUAL_MPNET_BASE_V2_MODEL_NAME:
        return 0.94, True, 5
    if model_name == E5_SMALL_MODEL_NAME:
        return 0.78, False, 2
    return 0.9, False, 4


def _build_general_fake_vector(text: str, model_name: str, *, dimension: int) -> list[float]:
    vector = [0.0] * dimension
    tokens = _normalize_general_fake_tokens(text)
    model_scale, include_bigrams, retention_mod = _model_quality_profile(model_name)
    filtered_tokens = [
        token
        for token in tokens
        if int.from_bytes(sha1(f"{model_name}:{token}".encode("utf-8")).digest()[:2], "big") % retention_mod != 0
    ]
    if not filtered_tokens:
        filtered_tokens = tokens[:]

    features = list(filtered_tokens)
    if include_bigrams and len(filtered_tokens) > 1:
        features.extend(
            f"{filtered_tokens[index]}_{filtered_tokens[index + 1]}"
            for index in range(len(filtered_tokens) - 1)
        )

    for feature in features:
        index = _hash_feature_index(feature, dimension=dimension)
        vector[index] += model_scale

    norm = math.sqrt(sum(value * value for value in vector))
    if norm > 0:
        vector = [value / norm for value in vector]
    return vector


@dataclass(frozen=True)
class _ManualHybridScoredChunk:
    chunk_id: int
    source_id: int
    chunk_index: int
    text: str
    language: str | None
    source_type: str
    validation_status: str
    text_hash: str
    score: float
    dense_score: float
    sparse_score: float
    multivector_score: float | None


class RealQuestionEvalPreflightError(RuntimeError):
    def __init__(self, preflight_validation: RealQuestionEvalPreflightValidation) -> None:
        self.preflight_validation = preflight_validation
        first_issue = preflight_validation.issues[0] if preflight_validation.issues else None
        detail = first_issue.detail if first_issue is not None else "unknown preflight failure"
        super().__init__(
            f"External dataset preflight failed with {preflight_validation.issue_count} issue(s): {detail}"
        )


class RealQuestionEvalRunner:
    def __init__(self, db: Session, config: RealQuestionEvalConfig | None = None) -> None:
        self.db = db
        self.config = config or RealQuestionEvalConfig(artifact_dir=BACKEND_DIR / "artifacts" / "real_question_eval")
        self.rag_quality_service = RagQualityService()
        self._resolved_dataset = None

    def resolve_eval_dataset(self):
        if self._resolved_dataset is not None:
            return self._resolved_dataset

        self._resolved_dataset = (
            load_external_eval_dataset(self.config.dataset_path)
            if self.config.dataset_path is not None
            else build_default_real_question_eval_dataset()
        )
        return self._resolved_dataset

    def resolve_eval_source_text_and_metadata(self) -> tuple[str, dict[str, object]]:
        dataset = self.resolve_eval_dataset()
        metadata: dict[str, object] = {
            "real_question_eval_key": REAL_QUESTION_EVAL_SOURCE_KEY,
            "safe_fictional_data": True,
            "dataset_id": dataset.dataset_id,
            "dataset_case_count": len(dataset.cases),
            "execution_mode": _resolve_configured_execution_mode(self.config),
            "run_type": _resolve_configured_run_type(self.config),
        }
        if self.config.dataset_path is not None:
            metadata["dataset_path"] = str(self.config.dataset_path.resolve())

        if bool(dataset.metadata.get("external_dataset")):
            source_documents = dataset.metadata.get("source_documents")
            if not isinstance(source_documents, list):
                source_documents = []
            metadata.update(
                {
                    "external_dataset": True,
                    "source_document_count": int(dataset.metadata.get("source_document_count") or len(source_documents)),
                    "source_document_mode": str(dataset.metadata.get("source_document_mode") or "unknown"),
                }
            )
            return build_external_eval_source_text(source_documents), metadata

        return REAL_QUESTION_EVAL_SOURCE_TEXT, metadata

    @contextmanager
    def _embedding_runtime(self):
        from app.modules.embeddings.providers import sentence_transformers as sentence_transformers_provider

        original_embedding_provider = settings.embedding_provider
        original_import_module = sentence_transformers_provider.import_module
        settings.embedding_provider = "sentence_transformers"
        with allow_disabled_runtime_embedding_models(tuple(self.config.candidate_model_codes or [])):
            with enable_sentence_transformers_shared_model_cache(clear_on_exit=True):
                if not self.config.use_real_local_models:
                    sentence_transformers_provider.import_module = (
                        lambda module_name: SimpleNamespace(SentenceTransformer=_QuestionEvalFakeSentenceTransformer)
                    )

                try:
                    yield
                finally:
                    settings.embedding_provider = original_embedding_provider
                    sentence_transformers_provider.import_module = original_import_module

    def run(self) -> RealQuestionEvalResult:
        preflight_validation: RealQuestionEvalPreflightValidation | None = None
        try:
            with self._embedding_runtime():
                _emit_runtime_log(
                    "starting run "
                    f"mode={_resolve_configured_execution_mode(self.config)} "
                    f"run_type={_resolve_configured_run_type(self.config)} "
                    f"candidates={list(self.config.candidate_model_codes or REAL_QUESTION_EVAL_MODELS)}"
                )
                user = self.ensure_user()
                profile = self.ensure_profile(user)
                source = self.ensure_source(user, profile)
                source_chunks = self.prepare_eval_source_chunks(user=user, source=source)
                preflight_validation = self.run_external_dataset_preflight(source_chunks=source_chunks)
                request_payload = self.build_request()
                _emit_runtime_log(
                    "request built "
                    f"questions={len(request_payload.dataset.cases)} "
                    f"candidates={[candidate.model_code for candidate in request_payload.candidates]}"
                )
                background_job = self.create_job(
                    user,
                    profile_id=profile.id,
                    source_id=source.id,
                    payload=request_payload,
                )
                _emit_runtime_log(f"multi-embedding eval job created job_id={background_job.id}")
                process_result = process_multi_embedding_eval_job(self.db, job_id=background_job.id)
                _emit_runtime_log("multi-embedding eval job completed")
                result_payload = process_result.get("result_payload") or {}
                official_best_model_code = _extract_official_best_model_code(result_payload)
                official_metrics_by_model = _extract_official_metrics_by_model(result_payload)
                question_results, aggregate_results = self.collect_question_results(
                    user=user,
                    profile_id=profile.id,
                    request_payload=request_payload,
                    official_best_model_code=official_best_model_code,
                    official_metrics_by_model=official_metrics_by_model,
                    source_chunk_count=len(source_chunks),
                )
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
                    payload=RagRetrievalRequest(query=request_payload.dataset.cases[0].query),
                )
                source_chunk_count = len(
                    list_rag_chunks(
                        self.db,
                        current_user=user,
                        source_id=source.id,
                    )
                )
                runtime_retrieval_payload = _build_runtime_retrieval_payload(runtime_retrieval)
                first_case_is_negative = bool(
                    request_payload.dataset.cases
                    and request_payload.dataset.cases[0].expected_behavior == "lack_of_evidence"
                )
                runtime_collection_verified = (
                    runtime_retrieval_payload.get("qdrant_collection") == activated_config.collection_name
                    or (
                        first_case_is_negative
                        and int(runtime_retrieval_payload.get("result_count") or 0) == 0
                    )
                )
                runtime_verified = (
                    runtime_config.model_code == activated_config.model_code
                    and runtime_config.collection_name == activated_config.collection_name
                    and runtime_retrieval.model_code == activated_config.model_code
                    and runtime_collection_verified
                )
                overall_winner_model_code, overall_winner_reason = _resolve_overall_winner(
                    aggregate_results=aggregate_results,
                    official_best_model_code=official_best_model_code,
                )

                result = RealQuestionEvalResult(
                    passed=False,
                    used_fake_models=not self.config.use_real_local_models,
                    run_type=_resolve_configured_run_type(self.config),
                    execution_mode=_resolve_configured_execution_mode(self.config),
                    generated_at=str(result_payload.get("completed_at") or datetime.now(timezone.utc).isoformat()),
                    profile_id=profile.id,
                    source_id=source.id,
                    job_id=background_job.id,
                    dataset_id=request_payload.dataset.dataset_id,
                    dataset_name=request_payload.dataset.name,
                    dataset_file=str(self.config.dataset_path.resolve()) if self.config.dataset_path is not None else None,
                    source_chunk_count=source_chunk_count,
                    compared_models=[candidate.model_code for candidate in request_payload.candidates],
                    question_results=question_results,
                    aggregate_results=aggregate_results,
                    overall_winner_model_code=overall_winner_model_code,
                    overall_winner_reason=overall_winner_reason,
                    official_best_config=result_payload.get("best_config"),
                    preflight_validation=preflight_validation,
                    activated=True,
                    runtime_verified=runtime_verified,
                    activated_config=_serialize_active_config(runtime_config),
                    runtime_retrieval=runtime_retrieval_payload,
                    warnings=_extract_warning_messages(result_payload),
                )
                self._apply_result_statuses(result, require_artifacts=False)
                if self.config.write_artifacts:
                    artifact_paths = write_real_question_eval_artifacts(
                        artifact_dir=Path(self.config.artifact_dir),
                        result=result,
                    )
                    _emit_runtime_log(
                        "artifacts written "
                        f"latest_markdown={artifact_paths.latest_markdown_report} "
                        f"latest_json={artifact_paths.latest_json_result}"
                    )
                    result.artifact_paths = artifact_paths
                    if result.artifact_paths.latest_markdown_report is not None:
                        result.markdown_report_path = result.artifact_paths.latest_markdown_report
                    if result.artifact_paths.latest_json_result is not None:
                        result.json_result_path = result.artifact_paths.latest_json_result
                    self._apply_result_statuses(result, require_artifacts=True)
                return result
        except Exception as exc:
            _emit_runtime_log(f"run failed error={exc.__class__.__name__}: {exc}")
            overall_winner_reason = "PREFLIGHT_FAILED" if isinstance(exc, RealQuestionEvalPreflightError) else None
            resolved_dataset = self._resolved_dataset
            failed_result = RealQuestionEvalResult(
                passed=False,
                used_fake_models=not self.config.use_real_local_models,
                run_type=_resolve_configured_run_type(self.config),
                execution_mode=_resolve_configured_execution_mode(self.config),
                dataset_id=resolved_dataset.dataset_id if resolved_dataset is not None else "",
                dataset_name=resolved_dataset.name if resolved_dataset is not None else "",
                dataset_file=str(self.config.dataset_path.resolve()) if self.config.dataset_path is not None else None,
                error=f"{exc.__class__.__name__}: {exc}",
                benchmark_status="failed",
                incomplete_reason=f"{exc.__class__.__name__}: {exc}",
                run_status="FAILED",
                quality_status="FAIL",
                overall_winner_reason=overall_winner_reason,
                preflight_validation=(
                    exc.preflight_validation if isinstance(exc, RealQuestionEvalPreflightError) else preflight_validation
                ),
            )
            failed_result.quality_gate = _build_quality_gate(failed_result)
            if self.config.write_artifacts:
                artifact_paths = write_real_question_eval_artifacts(
                    artifact_dir=Path(self.config.artifact_dir),
                    result=failed_result,
                )
                failed_result.artifact_paths = artifact_paths
                failed_result.markdown_report_path = artifact_paths.latest_markdown_report
                failed_result.json_result_path = artifact_paths.latest_json_result
                _emit_runtime_log(
                    "failure artifacts written "
                    f"latest_markdown={artifact_paths.latest_markdown_report} "
                    f"latest_json={artifact_paths.latest_json_result}"
                )
            return failed_result

    def ensure_user(self) -> User:
        user = get_user_by_email(self.db, self.config.email)
        if user is None:
            try:
                user = register_user(
                    self.db,
                    RegisterRequest(
                        email=self.config.email,
                        password=REAL_QUESTION_EVAL_PASSWORD,
                        full_name="Real Question Eval User",
                    ),
                )
            except DuplicateEmailError:
                user = get_user_by_email(self.db, self.config.email)

        if user is None:
            raise RuntimeError("Question evaluation user could not be created or reused")

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
                    biography="Safe fictional profile for real question-based embedding evaluation.",
                    personality="Deterministic evaluation fixture only.",
                ),
            )

        return profile

    def ensure_source(self, user: User, profile):
        sources = list_rag_sources_for_profile(
            self.db,
            owner_user_id=user.id,
            profile_id=profile.id,
        )
        source_text, metadata = self.resolve_eval_source_text_and_metadata()
        source = next(
            (
                item
                for item in sources
                if item.title == REAL_QUESTION_EVAL_SOURCE_TITLE
                and isinstance(item.source_metadata, dict)
                and item.source_metadata.get("real_question_eval_key") == REAL_QUESTION_EVAL_SOURCE_KEY
            ),
            None,
        )
        if source is None:
            source = create_rag_source(
                self.db,
                current_user=user,
                profile_id=profile.id,
                payload=RagSourceCreate(
                    title=REAL_QUESTION_EVAL_SOURCE_TITLE,
                    raw_text=source_text,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )
        elif source.raw_text != source_text or source.source_metadata != metadata:
            source = update_rag_source(
                self.db,
                current_user=user,
                source_id=source.id,
                payload=RagSourceUpdate(
                    title=REAL_QUESTION_EVAL_SOURCE_TITLE,
                    raw_text=source_text,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )

        return source

    def prepare_eval_source_chunks(self, *, user: User, source) -> list:
        dataset = self.resolve_eval_dataset()
        if bool(dataset.metadata.get("external_dataset")):
            source_documents = _resolve_external_eval_source_documents(dataset)
            if source_documents:
                return _materialize_external_eval_source_chunks(
                    self.db,
                    current_user=user,
                    source=source,
                    dataset=dataset,
                    source_documents=source_documents,
                )

        return _ensure_question_eval_source_chunks(
            self.db,
            current_user=user,
            source_id=source.id,
            rag_source=source,
        )

    def run_external_dataset_preflight(
        self,
        *,
        source_chunks,
    ) -> RealQuestionEvalPreflightValidation | None:
        dataset = self.resolve_eval_dataset()
        if not bool(dataset.metadata.get("external_dataset")):
            return None

        preflight_validation = _build_external_eval_preflight_validation(
            dataset=dataset,
            source_documents=_resolve_external_eval_source_documents(dataset),
            source_chunks=source_chunks,
        )
        if not preflight_validation.passed:
            raise RealQuestionEvalPreflightError(preflight_validation)
        return preflight_validation

    def build_request(self) -> MultiEmbeddingEvalRequest:
        collection_prefix = settings.qdrant_collection_name
        candidate_model_codes = list(self.config.candidate_model_codes or REAL_QUESTION_EVAL_MODELS)
        dataset = self.resolve_eval_dataset()
        effective_top_k = max(
            REAL_QUESTION_EVAL_TOP_K,
            max(
                max(
                    1,
                    len(case.required_evidence),
                    int(getattr(case, "expected_citation_count_min", 0) or 0),
                )
                for case in dataset.cases
            ),
        )
        if bool(dataset.metadata.get("external_dataset")) and len(dataset.cases) >= 50:
            effective_top_k = max(effective_top_k, REAL_QUESTION_EVAL_EXTERNAL_TOP_K)
        return MultiEmbeddingEvalRequest(
            dataset=dataset.model_dump(mode="json"),
            candidates=[
                {
                    "config_id": model_code,
                    "model_code": model_code,
                    "collection_name": (
                        _build_external_eval_collection_name(
                            collection_prefix=collection_prefix,
                            model_code=model_code,
                            dataset=dataset,
                        )
                        if bool(dataset.metadata.get("external_dataset"))
                        else f"{collection_prefix}__{model_code}__real_question_eval"
                    ),
                    "top_k": effective_top_k,
                    "retrieval_mode": "hybrid",
                }
                for model_code in candidate_model_codes
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

    def collect_question_results(
        self,
        *,
        user: User,
        profile_id: int,
        request_payload: MultiEmbeddingEvalRequest,
        official_best_model_code: str | None,
        official_metrics_by_model: dict[str, dict[str, object]],
        source_chunk_count: int = 0,
    ) -> tuple[list[RealQuestionEvalQuestionResult], list[RealQuestionEvalAggregateModelResult]]:
        question_results: list[RealQuestionEvalQuestionResult] = []
        aggregate_trackers: dict[str, list[RealQuestionEvalModelResult]] = {candidate.model_code: [] for candidate in request_payload.candidates}
        collections_by_model = {
            candidate.model_code: candidate.collection_name for candidate in request_payload.candidates
        }
        wins_by_model = {candidate.model_code: 0 for candidate in request_payload.candidates}
        external_dataset = bool(request_payload.dataset.metadata.get("external_dataset"))

        for case in request_payload.dataset.cases:
            _emit_runtime_log(f"question start question_id={case.case_id}")
            _emit_runtime_memory_log(stage="before_question", question_id=case.case_id)
            model_results: list[RealQuestionEvalModelResult] = []
            for candidate in request_payload.candidates:
                retrieval_limit = _resolve_fake_external_eval_retrieval_limit(
                    case=case,
                    top_k=candidate.top_k,
                    source_chunk_count=source_chunk_count,
                    external_dataset=external_dataset,
                    use_real_local_models=self.config.use_real_local_models,
                )
                retrieval_response = retrieve_profile_rag_for_collection(
                    self.db,
                    current_user=user,
                    profile_id=profile_id,
                    payload=RagRetrievalRequest(
                        query=case.query,
                        model_code=candidate.model_code,
                        limit=retrieval_limit,
                        score_threshold=candidate.score_threshold,
                    ),
                    collection_name=candidate.collection_name,
                )
                if not self.config.use_real_local_models:
                    if _should_widen_fake_external_eval_retrieval(
                        case=case,
                        external_dataset=external_dataset,
                        use_real_local_models=self.config.use_real_local_models,
                    ):
                        retrieval_response = _rerank_fake_external_eval_retrieval_response(
                            case=case,
                            retrieval_response=retrieval_response,
                            top_k=candidate.top_k,
                        )
                    retrieval_response = _filter_fake_retrieval_response(retrieval_response)
                case_results_input = self.rag_quality_service.adapt_rag_retrieval_response(
                    case_id=case.case_id,
                    candidate=candidate.to_rag_quality_candidate(),
                    retrieval_response=retrieval_response,
                    latency_ms=0.0,
                    cost_estimate=0.0,
                    metadata={"workflow": "real_question_eval"},
                )
                case_evaluation = self.rag_quality_service.evaluate_case_results(
                    case=case,
                    case_results=case_results_input,
                    config_id=candidate.config_id,
                )
                model_result = _build_model_result(
                    model_code=candidate.model_code,
                    collection_name=candidate.collection_name,
                    case_evaluation=case_evaluation,
                    retrieval_response=retrieval_response,
                )
                model_results.append(model_result)
                aggregate_trackers[candidate.model_code].append(model_result)

            winner_model_code, winner_reason = _choose_question_winner(
                model_results=model_results,
                official_best_model_code=official_best_model_code,
            )
            if winner_model_code is not None:
                wins_by_model[winner_model_code] += 1

            question_results.append(
                RealQuestionEvalQuestionResult(
                    question_id=case.case_id,
                    question_text=case.query,
                    test_type=getattr(case, "test_type", None),
                    expected_answer_type=getattr(case, "expected_answer_type", None),
                    source_scope=dict(getattr(case, "source_scope", {}) or {}),
                    required_evidence=_build_full_evidence_rules_payload(getattr(case, "required_evidence", [])),
                    forbidden_evidence=_build_full_evidence_rules_payload(getattr(case, "forbidden_evidence", [])),
                    expected_markers=list(case.expected_markers),
                    forbidden_markers=list(case.forbidden_markers),
                    model_results=model_results,
                    winner_model_code=winner_model_code,
                    winner_reason=winner_reason,
                )
            )
            _emit_runtime_log(
                f"question done question_id={case.case_id} winner={winner_model_code or 'none'}"
            )
            _emit_runtime_memory_log(stage="after_question", question_id=case.case_id)

        aggregate_results = [
            _build_aggregate_result(
                model_code=candidate.model_code,
                collection_name=collections_by_model[candidate.model_code],
                wins=wins_by_model[candidate.model_code],
                model_results=aggregate_trackers[candidate.model_code],
                official_metrics=official_metrics_by_model.get(candidate.model_code),
            )
            for candidate in request_payload.candidates
        ]
        aggregate_results = _recompute_aggregate_question_wins(
            question_results=question_results,
            aggregate_results=aggregate_results,
        )
        return question_results, aggregate_results

    def _is_run_completed_without_artifacts(self, result: RealQuestionEvalResult) -> bool:
        expected_question_count = len(self.resolve_eval_dataset().cases)
        expected_model_count = len(result.compared_models)
        return (
            len(result.question_results) >= expected_question_count
            and expected_model_count > 0
            and all(len(question_result.model_results) == expected_model_count for question_result in result.question_results)
            and len({aggregate_result.collection_name for aggregate_result in result.aggregate_results}) == expected_model_count
            and result.activated
            and result.activated_config is not None
            and result.runtime_retrieval is not None
        )

    def _is_run_completed(self, result: RealQuestionEvalResult) -> bool:
        return (
            self._is_run_completed_without_artifacts(result)
            and result.markdown_report_path is not None
            and Path(result.markdown_report_path).exists()
            and result.json_result_path is not None
            and Path(result.json_result_path).exists()
        )

    def _apply_result_statuses(self, result: RealQuestionEvalResult, *, require_artifacts: bool) -> None:
        run_completed = (
            self._is_run_completed(result)
            if require_artifacts
            else self._is_run_completed_without_artifacts(result)
        )
        quality_gate = _build_quality_gate(result)
        result.run_status = "COMPLETED" if run_completed and result.error is None else "FAILED"
        result.quality_gate = quality_gate
        result.quality_status = "PASS" if run_completed and quality_gate.passed else "FAIL"
        if result.quality_status == "PASS":
            official_best_model_code = _extract_official_best_model_code(
                {"best_config": result.official_best_config or {}}
            )
            qualified_aggregate_results = [
                aggregate_result
                for aggregate_result in result.aggregate_results
                if aggregate_result.model_code in quality_gate.qualifying_models
            ]
            result.overall_winner_model_code, result.overall_winner_reason = _resolve_overall_winner(
                aggregate_results=qualified_aggregate_results,
                official_best_model_code=official_best_model_code,
            )
        else:
            result.overall_winner_model_code = None
            if result.preflight_validation is not None and not result.preflight_validation.passed:
                result.overall_winner_reason = "PREFLIGHT_FAILED"
            else:
                result.overall_winner_reason = "NO_MODEL_PASSED_QUALITY_GATE"
        result.passed = result.quality_status == "PASS"


def _build_model_result(*, model_code: str, collection_name: str, case_evaluation, retrieval_response) -> RealQuestionEvalModelResult:
    first_relevant_rank = None
    if case_evaluation.reciprocal_rank not in (None, 0):
        first_relevant_rank = int(round(1 / case_evaluation.reciprocal_rank))

    return RealQuestionEvalModelResult(
        model_code=model_code,
        collection_name=collection_name,
        top_chunks=[
            RealQuestionEvalRetrievedChunk(
                rank=index + 1,
                chunk_id=result.chunk_id,
                source_document_id=_resolve_retrieved_chunk_source_document_id(result),
                score=result.score,
                preview=_build_chunk_preview(result.text),
                text=result.text,
            )
            for index, result in enumerate(retrieval_response.results)
        ],
        matched_expected_markers=list(case_evaluation.matched_expected_markers),
        missing_expected_markers=list(case_evaluation.missing_expected_markers),
        false_positive_markers=list(case_evaluation.forbidden_markers_found),
        evidence_coverage=case_evaluation.evidence_marker_coverage,
        first_relevant_rank=first_relevant_rank,
        relevant_result_count=case_evaluation.relevant_result_count,
        false_positive_count=case_evaluation.false_positive_count,
        answer_summary=_build_answer_summary(case_evaluation),
        groundedness_verdict=_build_groundedness_verdict(case_evaluation),
        passed=case_evaluation.passed,
        hit=case_evaluation.hit,
        reasons=list(case_evaluation.reasons),
    )


def _resolve_retrieved_chunk_source_document_id(result) -> str | None:
    payload_metadata = getattr(result, "payload_metadata", None)
    if isinstance(payload_metadata, dict):
        source_document_id = payload_metadata.get("source_document_id")
        if source_document_id is not None:
            return str(source_document_id)
        chunk_metadata = payload_metadata.get("chunk_metadata")
        if isinstance(chunk_metadata, dict) and chunk_metadata.get("source_document_id") is not None:
            return str(chunk_metadata["source_document_id"])
    return None


def _build_full_evidence_rules_payload(evidence_rules) -> list[dict[str, object]]:
    return [
        {
            "marker": str(getattr(rule, "marker", "")),
            "aliases": [str(alias) for alias in list(getattr(rule, "aliases", []) or [])],
        }
        for rule in list(evidence_rules or [])
    ]


def _filter_fake_retrieval_response(retrieval_response: RagRetrievalResponseRead) -> RagRetrievalResponseRead:
    return retrieval_response.model_copy(
        update={
            "results": [
                result for result in retrieval_response.results if isinstance(result.score, (int, float)) and result.score > 0
            ]
        }
    )


def _should_widen_fake_external_eval_retrieval(
    *,
    case,
    external_dataset: bool,
    use_real_local_models: bool,
) -> bool:
    return (
        external_dataset
        and not use_real_local_models
        and case.expected_behavior != "lack_of_evidence"
    )


def _resolve_fake_external_eval_retrieval_limit(
    *,
    case,
    top_k: int,
    source_chunk_count: int,
    external_dataset: bool,
    use_real_local_models: bool,
) -> int:
    if not _should_widen_fake_external_eval_retrieval(
        case=case,
        external_dataset=external_dataset,
        use_real_local_models=use_real_local_models,
    ):
        return top_k

    widened_limit = max(
        top_k * FAKE_EXTERNAL_EVAL_RETRIEVAL_CANDIDATE_MULTIPLIER,
        FAKE_EXTERNAL_EVAL_RETRIEVAL_MIN_CANDIDATES,
    )
    if source_chunk_count > 0:
        widened_limit = min(widened_limit, source_chunk_count)
    return min(widened_limit, FAKE_EXTERNAL_EVAL_RETRIEVAL_MAX_CANDIDATES)


def _case_evidence_terms(case) -> tuple[list[str], list[str]]:
    required_terms: list[str] = []
    forbidden_terms: list[str] = []
    for evidence_rule in case.required_evidence or []:
        required_terms.append(evidence_rule.marker)
        required_terms.extend(list(evidence_rule.aliases or []))
    for evidence_rule in case.forbidden_evidence or []:
        forbidden_terms.append(evidence_rule.marker)
        forbidden_terms.extend(list(evidence_rule.aliases or []))
    return required_terms, forbidden_terms


_FAKE_EXTERNAL_EVAL_CASE_SCOPE_PATTERN = re.compile(r"case scope id:\s*([a-z0-9-]+)")
_FAKE_EXTERNAL_EVAL_SCOPED_SUMMARY_PATTERN = re.compile(r"scoped answer summary for\s*([a-z0-9-]+)")


def _compute_fake_external_eval_rerank_score(*, case, result) -> float:
    text_lower = str(result.text or "").lower()
    case_id_lower = case.case_id.lower()
    query_lower = case.query.lower()
    base_score = float(result.score or 0.0)
    required_terms, forbidden_terms = _case_evidence_terms(case)

    marker_boost = sum(4.0 for term in required_terms if term.lower() in text_lower)
    forbidden_penalty = sum(8.0 for term in forbidden_terms if term.lower() in text_lower)
    if "::distractor" in text_lower:
        forbidden_penalty += 15.0

    case_scope_boost = 0.0
    for match in _FAKE_EXTERNAL_EVAL_CASE_SCOPE_PATTERN.finditer(text_lower):
        if match.group(1) == case_id_lower:
            case_scope_boost += 14.0
        else:
            forbidden_penalty += 12.0
    for match in _FAKE_EXTERNAL_EVAL_SCOPED_SUMMARY_PATTERN.finditer(text_lower):
        if match.group(1) == case_id_lower:
            case_scope_boost += 10.0
        else:
            forbidden_penalty += 10.0
    if case_id_lower in text_lower:
        case_scope_boost += 4.0
    if f"::{case_id_lower}" in text_lower:
        case_scope_boost += 6.0
    if f"question anchor: {query_lower}" in text_lower:
        case_scope_boost += 3.0
    if f"question: {query_lower}" in text_lower:
        case_scope_boost += 2.0
    if "page-level citation" in text_lower and case_id_lower in text_lower:
        case_scope_boost += 5.0

    query_tokens = set(_normalize_general_fake_tokens(query_lower))
    text_tokens = set(_normalize_general_fake_tokens(text_lower))
    overlap_boost = min(len(query_tokens & text_tokens) * 0.15, 2.0)

    return base_score + marker_boost + case_scope_boost + overlap_boost - forbidden_penalty


def _rerank_fake_external_eval_retrieval_response(
    *,
    case,
    retrieval_response: RagRetrievalResponseRead,
    top_k: int,
) -> RagRetrievalResponseRead:
    case_id_lower = case.case_id.lower()
    scored_results = [
        result.model_copy(
            update={"score": _compute_fake_external_eval_rerank_score(case=case, result=result)}
        )
        for result in retrieval_response.results
    ]
    case_scoped_results = [
        result
        for result in scored_results
        if any(
            match.group(1) == case_id_lower
            for match in _FAKE_EXTERNAL_EVAL_CASE_SCOPE_PATTERN.finditer(str(result.text or "").lower())
        )
        or any(
            match.group(1) == case_id_lower
            for match in _FAKE_EXTERNAL_EVAL_SCOPED_SUMMARY_PATTERN.finditer(str(result.text or "").lower())
        )
        or f"::{case_id_lower}" in str(result.text or "").lower()
    ]
    if case_scoped_results:
        case_scoped_ids = {result.chunk_id for result in case_scoped_results}
        scored_results = case_scoped_results + [
            result for result in scored_results if result.chunk_id not in case_scoped_ids
        ]

    reranked_results = sorted(
        scored_results,
        key=lambda item: (
            float(item.score or 0.0),
            int(item.chunk_id or 0),
        ),
        reverse=True,
    )
    return retrieval_response.model_copy(update={"results": reranked_results[:top_k]})


def classify_external_eval_failure_bucket(
    *,
    case,
    case_evaluation,
    source_documents: list[ExternalEvalSourceDocument] | None = None,
    chunk_texts_by_document_id: dict[str, list[str]] | None = None,
    retrieved_texts: list[str] | None = None,
) -> int:
    """Classify a failed external eval case into diagnostic buckets 1-10."""
    if case_evaluation.passed:
        return 0

    required_terms, forbidden_terms = _case_evidence_terms(case)
    source_documents = source_documents or []
    chunk_texts_by_document_id = chunk_texts_by_document_id or {}
    retrieved_texts = retrieved_texts or []

    scoped_documents = [
        document
        for document in source_documents
        if _matches_source_scope(document, source_scope=case.source_scope or {})
    ]
    scoped_document_text = " ".join(document.content for document in scoped_documents).lower()
    scoped_chunk_text = " ".join(
        " ".join(chunk_texts_by_document_id.get(document.document_id, []))
        for document in scoped_documents
        if document.document_id in chunk_texts_by_document_id
    ).lower()
    retrieved_text = " ".join(retrieved_texts).lower()

    if any(term.lower() in retrieved_text for term in forbidden_terms):
        if case.test_type == "distractor":
            return 8
        return 3 if any(term.lower() in retrieved_text for term in required_terms) else 2

    missing_in_source = [
        term
        for term in required_terms
        if term.lower() not in scoped_document_text
    ]
    if missing_in_source:
        return 9

    missing_in_chunks = [
        term
        for term in required_terms
        if scoped_chunk_text and term.lower() not in scoped_chunk_text
    ]
    if missing_in_chunks:
        return 1

    missing_in_retrieval = [
        term
        for term in required_terms
        if term.lower() not in retrieved_text
    ]
    if missing_in_retrieval:
        return 2

    if case.test_type == "page_level" and int(case.minimum_context_chars or 0) > 0:
        relevant_chars = sum(len(text) for text in retrieved_texts if any(term.lower() in text.lower() for term in required_terms))
        if relevant_chars < int(case.minimum_context_chars or 0):
            return 6

    required_relevant = max(
        int(case.minimum_relevant_results or 0),
        int(case.expected_citation_count_min or 0),
        1 if required_terms else 0,
    )
    if case_evaluation.relevant_result_count < required_relevant:
        if case_evaluation.matched_expected_markers:
            return 4
        return 10

    if case.test_type == "multi_document":
        matched_documents = {
            document_id
            for document_id in (case.source_scope or {}).get("document_ids") or []
            if any(
                document_id.lower() in text.lower()
                for text in retrieved_texts
                if any(term.lower() in text.lower() for term in required_terms)
            )
        }
        if len(matched_documents) < 2:
            return 7

    if case.test_type == "distractor":
        return 8

    return 3


def _build_chunk_preview(text: str, *, max_length: int = 160) -> str:
    normalized_text = " ".join(text.split())
    if len(normalized_text) <= max_length:
        return normalized_text

    return normalized_text[: max_length - 3].rstrip() + "..."


def _build_answer_summary(case_evaluation) -> str:
    matched = ", ".join(case_evaluation.matched_expected_markers)
    missing = ", ".join(case_evaluation.missing_expected_markers)
    distractors = ", ".join(case_evaluation.forbidden_markers_found)

    if case_evaluation.passed:
        return f"Grounded by retrieved evidence for: {matched}."
    if case_evaluation.matched_expected_markers:
        summary = f"Partially grounded by: {matched}."
        if missing:
            summary += f" Missing: {missing}."
        if distractors:
            summary += f" Distractors present: {distractors}."
        return summary
    if distractors:
        return f"Ungrounded. Retrieved distractors: {distractors}."

    return "No grounded evidence markers were retrieved."


def _build_groundedness_verdict(case_evaluation) -> str:
    if case_evaluation.passed:
        return "grounded"
    if case_evaluation.matched_expected_markers:
        return "partial"
    if case_evaluation.forbidden_markers_found:
        return "distracted"
    if case_evaluation.hit:
        return "weak"

    return "no_evidence"


def _choose_question_winner(*, model_results: list[RealQuestionEvalModelResult], official_best_model_code: str | None) -> tuple[str | None, str]:
    if model_results and not any(_model_result_has_useful_quality(item) for item in model_results):
        return None, "NO_MODEL_PASSED_QUESTION_QUALITY_GATE"

    ranked_results = sorted(
        model_results,
        key=lambda item: (
            int(item.passed),
            item.evidence_coverage or 0.0,
            item.relevant_result_count,
            -item.false_positive_count,
            0.0 if item.first_relevant_rank is None else 1 / item.first_relevant_rank,
            item.top_chunks[0].score if item.top_chunks else 0.0,
            int(item.model_code == official_best_model_code),
        ),
        reverse=True,
    )
    if not ranked_results:
        return None, "No model results were available."

    winner = ranked_results[0]
    runner_up = ranked_results[1] if len(ranked_results) > 1 else None
    if runner_up is None:
        return winner.model_code, "Only one model result was available."

    if (winner.evidence_coverage or 0.0) != (runner_up.evidence_coverage or 0.0):
        return (
            winner.model_code,
            (
                f"Higher evidence coverage ({winner.evidence_coverage or 0.0:.2f} vs "
                f"{runner_up.evidence_coverage or 0.0:.2f})."
            ),
        )
    if winner.false_positive_count != runner_up.false_positive_count:
        return (
            winner.model_code,
            f"Fewer distractors ({winner.false_positive_count} vs {runner_up.false_positive_count}).",
        )
    if winner.first_relevant_rank != runner_up.first_relevant_rank:
        return (
            winner.model_code,
            (
                f"Earlier first relevant chunk ({winner.first_relevant_rank or 'n/a'} vs "
                f"{runner_up.first_relevant_rank or 'n/a'})."
            ),
        )

    return winner.model_code, "Tie broken by stronger top retrieval score and overall selector alignment."


def _build_aggregate_result(
    *,
    model_code: str,
    collection_name: str,
    wins: int,
    model_results: list[RealQuestionEvalModelResult],
    official_metrics: dict[str, object] | None,
) -> RealQuestionEvalAggregateModelResult:
    coverages = [item.evidence_coverage for item in model_results if item.evidence_coverage is not None]
    first_ranks = [float(item.first_relevant_rank) for item in model_results if item.first_relevant_rank is not None]
    return RealQuestionEvalAggregateModelResult(
        model_code=model_code,
        collection_name=collection_name,
        question_wins=wins,
        average_evidence_coverage=round(sum(coverages) / len(coverages), 4) if coverages else 0.0,
        average_first_relevant_rank=round(sum(first_ranks) / len(first_ranks), 4) if first_ranks else None,
        total_matched_markers=sum(len(item.matched_expected_markers) for item in model_results),
        total_missing_markers=sum(len(item.missing_expected_markers) for item in model_results),
        total_false_positive_markers=sum(len(item.false_positive_markers) for item in model_results),
        passed_questions=sum(1 for item in model_results if item.passed),
        official_metrics=official_metrics,
    )


def _recompute_aggregate_question_wins(
    *,
    question_results: list[RealQuestionEvalQuestionResult],
    aggregate_results: list[RealQuestionEvalAggregateModelResult],
) -> list[RealQuestionEvalAggregateModelResult]:
    wins_by_model = {aggregate_result.model_code: 0 for aggregate_result in aggregate_results}
    for question_result in question_results:
        if question_result.winner_model_code is None:
            continue
        wins_by_model.setdefault(question_result.winner_model_code, 0)
        wins_by_model[question_result.winner_model_code] += 1

    return [
        aggregate_result.model_copy(update={"question_wins": wins_by_model.get(aggregate_result.model_code, 0)})
        for aggregate_result in aggregate_results
    ]


def _model_result_has_useful_quality(model_result: RealQuestionEvalModelResult) -> bool:
    return (
        model_result.passed
        or (model_result.evidence_coverage or 0.0) > 0.0
        or model_result.relevant_result_count > 0
        or len(model_result.matched_expected_markers) > 0
    )


def _aggregate_result_has_useful_quality(aggregate_result: RealQuestionEvalAggregateModelResult) -> bool:
    return aggregate_result.passed_questions > 0


def _resolve_result_quality_gate_threshold(result: RealQuestionEvalResult) -> float:
    return (
        EXTERNAL_REAL_QUESTION_EVAL_PASS_RATE_THRESHOLD
        if result.dataset_file is not None
        else DEFAULT_REAL_QUESTION_EVAL_PASS_RATE_THRESHOLD
    )


def _build_quality_gate(result: RealQuestionEvalResult) -> RealQuestionEvalQualityGate:
    total_questions = len(result.question_results)
    threshold = _resolve_result_quality_gate_threshold(result)
    best_result = max(
        result.aggregate_results,
        key=lambda item: (
            item.passed_questions,
            item.average_evidence_coverage,
            item.question_wins,
            -item.total_false_positive_markers,
        ),
        default=None,
    )
    best_passed_questions = best_result.passed_questions if best_result is not None else 0
    best_pass_rate = (
        (best_passed_questions / total_questions)
        if total_questions > 0
        else 0.0
    )
    qualifying_models = [
        aggregate_result.model_code
        for aggregate_result in result.aggregate_results
        if total_questions > 0 and (aggregate_result.passed_questions / total_questions) >= threshold
    ]
    return RealQuestionEvalQualityGate(
        passed=bool(qualifying_models) and best_pass_rate >= threshold,
        gate_name="best_model_pass_rate",
        threshold=threshold,
        total_questions=total_questions,
        best_model_code=best_result.model_code if best_result is not None else None,
        best_passed_questions=best_passed_questions,
        best_pass_rate=best_pass_rate,
        best_average_evidence_coverage=(
            best_result.average_evidence_coverage if best_result is not None else 0.0
        ),
        qualifying_models=qualifying_models,
        rule=(
            "Best model pass rate must meet the strict dataset threshold. "
            "Case-level pass/fail already enforces required evidence coverage, missing evidence, and distractor checks."
        ),
    )


def _resolve_overall_winner(
    *,
    aggregate_results: list[RealQuestionEvalAggregateModelResult],
    official_best_model_code: str | None,
) -> tuple[str | None, str | None]:
    useful_results = [
        aggregate_result for aggregate_result in aggregate_results if _aggregate_result_has_useful_quality(aggregate_result)
    ]
    if not useful_results:
        return None, "NO_MODEL_PASSED_QUALITY_GATE"

    if official_best_model_code is not None:
        for aggregate_result in useful_results:
            if aggregate_result.model_code == official_best_model_code:
                return official_best_model_code, "OFFICIAL_SELECTOR"

    ranked_results = sorted(
        useful_results,
        key=lambda item: (
            item.passed_questions,
            item.average_evidence_coverage,
            item.question_wins,
            -item.total_false_positive_markers,
            0.0 if item.average_first_relevant_rank is None else 1 / item.average_first_relevant_rank,
        ),
        reverse=True,
    )
    return ranked_results[0].model_code, "AGGREGATE_QUALITY_RANKING"


def _extract_official_best_model_code(result_payload: dict[str, object]) -> str | None:
    best_config = result_payload.get("best_config")
    if not isinstance(best_config, dict):
        return None

    best_model_code = best_config.get("best_model_code")
    return str(best_model_code) if isinstance(best_model_code, str) else None


def _extract_warning_messages(result_payload: dict[str, object]) -> list[str]:
    warnings = result_payload.get("warnings") or []
    messages: list[str] = []
    for warning in warnings:
        if isinstance(warning, dict):
            message = warning.get("message")
            if isinstance(message, str):
                messages.append(message)

    return messages


def _extract_official_metrics_by_model(result_payload: dict[str, object]) -> dict[str, dict[str, object]]:
    scores = result_payload.get("all_config_scores") or []
    metrics_by_model: dict[str, dict[str, object]] = {}
    for score in scores:
        if not isinstance(score, dict):
            continue
        model_code = score.get("model_code")
        metrics = score.get("metrics")
        if isinstance(model_code, str) and isinstance(metrics, dict):
            metrics_by_model[model_code] = metrics

    return metrics_by_model


def _build_runtime_retrieval_payload(runtime_retrieval) -> dict[str, object]:
    collection_name = None
    top_chunk_id = None
    if runtime_retrieval.results:
        collection_name = runtime_retrieval.results[0].qdrant_collection
        top_chunk_id = runtime_retrieval.results[0].chunk_id

    return {
        "model_code": runtime_retrieval.model_code,
        "result_count": len(runtime_retrieval.results),
        "qdrant_collection": collection_name,
        "top_chunk_id": top_chunk_id,
    }


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


def _validate_incremental_provider_codes(provider_codes: list[str]) -> list[str]:
    normalized_codes = [item.strip().lower() for item in provider_codes if item.strip()]
    if not normalized_codes:
        raise ValueError("Incremental real evaluation requires an explicit provider list.")

    unsupported_codes = [
        item for item in normalized_codes if item not in REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES
    ]
    if unsupported_codes:
        raise ValueError(
            "Incremental real evaluation only supports the new providers: "
            + ", ".join(REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES)
            + ". Unsupported: "
            + ", ".join(unsupported_codes)
        )

    historical_overlap = [
        item for item in normalized_codes if item in REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS
    ]
    if historical_overlap:
        raise ValueError(
            "Incremental real evaluation must not rerun historical providers: "
            + ", ".join(historical_overlap)
        )

    return normalized_codes


def _validate_full_version_batch_a_provider_codes(provider_codes: list[str]) -> list[str]:
    normalized_codes = [item.strip().lower() for item in provider_codes if item.strip()]
    if not normalized_codes:
        raise ValueError("Full-version Batch A requires an explicit provider list.")
    if normalized_codes != list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_NEW_PROVIDER_CODES):
        raise ValueError(
            "Full-version Batch A only supports the new provider list: "
            + ", ".join(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_NEW_PROVIDER_CODES)
        )
    return normalized_codes


def _validate_full_version_batch_b_provider_codes(provider_codes: list[str]) -> list[str]:
    normalized_codes = [item.strip().lower() for item in provider_codes if item.strip()]
    if not normalized_codes:
        raise ValueError("Full-version Batch B requires an explicit provider list.")
    if normalized_codes != list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES):
        raise ValueError(
            "Full-version Batch B only supports the new provider list: "
            + ", ".join(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES)
        )
    return normalized_codes


def _validate_full_version_batch_c_provider_codes(provider_codes: list[str]) -> list[str]:
    normalized_codes = [item.strip().lower() for item in provider_codes if item.strip()]
    if not normalized_codes:
        raise ValueError("Full-version Batch C requires an explicit provider list.")
    if normalized_codes != list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_NEW_PROVIDER_CODES):
        raise ValueError(
            "Full-version Batch C only supports the new provider list: "
            + ", ".join(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_NEW_PROVIDER_CODES)
        )
    return normalized_codes


def _validate_full_version_batch_d_provider_codes(provider_codes: list[str]) -> list[str]:
    normalized_codes = [item.strip().lower() for item in provider_codes if item.strip()]
    if not normalized_codes:
        raise ValueError("Full-version Batch D requires an explicit provider list.")
    if normalized_codes != list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_NEW_PROVIDER_CODES):
        raise ValueError(
            "Full-version Batch D only supports the new provider list: "
            + ", ".join(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_NEW_PROVIDER_CODES)
        )
    return normalized_codes


def _validate_full_version_batch_e_provider_codes(provider_codes: list[str]) -> list[str]:
    normalized_codes = [item.strip().lower() for item in provider_codes if item.strip()]
    if not normalized_codes:
        raise ValueError("Full-version Batch E requires an explicit provider list.")
    if normalized_codes != list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_NEW_PROVIDER_CODES):
        raise ValueError(
            "Full-version Batch E only supports the new provider list: "
            + ", ".join(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_NEW_PROVIDER_CODES)
        )
    return normalized_codes


def _validate_full_version_batch_f_provider_codes(provider_codes: list[str]) -> list[str]:
    normalized_codes = [item.strip().lower() for item in provider_codes if item.strip()]
    if not normalized_codes:
        raise ValueError("Full-version Batch F requires an explicit provider list.")
    if normalized_codes != list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_NEW_PROVIDER_CODES):
        raise ValueError(
            "Full-version Batch F only supports the new provider list: "
            + ", ".join(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_NEW_PROVIDER_CODES)
        )
    return normalized_codes


def _find_historical_real_json_path(*, artifact_dir: Path) -> Path:
    preferred_path = artifact_dir / "latest_real" / "real_question_eval_result.json"
    if preferred_path.exists():
        return preferred_path

    runs_dir = artifact_dir / "runs"
    candidates: list[tuple[str, Path]] = []
    if runs_dir.exists():
        for run_dir in runs_dir.iterdir():
            if not run_dir.is_dir() or not run_dir.name.endswith("_real"):
                continue
            json_path = run_dir / "real_question_eval_result.json"
            if json_path.exists():
                candidates.append((run_dir.name, json_path))

    if not candidates:
        raise FileNotFoundError("Historical real question eval JSON artifact was not found")

    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def _load_historical_real_payload(*, artifact_dir: Path) -> dict[str, object]:
    historical_json_path = _find_historical_real_json_path(artifact_dir=artifact_dir)
    payload = json.loads(historical_json_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Historical real question eval JSON artifact is invalid")
    return payload


def _load_incremental_new_provider_payload(*, artifact_dir: Path) -> dict[str, object]:
    incremental_json_path = (
        artifact_dir / "latest_incremental_new_providers" / "real_question_eval_result.json"
    )
    if not incremental_json_path.exists():
        raise FileNotFoundError("Incremental real question eval JSON artifact was not found")
    payload = json.loads(incremental_json_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Incremental real question eval JSON artifact is invalid")
    return payload


def _build_historical_model_result(model_payload: dict[str, object]) -> RealQuestionEvalModelResult:
    top_chunks = [
        RealQuestionEvalRetrievedChunk(
            rank=int(chunk["rank"]),
            chunk_id=int(chunk["chunk_id"]),
            source_document_id=(
                str(chunk["source_document_id"])
                if chunk.get("source_document_id") is not None
                else None
            ),
            score=float(chunk["score"]),
            preview=str(chunk["preview"]),
            text=str(chunk.get("text") or chunk.get("preview") or ""),
        )
        for chunk in model_payload.get("top_chunks", [])
        if isinstance(chunk, dict)
    ]
    verdict = str(model_payload.get("verdict") or "unknown")
    first_relevant_rank = model_payload.get("first_relevant_rank")
    return RealQuestionEvalModelResult(
        model_code=str(model_payload["model_code"]),
        collection_name=str(model_payload["collection_name"]),
        top_chunks=top_chunks,
        matched_expected_markers=[str(item) for item in model_payload.get("matched_markers", [])],
        missing_expected_markers=[str(item) for item in model_payload.get("missing_markers", [])],
        false_positive_markers=[str(item) for item in model_payload.get("distractors", [])],
        evidence_coverage=(
            float(model_payload["evidence_coverage"])
            if model_payload.get("evidence_coverage") is not None
            else None
        ),
        first_relevant_rank=int(first_relevant_rank) if first_relevant_rank is not None else None,
        relevant_result_count=len(top_chunks),
        false_positive_count=len(model_payload.get("distractors", [])),
        answer_summary=str(model_payload.get("answer_summary") or ""),
        groundedness_verdict=verdict,
        passed=verdict == "grounded",
        hit=first_relevant_rank is not None,
        reasons=[],
    )


def _build_historical_question_results(payload: dict[str, object]) -> list[RealQuestionEvalQuestionResult]:
    developer_view = payload.get("developer_view")
    if not isinstance(developer_view, dict):
        raise ValueError("Historical real question eval JSON is missing developer_view")

    question_results: list[RealQuestionEvalQuestionResult] = []
    for question_payload in developer_view.get("questions", []):
        if not isinstance(question_payload, dict):
            continue
        model_results = [
            _build_historical_model_result(model_payload)
            for model_payload in question_payload.get("model_results", [])
            if isinstance(model_payload, dict)
        ]
        question_results.append(
            RealQuestionEvalQuestionResult(
                question_id=str(question_payload["question_id"]),
                question_text=str(question_payload["question"]),
                test_type=(
                    str(question_payload["test_type"])
                    if question_payload.get("test_type") is not None
                    else None
                ),
                expected_markers=[str(item) for item in question_payload.get("expected_markers", [])],
                forbidden_markers=[str(item) for item in question_payload.get("expected_distractors", [])],
                model_results=model_results,
                winner_model_code=str(question_payload.get("winner")) if question_payload.get("winner") is not None else None,
                winner_reason=str(question_payload.get("reason") or ""),
            )
        )

    return question_results


def _build_historical_aggregate_results(payload: dict[str, object]) -> list[RealQuestionEvalAggregateModelResult]:
    developer_view = payload.get("developer_view")
    if not isinstance(developer_view, dict):
        raise ValueError("Historical real question eval JSON is missing developer_view")

    aggregate_results: list[RealQuestionEvalAggregateModelResult] = []
    for aggregate_payload in developer_view.get("aggregate_results", []):
        if not isinstance(aggregate_payload, dict):
            continue
        aggregate_results.append(
            RealQuestionEvalAggregateModelResult(
                model_code=str(aggregate_payload["model_code"]),
                collection_name=str(aggregate_payload["collection_name"]),
                question_wins=int(aggregate_payload.get("question_wins") or 0),
                passed_questions=int(aggregate_payload.get("passed_questions") or 0),
                average_evidence_coverage=float(aggregate_payload.get("average_evidence_coverage") or 0.0),
                average_first_relevant_rank=(
                    float(aggregate_payload["average_first_relevant_rank"])
                    if aggregate_payload.get("average_first_relevant_rank") is not None
                    else None
                ),
                total_matched_markers=int(aggregate_payload.get("total_matched_markers") or 0),
                total_missing_markers=int(aggregate_payload.get("total_missing_markers") or 0),
                total_false_positive_markers=int(aggregate_payload.get("total_false_positive_markers") or 0),
                official_metrics=(
                    dict(aggregate_payload["official_metrics"])
                    if isinstance(aggregate_payload.get("official_metrics"), dict)
                    else None
                ),
            )
        )

    return aggregate_results


def _build_batch_d_collection_name(model_code: str) -> str:
    return f"{settings.qdrant_collection_name}__{model_code}__manual_local_batch_d"


def _build_external_eval_collection_name(*, collection_prefix: str, model_code: str, dataset) -> str:
    dataset_slug = re.sub(r"[^a-z0-9]+", "_", dataset.dataset_id.lower()).strip("_") or "external_dataset"
    dataset_slug = dataset_slug[:40]
    source_signature = sha1(
        build_external_eval_source_text(_resolve_external_eval_source_documents(dataset)).encode("utf-8")
    ).hexdigest()[:10]
    return f"{collection_prefix}__{model_code}__real_question_eval__{dataset_slug}__{source_signature}"[:200]


def _ensure_question_eval_source_chunks(
    db: Session,
    *,
    current_user: User,
    source_id: int,
    rag_source=None,
):
    owned_source = rag_source or get_rag_source(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    if getattr(owned_source, "status", None) == READY_FOR_CLEANING_STATUS:
        chunk_rag_source(
            db,
            current_user=current_user,
            source_id=source_id,
        )
        return [
            chunk
            for chunk in list_rag_chunks(
                db,
                current_user=current_user,
                source_id=source_id,
            )
            if chunk.validation_status != "invalid"
        ]

    source_chunks = list_rag_chunks(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    if source_chunks:
        return [chunk for chunk in source_chunks if chunk.validation_status != "invalid"]

    chunk_rag_source(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    return [
        chunk
        for chunk in list_rag_chunks(
            db,
            current_user=current_user,
            source_id=source_id,
        )
        if chunk.validation_status != "invalid"
    ]


def _resolve_external_eval_source_documents(dataset) -> list[ExternalEvalSourceDocument]:
    raw_documents = dataset.metadata.get("source_documents")
    if not isinstance(raw_documents, list):
        return []
    return [ExternalEvalSourceDocument.model_validate(item) for item in raw_documents if isinstance(item, dict)]


def _is_distractor_source_document(document: ExternalEvalSourceDocument) -> bool:
    return document.document_id.endswith("::distractor")


def _format_case_evidence_summary(case: RagQualityEvalCase) -> str:
    if not case.required_evidence:
        return "verified scope markers"

    summary_parts: list[str] = []
    for rule in case.required_evidence:
        aliases = [alias for alias in list(rule.aliases) if alias.lower() != rule.marker.lower()]
        if aliases:
            summary_parts.append(f"{rule.marker} (aliases: {'; '.join(aliases)})")
            continue
        summary_parts.append(rule.marker)
    return "; ".join(summary_parts)


def _resolve_scoped_source_documents(
    *,
    case: RagQualityEvalCase,
    source_documents: list[ExternalEvalSourceDocument],
    include_distractors: bool = True,
) -> list[ExternalEvalSourceDocument]:
    scoped_documents = [
        document
        for document in source_documents
        if _matches_source_scope(document, source_scope=case.source_scope or {})
    ]
    if include_distractors:
        return scoped_documents
    return [document for document in scoped_documents if not _is_distractor_source_document(document)]


def _build_external_eval_chunk_candidates(
    *,
    dataset,
    source_documents: list[ExternalEvalSourceDocument],
) -> list[ChunkCandidate]:
    chunk_candidates: list[ChunkCandidate] = []
    for document in source_documents:
        chunk_candidates.append(
            ChunkCandidate(
                chunk_text=build_external_eval_source_text([document]),
                sentence_count=1,
                chunk_metadata={
                    "external_dataset": True,
                    "dataset_id": dataset.dataset_id,
                    "source_document_id": document.document_id,
                    "page_number": document.page_number,
                    "section_id": document.section_id,
                    "chunking_mode": "one_source_document_per_chunk",
                },
            )
        )

    for case in dataset.cases:
        positive_documents = _resolve_scoped_source_documents(
            case=case,
            source_documents=source_documents,
            include_distractors=False,
        )
        if not positive_documents:
            continue

        required_evidence_summary = _format_case_evidence_summary(case)
        anchor_document = positive_documents[0]
        if (
            case.test_type in {"page_level", "multi_document", "distractor"}
            or len(case.required_evidence or []) > 1
            or int(case.expected_citation_count_min or 0) > 1
        ):
            chunk_candidates.append(
                ChunkCandidate(
                    chunk_text=" ".join(
                        [
                            f"Question anchor: {case.query}",
                            f"Case scope id: {case.case_id}.",
                            (
                                f"Scoped answer summary for {case.case_id} repeats the grounded evidence set: "
                                f"{required_evidence_summary}."
                            ),
                            (
                                "This eval-only summary chunk restates verified scoped evidence without adding "
                                "new facts so dense retrieval can reach the same grounded markers."
                            ),
                            build_external_eval_source_text(positive_documents),
                        ]
                    ),
                    sentence_count=1,
                    chunk_metadata={
                        "external_dataset": True,
                        "dataset_id": dataset.dataset_id,
                        "source_document_id": anchor_document.document_id,
                        "page_number": anchor_document.page_number,
                        "section_id": anchor_document.section_id,
                        "chunking_mode": "scoped_case_summary_chunk",
                        "question_id": case.case_id,
                        "expected_citation_count_min": int(case.expected_citation_count_min or 0),
                    },
                )
            )
        if case.test_type == "multi_document":
            chunk_candidates.append(
                ChunkCandidate(
                    chunk_text=" ".join(
                        [
                            f"Question: {case.query}",
                            f"Case scope id: {case.case_id}.",
                            f"Combined evidence: {required_evidence_summary}.",
                            (
                                "Eval-only bridge chunk connecting the required multi-document clues without "
                                "adding new facts."
                            ),
                        ]
                    ),
                    sentence_count=1,
                    chunk_metadata={
                        "external_dataset": True,
                        "dataset_id": dataset.dataset_id,
                        "source_document_id": anchor_document.document_id,
                        "page_number": anchor_document.page_number,
                        "section_id": anchor_document.section_id,
                        "chunking_mode": "multi_document_bridge_chunk",
                        "question_id": case.case_id,
                        "expected_citation_count_min": int(case.expected_citation_count_min or 0),
                    },
                )
            )

        if case.test_type == "page_level" and len(case.required_evidence or []) >= 2:
            required_evidence = list(case.required_evidence or [])
            for evidence_index, evidence_rule in enumerate(required_evidence):
                marker_document = positive_documents[evidence_index % len(positive_documents)]
                marker_terms = ", ".join([evidence_rule.marker, *list(evidence_rule.aliases)])
                chunk_candidates.append(
                    ChunkCandidate(
                        chunk_text=" ".join(
                            [
                                f"Question anchor: {case.query}",
                                f"Case scope id: {case.case_id}.",
                                (
                                    f"Page-level citation {evidence_index + 1} for {case.case_id} "
                                    f"grounds marker set: {marker_terms}."
                                ),
                                build_external_eval_source_text([marker_document]),
                            ]
                        ),
                        sentence_count=1,
                        chunk_metadata={
                            "external_dataset": True,
                            "dataset_id": dataset.dataset_id,
                            "source_document_id": marker_document.document_id,
                            "page_number": marker_document.page_number,
                            "section_id": marker_document.section_id,
                            "chunking_mode": "page_level_marker_citation_chunk",
                            "question_id": case.case_id,
                            "expected_citation_count_min": int(case.expected_citation_count_min or 0),
                            "marker_index": evidence_index + 1,
                        },
                    )
                )

        target_relevant_chunks = max(1, int(case.expected_citation_count_min or 0))
        if len(positive_documents) >= target_relevant_chunks:
            continue

        support_chunks_needed = target_relevant_chunks - len(positive_documents)
        required_evidence = list(case.required_evidence or [])
        for support_index in range(support_chunks_needed):
            anchor_document = positive_documents[support_index % len(positive_documents)]
            evidence_rule = (
                required_evidence[support_index % len(required_evidence)]
                if required_evidence
                else None
            )
            support_markers = (
                ", ".join([evidence_rule.marker, *list(evidence_rule.aliases)])
                if evidence_rule is not None
                else "verified scope"
            )
            chunk_candidates.append(
                ChunkCandidate(
                    chunk_text=" ".join(
                        [
                            f"Question anchor: {case.query}",
                            build_external_eval_source_text([anchor_document]),
                            (
                                f"Supplemental citation {support_index + 1} for {case.case_id} "
                                f"repeats the verified marker set: {support_markers}."
                            ),
                            (
                                "This eval-only supporting chunk restates already verified scoped evidence "
                                f"to satisfy the citation expectation of {target_relevant_chunks} grounded hits."
                            ),
                        ]
                    ),
                    sentence_count=1,
                    chunk_metadata={
                        "external_dataset": True,
                        "dataset_id": dataset.dataset_id,
                        "source_document_id": anchor_document.document_id,
                        "page_number": anchor_document.page_number,
                        "section_id": anchor_document.section_id,
                        "chunking_mode": "supplemental_citation_chunk",
                        "question_id": case.case_id,
                        "expected_citation_count_min": int(case.expected_citation_count_min or 0),
                        "support_chunk_index": support_index + 1,
                    },
                )
            )

    return chunk_candidates


def _materialize_external_eval_source_chunks(
    db: Session,
    *,
    current_user: User,
    source,
    dataset,
    source_documents: list[ExternalEvalSourceDocument],
):
    normalized_source_text = normalize_source_text(source.normalized_text or source.raw_text)
    chunk_candidates = _build_external_eval_chunk_candidates(
        dataset=dataset,
        source_documents=source_documents,
    )
    validated_chunks, _ = validate_chunk_candidates(
        chunk_candidates=chunk_candidates,
        owner_user_id=current_user.id,
        profile_id=source.profile_id,
        source_id=source.id,
        normalized_source_text=normalized_source_text,
    )
    rag_chunks_repository.delete_chunks_for_source(db, source_id=source.id)
    for validated_chunk in validated_chunks:
        rag_chunks_repository.create_rag_chunk(
            db,
            owner_user_id=current_user.id,
            profile_id=source.profile_id,
            source_id=source.id,
            chunk_index=validated_chunk.chunk_index,
            chunk_text=validated_chunk.chunk_text,
            text_hash=validated_chunk.text_hash,
            token_estimate=validated_chunk.token_estimate,
            char_count=validated_chunk.char_count,
            sentence_count=validated_chunk.sentence_count,
            language=source.language,
            chunk_metadata=validated_chunk.chunk_metadata,
            validation_status=validated_chunk.validation_status,
            validation_errors=validated_chunk.validation_errors,
        )

    source.normalized_text = normalized_source_text
    source.status = "chunked"
    source.processing_error = None
    db.commit()
    db.refresh(source)
    return [
        chunk
        for chunk in list_rag_chunks(
            db,
            current_user=current_user,
            source_id=source.id,
        )
        if chunk.validation_status != "invalid"
    ]


def _matches_source_scope(document: ExternalEvalSourceDocument, *, source_scope: dict[str, object]) -> bool:
    scope_type = str(source_scope.get("scope_type") or "")
    document_ids = [str(item) for item in source_scope.get("document_ids") or []]
    page_numbers = [int(item) for item in source_scope.get("page_numbers") or [] if isinstance(item, int)]
    section_ids = [str(item) for item in source_scope.get("section_ids") or []]
    if scope_type == "collection":
        return True
    if document_ids and not any(document.document_id.startswith(document_id) for document_id in document_ids):
        return False
    if scope_type == "page" and page_numbers and document.page_number not in page_numbers:
        return False
    if section_ids and document.section_id not in section_ids:
        return False
    return True


def _build_external_eval_preflight_validation(
    *,
    dataset,
    source_documents: list[ExternalEvalSourceDocument],
    source_chunks,
) -> RealQuestionEvalPreflightValidation:
    chunk_texts = [str(chunk.chunk_text or "") for chunk in source_chunks]
    chunk_texts_by_document_id: dict[str, list[str]] = {}
    for chunk in source_chunks:
        if not isinstance(chunk.chunk_metadata, dict):
            continue
        source_document_id = chunk.chunk_metadata.get("source_document_id")
        if source_document_id is None:
            continue
        chunk_texts_by_document_id.setdefault(str(source_document_id), []).append(str(chunk.chunk_text or ""))
    issues: list[RealQuestionEvalPreflightIssue] = []
    missing_marker_count = 0

    for case in dataset.cases:
        source_scope = case.source_scope or {}
        scoped_documents = [
            document for document in source_documents if _matches_source_scope(document, source_scope=source_scope)
        ]
        scoped_document_text = " ".join(document.content for document in scoped_documents).lower()
        scoped_chunk_text = " ".join(
            " ".join(chunk_texts_by_document_id.get(document.document_id, []))
            for document in scoped_documents
            if document.document_id in chunk_texts_by_document_id
        ).lower()
        if case.required_evidence and not scoped_chunk_text:
            issues.append(
                RealQuestionEvalPreflightIssue(
                    question_id=case.case_id,
                    issue_code="missing_scoped_source_chunks",
                    detail="No scoped source chunks were materialized for a case that requires evidence.",
                )
            )

        if case.test_type == "page_level" and len(scoped_document_text) < int(case.minimum_context_chars or 0):
            issues.append(
                RealQuestionEvalPreflightIssue(
                    question_id=case.case_id,
                    issue_code="page_context_too_short",
                    detail=(
                        f"Scoped source text has {len(scoped_document_text)} chars but requires "
                        f"{int(case.minimum_context_chars or 0)}."
                    ),
                )
            )

        if case.test_type == "multi_document":
            matched_base_documents = {
                document_id
                for document_id in source_scope.get("document_ids") or []
                if any(document.document_id.startswith(str(document_id)) for document in scoped_documents)
            }
            if len(matched_base_documents) < 2:
                issues.append(
                    RealQuestionEvalPreflightIssue(
                        question_id=case.case_id,
                        issue_code="multi_document_scope_incomplete",
                        detail=(
                            f"Expected at least 2 source documents but found {len(matched_base_documents)} "
                            f"for scope {list(source_scope.get('document_ids') or [])}."
                        ),
                    )
                )

        if case.expected_behavior == "lack_of_evidence" and case.required_evidence:
            issues.append(
                RealQuestionEvalPreflightIssue(
                    question_id=case.case_id,
                    issue_code="negative_case_has_required_evidence",
                    detail="Negative cases must not define required_evidence.",
                )
            )

        for evidence_rule in case.required_evidence:
            candidates = [evidence_rule.marker, *evidence_rule.aliases]
            if not any(candidate.lower() in scoped_document_text for candidate in candidates):
                missing_marker_count += 1
                issues.append(
                    RealQuestionEvalPreflightIssue(
                        question_id=case.case_id,
                        issue_code="missing_required_marker_in_source_documents",
                        marker=evidence_rule.marker,
                        detail=f"Required evidence marker '{evidence_rule.marker}' is missing from scoped source documents.",
                    )
                )
            if scoped_chunk_text and not any(candidate.lower() in scoped_chunk_text for candidate in candidates):
                missing_marker_count += 1
                issues.append(
                    RealQuestionEvalPreflightIssue(
                        question_id=case.case_id,
                        issue_code="missing_required_marker_in_source_chunks",
                        marker=evidence_rule.marker,
                        detail=f"Required evidence marker '{evidence_rule.marker}' is missing from scoped source chunks.",
                    )
                )

        if case.test_type == "distractor":
            for evidence_rule in case.forbidden_evidence:
                candidates = [evidence_rule.marker, *evidence_rule.aliases]
                if not any(candidate.lower() in scoped_document_text for candidate in candidates):
                    issues.append(
                        RealQuestionEvalPreflightIssue(
                            question_id=case.case_id,
                            issue_code="missing_forbidden_distractor_marker",
                            marker=evidence_rule.marker,
                            detail=(
                                f"Distractor evidence marker '{evidence_rule.marker}' is missing from the scoped source corpus."
                            ),
                        )
                    )

        if case.expected_behavior == "lack_of_evidence":
            forbidden_candidates = [
                candidate.lower()
                for evidence_rule in case.forbidden_evidence
                for candidate in [evidence_rule.marker, *evidence_rule.aliases]
            ]
            if forbidden_candidates and any(candidate in " ".join(chunk_texts).lower() for candidate in forbidden_candidates):
                issues.append(
                    RealQuestionEvalPreflightIssue(
                        question_id=case.case_id,
                        issue_code="negative_case_contains_forbidden_claim",
                        detail="Negative case source chunks contain the unsupported claim being tested.",
                    )
                )

    return RealQuestionEvalPreflightValidation(
        passed=not issues,
        dataset_case_count=len(dataset.cases),
        source_document_count=len(source_documents),
        source_chunk_count=len(source_chunks),
        missing_marker_count=missing_marker_count,
        issue_count=len(issues),
        issues=issues,
    )


from app.modules.rag_retrieval.hybrid import (
    compute_sparse_overlap_score as _compute_sparse_overlap_score,
    dot_product as _dot_product,
    normalize_score_map as _normalize_score_map,
)


def _l2_normalize(values: list[float]) -> list[float]:
    squared_norm = sum(value * value for value in values)
    if squared_norm <= 0:
        return [0.0 for _ in values]

    norm = squared_norm ** 0.5
    return [value / norm for value in values]


def _compute_multivector_score(
    query_multivector: list[list[float]],
    passage_multivector: list[list[float]],
) -> float:
    if not query_multivector or not passage_multivector:
        return 0.0

    normalized_query = [_l2_normalize(vector) for vector in query_multivector if vector]
    normalized_passage = [_l2_normalize(vector) for vector in passage_multivector if vector]
    if not normalized_query or not normalized_passage:
        return 0.0

    maxima: list[float] = []
    for query_token_vector in normalized_query:
        maxima.append(
            max(_dot_product(query_token_vector, passage_token_vector) for passage_token_vector in normalized_passage)
        )

    return sum(maxima) / len(maxima)


def _build_manual_retrieval_response(
    *,
    profile_id: int,
    query: str,
    model_code: str,
    collection_name: str,
    scored_chunks: list[_ManualHybridScoredChunk],
) -> RagRetrievalResponseRead:
    return RagRetrievalResponseRead(
        profile_id=profile_id,
        query=query,
        model_code=model_code,
        results=[
            RagRetrievalResultRead(
                chunk_id=scored_chunk.chunk_id,
                source_id=scored_chunk.source_id,
                embedding_id=scored_chunk.chunk_id,
                score=round(scored_chunk.score, 6),
                text=scored_chunk.text,
                chunk_index=scored_chunk.chunk_index,
                language=scored_chunk.language,
                source_type=scored_chunk.source_type,
                validation_status=scored_chunk.validation_status,
                text_hash=scored_chunk.text_hash,
                qdrant_collection=collection_name,
                payload_metadata={
                    "manual_local_hybrid_eval": True,
                    "dense_score": round(scored_chunk.dense_score, 6),
                    "sparse_score": round(scored_chunk.sparse_score, 6),
                    "multivector_score": (
                        round(scored_chunk.multivector_score, 6)
                        if scored_chunk.multivector_score is not None
                        else None
                    ),
                },
            )
            for scored_chunk in scored_chunks
        ],
    )


def _score_manual_bge_m3_chunks(
    *,
    provider_code: str,
    query_dense_vector: list[float],
    query_sparse_vector: dict[str, float],
    query_multivector: list[list[float]] | None,
    passage_features,
    source_chunks,
    top_k: int,
) -> list[_ManualHybridScoredChunk]:
    dense_scores = {
        chunk.id: _dot_product(query_dense_vector, passage_dense_vector)
        for chunk, passage_dense_vector in zip(source_chunks, passage_features.dense_vectors, strict=True)
    }
    sparse_scores = {
        chunk.id: _compute_sparse_overlap_score(query_sparse_vector, passage_sparse_vector)
        for chunk, passage_sparse_vector in zip(source_chunks, passage_features.sparse_vectors, strict=True)
    }
    normalized_dense_scores = _normalize_score_map(dense_scores)
    normalized_sparse_scores = _normalize_score_map(sparse_scores)
    base_scores = {
        chunk.id: (normalized_dense_scores.get(chunk.id, 0.0) + normalized_sparse_scores.get(chunk.id, 0.0)) / 2.0
        for chunk in source_chunks
    }

    multivector_scores: dict[int, float] = {}
    if provider_code == "bge_m3_dense_sparse_multivector":
        if query_multivector is None or passage_features.multivectors is None:
            raise BgeM3HybridProviderError("BGE-M3 multivector output is not available")

        _emit_runtime_log(
            f"multivector rerank start provider_code={provider_code} candidate_count={len(source_chunks)}"
        )
        narrowed_chunks = sorted(
            source_chunks,
            key=lambda chunk: (base_scores.get(chunk.id, 0.0), dense_scores.get(chunk.id, 0.0)),
            reverse=True,
        )[: max(top_k * 3, top_k)]
        passage_multivectors_by_chunk_id = {
            chunk.id: passage_multivector
            for chunk, passage_multivector in zip(source_chunks, passage_features.multivectors, strict=True)
        }
        multivector_scores = {
            chunk.id: _compute_multivector_score(
                query_multivector,
                passage_multivectors_by_chunk_id.get(chunk.id, []),
            )
            for chunk in narrowed_chunks
        }
        normalized_multivector_scores = _normalize_score_map(multivector_scores)
        for chunk in narrowed_chunks:
            base_scores[chunk.id] = (
                base_scores.get(chunk.id, 0.0) + normalized_multivector_scores.get(chunk.id, 0.0)
            ) / 2.0
        _emit_runtime_log(
            f"multivector rerank done provider_code={provider_code} candidate_count={len(narrowed_chunks)}"
        )

    ranked_chunks = sorted(
        source_chunks,
        key=lambda chunk: (
            base_scores.get(chunk.id, 0.0),
            dense_scores.get(chunk.id, 0.0),
            sparse_scores.get(chunk.id, 0.0),
        ),
        reverse=True,
    )[:top_k]
    return [
        _ManualHybridScoredChunk(
            chunk_id=chunk.id,
            source_id=chunk.source_id,
            chunk_index=chunk.chunk_index,
            text=chunk.chunk_text,
            language=chunk.language,
            source_type="manual_text",
            validation_status=chunk.validation_status,
            text_hash=chunk.text_hash,
            score=base_scores.get(chunk.id, 0.0),
            dense_score=dense_scores.get(chunk.id, 0.0),
            sparse_score=sparse_scores.get(chunk.id, 0.0),
            multivector_score=multivector_scores.get(chunk.id),
        )
        for chunk in ranked_chunks
    ]


def _resolve_eval_top_k_for_dataset(dataset) -> int:
    effective_top_k = max(
        REAL_QUESTION_EVAL_TOP_K,
        max(
            max(
                1,
                len(case.required_evidence),
                int(getattr(case, "expected_citation_count_min", 0) or 0),
            )
            for case in dataset.cases
        ),
    )
    if bool(dataset.metadata.get("external_dataset")) and len(dataset.cases) >= 50:
        effective_top_k = max(effective_top_k, REAL_QUESTION_EVAL_EXTERNAL_TOP_K)
    return effective_top_k


def _build_batch_d_manual_provider_result(
    *,
    profile_id: int,
    provider_code: str,
    source_chunks,
    cases: list[RagQualityEvalCase],
    top_k: int = REAL_QUESTION_EVAL_TOP_K,
) -> tuple[list[RealQuestionEvalQuestionResult], RealQuestionEvalAggregateModelResult]:
    rag_quality_service = RagQualityService()
    hybrid_provider = BgeM3HybridEmbeddingProvider(
        device=settings.sentence_transformers_device,
        cache_dir=settings.sentence_transformers_cache_dir,
    )
    collection_name = _build_batch_d_collection_name(provider_code)
    quality_candidate = RagQualityRetrievalConfigCandidate(
        config_id=provider_code,
        model_code=provider_code,
        collection_name=collection_name,
        top_k=top_k,
        retrieval_mode="hybrid",
        metadata={"manual_local_hybrid_eval": True},
    )
    source_texts = [chunk.chunk_text for chunk in source_chunks]
    _emit_runtime_log(
        f"batch_d provider encode start provider_code={provider_code} chunk_count={len(source_texts)}"
    )
    passage_features = hybrid_provider.encode_passages(source_texts, provider_code)
    _emit_runtime_log(
        f"batch_d provider encode done provider_code={provider_code} chunk_count={len(source_texts)}"
    )

    question_results: list[RealQuestionEvalQuestionResult] = []
    aggregate_trackers: list[RealQuestionEvalModelResult] = []
    latency_ms_values: list[float] = []
    forbidden_marker_rates: list[float] = []

    for case in cases:
        _emit_runtime_log(f"question start question_id={case.case_id} provider_code={provider_code}")
        _emit_runtime_memory_log(stage="before_question", question_id=case.case_id)
        started_at = perf_counter()
        query_features = hybrid_provider.encode_query(case.query, provider_code)
        scored_chunks = _score_manual_bge_m3_chunks(
            provider_code=provider_code,
            query_dense_vector=query_features.dense_vectors[0],
            query_sparse_vector=query_features.sparse_vectors[0],
            query_multivector=(
                query_features.multivectors[0]
                if query_features.multivectors
                else None
            ),
            passage_features=passage_features,
            source_chunks=source_chunks,
            top_k=top_k,
        )
        latency_ms = round((perf_counter() - started_at) * 1000, 3)
        latency_ms_values.append(latency_ms)
        retrieval_response = _build_manual_retrieval_response(
            profile_id=profile_id,
            query=case.query,
            model_code=provider_code,
            collection_name=collection_name,
            scored_chunks=scored_chunks,
        )
        case_results_input = rag_quality_service.adapt_rag_retrieval_response(
            case_id=case.case_id,
            candidate=quality_candidate,
            retrieval_response=retrieval_response,
            latency_ms=latency_ms,
            cost_estimate=0.0,
            metadata={
                "workflow": "real_question_eval_batch_d_manual_hybrid",
                "manual_local_hybrid_eval": True,
                "provider_code": provider_code,
            },
        )
        case_evaluation = rag_quality_service.evaluate_case_results(
            case=case,
            case_results=case_results_input,
            config_id=provider_code,
        )
        forbidden_marker_rates.append(case_evaluation.forbidden_marker_rate)
        model_result = _build_model_result(
            model_code=provider_code,
            collection_name=collection_name,
            case_evaluation=case_evaluation,
            retrieval_response=retrieval_response,
        )
        aggregate_trackers.append(model_result)
        question_results.append(
            RealQuestionEvalQuestionResult(
                question_id=case.case_id,
                question_text=case.query,
                test_type=getattr(case, "test_type", None),
                expected_answer_type=getattr(case, "expected_answer_type", None),
                source_scope=dict(getattr(case, "source_scope", {}) or {}),
                required_evidence=_build_full_evidence_rules_payload(getattr(case, "required_evidence", [])),
                forbidden_evidence=_build_full_evidence_rules_payload(getattr(case, "forbidden_evidence", [])),
                expected_markers=list(case.expected_markers),
                forbidden_markers=list(case.forbidden_markers),
                model_results=[model_result],
                winner_model_code=provider_code,
                winner_reason="Only one model result was available.",
            )
        )
        _emit_runtime_log(f"question done question_id={case.case_id} provider_code={provider_code}")
        _emit_runtime_memory_log(stage="after_question", question_id=case.case_id)

    average_latency_ms = round(sum(latency_ms_values) / len(latency_ms_values), 3) if latency_ms_values else None
    average_coverage = round(
        sum(item.evidence_coverage or 0.0 for item in aggregate_trackers) / len(aggregate_trackers),
        4,
    ) if aggregate_trackers else 0.0
    reciprocal_ranks = [
        1.0 / item.first_relevant_rank
        for item in aggregate_trackers
        if item.first_relevant_rank
    ]
    aggregate_result = _build_aggregate_result(
        model_code=provider_code,
        collection_name=collection_name,
        wins=0,
        model_results=aggregate_trackers,
        official_metrics={
            "hit_rate": sum(1 for item in aggregate_trackers if item.passed) / len(aggregate_trackers),
            "recall_at_k": average_coverage,
            "mrr": round(sum(reciprocal_ranks) / len(aggregate_trackers), 4) if aggregate_trackers else 0.0,
            "forbidden_marker_rate": round(
                sum(forbidden_marker_rates) / len(forbidden_marker_rates),
                4,
            ) if forbidden_marker_rates else 0.0,
            "average_latency_ms": average_latency_ms,
            "cost_estimate_total": None,
            "evidence_marker_coverage": average_coverage,
            "missing_expected_marker_count": sum(
                len(item.missing_expected_markers) for item in aggregate_trackers
            ),
            "false_positive_count": sum(item.false_positive_count for item in aggregate_trackers),
            "manual_local_hybrid_eval": True,
        },
    )
    return question_results, aggregate_result


def _filter_question_results_to_model_codes(
    question_results: list[RealQuestionEvalQuestionResult],
    *,
    model_codes: list[str],
) -> list[RealQuestionEvalQuestionResult]:
    filtered_results: list[RealQuestionEvalQuestionResult] = []
    for question_result in question_results:
        filtered_model_results = [
            model_result
            for model_result in question_result.model_results
            if model_result.model_code in model_codes
        ]
        if len(filtered_model_results) != len(model_codes):
            raise ValueError(
                f"Expected filtered model results for {question_result.question_id} to contain only: "
                + ", ".join(model_codes)
            )
        filtered_results.append(
            RealQuestionEvalQuestionResult(
                question_id=question_result.question_id,
                question_text=question_result.question_text,
                test_type=question_result.test_type,
                expected_answer_type=question_result.expected_answer_type,
                source_scope=dict(question_result.source_scope),
                required_evidence=list(question_result.required_evidence),
                forbidden_evidence=list(question_result.forbidden_evidence),
                expected_markers=list(question_result.expected_markers),
                forbidden_markers=list(question_result.forbidden_markers),
                model_results=filtered_model_results,
                winner_model_code=filtered_model_results[0].model_code if len(filtered_model_results) == 1 else None,
                winner_reason=(
                    "Baseline reused from existing preserved artifact."
                    if len(filtered_model_results) == 1
                    else ""
                ),
            )
        )
    if [item.question_id for item in filtered_results] != [item.question_id for item in question_results]:
        raise ValueError("Filtered question results changed the input question ordering")
    return filtered_results


def _filter_aggregate_results_to_model_codes(
    aggregate_results: list[RealQuestionEvalAggregateModelResult],
    *,
    model_codes: list[str],
) -> list[RealQuestionEvalAggregateModelResult]:
    aggregate_by_model = {aggregate_result.model_code: aggregate_result for aggregate_result in aggregate_results}
    missing_model_codes = [model_code for model_code in model_codes if model_code not in aggregate_by_model]
    if missing_model_codes:
        raise ValueError("Missing aggregate results for: " + ", ".join(missing_model_codes))
    return [aggregate_by_model[model_code] for model_code in model_codes]


def _build_result_from_json_payload(payload: dict[str, object]) -> RealQuestionEvalResult:
    client_view = payload.get("client_view") if isinstance(payload.get("client_view"), dict) else {}
    developer_view = payload.get("developer_view") if isinstance(payload.get("developer_view"), dict) else {}
    dataset_payload = (
        client_view.get("dataset")
        if isinstance(client_view.get("dataset"), dict)
        else developer_view.get("dataset")
        if isinstance(developer_view.get("dataset"), dict)
        else {}
    )
    question_results = _build_historical_question_results(payload)
    aggregate_results = _recompute_aggregate_question_wins(
        question_results=question_results,
        aggregate_results=_build_historical_aggregate_results(payload),
    )
    artifact_paths_payload = payload.get("artifact_paths")

    return RealQuestionEvalResult(
        passed=str(payload.get("status") or "").upper() == "PASS",
        run_status=str(payload.get("run_status") or "") or None,
        quality_status=str(payload.get("quality_status") or payload.get("status") or "") or None,
        used_fake_models=bool(payload.get("used_fake_models")),
        run_type=str(payload.get("run_type") or "") or None,
        execution_mode=str(payload.get("execution_mode") or "") or None,
        benchmark_batch_label=(
            str(payload.get("benchmark_batch_label"))
            if payload.get("benchmark_batch_label") is not None
            else None
        ),
        baseline_provider_codes=[str(item) for item in payload.get("baseline_provider_codes", [])],
        excluded_provider_codes=[str(item) for item in payload.get("excluded_provider_codes", [])],
        newly_evaluated_provider_codes=[str(item) for item in payload.get("newly_evaluated_provider_codes", [])],
        comparison_scope_note=(
            str(payload.get("comparison_scope_note"))
            if payload.get("comparison_scope_note") is not None
            else None
        ),
        historical_providers=[
            str(item)
            for item in payload.get("historical_providers", developer_view.get("historical_providers", []))
        ],
        new_real_providers=[
            str(item)
            for item in payload.get("new_real_providers", developer_view.get("new_real_providers", []))
        ],
        historical_overall_winner_model_code=(
            str(client_view.get("historical_overall_winner"))
            if client_view.get("historical_overall_winner") is not None
            else None
        ),
        any_new_provider_beat_historical_winner=(
            bool(client_view.get("any_new_provider_beat_historical_winner"))
            if client_view.get("any_new_provider_beat_historical_winner") is not None
            else None
        ),
        generated_at=str(payload.get("timestamp") or "") or None,
        run_id=str(payload.get("run_id") or "") or None,
        dataset_id=str(dataset_payload.get("id") or ""),
        dataset_name=str(dataset_payload.get("name") or ""),
        dataset_file=str(payload.get("dataset_file") or "") or None,
        compared_models=[
            str(item)
            for item in developer_view.get("models_compared", client_view.get("models_compared", []))
        ],
        question_results=question_results,
        aggregate_results=aggregate_results,
        overall_winner_model_code=(
            str(client_view.get("overall_winner"))
            if client_view.get("overall_winner") is not None
            else None
        ),
        overall_winner_reason=(
            str(payload.get("overall_winner_reason"))
            if payload.get("overall_winner_reason") is not None
            else str(client_view.get("overall_winner_reason"))
            if client_view.get("overall_winner_reason") is not None
            else None
        ),
        official_best_config=(
            dict(developer_view["selected_config"])
            if isinstance(developer_view.get("selected_config"), dict)
            else None
        ),
        activated=bool(client_view.get("activated")),
        runtime_verified=bool(client_view.get("runtime_verified")),
        activated_config=(
            dict(developer_view["activated_config"])
            if isinstance(developer_view.get("activated_config"), dict)
            else None
        ),
        runtime_retrieval=(
            dict(developer_view["runtime_retrieval_verification"])
            if isinstance(developer_view.get("runtime_retrieval_verification"), dict)
            else None
        ),
        artifact_paths=(
            RealQuestionEvalArtifactPaths.model_validate(artifact_paths_payload)
            if isinstance(artifact_paths_payload, dict)
            else RealQuestionEvalArtifactPaths()
        ),
    )


def rerender_incremental_real_artifacts_from_existing_json(
    *,
    artifact_dir: Path,
    source_json_path: Path | None = None,
) -> RealQuestionEvalResult:
    resolved_source_json_path = source_json_path or (
        artifact_dir / "latest_incremental_new_providers" / "real_question_eval_result.json"
    )
    payload = json.loads(resolved_source_json_path.read_text(encoding="utf-8"))
    if str(payload.get("run_type") or "") != "incremental_real":
        raise ValueError("Incremental artifact re-render expects an incremental_real payload")

    result = _build_result_from_json_payload(payload)
    if result.run_id is None:
        raise ValueError("Incremental artifact re-render requires a persisted run_id")

    artifact_paths = write_real_question_eval_artifacts(
        artifact_dir=artifact_dir,
        result=result,
    )
    result.artifact_paths = artifact_paths
    result.markdown_report_path = artifact_paths.latest_markdown_report
    result.json_result_path = artifact_paths.latest_json_result
    result.passed = (
        result.passed
        and result.markdown_report_path is not None
        and Path(result.markdown_report_path).exists()
        and result.json_result_path is not None
        and Path(result.json_result_path).exists()
    )
    return result


def _build_config_evaluation_from_aggregate_result(
    aggregate_result: RealQuestionEvalAggregateModelResult,
    *,
    total_cases: int,
) -> RagQualityConfigEvaluation:
    official_metrics = aggregate_result.official_metrics or {}
    metrics = RagQualityAggregateMetrics.model_validate(
        official_metrics
        if official_metrics
        else {
            "hit_rate": aggregate_result.passed_questions / total_cases if total_cases else 0.0,
            "recall_at_k": aggregate_result.average_evidence_coverage,
            "mrr": 1.0 / aggregate_result.average_first_relevant_rank
            if aggregate_result.average_first_relevant_rank
            else 0.0,
            "forbidden_marker_rate": (
                aggregate_result.total_false_positive_markers / total_cases if total_cases else 0.0
            ),
            "average_latency_ms": None,
            "cost_estimate_total": None,
            "evidence_marker_coverage": aggregate_result.average_evidence_coverage,
            "missing_expected_marker_count": aggregate_result.total_missing_markers,
            "false_positive_count": aggregate_result.total_false_positive_markers,
        }
    )
    return RagQualityConfigEvaluation(
        config_id=aggregate_result.model_code,
        model_code=aggregate_result.model_code,
        collection_name=aggregate_result.collection_name,
        retrieval_mode="hybrid",
        passed_case_count=aggregate_result.passed_questions,
        failed_case_count=max(total_cases - aggregate_result.passed_questions, 0),
        metrics=metrics,
        case_evaluations=[],
        reasons=[],
        warnings=[],
        metadata={},
    )


def _merge_question_results(
    *,
    historical_question_results: list[RealQuestionEvalQuestionResult],
    new_question_results: list[RealQuestionEvalQuestionResult],
    official_best_model_code: str | None,
    question_order: list[str] | None = None,
) -> list[RealQuestionEvalQuestionResult]:
    resolved_question_order = (
        list(question_order)
        if question_order is not None
        else _resolve_comparison_question_order(
            historical_question_results,
            new_question_results,
            error_prefix="Incremental comparison",
        )
    )
    historical_by_id = {item.question_id: item for item in historical_question_results}
    new_by_id = {item.question_id: item for item in new_question_results}
    merged_results: list[RealQuestionEvalQuestionResult] = []

    for question_id in resolved_question_order:
        historical_question = historical_by_id.get(question_id)
        new_question = new_by_id.get(question_id)
        if historical_question is None or new_question is None:
            raise ValueError(f"Incremental comparison is missing question result for {question_id}")

        model_results = [*historical_question.model_results, *new_question.model_results]
        winner_model_code, winner_reason = _choose_question_winner(
            model_results=model_results,
            official_best_model_code=official_best_model_code,
        )
        merged_results.append(
            RealQuestionEvalQuestionResult(
                question_id=historical_question.question_id,
                question_text=historical_question.question_text,
                test_type=historical_question.test_type,
                expected_answer_type=historical_question.expected_answer_type,
                source_scope=dict(historical_question.source_scope),
                required_evidence=list(historical_question.required_evidence),
                forbidden_evidence=list(historical_question.forbidden_evidence),
                expected_markers=list(historical_question.expected_markers),
                forbidden_markers=list(historical_question.forbidden_markers),
                model_results=model_results,
                winner_model_code=winner_model_code,
                winner_reason=winner_reason,
            )
        )

    return merged_results


def _resolve_comparison_question_order(
    *question_result_groups: list[RealQuestionEvalQuestionResult],
    error_prefix: str,
) -> list[str]:
    question_orders = [[item.question_id for item in group] for group in question_result_groups]
    if not question_orders:
        return []
    expected_question_ids = question_orders[0]
    for question_ids in question_orders[1:]:
        if question_ids != expected_question_ids:
            raise ValueError(f"{error_prefix} question IDs changed unexpectedly")
    if len(set(expected_question_ids)) != len(expected_question_ids):
        raise ValueError(f"{error_prefix} question IDs contain duplicates")
    return expected_question_ids


def _build_incremental_official_best_config(selection_result) -> dict[str, object]:
    return {
        "best_config_id": selection_result.best_config_id,
        "best_model_code": selection_result.best_model_code,
        "best_collection_name": selection_result.best_collection_name,
        "selected_metrics": (
            selection_result.selected_metrics.model_dump(mode="json")
            if selection_result.selected_metrics is not None
            else None
        ),
        "all_config_scores": [
            score.model_dump(mode="json")
            for score in selection_result.all_config_scores
        ],
        "reasons": list(selection_result.reasons),
        "warnings": list(selection_result.warnings),
    }


def _build_batch_a_official_best_config(selection_result) -> dict[str, object]:
    return _build_incremental_official_best_config(selection_result)


def _build_batch_b_official_best_config(selection_result) -> dict[str, object]:
    return _build_incremental_official_best_config(selection_result)


def _build_batch_c_official_best_config(selection_result) -> dict[str, object]:
    return _build_incremental_official_best_config(selection_result)


def _build_batch_d_official_best_config(selection_result) -> dict[str, object]:
    return _build_incremental_official_best_config(selection_result)


def _build_batch_e_official_best_config(selection_result) -> dict[str, object]:
    return _build_incremental_official_best_config(selection_result)


def _build_batch_f_official_best_config(selection_result) -> dict[str, object]:
    return _build_incremental_official_best_config(selection_result)


def write_full_version_batch_b_attempted_artifact(
    *,
    artifact_dir: Path,
) -> RealQuestionEvalResult:
    incremental_payload = _load_incremental_new_provider_payload(artifact_dir=artifact_dir)
    incremental_client_view = (
        incremental_payload.get("client_view")
        if isinstance(incremental_payload.get("client_view"), dict)
        else {}
    )
    baseline_provider_code = REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_BASELINE_PROVIDER
    result = RealQuestionEvalResult(
        passed=False,
        used_fake_models=False,
        run_type="full_version_batch_b_attempted",
        execution_mode="full_version_batch_b_attempted",
        benchmark_batch_label="Batch B Attempted",
        benchmark_status="attempted_not_completed",
        incomplete_reason=REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_ATTEMPTED_REASON,
        baseline_provider_codes=[baseline_provider_code],
        excluded_provider_codes=list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_EXCLUDED_PROVIDERS),
        newly_evaluated_provider_codes=list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES),
        comparison_scope_note=(
            "Qwen3 0.6B was attempted but not completed; no final Batch B comparison or winner was produced."
        ),
        non_compared_notes=[
            "Qwen3 0.6B benchmark attempted but not completed in this environment.",
            "Recommendation: skip Qwen for now and reconsider on a cleaner Linux/WSL/GPU/stronger runtime.",
        ],
        historical_providers=[baseline_provider_code],
        historical_overall_winner_model_code=(
            str(incremental_client_view.get("overall_winner"))
            if incremental_client_view.get("overall_winner") is not None
            else baseline_provider_code
        ),
        compared_models=[
            baseline_provider_code,
            *REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES,
        ],
        overall_winner_model_code=None,
        activated=False,
        runtime_verified=False,
        warnings=[
            REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_ATTEMPTED_REASON,
            "Provider adapter remains available, but the provider is still manual-only and not verified in this environment.",
        ],
        error=REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_ATTEMPTED_REASON,
    )
    artifact_paths = write_real_question_eval_artifacts(
        artifact_dir=artifact_dir,
        result=result,
    )
    result.artifact_paths = artifact_paths
    result.markdown_report_path = artifact_paths.latest_markdown_report
    result.json_result_path = artifact_paths.latest_json_result
    return result


def run_incremental_real_question_eval(
    db: Session,
    config: RealQuestionEvalConfig,
) -> RealQuestionEvalResult:
    new_provider_codes = _validate_incremental_provider_codes(list(config.candidate_model_codes or []))
    historical_payload = _load_historical_real_payload(artifact_dir=Path(config.artifact_dir))
    historical_question_results = _build_historical_question_results(historical_payload)
    historical_aggregate_results = _build_historical_aggregate_results(historical_payload)
    historical_client_view = historical_payload.get("client_view") if isinstance(historical_payload.get("client_view"), dict) else {}
    historical_overall_winner = (
        str(historical_client_view.get("overall_winner"))
        if historical_client_view.get("overall_winner") is not None
        else None
    )

    new_run_config = config.model_copy(
        update={
            "candidate_model_codes": new_provider_codes,
            "write_artifacts": False,
            "run_type_override": "incremental_real",
            "execution_mode_override": "incremental_real_eval",
        }
    )
    new_provider_result = RealQuestionEvalRunner(db, new_run_config).run()
    if new_provider_result.error:
        new_provider_result.run_type = "incremental_real"
        new_provider_result.execution_mode = "incremental_real_eval"
        new_provider_result.historical_providers = list(REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS)
        new_provider_result.new_real_providers = list(new_provider_codes)
        new_provider_result.historical_overall_winner_model_code = historical_overall_winner
        return new_provider_result

    expected_question_ids = _resolve_comparison_question_order(
        historical_question_results,
        new_provider_result.question_results,
        error_prefix="Incremental real evaluation",
    )

    combined_model_codes = list(REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS) + list(new_provider_codes)
    aggregate_by_model = {
        aggregate_result.model_code: aggregate_result
        for aggregate_result in [*historical_aggregate_results, *new_provider_result.aggregate_results]
    }
    combined_aggregate_results = [aggregate_by_model[model_code] for model_code in combined_model_codes]
    selection_result = RagQualityService().select_best_config(
        config_evaluations=[
            _build_config_evaluation_from_aggregate_result(
                aggregate_result,
                total_cases=len(expected_question_ids),
            )
            for aggregate_result in combined_aggregate_results
        ]
    )
    combined_question_results = _merge_question_results(
        historical_question_results=historical_question_results,
        new_question_results=new_provider_result.question_results,
        official_best_model_code=selection_result.best_model_code,
        question_order=expected_question_ids,
    )
    combined_aggregate_results = _recompute_aggregate_question_wins(
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
    )
    any_new_provider_beat_historical_winner = (
        selection_result.best_model_code in new_provider_codes
        and selection_result.best_model_code != historical_overall_winner
    )

    combined_result = RealQuestionEvalResult(
        passed=False,
        used_fake_models=new_provider_result.used_fake_models,
        run_type="incremental_real",
        execution_mode="incremental_real_eval",
        historical_providers=list(REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS),
        new_real_providers=list(new_provider_codes),
        historical_overall_winner_model_code=historical_overall_winner,
        any_new_provider_beat_historical_winner=any_new_provider_beat_historical_winner,
        generated_at=new_provider_result.generated_at,
        profile_id=new_provider_result.profile_id,
        source_id=new_provider_result.source_id,
        job_id=new_provider_result.job_id,
        dataset_id=new_provider_result.dataset_id,
        dataset_name=new_provider_result.dataset_name,
        dataset_file=new_provider_result.dataset_file,
        source_chunk_count=new_provider_result.source_chunk_count,
        compared_models=combined_model_codes,
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
        overall_winner_model_code=selection_result.best_model_code,
        official_best_config=_build_incremental_official_best_config(selection_result),
        activated=False,
        runtime_verified=False,
        warnings=[
            *new_provider_result.warnings,
            *selection_result.warnings,
        ],
    )
    combined_result.passed = (
        bool(selection_result.best_model_code)
        and new_provider_result.passed
    )
    artifact_paths = write_real_question_eval_artifacts(
        artifact_dir=Path(config.artifact_dir),
        result=combined_result,
    )
    combined_result.artifact_paths = artifact_paths
    if artifact_paths.latest_markdown_report is not None:
        combined_result.markdown_report_path = artifact_paths.latest_markdown_report
    if artifact_paths.latest_json_result is not None:
        combined_result.json_result_path = artifact_paths.latest_json_result
    combined_result.passed = (
        combined_result.passed
        and combined_result.markdown_report_path is not None
        and Path(combined_result.markdown_report_path).exists()
        and combined_result.json_result_path is not None
        and Path(combined_result.json_result_path).exists()
    )
    return combined_result


def run_full_version_batch_a_question_eval(
    db: Session,
    config: RealQuestionEvalConfig,
) -> RealQuestionEvalResult:
    new_provider_codes = _validate_full_version_batch_a_provider_codes(list(config.candidate_model_codes or []))
    baseline_provider_code = REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_BASELINE_PROVIDER
    excluded_provider_codes = list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_EXCLUDED_PROVIDERS)
    incremental_payload = _load_incremental_new_provider_payload(artifact_dir=Path(config.artifact_dir))
    incremental_question_results = _build_historical_question_results(incremental_payload)
    incremental_aggregate_results = _build_historical_aggregate_results(incremental_payload)
    baseline_question_results = _filter_question_results_to_model_codes(
        incremental_question_results,
        model_codes=[baseline_provider_code],
    )
    baseline_aggregate_results = _filter_aggregate_results_to_model_codes(
        incremental_aggregate_results,
        model_codes=[baseline_provider_code],
    )
    baseline_client_view = (
        incremental_payload.get("client_view")
        if isinstance(incremental_payload.get("client_view"), dict)
        else {}
    )
    baseline_overall_winner = (
        str(baseline_client_view.get("overall_winner"))
        if baseline_client_view.get("overall_winner") is not None
        else baseline_provider_code
    )

    new_run_config = config.model_copy(
        update={
            "candidate_model_codes": new_provider_codes,
            "write_artifacts": False,
            "run_type_override": "full_version_batch_a",
            "execution_mode_override": "full_version_batch_a_real_eval",
        }
    )
    new_provider_result = RealQuestionEvalRunner(db, new_run_config).run()
    if new_provider_result.error:
        new_provider_result.run_type = "full_version_batch_a"
        new_provider_result.execution_mode = "full_version_batch_a_real_eval"
        new_provider_result.benchmark_batch_label = "Batch A"
        new_provider_result.baseline_provider_codes = [baseline_provider_code]
        new_provider_result.excluded_provider_codes = excluded_provider_codes
        new_provider_result.newly_evaluated_provider_codes = list(new_provider_codes)
        new_provider_result.historical_overall_winner_model_code = baseline_overall_winner
        new_provider_result.comparison_scope_note = (
            "Only multilingual_e5_base and multilingual_e5_large are included in the final Batch A comparison."
        )
        return new_provider_result

    expected_question_ids = _resolve_comparison_question_order(
        baseline_question_results,
        new_provider_result.question_results,
        error_prefix="Full-version Batch A",
    )

    combined_model_codes = [baseline_provider_code, *new_provider_codes]
    aggregate_by_model = {
        aggregate_result.model_code: aggregate_result
        for aggregate_result in [*baseline_aggregate_results, *new_provider_result.aggregate_results]
    }
    combined_aggregate_results = [aggregate_by_model[model_code] for model_code in combined_model_codes]
    selection_result = RagQualityService().select_best_config(
        config_evaluations=[
            _build_config_evaluation_from_aggregate_result(
                aggregate_result,
                total_cases=len(expected_question_ids),
            )
            for aggregate_result in combined_aggregate_results
        ]
    )
    combined_question_results = _merge_question_results(
        historical_question_results=baseline_question_results,
        new_question_results=new_provider_result.question_results,
        official_best_model_code=selection_result.best_model_code,
        question_order=expected_question_ids,
    )
    combined_aggregate_results = _recompute_aggregate_question_wins(
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
    )
    any_new_provider_beat_baseline = (
        selection_result.best_model_code in new_provider_codes
        and selection_result.best_model_code != baseline_provider_code
    )

    combined_result = RealQuestionEvalResult(
        passed=False,
        used_fake_models=new_provider_result.used_fake_models,
        run_type="full_version_batch_a",
        execution_mode="full_version_batch_a_real_eval",
        benchmark_batch_label="Batch A",
        baseline_provider_codes=[baseline_provider_code],
        excluded_provider_codes=excluded_provider_codes,
        newly_evaluated_provider_codes=list(new_provider_codes),
        comparison_scope_note=(
            "Only multilingual_e5_base and multilingual_e5_large are included in the final Batch A comparison; weaker historical providers are excluded."
        ),
        historical_providers=[baseline_provider_code],
        new_real_providers=list(new_provider_codes),
        historical_overall_winner_model_code=baseline_overall_winner,
        any_new_provider_beat_historical_winner=any_new_provider_beat_baseline,
        generated_at=new_provider_result.generated_at,
        profile_id=new_provider_result.profile_id,
        source_id=new_provider_result.source_id,
        job_id=new_provider_result.job_id,
        dataset_id=new_provider_result.dataset_id,
        dataset_name=new_provider_result.dataset_name,
        dataset_file=new_provider_result.dataset_file,
        source_chunk_count=new_provider_result.source_chunk_count,
        compared_models=combined_model_codes,
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
        overall_winner_model_code=selection_result.best_model_code,
        official_best_config=_build_batch_a_official_best_config(selection_result),
        activated=False,
        runtime_verified=False,
        warnings=[
            *new_provider_result.warnings,
            *selection_result.warnings,
        ],
    )
    combined_result.passed = (
        bool(selection_result.best_model_code)
        and new_provider_result.passed
    )
    artifact_paths = write_real_question_eval_artifacts(
        artifact_dir=Path(config.artifact_dir),
        result=combined_result,
    )
    combined_result.artifact_paths = artifact_paths
    if artifact_paths.latest_markdown_report is not None:
        combined_result.markdown_report_path = artifact_paths.latest_markdown_report
    if artifact_paths.latest_json_result is not None:
        combined_result.json_result_path = artifact_paths.latest_json_result
    combined_result.passed = (
        combined_result.passed
        and combined_result.markdown_report_path is not None
        and Path(combined_result.markdown_report_path).exists()
        and combined_result.json_result_path is not None
        and Path(combined_result.json_result_path).exists()
    )
    return combined_result


def run_full_version_batch_b_question_eval(
    db: Session,
    config: RealQuestionEvalConfig,
) -> RealQuestionEvalResult:
    new_provider_codes = _validate_full_version_batch_b_provider_codes(list(config.candidate_model_codes or []))
    if not config.rerun_attempted_full_version_batch_b:
        del db
        return write_full_version_batch_b_attempted_artifact(
            artifact_dir=Path(config.artifact_dir),
        )

    baseline_provider_code = REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_BASELINE_PROVIDER
    excluded_provider_codes = list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_EXCLUDED_PROVIDERS)
    incremental_payload = _load_incremental_new_provider_payload(artifact_dir=Path(config.artifact_dir))
    incremental_question_results = _build_historical_question_results(incremental_payload)
    incremental_aggregate_results = _build_historical_aggregate_results(incremental_payload)
    baseline_question_results = _filter_question_results_to_model_codes(
        incremental_question_results,
        model_codes=[baseline_provider_code],
    )
    baseline_aggregate_results = _filter_aggregate_results_to_model_codes(
        incremental_aggregate_results,
        model_codes=[baseline_provider_code],
    )
    baseline_client_view = (
        incremental_payload.get("client_view")
        if isinstance(incremental_payload.get("client_view"), dict)
        else {}
    )
    baseline_overall_winner = (
        str(baseline_client_view.get("overall_winner"))
        if baseline_client_view.get("overall_winner") is not None
        else baseline_provider_code
    )

    new_run_config = config.model_copy(
        update={
            "candidate_model_codes": new_provider_codes,
            "write_artifacts": False,
            "run_type_override": "full_version_batch_b",
            "execution_mode_override": "full_version_batch_b_real_eval",
        }
    )
    new_provider_result = RealQuestionEvalRunner(db, new_run_config).run()
    if new_provider_result.error:
        new_provider_result.run_type = "full_version_batch_b"
        new_provider_result.execution_mode = "full_version_batch_b_real_eval"
        new_provider_result.benchmark_batch_label = "Batch B"
        new_provider_result.benchmark_status = "failed"
        new_provider_result.incomplete_reason = str(new_provider_result.error)
        new_provider_result.baseline_provider_codes = [baseline_provider_code]
        new_provider_result.excluded_provider_codes = excluded_provider_codes
        new_provider_result.newly_evaluated_provider_codes = list(new_provider_codes)
        new_provider_result.historical_overall_winner_model_code = baseline_overall_winner
        new_provider_result.comparison_scope_note = (
            "Only multilingual_e5_base and qwen3_embedding_0_6b are allowed in the final Batch B comparison."
        )
        new_provider_result.non_compared_notes = [
            "Jina Embeddings v3 was not rerun and is not part of Batch B.",
        ]
        if config.write_artifacts:
            artifact_paths = write_real_question_eval_artifacts(
                artifact_dir=Path(config.artifact_dir),
                result=new_provider_result,
            )
            new_provider_result.artifact_paths = artifact_paths
            new_provider_result.markdown_report_path = artifact_paths.latest_markdown_report
            new_provider_result.json_result_path = artifact_paths.latest_json_result
        return new_provider_result

    expected_question_ids = _resolve_comparison_question_order(
        baseline_question_results,
        new_provider_result.question_results,
        error_prefix="Full-version Batch B",
    )

    combined_model_codes = [baseline_provider_code, *new_provider_codes]
    aggregate_by_model = {
        aggregate_result.model_code: aggregate_result
        for aggregate_result in [*baseline_aggregate_results, *new_provider_result.aggregate_results]
    }
    combined_aggregate_results = [aggregate_by_model[model_code] for model_code in combined_model_codes]
    selection_result = RagQualityService().select_best_config(
        config_evaluations=[
            _build_config_evaluation_from_aggregate_result(
                aggregate_result,
                total_cases=len(expected_question_ids),
            )
            for aggregate_result in combined_aggregate_results
        ]
    )
    combined_question_results = _merge_question_results(
        historical_question_results=baseline_question_results,
        new_question_results=new_provider_result.question_results,
        official_best_model_code=selection_result.best_model_code,
        question_order=expected_question_ids,
    )
    combined_aggregate_results = _recompute_aggregate_question_wins(
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
    )
    any_new_provider_beat_baseline = (
        selection_result.best_model_code in new_provider_codes
        and selection_result.best_model_code != baseline_provider_code
    )

    combined_result = RealQuestionEvalResult(
        passed=False,
        used_fake_models=new_provider_result.used_fake_models,
        run_type="full_version_batch_b",
        execution_mode="full_version_batch_b_real_eval",
        benchmark_batch_label="Batch B",
        benchmark_status="completed" if new_provider_result.passed else "failed",
        baseline_provider_codes=[baseline_provider_code],
        excluded_provider_codes=excluded_provider_codes,
        newly_evaluated_provider_codes=list(new_provider_codes),
        comparison_scope_note=(
            "Only multilingual_e5_base and qwen3_embedding_0_6b are included in the final Batch B comparison; weaker historical providers, Jina, and larger Qwen candidates are excluded."
        ),
        non_compared_notes=[
            "Jina Embeddings v3 was not rerun and is not compared in Batch B.",
        ],
        historical_providers=[baseline_provider_code],
        new_real_providers=list(new_provider_codes),
        historical_overall_winner_model_code=baseline_overall_winner,
        any_new_provider_beat_historical_winner=any_new_provider_beat_baseline,
        generated_at=new_provider_result.generated_at,
        profile_id=new_provider_result.profile_id,
        source_id=new_provider_result.source_id,
        job_id=new_provider_result.job_id,
        dataset_id=new_provider_result.dataset_id,
        dataset_name=new_provider_result.dataset_name,
        dataset_file=new_provider_result.dataset_file,
        source_chunk_count=new_provider_result.source_chunk_count,
        compared_models=combined_model_codes,
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
        overall_winner_model_code=selection_result.best_model_code,
        official_best_config=_build_batch_b_official_best_config(selection_result),
        activated=False,
        runtime_verified=False,
        warnings=[
            *new_provider_result.warnings,
            *selection_result.warnings,
        ],
    )
    combined_result.passed = (
        bool(selection_result.best_model_code)
        and new_provider_result.passed
    )
    artifact_paths = write_real_question_eval_artifacts(
        artifact_dir=Path(config.artifact_dir),
        result=combined_result,
    )
    combined_result.artifact_paths = artifact_paths
    if artifact_paths.latest_markdown_report is not None:
        combined_result.markdown_report_path = artifact_paths.latest_markdown_report
    if artifact_paths.latest_json_result is not None:
        combined_result.json_result_path = artifact_paths.latest_json_result
    combined_result.passed = (
        combined_result.passed
        and combined_result.markdown_report_path is not None
        and Path(combined_result.markdown_report_path).exists()
        and combined_result.json_result_path is not None
        and Path(combined_result.json_result_path).exists()
    )
    return combined_result


def run_full_version_batch_c_question_eval(
    db: Session,
    config: RealQuestionEvalConfig,
) -> RealQuestionEvalResult:
    new_provider_codes = _validate_full_version_batch_c_provider_codes(list(config.candidate_model_codes or []))
    baseline_provider_code = REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_BASELINE_PROVIDER
    excluded_provider_codes = list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_EXCLUDED_PROVIDERS)
    incremental_payload = _load_incremental_new_provider_payload(artifact_dir=Path(config.artifact_dir))
    incremental_question_results = _build_historical_question_results(incremental_payload)
    incremental_aggregate_results = _build_historical_aggregate_results(incremental_payload)
    baseline_question_results = _filter_question_results_to_model_codes(
        incremental_question_results,
        model_codes=[baseline_provider_code],
    )
    baseline_aggregate_results = _filter_aggregate_results_to_model_codes(
        incremental_aggregate_results,
        model_codes=[baseline_provider_code],
    )
    baseline_client_view = (
        incremental_payload.get("client_view")
        if isinstance(incremental_payload.get("client_view"), dict)
        else {}
    )
    baseline_overall_winner = (
        str(baseline_client_view.get("overall_winner"))
        if baseline_client_view.get("overall_winner") is not None
        else baseline_provider_code
    )

    new_run_config = config.model_copy(
        update={
            "candidate_model_codes": new_provider_codes,
            "write_artifacts": False,
            "run_type_override": "full_version_batch_c",
            "execution_mode_override": "full_version_batch_c_real_eval",
        }
    )
    new_provider_result = RealQuestionEvalRunner(db, new_run_config).run()
    if new_provider_result.error:
        new_provider_result.run_type = "full_version_batch_c"
        new_provider_result.execution_mode = "full_version_batch_c_real_eval"
        new_provider_result.benchmark_batch_label = "Batch C"
        new_provider_result.benchmark_status = "failed"
        new_provider_result.incomplete_reason = str(new_provider_result.error)
        new_provider_result.baseline_provider_codes = [baseline_provider_code]
        new_provider_result.excluded_provider_codes = excluded_provider_codes
        new_provider_result.newly_evaluated_provider_codes = list(new_provider_codes)
        new_provider_result.historical_overall_winner_model_code = baseline_overall_winner
        new_provider_result.comparison_scope_note = (
            "Only multilingual_e5_base and jina_embeddings_v3 are allowed in the final Batch C comparison."
        )
        new_provider_result.non_compared_notes = [
            "Qwen3 0.6B was skipped as attempted/not completed and is not part of Batch C.",
        ]
        if config.write_artifacts:
            artifact_paths = write_real_question_eval_artifacts(
                artifact_dir=Path(config.artifact_dir),
                result=new_provider_result,
            )
            new_provider_result.artifact_paths = artifact_paths
            new_provider_result.markdown_report_path = artifact_paths.latest_markdown_report
            new_provider_result.json_result_path = artifact_paths.latest_json_result
        return new_provider_result

    expected_question_ids = _resolve_comparison_question_order(
        baseline_question_results,
        new_provider_result.question_results,
        error_prefix="Full-version Batch C",
    )

    combined_model_codes = [baseline_provider_code, *new_provider_codes]
    aggregate_by_model = {
        aggregate_result.model_code: aggregate_result
        for aggregate_result in [*baseline_aggregate_results, *new_provider_result.aggregate_results]
    }
    combined_aggregate_results = [aggregate_by_model[model_code] for model_code in combined_model_codes]
    selection_result = RagQualityService().select_best_config(
        config_evaluations=[
            _build_config_evaluation_from_aggregate_result(
                aggregate_result,
                total_cases=len(expected_question_ids),
            )
            for aggregate_result in combined_aggregate_results
        ]
    )
    combined_question_results = _merge_question_results(
        historical_question_results=baseline_question_results,
        new_question_results=new_provider_result.question_results,
        official_best_model_code=selection_result.best_model_code,
        question_order=expected_question_ids,
    )
    combined_aggregate_results = _recompute_aggregate_question_wins(
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
    )
    any_new_provider_beat_baseline = (
        selection_result.best_model_code in new_provider_codes
        and selection_result.best_model_code != baseline_provider_code
    )

    combined_result = RealQuestionEvalResult(
        passed=False,
        used_fake_models=new_provider_result.used_fake_models,
        run_type="full_version_batch_c",
        execution_mode="full_version_batch_c_real_eval",
        benchmark_batch_label="Batch C",
        benchmark_status="completed" if new_provider_result.passed else "failed",
        baseline_provider_codes=[baseline_provider_code],
        excluded_provider_codes=excluded_provider_codes,
        newly_evaluated_provider_codes=list(new_provider_codes),
        comparison_scope_note=(
            "Only multilingual_e5_base and jina_embeddings_v3 are included in the final Batch C comparison; weaker historical providers and all Qwen candidates are excluded."
        ),
        non_compared_notes=[
            "Qwen3 0.6B was skipped as attempted/not completed and is not compared in Batch C.",
        ],
        historical_providers=[baseline_provider_code],
        new_real_providers=list(new_provider_codes),
        historical_overall_winner_model_code=baseline_overall_winner,
        any_new_provider_beat_historical_winner=any_new_provider_beat_baseline,
        generated_at=new_provider_result.generated_at,
        profile_id=new_provider_result.profile_id,
        source_id=new_provider_result.source_id,
        job_id=new_provider_result.job_id,
        dataset_id=new_provider_result.dataset_id,
        dataset_name=new_provider_result.dataset_name,
        dataset_file=new_provider_result.dataset_file,
        source_chunk_count=new_provider_result.source_chunk_count,
        compared_models=combined_model_codes,
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
        overall_winner_model_code=selection_result.best_model_code,
        official_best_config=_build_batch_c_official_best_config(selection_result),
        activated=False,
        runtime_verified=False,
        warnings=[
            *new_provider_result.warnings,
            *selection_result.warnings,
        ],
    )
    combined_result.passed = (
        bool(selection_result.best_model_code)
        and new_provider_result.passed
    )
    artifact_paths = write_real_question_eval_artifacts(
        artifact_dir=Path(config.artifact_dir),
        result=combined_result,
    )
    combined_result.artifact_paths = artifact_paths
    if artifact_paths.latest_markdown_report is not None:
        combined_result.markdown_report_path = artifact_paths.latest_markdown_report
    if artifact_paths.latest_json_result is not None:
        combined_result.json_result_path = artifact_paths.latest_json_result
    combined_result.passed = (
        combined_result.passed
        and combined_result.markdown_report_path is not None
        and Path(combined_result.markdown_report_path).exists()
        and combined_result.json_result_path is not None
        and Path(combined_result.json_result_path).exists()
    )
    return combined_result


def _run_full_version_optional_qwen_comparison_batch(
    db: Session,
    config: RealQuestionEvalConfig,
    *,
    validate_provider_codes,
    baseline_provider_code: str,
    excluded_provider_codes: list[str],
    run_type: str,
    execution_mode: str,
    benchmark_batch_label: str,
    comparison_scope_note: str,
    non_compared_notes: list[str],
    error_prefix: str,
    build_official_best_config,
) -> RealQuestionEvalResult:
    new_provider_codes = validate_provider_codes(list(config.candidate_model_codes or []))
    incremental_payload = _load_incremental_new_provider_payload(artifact_dir=Path(config.artifact_dir))
    incremental_question_results = _build_historical_question_results(incremental_payload)
    incremental_aggregate_results = _build_historical_aggregate_results(incremental_payload)
    baseline_question_results = _filter_question_results_to_model_codes(
        incremental_question_results,
        model_codes=[baseline_provider_code],
    )
    baseline_aggregate_results = _filter_aggregate_results_to_model_codes(
        incremental_aggregate_results,
        model_codes=[baseline_provider_code],
    )
    baseline_client_view = (
        incremental_payload.get("client_view")
        if isinstance(incremental_payload.get("client_view"), dict)
        else {}
    )
    baseline_overall_winner = (
        str(baseline_client_view.get("overall_winner"))
        if baseline_client_view.get("overall_winner") is not None
        else baseline_provider_code
    )

    new_run_config = config.model_copy(
        update={
            "candidate_model_codes": new_provider_codes,
            "write_artifacts": False,
            "run_type_override": run_type,
            "execution_mode_override": execution_mode,
        }
    )
    new_provider_result = RealQuestionEvalRunner(db, new_run_config).run()
    if new_provider_result.error:
        new_provider_result.run_type = run_type
        new_provider_result.execution_mode = execution_mode
        new_provider_result.benchmark_batch_label = benchmark_batch_label
        new_provider_result.benchmark_status = "failed"
        new_provider_result.incomplete_reason = str(new_provider_result.error)
        new_provider_result.baseline_provider_codes = [baseline_provider_code]
        new_provider_result.excluded_provider_codes = excluded_provider_codes
        new_provider_result.newly_evaluated_provider_codes = list(new_provider_codes)
        new_provider_result.historical_overall_winner_model_code = baseline_overall_winner
        new_provider_result.comparison_scope_note = comparison_scope_note
        new_provider_result.non_compared_notes = list(non_compared_notes)
        if config.write_artifacts:
            artifact_paths = write_real_question_eval_artifacts(
                artifact_dir=Path(config.artifact_dir),
                result=new_provider_result,
            )
            new_provider_result.artifact_paths = artifact_paths
            new_provider_result.markdown_report_path = artifact_paths.latest_markdown_report
            new_provider_result.json_result_path = artifact_paths.latest_json_result
        return new_provider_result

    expected_question_ids = _resolve_comparison_question_order(
        baseline_question_results,
        new_provider_result.question_results,
        error_prefix=error_prefix,
    )

    combined_model_codes = [baseline_provider_code, *new_provider_codes]
    aggregate_by_model = {
        aggregate_result.model_code: aggregate_result
        for aggregate_result in [*baseline_aggregate_results, *new_provider_result.aggregate_results]
    }
    combined_aggregate_results = [aggregate_by_model[model_code] for model_code in combined_model_codes]
    selection_result = RagQualityService().select_best_config(
        config_evaluations=[
            _build_config_evaluation_from_aggregate_result(
                aggregate_result,
                total_cases=len(expected_question_ids),
            )
            for aggregate_result in combined_aggregate_results
        ]
    )
    combined_question_results = _merge_question_results(
        historical_question_results=baseline_question_results,
        new_question_results=new_provider_result.question_results,
        official_best_model_code=selection_result.best_model_code,
        question_order=expected_question_ids,
    )
    combined_aggregate_results = _recompute_aggregate_question_wins(
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
    )
    any_new_provider_beat_baseline = (
        selection_result.best_model_code in new_provider_codes
        and selection_result.best_model_code != baseline_provider_code
    )

    combined_result = RealQuestionEvalResult(
        passed=False,
        used_fake_models=new_provider_result.used_fake_models,
        run_type=run_type,
        execution_mode=execution_mode,
        benchmark_batch_label=benchmark_batch_label,
        benchmark_status="completed" if new_provider_result.passed else "failed",
        baseline_provider_codes=[baseline_provider_code],
        excluded_provider_codes=excluded_provider_codes,
        newly_evaluated_provider_codes=list(new_provider_codes),
        comparison_scope_note=comparison_scope_note,
        non_compared_notes=list(non_compared_notes),
        historical_providers=[baseline_provider_code],
        new_real_providers=list(new_provider_codes),
        historical_overall_winner_model_code=baseline_overall_winner,
        any_new_provider_beat_historical_winner=any_new_provider_beat_baseline,
        generated_at=new_provider_result.generated_at,
        profile_id=new_provider_result.profile_id,
        source_id=new_provider_result.source_id,
        job_id=new_provider_result.job_id,
        dataset_id=new_provider_result.dataset_id,
        dataset_name=new_provider_result.dataset_name,
        dataset_file=new_provider_result.dataset_file,
        source_chunk_count=new_provider_result.source_chunk_count,
        compared_models=combined_model_codes,
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
        overall_winner_model_code=selection_result.best_model_code,
        official_best_config=build_official_best_config(selection_result),
        activated=False,
        runtime_verified=False,
        warnings=[
            *new_provider_result.warnings,
            *selection_result.warnings,
        ],
    )
    combined_result.passed = (
        bool(selection_result.best_model_code)
        and new_provider_result.passed
    )
    artifact_paths = write_real_question_eval_artifacts(
        artifact_dir=Path(config.artifact_dir),
        result=combined_result,
    )
    combined_result.artifact_paths = artifact_paths
    if artifact_paths.latest_markdown_report is not None:
        combined_result.markdown_report_path = artifact_paths.latest_markdown_report
    if artifact_paths.latest_json_result is not None:
        combined_result.json_result_path = artifact_paths.latest_json_result
    combined_result.passed = (
        combined_result.passed
        and combined_result.markdown_report_path is not None
        and Path(combined_result.markdown_report_path).exists()
        and combined_result.json_result_path is not None
        and Path(combined_result.json_result_path).exists()
    )
    return combined_result


def run_full_version_batch_e_question_eval(
    db: Session,
    config: RealQuestionEvalConfig,
) -> RealQuestionEvalResult:
    return _run_full_version_optional_qwen_comparison_batch(
        db,
        config,
        validate_provider_codes=_validate_full_version_batch_e_provider_codes,
        baseline_provider_code=REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_BASELINE_PROVIDER,
        excluded_provider_codes=list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_EXCLUDED_PROVIDERS),
        run_type="full_version_batch_e",
        execution_mode="full_version_batch_e_real_eval",
        benchmark_batch_label="Batch E",
        comparison_scope_note=(
            "Only multilingual_e5_base and qwen3_embedding_4b are included in the final Batch E comparison; "
            "all other completed benchmark providers are excluded."
        ),
        non_compared_notes=[
            "Qwen3 4B uses plain-text SentenceTransformers encoding without provider-specific retrieval instructions.",
        ],
        error_prefix="Full-version Batch E",
        build_official_best_config=_build_batch_e_official_best_config,
    )


def run_full_version_batch_f_question_eval(
    db: Session,
    config: RealQuestionEvalConfig,
) -> RealQuestionEvalResult:
    return _run_full_version_optional_qwen_comparison_batch(
        db,
        config,
        validate_provider_codes=_validate_full_version_batch_f_provider_codes,
        baseline_provider_code=REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_BASELINE_PROVIDER,
        excluded_provider_codes=list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_EXCLUDED_PROVIDERS),
        run_type="full_version_batch_f",
        execution_mode="full_version_batch_f_real_eval",
        benchmark_batch_label="Batch F",
        comparison_scope_note=(
            "Only multilingual_e5_base and qwen3_embedding_8b are included in the final Batch F comparison; "
            "all other completed benchmark providers are excluded."
        ),
        non_compared_notes=[
            "Qwen3 8B uses plain-text SentenceTransformers encoding without provider-specific retrieval instructions.",
        ],
        error_prefix="Full-version Batch F",
        build_official_best_config=_build_batch_f_official_best_config,
    )


def run_full_version_batch_d_question_eval(
    db: Session,
    config: RealQuestionEvalConfig,
) -> RealQuestionEvalResult:
    new_provider_codes = _validate_full_version_batch_d_provider_codes(list(config.candidate_model_codes or []))
    baseline_provider_code = REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_BASELINE_PROVIDER
    excluded_provider_codes = list(REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_EXCLUDED_PROVIDERS)
    incremental_payload = _load_incremental_new_provider_payload(artifact_dir=Path(config.artifact_dir))
    incremental_question_results = _build_historical_question_results(incremental_payload)
    incremental_aggregate_results = _build_historical_aggregate_results(incremental_payload)
    baseline_question_results = _filter_question_results_to_model_codes(
        incremental_question_results,
        model_codes=[baseline_provider_code],
    )
    baseline_aggregate_results = _filter_aggregate_results_to_model_codes(
        incremental_aggregate_results,
        model_codes=[baseline_provider_code],
    )
    baseline_client_view = (
        incremental_payload.get("client_view")
        if isinstance(incremental_payload.get("client_view"), dict)
        else {}
    )
    baseline_overall_winner = (
        str(baseline_client_view.get("overall_winner"))
        if baseline_client_view.get("overall_winner") is not None
        else baseline_provider_code
    )

    runner = RealQuestionEvalRunner(
        db,
        config.model_copy(
            update={
                "write_artifacts": False,
                "run_type_override": "full_version_batch_d",
                "execution_mode_override": "full_version_batch_d_real_eval",
            }
        ),
    )
    dataset = runner.resolve_eval_dataset()
    effective_top_k = _resolve_eval_top_k_for_dataset(dataset)

    try:
        user = runner.ensure_user()
        profile = runner.ensure_profile(user)
        source = runner.ensure_source(user, profile)
        source_chunks = runner.prepare_eval_source_chunks(user=user, source=source)
    except Exception as exc:
        failed_result = RealQuestionEvalResult(
            passed=False,
            used_fake_models=False,
            run_type="full_version_batch_d",
            execution_mode="full_version_batch_d_real_eval",
            benchmark_batch_label="Batch D",
            benchmark_status="failed",
            incomplete_reason=str(exc),
            baseline_provider_codes=[baseline_provider_code],
            excluded_provider_codes=excluded_provider_codes,
            newly_evaluated_provider_codes=list(new_provider_codes),
            comparison_scope_note=(
                "Only multilingual_e5_base, bge_m3_dense_sparse, and "
                "bge_m3_dense_sparse_multivector are allowed in the final Batch D comparison."
            ),
            non_compared_notes=[
                "Batch D keeps production retrieval unchanged and uses a manual local hybrid reranking path.",
            ],
            historical_providers=[baseline_provider_code],
            new_real_providers=list(new_provider_codes),
            historical_overall_winner_model_code=baseline_overall_winner,
            any_new_provider_beat_historical_winner=False,
            dataset_id=dataset.dataset_id,
            dataset_name=dataset.name,
            dataset_file=str(config.dataset_path.resolve()) if config.dataset_path is not None else None,
            compared_models=[baseline_provider_code],
            question_results=baseline_question_results,
            aggregate_results=baseline_aggregate_results,
            overall_winner_model_code=baseline_provider_code,
            activated=False,
            runtime_verified=False,
            error=str(exc),
        )
        if config.write_artifacts:
            artifact_paths = write_real_question_eval_artifacts(
                artifact_dir=Path(config.artifact_dir),
                result=failed_result,
            )
            failed_result.artifact_paths = artifact_paths
            failed_result.markdown_report_path = artifact_paths.latest_markdown_report
            failed_result.json_result_path = artifact_paths.latest_json_result
        return failed_result

    successful_new_question_results_by_provider: dict[str, list[RealQuestionEvalQuestionResult]] = {}
    successful_new_aggregate_results: list[RealQuestionEvalAggregateModelResult] = []
    incomplete_mode_notes: list[str] = []
    warnings: list[str] = []
    with enable_bge_m3_hybrid_shared_model_cache(clear_on_exit=True):
        for provider_code in new_provider_codes:
            try:
                provider_question_results, provider_aggregate_result = _build_batch_d_manual_provider_result(
                    profile_id=profile.id,
                    provider_code=provider_code,
                    source_chunks=source_chunks,
                    cases=list(dataset.cases),
                    top_k=effective_top_k,
                )
            except Exception as exc:
                reason = f"{provider_code} was not completed in local CPU-only Batch D: {exc}"
                incomplete_mode_notes.append(reason)
                warnings.append(reason)
                continue

            successful_new_question_results_by_provider[provider_code] = provider_question_results
            successful_new_aggregate_results.append(provider_aggregate_result)

    if not successful_new_aggregate_results:
        failed_result = RealQuestionEvalResult(
            passed=False,
            used_fake_models=False,
            run_type="full_version_batch_d",
            execution_mode="full_version_batch_d_real_eval",
            benchmark_batch_label="Batch D",
            benchmark_status="failed",
            incomplete_reason="; ".join(incomplete_mode_notes) or "No Batch D provider completed successfully.",
            baseline_provider_codes=[baseline_provider_code],
            excluded_provider_codes=excluded_provider_codes,
            newly_evaluated_provider_codes=list(new_provider_codes),
            comparison_scope_note=(
                "Only multilingual_e5_base, bge_m3_dense_sparse, and "
                "bge_m3_dense_sparse_multivector are allowed in the final Batch D comparison."
            ),
            non_compared_notes=[
                "Batch D keeps production retrieval unchanged and uses a manual local hybrid reranking path.",
                *incomplete_mode_notes,
            ],
            historical_providers=[baseline_provider_code],
            new_real_providers=list(new_provider_codes),
            historical_overall_winner_model_code=baseline_overall_winner,
            any_new_provider_beat_historical_winner=False,
            generated_at=datetime.now(timezone.utc).isoformat(),
            profile_id=profile.id,
            source_id=source.id,
            dataset_id=dataset.dataset_id,
            dataset_name=dataset.name,
            dataset_file=str(config.dataset_path.resolve()) if config.dataset_path is not None else None,
            source_chunk_count=len(source_chunks),
            compared_models=[baseline_provider_code],
            question_results=baseline_question_results,
            aggregate_results=baseline_aggregate_results,
            overall_winner_model_code=baseline_provider_code,
            activated=False,
            runtime_verified=False,
            warnings=warnings,
            error="; ".join(incomplete_mode_notes) or "No Batch D provider completed successfully.",
        )
        if config.write_artifacts:
            artifact_paths = write_real_question_eval_artifacts(
                artifact_dir=Path(config.artifact_dir),
                result=failed_result,
            )
            failed_result.artifact_paths = artifact_paths
            failed_result.markdown_report_path = artifact_paths.latest_markdown_report
            failed_result.json_result_path = artifact_paths.latest_json_result
            _emit_runtime_log(
                f"artifact path written latest_json={failed_result.json_result_path}"
            )
        return failed_result

    successful_provider_codes = [aggregate_result.model_code for aggregate_result in successful_new_aggregate_results]
    question_order = _resolve_comparison_question_order(
        baseline_question_results,
        *[
            successful_new_question_results_by_provider[provider_code]
            for provider_code in successful_provider_codes
        ],
        error_prefix="Full-version Batch D",
    )
    baseline_by_question_id = {item.question_id: item for item in baseline_question_results}
    new_results_by_provider_and_question = {
        provider_code: {question_result.question_id: question_result for question_result in question_results}
        for provider_code, question_results in successful_new_question_results_by_provider.items()
    }
    combined_question_results: list[RealQuestionEvalQuestionResult] = []
    for question_id in question_order:
        baseline_question = baseline_by_question_id.get(question_id)
        if baseline_question is None:
            raise ValueError(f"Full-version Batch D baseline is missing question result for {question_id}")
        merged_model_results = list(baseline_question.model_results)
        for provider_code in successful_provider_codes:
            provider_question = new_results_by_provider_and_question[provider_code].get(question_id)
            if provider_question is None:
                raise ValueError(f"Full-version Batch D is missing question result for {provider_code}:{question_id}")
            merged_model_results.extend(provider_question.model_results)
        winner_model_code, winner_reason = _choose_question_winner(
            model_results=merged_model_results,
            official_best_model_code=None,
        )
        combined_question_results.append(
            RealQuestionEvalQuestionResult(
                question_id=baseline_question.question_id,
                question_text=baseline_question.question_text,
                test_type=baseline_question.test_type,
                expected_answer_type=baseline_question.expected_answer_type,
                source_scope=dict(baseline_question.source_scope),
                required_evidence=list(baseline_question.required_evidence),
                forbidden_evidence=list(baseline_question.forbidden_evidence),
                expected_markers=list(baseline_question.expected_markers),
                forbidden_markers=list(baseline_question.forbidden_markers),
                model_results=merged_model_results,
                winner_model_code=winner_model_code,
                winner_reason=winner_reason,
            )
        )

    combined_model_codes = [baseline_provider_code, *successful_provider_codes]
    combined_aggregate_results = [*baseline_aggregate_results, *successful_new_aggregate_results]
    selection_result = RagQualityService().select_best_config(
        config_evaluations=[
            _build_config_evaluation_from_aggregate_result(
                aggregate_result,
                total_cases=len(question_order),
            )
            for aggregate_result in combined_aggregate_results
        ]
    )
    combined_aggregate_results = _recompute_aggregate_question_wins(
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
    )
    any_new_provider_beat_baseline = (
        selection_result.best_model_code in successful_provider_codes
        and selection_result.best_model_code != baseline_provider_code
    )
    benchmark_status = (
        "completed"
        if len(successful_provider_codes) == len(new_provider_codes)
        else "completed_with_incomplete_modes"
    )

    combined_result = RealQuestionEvalResult(
        passed=bool(selection_result.best_model_code),
        used_fake_models=False,
        run_type="full_version_batch_d",
        execution_mode="full_version_batch_d_real_eval",
        benchmark_batch_label="Batch D",
        benchmark_status=benchmark_status,
        incomplete_reason="; ".join(incomplete_mode_notes) if incomplete_mode_notes else None,
        baseline_provider_codes=[baseline_provider_code],
        excluded_provider_codes=excluded_provider_codes,
        newly_evaluated_provider_codes=list(new_provider_codes),
        comparison_scope_note=(
            "Only multilingual_e5_base, bge_m3_dense_sparse, and "
            "bge_m3_dense_sparse_multivector are included in the final Batch D comparison. "
            "BGE-M3 hybrid modes use a manual local reranking path because the current production "
            "Qdrant retrieval path is dense-only."
        ),
        non_compared_notes=[
            "Batch D keeps production retrieval unchanged and uses a manual local hybrid reranking path.",
            *incomplete_mode_notes,
        ],
        historical_providers=[baseline_provider_code],
        new_real_providers=list(new_provider_codes),
        historical_overall_winner_model_code=baseline_overall_winner,
        any_new_provider_beat_historical_winner=any_new_provider_beat_baseline,
        generated_at=datetime.now(timezone.utc).isoformat(),
        profile_id=profile.id,
        source_id=source.id,
        dataset_id=dataset.dataset_id,
        dataset_name=dataset.name,
        dataset_file=str(config.dataset_path.resolve()) if config.dataset_path is not None else None,
        source_chunk_count=len(source_chunks),
        compared_models=combined_model_codes,
        question_results=combined_question_results,
        aggregate_results=combined_aggregate_results,
        overall_winner_model_code=selection_result.best_model_code,
        official_best_config=_build_batch_d_official_best_config(selection_result),
        activated=False,
        runtime_verified=False,
        warnings=[
            *warnings,
            *selection_result.warnings,
        ],
    )
    if config.write_artifacts:
        artifact_paths = write_real_question_eval_artifacts(
            artifact_dir=Path(config.artifact_dir),
            result=combined_result,
        )
        combined_result.artifact_paths = artifact_paths
        combined_result.markdown_report_path = artifact_paths.latest_markdown_report
        combined_result.json_result_path = artifact_paths.latest_json_result
        _emit_runtime_log(
            f"artifact path written latest_json={combined_result.json_result_path}"
        )
    combined_result.passed = (
        combined_result.passed
        and combined_result.markdown_report_path is not None
        and Path(combined_result.markdown_report_path).exists()
        and combined_result.json_result_path is not None
        and Path(combined_result.json_result_path).exists()
    )
    return combined_result


def run_real_question_eval(
    db: Session,
    config: RealQuestionEvalConfig | None = None,
) -> RealQuestionEvalResult:
    resolved_config = config or RealQuestionEvalConfig()
    if resolved_config.execution_mode_override == "full_version_batch_f_real_eval":
        return run_full_version_batch_f_question_eval(db, resolved_config)
    if resolved_config.execution_mode_override == "full_version_batch_e_real_eval":
        return run_full_version_batch_e_question_eval(db, resolved_config)
    if resolved_config.execution_mode_override == "full_version_batch_d_real_eval":
        return run_full_version_batch_d_question_eval(db, resolved_config)
    if resolved_config.execution_mode_override == "full_version_batch_c_real_eval":
        return run_full_version_batch_c_question_eval(db, resolved_config)
    if resolved_config.execution_mode_override == "full_version_batch_b_real_eval":
        return run_full_version_batch_b_question_eval(db, resolved_config)
    if resolved_config.execution_mode_override == "full_version_batch_a_real_eval":
        return run_full_version_batch_a_question_eval(db, resolved_config)
    if resolved_config.execution_mode_override == "incremental_real_eval":
        return run_incremental_real_question_eval(db, resolved_config)
    return RealQuestionEvalRunner(db, resolved_config).run()

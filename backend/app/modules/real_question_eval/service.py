from __future__ import annotations

import json
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
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
from app.modules.embeddings.providers.sentence_transformers import (
    BGE_M3_MODEL_NAME,
    E5_BASE_MODEL_NAME,
    E5_SMALL_MODEL_NAME,
    PARAPHRASE_MULTILINGUAL_MPNET_BASE_V2_MODEL_NAME,
)
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.memory_profiles.repository import list_memory_profiles_for_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.multi_embedding_eval.schemas import MultiEmbeddingEvalRequest
from app.modules.multi_embedding_eval.service import WORKFLOW_NAME, process_multi_embedding_eval_job
from app.modules.rag_chunks.service import list_rag_chunks
from app.modules.rag_quality.schemas import (
    RagQualityAggregateMetrics,
    RagQualityConfigEvaluation,
    RagQualityEvalCase,
)
from app.modules.rag_quality.service import RagQualityService
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag, retrieve_profile_rag_for_collection
from app.modules.rag_sources.repository import list_rag_sources_for_profile
from app.modules.rag_sources.schemas import RagSourceCreate, RagSourceUpdate
from app.modules.rag_sources.service import create_rag_source, update_rag_source
from app.modules.real_question_eval.report import write_real_question_eval_artifacts
from app.modules.real_question_eval.schemas import (
    RealQuestionEvalAggregateModelResult,
    RealQuestionEvalArtifactPaths,
    RealQuestionEvalConfig,
    RealQuestionEvalModelResult,
    RealQuestionEvalQuestionResult,
    RealQuestionEvalResult,
    RealQuestionEvalRetrievedChunk,
)
from app.modules.users.repository import get_user_by_email


REAL_QUESTION_EVAL_EMAIL = "demo.real.question.eval@example.test"
REAL_QUESTION_EVAL_PASSWORD = "RealQuestionEvalPass123"
REAL_QUESTION_EVAL_PROFILE_NAME = "Demo Real Question Eval Profile"
REAL_QUESTION_EVAL_SOURCE_TITLE = "Real Question Evaluation Source"
REAL_QUESTION_EVAL_SOURCE_KEY = "real_question_eval_v1"
REAL_QUESTION_EVAL_DATASET_ID = "real-question-eval-dataset"
REAL_QUESTION_EVAL_DATASET_NAME = "Real Question Evaluation Dataset"
REAL_QUESTION_EVAL_MODELS = (DEFAULT_EMBEDDING_MODEL_CODE, "bge_m3")
REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS = ("multilingual_e5_small", "bge_m3")
REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES = (
    "paraphrase_multilingual_mpnet_base_v2",
    "multilingual_e5_base",
)
REAL_QUESTION_EVAL_TOP_K = 2


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
    return [
        RagQualityEvalCase(
            case_id="question-sunflower-house",
            title="Village house flower evidence",
            query="What details show which flower was kept at the old village house and what part of the entrance is mentioned?",
            expected_markers=["sunflower seeds", "blue gate latch"],
            forbidden_markers=["rose market poster"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=2,
        ),
        RagQualityEvalCase(
            case_id="question-winter-trip",
            title="Winter trip travel evidence",
            query="During the winter trip, what travel item was saved and what container kept everyone warm?",
            expected_markers=["overnight train ticket", "wooden thermos"],
            forbidden_markers=["summer bus timetable"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=2,
        ),
        RagQualityEvalCase(
            case_id="question-grandmother-soup",
            title="Grandmother soup evidence",
            query="Which ingredients and cooking setup explain why grandmother's soup tasted smoky?",
            expected_markers=["dried mushrooms", "oak stove"],
            forbidden_markers=["vanilla jam"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=2,
        ),
    ]


class _QuestionEvalFakeSentenceTransformer:
    def __init__(self, model_name: str, *, device: str = "cpu", cache_folder: str | None = None):
        self.model_name = model_name
        self.device = device
        self.cache_folder = cache_folder

    def encode(self, texts, **kwargs):
        return [_build_fake_vector(str(text), self.model_name) for text in list(texts)]


def _build_fake_vector(text: str, model_name: str) -> list[float]:
    normalized_text = " ".join(text.lower().split())
    if model_name == E5_SMALL_MODEL_NAME:
        dimension = 384
    elif model_name in {E5_BASE_MODEL_NAME, PARAPHRASE_MULTILINGUAL_MPNET_BASE_V2_MODEL_NAME}:
        dimension = 768
    elif model_name == BGE_M3_MODEL_NAME:
        dimension = 1024
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

    return vector


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


class RealQuestionEvalRunner:
    def __init__(self, db: Session, config: RealQuestionEvalConfig | None = None) -> None:
        self.db = db
        self.config = config or RealQuestionEvalConfig(artifact_dir=BACKEND_DIR / "artifacts" / "real_question_eval")
        self.rag_quality_service = RagQualityService()

    @contextmanager
    def _embedding_runtime(self):
        from app.modules.embeddings.providers import sentence_transformers as sentence_transformers_provider

        original_embedding_provider = settings.embedding_provider
        original_import_module = sentence_transformers_provider.import_module
        settings.embedding_provider = "sentence_transformers"
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
        try:
            with self._embedding_runtime():
                user = self.ensure_user()
                profile = self.ensure_profile(user)
                source = self.ensure_source(user, profile)
                request_payload = self.build_request()
                background_job = self.create_job(
                    user,
                    profile_id=profile.id,
                    source_id=source.id,
                    payload=request_payload,
                )
                process_result = process_multi_embedding_eval_job(self.db, job_id=background_job.id)
                official_metrics_by_model = _extract_official_metrics_by_model(process_result.get("result_payload") or {})
                question_results, aggregate_results = self.collect_question_results(
                    user=user,
                    profile_id=profile.id,
                    request_payload=request_payload,
                    official_best_model_code=_extract_official_best_model_code(process_result.get("result_payload") or {}),
                    official_metrics_by_model=official_metrics_by_model,
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
                runtime_verified = (
                    runtime_config.model_code == activated_config.model_code
                    and runtime_config.collection_name == activated_config.collection_name
                    and runtime_retrieval.model_code == activated_config.model_code
                    and runtime_retrieval_payload.get("qdrant_collection") == activated_config.collection_name
                )

                result = RealQuestionEvalResult(
                    passed=False,
                    used_fake_models=not self.config.use_real_local_models,
                    run_type=_resolve_configured_run_type(self.config),
                    execution_mode=_resolve_configured_execution_mode(self.config),
                    generated_at=str((process_result.get("result_payload") or {}).get("completed_at") or datetime.now(timezone.utc).isoformat()),
                    profile_id=profile.id,
                    source_id=source.id,
                    job_id=background_job.id,
                    dataset_id=request_payload.dataset.dataset_id,
                    dataset_name=request_payload.dataset.name,
                    source_chunk_count=source_chunk_count,
                    compared_models=[candidate.model_code for candidate in request_payload.candidates],
                    question_results=question_results,
                    aggregate_results=aggregate_results,
                    overall_winner_model_code=_extract_official_best_model_code(process_result.get("result_payload") or {}),
                    official_best_config=(process_result.get("result_payload") or {}).get("best_config"),
                    activated=True,
                    runtime_verified=runtime_verified,
                    activated_config=_serialize_active_config(runtime_config),
                    runtime_retrieval=runtime_retrieval_payload,
                    warnings=_extract_warning_messages(process_result.get("result_payload") or {}),
                )
                result.passed = self._is_run_successful_without_artifacts(result)
                if self.config.write_artifacts:
                    artifact_paths = write_real_question_eval_artifacts(
                        artifact_dir=Path(self.config.artifact_dir),
                        result=result,
                    )
                    result.artifact_paths = artifact_paths
                    result.passed = self._is_run_successful(result)
                    if result.artifact_paths.latest_markdown_report is not None:
                        result.markdown_report_path = result.artifact_paths.latest_markdown_report
                    if result.artifact_paths.latest_json_result is not None:
                        result.json_result_path = result.artifact_paths.latest_json_result
                    result.passed = self._is_run_successful(result)
                return result
        except Exception as exc:
            return RealQuestionEvalResult(
                passed=False,
                used_fake_models=not self.config.use_real_local_models,
                run_type=_resolve_configured_run_type(self.config),
                execution_mode=_resolve_configured_execution_mode(self.config),
                error=f"{exc.__class__.__name__}: {exc}",
            )

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
        metadata = {
            "real_question_eval_key": REAL_QUESTION_EVAL_SOURCE_KEY,
            "safe_fictional_data": True,
        }
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
                    raw_text=REAL_QUESTION_EVAL_SOURCE_TEXT,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )
        elif source.raw_text != REAL_QUESTION_EVAL_SOURCE_TEXT or source.source_metadata != metadata:
            source = update_rag_source(
                self.db,
                current_user=user,
                source_id=source.id,
                payload=RagSourceUpdate(
                    title=REAL_QUESTION_EVAL_SOURCE_TITLE,
                    raw_text=REAL_QUESTION_EVAL_SOURCE_TEXT,
                    source_type="manual_text",
                    language="en",
                    source_metadata=metadata,
                ),
            )

        return source

    def build_request(self) -> MultiEmbeddingEvalRequest:
        collection_prefix = settings.qdrant_collection_name
        candidate_model_codes = list(self.config.candidate_model_codes or REAL_QUESTION_EVAL_MODELS)
        return MultiEmbeddingEvalRequest(
            dataset={
                "dataset_id": REAL_QUESTION_EVAL_DATASET_ID,
                "name": REAL_QUESTION_EVAL_DATASET_NAME,
                "cases": [case.model_dump(mode="json") for case in _build_question_cases()],
            },
            candidates=[
                {
                    "config_id": model_code,
                    "model_code": model_code,
                    "collection_name": f"{collection_prefix}__{model_code}__real_question_eval",
                    "top_k": REAL_QUESTION_EVAL_TOP_K,
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
    ) -> tuple[list[RealQuestionEvalQuestionResult], list[RealQuestionEvalAggregateModelResult]]:
        question_results: list[RealQuestionEvalQuestionResult] = []
        aggregate_trackers: dict[str, list[RealQuestionEvalModelResult]] = {candidate.model_code: [] for candidate in request_payload.candidates}
        collections_by_model = {
            candidate.model_code: candidate.collection_name for candidate in request_payload.candidates
        }
        wins_by_model = {candidate.model_code: 0 for candidate in request_payload.candidates}

        for case in request_payload.dataset.cases:
            model_results: list[RealQuestionEvalModelResult] = []
            for candidate in request_payload.candidates:
                retrieval_response = retrieve_profile_rag_for_collection(
                    self.db,
                    current_user=user,
                    profile_id=profile_id,
                    payload=RagRetrievalRequest(
                        query=case.query,
                        model_code=candidate.model_code,
                        limit=candidate.top_k,
                        score_threshold=candidate.score_threshold,
                    ),
                    collection_name=candidate.collection_name,
                )
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
                    expected_markers=list(case.expected_markers),
                    forbidden_markers=list(case.forbidden_markers),
                    model_results=model_results,
                    winner_model_code=winner_model_code,
                    winner_reason=winner_reason,
                )
            )

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

    def _is_run_successful_without_artifacts(self, result: RealQuestionEvalResult) -> bool:
        expected_question_count = len(_build_question_cases())
        expected_model_count = len(result.compared_models)
        return (
            len(result.question_results) >= expected_question_count
            and expected_model_count > 0
            and all(len(question_result.model_results) == expected_model_count for question_result in result.question_results)
            and all(question_result.winner_model_code is not None for question_result in result.question_results)
            and len({aggregate_result.collection_name for aggregate_result in result.aggregate_results}) == expected_model_count
            and result.overall_winner_model_code is not None
            and result.activated
            and result.runtime_verified
            and result.activated_config is not None
            and result.runtime_retrieval is not None
        )

    def _is_run_successful(self, result: RealQuestionEvalResult) -> bool:
        return (
            self._is_run_successful_without_artifacts(result)
            and result.markdown_report_path is not None
            and Path(result.markdown_report_path).exists()
            and result.json_result_path is not None
            and Path(result.json_result_path).exists()
        )


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
                score=result.score,
                preview=_build_chunk_preview(result.text),
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


def _build_historical_model_result(model_payload: dict[str, object]) -> RealQuestionEvalModelResult:
    top_chunks = [
        RealQuestionEvalRetrievedChunk(
            rank=int(chunk["rank"]),
            chunk_id=int(chunk["chunk_id"]),
            score=float(chunk["score"]),
            preview=str(chunk["preview"]),
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
        used_fake_models=bool(payload.get("used_fake_models")),
        run_type=str(payload.get("run_type") or "") or None,
        execution_mode=str(payload.get("execution_mode") or "") or None,
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
) -> list[RealQuestionEvalQuestionResult]:
    question_order = [case.case_id for case in _build_question_cases()]
    historical_by_id = {item.question_id: item for item in historical_question_results}
    new_by_id = {item.question_id: item for item in new_question_results}
    merged_results: list[RealQuestionEvalQuestionResult] = []

    for question_id in question_order:
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
                expected_markers=list(historical_question.expected_markers),
                forbidden_markers=list(historical_question.forbidden_markers),
                model_results=model_results,
                winner_model_code=winner_model_code,
                winner_reason=winner_reason,
            )
        )

    return merged_results


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

    expected_question_ids = [case.case_id for case in _build_question_cases()]
    historical_question_ids = [item.question_id for item in historical_question_results]
    new_question_ids = [item.question_id for item in new_provider_result.question_results]
    if historical_question_ids != expected_question_ids or new_question_ids != expected_question_ids:
        raise ValueError("Incremental real evaluation question IDs changed unexpectedly")

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
        and historical_question_ids == expected_question_ids
        and new_question_ids == expected_question_ids
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


def run_real_question_eval(
    db: Session,
    config: RealQuestionEvalConfig | None = None,
) -> RealQuestionEvalResult:
    resolved_config = config or RealQuestionEvalConfig()
    if resolved_config.execution_mode_override == "incremental_real_eval":
        return run_incremental_real_question_eval(db, resolved_config)
    return RealQuestionEvalRunner(db, resolved_config).run()

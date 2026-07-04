from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_logger, log_event
from app.db.models import ActiveRetrievalConfig, User
from app.modules.active_retrieval_config import repository
from app.modules.active_retrieval_config.exceptions import (
    ActiveRetrievalConfigActivationError,
    ActiveRetrievalConfigJobNotFoundError,
    ActiveRetrievalConfigNotFoundError,
    ActiveRetrievalConfigProfileNotFoundError,
)
from app.modules.active_retrieval_config.schemas import ActiveRetrievalConfigUpsertRequest
from app.modules.embedding_models.exceptions import EmbeddingModelNotFoundError
from app.modules.embedding_models.registry import (
    BGE_M3_DENSE_SPARSE_MULTIVECTOR_RETRIEVAL_MODE,
    BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE,
)
from app.modules.embedding_models.service import is_embedding_model_runtime_available
from app.modules.memory_profiles.service import MemoryProfileNotFoundError, get_memory_profile
from app.modules.rag_retrieval.hybrid import is_bge_m3_dense_sparse_model
from app.modules.multi_embedding_eval.schemas import MultiEmbeddingEvalRequest
from app.modules.rag_sources.service import RagSourceNotFoundError, get_rag_source


MULTI_EMBEDDING_EVAL_WORKFLOW = "multi_embedding_eval"
PRODUCTION_ACTIVE_RETRIEVAL_MODEL_CODE = "bge_m3_dense_sparse"
PRODUCTION_ACTIVE_RETRIEVAL_MODE = BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE
PRODUCTION_FALLBACK_RETRIEVAL_MODEL_CODE = "multilingual_e5_base"
PRODUCTION_FALLBACK_RETRIEVAL_MODE = "dense"
PRODUCTION_DEFAULT_TOP_K = 5

logger = get_logger("active_retrieval_config")


@dataclass(frozen=True)
class RuntimeActiveRetrievalSelection:
    model_code: str
    collection_name: str
    top_k: int
    score_threshold: float | None
    retrieval_mode: str
    selection_reason: str
    source: str
    source_eval_job_id: int | None = None
    source_eval_dataset_id: str | None = None


def _build_collection_name(model_code: str) -> str:
    return f"{settings.qdrant_collection_name}__{model_code}"


def get_production_recommended_active_retrieval_config() -> RuntimeActiveRetrievalSelection:
    return RuntimeActiveRetrievalSelection(
        model_code=PRODUCTION_ACTIVE_RETRIEVAL_MODEL_CODE,
        collection_name=_build_collection_name(PRODUCTION_ACTIVE_RETRIEVAL_MODEL_CODE),
        top_k=PRODUCTION_DEFAULT_TOP_K,
        score_threshold=None,
        retrieval_mode=PRODUCTION_ACTIVE_RETRIEVAL_MODE,
        selection_reason=(
            "Promoted from Task 49 Batch D as the current production retrieval recommendation."
        ),
        source="production_recommendation",
    )


def _build_runtime_selection_from_active_config(
    active_config: ActiveRetrievalConfig,
) -> RuntimeActiveRetrievalSelection:
    return RuntimeActiveRetrievalSelection(
        model_code=active_config.model_code,
        collection_name=active_config.collection_name,
        top_k=active_config.top_k,
        score_threshold=active_config.score_threshold,
        retrieval_mode=active_config.retrieval_mode,
        selection_reason=active_config.selection_reason or "Profile-specific active retrieval config.",
        source="profile_active_config",
        source_eval_job_id=active_config.source_eval_job_id,
        source_eval_dataset_id=active_config.source_eval_dataset_id,
    )


def _build_fallback_runtime_selection(
    candidate: RuntimeActiveRetrievalSelection,
    *,
    reason: str,
) -> RuntimeActiveRetrievalSelection:
    return RuntimeActiveRetrievalSelection(
        model_code=PRODUCTION_FALLBACK_RETRIEVAL_MODEL_CODE,
        collection_name=_build_collection_name(PRODUCTION_FALLBACK_RETRIEVAL_MODEL_CODE),
        top_k=candidate.top_k,
        score_threshold=candidate.score_threshold,
        retrieval_mode=PRODUCTION_FALLBACK_RETRIEVAL_MODE,
        selection_reason=(
            f"Fell back from {candidate.model_code} to {PRODUCTION_FALLBACK_RETRIEVAL_MODEL_CODE}: {reason}"
        ),
        source="guarded_fallback",
        source_eval_job_id=candidate.source_eval_job_id,
        source_eval_dataset_id=candidate.source_eval_dataset_id,
    )


def _get_runtime_rejection_reason(candidate: RuntimeActiveRetrievalSelection) -> str | None:
    if candidate.retrieval_mode == BGE_M3_DENSE_SPARSE_MULTIVECTOR_RETRIEVAL_MODE:
        return (
            "BGE-M3 multivector retrieval stays benchmark-only and is not enabled as a "
            "production runtime default."
        )
    if is_bge_m3_dense_sparse_model(candidate.model_code) and candidate.retrieval_mode not in (
        None,
        "",
        BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE,
    ):
        return (
            f"Configured retrieval mode `{candidate.retrieval_mode}` is not supported for "
            f"`{candidate.model_code}`."
        )

    try:
        runtime_available = is_embedding_model_runtime_available(candidate.model_code)
    except EmbeddingModelNotFoundError:
        return f"Configured retrieval model `{candidate.model_code}` is not registered."

    if not runtime_available:
        return f"Configured retrieval model `{candidate.model_code}` is not available in this runtime."

    return None


def resolve_runtime_active_retrieval_config(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> RuntimeActiveRetrievalSelection:
    stored_active_config = repository.get_active_config_for_profile(
        db,
        owner_user_id=current_user.id,
        profile_id=profile_id,
    )
    candidate = (
        _build_runtime_selection_from_active_config(stored_active_config)
        if stored_active_config is not None
        else get_production_recommended_active_retrieval_config()
    )
    rejection_reason = _get_runtime_rejection_reason(candidate)
    if rejection_reason is None or candidate.model_code == PRODUCTION_FALLBACK_RETRIEVAL_MODEL_CODE:
        return candidate

    fallback = _build_fallback_runtime_selection(candidate, reason=rejection_reason)
    log_event(
        logger,
        logging.WARNING,
        "active_retrieval_config_runtime_fallback",
        owner_user_id=current_user.id,
        profile_id=profile_id,
        configured_model_code=candidate.model_code,
        configured_retrieval_mode=candidate.retrieval_mode,
        fallback_model_code=fallback.model_code,
        fallback_retrieval_mode=fallback.retrieval_mode,
        reason=rejection_reason,
        source=candidate.source,
    )
    return fallback


def _get_owned_profile_or_raise(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
):
    try:
        return get_memory_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except MemoryProfileNotFoundError as exc:
        raise ActiveRetrievalConfigProfileNotFoundError("Memory profile not found") from exc


def _build_selection_reason(
    *,
    job_id: int,
    dataset_id: str,
    best_config_id: str,
) -> str:
    return (
        f"Activated best config from multi-embedding evaluation job {job_id} "
        f"for dataset {dataset_id} using candidate {best_config_id}."
    )


def _upsert_active_config(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
    payload: ActiveRetrievalConfigUpsertRequest,
) -> ActiveRetrievalConfig:
    active_config = repository.get_active_config_for_profile(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
    )
    selected_at = datetime.now(timezone.utc)

    if active_config is None:
        active_config = ActiveRetrievalConfig(
            owner_user_id=owner_user_id,
            profile_id=profile_id,
        )
        db.add(active_config)

    active_config.model_code = payload.model_code
    active_config.collection_name = payload.collection_name
    active_config.top_k = payload.top_k
    active_config.score_threshold = payload.score_threshold
    active_config.retrieval_mode = payload.retrieval_mode
    active_config.source_eval_job_id = payload.source_eval_job_id
    active_config.source_eval_dataset_id = payload.source_eval_dataset_id
    active_config.selected_metrics = payload.selected_metrics
    active_config.all_config_scores = payload.all_config_scores
    active_config.selection_reason = payload.selection_reason
    active_config.warnings = payload.warnings
    active_config.is_active = True
    active_config.selected_at = selected_at

    db.commit()
    db.refresh(active_config)
    return active_config


def resolve_active_retrieval_config(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> ActiveRetrievalConfig | None:
    return repository.get_active_config_for_profile(
        db,
        owner_user_id=current_user.id,
        profile_id=profile_id,
    )


def get_active_retrieval_config(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> ActiveRetrievalConfig:
    _get_owned_profile_or_raise(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    active_config = resolve_active_retrieval_config(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    if active_config is None:
        raise ActiveRetrievalConfigNotFoundError("Active retrieval config not found")

    return active_config


def upsert_active_retrieval_config(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: ActiveRetrievalConfigUpsertRequest,
) -> ActiveRetrievalConfig:
    _get_owned_profile_or_raise(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    return _upsert_active_config(
        db,
        owner_user_id=current_user.id,
        profile_id=profile_id,
        payload=payload,
    )


def activate_best_multi_embedding_eval_result(
    db: Session,
    *,
    current_user: User,
    source_id: int,
    job_id: int,
) -> ActiveRetrievalConfig:
    rag_source = get_rag_source(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    background_job = repository.get_background_job_for_owner(
        db,
        owner_user_id=current_user.id,
        job_id=job_id,
    )
    if background_job is None:
        raise ActiveRetrievalConfigJobNotFoundError("Background job not found")

    input_payload = background_job.input_payload or {}
    result_payload = background_job.result_payload or {}
    if (
        input_payload.get("workflow") != MULTI_EMBEDDING_EVAL_WORKFLOW
        or input_payload.get("source_id") != source_id
        or background_job.profile_id != rag_source.profile_id
    ):
        raise ActiveRetrievalConfigActivationError(
            "Background job is not a matching multi-embedding evaluation result"
        )
    if background_job.status != "succeeded":
        raise ActiveRetrievalConfigActivationError(
            "Multi-embedding evaluation result is not eligible for activation"
        )

    request_payload_raw = input_payload.get("request")
    if not isinstance(request_payload_raw, dict):
        raise ActiveRetrievalConfigActivationError(
            "Multi-embedding evaluation request payload is invalid"
        )

    best_config = result_payload.get("best_config")
    if not isinstance(best_config, dict):
        raise ActiveRetrievalConfigActivationError(
            "Multi-embedding evaluation did not produce a best config"
        )

    best_config_id = best_config.get("best_config_id")
    dataset_id = result_payload.get("dataset_id")
    if not isinstance(best_config_id, str) or not isinstance(dataset_id, str):
        raise ActiveRetrievalConfigActivationError(
            "Multi-embedding evaluation best config metadata is invalid"
        )

    request_payload = MultiEmbeddingEvalRequest.model_validate(request_payload_raw)
    selected_candidate = next(
        (
            candidate
            for candidate in request_payload.candidates
            if candidate.config_id == best_config_id
        ),
        None,
    )
    if selected_candidate is None:
        raise ActiveRetrievalConfigActivationError(
            "Winning candidate is missing from the evaluation request"
        )

    warnings = result_payload.get("warnings")
    all_config_scores = result_payload.get("all_config_scores")

    payload = ActiveRetrievalConfigUpsertRequest(
        model_code=selected_candidate.model_code,
        collection_name=selected_candidate.collection_name,
        top_k=selected_candidate.top_k,
        score_threshold=selected_candidate.score_threshold,
        retrieval_mode=selected_candidate.retrieval_mode,
        source_eval_job_id=background_job.id,
        source_eval_dataset_id=dataset_id,
        selected_metrics=best_config.get("selected_metrics"),
        all_config_scores=all_config_scores if isinstance(all_config_scores, list) else None,
        selection_reason=_build_selection_reason(
            job_id=background_job.id,
            dataset_id=dataset_id,
            best_config_id=best_config_id,
        ),
        warnings=warnings if isinstance(warnings, list) else None,
    )
    return _upsert_active_config(
        db,
        owner_user_id=current_user.id,
        profile_id=rag_source.profile_id,
        payload=payload,
    )

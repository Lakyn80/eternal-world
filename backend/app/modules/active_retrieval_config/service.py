from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models import ActiveRetrievalConfig, User
from app.modules.active_retrieval_config import repository
from app.modules.active_retrieval_config.exceptions import (
    ActiveRetrievalConfigActivationError,
    ActiveRetrievalConfigJobNotFoundError,
    ActiveRetrievalConfigNotFoundError,
    ActiveRetrievalConfigProfileNotFoundError,
)
from app.modules.active_retrieval_config.schemas import ActiveRetrievalConfigUpsertRequest
from app.modules.memory_profiles.service import MemoryProfileNotFoundError, get_memory_profile
from app.modules.multi_embedding_eval.schemas import MultiEmbeddingEvalRequest
from app.modules.rag_sources.service import RagSourceNotFoundError, get_rag_source


MULTI_EMBEDDING_EVAL_WORKFLOW = "multi_embedding_eval"


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

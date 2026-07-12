from __future__ import annotations

import logging as std_logging
from time import perf_counter
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, Request, status
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import observe_fa_chat_error, observe_fa_chat_success
from app.db.session import get_db
from app.modules.avatar_memory_promotions.schemas import (
    AvatarMemoryPromotionRead,
    build_avatar_memory_promotion_read,
)
from app.modules.avatar_memory_promotions.service import (
    AvatarMemoryPromotionInvalidTransitionError,
    AvatarMemoryPromotionNotFoundError,
)
from app.modules.avatar_memory_indexing.schemas import AvatarMemoryIndexingRead
from app.modules.avatar_memory_indexing.service import (
    AvatarMemoryIndexingConflictError,
    AvatarMemoryIndexingEligibilityError,
    AvatarMemoryIndexingExecutionError,
    AvatarMemoryIndexingNotFoundError,
)
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateListResponse,
    MemoryCandidateRead,
    MemoryCandidateReviewUpdate,
    build_memory_candidate_read,
)

from .schemas import (
    DemoFaChatErrorResponse,
    DemoFaChatMemoryCandidateReviewResponse,
    DemoFaChatMemoryPromotionListResponse,
    DemoFaChatMessageRequest,
    DemoFaChatMessageResponse,
)
from .service import (
    DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL,
    DemoFaChatInitializationError,
    DemoFaChatProfileUnavailableError,
    DemoFaChatValidationError,
    approve_demo_memory_candidate,
    archive_demo_memory_candidate,
    build_demo_memory_candidate_review_response,
    cancel_demo_memory_promotion,
    get_demo_memory_candidate,
    get_demo_memory_promotion,
    index_demo_memory_promotion,
    list_demo_memory_candidates,
    list_demo_memory_promotions,
    reject_demo_memory_candidate,
    run_demo_fa_chat_message,
)
from app.modules.conversation_memory_candidates.service import (
    ConversationMemoryCandidateInvalidTransitionError,
    ConversationMemoryCandidateNotFoundError,
)
from app.modules.family_memory_enrichment.service import (
    FamilyMemoryAuthorizationError,
    FamilyMemoryInvalidTransitionError,
    FamilyMemoryNotFoundError,
    validate_demo_actor,
)
from app.modules.family_memory_enrichment.enums import FamilyMemoryActorRole
from app.modules.family_memory_enrichment.schemas import DemoFamilyActorContext


router = APIRouter(prefix="/api/demo/fa-chat", tags=["demo-fa-chat"])
logger = get_logger("demo_fa_chat_router")
CandidateIdPath = Annotated[int, Path(gt=0)]

CANDIDATE_NOT_FOUND_DETAIL = "Кандидат воспоминания не найден."
CANDIDATE_INVALID_TRANSITION_DETAIL = "Недопустимое изменение статуса кандидата."
PROMOTION_NOT_FOUND_DETAIL = "Продвижение воспоминания не найдено."
PROMOTION_INVALID_TRANSITION_DETAIL = "Недопустимое изменение статуса продвижения."
PROMOTION_INDEXING_FAILED_DETAIL = "Индексация подтвержденного воспоминания не выполнена."


def _optional_actor_context(
    *,
    actor_id: str | None,
    actor_role: FamilyMemoryActorRole | None,
    relationship_to_owner: str | None,
) -> DemoFamilyActorContext | None:
    if actor_id is None and actor_role is None and relationship_to_owner is None:
        return None
    if actor_id is None or actor_role is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="actor_id and actor_role must be provided together",
        )
    actor = DemoFamilyActorContext(
        actor_id=actor_id,
        actor_role=actor_role,
        relationship_to_owner=relationship_to_owner,
    )
    try:
        validate_demo_actor(actor)
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Указанный контекст участника семьи недопустим.",
        ) from exc
    return actor


@router.post(
    "/message",
    response_model=DemoFaChatMessageResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": DemoFaChatErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": DemoFaChatErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": DemoFaChatErrorResponse},
    },
)
def send_demo_fa_chat_message(
    payload: DemoFaChatMessageRequest,
    request: Request,
    db: Session = Depends(get_db),
) -> DemoFaChatMessageResponse:
    trace_id = getattr(request.state, "request_id", None) or "unknown"
    started_at = perf_counter()
    debug_enabled = bool(payload.debug)
    try:
        response = run_demo_fa_chat_message(
            db,
            profile_id=payload.profile_id,
            message=payload.message,
            debug=debug_enabled,
            trace_id=trace_id,
            active_memory_candidate_id=payload.active_memory_candidate_id,
            actor_id=payload.actor_id,
            actor_role=payload.actor_role.value if payload.actor_role is not None else None,
            relationship_to_owner=payload.relationship_to_owner,
        )
        observe_fa_chat_success(
            duration_seconds=perf_counter() - started_at,
            retrieval_used=response.retrieval_used,
            guard_applied=response.guard_applied,
            guard_reason=response.guard_reason,
            lack_of_evidence=response.lack_of_evidence,
            debug=debug_enabled,
        )
        return response
    except DemoFaChatValidationError as exc:
        observe_fa_chat_error(
            outcome="validation_error",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except DemoFaChatProfileUnavailableError as exc:
        observe_fa_chat_error(
            outcome="profile_unavailable",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except DemoFaChatInitializationError as exc:
        observe_fa_chat_error(
            outcome="not_initialized",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Участник семьи не имеет права выполнять это действие.",
        ) from exc
    except FamilyMemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Кандидат семейного воспоминания не найден.",
        ) from exc
    except FamilyMemoryInvalidTransitionError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Для кандидата нет ожидающего уточняющего вопроса.",
        ) from exc
    except HTTPException:
        raise
    except Exception as exc:
        observe_fa_chat_error(
            outcome="internal_error",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        log_event(
            logger,
            std_logging.ERROR,
            "fa_demo_chat_failed",
            trace_id=trace_id,
            profile_id=payload.profile_id,
            error_type=exc.__class__.__name__,
            error_summary=str(exc)[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL,
        ) from exc


@router.get(
    "/memory-candidates",
    response_model=MemoryCandidateListResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def list_demo_memory_candidates_endpoint(
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    db: Session = Depends(get_db),
) -> MemoryCandidateListResponse:
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
        )
        candidates = list_demo_memory_candidates(
            db,
            profile_id=profile_id,
            actor=actor,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    items = [build_memory_candidate_read(candidate) for candidate in candidates]
    return MemoryCandidateListResponse(items=items, total=len(items))


@router.get(
    "/memory-candidates/{candidate_id}",
    response_model=MemoryCandidateRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def get_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    db: Session = Depends(get_db),
) -> MemoryCandidateRead:
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
        )
        candidate = get_demo_memory_candidate(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
            actor=actor,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ConversationMemoryCandidateNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_candidate_not_found",
            profile_id=profile_id,
            candidate_id=candidate_id,
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=CANDIDATE_NOT_FOUND_DETAIL,
        ) from exc
    except FamilyMemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=CANDIDATE_NOT_FOUND_DETAIL,
        ) from exc

    return build_memory_candidate_read(candidate)


def _review_demo_memory_candidate(
    *,
    db: Session,
    profile_id: int | None,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None,
    action: str,
 ) -> MemoryCandidateRead | DemoFaChatMemoryCandidateReviewResponse:
    action_map = {
        "approve": approve_demo_memory_candidate,
        "reject": reject_demo_memory_candidate,
        "archive": archive_demo_memory_candidate,
    }
    handler = action_map[action]
    try:
        candidate = handler(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
            payload=payload,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ConversationMemoryCandidateNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_candidate_not_found",
            profile_id=profile_id,
            candidate_id=candidate_id,
            action=action,
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=CANDIDATE_NOT_FOUND_DETAIL,
        ) from exc
    except ConversationMemoryCandidateInvalidTransitionError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_candidate_invalid_transition",
            profile_id=profile_id,
            candidate_id=candidate_id,
            action=action,
            error_type=exc.__class__.__name__,
            error_summary=str(exc)[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=CANDIDATE_INVALID_TRANSITION_DETAIL,
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Для обогащённого воспоминания требуется явная проверка владельцем.",
        ) from exc

    if action == "approve":
        return build_demo_memory_candidate_review_response(candidate)
    return build_memory_candidate_read(candidate)


@router.post(
    "/memory-candidates/{candidate_id}/approve",
    response_model=DemoFaChatMemoryCandidateReviewResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def approve_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    payload: MemoryCandidateReviewUpdate | None = None,
    profile_id: int | None = None,
    db: Session = Depends(get_db),
) -> DemoFaChatMemoryCandidateReviewResponse:
    return _review_demo_memory_candidate(
        db=db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        payload=payload,
        action="approve",
    )


@router.get(
    "/memory-promotions",
    response_model=DemoFaChatMemoryPromotionListResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def list_demo_memory_promotions_endpoint(
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    db: Session = Depends(get_db),
) -> DemoFaChatMemoryPromotionListResponse:
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
        )
        promotions = list_demo_memory_promotions(
            db,
            profile_id=profile_id,
            actor=actor,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    items = [build_avatar_memory_promotion_read(promotion) for promotion in promotions]
    return DemoFaChatMemoryPromotionListResponse(items=items, total=len(items))


@router.get(
    "/memory-promotions/{promotion_id}",
    response_model=AvatarMemoryPromotionRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def get_demo_memory_promotion_endpoint(
    promotion_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    db: Session = Depends(get_db),
) -> AvatarMemoryPromotionRead:
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
        )
        promotion = get_demo_memory_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion_id,
            actor=actor,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except AvatarMemoryPromotionNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_not_found",
            profile_id=profile_id,
            promotion_id=promotion_id,
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROMOTION_NOT_FOUND_DETAIL,
        ) from exc
    except FamilyMemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROMOTION_NOT_FOUND_DETAIL,
        ) from exc

    return build_avatar_memory_promotion_read(promotion)


@router.post(
    "/memory-promotions/{promotion_id}/cancel",
    response_model=AvatarMemoryPromotionRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def cancel_demo_memory_promotion_endpoint(
    promotion_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    db: Session = Depends(get_db),
) -> AvatarMemoryPromotionRead:
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
        )
        promotion = cancel_demo_memory_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion_id,
            actor=actor,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except AvatarMemoryPromotionNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_not_found",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="cancel",
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROMOTION_NOT_FOUND_DETAIL,
        ) from exc
    except AvatarMemoryPromotionInvalidTransitionError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_invalid_transition",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="cancel",
            error_type=exc.__class__.__name__,
            error_summary=str(exc)[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=PROMOTION_INVALID_TRANSITION_DETAIL,
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Только владелец аватара может отменить продвижение воспоминания.",
        ) from exc

    return build_avatar_memory_promotion_read(promotion)


@router.post(
    "/memory-promotions/{promotion_id}/index",
    response_model=AvatarMemoryIndexingRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": DemoFaChatErrorResponse},
    },
)
def index_demo_memory_promotion_endpoint(
    promotion_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    db: Session = Depends(get_db),
) -> AvatarMemoryIndexingRead:
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
        )
        return index_demo_memory_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion_id,
            actor=actor,
        )
    except (AvatarMemoryPromotionNotFoundError, AvatarMemoryIndexingNotFoundError) as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_not_found",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="index",
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROMOTION_NOT_FOUND_DETAIL,
        ) from exc
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except (AvatarMemoryIndexingEligibilityError, AvatarMemoryIndexingConflictError) as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_index_rejected",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="index",
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=PROMOTION_INVALID_TRANSITION_DETAIL,
        ) from exc
    except AvatarMemoryIndexingExecutionError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=PROMOTION_INDEXING_FAILED_DETAIL,
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Только владелец аватара может индексировать воспоминание.",
        ) from exc


@router.post(
    "/memory-candidates/{candidate_id}/reject",
    response_model=MemoryCandidateRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def reject_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    payload: MemoryCandidateReviewUpdate | None = None,
    profile_id: int | None = None,
    db: Session = Depends(get_db),
) -> MemoryCandidateRead:
    return _review_demo_memory_candidate(
        db=db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        payload=payload,
        action="reject",
    )


@router.post(
    "/memory-candidates/{candidate_id}/archive",
    response_model=MemoryCandidateRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def archive_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    payload: MemoryCandidateReviewUpdate | None = None,
    profile_id: int | None = None,
    db: Session = Depends(get_db),
) -> MemoryCandidateRead:
    return _review_demo_memory_candidate(
        db=db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        payload=payload,
        action="archive",
    )

from __future__ import annotations

import logging as std_logging
from time import perf_counter
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import observe_fa_chat_error, observe_fa_chat_success
from app.db.session import get_db
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateListResponse,
    MemoryCandidateRead,
    MemoryCandidateReviewUpdate,
    build_memory_candidate_read,
)

from .schemas import DemoFaChatErrorResponse, DemoFaChatMessageRequest, DemoFaChatMessageResponse
from .service import (
    DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL,
    DemoFaChatInitializationError,
    DemoFaChatProfileUnavailableError,
    DemoFaChatValidationError,
    approve_demo_memory_candidate,
    archive_demo_memory_candidate,
    get_demo_memory_candidate,
    list_demo_memory_candidates,
    reject_demo_memory_candidate,
    run_demo_fa_chat_message,
)
from app.modules.conversation_memory_candidates.service import (
    ConversationMemoryCandidateInvalidTransitionError,
    ConversationMemoryCandidateNotFoundError,
)


router = APIRouter(prefix="/api/demo/fa-chat", tags=["demo-fa-chat"])
logger = get_logger("demo_fa_chat_router")
CandidateIdPath = Annotated[int, Path(gt=0)]

CANDIDATE_NOT_FOUND_DETAIL = "Кандидат воспоминания не найден."
CANDIDATE_INVALID_TRANSITION_DETAIL = "Недопустимое изменение статуса кандидата."


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
    db: Session = Depends(get_db),
) -> MemoryCandidateListResponse:
    try:
        candidates = list_demo_memory_candidates(
            db,
            profile_id=profile_id,
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
    db: Session = Depends(get_db),
) -> MemoryCandidateRead:
    try:
        candidate = get_demo_memory_candidate(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
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

    return build_memory_candidate_read(candidate)


def _review_demo_memory_candidate(
    *,
    db: Session,
    profile_id: int | None,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None,
    action: str,
) -> MemoryCandidateRead:
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

    return build_memory_candidate_read(candidate)


@router.post(
    "/memory-candidates/{candidate_id}/approve",
    response_model=MemoryCandidateRead,
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
) -> MemoryCandidateRead:
    return _review_demo_memory_candidate(
        db=db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        payload=payload,
        action="approve",
    )


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

from __future__ import annotations

import logging as std_logging
from time import perf_counter

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import observe_fa_chat_error, observe_fa_chat_success
from app.db.session import get_db

from .schemas import DemoFaChatErrorResponse, DemoFaChatMessageRequest, DemoFaChatMessageResponse
from .service import (
    DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL,
    DemoFaChatInitializationError,
    DemoFaChatProfileUnavailableError,
    DemoFaChatValidationError,
    run_demo_fa_chat_message,
)


router = APIRouter(prefix="/api/demo/fa-chat", tags=["demo-fa-chat"])
logger = get_logger("demo_fa_chat_router")


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
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL,
        ) from exc

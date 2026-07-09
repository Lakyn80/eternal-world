from __future__ import annotations

import logging as std_logging

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
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
    try:
        return run_demo_fa_chat_message(
            db,
            profile_id=payload.profile_id,
            message=payload.message,
            debug=bool(payload.debug),
            trace_id=trace_id,
        )
    except DemoFaChatValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except DemoFaChatInitializationError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except HTTPException:
        raise
    except Exception as exc:
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

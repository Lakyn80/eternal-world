from __future__ import annotations

import logging as std_logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logging import REQUEST_ID_HEADER, get_logger, get_request_id, log_event
from app.modules.billing.exceptions import BillingLimitExceededError


logger = get_logger("errors")


async def handle_billing_limit_exceeded(
    request: Request,
    exc: BillingLimitExceededError,
) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None) or get_request_id()
    log_event(
        logger,
        std_logging.WARNING,
        "billing_limit_exceeded",
        method=request.method,
        path=request.url.path,
        status_code=403,
        error_code=exc.code,
    )

    headers = {}
    if request_id:
        headers[REQUEST_ID_HEADER] = request_id

    return JSONResponse(
        status_code=403,
        content={
            "detail": exc.detail,
            "error": exc.error,
            "code": exc.code,
        },
        headers=headers,
    )


async def handle_unexpected_exception(request: Request, exc: Exception) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None) or get_request_id()
    log_event(
        logger,
        std_logging.ERROR,
        "unhandled_exception",
        method=request.method,
        path=request.url.path,
        status_code=500,
        error_type=exc.__class__.__name__,
    )

    headers = {}
    if request_id:
        headers[REQUEST_ID_HEADER] = request_id

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "request_id": request_id,
        },
        headers=headers,
    )


def install_error_handlers(app: FastAPI) -> None:
    app.add_exception_handler(BillingLimitExceededError, handle_billing_limit_exceeded)
    app.add_exception_handler(Exception, handle_unexpected_exception)

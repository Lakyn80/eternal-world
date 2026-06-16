from __future__ import annotations

import logging as std_logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logging import REQUEST_ID_HEADER, get_logger, get_request_id, log_event


logger = get_logger("errors")


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
    app.add_exception_handler(Exception, handle_unexpected_exception)

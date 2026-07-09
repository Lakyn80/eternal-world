from __future__ import annotations

import logging as std_logging
import re
import time
from uuid import uuid4

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.errors import handle_unexpected_exception
from app.core.logging import (
    REQUEST_ID_HEADER,
    clear_request_id,
    get_logger,
    log_event,
    set_request_id,
)
from app.core.metrics import observe_http_request


SAFE_REQUEST_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,63}$")
logger = get_logger("middleware")


def resolve_request_id(request_id: str | None) -> str:
    if request_id is None:
        return str(uuid4())

    normalized_request_id = request_id.strip()
    if SAFE_REQUEST_ID_PATTERN.fullmatch(normalized_request_id):
        return normalized_request_id

    return str(uuid4())


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.perf_counter()
        request_id = resolve_request_id(request.headers.get(REQUEST_ID_HEADER))
        request.state.request_id = request_id
        context_token = set_request_id(request_id)

        log_event(
            logger,
            std_logging.INFO,
            "request_started",
            method=request.method,
            path=request.url.path,
        )

        try:
            response = await call_next(request)
        except Exception as exc:
            response = await handle_unexpected_exception(request, exc)

        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
        route = getattr(request.scope.get("route"), "path", None)
        response.headers[REQUEST_ID_HEADER] = request_id
        observe_http_request(
            method=request.method,
            route=route,
            status_code=response.status_code,
            duration_seconds=duration_ms / 1000,
        )

        log_event(
            logger,
            std_logging.INFO,
            "request_completed",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=duration_ms,
        )

        clear_request_id(context_token)
        return response


def install_middleware(app: FastAPI) -> None:
    app.add_middleware(RequestContextMiddleware)

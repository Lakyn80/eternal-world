from __future__ import annotations

import json
import logging as std_logging
from contextvars import ContextVar, Token
from datetime import datetime, timezone
from typing import Any


REQUEST_ID_HEADER = "X-Request-ID"
REDACTED_VALUE = "[REDACTED]"
SENSITIVE_EXACT_KEYS = {
    "password",
    "access_token",
    "authorization",
    "secret",
    "api_key",
}
LOGGER_NAME = "eternal_world"
_request_id_context: ContextVar[str | None] = ContextVar("request_id", default=None)


def _is_sensitive_key(key: str) -> bool:
    normalized_key = key.strip().lower()
    return (
        normalized_key in SENSITIVE_EXACT_KEYS
        or normalized_key.endswith("_password")
        or normalized_key.endswith("_secret")
        or normalized_key.endswith("_api_key")
        or normalized_key.endswith("_access_token")
        or normalized_key.startswith("authorization")
    )


def sanitize_log_data(data: Any) -> Any:
    if isinstance(data, dict):
        sanitized: dict[str, Any] = {}
        for key, value in data.items():
            normalized_key = str(key)
            if _is_sensitive_key(normalized_key):
                sanitized[normalized_key] = REDACTED_VALUE
            else:
                sanitized[normalized_key] = sanitize_log_data(value)
        return sanitized

    if isinstance(data, list):
        return [sanitize_log_data(item) for item in data]

    if isinstance(data, tuple):
        return [sanitize_log_data(item) for item in data]

    return data


def set_request_id(request_id: str) -> Token[str | None]:
    return _request_id_context.set(request_id)


def get_request_id() -> str | None:
    return _request_id_context.get()


def clear_request_id(token: Token[str | None]) -> None:
    _request_id_context.reset(token)


class RequestContextFilter(std_logging.Filter):
    def filter(self, record: std_logging.LogRecord) -> bool:
        if not hasattr(record, "request_id") or record.request_id is None:
            record.request_id = get_request_id()
        return True


class JsonFormatter(std_logging.Formatter):
    def format(self, record: std_logging.LogRecord) -> str:
        payload = {
            "timestamp": datetime.fromtimestamp(
                record.created,
                tz=timezone.utc,
            ).isoformat(),
            "level": record.levelname,
            "event": getattr(record, "event", record.getMessage() or record.name),
        }

        request_id = getattr(record, "request_id", None)
        if request_id:
            payload["request_id"] = request_id

        extra_fields = sanitize_log_data(getattr(record, "payload", {}))
        if isinstance(extra_fields, dict):
            payload.update(extra_fields)

        return json.dumps(payload, default=str)


def configure_logging(level: int = std_logging.INFO) -> None:
    logger = std_logging.getLogger(LOGGER_NAME)
    if getattr(logger, "_eternal_world_configured", False):
        return

    logger.setLevel(level)
    logger.propagate = False
    logger.handlers.clear()

    handler = std_logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    handler.addFilter(RequestContextFilter())
    logger.addHandler(handler)

    logger._eternal_world_configured = True


def get_logger(name: str) -> std_logging.Logger:
    return std_logging.getLogger(f"{LOGGER_NAME}.{name}")


def log_event(
    logger: std_logging.Logger,
    level: int,
    event: str,
    **fields: Any,
) -> None:
    logger.log(
        level,
        event,
        extra={
            "event": event,
            "payload": sanitize_log_data(fields),
        },
    )

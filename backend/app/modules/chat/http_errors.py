"""HTTP mapping for chat admission / provider overload (Task 65.13.11)."""

from __future__ import annotations

from fastapi import HTTPException, status

from app.core.metrics import observe_chat_operation
from app.modules.chat.admission import (
    ChatAdmissionRateLimitedError,
    ChatAdmissionSaturatedError,
    ChatAdmissionUnavailableError,
    ChatAdmissionUserBusyError,
    ChatProviderUnavailableError,
)

CHAT_ADMISSION_HTTP_ERRORS = (
    ChatAdmissionRateLimitedError,
    ChatAdmissionUserBusyError,
    ChatAdmissionSaturatedError,
    ChatAdmissionUnavailableError,
    ChatProviderUnavailableError,
)


def raise_chat_admission_http(exc: BaseException) -> None:
    """Raise the matching HTTPException for admission/provider overload errors.

    Callers must only pass known admission/provider overload exceptions.
    """

    if isinstance(exc, (ChatAdmissionRateLimitedError, ChatAdmissionUserBusyError)):
        observe_chat_operation(operation="send", result="rate_limited")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=str(exc),
            headers={"Retry-After": str(exc.retry_after_seconds)},
        ) from exc
    if isinstance(exc, ChatAdmissionSaturatedError):
        observe_chat_operation(operation="send", result="saturated")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
            headers={"Retry-After": str(exc.retry_after_seconds)},
        ) from exc
    if isinstance(exc, ChatAdmissionUnavailableError):
        observe_chat_operation(operation="send", result="admission_unavailable")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
            headers={"Retry-After": str(exc.retry_after_seconds)},
        ) from exc
    if isinstance(exc, ChatProviderUnavailableError):
        observe_chat_operation(operation="send", result="provider_unavailable")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
            headers={"Retry-After": str(exc.retry_after_seconds)},
        ) from exc
    raise TypeError(f"Unsupported chat admission error type: {type(exc)!r}")

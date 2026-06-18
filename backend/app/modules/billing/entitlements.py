from __future__ import annotations

from dataclasses import dataclass

from app.modules.billing.exceptions import BillingLimitExceededError


@dataclass(frozen=True)
class UsageLimitCheckResult:
    is_allowed: bool
    current_usage: int
    limit: int | None
    error: str | None = None
    code: str | None = None
    detail: str | None = None


def check_usage_limit(
    *,
    current_usage: int,
    limit: int | None,
    error: str,
    code: str,
    detail: str,
) -> UsageLimitCheckResult:
    if current_usage < 0:
        raise ValueError("current_usage must be non-negative")

    if limit is None:
        return UsageLimitCheckResult(
            is_allowed=True,
            current_usage=current_usage,
            limit=None,
        )

    is_allowed = current_usage < limit
    if is_allowed:
        return UsageLimitCheckResult(
            is_allowed=True,
            current_usage=current_usage,
            limit=limit,
        )

    return UsageLimitCheckResult(
        is_allowed=False,
        current_usage=current_usage,
        limit=limit,
        error=error,
        code=code,
        detail=detail,
    )


def enforce_usage_limit(
    *,
    current_usage: int,
    limit: int | None,
    error: str,
    code: str,
    detail: str,
) -> UsageLimitCheckResult:
    result = check_usage_limit(
        current_usage=current_usage,
        limit=limit,
        error=error,
        code=code,
        detail=detail,
    )
    if not result.is_allowed:
        raise BillingLimitExceededError(
            detail=result.detail or detail,
            code=result.code or code,
            error=result.error or error,
        )

    return result

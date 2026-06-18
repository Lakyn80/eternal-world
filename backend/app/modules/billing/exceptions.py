from __future__ import annotations


class BillingLimitExceededError(Exception):
    def __init__(
        self,
        *,
        detail: str,
        code: str,
        error: str = "limit_exceeded",
    ) -> None:
        super().__init__(detail)
        self.detail = detail
        self.code = code
        self.error = error

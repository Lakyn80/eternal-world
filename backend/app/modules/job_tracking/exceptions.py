class BackgroundJobNotFoundError(Exception):
    pass


class BackgroundJobProfileNotFoundError(Exception):
    pass


class PerUserActiveJobLimitExceededError(Exception):
    """Task 65.9 (Part Q) - the requesting user already has the maximum
    allowed number of active heavy (embedding) jobs. Maps to HTTP 429."""

    def __init__(self, *, limit: int, current: int) -> None:
        super().__init__(
            f"Active job limit exceeded for this account ({current}/{limit})"
        )
        self.limit = limit
        self.current = current


class PerProfileActiveJobLimitExceededError(Exception):
    """Task 65.9 (Part Q) - the target memorial/profile already has the
    maximum allowed number of active heavy (embedding) jobs. Maps to HTTP
    429."""

    def __init__(self, *, limit: int, current: int) -> None:
        super().__init__(
            f"Active job limit exceeded for this memorial ({current}/{limit})"
        )
        self.limit = limit
        self.current = current


class GlobalQueueSaturationError(Exception):
    """Task 65.9 (Part Q) - the global ceiling of active heavy jobs across
    the whole system has been reached. Maps to HTTP 503 with
    `Retry-After`."""

    def __init__(self, *, limit: int, current: int, retry_after_seconds: int) -> None:
        super().__init__(
            f"System is temporarily at capacity ({current}/{limit} active jobs)"
        )
        self.limit = limit
        self.current = current
        self.retry_after_seconds = retry_after_seconds

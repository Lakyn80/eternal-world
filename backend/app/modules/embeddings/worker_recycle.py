"""Safe embedding-worker recycling (Task 65.9, Part N).

Application code here never controls Docker directly - no socket mount,
no Docker API client, no `docker`/`systemctl`/`reboot` subprocess calls.
The only mechanism available is exiting *this* worker process; recovery
after that relies entirely on the container's own `restart: unless-
stopped` policy (configured in `docker-compose.yml`) recreating it - a
policy the host's container runtime enforces, not this code.

`trigger_worker_recycle` is gated behind
`settings.embedding_worker_self_recycle_enabled`, which must only be set
`true` on the dedicated embedding-worker container. It is a no-op
everywhere else (FastAPI, the general Celery worker, the maintenance
worker, and every test process) so a bug elsewhere can never cause an
unexpected process exit outside that one container.
"""

from __future__ import annotations

import logging
import os
from typing import Protocol

from app.core.config import settings
from app.core.logging import get_logger, log_event


logger = get_logger("embedding_worker_recycle")


class WorkerRecycleAction(Protocol):
    def __call__(self) -> None: ...


def _default_recycle_action() -> None:
    #: `os._exit` (never `sys.exit`/`raise SystemExit`) - must not be
    #: caught by Celery's own task/worker exception handling, and must not
    #: run Python `atexit`/`finally` cleanup that could re-acknowledge or
    #: otherwise interact with in-flight broker state. The job's own
    #: recovery state was already committed to PostgreSQL before this is
    #: called (Part O: "must not acknowledge unfinished work, interrupt an
    #: active database transaction").
    os._exit(1)


def trigger_worker_recycle(*, action: WorkerRecycleAction | None = None) -> bool:
    """Returns True if a recycle was actually triggered (or would have
    been, in a test-injected `action`), False if this process is not
    configured as a recyclable embedding worker (safe no-op)."""

    if not settings.embedding_worker_self_recycle_enabled:
        log_event(
            logger,
            logging.WARNING,
            "embedding_worker_recycle_skipped_not_enabled",
        )
        return False

    log_event(logger, logging.WARNING, "embedding_worker_recycle_triggered")
    (action or _default_recycle_action)()
    return True

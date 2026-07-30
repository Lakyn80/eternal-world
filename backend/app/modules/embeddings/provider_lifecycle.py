"""Explicit embedding provider lifecycle (Task 65.9, Part J).

Exactly one `EmbeddingProviderLifecycle` singleton exists per process
(module-level `_lifecycle`). It is the only place in this codebase that
should ever hold a live, initialized BGE-M3 model instance across more
than one call - avatar_memory_indexing/memorial_contribution_indexing/
biography_ingestion's `Default*EmbeddingEncoder` classes call through it
(via `app.modules.embeddings.self_healing`) instead of calling
`build_embedding_provider` fresh on every single embed.

This module must only ever be imported and actually initialized inside a
worker process (the dedicated embedding Celery worker, or - in this
repository's current topology - the general Celery worker while it still
also carries embedding-heavy tasks). FastAPI's HTTP process must never
call `get_or_initialize` - it is safe to *import* this module from
anywhere (no model is loaded at import time), only unsafe to *call*
`get_or_initialize` outside a worker.
"""

from __future__ import annotations

import gc
from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import Lock

from app.core.metrics import (
    observe_embedding_provider_initialization,
    observe_embedding_provider_probe_failure,
    observe_embedding_provider_reload,
    set_embedding_provider_health,
)
from app.modules.embeddings.provider_integrity import ProviderIntegrityError, run_provider_integrity_probe
from app.modules.embeddings.providers import build_embedding_provider
from app.modules.embeddings.providers.base import BaseEmbeddingProvider


class ProviderState:
    NEVER_INITIALIZED = "never_initialized"
    INITIALIZING = "initializing"
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    RECOVERY_IN_PROGRESS = "recovery_in_progress"
    FAILED = "failed"


@dataclass
class ProviderHealth:
    state: str = ProviderState.NEVER_INITIALIZED
    consecutive_probe_failures: int = 0
    last_successful_probe_at: datetime | None = None
    last_probe_error_reason: str | None = None


@dataclass
class _ProviderSlot:
    provider: BaseEmbeddingProvider | None = None
    health: ProviderHealth = field(default_factory=ProviderHealth)


class EmbeddingProviderLifecycle:
    """One instance of this class exists per worker process. All mutation
    is guarded by a single `Lock` so two Celery task threads (or, more
    realistically for this codebase's prefork pool, two calls racing in
    the same interpreter) can never both start initializing a second
    BGE-M3 instance concurrently (Part J: "Prevent concurrent
    initialization of multiple BGE-M3 instances in one worker process")."""

    def __init__(self) -> None:
        self._lock = Lock()
        self._slots: dict[str, _ProviderSlot] = {}

    def _slot(self, model_code: str) -> _ProviderSlot:
        slot = self._slots.get(model_code)
        if slot is None:
            slot = _ProviderSlot()
            self._slots[model_code] = slot
        return slot

    def get_health(self, *, model_code: str) -> ProviderHealth:
        return self._slot(model_code).health

    def get_or_initialize(self, *, model_code: str) -> BaseEmbeddingProvider:
        with self._lock:
            slot = self._slot(model_code)
            if slot.provider is not None and slot.health.state in (
                ProviderState.HEALTHY,
                ProviderState.DEGRADED,
            ):
                return slot.provider
            return self._initialize_locked(model_code=model_code, slot=slot)

    def _initialize_locked(self, *, model_code: str, slot: _ProviderSlot) -> BaseEmbeddingProvider:
        slot.health.state = ProviderState.INITIALIZING
        set_embedding_provider_health(model_code=model_code, state=ProviderState.INITIALIZING)
        provider = build_embedding_provider(model_code=model_code)
        try:
            run_provider_integrity_probe(provider, model_code=model_code)
        except ProviderIntegrityError as exc:
            slot.provider = None
            slot.health.state = ProviderState.FAILED
            slot.health.consecutive_probe_failures += 1
            slot.health.last_probe_error_reason = exc.reason_code
            observe_embedding_provider_probe_failure(model_code=model_code, reason=exc.reason_code)
            set_embedding_provider_health(model_code=model_code, state=ProviderState.FAILED)
            raise

        slot.provider = provider
        slot.health.state = ProviderState.HEALTHY
        slot.health.consecutive_probe_failures = 0
        slot.health.last_successful_probe_at = datetime.now(timezone.utc)
        slot.health.last_probe_error_reason = None
        observe_embedding_provider_initialization(model_code=model_code, result="success")
        set_embedding_provider_health(model_code=model_code, state=ProviderState.HEALTHY)
        return provider

    def invalidate(self, *, model_code: str) -> None:
        """Release the reference to a (suspected-corrupt) provider and
        run garbage collection so its underlying model tensors are freed
        before a replacement is loaded (Part J: "release provider
        references, clear provider-specific caches, perform garbage
        collection where appropriate")."""

        with self._lock:
            slot = self._slot(model_code)
            slot.provider = None
            slot.health.state = ProviderState.RECOVERY_IN_PROGRESS
            set_embedding_provider_health(model_code=model_code, state=ProviderState.RECOVERY_IN_PROGRESS)
        gc.collect()

    def reload(self, *, model_code: str) -> BaseEmbeddingProvider:
        self.invalidate(model_code=model_code)
        observe_embedding_provider_reload(model_code=model_code)
        return self.get_or_initialize(model_code=model_code)

    def reset_for_tests(self) -> None:
        with self._lock:
            self._slots.clear()


_lifecycle = EmbeddingProviderLifecycle()


def get_embedding_provider_lifecycle() -> EmbeddingProviderLifecycle:
    """Process-local singleton accessor. A brand-new interpreter process
    (a genuinely fresh embedding-worker process after a recycle) naturally
    gets a brand-new module-level `_lifecycle`, which is exactly the
    "fresh process" semantics Part M relies on - no explicit reset step is
    needed on real process restart, only in-process tests use
    `reset_for_tests()` to simulate one."""

    return _lifecycle

"""Bounded provider self-healing (Task 65.9, Part M).

Implements this exact semantic policy, and no more:

    Attempt 1: use the currently validated provider.
    -> corruption: invalidate, load a new provider, re-probe.
    Attempt 2: retry the *same job* on the new provider instance.
    -> corruption again: persist `fresh_process_retry_used`, persist
       `worker_recycle_requested`, requeue the same semantic job.
    Attempt 3: run once in a genuinely fresh embedding-worker process.
    -> corruption again: mark the job permanently failed, keep manual
       retry eligible, never request a second automatic recycle, never
       loop.

All counters live on the `BackgroundJob` row (`provider_recovery_count`,
`fresh_process_retry_used`, `worker_recycle_requested`), so they survive
worker restart, container restart, broker redelivery, and duplicate task
delivery - a second process picking up the same `job_id` reads the exact
same persisted state and continues the bound from where it left off,
never resetting the counter to zero.

This module is deliberately the *only* place that decides "is this
exception a provider-health issue" for the embedding call site: the three
`Default*EmbeddingEncoder.encode()` implementations only ever call
`provider.embed_passage(...)` here, never Qdrant or domain validation, so
this narrow call site's exceptions are always provider-health matters by
construction (Part L/M invariant: Qdrant failures and input-validation
failures never reach this code at all, because they happen in
surrounding code the encoder never touches).
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.metrics import observe_embedding_provider_recovery, observe_embedding_worker_recycle_request
from app.db.models import BackgroundJob
from app.modules.embeddings.provider_integrity import validate_embedding_output
from app.modules.embeddings.provider_lifecycle import EmbeddingProviderLifecycle, get_embedding_provider_lifecycle
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.job_tracking import service as job_tracking_service


class ProviderRecoveryExhaustedError(Exception):
    """Raised when the bounded self-healing policy above has been fully
    exhausted for this call. `requires_fresh_process` distinguishes the
    two possible outcomes for the caller (a Celery task):

    - `requires_fresh_process=True`: attempts 1+2 both failed in this
      process. The job has been persisted as `recovery_pending` with
      `fresh_process_retry_used`/`worker_recycle_requested` set; the
      caller must requeue the same job and safely recycle the embedding
      worker (Part N) - never raise this straight through as a normal
      task failure.
    - `requires_fresh_process=False`: this call *was* the one permitted
      fresh-process attempt (attempt 3) and it also failed, or there was
      no job context at all to persist recovery state against (e.g. a
      dev/eval script calling the encoder directly). The job is now
      permanently failed; manual retry remains available; no further
      automatic recycle may be requested.
    """

    def __init__(self, message: str, *, requires_fresh_process: bool) -> None:
        super().__init__(message)
        self.requires_fresh_process = requires_fresh_process


class SelfHealingEmbeddingEncoder:
    """Drop-in for the `encode(*, text, model_code) -> EmbeddingVector`
    protocol already used by `Default*EmbeddingEncoder` classes across
    `avatar_memory_indexing`, `memorial_contribution_indexing`, and
    `biography_ingestion`. Constructed by the Celery task with the current
    `job_id` so recovery counters land on the right row; constructed
    without a `job_id` (e.g. by a dev/eval script) it still runs the
    bounded 1-reload-retry policy in-process, but any exhaustion is always
    treated as a final failure (no job row to mark `recovery_pending`
    against, so there is nothing to safely resume later)."""

    def __init__(
        self,
        *,
        db: Session,
        job_id: int | None,
        lifecycle: EmbeddingProviderLifecycle | None = None,
    ) -> None:
        self._db = db
        self._job_id = job_id
        self._lifecycle = lifecycle or get_embedding_provider_lifecycle()

    def _load_job(self) -> BackgroundJob | None:
        if self._job_id is None:
            return None
        from app.modules.job_tracking import repository as job_tracking_repository

        return job_tracking_repository.get_background_job_by_id(self._db, job_id=self._job_id)

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        job = self._load_job()
        already_used_fresh_process = bool(job and job.fresh_process_retry_used)
        max_local_attempts = 1 if already_used_fresh_process else 2

        last_error: Exception | None = None
        for attempt in range(1, max_local_attempts + 1):
            try:
                provider = self._lifecycle.get_or_initialize(model_code=model_code)
                vector = provider.embed_passage(text, model_code)
                validate_embedding_output(vector)
            except Exception as exc:  # noqa: BLE001 - see module docstring: this call
                # site only ever talks to the embedding provider, so any
                # failure here is a provider-health matter by construction.
                last_error = exc
                if self._job_id is not None:
                    job_tracking_service.record_provider_recovery_attempt(self._db, job_id=self._job_id)
                self._lifecycle.invalidate(model_code=model_code)
                if attempt < max_local_attempts:
                    observe_embedding_provider_recovery(outcome="reloaded")
                    continue
                break
            else:
                return vector

        if self._job_id is not None and not already_used_fresh_process:
            requested = job_tracking_service.request_fresh_process_retry(self._db, job_id=self._job_id)
            if requested:
                observe_embedding_worker_recycle_request()
                observe_embedding_provider_recovery(outcome="fresh_process_requested")
            raise ProviderRecoveryExhaustedError(
                "Embedding provider recovery requires a fresh worker process",
                requires_fresh_process=True,
            ) from last_error

        if self._job_id is not None:
            job_tracking_service.record_permanent_provider_failure(self._db, job_id=self._job_id)
        observe_embedding_provider_recovery(outcome="permanent_failure")
        raise ProviderRecoveryExhaustedError(
            "Embedding provider recovery failed permanently after the bounded retry policy",
            requires_fresh_process=False,
        ) from last_error

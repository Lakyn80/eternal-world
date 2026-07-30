"""Idempotent reconciliation for approved candidates missing downstream
promotion/indexing state (Task 65.6.1, Part H).

Mirrors the existing `avatar_biographer.repair` shape exactly: a read-only
finder function plus a separate idempotent repair function, a structured
dataclass result, and `log_event` for every state transition actually made.
Never touches a candidate that is not `status == "approved"`; never creates
a second promotion for a candidate that already has one; never re-indexes
an already-`indexed` promotion; never cancels/rejects/archives anything.

This exists because approval, in general, only ever performs the cheap
DB-side promotion step and (if it succeeds) a best-effort Celery enqueue -
see `family_memory_enrichment.service._enqueue_promotion_indexing_safely`
and `memorial_access.service._promote_and_enqueue_indexing_safely`. Either
step can be legitimately incomplete for a candidate approved before this
task's fix existed (no promotion was ever created, because
`privacy_scope="private_owner"` used to be ineligible - see
`family_memory_enrichment.eligibility.INDEXABLE_PRIVACY_SCOPES`), or for a
candidate whose enqueue attempt failed transiently (e.g. the Celery broker
was briefly unreachable). This module completes exactly those two missing
steps, and only those two - it never invents a new lifecycle state.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.db.models import ConversationMemoryCandidate, MemoryProfile
from app.modules.avatar_memory_indexing import service as avatar_memory_indexing_service
from app.modules.avatar_memory_promotions import service as promotion_service
from app.modules.family_memory_enrichment.eligibility import get_promotion_block_reason

_logger = get_logger("avatar_memory_promotions")

#: Promotion states that already represent a complete, correctly-indexed
#: (or deliberately terminal) outcome - reconciliation must never touch
#: these. `cancelled` is intentionally left alone: it reflects an explicit
#: prior decision (see `avatar_memory_promotions.service.cancel_promotion`),
#: not a stuck state, and resurrecting it automatically would be a
#: destructive, non-idempotent surprise.
_COMPLETE_OR_TERMINAL_PROMOTION_STATUSES = frozenset({"indexed", "cancelled"})
_RETRYABLE_PROMOTION_STATUSES = frozenset({"pending_index", "failed"})


@dataclass(frozen=True)
class ReconciliationOutcome:
    candidate_id: int
    profile_id: int | None
    action: str  # "already_complete" | "promoted" | "indexing_enqueued" | "failed" | "skipped"
    promotion_id: int | None
    promotion_status: str | None
    detail: str | None = None


@dataclass(frozen=True)
class ReconciliationResult:
    scanned: int
    already_complete: int = 0
    promoted: int = 0
    indexing_enqueued: int = 0
    failed: int = 0
    skipped: int = 0
    outcomes: list[ReconciliationOutcome] = field(default_factory=list)


def find_approved_candidates_for_reconciliation(
    db: Session, *, profile_id: int | None = None
) -> list[ConversationMemoryCandidate]:
    """Read-only: every currently-approved candidate in scope. This is the
    full "scanned" set - it deliberately includes candidates that are
    already fully indexed (they will be reported as `already_complete`,
    never re-processed) so the returned counts always add up to the number
    of approved candidates actually examined."""

    statement = select(ConversationMemoryCandidate).where(
        ConversationMemoryCandidate.status == "approved",
    )
    if profile_id is not None:
        statement = statement.where(ConversationMemoryCandidate.profile_id == profile_id)
    statement = statement.order_by(ConversationMemoryCandidate.id.asc())
    return list(db.scalars(statement))


def _enqueue_indexing_or_record_failure(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
    promotion,
    trace_id: str | None,
) -> ReconciliationOutcome:
    profile = db.get(MemoryProfile, candidate.profile_id) if candidate.profile_id is not None else None
    if profile is None:
        return ReconciliationOutcome(
            candidate_id=candidate.id,
            profile_id=candidate.profile_id,
            action="skipped",
            promotion_id=promotion.id,
            promotion_status=promotion.promotion_status,
            detail="missing_profile",
        )
    try:
        avatar_memory_indexing_service.enqueue_indexing_job(db, profile=profile, promotion=promotion)
    except Exception as exc:  # noqa: BLE001 - reconciliation must keep scanning the rest of the batch
        log_event(
            _logger,
            logging.ERROR,
            "avatar_memory_promotion_reconciliation_enqueue_failed",
            trace_id=trace_id,
            candidate_id=candidate.id,
            profile_id=candidate.profile_id,
            promotion_id=promotion.id,
            error_type=exc.__class__.__name__,
        )
        return ReconciliationOutcome(
            candidate_id=candidate.id,
            profile_id=candidate.profile_id,
            action="failed",
            promotion_id=promotion.id,
            promotion_status=promotion.promotion_status,
            detail=f"enqueue_failed:{exc.__class__.__name__}",
        )
    log_event(
        _logger,
        logging.INFO,
        "avatar_memory_promotion_reconciliation_indexing_enqueued",
        trace_id=trace_id,
        candidate_id=candidate.id,
        profile_id=candidate.profile_id,
        promotion_id=promotion.id,
    )
    return ReconciliationOutcome(
        candidate_id=candidate.id,
        profile_id=candidate.profile_id,
        action="indexing_enqueued",
        promotion_id=promotion.id,
        promotion_status=promotion.promotion_status,
    )


def reconcile_candidate_promotions(
    db: Session,
    *,
    profile_id: int | None = None,
    dry_run: bool = False,
    trace_id: str | None = None,
) -> ReconciliationResult:
    """Idempotent: repeated calls converge to a no-op once every in-scope
    candidate is `indexed` (or `cancelled`, or ineligible). Never raises for
    a single candidate's failure - one bad candidate is recorded as
    `failed` and processing continues with the rest of the batch."""

    candidates = find_approved_candidates_for_reconciliation(db, profile_id=profile_id)
    outcomes: list[ReconciliationOutcome] = []
    already_complete = 0
    promoted = 0
    indexing_enqueued = 0
    failed = 0
    skipped = 0

    for candidate in candidates:
        existing_promotion = candidate.avatar_memory_promotion

        if existing_promotion is not None and existing_promotion.promotion_status in _COMPLETE_OR_TERMINAL_PROMOTION_STATUSES:
            already_complete += 1
            outcomes.append(
                ReconciliationOutcome(
                    candidate_id=candidate.id,
                    profile_id=candidate.profile_id,
                    action="already_complete",
                    promotion_id=existing_promotion.id,
                    promotion_status=existing_promotion.promotion_status,
                )
            )
            continue

        if existing_promotion is None:
            block_reason = get_promotion_block_reason(db, candidate=candidate)
            if block_reason is not None:
                skipped += 1
                outcomes.append(
                    ReconciliationOutcome(
                        candidate_id=candidate.id,
                        profile_id=candidate.profile_id,
                        action="skipped",
                        promotion_id=None,
                        promotion_status=None,
                        detail=f"ineligible:{block_reason}",
                    )
                )
                continue

            if dry_run:
                outcomes.append(
                    ReconciliationOutcome(
                        candidate_id=candidate.id,
                        profile_id=candidate.profile_id,
                        action="promoted",
                        promotion_id=None,
                        promotion_status=None,
                        detail="dry_run",
                    )
                )
                promoted += 1
                continue

            try:
                outcome = promotion_service.create_or_get_promotion_for_candidate(db, candidate=candidate)
                db.commit()
                db.refresh(candidate)
                db.refresh(outcome.promotion)
            except Exception as exc:  # noqa: BLE001 - see docstring
                db.rollback()
                failed += 1
                log_event(
                    _logger,
                    logging.ERROR,
                    "avatar_memory_promotion_reconciliation_promote_failed",
                    trace_id=trace_id,
                    candidate_id=candidate.id,
                    profile_id=candidate.profile_id,
                    error_type=exc.__class__.__name__,
                )
                outcomes.append(
                    ReconciliationOutcome(
                        candidate_id=candidate.id,
                        profile_id=candidate.profile_id,
                        action="failed",
                        promotion_id=None,
                        promotion_status=None,
                        detail=f"promote_failed:{exc.__class__.__name__}",
                    )
                )
                continue

            promoted += 1
            existing_promotion = outcome.promotion
            log_event(
                _logger,
                logging.INFO,
                "avatar_memory_promotion_reconciliation_promoted",
                trace_id=trace_id,
                candidate_id=candidate.id,
                profile_id=candidate.profile_id,
                promotion_id=existing_promotion.id,
            )

        if existing_promotion.promotion_status not in _RETRYABLE_PROMOTION_STATUSES:
            # Freshly created promotions always start `pending_index`; this
            # branch only guards against an unexpected/unknown status
            # value reaching here without a code change to this module.
            already_complete += 1
            outcomes.append(
                ReconciliationOutcome(
                    candidate_id=candidate.id,
                    profile_id=candidate.profile_id,
                    action="already_complete",
                    promotion_id=existing_promotion.id,
                    promotion_status=existing_promotion.promotion_status,
                )
            )
            continue

        if dry_run:
            outcomes.append(
                ReconciliationOutcome(
                    candidate_id=candidate.id,
                    profile_id=candidate.profile_id,
                    action="indexing_enqueued",
                    promotion_id=existing_promotion.id,
                    promotion_status=existing_promotion.promotion_status,
                    detail="dry_run",
                )
            )
            indexing_enqueued += 1
            continue

        outcome_row = _enqueue_indexing_or_record_failure(
            db,
            candidate=candidate,
            promotion=existing_promotion,
            trace_id=trace_id,
        )
        outcomes.append(outcome_row)
        if outcome_row.action == "indexing_enqueued":
            indexing_enqueued += 1
        elif outcome_row.action == "failed":
            failed += 1
        else:
            skipped += 1

    return ReconciliationResult(
        scanned=len(candidates),
        already_complete=already_complete,
        promoted=promoted,
        indexing_enqueued=indexing_enqueued,
        failed=failed,
        skipped=skipped,
        outcomes=outcomes,
    )

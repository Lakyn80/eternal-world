"""Idempotent repair for AI Biographer candidates genuinely stuck with a
long-abandoned mandatory clarification (Task 65.7C, Part E - correcting an
uncommitted Task 65.7 draft that instead disabled mandatory clarifications
for every new Biographer answer; see `avatar_biographer/service.py` and
`PROJECT_PROGRESS.md`'s Task 65.7C entry for the full root-cause).

A candidate mid-way through answering a real, currently-reachable
clarification (the owner has not gotten to it yet, but the review UI works
normally) is NOT stuck - it is simply in progress. This module only ever
targets a candidate whose oldest pending *required* clarification has sat
unanswered for at least `settings.biographer_stuck_clarification_min_age_hours`
(default 24h), so it can never race a real user filling out the review form.

Never touches family-contribution-sourced candidates (`workflow_version !=
2`), never touches an already-reviewed or already-indexed candidate, never
approves, never indexes, never calls a provider, never modifies the
biography, and never prints candidate content - callers may log/print only
`candidate_id`/`profile_id`/status transitions.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_logger, log_event
from app.db.models import BiographerQuestion, ConversationMemoryCandidate, MemoryClarificationQuestion
from app.modules.family_memory_enrichment.service import bypass_mandatory_clarifications_and_finalize

_logger = get_logger("avatar_biographer")


@dataclass(frozen=True)
class RepairedCandidate:
    candidate_id: int
    profile_id: int
    previous_enrichment_status: str
    new_enrichment_status: str
    cancelled_clarification_count: int


@dataclass(frozen=True)
class RepairedStaleClarificationBlock:
    candidate_id: int
    profile_id: int
    previous_unresolved_clarification_count: int


def find_stuck_biographer_candidates(
    db: Session, *, profile_id: int | None = None, min_age_hours: int | None = None
) -> list[ConversationMemoryCandidate]:
    """Read-only: AI-Biographer-sourced candidates (`workflow_version=2`)
    that have had at least one unresolved *required* clarification pending
    for longer than `min_age_hours` (default
    `settings.biographer_stuck_clarification_min_age_hours`) - never
    reviewed (`status="needs_review"`), never finalized
    (`enrichment_status="collecting_details"`). The age floor is what
    distinguishes a genuinely abandoned candidate from one the owner is
    simply, normally, still in the middle of answering right now."""

    threshold_hours = min_age_hours if min_age_hours is not None else settings.biographer_stuck_clarification_min_age_hours
    cutoff = datetime.now(timezone.utc) - timedelta(hours=threshold_hours)

    statement = (
        select(ConversationMemoryCandidate)
        .join(
            MemoryClarificationQuestion,
            MemoryClarificationQuestion.candidate_id == ConversationMemoryCandidate.id,
        )
        .where(
            ConversationMemoryCandidate.workflow_version == 2,
            ConversationMemoryCandidate.status == "needs_review",
            ConversationMemoryCandidate.enrichment_status == "collecting_details",
            ConversationMemoryCandidate.unresolved_clarification_count > 0,
            MemoryClarificationQuestion.status == "pending",
            MemoryClarificationQuestion.required.is_(True),
            MemoryClarificationQuestion.asked_at < cutoff,
        )
        .distinct()
    )
    if profile_id is not None:
        statement = statement.where(ConversationMemoryCandidate.profile_id == profile_id)
    return list(db.scalars(statement))


def repair_stuck_biographer_candidates(
    db: Session,
    *,
    profile_id: int | None = None,
    trace_id: str | None = None,
    min_age_hours: int | None = None,
    limit: int | None = None,
) -> list[RepairedCandidate]:
    """Idempotent: a candidate already repaired (no pending required
    clarifications left, `enrichment_status` already
    `ready_for_owner_review`) no longer matches
    `find_stuck_biographer_candidates`'s filter, so re-running this finds
    nothing left to do for it. `limit` bounds how many candidates a single
    call will repair (Part E.10 - bounded batch size), never a silent
    unbounded sweep of an entire table."""

    candidates = find_stuck_biographer_candidates(db, profile_id=profile_id, min_age_hours=min_age_hours)
    if limit is not None:
        candidates = candidates[:limit]
    repaired: list[RepairedCandidate] = []
    for candidate in candidates:
        previous_status = candidate.enrichment_status
        cancelled_count = bypass_mandatory_clarifications_and_finalize(
            db, candidate=candidate, finalized_by="system:repair_task_65_7"
        )
        db.commit()
        db.refresh(candidate)
        log_event(
            _logger,
            logging.INFO,
            "biographer_stuck_state_repaired",
            trace_id=trace_id,
            candidate_id=candidate.id,
            profile_id=candidate.profile_id,
            previous_status=previous_status,
            new_status=candidate.enrichment_status,
            cancelled_clarification_count=cancelled_count,
        )
        repaired.append(
            RepairedCandidate(
                candidate_id=candidate.id,
                profile_id=candidate.profile_id,
                previous_enrichment_status=previous_status,
                new_enrichment_status=candidate.enrichment_status,
                cancelled_clarification_count=cancelled_count,
            )
        )
    return repaired


def find_stale_active_clarification_blocks(
    db: Session, *, profile_id: int
) -> list[ConversationMemoryCandidate]:
    """Read-only: Biographer-sourced candidates whose stored
    `unresolved_clarification_count` claims a clarification is still
    pending (> 0 - the exact signal `service._get_open_biographer_candidate`
    uses to block the Biographer tab with `active_clarification_exists`)
    but for which no `MemoryClarificationQuestion` row with
    `status="pending"` actually exists (Task 65.10.1).

    Unlike `find_stuck_biographer_candidates` above - which targets a real,
    still-answerable clarification that has simply sat unanswered too long
    (age-gated, never touching a candidate the owner is normally still in
    the middle of answering) - this targets a stored counter that disagrees
    with reality regardless of age: there is no real question behind the
    block for the owner to "wait out" or answer, so age can never make it
    correct. Left uncorrected, this is exactly the reported bug: the
    Biographer tab shows "please answer the current clarification question
    below" with no question rendered below it and no way to proceed."""

    statement = (
        select(ConversationMemoryCandidate)
        .join(BiographerQuestion, BiographerQuestion.resulting_candidate_id == ConversationMemoryCandidate.id)
        .where(
            BiographerQuestion.profile_id == profile_id,
            ConversationMemoryCandidate.status == "needs_review",
            ConversationMemoryCandidate.unresolved_clarification_count > 0,
        )
        .distinct()
    )
    candidates = list(db.scalars(statement))
    stale: list[ConversationMemoryCandidate] = []
    for candidate in candidates:
        has_real_pending_clarification = db.scalar(
            select(MemoryClarificationQuestion.id)
            .where(
                MemoryClarificationQuestion.candidate_id == candidate.id,
                MemoryClarificationQuestion.status == "pending",
            )
            .limit(1)
        )
        if has_real_pending_clarification is None:
            stale.append(candidate)
    return stale


def repair_stale_active_clarification_blocks(
    db: Session, *, profile_id: int, trace_id: str | None = None
) -> list[RepairedStaleClarificationBlock]:
    """Idempotent read-time reconciliation (Task 65.10.1): corrects
    `unresolved_clarification_count` back to 0 for any candidate matched by
    `find_stale_active_clarification_blocks` - a denormalized counter proven
    to disagree with the real, canonical clarification rows for that
    candidate, never a finalize/approval/index action (does not touch
    `enrichment_status`, `finalized_memory_text`, or any promotion/index
    state). Re-running this after a repair finds nothing left to do for
    that candidate, since the query itself no longer matches
    `unresolved_clarification_count > 0`.

    Called from `avatar_biographer/resume.py` before eligibility is
    evaluated, so a resumed session (one left mid-clarification whose
    underlying clarification row was independently removed/corrected, e.g.
    by a data fix or an unrelated bug elsewhere) self-heals on the very next
    read instead of surfacing an impossible, permanently-blocking state to
    the owner."""

    candidates = find_stale_active_clarification_blocks(db, profile_id=profile_id)
    repaired: list[RepairedStaleClarificationBlock] = []
    for candidate in candidates:
        previous_count = candidate.unresolved_clarification_count
        candidate.unresolved_clarification_count = 0
        db.commit()
        db.refresh(candidate)
        log_event(
            _logger,
            logging.INFO,
            "biographer_stale_clarification_block_repaired",
            trace_id=trace_id,
            candidate_id=candidate.id,
            profile_id=candidate.profile_id,
            previous_unresolved_clarification_count=previous_count,
        )
        repaired.append(
            RepairedStaleClarificationBlock(
                candidate_id=candidate.id,
                profile_id=candidate.profile_id,
                previous_unresolved_clarification_count=previous_count,
            )
        )
    return repaired

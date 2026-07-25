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
from app.db.models import ConversationMemoryCandidate, MemoryClarificationQuestion
from app.modules.family_memory_enrichment.service import bypass_mandatory_clarifications_and_finalize

_logger = get_logger("avatar_biographer")


@dataclass(frozen=True)
class RepairedCandidate:
    candidate_id: int
    profile_id: int
    previous_enrichment_status: str
    new_enrichment_status: str
    cancelled_clarification_count: int


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

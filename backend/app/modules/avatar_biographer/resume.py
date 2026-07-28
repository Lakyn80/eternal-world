"""Read-only Biographer resume-state aggregation (Task 65.7, Part D.25).

Composes existing authoritative records (eligibility, the current pending
question, the most recent Biographer-sourced candidate and its review/
promotion status) into one response so the frontend can always render
exactly one actionable current state after navigating back to the
workspace, instead of juggling several separate, possibly-inconsistent
fetches. Never duplicates authoritative data and never approves/finalizes/
indexes anything - a read composition, like `memorial_candidates.router`'s
existing `/history` endpoint (Task 65.4/65.5 precedent), with one narrow
exception (Task 65.10.1): before evaluating eligibility it opportunistically
self-heals a denormalized `unresolved_clarification_count` proven to
disagree with the real clarification rows behind it (see
`avatar_biographer/repair.repair_stale_active_clarification_blocks`), the
same "reconcile canonical state instead of inferring it" precedent used
elsewhere in this codebase (e.g. Task 65.9.1's self-healing embedding
workers) - never a finalize/approval/index side effect.
"""

from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.metrics import observe_biographer_resume
from app.db.models import BiographerQuestion, ConversationMemoryCandidate, MemoryProfile
from app.modules.avatar_biographer import repository
from app.modules.avatar_biographer.repair import repair_stale_active_clarification_blocks
from app.modules.avatar_biographer.schemas import BiographerQuestionRead
from app.modules.avatar_biographer.service import (
    BLOCKED_ACTIVE_CLARIFICATION_EXISTS,
    BLOCKED_CANDIDATE_WAITING_FOR_REVIEW,
    _build_read,
    get_eligibility,
)
from app.modules.family_memory_enrichment import repository as fm_repository
from app.modules.family_memory_enrichment.clarification import localize_question_text
from app.modules.family_memory_enrichment.schemas import ClarificationQuestionRead
from app.modules.family_memory_enrichment.service import _build_clarification_read

_INDEXING_STATES = frozenset({"indexing_in_progress"})
_NOT_INDEXED_STATES = frozenset({"biography_missing", "biography_not_indexed", "biography_stale"})


@dataclass(frozen=True)
class BiographerResumeState:
    profile_id: int
    biography_status: str
    eligible: bool
    blocked_reason: str | None
    active_question: BiographerQuestionRead | None
    candidate_id: int | None
    review_status: str | None
    enrichment_status: str | None
    unresolved_clarification_count: int | None
    promotion_status: str | None
    next_action: str
    next_clarification_question: ClarificationQuestionRead | None


def _latest_biographer_candidate(db: Session, *, profile_id: int) -> ConversationMemoryCandidate | None:
    statement = (
        select(ConversationMemoryCandidate)
        .join(BiographerQuestion, BiographerQuestion.resulting_candidate_id == ConversationMemoryCandidate.id)
        .where(BiographerQuestion.profile_id == profile_id)
        .order_by(ConversationMemoryCandidate.id.desc())
    )
    return db.scalars(statement).first()


def _next_clarification_question_read(
    db: Session, *, candidate_id: int, locale: str
) -> ClarificationQuestionRead | None:
    """The real, currently-answerable clarification question behind an
    `active_clarification_exists` block - re-localized for the current
    viewer exactly like `memorial_candidates.router._localize_enrichment`
    does for the equivalent candidate-review-history text (Task 65.7), so
    this never leaks the canonical Russian source text into a Czech UI."""

    pending = next(
        (item for item in fm_repository.list_clarifications(db, candidate_id=candidate_id) if item.status == "pending"),
        None,
    )
    if pending is None:
        return None
    read = _build_clarification_read(pending)
    read.question_text = localize_question_text(
        question_key=read.question_key, source_text=read.question_text, locale=locale
    )
    return read


def get_resume_state(db: Session, *, profile: MemoryProfile, locale: str = "cs") -> BiographerResumeState:
    # Task 65.10.1: self-heal a resumed session whose stored
    # `unresolved_clarification_count` claims a clarification is pending but
    # no real, answerable clarification row exists for it - BEFORE
    # eligibility is evaluated, so the corrected state (never the stale,
    # impossible one) is what `get_eligibility` and everything below sees.
    repair_stale_active_clarification_blocks(db, profile_id=profile.id)

    eligibility = get_eligibility(db, profile=profile)
    pending = repository.get_pending_question(db, profile_id=profile.id)
    active_question = _build_read(pending) if pending is not None else None

    candidate = _latest_biographer_candidate(db, profile_id=profile.id)
    candidate_id = candidate.id if candidate is not None else None
    review_status = candidate.status if candidate is not None else None
    enrichment_status = candidate.enrichment_status if candidate is not None else None
    unresolved_count = candidate.unresolved_clarification_count if candidate is not None else None
    promotion = candidate.avatar_memory_promotion if candidate is not None else None
    promotion_status = promotion.promotion_status if promotion is not None else None

    next_clarification_question: ClarificationQuestionRead | None = None
    if eligibility.blocked_reason == BLOCKED_ACTIVE_CLARIFICATION_EXISTS and candidate_id is not None:
        # Requirement 2 (Task 65.10.1): whenever the resume state blocks on
        # a real active clarification, the actual current question must be
        # returned alongside it - never just the generic blocked_reason -
        # so the frontend can render it directly instead of showing the
        # blocking notice with nothing answerable underneath it.
        next_clarification_question = _next_clarification_question_read(db, candidate_id=candidate_id, locale=locale)

    if not eligibility.eligible:
        if eligibility.blocked_reason in _INDEXING_STATES:
            next_action = "biography_indexing"
        elif eligibility.blocked_reason in _NOT_INDEXED_STATES:
            next_action = "biography_not_indexed"
        elif eligibility.blocked_reason == BLOCKED_ACTIVE_CLARIFICATION_EXISTS:
            # Task 65.7C: a real, mandatory, still-answerable clarification is
            # blocking the next topic - a distinct, actionable resume state,
            # never lumped into the generic "blocked" bucket the frontend
            # cannot act on.
            next_action = "clarification_pending"
        elif eligibility.blocked_reason == BLOCKED_CANDIDATE_WAITING_FOR_REVIEW:
            next_action = "candidate_ready_for_review"
        else:
            next_action = "blocked"
    elif active_question is not None:
        next_action = "question_ready"
    elif promotion_status == "indexed":
        next_action = "candidate_indexed"
    elif promotion_status == "pending_index":
        next_action = "candidate_pending_index"
    elif review_status == "needs_review" and enrichment_status == "ready_for_owner_review":
        next_action = "candidate_ready_for_review"
    elif review_status == "needs_review":
        # Legacy stuck state (pre Task 65.7 repair) or a rejected/other
        # transient status - surfaced explicitly rather than silently
        # falling through, so the frontend never guesses.
        next_action = "candidate_needs_owner_action"
    else:
        next_action = "question_ready"

    observe_biographer_resume(state=next_action, result="success")
    return BiographerResumeState(
        profile_id=profile.id,
        biography_status=profile.biography_status,
        eligible=eligibility.eligible,
        blocked_reason=eligibility.blocked_reason,
        active_question=active_question,
        candidate_id=candidate_id,
        review_status=review_status,
        enrichment_status=enrichment_status,
        unresolved_clarification_count=unresolved_count,
        promotion_status=promotion_status,
        next_action=next_action,
        next_clarification_question=next_clarification_question,
    )

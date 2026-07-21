"""AI Biographer question/answer loop (Task 65.2).

Turns one answered biographer question into a real `ConversationMemoryCandidate`
by reusing the existing avatar-chat-derived candidate/enrichment pipeline
(`conversation_memory_candidates` + `family_memory_enrichment`) exactly as-is
- this module never writes to those tables directly and never touches
Qdrant/promotions/indexing. A biographer answer is never approved or indexed
automatically; it only ever reaches `needs_review`, same as any other
workflow_version=2 candidate.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import BiographerQuestion, ConversationMemoryCandidate, MemoryProfile, User
from app.modules.avatar_biographer import repository
from app.modules.avatar_biographer import topics as topic_catalog
from app.modules.avatar_biographer.schemas import (
    BiographerAnswerResponse,
    BiographerEligibilityRead,
    BiographerQuestionRead,
)
from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
from app.modules.conversation_memory_candidates.service import create_candidate
from app.modules.family_memory_enrichment.enums import EnrichmentStatus, FamilyMemoryActorRole, PrivacyScope
from app.modules.family_memory_enrichment.schemas import DemoFamilyActorContext
from app.modules.family_memory_enrichment.service import (
    _synchronize_candidate,  # re-entrant re-sync after correcting memory_type below
    get_candidate_enrichment,
    initialize_candidate,
)


BLOCKED_BIOGRAPHY_MISSING = "biography_missing"
BLOCKED_BIOGRAPHY_NOT_INDEXED = "biography_not_indexed"
BLOCKED_ACTIVE_CANDIDATE_REQUIRES_ANSWER = "active_candidate_requires_answer"


class BiographerNotFoundError(Exception):
    pass


class BiographerBlockedError(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


class BiographerConflictError(Exception):
    pass


def _build_read(question: BiographerQuestion) -> BiographerQuestionRead:
    return BiographerQuestionRead(
        id=question.id,
        profile_id=question.profile_id,
        topic=question.topic,
        locale=question.locale,
        question_text=question.question_text,
        status=question.status,
        asked_at=question.asked_at,
        answered_at=question.answered_at,
        resulting_candidate_id=question.resulting_candidate_id,
    )


def _get_open_biographer_candidate(db: Session, *, profile_id: int) -> ConversationMemoryCandidate | None:
    """A biographer-originated candidate that still needs a clarification
    answered before a new topic should be offered - resuming state, not a
    new duplicate candidate for the same in-progress topic."""

    statement = (
        select(ConversationMemoryCandidate)
        .join(BiographerQuestion, BiographerQuestion.resulting_candidate_id == ConversationMemoryCandidate.id)
        .where(
            BiographerQuestion.profile_id == profile_id,
            ConversationMemoryCandidate.status == "needs_review",
            ConversationMemoryCandidate.unresolved_clarification_count > 0,
        )
    )
    return db.scalar(statement)


def get_eligibility(db: Session, *, profile: MemoryProfile) -> BiographerEligibilityRead:
    if not (profile.biography or "").strip():
        return BiographerEligibilityRead(eligible=False, blocked_reason=BLOCKED_BIOGRAPHY_MISSING)
    if profile.biography_status != "indexed":
        return BiographerEligibilityRead(eligible=False, blocked_reason=BLOCKED_BIOGRAPHY_NOT_INDEXED)
    if _get_open_biographer_candidate(db, profile_id=profile.id) is not None:
        return BiographerEligibilityRead(
            eligible=False,
            blocked_reason=BLOCKED_ACTIVE_CANDIDATE_REQUIRES_ANSWER,
        )
    return BiographerEligibilityRead(eligible=True, blocked_reason=None)


def get_next_question(db: Session, *, profile: MemoryProfile, locale: str) -> BiographerQuestionRead | None:
    """Returns the current pending question (resuming state if one already
    exists), the next never-asked topic's question, or `None` once every
    bounded topic has been asked - never more than one pending question."""

    eligibility = get_eligibility(db, profile=profile)
    if not eligibility.eligible:
        raise BiographerBlockedError(eligibility.blocked_reason or "blocked")

    pending = repository.get_pending_question(db, profile_id=profile.id)
    if pending is not None:
        return _build_read(pending)

    used_topic_keys = {question.topic for question in repository.list_questions_for_profile(db, profile_id=profile.id)}
    topic = topic_catalog.next_unused_topic(used_topic_keys=used_topic_keys)
    if topic is None:
        return None

    question_text = topic_catalog.question_text_for(topic, locale=locale)
    question = repository.create_question(
        db,
        profile_id=profile.id,
        topic=topic.key,
        locale=locale,
        question_text=question_text,
    )
    db.commit()
    db.refresh(question)
    return _build_read(question)


def skip_question(db: Session, *, profile: MemoryProfile, question_id: int) -> BiographerQuestionRead:
    """Skipping never creates a candidate - the topic is simply marked
    covered so it is not offered again for this memorial."""

    question = repository.get_question_for_profile(db, profile_id=profile.id, question_id=question_id)
    if question is None:
        raise BiographerNotFoundError("Biographer question not found")
    if question.status != "pending":
        raise BiographerConflictError("Question is not pending")
    repository.mark_skipped(db, question=question)
    db.commit()
    db.refresh(question)
    return _build_read(question)


def answer_question(
    db: Session,
    *,
    profile: MemoryProfile,
    question_id: int,
    current_user: User,
    actor_role: FamilyMemoryActorRole,
    locale: str,
    answer_text: str,
) -> BiographerAnswerResponse:
    question = repository.get_question_for_profile(db, profile_id=profile.id, question_id=question_id)
    if question is None:
        raise BiographerNotFoundError("Biographer question not found")
    if question.status != "pending":
        raise BiographerConflictError("Question is not pending")

    topic = topic_catalog.get_topic(question.topic)
    intended_memory_type = topic.memory_type if topic is not None else "general"
    excerpt = answer_text[:500]

    payload = MemoryCandidateCreate(
        owner_user_id=profile.user_id,
        avatar_id=str(profile.id),
        profile_id=profile.id,
        conversation_id=None,
        trace_id=None,
        user_message_excerpt=excerpt,
        proposed_memory_text=excerpt,
        reason=f"AI Biographer topic: {question.topic}",
        language=locale,
        enrichment_status=EnrichmentStatus.DRAFT,
        finalized_memory_text=None,
        privacy_scope=PrivacyScope.PRIVATE_OWNER,
        workflow_version=2,
    )
    candidate = create_candidate(db, payload=payload, commit=False)
    db.flush()

    actor = DemoFamilyActorContext(actor_id=str(current_user.id), actor_role=actor_role)
    enrichment = initialize_candidate(
        db,
        owner_user_id=profile.user_id,
        candidate_id=candidate.id,
        actor=actor,
        initial_text=answer_text,
    )

    if candidate.memory_type != intended_memory_type:
        # `initialize_candidate` classifies `memory_type` from a Russian-
        # keyword heuristic tuned for free-form avatar chat, which will not
        # recognize a topic-driven biographer answer. The topic already
        # unambiguously determines the correct `memory_type` (and therefore
        # which clarification questions, if any, are required) - re-running
        # the same deterministic synchronization step the module already
        # uses after every contribution keeps this a single source of
        # truth for the state machine, rather than duplicating it here.
        candidate.memory_type = intended_memory_type
        _synchronize_candidate(db, candidate=candidate, finalized_by="system:ai-biographer-topic")
        db.commit()
        db.refresh(candidate)
        enrichment = get_candidate_enrichment(
            db,
            owner_user_id=profile.user_id,
            candidate_id=candidate.id,
            actor=actor,
        )

    repository.mark_answered(
        db,
        question=question,
        answered_by_user_id=current_user.id,
        resulting_candidate_id=candidate.id,
    )
    db.commit()
    db.refresh(question)

    return BiographerAnswerResponse(
        question=_build_read(question),
        candidate_id=candidate.id,
        enrichment_status=enrichment.enrichment_status.value,
        unresolved_clarification_count=enrichment.unresolved_clarification_count,
    )

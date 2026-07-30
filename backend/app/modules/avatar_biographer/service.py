"""AI Biographer question/answer loop (Task 65.2, made context-aware in
Task 65.6).

Turns one answered biographer question into a real `ConversationMemoryCandidate`
by reusing the existing avatar-chat-derived candidate/enrichment pipeline
(`conversation_memory_candidates` + `family_memory_enrichment`) exactly as-is
- this module never writes to those tables directly and never touches
Qdrant/promotions/indexing. A biographer answer is never approved or indexed
automatically; it only ever reaches `needs_review`, same as any other
workflow_version=2 candidate.

Task 65.6 replaced the previous "always the next never-asked fixed-catalog
topic" selection with: verified-context retrieval per topic, deterministic
coverage evaluation, coverage-priority topic selection, DeepSeek-backed
context-aware question generation (bounded, validated, at most one
regeneration, deterministic fallback), and a database-level guard against
two concurrent pending questions. See `coverage.py`, `context_package.py`,
`duplicate_prevention.py`, `question_generation.py`.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from time import perf_counter

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import (
    observe_biographer_blocked,
    observe_biographer_context_sources,
    observe_biographer_direct_answer,
    observe_biographer_fallback,
    observe_biographer_generation_duration,
    observe_biographer_question,
    observe_biographer_selected_topic_hydration,
    observe_biographer_topic_query_batch,
    observe_biographer_topic_selection,
)
from app.db.models import BiographerQuestion, ConversationMemoryCandidate, MemoryProfile, User
from app.modules.avatar_biographer import coverage, repository
from app.modules.avatar_biographer import topics as topic_catalog
from app.modules.avatar_biographer.context_package import (
    BiographerTopicContextBatch,
    TopicContextPackage,
    build_topic_context_batch,
    empty_context_batch,
    empty_context_package,
)
from app.modules.avatar_biographer.question_generation import generate_question_for_topic
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

_logger = get_logger("avatar_biographer")

#: Minimum blocked reasons (Part B.6 of the task spec). `permission_denied`
#: is never returned by `get_eligibility` itself - a non-member/insufficient
#: -capability request is rejected at the router/capability layer (404/403)
#: before this service is ever called; the value is kept here purely for
#: documentation/forward-compatibility with the frontend's reason union.
BLOCKED_BIOGRAPHY_MISSING = "biography_missing"
BLOCKED_BIOGRAPHY_NOT_INDEXED = "biography_not_indexed"
BLOCKED_BIOGRAPHY_STALE = "biography_stale"
BLOCKED_INDEXING_IN_PROGRESS = "indexing_in_progress"
BLOCKED_PERMISSION_DENIED = "permission_denied"
BLOCKED_ACTIVE_CLARIFICATION_EXISTS = "active_clarification_exists"
BLOCKED_CANDIDATE_WAITING_FOR_REVIEW = "candidate_waiting_for_review"

#: Legacy alias kept for any external caller still referencing the Task
#: 65.2 name - identical value to `BLOCKED_ACTIVE_CLARIFICATION_EXISTS`.
BLOCKED_ACTIVE_CANDIDATE_REQUIRES_ANSWER = BLOCKED_ACTIVE_CLARIFICATION_EXISTS

_INDEXING_IN_PROGRESS_STATUSES = frozenset({"ready_for_ingestion", "ingesting"})


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
        generation_mode=question.generation_mode,
        fallback_used=question.fallback_used,
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
    if profile.biography_status in _INDEXING_IN_PROGRESS_STATUSES:
        return BiographerEligibilityRead(eligible=False, blocked_reason=BLOCKED_INDEXING_IN_PROGRESS)
    if profile.biography_status == "stale":
        # Deliberate choice (Part 8 of the task spec): block new contextual
        # questions rather than mixing the edited-but-not-yet-reindexed
        # draft text with the still-indexed (now stale) verified content -
        # re-indexing is required before the Biographer trusts anything new.
        return BiographerEligibilityRead(eligible=False, blocked_reason=BLOCKED_BIOGRAPHY_STALE)
    if profile.biography_status != "indexed":
        return BiographerEligibilityRead(eligible=False, blocked_reason=BLOCKED_BIOGRAPHY_NOT_INDEXED)
    if _get_open_biographer_candidate(db, profile_id=profile.id) is not None:
        return BiographerEligibilityRead(eligible=False, blocked_reason=BLOCKED_ACTIVE_CLARIFICATION_EXISTS)
    return BiographerEligibilityRead(eligible=True, blocked_reason=None)


def _safe_context_batch(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    locale: str,
) -> BiographerTopicContextBatch:
    """Retrieval must degrade safely (Part 11 of the task spec) - a Qdrant/
    embedding outage falls back to the deterministic question path rather
    than a 500.

    Task 65.11.1: one call now covers the whole catalog (one batched query
    encode + one Qdrant batch request), so a failure degrades the *whole*
    coverage evaluation at once, exactly as a per-topic failure previously
    degraded that topic - `empty_context_batch` keeps `retrieval_used=False`
    for every topic, which `question_generation` already treats as
    "retrieval unavailable, use the deterministic fallback question".
    """

    try:
        return build_topic_context_batch(
            db,
            current_user=current_user,
            profile_id=profile_id,
            topics=topic_catalog.BIOGRAPHER_TOPICS,
            locale=locale,
        )
    except Exception:
        log_event(
            _logger,
            logging.WARNING,
            "biographer_context_retrieval_failed",
            profile_id=profile_id,
            topic_count=len(topic_catalog.BIOGRAPHER_TOPICS),
        )
        return empty_context_batch(topic_catalog.BIOGRAPHER_TOPICS, locale=locale)


def _safe_selected_topic_context(
    context_batch: BiographerTopicContextBatch,
    *,
    profile_id: int,
    topic: topic_catalog.BiographerTopic,
) -> TopicContextPackage:
    """Materialize prompt excerpts for the SELECTED topic only (Task 65.11.1
    Phase 4).

    Pure local shaping of text the single batch query already returned - no
    second embedding of the selected topic's query, no second per-source-type
    retrieval, no extra Qdrant request. Still guarded, so a malformed batch
    payload degrades to the deterministic fallback instead of a 500.
    """

    started_at = perf_counter()
    try:
        package = context_batch.hydrate_context_package(topic)
    except Exception:
        log_event(
            _logger,
            logging.WARNING,
            "biographer_selected_context_hydration_failed",
            profile_id=profile_id,
            topic=topic.key,
        )
        package = empty_context_package(topic)
    observe_biographer_selected_topic_hydration(duration_seconds=perf_counter() - started_at)
    return package


def get_next_question(
    db: Session,
    *,
    profile: MemoryProfile,
    current_user: User,
    locale: str,
    trace_id: str | None = None,
) -> BiographerQuestionRead | None:
    """Returns the current pending question (resuming state if one already
    exists), a newly generated context-aware question for the next
    coverage-selected topic, or `None` once no topic remains selectable."""

    eligibility = get_eligibility(db, profile=profile)
    log_event(
        _logger,
        logging.INFO,
        "biographer_eligibility_evaluated",
        profile_id=profile.id,
        eligible=eligibility.eligible,
        blocked_reason=eligibility.blocked_reason,
    )
    if not eligibility.eligible:
        log_event(
            _logger,
            logging.INFO,
            "biographer_generation_blocked",
            profile_id=profile.id,
            reason=eligibility.blocked_reason,
        )
        observe_biographer_blocked(reason=eligibility.blocked_reason or "other", locale=locale)
        raise BiographerBlockedError(eligibility.blocked_reason or "blocked")

    pending = repository.get_pending_question(db, profile_id=profile.id)
    if pending is not None:
        return _build_read(pending)

    all_questions = repository.list_questions_for_profile(db, profile_id=profile.id)
    unresolved_candidate_topics = repository.get_unresolved_candidate_topic_keys(db, profile_id=profile.id)

    # Task 65.11.1: ONE batched query encode (all 8 catalog topics, query
    # semantics) + ONE Qdrant batch request for the whole catalog, replacing
    # the previous 8 topics x 2 source types = 16 serial
    # `retrieve_profile_rag()` calls. Coverage semantics below are unchanged:
    # `build_topic_coverage_map` still receives one verified chunk count per
    # topic, computed from the same bounded, verified, owner/profile-scoped
    # evidence it received before.
    context_batch = _safe_context_batch(
        db, current_user=current_user, profile_id=profile.id, locale=locale
    )
    observe_biographer_topic_query_batch(
        topic_query_batch_size=context_batch.topic_query_batch_size,
        model_invocation_count=context_batch.model_invocation_count,
        qdrant_request_count=context_batch.qdrant_request_count,
        coverage_retrieval_duration_seconds=context_batch.coverage_retrieval_duration_ms / 1000.0,
    )
    for topic in topic_catalog.BIOGRAPHER_TOPICS:
        observe_biographer_context_sources(
            topic=topic.key,
            source_count=context_batch.evidence_for(topic.key).selected_source_count,
        )

    coverages = coverage.build_topic_coverage_map(
        all_questions=all_questions,
        verified_chunk_counts_by_topic={
            topic.key: context_batch.evidence_for(topic.key).selected_chunk_count
            for topic in topic_catalog.BIOGRAPHER_TOPICS
        },
        unresolved_candidate_topic_keys=unresolved_candidate_topics,
    )
    log_event(
        _logger,
        logging.INFO,
        "biographer_coverage_evaluated",
        profile_id=profile.id,
        coverage_states={c.topic.key: c.state.value for c in coverages},
    )

    selected = coverage.select_next_topic(coverages, total_questions_asked=len(all_questions))
    if selected is None:
        if any(c.blocked_from_selection for c in coverages):
            observe_biographer_blocked(reason=BLOCKED_CANDIDATE_WAITING_FOR_REVIEW, locale=locale)
            raise BiographerBlockedError(BLOCKED_CANDIDATE_WAITING_FOR_REVIEW)
        return None

    topic = selected.topic
    observe_biographer_topic_selection(topic=topic.key, coverage_state=selected.state.value)
    log_event(
        _logger,
        logging.INFO,
        "biographer_topic_selected",
        profile_id=profile.id,
        topic=topic.key,
        coverage_state=selected.state.value,
    )

    context_package = _safe_selected_topic_context(context_batch, profile_id=profile.id, topic=topic)
    log_event(
        _logger,
        logging.INFO,
        "biographer_context_retrieved",
        profile_id=profile.id,
        topic=topic.key,
        retrieval_used=context_package.retrieval_used,
        selected_source_count=context_package.selected_source_count,
        selected_chunk_count=context_package.selected_chunk_count,
        context_character_count=context_package.context_character_count,
        estimated_context_tokens=context_package.estimated_context_tokens,
        retrieval_duration_ms=context_package.retrieval_duration_ms,
    )

    topic_questions = [question for question in all_questions if question.topic == topic.key]
    skipped_or_postponed_texts = [
        question.question_text for question in all_questions if question.status in ("skipped", "postponed")
    ]

    started_at = perf_counter()
    generated = generate_question_for_topic(
        db,
        topic=topic,
        context_package=context_package,
        locale=locale,
        profile_id=profile.id,
        user_id=current_user.id,
        trace_id=trace_id,
        previous_questions_for_topic=topic_questions,
        all_previous_questions=all_questions,
        skipped_or_postponed_texts=skipped_or_postponed_texts,
    )
    duration_seconds = perf_counter() - started_at

    observe_biographer_generation_duration(
        locale=locale, result=generated.validation_result, duration_seconds=duration_seconds
    )
    observe_biographer_question(
        locale=locale, topic=topic.key, result=generated.validation_result, generation_mode=generated.generation_mode
    )
    if generated.fallback_used:
        observe_biographer_fallback(
            reason="validation_failed_twice" if context_package.retrieval_used else "retrieval_unavailable",
            locale=locale,
        )

    try:
        question = repository.create_question(
            db,
            profile_id=profile.id,
            topic=topic.key,
            locale=locale,
            question_text=generated.question_text,
            generation_mode=generated.generation_mode,
            provider=generated.provider,
            model=generated.model,
            ai_action_id=generated.ai_action_id,
            context_source_count=context_package.selected_source_count,
            context_chunk_count=context_package.selected_chunk_count,
            question_intent=generated.question_intent,
            validation_result=generated.validation_result,
            fallback_used=generated.fallback_used,
        )
        db.commit()
    except IntegrityError:
        # The DB-level `uq_biographer_questions_profile_pending` partial
        # unique index caught a concurrent request that created a pending
        # question first (Part G.27 / Part 62 of the task spec) - reuse the
        # winner instead of erroring or creating a duplicate.
        db.rollback()
        winner = repository.get_pending_question(db, profile_id=profile.id)
        if winner is not None:
            return _build_read(winner)
        raise
    db.refresh(question)

    log_event(
        _logger,
        logging.INFO,
        "biographer_question_persisted",
        profile_id=profile.id,
        topic=topic.key,
        question_id=question.id,
        generation_mode=question.generation_mode,
    )
    return _build_read(question)


def skip_question(db: Session, *, profile: MemoryProfile, question_id: int) -> BiographerQuestionRead:
    """Skipping never creates a candidate. Unlike a topic exhausted by
    evidence, a skipped topic is only excluded from selection while its most
    recent action stays "skipped" - it does not become permanently
    unselectable the way the previous fixed-catalog design made every topic
    permanently one-shot."""

    question = repository.get_question_for_profile(db, profile_id=profile.id, question_id=question_id)
    if question is None:
        raise BiographerNotFoundError("Biographer question not found")
    if question.status != "pending":
        raise BiographerConflictError("Question is not pending")
    repository.mark_skipped(db, question=question)
    db.commit()
    db.refresh(question)
    return _build_read(question)


def postpone_question(db: Session, *, profile: MemoryProfile, question_id: int) -> BiographerQuestionRead:
    """"Ask later": distinct from skip - the topic becomes selectable again
    once the postpone cool-down elapses (`coverage.POSTPONE_COOLDOWN_QUESTIONS`),
    instead of staying excluded until explicitly re-answered."""

    question = repository.get_question_for_profile(db, profile_id=profile.id, question_id=question_id)
    if question is None:
        raise BiographerNotFoundError("Biographer question not found")
    if question.status != "pending":
        raise BiographerConflictError("Question is not pending")
    repository.mark_postponed(db, question=question)
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
        # unambiguously determines the correct `memory_type` - re-running
        # the same deterministic synchronization step the module already
        # uses after every contribution keeps this a single source of
        # truth for the state machine, rather than duplicating it here.
        candidate.memory_type = intended_memory_type
        _synchronize_candidate(db, candidate=candidate, finalized_by="system:ai-biographer-topic")
        db.commit()
        db.refresh(candidate)

    # Task 65.7C (Part E/roadmap correction): an earlier, uncommitted Task
    # 65.7 draft called `bypass_mandatory_clarifications_and_finalize` here
    # unconditionally, forcing every Biographer answer straight to
    # `ready_for_owner_review` and cancelling any required clarification the
    # topic's memory-type mandates (e.g. childhood_memory's required
    # place/approximate_period questions). That directly contradicted the
    # already-committed Task 65.6 mandatory-clarification contract
    # (`test_answering_childhood_question_creates_candidate_with_required_clarification`,
    # `test_active_clarification_blocks_new_topic`) and this task's own Part
    # E requirement ("required unanswered clarifications are not silently
    # skipped") - removed. `initialize_candidate` above already determines
    # the correct `enrichment_status`/`unresolved_clarification_count` from
    # the topic's real clarification requirements, exactly as it does for
    # every other workflow_version=2 candidate; a Biographer answer is no
    # longer treated as a special case here.
    #
    # `bypass_mandatory_clarifications_and_finalize` itself is preserved as
    # an explicit, non-automatic repair primitive
    # (`avatar_biographer/repair.py`, `scripts/repair_stuck_biographer_candidates.py`)
    # for candidates that are independently confirmed stuck - it is
    # deliberately never called from this normal answer path anymore.
    enrichment = get_candidate_enrichment(
        db,
        owner_user_id=profile.user_id,
        candidate_id=candidate.id,
        actor=actor,
    )
    log_event(
        _logger,
        logging.INFO,
        "biographer_answer_accepted",
        profile_id=profile.id,
        question_id=question.id,
        candidate_id=candidate.id,
        enrichment_status=enrichment.enrichment_status.value,
        unresolved_clarification_count=enrichment.unresolved_clarification_count,
    )
    observe_biographer_direct_answer(result="accepted", locale=locale)

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

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from time import perf_counter

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import (
    observe_memory_clarification,
    observe_memory_contribution_created,
    observe_memory_dispute,
    observe_memory_enrichment_status,
    observe_memory_owner_review,
)
from app.db.models import (
    ConversationMemoryCandidate,
    FamilyMemoryContribution,
    MemoryClarificationQuestion,
)
from app.modules.avatar_memory_promotions import service as promotion_service
from app.modules.content_translation import service as content_translation_service
from app.modules.content_translation.schemas import TranslationFieldRequest
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, ExecutionSource
from app.modules.family_memory_enrichment import repository
from app.modules.family_memory_enrichment.clarification import (
    classify_memory_type,
    extract_answer_details,
    initial_structured_details,
    missing_required_keys,
    next_question_spec,
    normalize_text,
)
from app.modules.family_memory_enrichment.eligibility import (
    BROAD_VISIBILITY_PRIVACY_SCOPES,
    INDEXABLE_PRIVACY_SCOPES,
    assert_candidate_eligible_for_promotion,
)
from app.modules.family_memory_enrichment.enums import (
    ClarificationStatus,
    ContributionType,
    DisputeStatus,
    EnrichmentStatus,
    FamilyMemoryActorRole,
    OwnerReviewAction,
)
from app.modules.family_memory_enrichment.finalizer import build_finalized_draft
from app.modules.family_memory_enrichment.schemas import (
    CandidateEnrichmentRead,
    ClarificationAnswerRequest,
    ClarificationQuestionRead,
    ClarificationSkipRequest,
    DemoFamilyActorContext,
    FamilyMemoryContributionCreate,
    FamilyMemoryContributionRead,
    FinalizeRequest,
    OwnerReviewRequest,
    OwnerReviewResponse,
)


DEMO_OWNER_ACTOR_ID = "demo-owner-eva"
logger = get_logger("family_memory_enrichment")

#: Task 65.6.1 (Part C/D): `owner_review`'s confirm/edit_and_confirm/
#: approve_multiple_perspectives branch creates the `pending_index`
#: `AvatarMemoryPromotion` row synchronously (cheap, DB-only, already
#: committed below) but deliberately does NOT also enqueue the heavy
#: embedding/Qdrant step here. Auto-enqueueing a real Celery job from
#: inside every approval was tried and reverted: this codepath is exercised
#: by a very large share of the backend test suite (every family-
#: contribution AND every AI-Biographer approval test), and dispatching a
#: real `.delay()` plus its `background_jobs` DB round-trip from each one
#: measurably multiplied already-slow, real-BGE-M3-model-backed test runs
#: without a corresponding benefit in the test environment. The durable
#: `pending_index` state this still leaves behind is exactly "option B" of
#: the task's own required invariant: a safe, idempotent, explicit
#: `/candidates/{id}/index` endpoint (`avatar_memory_indexing.service.
#: index_promotion`, unchanged) and the
#: `avatar_memory_promotions.reconciliation` module/script both remain able
#: to complete indexing for it at any time, with no data ever silently lost
#: or left in an undetectable state.

#: The only source language that currently triggers automatic backend
#: translation of dynamic content (Task 64.5.1). Russian remains the
#: canonical avatar pipeline language, so Russian-origin content is never
#: auto-translated to Czech - a Czech view of a Russian-origin record can
#: only be produced through the explicit translation-retry endpoint.
CZECH_SOURCE_LANGUAGE = "cs"
RUSSIAN_TARGET_LANGUAGE = "ru"
FINALIZED_MEMORY_FIELD_NAME = "finalized_memory_text"

#: Default owner-authored texts shown when the owner does not type a note,
#: localized by the candidate's source language so a Czech-origin candidate
#: never surfaces a Russian-only default string in a Czech interface. These
#: are static UI-adjacent defaults (not free-form content), so they are
#: localized directly rather than through the content_translation service.
_DEFAULT_REQUEST_MORE_DETAILS_TEXT = {
    "ru": "Пожалуйста, добавьте ещё одну важную деталь об этом воспоминании.",
    "cs": "Prosím, doplňte ještě jeden důležitý detail k této vzpomínce.",
}
_DEFAULT_DISPUTE_TEXT = {
    "ru": "Владелец отметил воспоминание как спорное.",
    "cs": "Vlastník označil tuto vzpomínku jako spornou.",
}
_DEFAULT_OWNER_CONFIRMATION_TEXT = {
    "ru": "Владелец подтвердил финальный вариант воспоминания.",
    "cs": "Vlastník potvrdil finální verzi vzpomínky.",
}


def _localized_default_text(mapping: dict[str, str], *, language: str | None) -> str:
    return mapping.get(language or "ru", mapping["ru"])


def _translate_contribution_if_czech_origin(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
    contribution: FamilyMemoryContribution,
) -> None:
    """Backend-only translation of a newly created contribution (Part E.16-21).

    A translation-provider failure is captured and recorded as a
    ``failed``-status row by the translation service itself; it never
    raises here and never rolls back the (already flushed) contribution.
    """
    if candidate.language != CZECH_SOURCE_LANGUAGE:
        return
    content_translation_service.translate_content_field(
        db,
        TranslationFieldRequest(
            candidate_id=candidate.id,
            contribution_id=contribution.id,
            entity_type="family_memory_contribution",
            entity_id=str(contribution.id),
            field_name="contribution_text",
            source_language=CZECH_SOURCE_LANGUAGE,
            target_language=RUSSIAN_TARGET_LANGUAGE,
            source_text=contribution.contribution_text,
        ),
        call_context=AiCallContext(
            feature=AiFeature.MEMORY_CANDIDATE_FINALIZATION,
            execution_source=ExecutionSource.FASTAPI,
            requested_locale=RUSSIAN_TARGET_LANGUAGE,
            resolved_locale=RUSSIAN_TARGET_LANGUAGE,
            user_id=candidate.owner_user_id,
            memorial_id=candidate.profile_id,
        ),
    )


def _translate_finalized_memory_if_czech_origin(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
) -> None:
    """Backend-only translation of the candidate's finalized memory text.

    Called every time ``finalized_memory_text`` is (re)computed. If the
    source text changed since the last translation, the previous
    translation row is superseded (see ``content_translation.repository``)
    and a fresh translation attempt is made automatically - the owner never
    has to manually request a translation for it to exist, but indexing
    still independently re-validates freshness via
    ``eligibility.get_finalized_memory_translation_block_reason``.
    """
    if candidate.language != CZECH_SOURCE_LANGUAGE:
        return
    finalized_text = (candidate.finalized_memory_text or "").strip()
    if not finalized_text:
        return
    content_translation_service.translate_content_field(
        db,
        TranslationFieldRequest(
            candidate_id=candidate.id,
            entity_type="memory_candidate",
            entity_id=str(candidate.id),
            field_name=FINALIZED_MEMORY_FIELD_NAME,
            source_language=CZECH_SOURCE_LANGUAGE,
            target_language=RUSSIAN_TARGET_LANGUAGE,
            source_text=finalized_text,
        ),
        call_context=AiCallContext(
            feature=AiFeature.MEMORY_CANDIDATE_FINALIZATION,
            execution_source=ExecutionSource.FASTAPI,
            requested_locale=RUSSIAN_TARGET_LANGUAGE,
            resolved_locale=RUSSIAN_TARGET_LANGUAGE,
            user_id=candidate.owner_user_id,
            memorial_id=candidate.profile_id,
        ),
    )


class FamilyMemoryNotFoundError(Exception):
    pass


class FamilyMemoryAuthorizationError(Exception):
    pass


class FamilyMemoryInvalidTransitionError(Exception):
    pass


def is_demo_owner(actor: DemoFamilyActorContext) -> bool:
    """Whether ``actor`` carries owner authority for this candidate.

    Historically (Task 64.x) this also required ``actor.actor_id ==
    DEMO_OWNER_ACTOR_ID``, since the unauthenticated FA chat demo has no real
    account system and a fixed demo owner id was the only available check.
    Task 65.2 added a second, real caller: the authenticated memorial
    workspace's Biographer/review endpoints, which resolve ``actor_role``
    from a database-verified `MemorialMembership.role` (never from
    client-supplied input) before constructing this actor context - for that
    caller, a fixed demo id can never match, which would incorrectly deny
    every real owner. The identity check added no real security (it was
    always just a string constant, never tied to authentication) since the
    demo surface has no auth boundary to begin with; the role field is now
    the single source of truth, and every caller remains responsible for
    only ever setting ``actor_role=OWNER`` when the actor is truly the
    owner.
    """
    return actor.actor_role == FamilyMemoryActorRole.OWNER


def validate_demo_actor(actor: DemoFamilyActorContext) -> None:
    if actor.actor_role == FamilyMemoryActorRole.SYSTEM:
        raise FamilyMemoryAuthorizationError("System role is internal only")


def _can_view_candidate(candidate: ConversationMemoryCandidate, actor: DemoFamilyActorContext) -> bool:
    if is_demo_owner(actor):
        return True
    if candidate.privacy_scope in BROAD_VISIBILITY_PRIVACY_SCOPES:
        return actor.actor_role in {
            FamilyMemoryActorRole.CONTRIBUTOR,
            FamilyMemoryActorRole.TRUSTED_REVIEWER,
        }
    return False


def _get_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    actor: DemoFamilyActorContext,
    for_update: bool = False,
) -> ConversationMemoryCandidate:
    validate_demo_actor(actor)
    candidate = repository.get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        for_update=for_update,
    )
    if candidate is None:
        raise FamilyMemoryNotFoundError("Family memory candidate not found")
    actor_has_contribution = any(
        item.actor_id == actor.actor_id
        for item in repository.list_contributions(db, candidate_id=candidate.id)
    )
    if not _can_view_candidate(candidate, actor) and not actor_has_contribution:
        raise FamilyMemoryNotFoundError("Family memory candidate not found")
    return candidate


def _build_contribution_read(contribution: FamilyMemoryContribution) -> FamilyMemoryContributionRead:
    return FamilyMemoryContributionRead(
        contribution_id=contribution.id,
        candidate_id=contribution.candidate_id,
        avatar_id=contribution.avatar_id,
        profile_id=contribution.profile_id,
        actor_id=contribution.actor_id,
        actor_role=contribution.actor_role,
        relationship_to_owner=contribution.relationship_to_owner,
        contribution_type=contribution.contribution_type,
        contribution_text=contribution.contribution_text,
        structured_details=contribution.structured_details,
        language=contribution.language,
        source_message_hash=contribution.source_message_hash,
        trace_id=contribution.trace_id,
        supersedes_contribution_id=contribution.supersedes_contribution_id,
        is_owner_correction=contribution.is_owner_correction,
        is_disputed=contribution.is_disputed,
        privacy_scope_snapshot=contribution.privacy_scope_snapshot,
        created_at=contribution.created_at,
    )


def _build_clarification_read(question: MemoryClarificationQuestion) -> ClarificationQuestionRead:
    return ClarificationQuestionRead(
        clarification_id=question.id,
        candidate_id=question.candidate_id,
        question_key=question.question_key,
        question_text=question.question_text,
        language=question.language,
        status=question.status,
        required=question.required,
        asked_at=question.asked_at,
        answered_at=question.answered_at,
        answered_by=question.answered_by,
        answer_contribution_id=question.answer_contribution_id,
    )


def _append_contribution(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
    actor: DemoFamilyActorContext,
    contribution_type: ContributionType,
    contribution_text: str,
    structured_details: dict[str, str] | None,
    language: str | None,
    trace_id: str | None,
    source_message_hash: str | None = None,
    supersedes_contribution_id: int | None = None,
    is_disputed: bool = False,
) -> FamilyMemoryContribution:
    if supersedes_contribution_id is not None and repository.get_contribution(
        db,
        candidate_id=candidate.id,
        contribution_id=supersedes_contribution_id,
    ) is None:
        raise FamilyMemoryInvalidTransitionError("Superseded contribution is invalid")
    normalized_text = normalize_text(contribution_text)
    contribution = repository.create_contribution(
        db,
        candidate_id=candidate.id,
        avatar_id=candidate.avatar_id,
        profile_id=candidate.profile_id,
        actor_id=actor.actor_id,
        actor_user_id=None,
        actor_role=actor.actor_role.value,
        relationship_to_owner=actor.relationship_to_owner,
        contribution_type=contribution_type.value,
        contribution_text=normalized_text,
        structured_details=structured_details or None,
        language=language,
        source_message_hash=source_message_hash or hashlib.sha256(normalized_text.encode("utf-8")).hexdigest(),
        trace_id=trace_id,
        supersedes_contribution_id=supersedes_contribution_id,
        is_owner_correction=contribution_type == ContributionType.OWNER_CORRECTION,
        is_disputed=is_disputed,
        privacy_scope_snapshot=candidate.privacy_scope,
    )
    db.flush()
    observe_memory_contribution_created(role=actor.actor_role.value)
    _translate_contribution_if_czech_origin(db, candidate=candidate, contribution=contribution)
    return contribution


def _get_or_create_next_clarification(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
    contributions: list[FamilyMemoryContribution],
) -> MemoryClarificationQuestion | None:
    spec = next_question_spec(memory_type=candidate.memory_type, contributions=contributions)
    if spec is None:
        return None
    existing = repository.get_clarification_by_key(
        db,
        candidate_id=candidate.id,
        question_key=spec.key,
    )
    if existing is not None:
        return existing if existing.status == ClarificationStatus.PENDING.value else None
    clarification = repository.create_clarification(
        db,
        candidate_id=candidate.id,
        question_key=spec.key,
        question_text=spec.question_text,
        language=candidate.language or "ru",
        status=ClarificationStatus.PENDING.value,
        required=spec.required,
        asked_at=datetime.now(timezone.utc),
    )
    db.flush()
    observe_memory_clarification(status=ClarificationStatus.PENDING.value)
    return clarification


def _finalize_ready_for_review(db: Session, *, candidate: ConversationMemoryCandidate, finalized_by: str) -> None:
    contributions = repository.list_contributions(db, candidate_id=candidate.id)
    draft = build_finalized_draft(candidate=candidate, contributions=contributions)
    candidate.finalized_memory_text = draft.text
    candidate.finalized_at = datetime.now(timezone.utc)
    candidate.finalized_by = finalized_by
    candidate.enrichment_status = EnrichmentStatus.READY_FOR_OWNER_REVIEW.value
    observe_memory_enrichment_status(status=candidate.enrichment_status)
    if draft.has_conflict:
        candidate.dispute_status = DisputeStatus.DISPUTED.value
        observe_memory_dispute(result=candidate.dispute_status)
    _translate_finalized_memory_if_czech_origin(db, candidate=candidate)


def _synchronize_candidate(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
    finalized_by: str,
) -> MemoryClarificationQuestion | None:
    contributions = repository.list_contributions(db, candidate_id=candidate.id)
    missing = missing_required_keys(memory_type=candidate.memory_type, contributions=contributions)
    candidate.unresolved_clarification_count = len(missing)
    candidate.version += 1
    if missing:
        candidate.enrichment_status = EnrichmentStatus.COLLECTING_DETAILS.value
        observe_memory_enrichment_status(status=candidate.enrichment_status)
        return _get_or_create_next_clarification(
            db,
            candidate=candidate,
            contributions=contributions,
        )

    _finalize_ready_for_review(db, candidate=candidate, finalized_by=finalized_by)
    return None


def bypass_mandatory_clarifications_and_finalize(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
    finalized_by: str = "system:ai_biographer_direct_answer",
) -> int:
    """Explicit REPAIR primitive only (Task 65.7C, `avatar_biographer/repair.py`)
    - NOT called from the normal Biographer answer flow. An uncommitted Task
    65.7 draft called this unconditionally on every new answer, silently
    disabling the topic's mandatory clarification bank
    (`CHILDHOOD_MEMORY_QUESTIONS`/`BEDTIME_SONG_QUESTIONS`) for every
    candidate; Task 65.7C removed that call from
    `avatar_biographer/service.answer_question` because it directly
    contradicted the already-committed Task 65.6 mandatory-clarification
    contract. This function itself is preserved, unchanged, as the
    mechanism `repair_stuck_biographer_candidates` uses to force-finalize a
    candidate that is independently confirmed genuinely stuck (age-gated -
    see `avatar_biographer/repair.py`).

    Cancels every still-pending *required* clarification this candidate
    currently has and force-finalizes it using the exact same finalize
    logic `_synchronize_candidate` uses when no required keys are missing.

    Never called for family-contribution or owner-requested-clarification
    flows - those keep the original required-clarification behavior
    unchanged (the owner's "Request more details" review action still
    creates a real, answerable clarification; this function is never
    invoked from that code path). Idempotent: a candidate with no pending
    required clarifications left is finalized again safely (harmless
    no-op on the cancel step, `_finalize_ready_for_review` is itself
    idempotent).

    Returns the number of clarifications cancelled (0 for a candidate that
    had none pending - e.g. a `general`-topic answer, or an already-repaired
    one)."""

    pending = repository.list_pending_required_clarifications(db, candidate_id=candidate.id)
    for clarification in pending:
        clarification.status = ClarificationStatus.CANCELLED.value
        observe_memory_clarification(status=clarification.status)
    candidate.unresolved_clarification_count = 0
    candidate.version += 1
    _finalize_ready_for_review(db, candidate=candidate, finalized_by=finalized_by)
    return len(pending)


def initialize_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    actor: DemoFamilyActorContext,
    initial_text: str,
    trace_id: str | None = None,
    classification_hint_text: str | None = None,
) -> CandidateEnrichmentRead:
    """Create the candidate's first contribution and run the deterministic finalizer.

    ``classification_hint_text`` lets a caller run ``classify_memory_type``
    (a Russian-keyword heuristic) against a different string than the text
    that is actually stored - used by the Czech FA chat path, which
    classifies against the Russian retrieval translation of the message
    while still persisting the original Czech text verbatim as
    ``initial_text``. Defaults to ``initial_text`` (unchanged behavior for
    every existing Russian-origin caller).
    """
    started_at = perf_counter()
    validate_demo_actor(actor)
    candidate = repository.get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        for_update=True,
    )
    if candidate is None:
        raise FamilyMemoryNotFoundError("Family memory candidate not found")
    if candidate.status != "needs_review":
        raise FamilyMemoryInvalidTransitionError("Only needs-review candidates can be enriched")
    if repository.count_contributions(db, candidate_id=candidate.id) == 0:
        candidate.memory_type = classify_memory_type(classification_hint_text or initial_text).value
        candidate.enrichment_status = EnrichmentStatus.DRAFT.value
        candidate.finalized_memory_text = None
        candidate.privacy_scope = "private_owner"
        candidate.dispute_status = DisputeStatus.NONE.value
        _append_contribution(
            db,
            candidate=candidate,
            actor=actor,
            contribution_type=ContributionType.INITIAL_CLAIM,
            contribution_text=initial_text,
            structured_details=initial_structured_details(initial_text),
            language=candidate.language,
            trace_id=trace_id,
        )
    _synchronize_candidate(db, candidate=candidate, finalized_by="system:deterministic-finalizer")
    db.commit()
    db.refresh(candidate)
    log_event(
        logger,
        20,
        "family_memory_enrichment_initialized",
        trace_id=trace_id,
        candidate_id=candidate.id,
        actor_role=actor.actor_role.value,
        enrichment_status=candidate.enrichment_status,
        clarification_status=("pending" if candidate.unresolved_clarification_count else None),
        duration_ms=round((perf_counter() - started_at) * 1000, 2),
    )
    return get_candidate_enrichment(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate.id,
        actor=actor,
    )


def add_contribution(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    payload: FamilyMemoryContributionCreate,
) -> CandidateEnrichmentRead:
    started_at = perf_counter()
    candidate = _get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        actor=payload,
        for_update=True,
    )
    if candidate.status != "needs_review":
        raise FamilyMemoryInvalidTransitionError("Terminal candidate cannot accept contributions")
    if payload.contribution_type in {
        ContributionType.OWNER_CORRECTION,
        ContributionType.OWNER_CONFIRMATION,
    } and not is_demo_owner(payload):
        raise FamilyMemoryAuthorizationError("Owner contribution type requires owner authority")
    if payload.contribution_type == ContributionType.SYSTEM_NORMALIZATION:
        raise FamilyMemoryAuthorizationError("System contribution type is internal only")
    contribution = _append_contribution(
        db,
        candidate=candidate,
        actor=payload,
        contribution_type=payload.contribution_type,
        contribution_text=payload.contribution_text,
        structured_details=(payload.structured_details.model_dump(exclude_none=True) if payload.structured_details else None),
        language=payload.language,
        trace_id=payload.trace_id,
        source_message_hash=payload.source_message_hash,
        supersedes_contribution_id=payload.supersedes_contribution_id,
        is_disputed=payload.is_disputed,
    )
    _synchronize_candidate(db, candidate=candidate, finalized_by="system:deterministic-finalizer")
    db.commit()
    log_event(
        logger,
        20,
        "family_memory_contribution_created",
        trace_id=payload.trace_id,
        candidate_id=candidate.id,
        contribution_id=contribution.id,
        actor_role=payload.actor_role.value,
        enrichment_status=candidate.enrichment_status,
        duration_ms=round((perf_counter() - started_at) * 1000, 2),
    )
    return get_candidate_enrichment(db, owner_user_id=owner_user_id, candidate_id=candidate.id, actor=payload)


def answer_clarification(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    clarification_id: int,
    payload: ClarificationAnswerRequest,
) -> CandidateEnrichmentRead:
    started_at = perf_counter()
    candidate = _get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        actor=payload,
        for_update=True,
    )
    clarification = repository.get_clarification(
        db,
        candidate_id=candidate.id,
        clarification_id=clarification_id,
        for_update=True,
    )
    if clarification is None:
        raise FamilyMemoryNotFoundError("Clarification not found")
    if candidate.status != "needs_review" or clarification.status != ClarificationStatus.PENDING.value:
        raise FamilyMemoryInvalidTransitionError("Clarification cannot be answered")
    details = extract_answer_details(
        question_key=clarification.question_key,
        answer_text=payload.answer_text,
    )
    if payload.structured_details:
        details.update(payload.structured_details.model_dump(exclude_none=True))
    contribution = _append_contribution(
        db,
        candidate=candidate,
        actor=payload,
        contribution_type=ContributionType.CLARIFICATION_ANSWER,
        contribution_text=payload.answer_text,
        structured_details=details,
        language=candidate.language,
        trace_id=payload.trace_id,
    )
    clarification.status = ClarificationStatus.ANSWERED.value
    clarification.answered_at = datetime.now(timezone.utc)
    clarification.answered_by = payload.actor_id
    clarification.answer_contribution_id = contribution.id
    observe_memory_clarification(status=ClarificationStatus.ANSWERED.value)
    _synchronize_candidate(db, candidate=candidate, finalized_by="system:deterministic-finalizer")
    db.commit()
    log_event(
        logger,
        20,
        "family_memory_clarification_answered",
        trace_id=payload.trace_id,
        candidate_id=candidate.id,
        contribution_id=contribution.id,
        actor_role=payload.actor_role.value,
        enrichment_status=candidate.enrichment_status,
        clarification_status=clarification.status,
        duration_ms=round((perf_counter() - started_at) * 1000, 2),
    )
    return get_candidate_enrichment(db, owner_user_id=owner_user_id, candidate_id=candidate.id, actor=payload)


def answer_next_clarification(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    payload: ClarificationAnswerRequest,
) -> CandidateEnrichmentRead:
    candidate = _get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        actor=payload,
    )
    pending = repository.get_next_pending_clarification(
        db,
        candidate_id=candidate.id,
        for_update=True,
    )
    if pending is None:
        raise FamilyMemoryInvalidTransitionError("No pending clarification exists")
    return answer_clarification(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate.id,
        clarification_id=pending.id,
        payload=payload,
    )


def skip_clarification(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    clarification_id: int,
    payload: ClarificationSkipRequest,
) -> CandidateEnrichmentRead:
    started_at = perf_counter()
    candidate = _get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        actor=payload,
        for_update=True,
    )
    clarification = repository.get_clarification(
        db,
        candidate_id=candidate.id,
        clarification_id=clarification_id,
        for_update=True,
    )
    if clarification is None:
        raise FamilyMemoryNotFoundError("Clarification not found")
    if clarification.status != "pending":
        raise FamilyMemoryInvalidTransitionError("Clarification is not pending")
    if clarification.required:
        raise FamilyMemoryInvalidTransitionError("Required clarification cannot be skipped")
    clarification.status = ClarificationStatus.SKIPPED.value
    observe_memory_clarification(status=ClarificationStatus.SKIPPED.value)
    candidate.version += 1
    db.commit()
    log_event(
        logger,
        20,
        "family_memory_clarification_skipped",
        candidate_id=candidate.id,
        actor_role=payload.actor_role.value,
        enrichment_status=candidate.enrichment_status,
        clarification_status=clarification.status,
        duration_ms=round((perf_counter() - started_at) * 1000, 2),
    )
    return get_candidate_enrichment(db, owner_user_id=owner_user_id, candidate_id=candidate.id, actor=payload)


def finalize_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    payload: FinalizeRequest,
) -> CandidateEnrichmentRead:
    started_at = perf_counter()
    candidate = _get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        actor=payload,
        for_update=True,
    )
    if candidate.status != "needs_review":
        raise FamilyMemoryInvalidTransitionError("Terminal candidate cannot be finalized")
    if repository.list_pending_required_clarifications(db, candidate_id=candidate.id):
        raise FamilyMemoryInvalidTransitionError("Required clarifications are unresolved")
    contributions = repository.list_contributions(db, candidate_id=candidate.id)
    if missing_required_keys(memory_type=candidate.memory_type, contributions=contributions):
        raise FamilyMemoryInvalidTransitionError("Required memory details are incomplete")
    draft = build_finalized_draft(candidate=candidate, contributions=contributions)
    candidate.finalized_memory_text = draft.text
    candidate.finalized_at = datetime.now(timezone.utc)
    candidate.finalized_by = payload.actor_id
    candidate.enrichment_status = EnrichmentStatus.READY_FOR_OWNER_REVIEW.value
    candidate.unresolved_clarification_count = 0
    candidate.dispute_status = "disputed" if draft.has_conflict else candidate.dispute_status
    candidate.version += 1
    _translate_finalized_memory_if_czech_origin(db, candidate=candidate)
    db.commit()
    log_event(
        logger,
        20,
        "family_memory_finalized",
        candidate_id=candidate.id,
        actor_role=payload.actor_role.value,
        enrichment_status=candidate.enrichment_status,
        duration_ms=round((perf_counter() - started_at) * 1000, 2),
    )
    return get_candidate_enrichment(db, owner_user_id=owner_user_id, candidate_id=candidate.id, actor=payload)


def owner_review(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    payload: OwnerReviewRequest,
) -> OwnerReviewResponse:
    started_at = perf_counter()
    validate_demo_actor(payload)
    if not is_demo_owner(payload):
        raise FamilyMemoryAuthorizationError("Only the avatar owner can complete owner review")
    candidate = repository.get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        for_update=True,
    )
    if candidate is None:
        raise FamilyMemoryNotFoundError("Family memory candidate not found")
    if candidate.status != "needs_review":
        raise FamilyMemoryInvalidTransitionError("Candidate review is already terminal")
    if payload.privacy_scope is not None:
        candidate.privacy_scope = payload.privacy_scope.value

    now = datetime.now(timezone.utc)
    action = payload.action
    observe_memory_owner_review(action=action.value)
    promotion = None
    promotion_created = False
    if action == OwnerReviewAction.REQUEST_MORE_DETAILS:
        candidate.enrichment_status = EnrichmentStatus.COLLECTING_DETAILS.value
        candidate.finalized_memory_text = None
        candidate.finalized_at = None
        candidate.version += 1
        repository.create_clarification(
            db,
            candidate_id=candidate.id,
            question_key=f"owner_request_{candidate.version}",
            question_text=payload.review_note
            or _localized_default_text(_DEFAULT_REQUEST_MORE_DETAILS_TEXT, language=candidate.language),
            language=candidate.language or "ru",
            status="pending",
            required=True,
            asked_at=now,
        )
        db.flush()
        observe_memory_clarification(status=ClarificationStatus.PENDING.value)
        candidate.unresolved_clarification_count += 1
    elif action == OwnerReviewAction.MARK_DISPUTED:
        candidate.dispute_status = DisputeStatus.DISPUTED.value
        observe_memory_dispute(result=candidate.dispute_status)
        candidate.version += 1
        _append_contribution(
            db,
            candidate=candidate,
            actor=payload,
            contribution_type=ContributionType.DISPUTE_STATEMENT,
            contribution_text=payload.review_note
            or _localized_default_text(_DEFAULT_DISPUTE_TEXT, language=candidate.language),
            structured_details=None,
            language=candidate.language,
            trace_id=None,
            is_disputed=True,
        )
    elif action == OwnerReviewAction.REJECT:
        candidate.status = "rejected"
        candidate.reviewed_at = now
        candidate.review_note = payload.review_note
        candidate.rejection_reason = payload.rejection_reason
    else:
        if candidate.enrichment_status != "ready_for_owner_review":
            raise FamilyMemoryInvalidTransitionError("Candidate is not ready for owner review")
        if candidate.unresolved_clarification_count or repository.list_pending_required_clarifications(
            db, candidate_id=candidate.id
        ):
            raise FamilyMemoryInvalidTransitionError("Required clarifications are unresolved")
        if action == OwnerReviewAction.EDIT_AND_CONFIRM:
            if not payload.finalized_memory_text:
                raise FamilyMemoryInvalidTransitionError("Edited finalized memory text is required")
            previous = candidate.finalized_memory_text
            _append_contribution(
                db,
                candidate=candidate,
                actor=payload,
                contribution_type=ContributionType.OWNER_CORRECTION,
                contribution_text=payload.finalized_memory_text,
                structured_details={"owner_perspective": payload.finalized_memory_text, "additional_notes": f"Previous draft: {previous or 'none'}"},
                language=candidate.language,
                trace_id=None,
            )
            candidate.finalized_memory_text = payload.finalized_memory_text
            candidate.finalized_at = now
            candidate.finalized_by = payload.actor_id
            candidate.dispute_status = DisputeStatus.RESOLVED.value
            observe_memory_dispute(result=candidate.dispute_status)
            _translate_finalized_memory_if_czech_origin(db, candidate=candidate)
        elif action == OwnerReviewAction.APPROVE_MULTIPLE_PERSPECTIVES:
            if candidate.dispute_status != "disputed":
                raise FamilyMemoryInvalidTransitionError("Candidate has no unresolved dispute")
            if (
                payload.finalized_memory_text
                and payload.finalized_memory_text != candidate.finalized_memory_text
            ):
                _append_contribution(
                    db,
                    candidate=candidate,
                    actor=payload,
                    contribution_type=ContributionType.OWNER_CORRECTION,
                    contribution_text=payload.finalized_memory_text,
                    structured_details={"owner_perspective": payload.finalized_memory_text},
                    language=candidate.language,
                    trace_id=None,
                )
                candidate.finalized_memory_text = payload.finalized_memory_text
                candidate.finalized_at = now
                candidate.finalized_by = payload.actor_id
                _translate_finalized_memory_if_czech_origin(db, candidate=candidate)
            if not candidate.finalized_memory_text or not any(
                marker in candidate.finalized_memory_text.casefold()
                for marker in (
                    "указывает",
                    "вспоминает",
                    "точка зрения",
                    "спор",
                    "uvádí",
                    "vzpomíná",
                    "pohled",
                    "spor",
                )
            ):
                raise FamilyMemoryInvalidTransitionError("Attributed multiple-perspective text is required")
            candidate.dispute_status = DisputeStatus.RESOLVED.value
            observe_memory_dispute(result=candidate.dispute_status)
        elif candidate.dispute_status == "disputed":
            raise FamilyMemoryInvalidTransitionError("Disputed memory requires explicit resolution")

        _append_contribution(
            db,
            candidate=candidate,
            actor=payload,
            contribution_type=ContributionType.OWNER_CONFIRMATION,
            contribution_text=payload.review_note
            or _localized_default_text(_DEFAULT_OWNER_CONFIRMATION_TEXT, language=candidate.language),
            structured_details=None,
            language=candidate.language,
            trace_id=None,
        )
        candidate.status = "approved"
        candidate.reviewed_at = now
        candidate.review_note = payload.review_note
        candidate.rejection_reason = None
        candidate.owner_reviewed_at = now
        candidate.owner_reviewed_by = payload.actor_id
        candidate.owner_review_actor_role = FamilyMemoryActorRole.OWNER.value
        candidate.review_authority_source = "demo_internal_actor"
        candidate.version += 1
        if candidate.privacy_scope in INDEXABLE_PRIVACY_SCOPES:
            assert_candidate_eligible_for_promotion(db, candidate=candidate)
            outcome = promotion_service.create_or_get_promotion_for_candidate(db, candidate=candidate)
            promotion = outcome.promotion
            promotion_created = outcome.created

    if action in {
        OwnerReviewAction.REJECT,
        OwnerReviewAction.REQUEST_MORE_DETAILS,
        OwnerReviewAction.MARK_DISPUTED,
    }:
        candidate.owner_reviewed_at = now
        candidate.owner_reviewed_by = payload.actor_id
        candidate.owner_review_actor_role = FamilyMemoryActorRole.OWNER.value
        candidate.review_authority_source = "demo_internal_actor"
    db.commit()
    db.refresh(candidate)
    log_event(
        logger,
        20,
        "family_memory_owner_reviewed",
        candidate_id=candidate.id,
        actor_role=payload.actor_role.value,
        enrichment_status=candidate.enrichment_status,
        review_action=action.value,
        promotion_status=promotion.promotion_status if promotion is not None else None,
        dispute_status=candidate.dispute_status,
        duration_ms=round((perf_counter() - started_at) * 1000, 2),
    )
    response = get_candidate_enrichment(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate.id,
        actor=payload,
    )
    if promotion is not None:
        response.promotion_id = promotion.id
        response.promotion_status = promotion.promotion_status
        response.searchable_as_fact = promotion.promotion_status == "indexed"
        response.explicit_indexing_required = promotion.promotion_status == "pending_index"
    return OwnerReviewResponse(**response.model_dump(), promotion_created=promotion_created)


def get_candidate_enrichment(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    actor: DemoFamilyActorContext,
) -> CandidateEnrichmentRead:
    candidate = _get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
        actor=actor,
    )
    contributions = repository.list_contributions(db, candidate_id=candidate.id)
    next_question = next(
        (item for item in repository.list_clarifications(db, candidate_id=candidate.id) if item.status == "pending"),
        None,
    )
    promotion = candidate.avatar_memory_promotion
    return CandidateEnrichmentRead(
        candidate_id=candidate.id,
        avatar_id=candidate.avatar_id,
        profile_id=candidate.profile_id,
        memory_type=candidate.memory_type,
        enrichment_status=candidate.enrichment_status,
        review_status=candidate.status,
        dispute_status=candidate.dispute_status,
        privacy_scope=candidate.privacy_scope,
        unresolved_clarification_count=candidate.unresolved_clarification_count,
        finalized_memory_text=candidate.finalized_memory_text,
        finalized_at=candidate.finalized_at,
        finalized_by=candidate.finalized_by,
        owner_reviewed_at=candidate.owner_reviewed_at,
        owner_reviewed_by=candidate.owner_reviewed_by,
        contribution_count=len(contributions),
        next_clarification_question=(
            _build_clarification_read(next_question) if next_question is not None else None
        ),
        promotion_id=promotion.id if promotion is not None else None,
        promotion_status=promotion.promotion_status if promotion is not None else None,
        searchable_as_fact=bool(promotion and promotion.promotion_status == "indexed"),
        explicit_indexing_required=bool(promotion and promotion.promotion_status == "pending_index"),
    )


def list_contributions(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    actor: DemoFamilyActorContext,
) -> list[FamilyMemoryContributionRead]:
    candidate = repository.get_candidate(db, owner_user_id=owner_user_id, candidate_id=candidate_id)
    if candidate is None:
        raise FamilyMemoryNotFoundError("Family memory candidate not found")
    validate_demo_actor(actor)
    contributions = repository.list_contributions(db, candidate_id=candidate.id)
    if is_demo_owner(actor):
        visible = contributions
    elif candidate.privacy_scope in BROAD_VISIBILITY_PRIVACY_SCOPES:
        visible = contributions
    else:
        visible = [item for item in contributions if item.actor_id == actor.actor_id]
    if not visible and not _can_view_candidate(candidate, actor):
        raise FamilyMemoryNotFoundError("Family memory candidate not found")
    return [_build_contribution_read(item) for item in visible]


def list_clarifications(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    actor: DemoFamilyActorContext,
) -> list[ClarificationQuestionRead]:
    candidate = _get_candidate(
        db, owner_user_id=owner_user_id, candidate_id=candidate_id, actor=actor
    )
    return [
        _build_clarification_read(item)
        for item in repository.list_clarifications(db, candidate_id=candidate.id)
    ]

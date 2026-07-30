"""Authenticated, membership-checked entry point onto the existing
conversation-memory-candidate / family-memory-enrichment / avatar-memory-
promotion / avatar-memory-indexing pipeline (Task 65.2).

This module intentionally contains almost no domain logic of its own - it
resolves real authorization (`resolve_authorized_profile`, never a client-
supplied role) and then calls straight into the already-implemented,
already-tested service functions in `conversation_memory_candidates`,
`family_memory_enrichment`, `avatar_memory_promotions`, and
`avatar_memory_indexing`, exactly as the previously-demo-only
`app.modules.demo_fa_chat.router` does for its own (unauthenticated) surface.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.avatar_memory_indexing import repository as avatar_memory_indexing_repository
from app.modules.avatar_memory_indexing.schemas import AvatarMemoryIndexingRead
from app.modules.avatar_memory_indexing.service import enqueue_indexing_job
from app.modules.job_tracking.exceptions import (
    GlobalQueueSaturationError,
    PerProfileActiveJobLimitExceededError,
    PerUserActiveJobLimitExceededError,
)
from app.modules.avatar_memory_promotions.service import list_biography_memory_entries
from app.modules.family_memory_enrichment.clarification import localize_question_text
from app.modules.family_memory_enrichment.eligibility import FamilyMemoryEligibilityError
from app.modules.conversation_memory_candidates.service import (
    ConversationMemoryCandidateNotFoundError,
    list_candidates as list_conversation_candidates,
)
from app.modules.family_memory_enrichment.enums import FamilyMemoryActorRole
from app.modules.family_memory_enrichment.schemas import (
    CandidateEnrichmentRead,
    ClarificationAnswerRequest,
    ClarificationSkipRequest,
    DemoFamilyActorContext,
    OwnerReviewRequest,
    OwnerReviewResponse,
)
from app.modules.family_memory_enrichment.service import (
    FamilyMemoryAuthorizationError,
    FamilyMemoryInvalidTransitionError,
    FamilyMemoryNotFoundError,
    answer_next_clarification,
    get_candidate_enrichment,
    list_clarifications,
    list_contributions,
    owner_review,
    skip_clarification,
)
from app.modules.memorial_access.capabilities import MemorialCapability, resolve_authorized_profile
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError
from app.modules.memorial_candidates.schemas import (
    BiographyMemoryEntryRead,
    CandidateHistoryRead,
    ClarificationAnswerBody,
    OwnerReviewBody,
)


router = APIRouter(tags=["memorial-candidates"])
ProfileIdPath = Annotated[int, Path(gt=0)]
CandidateIdPath = Annotated[int, Path(gt=0)]
ClarificationIdPath = Annotated[int, Path(gt=0)]

_ROLE_TO_ACTOR_ROLE = {
    "owner": FamilyMemoryActorRole.OWNER,
    "trusted_reviewer": FamilyMemoryActorRole.TRUSTED_REVIEWER,
    "contributor": FamilyMemoryActorRole.CONTRIBUTOR,
}


def _raise_access_error(exc: Exception) -> None:
    if isinstance(exc, MemorialNotFoundError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    if isinstance(exc, MemorialForbiddenError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    raise exc


#: Task 65.7 (Part D.42/12): every candidate/clarification endpoint below
#: accepts this as an explicit query parameter and threads it through -
#: never inferred from the record's own stored `language`/`question.language`
#: (that reflects who *originally answered*, not who is *currently
#: viewing*). Defaults to "cs" only because that matches every other
#: locale-aware endpoint's default in this codebase (Biographer's own
#: `next-question` has no default and requires the caller to pass one; this
#: endpoint family predates that convention and already shipped without a
#: locale param, so a default keeps it backward compatible for any existing
#: caller that doesn't pass one yet).
CandidateLocaleQuery = Annotated[str, Query(pattern="^(cs|ru)$")]


def _localize_enrichment(enrichment: CandidateEnrichmentRead, *, viewer_locale: str) -> CandidateEnrichmentRead:
    """`family_memory_enrichment._build_clarification_read` (existing,
    untouched code) always returns the canonical Russian `question_text` -
    re-localized here for display using the CURRENT VIEWER's chosen UI
    locale (`viewer_locale`), never the candidate's/question's own stored
    `language` (which only reflects whichever locale the original answerer
    happened to have selected at write time, and can therefore permanently
    disagree with a *different, later* viewer's own chosen UI language -
    the exact mechanism that let raw Russian clarification text leak into a
    Czech-locale UI, Task 65.7)."""

    question = enrichment.next_clarification_question
    if question is not None:
        question.question_text = localize_question_text(
            question_key=question.question_key,
            source_text=question.question_text,
            locale=viewer_locale,
        )
    return enrichment


def _actor_context(*, current_user: User, role: str) -> DemoFamilyActorContext:
    actor_role = _ROLE_TO_ACTOR_ROLE.get(role)
    if actor_role is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient memorial permissions")
    return DemoFamilyActorContext(actor_id=str(current_user.id), actor_role=actor_role)


def _resolve_profile(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    capability: MemorialCapability,
):
    try:
        return resolve_authorized_profile(db, current_user=current_user, profile_id=profile_id, capability=capability)
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
        raise  # unreachable, satisfies type checkers


@router.get(
    "/api/memorials/{profile_id}/candidates",
    response_model=list[CandidateEnrichmentRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_candidates_endpoint(
    profile_id: ProfileIdPath,
    locale: CandidateLocaleQuery = "cs",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[CandidateEnrichmentRead]:
    """Owner/trusted_reviewer only - a full cross-actor candidate list has no
    per-item visibility filtering today (unlike `get_candidate_enrichment`,
    which reuses the existing actor-based visibility check). A contributor
    still learns their own `candidate_id` directly from the biographer
    answer response and can fetch that one candidate's enrichment."""

    profile, membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.REVIEW_CONTRIBUTION,
    )
    actor = _actor_context(current_user=current_user, role=membership.role)
    candidates = list_conversation_candidates(db, owner_user_id=profile.user_id, profile_id=profile.id)
    results: list[CandidateEnrichmentRead] = []
    for candidate in candidates:
        try:
            results.append(
                _localize_enrichment(
                    get_candidate_enrichment(db, owner_user_id=profile.user_id, candidate_id=candidate.id, actor=actor),
                    viewer_locale=locale,
                )
            )
        except FamilyMemoryNotFoundError:
            # Not visible to this actor's real role/privacy scope (e.g. a
            # trusted_reviewer and a `private_owner`-scoped candidate) -
            # excluded from the list rather than surfaced as a 500.
            continue
    return results


@router.get(
    "/api/memorials/{profile_id}/biography/memory-entries",
    response_model=list[BiographyMemoryEntryRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_biography_memory_entries_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[BiographyMemoryEntryRead]:
    """Task 65.6.1 (Part E) - approved, promoted candidate memories
    projected into the Biography tab, separate from the manually-authored
    `biography` free-text field. Read-only; never mutates the biography
    text and never surfaces a pending/rejected/archived draft."""

    profile, _membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.VIEW_MEMORIAL,
    )
    entries = list_biography_memory_entries(
        db,
        owner_user_id=profile.user_id,
        profile_id=profile.id,
        viewer_is_profile_owner=current_user.id == profile.user_id,
    )
    return [
        BiographyMemoryEntryRead(
            promotion_id=promotion.id,
            candidate_id=promotion.candidate_id,
            text=promotion.approved_memory_text,
            privacy_scope=promotion.candidate.privacy_scope,
            promotion_status=promotion.promotion_status,
            searchable_as_fact=promotion.promotion_status == "indexed",
            created_at=promotion.created_at,
            indexed_at=promotion.indexed_at,
        )
        for promotion in entries
    ]


@router.get(
    "/api/memorials/{profile_id}/candidates/{candidate_id}",
    response_model=CandidateEnrichmentRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_candidate_endpoint(
    profile_id: ProfileIdPath,
    candidate_id: CandidateIdPath,
    locale: CandidateLocaleQuery = "cs",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CandidateEnrichmentRead:
    profile, membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.SUBMIT_CONTRIBUTION,
    )
    actor = _actor_context(current_user=current_user, role=membership.role)
    try:
        return _localize_enrichment(
            get_candidate_enrichment(db, owner_user_id=profile.user_id, candidate_id=candidate_id, actor=actor),
            viewer_locale=locale,
        )
    except (FamilyMemoryNotFoundError, ConversationMemoryCandidateNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/api/memorials/{profile_id}/candidates/{candidate_id}/history",
    response_model=CandidateHistoryRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_candidate_history_endpoint(
    profile_id: ProfileIdPath,
    candidate_id: CandidateIdPath,
    locale: CandidateLocaleQuery = "cs",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CandidateHistoryRead:
    """Task 65.4: the append-only contribution/clarification history behind
    one candidate, for the Review-tab candidate-detail view. Gated behind
    the exact same actor-visibility check `get_candidate_enrichment` already
    applies (a `private_owner`-scoped candidate invisible to a
    trusted_reviewer via the list/detail endpoints stays invisible here
    too) - no new authorization logic, only new read composition."""

    profile, membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.SUBMIT_CONTRIBUTION,
    )
    actor = _actor_context(current_user=current_user, role=membership.role)
    try:
        enrichment = _localize_enrichment(
            get_candidate_enrichment(db, owner_user_id=profile.user_id, candidate_id=candidate_id, actor=actor),
            viewer_locale=locale,
        )
        contributions = list_contributions(
            db, owner_user_id=profile.user_id, candidate_id=candidate_id, actor=actor
        )
        clarifications = list_clarifications(
            db, owner_user_id=profile.user_id, candidate_id=candidate_id, actor=actor
        )
    except (FamilyMemoryNotFoundError, ConversationMemoryCandidateNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    # Task 65.7: the append-only history view must never show a stale-
    # locale clarification question either - same viewer-locale projection
    # as the "current" clarification above, applied to every historical row.
    for clarification in clarifications:
        clarification.question_text = localize_question_text(
            question_key=clarification.question_key,
            source_text=clarification.question_text,
            locale=locale,
        )
    return CandidateHistoryRead(
        candidate=enrichment,
        contributions=contributions,
        clarifications=clarifications,
    )


@router.post(
    "/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/answer",
    response_model=CandidateEnrichmentRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def answer_next_clarification_endpoint(
    profile_id: ProfileIdPath,
    candidate_id: CandidateIdPath,
    payload: ClarificationAnswerBody,
    locale: CandidateLocaleQuery = "cs",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CandidateEnrichmentRead:
    profile, membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.SUBMIT_CONTRIBUTION,
    )
    actor_role = _ROLE_TO_ACTOR_ROLE.get(membership.role)
    if actor_role is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient memorial permissions")
    request = ClarificationAnswerRequest(
        actor_id=str(current_user.id),
        actor_role=actor_role,
        answer_text=payload.answer_text,
        structured_details=payload.structured_details,
    )
    try:
        return _localize_enrichment(
            answer_next_clarification(db, owner_user_id=profile.user_id, candidate_id=candidate_id, payload=request),
            viewer_locale=locale,
        )
    except (FamilyMemoryNotFoundError, ConversationMemoryCandidateNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except FamilyMemoryInvalidTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc


@router.post(
    "/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/{clarification_id}/skip",
    response_model=CandidateEnrichmentRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def skip_clarification_endpoint(
    profile_id: ProfileIdPath,
    candidate_id: CandidateIdPath,
    clarification_id: ClarificationIdPath,
    locale: CandidateLocaleQuery = "cs",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CandidateEnrichmentRead:
    profile, membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.SUBMIT_CONTRIBUTION,
    )
    actor_role = _ROLE_TO_ACTOR_ROLE.get(membership.role)
    if actor_role is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient memorial permissions")
    request = ClarificationSkipRequest(actor_id=str(current_user.id), actor_role=actor_role)
    try:
        return _localize_enrichment(
            skip_clarification(
                db,
                owner_user_id=profile.user_id,
                candidate_id=candidate_id,
                clarification_id=clarification_id,
                payload=request,
            ),
            viewer_locale=locale,
        )
    except (FamilyMemoryNotFoundError, ConversationMemoryCandidateNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except FamilyMemoryInvalidTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
    response_model=OwnerReviewResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def owner_review_endpoint(
    profile_id: ProfileIdPath,
    candidate_id: CandidateIdPath,
    payload: OwnerReviewBody,
    locale: CandidateLocaleQuery = "cs",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> OwnerReviewResponse:
    # `family_memory_enrichment.owner_review` only ever grants authority to
    # `actor_role == owner` (see `is_demo_owner`) - trusted_reviewer is
    # intentionally not extended here, matching that existing, already-
    # tested hard requirement rather than modifying it for this task.
    profile, membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.MANAGE_MEMORIAL,
    )
    if membership.role != "owner":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only the memorial owner can review")
    request = OwnerReviewRequest(
        actor_id=str(current_user.id),
        actor_role=FamilyMemoryActorRole.OWNER,
        action=payload.action,
        finalized_memory_text=payload.finalized_memory_text,
        privacy_scope=payload.privacy_scope,
        review_note=payload.review_note,
        rejection_reason=payload.rejection_reason,
    )
    try:
        response = owner_review(db, owner_user_id=profile.user_id, candidate_id=candidate_id, payload=request)
        _localize_enrichment(response, viewer_locale=locale)
        return response
    except (FamilyMemoryNotFoundError, ConversationMemoryCandidateNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except FamilyMemoryInvalidTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    except FamilyMemoryEligibilityError as exc:
        # Task 65.6.1 (Part C): before this fix, a candidate that failed
        # promotion eligibility at the exact moment of approval (e.g. a
        # Czech-origin candidate whose Russian translation is still
        # pending/failed) raised this uncaught, producing a raw 500 with no
        # indication of why - `owner_review`'s approval-state mutation and
        # its promotion-creation attempt share one DB transaction, so the
        # candidate correctly stays `needs_review` (the whole transaction
        # rolls back together; nothing is left half-applied), but the
        # owner had no way to know that, or why, without reading server
        # logs. Surfacing this as a clear 400 with the concrete block
        # reason lets the owner retry the same approval once the blocking
        # condition clears (e.g. the translation finishes) - "clear errors
        # and safe failure modes" instead of an opaque server error.
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"promotion_blocked:{exc.reason}") from exc


@router.post(
    "/api/memorials/{profile_id}/candidates/{candidate_id}/index",
    response_model=AvatarMemoryIndexingRead,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_413_REQUEST_ENTITY_TOO_LARGE: {"model": ErrorResponse},
        status.HTTP_429_TOO_MANY_REQUESTS: {"model": ErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse},
    },
)
def index_candidate_memory_endpoint(
    profile_id: ProfileIdPath,
    candidate_id: CandidateIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> AvatarMemoryIndexingRead:
    """Explicit indexing button: never runs automatically after approval.
    Approval (`owner_review` confirm/edit_and_confirm/approve_multiple_
    perspectives) only ever creates a `pending_index` promotion; this is
    the separate, owner-triggered step that requests indexing. Also
    doubles as the retry action for a `failed` promotion (idempotent).

    Task 65.9 (Part I): this used to call `index_promotion` directly here
    - a real BGE-M3 encode and Qdrant write running inside the HTTP
    request/FastAPI process. It now only authorizes, creates/reuses the
    persistent job and its transactional outbox record, and returns 202
    with the promotion's current (not-yet-confirmed) state - the encoder
    and Qdrant write happen only inside the Celery embedding-worker task
    (see `app.worker.tasks.run_avatar_memory_indexing_job`)."""

    profile, membership = _resolve_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.TRIGGER_INDEXING,
    )
    actor = DemoFamilyActorContext(actor_id=str(current_user.id), actor_role=FamilyMemoryActorRole.OWNER)
    try:
        enrichment = get_candidate_enrichment(db, owner_user_id=profile.user_id, candidate_id=candidate_id, actor=actor)
    except (FamilyMemoryNotFoundError, ConversationMemoryCandidateNotFoundError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    if enrichment.promotion_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Candidate has not been approved for indexing yet",
        )

    promotion = avatar_memory_indexing_repository.get_promotion_for_owner(
        db,
        owner_user_id=profile.user_id,
        promotion_id=enrichment.promotion_id,
    )
    if promotion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avatar memory promotion not found")
    if promotion.promotion_status not in {"pending_index", "failed", "indexed"}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Promotion status `{promotion.promotion_status}` is not eligible for indexing",
        )

    if promotion.promotion_status == "indexed":
        # Idempotent no-op: already confirmed searchable, nothing to
        # (re)queue - never re-runs the encoder for an already-indexed
        # promotion just because the button was clicked again.
        return AvatarMemoryIndexingRead(
            promotion_id=promotion.id,
            promotion_status=promotion.promotion_status,
            indexed_at=promotion.indexed_at,
            target_collection_name=promotion.target_collection_name,
            qdrant_point_id=promotion.qdrant_point_id,
            searchable_as_fact=True,
            result="already_indexed",
            job_id=None,
        )

    if promotion.promotion_status == "failed":
        # Retry: reactivate to pending so the projection reads "pending",
        # never a stale "failed", while the new job is in flight.
        promotion.promotion_status = "pending_index"
        db.commit()

    try:
        background_job = enqueue_indexing_job(db, profile=profile, promotion=promotion)
    except (PerUserActiveJobLimitExceededError, PerProfileActiveJobLimitExceededError) as exc:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=str(exc)) from exc
    except GlobalQueueSaturationError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
            headers={"Retry-After": str(exc.retry_after_seconds)},
        ) from exc

    db.refresh(promotion)
    return AvatarMemoryIndexingRead(
        promotion_id=promotion.id,
        promotion_status=promotion.promotion_status,
        indexed_at=promotion.indexed_at,
        target_collection_name=promotion.target_collection_name,
        qdrant_point_id=promotion.qdrant_point_id,
        searchable_as_fact=False,
        result="queued",
        job_id=background_job.id,
    )

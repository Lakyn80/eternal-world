from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import ConversationMemoryCandidate
from app.modules.demo_fa_chat.service import _resolve_demo_avatar_persona, _resolve_demo_profile
from app.modules.family_memory_enrichment.enums import FamilyMemoryActorRole
from app.modules.family_memory_enrichment.eligibility import FamilyMemoryEligibilityError
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
from app.modules.family_memory_enrichment.service import (
    FamilyMemoryAuthorizationError,
    FamilyMemoryInvalidTransitionError,
    FamilyMemoryNotFoundError,
    add_contribution,
    answer_clarification,
    finalize_candidate,
    get_candidate_enrichment,
    list_clarifications,
    list_contributions,
    owner_review,
    skip_clarification,
)


router = APIRouter(prefix="/api/demo/fa-chat/memory-candidates", tags=["family-memory-enrichment"])
CandidateIdPath = Annotated[int, Path(gt=0)]
ClarificationIdPath = Annotated[int, Path(gt=0)]


def get_demo_actor_context(
    actor_id: str = Query(min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole = Query(),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
) -> DemoFamilyActorContext:
    return DemoFamilyActorContext(
        actor_id=actor_id,
        actor_role=actor_role,
        relationship_to_owner=relationship_to_owner,
    )


def _resolve_candidate_scope(db: Session, candidate_id: int) -> tuple[int, int]:
    resolved = _resolve_demo_profile(db, profile_id=None)
    persona = _resolve_demo_avatar_persona()
    candidate = db.get(ConversationMemoryCandidate, candidate_id)
    if (
        candidate is None
        or candidate.owner_user_id != resolved.user.id
        or candidate.profile_id != resolved.profile.id
        or candidate.avatar_id != persona.avatar_id
    ):
        raise FamilyMemoryNotFoundError("Family memory candidate not found")
    return resolved.user.id, resolved.profile.id


def _raise_http(exc: Exception) -> None:
    if isinstance(exc, FamilyMemoryAuthorizationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Actor is not authorized for this action") from exc
    if isinstance(exc, FamilyMemoryNotFoundError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Family memory candidate not found") from exc
    if isinstance(exc, FamilyMemoryInvalidTransitionError):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Family memory action is not allowed in the current state") from exc
    if isinstance(exc, FamilyMemoryEligibilityError):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Family memory is not eligible for promotion: {exc.reason}",
        ) from exc
    raise exc


@router.get("/{candidate_id}/enrichment", response_model=CandidateEnrichmentRead)
def get_enrichment_endpoint(
    candidate_id: CandidateIdPath,
    actor: DemoFamilyActorContext = Depends(get_demo_actor_context),
    db: Session = Depends(get_db),
) -> CandidateEnrichmentRead:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return get_candidate_enrichment(db, owner_user_id=owner_user_id, candidate_id=candidate_id, actor=actor)
    except Exception as exc:
        _raise_http(exc)


@router.get("/{candidate_id}/contributions", response_model=list[FamilyMemoryContributionRead])
def list_contributions_endpoint(
    candidate_id: CandidateIdPath,
    actor: DemoFamilyActorContext = Depends(get_demo_actor_context),
    db: Session = Depends(get_db),
) -> list[FamilyMemoryContributionRead]:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return list_contributions(db, owner_user_id=owner_user_id, candidate_id=candidate_id, actor=actor)
    except Exception as exc:
        _raise_http(exc)


@router.get("/{candidate_id}/clarifications", response_model=list[ClarificationQuestionRead])
def list_clarifications_endpoint(
    candidate_id: CandidateIdPath,
    actor: DemoFamilyActorContext = Depends(get_demo_actor_context),
    db: Session = Depends(get_db),
) -> list[ClarificationQuestionRead]:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return list_clarifications(db, owner_user_id=owner_user_id, candidate_id=candidate_id, actor=actor)
    except Exception as exc:
        _raise_http(exc)


@router.post("/{candidate_id}/contributions", response_model=CandidateEnrichmentRead)
def add_contribution_endpoint(
    candidate_id: CandidateIdPath,
    payload: FamilyMemoryContributionCreate,
    db: Session = Depends(get_db),
) -> CandidateEnrichmentRead:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return add_contribution(db, owner_user_id=owner_user_id, candidate_id=candidate_id, payload=payload)
    except Exception as exc:
        _raise_http(exc)


@router.get("/{candidate_id}/clarifications/next", response_model=ClarificationQuestionRead | None)
def next_clarification_endpoint(
    candidate_id: CandidateIdPath,
    actor: DemoFamilyActorContext = Depends(get_demo_actor_context),
    db: Session = Depends(get_db),
) -> ClarificationQuestionRead | None:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        enrichment = get_candidate_enrichment(
            db, owner_user_id=owner_user_id, candidate_id=candidate_id, actor=actor
        )
        return enrichment.next_clarification_question
    except Exception as exc:
        _raise_http(exc)


@router.post("/{candidate_id}/clarifications/{clarification_id}/answer", response_model=CandidateEnrichmentRead)
def answer_clarification_endpoint(
    candidate_id: CandidateIdPath,
    clarification_id: ClarificationIdPath,
    payload: ClarificationAnswerRequest,
    db: Session = Depends(get_db),
) -> CandidateEnrichmentRead:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return answer_clarification(
            db,
            owner_user_id=owner_user_id,
            candidate_id=candidate_id,
            clarification_id=clarification_id,
            payload=payload,
        )
    except Exception as exc:
        _raise_http(exc)


@router.post("/{candidate_id}/clarifications/{clarification_id}/skip", response_model=CandidateEnrichmentRead)
def skip_clarification_endpoint(
    candidate_id: CandidateIdPath,
    clarification_id: ClarificationIdPath,
    payload: ClarificationSkipRequest,
    db: Session = Depends(get_db),
) -> CandidateEnrichmentRead:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return skip_clarification(
            db,
            owner_user_id=owner_user_id,
            candidate_id=candidate_id,
            clarification_id=clarification_id,
            payload=payload,
        )
    except Exception as exc:
        _raise_http(exc)


@router.post("/{candidate_id}/finalize", response_model=CandidateEnrichmentRead)
def finalize_endpoint(
    candidate_id: CandidateIdPath,
    payload: FinalizeRequest,
    db: Session = Depends(get_db),
) -> CandidateEnrichmentRead:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return finalize_candidate(db, owner_user_id=owner_user_id, candidate_id=candidate_id, payload=payload)
    except Exception as exc:
        _raise_http(exc)


@router.post("/{candidate_id}/owner-review", response_model=OwnerReviewResponse)
def owner_review_endpoint(
    candidate_id: CandidateIdPath,
    payload: OwnerReviewRequest,
    db: Session = Depends(get_db),
) -> OwnerReviewResponse:
    try:
        owner_user_id, _ = _resolve_candidate_scope(db, candidate_id)
        return owner_review(db, owner_user_id=owner_user_id, candidate_id=candidate_id, payload=payload)
    except Exception as exc:
        _raise_http(exc)

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from app.core.logging import get_request_id
from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.avatar_biographer.resume import get_resume_state
from app.modules.avatar_biographer.schemas import (
    BiographerAnswerRequest,
    BiographerAnswerResponse,
    BiographerEligibilityRead,
    BiographerQuestionRead,
    BiographerResumeRead,
)
from app.modules.avatar_biographer.service import (
    BiographerBlockedError,
    BiographerConflictError,
    BiographerNotFoundError,
    answer_question,
    get_eligibility,
    get_next_question,
    postpone_question,
    skip_question,
)
from app.modules.family_memory_enrichment.enums import FamilyMemoryActorRole
from app.modules.memorial_access.capabilities import MemorialCapability, resolve_authorized_profile
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError


router = APIRouter(tags=["avatar-biographer"])
ProfileIdPath = Annotated[int, Path(gt=0)]
QuestionIdPath = Annotated[int, Path(gt=0)]

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


@router.get(
    "/api/memorials/{profile_id}/biographer/eligibility",
    response_model=BiographerEligibilityRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_biographer_eligibility_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographerEligibilityRead:
    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.SUBMIT_CONTRIBUTION,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    return get_eligibility(db, profile=profile)


@router.get(
    "/api/memorials/{profile_id}/biographer/resume",
    response_model=BiographerResumeRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_biographer_resume_endpoint(
    profile_id: ProfileIdPath,
    # Task 65.10.1: defaults to "cs" for the same backward-compatibility
    # reason `CandidateLocaleQuery` does in `memorial_candidates.router` -
    # this endpoint shipped without a locale param and the resume state
    # previously never returned any viewer-facing clarification text of its
    # own to localize.
    locale: str = Query(default="cs", pattern="^(cs|en|ru)$"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographerResumeRead:
    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.SUBMIT_CONTRIBUTION,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    state = get_resume_state(db, profile=profile, locale=locale, current_user=current_user)
    return BiographerResumeRead(
        profile_id=state.profile_id,
        biography_status=state.biography_status,
        eligible=state.eligible,
        blocked_reason=state.blocked_reason,
        active_question=state.active_question,
        candidate_id=state.candidate_id,
        review_status=state.review_status,
        enrichment_status=state.enrichment_status,
        unresolved_clarification_count=state.unresolved_clarification_count,
        promotion_status=state.promotion_status,
        next_action=state.next_action,
        next_clarification_question=state.next_clarification_question,
    )


@router.get(
    "/api/memorials/{profile_id}/biographer/next-question",
    response_model=BiographerQuestionRead | None,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_next_biographer_question_endpoint(
    profile_id: ProfileIdPath,
    locale: str = Query(pattern="^(cs|en|ru)$"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographerQuestionRead | None:
    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.SUBMIT_CONTRIBUTION,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    try:
        return get_next_question(
            db,
            profile=profile,
            current_user=current_user,
            locale=locale,
            trace_id=get_request_id(),
        )
    except BiographerBlockedError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.reason) from exc


@router.post(
    "/api/memorials/{profile_id}/biographer/questions/{question_id}/answer",
    response_model=BiographerAnswerResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_409_CONFLICT: {"model": ErrorResponse},
    },
)
def answer_biographer_question_endpoint(
    profile_id: ProfileIdPath,
    question_id: QuestionIdPath,
    payload: BiographerAnswerRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographerAnswerResponse:
    try:
        profile, membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.SUBMIT_CONTRIBUTION,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    actor_role = _ROLE_TO_ACTOR_ROLE.get(membership.role)
    if actor_role is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient memorial permissions")
    try:
        return answer_question(
            db,
            profile=profile,
            question_id=question_id,
            current_user=current_user,
            actor_role=actor_role,
            locale=payload.locale,
            answer_text=payload.answer_text,
            source_language=payload.source_language,
        )
    except BiographerNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except BiographerConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post(
    "/api/memorials/{profile_id}/biographer/questions/{question_id}/skip",
    response_model=BiographerQuestionRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_409_CONFLICT: {"model": ErrorResponse},
    },
)
def skip_biographer_question_endpoint(
    profile_id: ProfileIdPath,
    question_id: QuestionIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographerQuestionRead:
    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.SUBMIT_CONTRIBUTION,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    try:
        return skip_question(db, profile=profile, question_id=question_id)
    except BiographerNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except BiographerConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post(
    "/api/memorials/{profile_id}/biographer/questions/{question_id}/postpone",
    response_model=BiographerQuestionRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_409_CONFLICT: {"model": ErrorResponse},
    },
)
def postpone_biographer_question_endpoint(
    profile_id: ProfileIdPath,
    question_id: QuestionIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BiographerQuestionRead:
    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.SUBMIT_CONTRIBUTION,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access_error(exc)
    try:
        return postpone_question(db, profile=profile, question_id=question_id)
    except BiographerNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except BiographerConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

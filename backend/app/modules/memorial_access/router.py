from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import (
    MemorialContribution,
    MemorialContributionPromotion,
    MemorialInvitation,
    MemorialMembership,
    MemoryProfile,
    User,
)
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.billing.schemas import BillingLimitExceededResponse
from app.modules.memorial_contribution_indexing import repository as contribution_indexing_repository
from app.modules.memorial_contribution_indexing.schemas import ContributionIndexingStatusRead
from app.modules.memorial_contribution_indexing.service import (
    ContributionIndexingConflictError,
    ContributionIndexingEligibilityError,
    ContributionIndexingNotFoundError,
    get_indexing_status_for_contribution,
)
from app.modules.memorial_access.schemas import (
    ContributionCreate,
    ContributionRead,
    ContributionRejectRequest,
    ContributionReviewRequest,
    InvitationAcceptRequest,
    InvitationCreate,
    InvitationCreateResponse,
    InvitationRead,
    MembershipRead,
    MemorialCreate,
    MemorialRead,
)
from app.modules.memorial_access.service import (
    ContributionInvalidTransitionError,
    ContributionNotFoundError,
    InvitationEmailMismatchError,
    InvitationExpiredError,
    InvitationInvalidError,
    MemorialConflictError,
    MemorialForbiddenError,
    MemorialNotFoundError,
    accept_invitation,
    approve_contribution,
    archive_contribution,
    contribution_is_active_memory,
    create_memorial,
    get_memorial,
    invite_participant,
    list_contributions,
    list_memberships,
    list_memorials,
    list_review_queue,
    reject_contribution,
    retry_contribution_indexing,
    submit_contribution,
)


router = APIRouter(tags=["memorial-access"])
ProfileIdPath = Annotated[int, Path(gt=0)]
ContributionIdPath = Annotated[int, Path(gt=0)]


def _build_memorial_read(profile: MemoryProfile, membership: MemorialMembership) -> MemorialRead:
    return MemorialRead(
        id=profile.id,
        owner_user_id=profile.user_id,
        name=profile.name,
        birth_date=profile.birth_date,
        death_date=profile.death_date,
        biography=profile.biography,
        personality=profile.personality,
        catchphrases=profile.catchphrases,
        is_public=profile.is_public,
        current_user_role=membership.role,
        created_at=profile.created_at,
        updated_at=profile.updated_at,
    )


def _build_membership_read(membership: MemorialMembership) -> MembershipRead:
    return MembershipRead(
        id=membership.id,
        profile_id=membership.profile_id,
        user_id=membership.user_id,
        email=membership.user.email,
        full_name=membership.user.full_name,
        role=membership.role,
        status=membership.status,
        created_at=membership.created_at,
        updated_at=membership.updated_at,
    )


def _build_invitation_read(invitation: MemorialInvitation) -> InvitationRead:
    return InvitationRead(
        id=invitation.id,
        profile_id=invitation.profile_id,
        email=invitation.email,
        role=invitation.role,
        expires_at=invitation.expires_at,
        accepted_at=invitation.accepted_at,
        revoked_at=invitation.revoked_at,
        created_at=invitation.created_at,
    )


def _build_invitation_response(invitation: MemorialInvitation, token: str) -> InvitationCreateResponse:
    base = _build_invitation_read(invitation)
    return InvitationCreateResponse(
        **base.model_dump(),
        token=token,
        accept_url=f"/invitations/accept?token={token}",
    )


def _build_indexing_status_read(
    contribution: MemorialContribution,
    promotion: MemorialContributionPromotion | None,
) -> ContributionIndexingStatusRead:
    state, resolved_promotion = get_indexing_status_for_contribution(contribution, promotion)
    return ContributionIndexingStatusRead(
        state=state,
        indexed_at=resolved_promotion.indexed_at if resolved_promotion else None,
        attempt_count=resolved_promotion.indexing_attempt_count if resolved_promotion else 0,
        failure_reason=resolved_promotion.failure_reason if resolved_promotion else None,
    )


def _build_contribution_read(
    contribution: MemorialContribution,
    *,
    promotion: MemorialContributionPromotion | None = None,
) -> ContributionRead:
    return ContributionRead(
        id=contribution.id,
        profile_id=contribution.profile_id,
        author_user_id=contribution.author_user_id,
        author_email=contribution.author_user.email,
        title=contribution.title,
        memory_text=contribution.memory_text,
        source_note=contribution.source_note,
        privacy_scope=contribution.privacy_scope,
        status=contribution.status,
        is_current=contribution.is_current,
        supersedes_contribution_id=contribution.supersedes_contribution_id,
        reviewed_at=contribution.reviewed_at,
        reviewed_by_user_id=contribution.reviewed_by_user_id,
        review_note=contribution.review_note,
        rejection_reason=contribution.rejection_reason,
        active_memory_eligible=contribution_is_active_memory(contribution),
        indexing_status=_build_indexing_status_read(contribution, promotion),
        created_at=contribution.created_at,
        updated_at=contribution.updated_at,
    )


def _build_contribution_reads(
    db: Session,
    contributions: list[MemorialContribution],
) -> list[ContributionRead]:
    promotions_by_contribution_id = contribution_indexing_repository.list_promotions_for_contributions(
        db,
        contribution_ids=[contribution.id for contribution in contributions],
    )
    return [
        _build_contribution_read(
            contribution,
            promotion=promotions_by_contribution_id.get(contribution.id),
        )
        for contribution in contributions
    ]


def _raise_access_error(exc: Exception) -> None:
    if isinstance(exc, MemorialNotFoundError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    if isinstance(exc, MemorialForbiddenError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    if isinstance(exc, MemorialConflictError):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    raise exc


@router.post(
    "/api/memorials",
    response_model=MemorialRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": BillingLimitExceededResponse},
    },
)
def create_memorial_endpoint(
    payload: MemorialCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemorialRead:
    profile, membership = create_memorial(db, current_user=current_user, payload=payload)
    return _build_memorial_read(profile, membership)


@router.get(
    "/api/memorials",
    response_model=list[MemorialRead],
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def list_memorials_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[MemorialRead]:
    return [_build_memorial_read(profile, membership) for profile, membership in list_memorials(db, current_user=current_user)]


@router.get(
    "/api/memorials/{profile_id}",
    response_model=MemorialRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_memorial_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MemorialRead:
    try:
        profile, membership = get_memorial(db, current_user=current_user, profile_id=profile_id)
    except MemorialNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    return _build_memorial_read(profile, membership)


@router.get(
    "/api/memorials/{profile_id}/members",
    response_model=list[MembershipRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_members_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[MembershipRead]:
    try:
        memberships = list_memberships(db, current_user=current_user, profile_id=profile_id)
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    return [_build_membership_read(membership) for membership in memberships]


@router.post(
    "/api/memorials/{profile_id}/invitations",
    response_model=InvitationCreateResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def invite_participant_endpoint(
    profile_id: ProfileIdPath,
    payload: InvitationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> InvitationCreateResponse:
    try:
        invitation, token = invite_participant(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    return _build_invitation_response(invitation, token)


@router.post(
    "/api/invitations/accept",
    response_model=MembershipRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_409_CONFLICT: {"model": ErrorResponse},
    },
)
def accept_invitation_endpoint(
    payload: InvitationAcceptRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MembershipRead:
    try:
        membership = accept_invitation(db, current_user=current_user, token=payload.token)
    except InvitationInvalidError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except (InvitationExpiredError, InvitationEmailMismatchError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except MemorialConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _build_membership_read(membership)


@router.post(
    "/api/memorials/{profile_id}/contributions",
    response_model=ContributionRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def submit_contribution_endpoint(
    profile_id: ProfileIdPath,
    payload: ContributionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ContributionRead:
    try:
        contribution = submit_contribution(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    return _build_contribution_read(contribution)  # freshly submitted: never has a promotion yet


@router.get(
    "/api/memorials/{profile_id}/contributions",
    response_model=list[ContributionRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_contributions_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[ContributionRead]:
    try:
        contributions = list_contributions(db, current_user=current_user, profile_id=profile_id)
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    return _build_contribution_reads(db, contributions)


@router.get(
    "/api/memorials/{profile_id}/review-queue",
    response_model=list[ContributionRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def list_review_queue_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[ContributionRead]:
    try:
        contributions = list_review_queue(db, current_user=current_user, profile_id=profile_id)
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    return _build_contribution_reads(db, contributions)


@router.post(
    "/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
    response_model=ContributionRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def approve_contribution_endpoint(
    profile_id: ProfileIdPath,
    contribution_id: ContributionIdPath,
    payload: ContributionReviewRequest | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ContributionRead:
    try:
        contribution = approve_contribution(
            db,
            current_user=current_user,
            profile_id=profile_id,
            contribution_id=contribution_id,
            payload=payload or ContributionReviewRequest(),
        )
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    except ContributionNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContributionInvalidTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    promotion = contribution_indexing_repository.get_promotion_by_contribution_id(
        db,
        contribution_id=contribution.id,
    )
    return _build_contribution_read(contribution, promotion=promotion)


@router.post(
    "/api/memorials/{profile_id}/contributions/{contribution_id}/reject",
    response_model=ContributionRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def reject_contribution_endpoint(
    profile_id: ProfileIdPath,
    contribution_id: ContributionIdPath,
    payload: ContributionRejectRequest | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ContributionRead:
    try:
        contribution = reject_contribution(
            db,
            current_user=current_user,
            profile_id=profile_id,
            contribution_id=contribution_id,
            payload=payload or ContributionRejectRequest(),
        )
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    except ContributionNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContributionInvalidTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    return _build_contribution_read(contribution)


@router.post(
    "/api/memorials/{profile_id}/contributions/{contribution_id}/archive",
    response_model=ContributionRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def archive_contribution_endpoint(
    profile_id: ProfileIdPath,
    contribution_id: ContributionIdPath,
    payload: ContributionRejectRequest | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ContributionRead:
    try:
        contribution = archive_contribution(
            db,
            current_user=current_user,
            profile_id=profile_id,
            contribution_id=contribution_id,
            payload=payload or ContributionRejectRequest(),
        )
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    except ContributionNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContributionInvalidTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    # A superseded contribution (already retired, see approve_contribution)
    # can still be archived afterwards - reflect its real promotion state
    # rather than silently reporting "not_applicable".
    promotion = contribution_indexing_repository.get_promotion_by_contribution_id(
        db,
        contribution_id=contribution.id,
    )
    return _build_contribution_read(contribution, promotion=promotion)


@router.post(
    "/api/memorials/{profile_id}/contributions/{contribution_id}/retry-indexing",
    response_model=ContributionRead,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def retry_contribution_indexing_endpoint(
    profile_id: ProfileIdPath,
    contribution_id: ContributionIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ContributionRead:
    """Task 65.8 (Part I) - safe, authorized retry of a failed indexing
    attempt. Only reachable for an approved+current contribution whose
    promotion is currently `failed`; idempotent and reuses the same
    canonical memory/promotion/Qdrant point (see
    `memorial_access.service.retry_contribution_indexing`)."""

    try:
        contribution = retry_contribution_indexing(
            db,
            current_user=current_user,
            profile_id=profile_id,
            contribution_id=contribution_id,
        )
    except (MemorialNotFoundError, MemorialForbiddenError, MemorialConflictError) as exc:
        _raise_access_error(exc)
    except ContributionNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContributionIndexingNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContributionInvalidTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except (ContributionIndexingEligibilityError, ContributionIndexingConflictError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    promotion = contribution_indexing_repository.get_promotion_by_contribution_id(
        db,
        contribution_id=contribution.id,
    )
    return _build_contribution_read(contribution, promotion=promotion)


from __future__ import annotations

import hashlib
import secrets
from datetime import datetime, timedelta, timezone

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models import MemorialContribution, MemorialInvitation, MemorialMembership, MemoryProfile, User
from app.modules.billing.service import enforce_memory_profile_creation_limit
from app.modules.memorial_access import repository
from app.modules.memorial_access.schemas import (
    ContributionCreate,
    ContributionRejectRequest,
    ContributionReviewRequest,
    InvitationCreate,
    MemorialCreate,
)
from app.modules.memory_profiles import repository as memory_profiles_repository


REVIEW_ROLES = frozenset({"owner", "trusted_reviewer"})
CONTRIBUTION_ROLES = frozenset({"owner", "trusted_reviewer", "contributor"})
MEMBERSHIP_VIEW_ROLES = frozenset({"owner", "trusted_reviewer"})
INVITABLE_ROLES = frozenset({"trusted_reviewer", "contributor", "viewer"})


class MemorialAccessError(Exception):
    pass


class MemorialNotFoundError(Exception):
    pass


class MemorialForbiddenError(Exception):
    pass


class MemorialConflictError(Exception):
    pass


class InvitationInvalidError(Exception):
    pass


class InvitationExpiredError(Exception):
    pass


class InvitationEmailMismatchError(Exception):
    pass


class ContributionNotFoundError(Exception):
    pass


class ContributionInvalidTransitionError(Exception):
    pass


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _as_aware(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value


def hash_invitation_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def _build_invitation_token() -> str:
    return secrets.token_urlsafe(32)


def _require_membership(db: Session, *, profile_id: int, user: User) -> MemorialMembership:
    membership = repository.get_active_membership(db, profile_id=profile_id, user_id=user.id)
    if membership is None:
        raise MemorialNotFoundError("Memorial not found")
    return membership


def _require_role(
    db: Session,
    *,
    profile_id: int,
    user: User,
    allowed_roles: frozenset[str],
) -> MemorialMembership:
    membership = _require_membership(db, profile_id=profile_id, user=user)
    if membership.role not in allowed_roles:
        raise MemorialForbiddenError("Insufficient memorial permissions")
    return membership


def _get_profile_for_member(db: Session, *, profile_id: int, user: User) -> tuple[MemoryProfile, MemorialMembership]:
    membership = _require_membership(db, profile_id=profile_id, user=user)
    profile = repository.get_profile(db, profile_id=profile_id)
    if profile is None:
        raise MemorialNotFoundError("Memorial not found")
    return profile, membership


def _active_memory_eligible(contribution: MemorialContribution) -> bool:
    return contribution.status == "approved" and contribution.is_current


def create_memorial(db: Session, *, current_user: User, payload: MemorialCreate) -> tuple[MemoryProfile, MemorialMembership]:
    current_profiles = memory_profiles_repository.count_memory_profiles_for_user(db, current_user.id)
    enforce_memory_profile_creation_limit(current_user=current_user, current_profiles=current_profiles)
    profile = memory_profiles_repository.create_memory_profile(
        db,
        user_id=current_user.id,
        **payload.model_dump(),
    )
    db.flush()
    membership = repository.create_membership(
        db,
        profile_id=profile.id,
        user_id=current_user.id,
        role="owner",
        created_by_user_id=current_user.id,
    )
    db.commit()
    db.refresh(profile)
    db.refresh(membership)
    return profile, membership


def list_memorials(db: Session, *, current_user: User) -> list[tuple[MemoryProfile, MemorialMembership]]:
    return repository.list_profiles_for_member(db, user_id=current_user.id)


def get_memorial(db: Session, *, current_user: User, profile_id: int) -> tuple[MemoryProfile, MemorialMembership]:
    return _get_profile_for_member(db, profile_id=profile_id, user=current_user)


def list_memberships(db: Session, *, current_user: User, profile_id: int) -> list[MemorialMembership]:
    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=MEMBERSHIP_VIEW_ROLES)
    return repository.list_active_memberships(db, profile_id=profile_id)


def invite_participant(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: InvitationCreate,
) -> tuple[MemorialInvitation, str]:
    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=frozenset({"owner"}))
    if payload.role not in INVITABLE_ROLES:
        raise MemorialForbiddenError("Role cannot be invited")

    token = _build_invitation_token()
    invitation = repository.create_invitation(
        db,
        profile_id=profile_id,
        email=payload.email,
        role=payload.role,
        token_hash=hash_invitation_token(token),
        expires_at=_now() + timedelta(days=payload.expires_in_days),
        created_by_user_id=current_user.id,
    )
    db.commit()
    db.refresh(invitation)
    return invitation, token


def accept_invitation(db: Session, *, current_user: User, token: str) -> MemorialMembership:
    invitation = repository.get_invitation_by_token_hash(db, token_hash=hash_invitation_token(token))
    if invitation is None or invitation.revoked_at is not None or invitation.accepted_at is not None:
        raise InvitationInvalidError("Invitation is invalid")
    if _as_aware(invitation.expires_at) <= _now():
        raise InvitationExpiredError("Invitation has expired")
    if invitation.email != current_user.email:
        raise InvitationEmailMismatchError("Invitation email does not match current user")

    existing = repository.get_active_membership(db, profile_id=invitation.profile_id, user_id=current_user.id)
    if existing is not None:
        invitation.accepted_at = _now()
        invitation.accepted_by_user_id = current_user.id
        db.commit()
        db.refresh(existing)
        return existing

    membership = repository.create_membership(
        db,
        profile_id=invitation.profile_id,
        user_id=current_user.id,
        role=invitation.role,
        created_by_user_id=invitation.created_by_user_id,
    )
    invitation.accepted_at = _now()
    invitation.accepted_by_user_id = current_user.id
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise MemorialConflictError("Membership already exists") from exc
    db.refresh(membership)
    return membership


def submit_contribution(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: ContributionCreate,
) -> MemorialContribution:
    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=CONTRIBUTION_ROLES)
    contribution = repository.create_contribution(
        db,
        profile_id=profile_id,
        author_user_id=current_user.id,
        title=payload.title,
        memory_text=payload.memory_text,
        source_note=payload.source_note,
        privacy_scope=payload.privacy_scope,
        status="needs_review" if payload.submit_for_review else "draft",
    )
    db.commit()
    db.refresh(contribution)
    return contribution


def list_contributions(db: Session, *, current_user: User, profile_id: int) -> list[MemorialContribution]:
    membership = _require_membership(db, profile_id=profile_id, user=current_user)
    if membership.role in REVIEW_ROLES:
        return repository.list_contributions_for_profile(db, profile_id=profile_id)
    return repository.list_contributions_for_author(db, profile_id=profile_id, author_user_id=current_user.id)


def list_review_queue(db: Session, *, current_user: User, profile_id: int) -> list[MemorialContribution]:
    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=REVIEW_ROLES)
    return repository.list_pending_contributions(db, profile_id=profile_id)


def approve_contribution(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    contribution_id: int,
    payload: ContributionReviewRequest,
) -> MemorialContribution:
    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=REVIEW_ROLES)
    contribution = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
    if contribution is None:
        raise ContributionNotFoundError("Contribution not found")
    if contribution.status not in {"needs_review", "draft"}:
        raise ContributionInvalidTransitionError("Contribution is not reviewable")

    if payload.supersedes_contribution_id is not None:
        superseded = repository.get_contribution(
            db,
            profile_id=profile_id,
            contribution_id=payload.supersedes_contribution_id,
        )
        if superseded is None or superseded.status != "approved" or not superseded.is_current:
            raise ContributionInvalidTransitionError("Superseded contribution is not current approved memory")
        superseded.status = "superseded"
        superseded.is_current = False
        superseded.review_note = payload.review_note or superseded.review_note
        contribution.supersedes_contribution_id = superseded.id

    contribution.status = "approved"
    contribution.is_current = True
    contribution.reviewed_at = _now()
    contribution.reviewed_by_user_id = current_user.id
    contribution.review_note = payload.review_note
    contribution.rejection_reason = None
    db.commit()
    db.refresh(contribution)
    return contribution


def reject_contribution(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    contribution_id: int,
    payload: ContributionRejectRequest,
) -> MemorialContribution:
    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=REVIEW_ROLES)
    contribution = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
    if contribution is None:
        raise ContributionNotFoundError("Contribution not found")
    if contribution.status not in {"needs_review", "draft"}:
        raise ContributionInvalidTransitionError("Contribution is not reviewable")

    contribution.status = "rejected"
    contribution.is_current = False
    contribution.reviewed_at = _now()
    contribution.reviewed_by_user_id = current_user.id
    contribution.rejection_reason = payload.reason
    db.commit()
    db.refresh(contribution)
    return contribution


def archive_contribution(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    contribution_id: int,
    payload: ContributionRejectRequest,
) -> MemorialContribution:
    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=REVIEW_ROLES)
    contribution = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
    if contribution is None:
        raise ContributionNotFoundError("Contribution not found")
    if contribution.status == "approved" and contribution.is_current:
        raise ContributionInvalidTransitionError("Current approved contribution cannot be archived")

    contribution.status = "archived"
    contribution.is_current = False
    contribution.reviewed_at = _now()
    contribution.reviewed_by_user_id = current_user.id
    contribution.rejection_reason = payload.reason
    db.commit()
    db.refresh(contribution)
    return contribution


def list_active_memory_contributions(db: Session, *, profile_id: int) -> list[MemorialContribution]:
    return repository.list_active_memory_contributions(db, profile_id=profile_id)


def contribution_is_active_memory(contribution: MemorialContribution) -> bool:
    return _active_memory_eligible(contribution)


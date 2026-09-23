from __future__ import annotations

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.db.models import MemorialContribution, MemorialInvitation, MemorialMembership, MemoryProfile


MEMBERSHIP_STATUS_ACTIVE = "active"
MEMBERSHIP_STATUS_REVOKED = "revoked"


def create_membership(
    db: Session,
    *,
    profile_id: int,
    user_id: int,
    role: str,
    created_by_user_id: int | None,
) -> MemorialMembership:
    membership = MemorialMembership(
        profile_id=profile_id,
        user_id=user_id,
        role=role,
        status=MEMBERSHIP_STATUS_ACTIVE,
        created_by_user_id=created_by_user_id,
    )
    db.add(membership)
    return membership


def get_membership(
    db: Session,
    *,
    profile_id: int,
    user_id: int,
) -> MemorialMembership | None:
    statement = (
        select(MemorialMembership)
        .options(selectinload(MemorialMembership.user))
        .where(
            MemorialMembership.profile_id == profile_id,
            MemorialMembership.user_id == user_id,
        )
    )
    return db.scalar(statement)


def get_active_membership(
    db: Session,
    *,
    profile_id: int,
    user_id: int,
) -> MemorialMembership | None:
    statement = select(MemorialMembership).where(
        MemorialMembership.profile_id == profile_id,
        MemorialMembership.user_id == user_id,
        MemorialMembership.status == MEMBERSHIP_STATUS_ACTIVE,
    )
    return db.scalar(statement)


def list_active_memberships(db: Session, *, profile_id: int) -> list[MemorialMembership]:
    statement = (
        select(MemorialMembership)
        .options(selectinload(MemorialMembership.user))
        .where(
            MemorialMembership.profile_id == profile_id,
            MemorialMembership.status == MEMBERSHIP_STATUS_ACTIVE,
        )
        .order_by(MemorialMembership.role.asc(), MemorialMembership.id.asc())
    )
    return list(db.scalars(statement))


def count_active_owner_memberships(db: Session, *, profile_id: int) -> int:
    statement = select(MemorialMembership).where(
        MemorialMembership.profile_id == profile_id,
        MemorialMembership.role == "owner",
        MemorialMembership.status == MEMBERSHIP_STATUS_ACTIVE,
    )
    return len(list(db.scalars(statement)))


def get_active_owner_membership(db: Session, *, profile_id: int) -> MemorialMembership | None:
    statement = select(MemorialMembership).where(
        MemorialMembership.profile_id == profile_id,
        MemorialMembership.role == "owner",
        MemorialMembership.status == MEMBERSHIP_STATUS_ACTIVE,
    )
    return db.scalar(statement)


def revoke_membership(
    db: Session,
    *,
    membership: MemorialMembership,
    revoked_by_user_id: int,
    revoked_at: datetime,
) -> MemorialMembership:
    membership.status = MEMBERSHIP_STATUS_REVOKED
    membership.revoked_at = revoked_at
    membership.revoked_by_user_id = revoked_by_user_id
    return membership


def reactivate_membership(
    db: Session,
    *,
    membership: MemorialMembership,
    role: str,
) -> MemorialMembership:
    """Reactivate a revoked membership with the invited role.

    Phase 5A: never demote an owner row via reactivation, and never create a
    second active owner for the same memorial.
    """
    if membership.role == "owner" and role != "owner":
        raise ValueError("Owner membership cannot be demoted via reactivation")
    if role == "owner":
        existing_owner = get_active_owner_membership(db, profile_id=membership.profile_id)
        if existing_owner is not None and existing_owner.id != membership.id:
            raise ValueError("Memorial already has an active owner membership")
    membership.status = MEMBERSHIP_STATUS_ACTIVE
    membership.role = role
    membership.revoked_at = None
    membership.revoked_by_user_id = None
    return membership


def list_profiles_for_member(db: Session, *, user_id: int) -> list[tuple[MemoryProfile, MemorialMembership]]:
    statement = (
        select(MemoryProfile, MemorialMembership)
        .join(MemorialMembership, MemorialMembership.profile_id == MemoryProfile.id)
        .where(
            MemorialMembership.user_id == user_id,
            MemorialMembership.status == MEMBERSHIP_STATUS_ACTIVE,
        )
        .order_by(MemoryProfile.id.asc())
    )
    return list(db.execute(statement).all())


def get_profile(db: Session, *, profile_id: int) -> MemoryProfile | None:
    return db.get(MemoryProfile, profile_id)


def create_invitation(
    db: Session,
    *,
    profile_id: int,
    email: str,
    role: str,
    token_hash: str,
    expires_at,
    created_by_user_id: int,
    preferred_locale_hint: str | None = None,
) -> MemorialInvitation:
    invitation = MemorialInvitation(
        profile_id=profile_id,
        email=email,
        role=role,
        preferred_locale_hint=preferred_locale_hint,
        token_hash=token_hash,
        expires_at=expires_at,
        created_by_user_id=created_by_user_id,
    )
    db.add(invitation)
    return invitation


def get_invitation_by_token_hash(db: Session, *, token_hash: str) -> MemorialInvitation | None:
    statement = select(MemorialInvitation).where(MemorialInvitation.token_hash == token_hash)
    return db.scalar(statement)


def get_active_pending_invitation(
    db: Session,
    *,
    profile_id: int,
    email: str,
    now,
) -> MemorialInvitation | None:
    statement = select(MemorialInvitation).where(
        MemorialInvitation.profile_id == profile_id,
        MemorialInvitation.email == email,
        MemorialInvitation.accepted_at.is_(None),
        MemorialInvitation.revoked_at.is_(None),
        MemorialInvitation.expires_at > now,
    )
    return db.scalar(statement)


def list_open_invitations(db: Session, *, profile_id: int) -> list[MemorialInvitation]:
    """Invitations still open for owner management: not accepted and not revoked.

    Includes both pending (unexpired) and expired rows so owners can see and
    revoke leftovers. Historical accepted/revoked rows are omitted.
    """
    statement = (
        select(MemorialInvitation)
        .where(
            MemorialInvitation.profile_id == profile_id,
            MemorialInvitation.accepted_at.is_(None),
            MemorialInvitation.revoked_at.is_(None),
        )
        .order_by(MemorialInvitation.created_at.desc(), MemorialInvitation.id.desc())
    )
    return list(db.scalars(statement))


def get_invitation(
    db: Session,
    *,
    profile_id: int,
    invitation_id: int,
) -> MemorialInvitation | None:
    statement = select(MemorialInvitation).where(
        MemorialInvitation.profile_id == profile_id,
        MemorialInvitation.id == invitation_id,
    )
    return db.scalar(statement)


def create_contribution(
    db: Session,
    *,
    profile_id: int,
    author_user_id: int,
    title: str,
    memory_text: str,
    source_language: str,
    source_note: str | None,
    privacy_scope: str,
    status: str,
) -> MemorialContribution:
    contribution = MemorialContribution(
        profile_id=profile_id,
        author_user_id=author_user_id,
        title=title,
        memory_text=memory_text,
        source_language=source_language,
        source_note=source_note,
        privacy_scope=privacy_scope,
        status=status,
        is_current=False,
    )
    db.add(contribution)
    return contribution


def get_contribution(
    db: Session,
    *,
    profile_id: int,
    contribution_id: int,
) -> MemorialContribution | None:
    statement = (
        select(MemorialContribution)
        .options(selectinload(MemorialContribution.author_user))
        .where(
            MemorialContribution.profile_id == profile_id,
            MemorialContribution.id == contribution_id,
        )
    )
    return db.scalar(statement)


def list_contributions_for_profile(db: Session, *, profile_id: int) -> list[MemorialContribution]:
    statement = (
        select(MemorialContribution)
        .options(selectinload(MemorialContribution.author_user))
        .where(MemorialContribution.profile_id == profile_id)
        .order_by(MemorialContribution.created_at.desc(), MemorialContribution.id.desc())
    )
    return list(db.scalars(statement))


def list_contributions_for_author(
    db: Session,
    *,
    profile_id: int,
    author_user_id: int,
) -> list[MemorialContribution]:
    statement = (
        select(MemorialContribution)
        .options(selectinload(MemorialContribution.author_user))
        .where(
            MemorialContribution.profile_id == profile_id,
            MemorialContribution.author_user_id == author_user_id,
        )
        .order_by(MemorialContribution.created_at.desc(), MemorialContribution.id.desc())
    )
    return list(db.scalars(statement))


def list_pending_contributions(db: Session, *, profile_id: int) -> list[MemorialContribution]:
    statement = (
        select(MemorialContribution)
        .options(selectinload(MemorialContribution.author_user))
        .where(
            MemorialContribution.profile_id == profile_id,
            MemorialContribution.status == "needs_review",
        )
        .order_by(MemorialContribution.created_at.asc(), MemorialContribution.id.asc())
    )
    return list(db.scalars(statement))


def list_active_memory_contributions(db: Session, *, profile_id: int) -> list[MemorialContribution]:
    statement = (
        select(MemorialContribution)
        .options(selectinload(MemorialContribution.author_user))
        .where(
            MemorialContribution.profile_id == profile_id,
            MemorialContribution.status == "approved",
            MemorialContribution.is_current.is_(True),
        )
        .order_by(MemorialContribution.reviewed_at.desc(), MemorialContribution.id.desc())
    )
    return list(db.scalars(statement))


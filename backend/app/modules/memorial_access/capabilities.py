"""Centralized membership-aware capability model for memorial-scoped operations.

Every module that authorizes an action against a ``memory_profiles`` row on
behalf of an authenticated user MUST resolve authorization through
:func:`resolve_authorized_profile` (or :func:`role_has_capability` directly
when the caller already holds a membership) instead of re-implementing a
strict-ownership or ad-hoc role check. This keeps the owner/trusted_reviewer/
contributor/viewer matrix defined in exactly one place and guarantees that
new call sites cannot silently drift from it.

Relationship labels (e.g. "daughter", "friend") are intentionally not part of
this model - they carry no capability today. Relationship-aware disclosure is
scoped to a later task (Task 65.2) and must not be anticipated here.
"""

from __future__ import annotations

from enum import Enum

from sqlalchemy.orm import Session

from app.db.models import MemorialMembership, MemoryProfile, User
from app.modules.memorial_access import repository
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError


class MemorialCapability(str, Enum):
    """A single permitted action on a memorial, independent of role names.

    Extend this enum (and ``ROLE_CAPABILITIES`` below) when a new memorial-
    scoped action is introduced. Do not encode capabilities as raw role-name
    string comparisons anywhere else in the codebase.
    """

    VIEW_MEMORIAL = "view_memorial"
    CHAT_WITH_AVATAR = "chat_with_avatar"
    SEARCH_APPROVED_MEMORY = "search_approved_memory"
    SUBMIT_CONTRIBUTION = "submit_contribution"
    REVIEW_CONTRIBUTION = "review_contribution"
    MANAGE_MEMBERS = "manage_members"
    MANAGE_MEMORIAL = "manage_memorial"
    DIRECT_MEMORY_WRITE = "direct_memory_write"
    UPLOAD_SOURCE = "upload_source"
    TRIGGER_INDEXING = "trigger_indexing"


# The full capability set, used for the `owner` role so that adding a new
# capability automatically grants it to owners without a matrix edit.
_ALL_CAPABILITIES: frozenset[MemorialCapability] = frozenset(MemorialCapability)

# Trusted reviewers get everything an owner has except account/billing/
# membership-management actions and raw canonical-memory mutation - matching
# the pre-existing Task 65 authorization model documented in
# `memorial_access.service` (REVIEW_ROLES/MEMBERSHIP_VIEW_ROLES), which this
# matrix must not regress.
_TRUSTED_REVIEWER_CAPABILITIES: frozenset[MemorialCapability] = frozenset(
    {
        MemorialCapability.VIEW_MEMORIAL,
        MemorialCapability.CHAT_WITH_AVATAR,
        MemorialCapability.SEARCH_APPROVED_MEMORY,
        MemorialCapability.SUBMIT_CONTRIBUTION,
        MemorialCapability.REVIEW_CONTRIBUTION,
    }
)

_CONTRIBUTOR_CAPABILITIES: frozenset[MemorialCapability] = frozenset(
    {
        MemorialCapability.VIEW_MEMORIAL,
        MemorialCapability.CHAT_WITH_AVATAR,
        MemorialCapability.SEARCH_APPROVED_MEMORY,
        MemorialCapability.SUBMIT_CONTRIBUTION,
    }
)

_VIEWER_CAPABILITIES: frozenset[MemorialCapability] = frozenset(
    {
        MemorialCapability.VIEW_MEMORIAL,
        MemorialCapability.CHAT_WITH_AVATAR,
        MemorialCapability.SEARCH_APPROVED_MEMORY,
    }
)

ROLE_CAPABILITIES: dict[str, frozenset[MemorialCapability]] = {
    "owner": _ALL_CAPABILITIES,
    "trusted_reviewer": _TRUSTED_REVIEWER_CAPABILITIES,
    "contributor": _CONTRIBUTOR_CAPABILITIES,
    "viewer": _VIEWER_CAPABILITIES,
}


def role_has_capability(role: str, capability: MemorialCapability) -> bool:
    """Pure, side-effect-free lookup - safe to unit test without a database."""

    return capability in ROLE_CAPABILITIES.get(role, frozenset())


def resolve_authorized_profile(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    capability: MemorialCapability,
) -> tuple[MemoryProfile, MemorialMembership]:
    """Resolve ``profile_id`` for ``current_user`` and require ``capability``.

    Non-member (no active membership row): raises :class:`MemorialNotFoundError`
    (404) - this deliberately matches the existing Task 65 behavior of never
    revealing whether a private memorial exists to a non-member.

    Member without the capability: raises :class:`MemorialForbiddenError` (403).

    Callers must never substitute a client-supplied role/profile ownership
    assumption for this resolution - the membership row is always re-read
    from the database on every call.
    """

    membership = repository.get_active_membership(db, profile_id=profile_id, user_id=current_user.id)
    profile = repository.get_profile(db, profile_id=profile_id)
    if profile is None:
        raise MemorialNotFoundError("Memorial not found")

    if membership is None:
        if profile.user_id != current_user.id:
            raise MemorialNotFoundError("Memorial not found")
        # Self-heal: every `memory_profiles` row is guaranteed an owner
        # membership by the Task 65 migration backfill and by
        # memorial_access.service.create_memorial for memorials created
        # through the new API. A profile created through the legacy
        # `/api/memory-profiles` endpoint after that migration ran can still
        # be missing one, since that endpoint predates membership-aware
        # authorization and was intentionally left unchanged. The profile's
        # own direct owner (`memory_profiles.user_id`) must never be treated
        # as unauthorized for their own memorial - create the missing
        # membership row once, so this converges going forward.
        membership = repository.create_membership(
            db,
            profile_id=profile_id,
            user_id=current_user.id,
            role="owner",
            created_by_user_id=current_user.id,
        )
        db.commit()
        db.refresh(membership)

    if not role_has_capability(membership.role, capability):
        raise MemorialForbiddenError("Insufficient memorial permissions")

    return profile, membership

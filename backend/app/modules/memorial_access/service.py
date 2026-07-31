from __future__ import annotations

import hashlib
import logging
import secrets
from datetime import datetime, timedelta, timezone

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
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
from app.modules.memorial_contribution_indexing import repository as contribution_indexing_repository
from app.modules.memorial_contribution_indexing import service as contribution_indexing_service
from app.modules.memory_profiles import repository as memory_profiles_repository


logger = get_logger("memorial_access")


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


def _promote_and_enqueue_indexing_safely(
    db: Session,
    *,
    contribution: MemorialContribution,
    profile: MemoryProfile,
) -> None:
    """Bridge an approved+current contribution into the canonical memory /
    embedding / indexing pipeline as a step separate from the approval
    transaction that already committed. `promote_contribution` is a cheap,
    DB-only, idempotent get-or-create; the heavy embedding/Qdrant step is
    then handed off to the existing Celery worker (see
    `enqueue_indexing_job`) rather than run inline here, so a request that
    approves a contribution never blocks on a model load. Never raises:
    approval success and indexing outcome are intentionally distinguishable,
    so a failure to even *enqueue* indexing must not turn an already-
    committed approval into an HTTP error, and must never leak internal
    exception details to the caller.
    """

    try:
        outcome = contribution_indexing_service.promote_contribution(db, contribution=contribution)
        contribution_indexing_service.enqueue_indexing_job(
            db,
            profile=profile,
            promotion=outcome.promotion,
        )
    except Exception as exc:  # noqa: BLE001 - deliberate safe-failure boundary, see docstring
        log_event(
            logger,
            logging.ERROR,
            "memorial_contribution_indexing_bridge_failed",
            contribution_id=contribution.id,
            profile_id=contribution.profile_id,
            error_type=exc.__class__.__name__,
        )


def _retire_contribution_promotion_safely(db: Session, *, contribution: MemorialContribution) -> None:
    """Best-effort de-indexing when a contribution stops being the current
    approved memory (superseded). Never raises for the same reason as
    `_promote_and_index_contribution_safely` above."""

    try:
        contribution_indexing_service.retire_contribution_promotion(db, contribution=contribution)
    except Exception as exc:  # noqa: BLE001 - deliberate safe-failure boundary, see docstring
        log_event(
            logger,
            logging.ERROR,
            "memorial_contribution_retire_bridge_failed",
            contribution_id=contribution.id,
            profile_id=contribution.profile_id,
            error_type=exc.__class__.__name__,
        )


def create_memorial(db: Session, *, current_user: User, payload: MemorialCreate) -> tuple[MemoryProfile, MemorialMembership]:
    from app.modules.language_registry.persona_sync import sync_persona_languages_to_canonical, utcnow

    current_profiles = memory_profiles_repository.count_memory_profiles_for_user(db, current_user.id)
    enforce_memory_profile_creation_limit(current_user=current_user, current_profiles=current_profiles)
    profile_fields = payload.model_dump(exclude={"confirm_canonical_language"})
    profile = memory_profiles_repository.create_memory_profile(
        db,
        user_id=current_user.id,
        canonical_language_source="creator_preference",
        canonical_language_locked_at=utcnow(),
        **profile_fields,
    )
    db.flush()
    sync_persona_languages_to_canonical(db, profile=profile)
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
    superseded_contribution = superseded if payload.supersedes_contribution_id is not None else None
    db.commit()
    db.refresh(contribution)

    # Indexing is a separate step from the approval transaction above (no
    # blocking model load inside the DB transaction that just committed the
    # review decision) and must never turn a successful approval into an
    # HTTP error - see _promote_and_enqueue_indexing_safely.
    if superseded_contribution is not None:
        _retire_contribution_promotion_safely(db, contribution=superseded_contribution)
    profile = repository.get_profile(db, profile_id=profile_id)
    if profile is not None:
        _promote_and_enqueue_indexing_safely(db, contribution=contribution, profile=profile)
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


def retry_contribution_indexing(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    contribution_id: int,
) -> MemorialContribution:
    """Explicit, reviewer-triggered start/retry of contribution indexing —
    the memory-contribution equivalent of the AI biography workflow's
    explicit `POST .../candidates/{id}/index` button.

    Task 65.9 (Part I): this used to run
    `index_contribution_promotion` synchronously inline, inside the HTTP
    request - meaning a real BGE-M3 encode and Qdrant write happened on
    the FastAPI process itself. That is exactly the invariant Task 65.9
    exists to close ("retry still performs embedding synchronously" /
    "FastAPI can initialize BGE-M3"). This now only authorizes, validates
    eligibility, ensures a promotion exists, reactivates a failed
    promotion when needed, and creates/reuses the persistent job +
    transactional outbox record - the encoder and Qdrant only run inside
    the Celery embedding-worker task.

    Restricted to `REVIEW_ROLES` (owner, trusted_reviewer). Eligible when
    the contribution is approved+current and indexing is not yet complete:

    * no promotion yet (approve bridge failed to promote) → promote + enqueue
    * promotion `failed` → reactivate to `pending_index` + enqueue
    * promotion `pending_index` with no active job → enqueue (stuck pending)
    * promotion `pending_index` with an active job → idempotent no-op (return as-is)

    Refused for `indexed` / `retired` and for contributions that are not
    approved+current.
    """

    _require_role(db, profile_id=profile_id, user=current_user, allowed_roles=REVIEW_ROLES)
    contribution = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
    if contribution is None:
        raise ContributionNotFoundError("Contribution not found")
    if contribution.status != "approved" or not contribution.is_current:
        raise ContributionInvalidTransitionError(
            "Indexing can only be started or retried for an approved, current contribution"
        )

    profile = db.get(MemoryProfile, profile_id)
    if profile is None:
        raise ContributionNotFoundError("Memorial profile not found")

    promotion = contribution_indexing_repository.get_promotion_by_contribution_id(
        db,
        contribution_id=contribution.id,
    )

    if promotion is None:
        outcome = contribution_indexing_service.promote_contribution(db, contribution=contribution)
        promotion = outcome.promotion
        contribution_indexing_service.enqueue_indexing_job(db, profile=profile, promotion=promotion)
        refreshed = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
        return refreshed if refreshed is not None else contribution

    if promotion.promotion_status in {"indexed", "retired"}:
        raise ContributionInvalidTransitionError(
            "Indexing can only be started or retried when the contribution is still awaiting indexing"
        )

    if promotion.promotion_status == "failed":
        #: Reactivate the same promotion to `pending_index` so its own
        #: indexing-status projection reads "pending" (not stale "failed")
        #: while the new job is queued/running - never claims "indexed" until
        #: the worker actually confirms it. The promotion row (and therefore
        #: the deterministic Qdrant point id it derives) is unchanged; only
        #: its status moves, which `index_contribution_promotion` already
        #: treats as an eligible starting state.
        promotion.promotion_status = "pending_index"
        db.commit()
        contribution_indexing_service.enqueue_indexing_job(db, profile=profile, promotion=promotion)
        refreshed = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
        return refreshed if refreshed is not None else contribution

    if promotion.promotion_status != "pending_index":
        raise ContributionInvalidTransitionError(
            "Indexing can only be started or retried when the contribution is still awaiting indexing"
        )

    active_job_id = contribution_indexing_service.get_active_indexing_job_id_for_promotion(
        db,
        promotion_id=promotion.id,
    )
    if active_job_id is not None:
        # Already queued/running — return current state; do not create a
        # second job. The frontend polls the existing job_id.
        refreshed = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
        return refreshed if refreshed is not None else contribution

    contribution_indexing_service.enqueue_indexing_job(db, profile=profile, promotion=promotion)

    refreshed = repository.get_contribution(db, profile_id=profile_id, contribution_id=contribution_id)
    return refreshed if refreshed is not None else contribution


def list_active_memory_contributions(db: Session, *, profile_id: int) -> list[MemorialContribution]:
    return repository.list_active_memory_contributions(db, profile_id=profile_id)


def contribution_is_active_memory(contribution: MemorialContribution) -> bool:
    return _active_memory_eligible(contribution)


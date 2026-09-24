"""Internal subscription write path for providers and test fixtures (Phase 6A).

Future payment-provider adapters must call :func:`apply_subscription_state`
(or a thin wrapper around it) after validating webhooks. They must never
patch entitlement consumers or ``PLAN_DEFINITIONS`` directly.

No HTTP endpoints live here - tests and future admin/provider adapters are
the only callers.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models import BillingSubscription
from app.modules.billing import repository
from app.modules.billing.plans import FREE_PLAN_CODE, get_plan_definition


SUBSCRIPTION_STATUSES = frozenset(
    {
        "active",
        "trialing",
        "past_due",
        "canceled",
        "expired",
    }
)

#: Statuses that may grant the stored ``plan_code`` entitlements, subject to
#: period-end and catalog validity checks in the effective-plan resolver.
ENTITLEMENT_GRANTING_STATUSES = frozenset({"active", "trialing"})


class BillingSubscriptionError(Exception):
    """Invalid subscription write payload."""


def _as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def apply_subscription_state(
    db: Session,
    *,
    user_id: int,
    plan_code: str,
    status: str,
    current_period_start: datetime | None = None,
    current_period_end: datetime | None = None,
    cancel_at_period_end: bool = False,
    provider: str | None = None,
    provider_customer_id: str | None = None,
    provider_subscription_id: str | None = None,
    provider_price_id: str | None = None,
    commit: bool = True,
) -> BillingSubscription:
    """Persist the user's current subscription state (upsert by user_id).

    Used by automated tests and reserved for future provider adapters.
    Rejects unknown statuses and unknown plan codes so an invalid provider
    payload cannot silently invent entitlements.
    """

    normalized_status = status.strip().lower()
    if normalized_status not in SUBSCRIPTION_STATUSES:
        raise BillingSubscriptionError(f"Unknown subscription status: {status}")

    normalized_plan = plan_code.strip().lower()
    if get_plan_definition(normalized_plan) is None:
        raise BillingSubscriptionError(f"Unknown billing plan code: {plan_code}")

    row = repository.upsert_subscription(
        db,
        user_id=user_id,
        plan_code=normalized_plan,
        status=normalized_status,
        current_period_start=current_period_start,
        current_period_end=current_period_end,
        cancel_at_period_end=cancel_at_period_end,
        provider=provider,
        provider_customer_id=provider_customer_id,
        provider_subscription_id=provider_subscription_id,
        provider_price_id=provider_price_id,
    )
    if commit:
        db.commit()
        db.refresh(row)
    return row


def clear_subscription_for_user(db: Session, *, user_id: int, commit: bool = True) -> None:
    """Remove the subscription row so the user falls back to free (tests)."""

    row = repository.get_subscription_for_user(db, user_id=user_id)
    if row is None:
        return
    db.delete(row)
    if commit:
        db.commit()


def subscription_grants_plan_entitlements(
    *,
    status: str,
    plan_code: str,
    current_period_end: datetime | None,
    now: datetime,
) -> bool:
    """Deterministic entitlement gate used by the effective-plan resolver.

    Paid entitlements are granted only when **all** of the following hold:

    1. ``status`` is ``active`` or ``trialing`` (not ``past_due``,
       ``canceled``, or ``expired`` - conservative until a provider grace
       policy is defined in a later phase).
    2. ``plan_code`` exists in the static catalog.
    3. ``plan_code`` is not the free plan (free is the default fallback).
    4. ``current_period_end`` is unset **or** strictly after ``now``.
    """

    if status not in ENTITLEMENT_GRANTING_STATUSES:
        return False
    plan = get_plan_definition(plan_code)
    if plan is None or plan.code == FREE_PLAN_CODE:
        return False
    if current_period_end is not None and _as_utc(current_period_end) <= _as_utc(now):
        return False
    return True

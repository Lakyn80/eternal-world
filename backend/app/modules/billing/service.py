from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models import BillingSubscription, User
from app.modules.billing import repository as billing_repository
from app.modules.billing.entitlements import enforce_usage_limit
from app.modules.billing.limits import build_plan_limits
from app.modules.billing.plans import FREE_PLAN_CODE, PLAN_DEFINITIONS, PlanDefinition, get_plan_definition
from app.modules.billing.schemas import (
    BillingCurrentPlanRead,
    BillingLimitsRead,
    BillingPlanRead,
    BillingSubscriptionStateRead,
)
from app.modules.billing.subscriptions import subscription_grants_plan_entitlements
from app.modules.billing.usage import BillingUsageTotals, build_usage_snapshot
from app.modules.memory_profiles import repository as memory_profiles_repository


BILLING_CURRENCY = "RUB"
BILLING_INTERVAL = "month"


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _build_plan_read(plan_code: str) -> BillingPlanRead:
    return build_plan_read(get_plan_definition_or_raise(plan_code))


def get_plan_definition_or_raise(plan_code: str) -> PlanDefinition:
    plan_definition = get_plan_definition(plan_code)
    if plan_definition is None:
        raise ValueError(f"Unknown billing plan code: {plan_code}")

    return plan_definition


def build_plan_read(plan_definition: PlanDefinition) -> BillingPlanRead:
    return BillingPlanRead(
        code=plan_definition.code,
        name=plan_definition.name,
        price_rub_monthly=plan_definition.price_rub_monthly,
        currency=BILLING_CURRENCY,
        billing_interval=BILLING_INTERVAL,
        features=list(plan_definition.features),
        limits=build_plan_limits(plan_definition),
        watermark_enabled=plan_definition.watermark_enabled,
        priority_support_enabled=plan_definition.priority_support_enabled,
    )


def list_billing_plans() -> list[BillingPlanRead]:
    return [_build_plan_read(plan_definition.code) for plan_definition in PLAN_DEFINITIONS]


def get_effective_plan_code_for_user(db: Session, current_user: User) -> str:
    """Resolve the plan code that entitlements must use.

    Rules (Phase 6A):

    * No subscription row → ``free``
    * Row whose status/period/plan fails :func:`subscription_grants_plan_entitlements`
      → ``free`` (covers canceled/expired/past_due, ended periods, invalid plan codes)
    * Otherwise → stored ``plan_code``
    """

    subscription = billing_repository.get_subscription_for_user(db, user_id=current_user.id)
    if subscription is None:
        return FREE_PLAN_CODE

    if subscription_grants_plan_entitlements(
        status=subscription.status,
        plan_code=subscription.plan_code,
        current_period_end=subscription.current_period_end,
        now=_utc_now(),
    ):
        return subscription.plan_code

    return FREE_PLAN_CODE


def get_effective_plan_definition_for_user(db: Session, current_user: User) -> PlanDefinition:
    return get_plan_definition_or_raise(get_effective_plan_code_for_user(db, current_user))


def _build_subscription_state_read(
    subscription: BillingSubscription | None,
) -> BillingSubscriptionStateRead:
    if subscription is None:
        return BillingSubscriptionStateRead()

    grants = subscription_grants_plan_entitlements(
        status=subscription.status,
        plan_code=subscription.plan_code,
        current_period_end=subscription.current_period_end,
        now=_utc_now(),
    )
    return BillingSubscriptionStateRead(
        status=subscription.status,
        plan_code=subscription.plan_code,
        current_period_start=subscription.current_period_start,
        current_period_end=subscription.current_period_end,
        cancel_at_period_end=subscription.cancel_at_period_end,
        grants_entitlements=grants,
    )


def get_current_user_plan(db: Session, current_user: User) -> BillingCurrentPlanRead:
    plan_definition = get_effective_plan_definition_for_user(db, current_user)
    subscription = billing_repository.get_subscription_for_user(db, user_id=current_user.id)
    current_profiles = memory_profiles_repository.count_memory_profiles_for_user(db, current_user.id)
    return BillingCurrentPlanRead(
        user_id=current_user.id,
        plan=build_plan_read(plan_definition),
        subscription=_build_subscription_state_read(subscription),
        limits=build_plan_limits(plan_definition),
        current_usage=build_usage_snapshot(BillingUsageTotals(current_profiles=current_profiles)),
    )


def get_current_user_limits(db: Session, current_user: User) -> BillingLimitsRead:
    # Task 65.5: `current_profiles` is wired to a real query; other usage
    # fields remain placeholder zeros until a later billing task needs them.
    plan_definition = get_effective_plan_definition_for_user(db, current_user)
    current_profiles = memory_profiles_repository.count_memory_profiles_for_user(db, current_user.id)
    return BillingLimitsRead(
        user_id=current_user.id,
        plan_code=plan_definition.code,
        limits=build_plan_limits(plan_definition),
        current_usage=build_usage_snapshot(BillingUsageTotals(current_profiles=current_profiles)),
    )


def enforce_memory_profile_limit_for_plan(
    *,
    plan_code: str,
    current_profiles: int,
) -> None:
    plan_definition = get_plan_definition_or_raise(plan_code)
    enforce_usage_limit(
        current_usage=current_profiles,
        limit=plan_definition.limits.max_profiles,
        error="limit_exceeded",
        code="profile_limit_exceeded",
        detail="Memory profile limit exceeded for current plan",
    )


def enforce_memory_profile_creation_limit(
    db: Session,
    *,
    current_user: User,
    current_profiles: int,
) -> None:
    enforce_memory_profile_limit_for_plan(
        plan_code=get_effective_plan_code_for_user(db, current_user),
        current_profiles=current_profiles,
    )


def enforce_memory_limit_for_plan(
    *,
    plan_code: str,
    current_memories: int,
) -> None:
    plan_definition = get_plan_definition_or_raise(plan_code)
    enforce_usage_limit(
        current_usage=current_memories,
        limit=plan_definition.limits.max_memories,
        error="limit_exceeded",
        code="memory_limit_exceeded",
        detail="Memory limit exceeded for current plan",
    )


def enforce_memory_creation_limit(
    db: Session,
    *,
    current_user: User,
    current_memories: int,
) -> None:
    enforce_memory_limit_for_plan(
        plan_code=get_effective_plan_code_for_user(db, current_user),
        current_memories=current_memories,
    )

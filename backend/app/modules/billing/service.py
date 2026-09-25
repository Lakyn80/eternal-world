from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import BillingSubscription, User
from app.modules.billing import repository as billing_repository
from app.modules.billing.entitlements import enforce_usage_limit
from app.modules.billing.limits import build_plan_limits
from app.modules.billing.market import (
    MarketCurrencyPolicy,
    resolve_checkout_currency,
    resolve_market_currency_policy,
)
from app.modules.billing.plans import FREE_PLAN_CODE, PLAN_DEFINITIONS, PlanDefinition, get_plan_definition
from app.modules.billing.prices import BILLING_INTERVAL_MONTH, list_prices_for_plan
from app.modules.billing.quota_locks import lock_user_row_for_billing_quota
from app.modules.billing.schemas import (
    BillingCatalogRead,
    BillingCurrentPlanRead,
    BillingLimitsRead,
    BillingPlanRead,
    BillingPriceRead,
    BillingSubscriptionStateRead,
)
from app.modules.billing.subscriptions import subscription_grants_plan_entitlements
from app.modules.billing.usage import BillingUsageTotals, build_usage_snapshot
from app.modules.memory_profiles import repository as memory_profiles_repository
from app.modules.memories import repository as memories_repository


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def get_configured_billing_market() -> str:
    return settings.billing_market


def resolve_request_currency_policy(locale: str | None = None) -> MarketCurrencyPolicy:
    return resolve_market_currency_policy(
        billing_market=get_configured_billing_market(),
        locale=locale,
    )


def get_plan_definition_or_raise(plan_code: str) -> PlanDefinition:
    plan_definition = get_plan_definition(plan_code)
    if plan_definition is None:
        raise ValueError(f"Unknown billing plan code: {plan_code}")

    return plan_definition


def build_plan_read(
    plan_definition: PlanDefinition,
    *,
    policy: MarketCurrencyPolicy,
) -> BillingPlanRead:
    price_rows = list_prices_for_plan(
        plan_code=plan_definition.code,
        billing_market=policy.billing_market,
        allowed_currencies=policy.allowed_currencies,
    )
    return BillingPlanRead(
        code=plan_definition.code,
        name=plan_definition.name,
        billing_interval=BILLING_INTERVAL_MONTH,
        features=list(plan_definition.features),
        limits=build_plan_limits(plan_definition),
        watermark_enabled=plan_definition.watermark_enabled,
        priority_support_enabled=plan_definition.priority_support_enabled,
        prices=[
            BillingPriceRead(
                currency=price.currency,
                amount=price.amount,
                availability=price.availability,  # type: ignore[arg-type]
                billing_interval=price.billing_interval,
            )
            for price in price_rows
        ],
    )


def list_billing_catalog(*, locale: str | None = None) -> BillingCatalogRead:
    policy = resolve_request_currency_policy(locale)
    return BillingCatalogRead(
        billing_market=policy.billing_market,
        default_currency=policy.default_currency,
        allowed_currencies=list(policy.allowed_currencies),
        locale=policy.locale,
        plans=[build_plan_read(plan_definition, policy=policy) for plan_definition in PLAN_DEFINITIONS],
    )


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
        currency=subscription.currency,
        current_period_start=subscription.current_period_start,
        current_period_end=subscription.current_period_end,
        cancel_at_period_end=subscription.cancel_at_period_end,
        grants_entitlements=grants,
    )


def get_current_user_plan(
    db: Session,
    current_user: User,
    *,
    locale: str | None = None,
) -> BillingCurrentPlanRead:
    policy = resolve_request_currency_policy(locale)
    plan_definition = get_effective_plan_definition_for_user(db, current_user)
    subscription = billing_repository.get_subscription_for_user(db, user_id=current_user.id)
    current_profiles = memory_profiles_repository.count_memory_profiles_for_user(db, current_user.id)
    return BillingCurrentPlanRead(
        user_id=current_user.id,
        billing_market=policy.billing_market,
        default_currency=policy.default_currency,
        allowed_currencies=list(policy.allowed_currencies),
        locale=policy.locale,
        plan=build_plan_read(plan_definition, policy=policy),
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


def reserve_memory_profile_creation_slot(db: Session, *, current_user: User) -> None:
    """Lock the user row, then count+enforce profile quota in one transaction window.

    Call before inserting a MemoryProfile from either memorial or memory-profile
    create paths so concurrent workers cannot both pass a stale count.
    """

    locked_user = lock_user_row_for_billing_quota(db, user_id=current_user.id)
    current_profiles = memory_profiles_repository.count_memory_profiles_for_user(
        db, locked_user.id
    )
    enforce_memory_profile_creation_limit(
        db,
        current_user=locked_user,
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


def reserve_memory_creation_slot(db: Session, *, current_user: User) -> None:
    """Lock the user row, then count+enforce memory quota in one transaction window."""

    locked_user = lock_user_row_for_billing_quota(db, user_id=current_user.id)
    current_memories = memories_repository.count_memories_for_user(db, locked_user.id)
    enforce_memory_creation_limit(
        db,
        current_user=locked_user,
        current_memories=current_memories,
    )


def prepare_checkout_stub(
    *,
    plan_code: str,
    requested_currency: str | None,
    locale: str | None = None,
) -> tuple[str, str, MarketCurrencyPolicy]:
    """Validate checkout inputs for the future provider path; no payment side effects.

    Returns ``(normalized_plan_code, validated_currency, policy)``.
    Raises ``ValueError`` for unknown plans or disallowed currencies.
    """

    plan_definition = get_plan_definition_or_raise(plan_code)
    policy = resolve_request_currency_policy(locale)
    currency = resolve_checkout_currency(
        requested_currency=requested_currency,
        policy=policy,
    )
    return plan_definition.code, currency, policy

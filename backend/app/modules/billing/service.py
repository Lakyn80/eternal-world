from __future__ import annotations

from app.db.models import User
from app.modules.billing.entitlements import enforce_usage_limit
from app.modules.billing.limits import build_plan_limits
from app.modules.billing.plans import FREE_PLAN_CODE, PLAN_DEFINITIONS, PlanDefinition, get_plan_definition
from app.modules.billing.schemas import (
    BillingCurrentPlanRead,
    BillingLimitsRead,
    BillingPlanRead,
)
from app.modules.billing.usage import build_usage_snapshot


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
        features=list(plan_definition.features),
        limits=build_plan_limits(plan_definition),
        watermark_enabled=plan_definition.watermark_enabled,
        priority_support_enabled=plan_definition.priority_support_enabled,
    )


def list_billing_plans() -> list[BillingPlanRead]:
    return [_build_plan_read(plan_definition.code) for plan_definition in PLAN_DEFINITIONS]


def get_effective_plan_code_for_user(current_user: User) -> str:
    _ = current_user
    return FREE_PLAN_CODE


def get_effective_plan_definition_for_user(current_user: User) -> PlanDefinition:
    return get_plan_definition_or_raise(get_effective_plan_code_for_user(current_user))


def get_current_user_plan(current_user: User) -> BillingCurrentPlanRead:
    return BillingCurrentPlanRead(
        user_id=current_user.id,
        plan=build_plan_read(get_effective_plan_definition_for_user(current_user)),
    )


def get_current_user_limits(current_user: User) -> BillingLimitsRead:
    plan_definition = get_effective_plan_definition_for_user(current_user)
    return BillingLimitsRead(
        user_id=current_user.id,
        plan_code=plan_definition.code,
        limits=build_plan_limits(plan_definition),
        current_usage=build_usage_snapshot(),
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
    *,
    current_user: User,
    current_profiles: int,
) -> None:
    enforce_memory_profile_limit_for_plan(
        plan_code=get_effective_plan_code_for_user(current_user),
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
    *,
    current_user: User,
    current_memories: int,
) -> None:
    enforce_memory_limit_for_plan(
        plan_code=get_effective_plan_code_for_user(current_user),
        current_memories=current_memories,
    )

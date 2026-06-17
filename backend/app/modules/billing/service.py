from __future__ import annotations

from app.db.models import User
from app.modules.billing.limits import build_plan_limits, build_usage_placeholders
from app.modules.billing.plans import FREE_PLAN_CODE, PLAN_DEFINITIONS, get_plan_definition
from app.modules.billing.schemas import (
    BillingCurrentPlanRead,
    BillingLimitsRead,
    BillingPlanRead,
)


def _build_plan_read(plan_code: str) -> BillingPlanRead:
    plan_definition = get_plan_definition(plan_code)
    if plan_definition is None:
        raise ValueError(f"Unknown billing plan code: {plan_code}")

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


def get_current_user_plan(current_user: User) -> BillingCurrentPlanRead:
    return BillingCurrentPlanRead(
        user_id=current_user.id,
        plan=_build_plan_read(get_effective_plan_code_for_user(current_user)),
    )


def get_current_user_limits(current_user: User) -> BillingLimitsRead:
    plan_code = get_effective_plan_code_for_user(current_user)
    plan_definition = get_plan_definition(plan_code)
    if plan_definition is None:
        raise ValueError(f"Unknown billing plan code: {plan_code}")

    return BillingLimitsRead(
        user_id=current_user.id,
        plan_code=plan_definition.code,
        limits=build_plan_limits(plan_definition),
        current_usage=build_usage_placeholders(),
    )

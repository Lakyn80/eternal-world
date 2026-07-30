from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.billing.schemas import BillingCurrentPlanRead, BillingLimitsRead, BillingPlanRead
from app.modules.billing.service import (
    get_current_user_limits,
    get_current_user_plan,
    list_billing_plans,
)


router = APIRouter(prefix="/api/billing", tags=["billing"])


@router.get(
    "/plans",
    response_model=list[BillingPlanRead],
)
def list_plans_endpoint() -> list[BillingPlanRead]:
    return list_billing_plans()


@router.get(
    "/me",
    response_model=BillingCurrentPlanRead,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def get_my_plan_endpoint(
    current_user: User = Depends(get_current_user),
) -> BillingCurrentPlanRead:
    return get_current_user_plan(current_user)


@router.get(
    "/limits",
    response_model=BillingLimitsRead,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def get_my_limits_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BillingLimitsRead:
    return get_current_user_limits(db, current_user)

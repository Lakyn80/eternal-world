from __future__ import annotations

from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.billing.schemas import (
    BillingCatalogRead,
    BillingCurrentPlanRead,
    BillingLimitsRead,
    CheckoutNotAvailableResponse,
    CheckoutRequest,
)
from app.modules.billing.service import (
    get_current_user_limits,
    get_current_user_plan,
    list_billing_catalog,
    prepare_checkout_stub,
)


router = APIRouter(prefix="/api/billing", tags=["billing"])


@router.get(
    "/plans",
    response_model=BillingCatalogRead,
)
def list_plans_endpoint(
    locale: str | None = Query(
        default=None,
        description="UI locale (cs/en/ru). Affects default/allowed currencies inside the market only.",
    ),
) -> BillingCatalogRead:
    return list_billing_catalog(locale=locale)


@router.get(
    "/me",
    response_model=BillingCurrentPlanRead,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def get_my_plan_endpoint(
    locale: str | None = Query(
        default=None,
        description="UI locale (cs/en/ru). Affects default/allowed currencies inside the market only.",
    ),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> BillingCurrentPlanRead:
    return get_current_user_plan(db, current_user, locale=locale)


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


@router.post(
    "/checkout/{plan_code}",
    response_model=CheckoutNotAvailableResponse,
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorResponse},
        status.HTTP_501_NOT_IMPLEMENTED: {"model": CheckoutNotAvailableResponse},
    },
)
def start_checkout_endpoint(
    plan_code: str,
    body: CheckoutRequest = Body(default_factory=CheckoutRequest),
    locale: str | None = Query(default=None),
    current_user: User = Depends(get_current_user),
) -> CheckoutNotAvailableResponse:
    """Phase 6A stub: payment-provider checkout arrives in Phase 6C.

    Validates ``plan_code`` + optional ``currency`` against the deployment
    billing market. Never mutates subscriptions or simulates payment success.
    """

    _ = current_user
    try:
        normalized_plan, currency, policy = prepare_checkout_stub(
            plan_code=plan_code,
            requested_currency=body.currency,
            locale=locale,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc

    return CheckoutNotAvailableResponse(
        plan_code=normalized_plan,
        currency=currency,
        billing_market=policy.billing_market,
    )

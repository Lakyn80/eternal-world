from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class BillingPlanLimits(BaseModel):
    max_profiles: int | None
    max_memories: int | None
    max_audio_minutes: int | None
    max_videos_per_month: int | None
    max_video_seconds: int | None
    allow_watermark_removal: bool
    allow_unlimited_chat: bool
    allow_priority_support: bool
    allow_family_members: bool
    allow_shared_memories: bool
    allow_family_tree: bool
    max_family_members: int | None
    max_video_quality: str


class BillingPriceRead(BaseModel):
    """One market-valid list price for a plan.

    ``amount`` is null when the commercial price is not yet defined
    (``availability=pending_price``). Never FX-converted at runtime.
    """

    model_config = ConfigDict(frozen=True)

    currency: str
    amount: int | None
    availability: Literal["priced", "pending_price"]
    billing_interval: str


class BillingPlanRead(BaseModel):
    model_config = ConfigDict(frozen=True)

    code: str
    name: str
    billing_interval: str
    features: list[str]
    limits: BillingPlanLimits
    watermark_enabled: bool
    priority_support_enabled: bool
    #: Only currencies allowed for the current market + locale context.
    prices: list[BillingPriceRead]


class BillingCatalogRead(BaseModel):
    """Market-aware plan catalog returned by ``GET /api/billing/plans``."""

    billing_market: str
    default_currency: str
    allowed_currencies: list[str]
    locale: str | None = None
    plans: list[BillingPlanRead]


class BillingSubscriptionStateRead(BaseModel):
    """Persisted subscription snapshot (null fields when user has no row)."""

    status: str | None = None
    plan_code: str | None = None
    currency: str | None = None
    current_period_start: datetime | None = None
    current_period_end: datetime | None = None
    cancel_at_period_end: bool = False
    #: True when the row currently grants its stored paid plan_code.
    grants_entitlements: bool = False


class BillingUsageSnapshot(BaseModel):
    current_profiles: int
    current_memories: int
    current_audio_minutes: int
    current_videos_month: int
    current_family_members: int


class BillingCurrentPlanRead(BaseModel):
    user_id: int
    billing_market: str
    default_currency: str
    allowed_currencies: list[str]
    locale: str | None = None
    #: Effective plan after subscription resolution (never null - defaults free).
    plan: BillingPlanRead
    subscription: BillingSubscriptionStateRead
    limits: BillingPlanLimits
    current_usage: BillingUsageSnapshot


class BillingLimitsRead(BaseModel):
    user_id: int
    plan_code: str
    limits: BillingPlanLimits
    current_usage: BillingUsageSnapshot


class BillingLimitExceededResponse(BaseModel):
    detail: str
    error: str
    code: str


class CheckoutRequest(BaseModel):
    """Future checkout body — currency is validated against market policy."""

    currency: str | None = Field(
        default=None,
        description="ISO currency code; must be in allowed_currencies for this market.",
    )


class CheckoutNotAvailableResponse(BaseModel):
    """Phase 6A placeholder until a payment provider is wired (Phase 6C)."""

    available: bool = False
    detail: str = "Checkout is not available yet"
    code: str = "checkout_not_available"
    plan_code: str | None = None
    currency: str | None = None
    billing_market: str | None = None

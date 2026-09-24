from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


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


class BillingPlanRead(BaseModel):
    model_config = ConfigDict(frozen=True)

    code: str
    name: str
    price_rub_monthly: int
    #: ISO-like currency code for future pricing UI (catalog is RUB today).
    currency: str
    #: Billing interval label for future pricing UI (`month` for all catalog plans).
    billing_interval: str
    features: list[str]
    limits: BillingPlanLimits
    watermark_enabled: bool
    priority_support_enabled: bool


class BillingSubscriptionStateRead(BaseModel):
    """Persisted subscription snapshot (null fields when user has no row)."""

    status: str | None = None
    plan_code: str | None = None
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


class CheckoutNotAvailableResponse(BaseModel):
    """Phase 6A placeholder until a payment provider is wired (Phase 6C)."""

    available: bool = False
    detail: str = "Checkout is not available yet"
    code: str = "checkout_not_available"

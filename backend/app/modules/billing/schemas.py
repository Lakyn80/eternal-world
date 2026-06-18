from __future__ import annotations

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
    features: list[str]
    limits: BillingPlanLimits
    watermark_enabled: bool
    priority_support_enabled: bool


class BillingCurrentPlanRead(BaseModel):
    user_id: int
    plan: BillingPlanRead


class BillingUsageSnapshot(BaseModel):
    current_profiles: int
    current_memories: int
    current_audio_minutes: int
    current_videos_month: int
    current_family_members: int


class BillingLimitsRead(BaseModel):
    user_id: int
    plan_code: str
    limits: BillingPlanLimits
    current_usage: BillingUsageSnapshot


class BillingLimitExceededResponse(BaseModel):
    detail: str
    error: str
    code: str

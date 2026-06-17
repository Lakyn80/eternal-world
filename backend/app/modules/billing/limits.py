from __future__ import annotations

from app.modules.billing.plans import PlanDefinition
from app.modules.billing.schemas import BillingPlanLimits, BillingUsageSnapshot


def build_plan_limits(plan_definition: PlanDefinition) -> BillingPlanLimits:
    plan_limits = plan_definition.limits
    return BillingPlanLimits(
        max_profiles=plan_limits.max_profiles,
        max_memories=plan_limits.max_memories,
        max_audio_minutes=plan_limits.max_audio_minutes,
        max_videos_per_month=plan_limits.max_videos_per_month,
        max_video_seconds=plan_limits.max_video_seconds,
        allow_watermark_removal=plan_limits.allow_watermark_removal,
        allow_unlimited_chat=plan_limits.allow_unlimited_chat,
        allow_priority_support=plan_limits.allow_priority_support,
        allow_family_members=plan_limits.allow_family_members,
        allow_shared_memories=plan_limits.allow_shared_memories,
        allow_family_tree=plan_limits.allow_family_tree,
        max_family_members=plan_limits.max_family_members,
        max_video_quality=plan_limits.max_video_quality,
    )


def build_usage_placeholders() -> BillingUsageSnapshot:
    return BillingUsageSnapshot(
        current_profiles=0,
        current_memories=0,
        current_audio_minutes=0,
        current_videos_month=0,
        current_family_members=0,
    )

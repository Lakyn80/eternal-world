from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlanLimitsDefinition:
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


@dataclass(frozen=True)
class PlanDefinition:
    code: str
    name: str
    price_rub_monthly: int
    features: tuple[str, ...]
    limits: PlanLimitsDefinition
    watermark_enabled: bool
    priority_support_enabled: bool


FREE_PLAN_CODE = "free"
BASIC_PLAN_CODE = "basic"
PREMIUM_PLAN_CODE = "premium"
FAMILY_PLAN_CODE = "family"
PLAN_ORDER = (
    FREE_PLAN_CODE,
    BASIC_PLAN_CODE,
    PREMIUM_PLAN_CODE,
    FAMILY_PLAN_CODE,
)


PLAN_DEFINITIONS: tuple[PlanDefinition, ...] = (
    PlanDefinition(
        code=FREE_PLAN_CODE,
        name="FREE",
        price_rub_monthly=0,
        features=(
            "1 profile",
            "up to 10 memories",
            "30 minutes audio",
            "3 videos per month up to 30 seconds",
            "watermark enabled",
        ),
        limits=PlanLimitsDefinition(
            max_profiles=1,
            max_memories=10,
            max_audio_minutes=30,
            max_videos_per_month=3,
            max_video_seconds=30,
            allow_watermark_removal=False,
            allow_unlimited_chat=False,
            allow_priority_support=False,
            allow_family_members=False,
            allow_shared_memories=False,
            allow_family_tree=False,
            max_family_members=0,
            max_video_quality="standard",
        ),
        watermark_enabled=True,
        priority_support_enabled=False,
    ),
    PlanDefinition(
        code=BASIC_PLAN_CODE,
        name="BASIC",
        price_rub_monthly=499,
        features=(
            "up to 3 profiles",
            "unlimited memories",
            "up to 5 hours audio",
            "10 videos per month up to 2 minutes",
            "no watermark",
        ),
        limits=PlanLimitsDefinition(
            max_profiles=3,
            max_memories=None,
            max_audio_minutes=300,
            max_videos_per_month=10,
            max_video_seconds=120,
            allow_watermark_removal=True,
            allow_unlimited_chat=False,
            allow_priority_support=False,
            allow_family_members=False,
            allow_shared_memories=False,
            allow_family_tree=False,
            max_family_members=0,
            max_video_quality="standard",
        ),
        watermark_enabled=False,
        priority_support_enabled=False,
    ),
    PlanDefinition(
        code=PREMIUM_PLAN_CODE,
        name="PREMIUM",
        price_rub_monthly=999,
        features=(
            "unlimited profiles",
            "unlimited audio and video",
            "4K quality",
            "video up to 10 minutes",
            "unlimited chat",
            "priority support",
        ),
        limits=PlanLimitsDefinition(
            max_profiles=None,
            max_memories=None,
            max_audio_minutes=None,
            max_videos_per_month=None,
            max_video_seconds=600,
            allow_watermark_removal=True,
            allow_unlimited_chat=True,
            allow_priority_support=True,
            allow_family_members=False,
            allow_shared_memories=False,
            allow_family_tree=False,
            max_family_members=0,
            max_video_quality="4k",
        ),
        watermark_enabled=False,
        priority_support_enabled=True,
    ),
    PlanDefinition(
        code=FAMILY_PLAN_CODE,
        name="FAMILY",
        price_rub_monthly=1999,
        features=(
            "everything from Premium",
            "up to 6 family members",
            "shared memories",
            "family tree support",
            "priority support",
        ),
        limits=PlanLimitsDefinition(
            max_profiles=None,
            max_memories=None,
            max_audio_minutes=None,
            max_videos_per_month=None,
            max_video_seconds=600,
            allow_watermark_removal=True,
            allow_unlimited_chat=True,
            allow_priority_support=True,
            allow_family_members=True,
            allow_shared_memories=True,
            allow_family_tree=True,
            max_family_members=6,
            max_video_quality="4k",
        ),
        watermark_enabled=False,
        priority_support_enabled=True,
    ),
)


def get_plan_definition(plan_code: str) -> PlanDefinition | None:
    normalized_plan_code = plan_code.strip().lower()
    for plan_definition in PLAN_DEFINITIONS:
        if plan_definition.code == normalized_plan_code:
            return plan_definition

    return None

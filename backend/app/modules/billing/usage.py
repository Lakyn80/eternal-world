from __future__ import annotations

from dataclasses import dataclass

from app.modules.billing.schemas import BillingUsageSnapshot


@dataclass(frozen=True)
class BillingUsageTotals:
    current_profiles: int = 0
    current_memories: int = 0
    current_audio_minutes: int = 0
    current_videos_month: int = 0
    current_family_members: int = 0


def build_usage_snapshot(usage_totals: BillingUsageTotals | None = None) -> BillingUsageSnapshot:
    totals = usage_totals or BillingUsageTotals()
    return BillingUsageSnapshot(
        current_profiles=totals.current_profiles,
        current_memories=totals.current_memories,
        current_audio_minutes=totals.current_audio_minutes,
        current_videos_month=totals.current_videos_month,
        current_family_members=totals.current_family_members,
    )

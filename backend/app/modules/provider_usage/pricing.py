from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal


class PricingConfigurationError(ValueError):
    """Raised when the pricing catalog itself is misconfigured (e.g. two
    entries for the same provider/model with overlapping effective ranges).
    This is a startup/config defect, never a per-request error."""


@dataclass(frozen=True)
class ProviderPricing:
    """One versioned price list for one (provider, model) pair, valid for a
    specific effective date range. Historical ``AiProviderAttempt`` rows keep
    referencing the ``pricing_version`` that was active when they were
    priced, so updating this catalog later never changes the meaning of past
    records - a new entry with a later ``effective_from`` is added instead of
    mutating an existing one.
    """

    provider: str
    model: str
    pricing_version: str
    effective_from: datetime
    effective_to: datetime | None
    currency: str
    uncached_input_per_million_tokens: Decimal | None
    cached_input_per_million_tokens: Decimal | None
    output_per_million_tokens: Decimal | None
    reasoning_per_million_tokens: Decimal | None
    pricing_source: str

    def covers(self, at: datetime) -> bool:
        if at < self.effective_from:
            return False
        if self.effective_to is not None and at >= self.effective_to:
            return False
        return True


#: Verified live via the official DeepSeek pricing page on 2026-07-21.
#: `deepseek-chat` (this deployment's configured `AI_BRAIN_MODEL` /
#: `CONTENT_TRANSLATION_MODEL`) is documented there as deprecating on
#: 2026-07-24 15:59 UTC, at which point it maps 1:1 to the non-thinking mode
#: of `deepseek-v4-flash` and already bills at that model's rates today -
#: DeepSeek states no separate historical rate applied to the old name.
#: Source: https://api-docs.deepseek.com/quick_start/pricing (no explicit
#: "effective from" date is published on that page itself, so the date this
#: catalog entry was verified is recorded as `effective_from`; DeepSeek
#: states prices "may vary" and recommends monitoring the page).
#: `deepseek-chat` runs in non-thinking mode, so it does not emit
#: `completion_tokens_details.reasoning_tokens` - reasoning price is left
#: unset (`None`) for this entry, not zero.
_DEEPSEEK_CHAT_PRICING_V1 = ProviderPricing(
    provider="openai_compatible",
    model="deepseek-chat",
    pricing_version="deepseek_2026_07_21_v1",
    effective_from=datetime(2026, 7, 21, tzinfo=timezone.utc),
    effective_to=None,
    currency="USD",
    uncached_input_per_million_tokens=Decimal("0.14"),
    cached_input_per_million_tokens=Decimal("0.0028"),
    output_per_million_tokens=Decimal("0.28"),
    reasoning_per_million_tokens=None,
    pricing_source="https://api-docs.deepseek.com/quick_start/pricing",
)

#: `deepseek-reasoner` (thinking mode of the same underlying model) is
#: documented at the same per-token rates as `deepseek-chat` above; DeepSeek
#: does not publish a separate reasoning-token price, so it is priced at the
#: same output rate as any other completion token and reasoning-specific
#: price is left unset (`None`), never zero.
_DEEPSEEK_REASONER_PRICING_V1 = ProviderPricing(
    provider="openai_compatible",
    model="deepseek-reasoner",
    pricing_version="deepseek_2026_07_21_v1",
    effective_from=datetime(2026, 7, 21, tzinfo=timezone.utc),
    effective_to=None,
    currency="USD",
    uncached_input_per_million_tokens=Decimal("0.14"),
    cached_input_per_million_tokens=Decimal("0.0028"),
    output_per_million_tokens=Decimal("0.28"),
    reasoning_per_million_tokens=None,
    pricing_source="https://api-docs.deepseek.com/quick_start/pricing",
)

#: Adding a new price: append a new `ProviderPricing` entry with a later
#: `effective_from` (and set the previous entry's `effective_to` to that same
#: instant) rather than editing an existing entry in place - this preserves
#: reproducibility for every already-persisted `AiProviderAttempt` row that
#: references the older `pricing_version`.
PRICING_CATALOG: tuple[ProviderPricing, ...] = (
    _DEEPSEEK_CHAT_PRICING_V1,
    _DEEPSEEK_REASONER_PRICING_V1,
)


def _validate_catalog(catalog: tuple[ProviderPricing, ...]) -> None:
    by_key: dict[tuple[str, str], list[ProviderPricing]] = {}
    for entry in catalog:
        by_key.setdefault((entry.provider, entry.model), []).append(entry)
    for entries in by_key.values():
        ordered = sorted(entries, key=lambda entry: entry.effective_from)
        for previous, current in zip(ordered, ordered[1:]):
            previous_end = previous.effective_to
            if previous_end is None or previous_end > current.effective_from:
                raise PricingConfigurationError(
                    "Overlapping pricing entries for "
                    f"{current.provider}/{current.model}: "
                    f"{previous.pricing_version} has no effective_to before "
                    f"{current.pricing_version} starts at {current.effective_from.isoformat()}"
                )


_validate_catalog(PRICING_CATALOG)


def get_pricing(*, provider: str, model: str, at: datetime | None = None) -> ProviderPricing | None:
    """Return the pricing entry covering ``at`` (default: now, UTC), or
    ``None`` if the model is entirely unknown to the catalog. Never falls
    back to another model's pricing - an unknown model must remain unknown,
    not silently priced as if it were something else."""

    resolved_at = at if at is not None else datetime.now(timezone.utc)
    normalized_provider = provider.strip().lower()
    normalized_model = model.strip()
    for entry in PRICING_CATALOG:
        if entry.provider != normalized_provider or entry.model != normalized_model:
            continue
        if entry.covers(resolved_at):
            return entry
    return None

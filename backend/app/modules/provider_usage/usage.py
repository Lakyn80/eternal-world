from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Any

from app.modules.provider_usage.enums import MonetaryCostStatus
from app.modules.provider_usage.pricing import ProviderPricing, get_pricing


#: Final stored precision for every monetary component. Nine decimal places
#: (nano-dollar granularity) keeps very small per-request costs (a few
#: hundred tokens can cost a small fraction of a cent) from rounding to zero,
#: while still comfortably fitting the `Numeric(18, 9)` database columns.
_COST_QUANTUM = Decimal("0.000000001")

#: Token-usage keys that are safe to retain verbatim in `raw_usage_redacted`
#: - every one of them is a small non-negative integer count, never prompt
#: or completion text, so retaining them cannot leak private content.
_SAFE_RAW_USAGE_KEYS = frozenset(
    {
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "prompt_cache_hit_tokens",
        "prompt_cache_miss_tokens",
        "reasoning_tokens",
    }
)


class UsageValidationError(ValueError):
    """Raised when raw or normalized provider usage is internally
    inconsistent (negative counts, cached tokens exceeding input tokens,
    totals that do not add up). Never raised for merely *missing* optional
    fields - only for values that are present but impossible."""


@dataclass(frozen=True)
class NormalizedTokenUsage:
    """Provider-independent token usage, before pricing is applied. All
    fields are optional because different providers/models return different
    subsets - missing fields are represented as ``None``, never fabricated
    as ``0``."""

    input_tokens: int | None
    cached_input_tokens: int | None
    uncached_input_tokens: int | None
    output_tokens: int | None
    reasoning_tokens: int | None
    total_tokens: int | None
    provider_request_id: str | None
    raw_usage_redacted: dict[str, int] | None


@dataclass(frozen=True)
class NormalizedProviderUsage:
    """Provider-independent usage + cost, ready to persist onto one
    ``AiProviderAttempt`` row."""

    provider: str
    model: str
    provider_request_id: str | None
    input_tokens: int | None
    cached_input_tokens: int | None
    uncached_input_tokens: int | None
    output_tokens: int | None
    reasoning_tokens: int | None
    total_tokens: int | None
    uncached_input_cost_usd: Decimal | None
    cached_input_cost_usd: Decimal | None
    output_cost_usd: Decimal | None
    reasoning_cost_usd: Decimal | None
    total_cost_usd: Decimal | None
    cached_input_savings_usd: Decimal | None
    monetary_cost_status: MonetaryCostStatus
    pricing_version: str | None
    raw_usage_redacted: dict[str, int] | None


def _validate_non_negative(value: int | None, *, field_name: str) -> None:
    if value is not None and value < 0:
        raise UsageValidationError(f"{field_name} must be >= 0, got {value}")


def validate_token_usage(usage: NormalizedTokenUsage) -> None:
    """Raise ``UsageValidationError`` if the token counts are internally
    impossible. Missing (``None``) fields are always valid - only present
    values are checked for consistency."""

    _validate_non_negative(usage.input_tokens, field_name="input_tokens")
    _validate_non_negative(usage.cached_input_tokens, field_name="cached_input_tokens")
    _validate_non_negative(usage.uncached_input_tokens, field_name="uncached_input_tokens")
    _validate_non_negative(usage.output_tokens, field_name="output_tokens")
    _validate_non_negative(usage.reasoning_tokens, field_name="reasoning_tokens")
    _validate_non_negative(usage.total_tokens, field_name="total_tokens")

    if usage.cached_input_tokens is not None and usage.input_tokens is not None:
        if usage.cached_input_tokens > usage.input_tokens:
            raise UsageValidationError(
                "cached_input_tokens "
                f"({usage.cached_input_tokens}) cannot exceed input_tokens ({usage.input_tokens})"
            )

    if (
        usage.uncached_input_tokens is not None
        and usage.input_tokens is not None
        and usage.cached_input_tokens is not None
    ):
        expected_uncached = usage.input_tokens - usage.cached_input_tokens
        if usage.uncached_input_tokens != expected_uncached:
            raise UsageValidationError(
                "uncached_input_tokens "
                f"({usage.uncached_input_tokens}) does not equal input_tokens - cached_input_tokens "
                f"({expected_uncached})"
            )

    if usage.reasoning_tokens is not None and usage.output_tokens is not None:
        if usage.reasoning_tokens > usage.output_tokens:
            raise UsageValidationError(
                "reasoning_tokens "
                f"({usage.reasoning_tokens}) cannot exceed output_tokens ({usage.output_tokens})"
            )

    if (
        usage.total_tokens is not None
        and usage.input_tokens is not None
        and usage.output_tokens is not None
    ):
        expected_total = usage.input_tokens + usage.output_tokens
        if usage.total_tokens != expected_total:
            raise UsageValidationError(
                "total_tokens "
                f"({usage.total_tokens}) does not equal input_tokens + output_tokens ({expected_total})"
            )


def normalize_openai_compatible_usage(
    *,
    raw_response: dict[str, Any] | None,
) -> NormalizedTokenUsage:
    """Normalize the actual DeepSeek/OpenAI-compatible chat-completion
    response fields. Verified against the real DeepSeek API docs
    (https://api-docs.deepseek.com/api/create-chat-completion): the
    top-level response has an ``id`` field, and ``usage`` has
    ``prompt_tokens``, ``prompt_cache_hit_tokens``,
    ``prompt_cache_miss_tokens``, ``completion_tokens``, ``total_tokens``,
    and an optional nested ``completion_tokens_details.reasoning_tokens``
    (present only for thinking-mode/reasoning models). Every field is read
    defensively - a model that omits cached/reasoning tokens (e.g. the
    currently configured non-thinking ``deepseek-chat``) normalizes to
    ``None`` for those fields rather than ``0``, so "unknown" is never
    confused with "known zero"."""

    if not isinstance(raw_response, dict):
        return NormalizedTokenUsage(
            input_tokens=None,
            cached_input_tokens=None,
            uncached_input_tokens=None,
            output_tokens=None,
            reasoning_tokens=None,
            total_tokens=None,
            provider_request_id=None,
            raw_usage_redacted=None,
        )

    provider_request_id: str | None = None
    raw_id = raw_response.get("id")
    if isinstance(raw_id, str) and raw_id.strip():
        provider_request_id = raw_id.strip()

    usage = raw_response.get("usage")
    if not isinstance(usage, dict):
        return NormalizedTokenUsage(
            input_tokens=None,
            cached_input_tokens=None,
            uncached_input_tokens=None,
            output_tokens=None,
            reasoning_tokens=None,
            total_tokens=None,
            provider_request_id=provider_request_id,
            raw_usage_redacted=None,
        )

    def _int_or_none(value: Any) -> int | None:
        return value if isinstance(value, int) else None

    input_tokens = _int_or_none(usage.get("prompt_tokens"))
    cached_input_tokens = _int_or_none(usage.get("prompt_cache_hit_tokens"))
    uncached_input_tokens = _int_or_none(usage.get("prompt_cache_miss_tokens"))
    output_tokens = _int_or_none(usage.get("completion_tokens"))
    total_tokens = _int_or_none(usage.get("total_tokens"))

    reasoning_tokens: int | None = None
    completion_details = usage.get("completion_tokens_details")
    if isinstance(completion_details, dict):
        reasoning_tokens = _int_or_none(completion_details.get("reasoning_tokens"))

    raw_usage_redacted = {
        key: value
        for key, value in usage.items()
        if key in _SAFE_RAW_USAGE_KEYS and isinstance(value, int)
    }
    if reasoning_tokens is not None:
        raw_usage_redacted["reasoning_tokens"] = reasoning_tokens

    return NormalizedTokenUsage(
        input_tokens=input_tokens,
        cached_input_tokens=cached_input_tokens,
        uncached_input_tokens=uncached_input_tokens,
        output_tokens=output_tokens,
        reasoning_tokens=reasoning_tokens,
        total_tokens=total_tokens,
        provider_request_id=provider_request_id,
        raw_usage_redacted=raw_usage_redacted or None,
    )


def _quantize(value: Decimal) -> Decimal:
    return value.quantize(_COST_QUANTUM, rounding=ROUND_HALF_UP)


def _price_component(
    tokens: int | None, *, price_per_million: Decimal | None
) -> tuple[Decimal | None, bool]:
    """Returns ``(cost, is_priceable)``. ``is_priceable`` is ``False`` when
    there were tokens to price but no price was configured for them (the
    caller uses this to decide between ``calculated``/``partial``/``unknown``)."""

    if tokens is None or tokens == 0:
        return Decimal("0"), True
    if price_per_million is None:
        return None, False
    return (Decimal(tokens) * price_per_million) / Decimal(1_000_000), True


def calculate_provider_usage_cost(
    *,
    provider: str,
    model: str,
    token_usage: NormalizedTokenUsage,
    pricing: ProviderPricing | None = None,
    priced_at: Any = None,
) -> NormalizedProviderUsage:
    """Validate ``token_usage`` and apply Decimal-precise pricing. Never
    rounds intermediate components before summing - only the final stored
    values are quantized. ``pricing`` may be injected directly (e.g. by
    tests); otherwise it is looked up from the catalog for ``provider``/
    ``model`` at ``priced_at`` (default: now)."""

    validate_token_usage(token_usage)

    resolved_pricing = pricing if pricing is not None else get_pricing(
        provider=provider, model=model, at=priced_at
    )

    has_any_tokens = any(
        value is not None
        for value in (
            token_usage.input_tokens,
            token_usage.cached_input_tokens,
            token_usage.uncached_input_tokens,
            token_usage.output_tokens,
            token_usage.reasoning_tokens,
        )
    )
    if not has_any_tokens:
        return NormalizedProviderUsage(
            provider=provider,
            model=model,
            provider_request_id=token_usage.provider_request_id,
            input_tokens=None,
            cached_input_tokens=None,
            uncached_input_tokens=None,
            output_tokens=None,
            reasoning_tokens=None,
            total_tokens=None,
            uncached_input_cost_usd=None,
            cached_input_cost_usd=None,
            output_cost_usd=None,
            reasoning_cost_usd=None,
            total_cost_usd=None,
            cached_input_savings_usd=None,
            monetary_cost_status=MonetaryCostStatus.NOT_APPLICABLE,
            pricing_version=None,
            raw_usage_redacted=token_usage.raw_usage_redacted,
        )

    if resolved_pricing is None:
        return NormalizedProviderUsage(
            provider=provider,
            model=model,
            provider_request_id=token_usage.provider_request_id,
            input_tokens=token_usage.input_tokens,
            cached_input_tokens=token_usage.cached_input_tokens,
            uncached_input_tokens=token_usage.uncached_input_tokens,
            output_tokens=token_usage.output_tokens,
            reasoning_tokens=token_usage.reasoning_tokens,
            total_tokens=token_usage.total_tokens,
            uncached_input_cost_usd=None,
            cached_input_cost_usd=None,
            output_cost_usd=None,
            reasoning_cost_usd=None,
            total_cost_usd=None,
            cached_input_savings_usd=None,
            monetary_cost_status=MonetaryCostStatus.UNKNOWN,
            pricing_version=None,
            raw_usage_redacted=token_usage.raw_usage_redacted,
        )

    uncached_cost, uncached_priceable = _price_component(
        token_usage.uncached_input_tokens, price_per_million=resolved_pricing.uncached_input_per_million_tokens
    )
    cached_cost, cached_priceable = _price_component(
        token_usage.cached_input_tokens, price_per_million=resolved_pricing.cached_input_per_million_tokens
    )
    output_cost, output_priceable = _price_component(
        token_usage.output_tokens, price_per_million=resolved_pricing.output_per_million_tokens
    )
    reasoning_cost, reasoning_priceable = _price_component(
        token_usage.reasoning_tokens, price_per_million=resolved_pricing.reasoning_per_million_tokens
    )

    priceable_flags = [uncached_priceable, cached_priceable, output_priceable, reasoning_priceable]
    all_priceable = all(priceable_flags)
    any_priceable_component_priced = any(
        cost is not None and cost != 0
        for cost in (uncached_cost, cached_cost, output_cost, reasoning_cost)
    )

    if all_priceable:
        monetary_cost_status = MonetaryCostStatus.CALCULATED
    elif any_priceable_component_priced:
        monetary_cost_status = MonetaryCostStatus.PARTIAL
    else:
        monetary_cost_status = MonetaryCostStatus.UNKNOWN

    total_cost: Decimal | None
    if monetary_cost_status == MonetaryCostStatus.UNKNOWN:
        total_cost = None
    else:
        # Sum only the known components; PARTIAL totals intentionally omit
        # unknown components rather than fabricating them as zero-cost.
        total_cost = sum(
            (cost for cost in (uncached_cost, cached_cost, output_cost, reasoning_cost) if cost is not None),
            start=Decimal("0"),
        )

    cached_input_savings: Decimal | None = None
    if (
        cached_priceable
        and uncached_priceable
        and token_usage.cached_input_tokens is not None
        and token_usage.cached_input_tokens > 0
        and resolved_pricing.uncached_input_per_million_tokens is not None
        and resolved_pricing.cached_input_per_million_tokens is not None
    ):
        would_be_uncached_cost = (
            Decimal(token_usage.cached_input_tokens) * resolved_pricing.uncached_input_per_million_tokens
        ) / Decimal(1_000_000)
        cached_input_savings = would_be_uncached_cost - (cached_cost or Decimal("0"))

    return NormalizedProviderUsage(
        provider=provider,
        model=model,
        provider_request_id=token_usage.provider_request_id,
        input_tokens=token_usage.input_tokens,
        cached_input_tokens=token_usage.cached_input_tokens,
        uncached_input_tokens=token_usage.uncached_input_tokens,
        output_tokens=token_usage.output_tokens,
        reasoning_tokens=token_usage.reasoning_tokens,
        total_tokens=token_usage.total_tokens,
        uncached_input_cost_usd=_quantize(uncached_cost) if uncached_cost is not None else None,
        cached_input_cost_usd=_quantize(cached_cost) if cached_cost is not None else None,
        output_cost_usd=_quantize(output_cost) if output_cost is not None else None,
        reasoning_cost_usd=_quantize(reasoning_cost) if reasoning_cost is not None else None,
        total_cost_usd=_quantize(total_cost) if total_cost is not None else None,
        cached_input_savings_usd=_quantize(cached_input_savings) if cached_input_savings is not None else None,
        monetary_cost_status=monetary_cost_status,
        pricing_version=resolved_pricing.pricing_version,
        raw_usage_redacted=token_usage.raw_usage_redacted,
    )

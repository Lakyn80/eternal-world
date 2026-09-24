"""Deployment billing-market rules (Phase 6A market correction).

Currency is determined by ``BILLING_MARKET``, not by UI language.

* ``RU`` — always RUB for every supported locale.
* ``CZ`` — locale may select among market-allowed currencies only.
"""

from __future__ import annotations

from dataclasses import dataclass


BILLING_MARKET_RU = "RU"
BILLING_MARKET_CZ = "CZ"
SUPPORTED_BILLING_MARKETS = frozenset({BILLING_MARKET_RU, BILLING_MARKET_CZ})

CURRENCY_RUB = "RUB"
CURRENCY_CZK = "CZK"
CURRENCY_EUR = "EUR"
CURRENCY_USD = "USD"

SUPPORTED_UI_LOCALES = frozenset({"cs", "en", "ru"})


@dataclass(frozen=True)
class MarketCurrencyPolicy:
    """Allowed + default currencies for one market + locale resolution."""

    billing_market: str
    allowed_currencies: tuple[str, ...]
    default_currency: str
    locale: str | None


def normalize_billing_market(market: str) -> str:
    normalized = market.strip().upper()
    if normalized not in SUPPORTED_BILLING_MARKETS:
        raise ValueError(f"Unsupported billing market: {market}")
    return normalized


def normalize_billing_locale(locale: str | None) -> str | None:
    """Map request locale to a supported UI locale primary tag, or None."""

    if locale is None:
        return None
    raw = locale.strip().lower().replace("_", "-")
    if not raw:
        return None
    primary = raw.split("-", 1)[0]
    if primary in SUPPORTED_UI_LOCALES:
        return primary
    return None


def resolve_market_currency_policy(
    *,
    billing_market: str,
    locale: str | None = None,
) -> MarketCurrencyPolicy:
    """Resolve allowed/default currencies for a deployment market + locale.

    Locale never overrides the market. On RU every locale yields RUB only.
    """

    market = normalize_billing_market(billing_market)
    normalized_locale = normalize_billing_locale(locale)

    if market == BILLING_MARKET_RU:
        return MarketCurrencyPolicy(
            billing_market=market,
            allowed_currencies=(CURRENCY_RUB,),
            default_currency=CURRENCY_RUB,
            locale=normalized_locale,
        )

    # CZ / EU market
    if normalized_locale == "cs":
        return MarketCurrencyPolicy(
            billing_market=market,
            allowed_currencies=(CURRENCY_CZK,),
            default_currency=CURRENCY_CZK,
            locale=normalized_locale,
        )
    if normalized_locale == "en":
        return MarketCurrencyPolicy(
            billing_market=market,
            allowed_currencies=(CURRENCY_EUR, CURRENCY_USD),
            default_currency=CURRENCY_EUR,
            locale=normalized_locale,
        )

    # Unsupported or missing locale → deterministic CZ market default (CZK).
    return MarketCurrencyPolicy(
        billing_market=market,
        allowed_currencies=(CURRENCY_CZK,),
        default_currency=CURRENCY_CZK,
        locale=normalized_locale,
    )


def is_currency_allowed_for_policy(currency: str, policy: MarketCurrencyPolicy) -> bool:
    return currency.strip().upper() in policy.allowed_currencies


def resolve_checkout_currency(
    *,
    requested_currency: str | None,
    policy: MarketCurrencyPolicy,
) -> str:
    """Return a validated checkout currency or the policy default.

    Explicit invalid currencies raise ``ValueError`` (API → 422).
    Missing/blank requested currency falls back to ``policy.default_currency``.
    """

    if requested_currency is None or not requested_currency.strip():
        return policy.default_currency

    normalized = requested_currency.strip().upper()
    if normalized not in policy.allowed_currencies:
        raise ValueError(
            f"Currency {normalized} is not allowed for billing market "
            f"{policy.billing_market} with locale {policy.locale!r}"
        )
    return normalized

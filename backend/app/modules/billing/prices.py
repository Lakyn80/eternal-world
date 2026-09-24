"""Explicit per-market / per-currency SaaS prices (Phase 6A).

No runtime FX conversion. Amounts are commercial list prices set per
``(plan_code, billing_market, currency)``. Missing commercial amounts use
``amount=None`` with availability ``pending_price`` — never invented from RUB.

Future payment-provider mappings attach via ``provider`` / ``provider_price_id``.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.modules.billing.market import (
    BILLING_MARKET_CZ,
    BILLING_MARKET_RU,
    CURRENCY_CZK,
    CURRENCY_EUR,
    CURRENCY_RUB,
    CURRENCY_USD,
)
from app.modules.billing.plans import (
    BASIC_PLAN_CODE,
    FAMILY_PLAN_CODE,
    FREE_PLAN_CODE,
    PLAN_ORDER,
    PREMIUM_PLAN_CODE,
)


BILLING_INTERVAL_MONTH = "month"
PRICE_AVAILABILITY_PRICED = "priced"
PRICE_AVAILABILITY_PENDING = "pending_price"


@dataclass(frozen=True)
class PriceDefinition:
    """One explicit list price slot for a plan in a market/currency.

    ``amount`` is the integer minor-unit-free SaaS list amount for the
    billing interval (e.g. 499 RUB / month). ``None`` means the commercial
    price has not been set yet — callers must not invent or FX-convert it.
    """

    plan_code: str
    billing_market: str
    currency: str
    amount: int | None
    billing_interval: str = BILLING_INTERVAL_MONTH
    #: Reserved for Phase 6C+ provider adapters (Stripe / YooKassa / …).
    provider: str | None = None
    provider_price_id: str | None = None

    @property
    def availability(self) -> str:
        if self.amount is None:
            return PRICE_AVAILABILITY_PENDING
        return PRICE_AVAILABILITY_PRICED


def _ru_rub(plan_code: str, amount: int) -> PriceDefinition:
    return PriceDefinition(
        plan_code=plan_code,
        billing_market=BILLING_MARKET_RU,
        currency=CURRENCY_RUB,
        amount=amount,
    )


def _cz_slot(plan_code: str, currency: str, amount: int | None) -> PriceDefinition:
    return PriceDefinition(
        plan_code=plan_code,
        billing_market=BILLING_MARKET_CZ,
        currency=currency,
        amount=amount,
    )


# Authoritative RU list prices (RUB). CZ commercial amounts intentionally unset.
PRICE_DEFINITIONS: tuple[PriceDefinition, ...] = (
    _ru_rub(FREE_PLAN_CODE, 0),
    _ru_rub(BASIC_PLAN_CODE, 499),
    _ru_rub(PREMIUM_PLAN_CODE, 999),
    _ru_rub(FAMILY_PLAN_CODE, 1999),
    # CZ — free is always 0; paid slots await product pricing input.
    _cz_slot(FREE_PLAN_CODE, CURRENCY_CZK, 0),
    _cz_slot(FREE_PLAN_CODE, CURRENCY_EUR, 0),
    _cz_slot(FREE_PLAN_CODE, CURRENCY_USD, 0),
    _cz_slot(BASIC_PLAN_CODE, CURRENCY_CZK, None),
    _cz_slot(BASIC_PLAN_CODE, CURRENCY_EUR, None),
    _cz_slot(BASIC_PLAN_CODE, CURRENCY_USD, None),
    _cz_slot(PREMIUM_PLAN_CODE, CURRENCY_CZK, None),
    _cz_slot(PREMIUM_PLAN_CODE, CURRENCY_EUR, None),
    _cz_slot(PREMIUM_PLAN_CODE, CURRENCY_USD, None),
    _cz_slot(FAMILY_PLAN_CODE, CURRENCY_CZK, None),
    _cz_slot(FAMILY_PLAN_CODE, CURRENCY_EUR, None),
    _cz_slot(FAMILY_PLAN_CODE, CURRENCY_USD, None),
)


def iter_price_definitions_for_market(billing_market: str) -> tuple[PriceDefinition, ...]:
    market = billing_market.strip().upper()
    return tuple(price for price in PRICE_DEFINITIONS if price.billing_market == market)


def get_price_definition(
    *,
    plan_code: str,
    billing_market: str,
    currency: str,
) -> PriceDefinition | None:
    plan = plan_code.strip().lower()
    market = billing_market.strip().upper()
    normalized_currency = currency.strip().upper()
    for price in PRICE_DEFINITIONS:
        if (
            price.plan_code == plan
            and price.billing_market == market
            and price.currency == normalized_currency
        ):
            return price
    return None


def list_prices_for_plan(
    *,
    plan_code: str,
    billing_market: str,
    allowed_currencies: tuple[str, ...] | list[str],
) -> list[PriceDefinition]:
    """Return catalog prices for ``plan_code`` limited to allowed currencies.

    Never invents missing slots via FX. Currencies without a catalog row are
    omitted (unsupported combination).
    """

    allowed = {currency.strip().upper() for currency in allowed_currencies}
    plan = plan_code.strip().lower()
    market = billing_market.strip().upper()
    results: list[PriceDefinition] = []
    for price in PRICE_DEFINITIONS:
        if price.plan_code != plan or price.billing_market != market:
            continue
        if price.currency not in allowed:
            continue
        results.append(price)
    # Stable order follows allowed_currencies declaration order.
    order = {currency: index for index, currency in enumerate(allowed_currencies)}
    results.sort(key=lambda item: order.get(item.currency, 999))
    return results


def pending_commercial_price_slots() -> tuple[PriceDefinition, ...]:
    """Price slots that require product input before checkout can sell them."""

    return tuple(
        price
        for price in PRICE_DEFINITIONS
        if price.amount is None and price.plan_code != FREE_PLAN_CODE
    )


def assert_plan_order_covers_catalog() -> None:
    """Dev/test helper: every PLAN_ORDER code has at least one RU RUB price."""

    for plan_code in PLAN_ORDER:
        if get_price_definition(
            plan_code=plan_code,
            billing_market=BILLING_MARKET_RU,
            currency=CURRENCY_RUB,
        ) is None:
            raise AssertionError(f"Missing RU/RUB price for plan {plan_code}")

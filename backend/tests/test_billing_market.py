"""Phase 6A market correction — billing market / currency invariants."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import httpx
import pytest

from app.core.config import settings
from app.db.models import User
from app.main import app
from app.modules.billing.market import resolve_checkout_currency, resolve_market_currency_policy
from app.modules.billing.plans import get_plan_definition
from app.modules.billing.prices import PRICE_DEFINITIONS, get_price_definition, pending_commercial_price_slots
from app.modules.billing.subscriptions import apply_subscription_state


PASSWORD = "StrongPass123"


def _register_and_login(client, email: str) -> str:
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": PASSWORD,
            "full_name": "Billing Market Test User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": PASSWORD},
    )
    return login_response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def billing_market_ru(monkeypatch):
    monkeypatch.setattr(settings, "billing_market", "RU")


@pytest.fixture
def billing_market_cz(monkeypatch):
    monkeypatch.setattr(settings, "billing_market", "CZ")


@pytest.mark.parametrize("locale", ["ru", "en", "cs", "fr", None])
def test_ru_market_always_rub_only(billing_market_ru, locale):
    policy = resolve_market_currency_policy(billing_market="RU", locale=locale)
    assert policy.allowed_currencies == ("RUB",)
    assert policy.default_currency == "RUB"


def test_ru_plans_api_never_exposes_cz_eur_usd(client, billing_market_ru):
    for locale in ("ru", "en", "cs"):
        body = client.get(f"/api/billing/plans?locale={locale}").json()
        assert body["billing_market"] == "RU"
        assert body["allowed_currencies"] == ["RUB"]
        assert body["default_currency"] == "RUB"
        for plan in body["plans"]:
            currencies = [price["currency"] for price in plan["prices"]]
            assert currencies == ["RUB"]
            assert "CZK" not in currencies
            assert "EUR" not in currencies
            assert "USD" not in currencies


def test_cz_cs_locale_exposes_czk_only(client, billing_market_cz):
    body = client.get("/api/billing/plans?locale=cs").json()
    assert body["billing_market"] == "CZ"
    assert body["allowed_currencies"] == ["CZK"]
    assert body["default_currency"] == "CZK"
    for plan in body["plans"]:
        assert [price["currency"] for price in plan["prices"]] == ["CZK"]


def test_cz_en_locale_exposes_eur_usd_with_eur_default(client, billing_market_cz):
    body = client.get("/api/billing/plans?locale=en").json()
    assert body["billing_market"] == "CZ"
    assert body["allowed_currencies"] == ["EUR", "USD"]
    assert body["default_currency"] == "EUR"
    for plan in body["plans"]:
        assert [price["currency"] for price in plan["prices"]] == ["EUR", "USD"]


def test_cz_me_exposes_market_currency_state(client, billing_market_cz):
    token = _register_and_login(client, "billing-market-me-cz@example.com")
    body = client.get("/api/billing/me?locale=en", headers=_auth_headers(token)).json()
    assert body["billing_market"] == "CZ"
    assert body["allowed_currencies"] == ["EUR", "USD"]
    assert body["default_currency"] == "EUR"
    assert body["plan"]["code"] == "free"


def test_invalid_checkout_currency_rejected(client, billing_market_ru):
    token = _register_and_login(client, "billing-market-bad-currency@example.com")
    response = client.post(
        "/api/billing/checkout/premium?locale=en",
        headers=_auth_headers(token),
        json={"currency": "EUR"},
    )
    assert response.status_code == 422
    me = client.get("/api/billing/me", headers=_auth_headers(token)).json()
    assert me["plan"]["code"] == "free"


def test_checkout_falls_back_to_default_currency_when_omitted(client, billing_market_cz):
    token = _register_and_login(client, "billing-market-default-currency@example.com")
    response = client.post(
        "/api/billing/checkout/premium?locale=en",
        headers=_auth_headers(token),
        json={},
    )
    assert response.status_code == 501
    body = response.json()
    assert body["available"] is False
    assert body["currency"] == "EUR"
    assert body["billing_market"] == "CZ"


def test_plan_entitlements_do_not_change_when_currency_changes(billing_market_cz):
    premium = get_plan_definition("premium")
    assert premium is not None
    for currency in ("CZK", "EUR", "USD"):
        # Entitlements live on PlanDefinition — independent of price slots.
        assert premium.limits.max_profiles is None
        assert premium.limits.allow_unlimited_chat is True
        price = get_price_definition(
            plan_code="premium",
            billing_market="CZ",
            currency=currency,
        )
        assert price is not None
        assert price.amount is None  # commercial amount unset; entitlements still identical


def test_no_runtime_fx_conversion_in_price_catalog():
    # Paid CZ amounts must remain explicitly unset — never derived from RUB.
    for price in PRICE_DEFINITIONS:
        if price.billing_market == "CZ" and price.plan_code != "free":
            assert price.amount is None
    rub_basic = get_price_definition(plan_code="basic", billing_market="RU", currency="RUB")
    assert rub_basic is not None and rub_basic.amount == 499
    pending = pending_commercial_price_slots()
    assert any(slot.currency == "CZK" and slot.plan_code == "basic" for slot in pending)
    assert any(slot.currency == "EUR" and slot.plan_code == "premium" for slot in pending)
    assert any(slot.currency == "USD" and slot.plan_code == "family" for slot in pending)


def test_subscription_currency_round_trips(client, billing_market_ru):
    email = "billing-market-currency-persist@example.com"
    token = _register_and_login(client, email)
    db = app.state.testing_session_local()
    try:
        user = db.query(User).filter(User.email == email).one()
        apply_subscription_state(
            db,
            user_id=user.id,
            plan_code="premium",
            status="active",
            current_period_start=datetime.now(timezone.utc) - timedelta(days=1),
            current_period_end=datetime.now(timezone.utc) + timedelta(days=30),
            currency="RUB",
        )
    finally:
        db.close()

    me = client.get("/api/billing/me", headers=_auth_headers(token)).json()
    assert me["plan"]["code"] == "premium"
    assert me["subscription"]["currency"] == "RUB"


def test_resolve_checkout_currency_rejects_disallowed():
    policy = resolve_market_currency_policy(billing_market="RU", locale="en")
    with pytest.raises(ValueError):
        resolve_checkout_currency(requested_currency="USD", policy=policy)


def test_billing_market_endpoints_make_no_external_http(client, billing_market_cz, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for billing market resolution")

    monkeypatch.setattr(httpx, "request", fail_http_call)
    monkeypatch.setattr(httpx, "get", fail_http_call)
    monkeypatch.setattr(httpx, "post", fail_http_call)

    token = _register_and_login(client, "billing-market-no-http@example.com")
    assert client.get("/api/billing/plans?locale=en").status_code == 200
    assert client.get("/api/billing/me?locale=cs", headers=_auth_headers(token)).status_code == 200

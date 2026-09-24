from __future__ import annotations

from datetime import datetime, timedelta, timezone

import httpx
import pytest
from pathlib import Path

from app.db.models import User
from app.main import app
from app.core.config import settings
from app.modules.billing.entitlements import check_usage_limit
from app.modules.billing.exceptions import BillingLimitExceededError
from app.modules.billing.service import (
    enforce_memory_limit_for_plan,
    enforce_memory_profile_limit_for_plan,
    get_effective_plan_code_for_user,
)
from app.modules.billing.subscriptions import apply_subscription_state, clear_subscription_for_user


PASSWORD = "StrongPass123"


@pytest.fixture(autouse=True)
def _force_ru_billing_market(monkeypatch):
    """Foundation catalog assertions are RUB-priced; market matrix lives in test_billing_market."""

    monkeypatch.setattr(settings, "billing_market", "RU")


def _register_and_login(client, email: str) -> str:
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": PASSWORD,
            "full_name": "Billing Test User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": PASSWORD},
    )
    return login_response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _user_id_for_email(email: str) -> int:
    db = app.state.testing_session_local()
    try:
        user = db.query(User).filter(User.email == email).one()
        return int(user.id)
    finally:
        db.close()


def _set_subscription(
    email: str,
    *,
    plan_code: str,
    status: str = "active",
    period_end: datetime | None = None,
) -> None:
    db = app.state.testing_session_local()
    try:
        user = db.query(User).filter(User.email == email).one()
        now = datetime.now(timezone.utc)
        apply_subscription_state(
            db,
            user_id=user.id,
            plan_code=plan_code,
            status=status,
            current_period_start=now - timedelta(days=1),
            current_period_end=period_end if period_end is not None else now + timedelta(days=30),
            cancel_at_period_end=False,
        )
    finally:
        db.close()


def test_list_plans_returns_all_four_plans(client):
    response = client.get("/api/billing/plans")

    assert response.status_code == 200
    body = response.json()
    assert body["billing_market"] == "RU"
    assert body["default_currency"] == "RUB"
    assert body["allowed_currencies"] == ["RUB"]
    assert len(body["plans"]) == 4
    for plan in body["plans"]:
        assert plan["billing_interval"] == "month"
        assert [price["currency"] for price in plan["prices"]] == ["RUB"]


def test_plan_codes_are_stable_and_ordered(client):
    response = client.get("/api/billing/plans")

    assert response.status_code == 200
    assert [plan["code"] for plan in response.json()["plans"]] == [
        "free",
        "basic",
        "premium",
        "family",
    ]


def test_unauthenticated_user_can_list_public_plans(client):
    response = client.get("/api/billing/plans")

    assert response.status_code == 200


def test_authenticated_user_defaults_to_free_plan(client):
    token = _register_and_login(client, "billing-free@example.com")

    response = client.get(
        "/api/billing/me",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["billing_market"] == "RU"
    assert body["default_currency"] == "RUB"
    assert body["allowed_currencies"] == ["RUB"]
    assert body["plan"]["code"] == "free"
    assert body["plan"]["prices"][0]["amount"] == 0
    assert body["plan"]["prices"][0]["currency"] == "RUB"
    assert body["subscription"]["status"] is None
    assert body["subscription"]["currency"] is None
    assert body["subscription"]["grants_entitlements"] is False
    assert body["limits"]["max_profiles"] == 1


def test_billing_me_rejects_unauthenticated_users(client):
    response = client.get("/api/billing/me")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_billing_limits_rejects_unauthenticated_users(client):
    response = client.get("/api/billing/limits")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_free_plan_has_correct_limits(client):
    response = client.get("/api/billing/plans")
    free_plan = response.json()["plans"][0]

    assert free_plan["code"] == "free"
    assert free_plan["prices"][0]["amount"] == 0
    assert free_plan["watermark_enabled"] is True
    assert free_plan["priority_support_enabled"] is False
    assert free_plan["limits"] == {
        "max_profiles": 1,
        "max_memories": 10,
        "max_audio_minutes": 30,
        "max_videos_per_month": 3,
        "max_video_seconds": 30,
        "allow_watermark_removal": False,
        "allow_unlimited_chat": False,
        "allow_priority_support": False,
        "allow_family_members": False,
        "allow_shared_memories": False,
        "allow_family_tree": False,
        "max_family_members": 0,
        "max_video_quality": "standard",
    }


def test_basic_plan_has_correct_limits(client):
    response = client.get("/api/billing/plans")
    basic_plan = response.json()["plans"][1]

    assert basic_plan["code"] == "basic"
    assert basic_plan["prices"][0]["amount"] == 499
    assert basic_plan["prices"][0]["currency"] == "RUB"
    assert basic_plan["watermark_enabled"] is False
    assert basic_plan["limits"]["max_profiles"] == 3
    assert basic_plan["limits"]["max_memories"] is None
    assert basic_plan["limits"]["max_audio_minutes"] == 300
    assert basic_plan["limits"]["max_videos_per_month"] == 10
    assert basic_plan["limits"]["max_video_seconds"] == 120
    assert basic_plan["limits"]["allow_watermark_removal"] is True


def test_premium_plan_has_unlimited_values_where_expected(client):
    response = client.get("/api/billing/plans")
    premium_plan = response.json()["plans"][2]

    assert premium_plan["code"] == "premium"
    assert premium_plan["prices"][0]["amount"] == 999
    assert premium_plan["limits"]["max_profiles"] is None
    assert premium_plan["limits"]["max_memories"] is None
    assert premium_plan["limits"]["max_audio_minutes"] is None
    assert premium_plan["limits"]["max_videos_per_month"] is None
    assert premium_plan["limits"]["max_video_seconds"] == 600
    assert premium_plan["limits"]["allow_unlimited_chat"] is True
    assert premium_plan["limits"]["allow_priority_support"] is True
    assert premium_plan["limits"]["max_video_quality"] == "4k"


def test_family_plan_includes_family_specific_flags(client):
    response = client.get("/api/billing/plans")
    family_plan = response.json()["plans"][3]

    assert family_plan["code"] == "family"
    assert family_plan["prices"][0]["amount"] == 1999
    assert family_plan["limits"]["allow_family_members"] is True
    assert family_plan["limits"]["allow_shared_memories"] is True
    assert family_plan["limits"]["allow_family_tree"] is True
    assert family_plan["limits"]["max_family_members"] == 6
    assert family_plan["priority_support_enabled"] is True


def test_billing_limits_returns_free_plan_limits_and_zero_usage_for_a_fresh_account(client):
    token = _register_and_login(client, "billing-limits@example.com")

    response = client.get(
        "/api/billing/limits",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["plan_code"] == "free"
    assert body["limits"]["max_profiles"] == 1
    assert body["current_usage"] == {
        "current_profiles": 0,
        "current_memories": 0,
        "current_audio_minutes": 0,
        "current_videos_month": 0,
        "current_family_members": 0,
    }


def test_billing_limits_current_profiles_reflects_real_memory_profile_count(client):
    token = _register_and_login(client, "billing-limits-real-usage@example.com")

    before = client.get("/api/billing/limits", headers=_auth_headers(token))
    assert before.json()["current_usage"]["current_profiles"] == 0

    create_response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={"name": "First Memorial", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    assert create_response.status_code == 201

    after = client.get("/api/billing/limits", headers=_auth_headers(token))
    assert after.json()["current_usage"]["current_profiles"] == 1


def test_billing_limits_current_profiles_is_scoped_to_the_requesting_user(client):
    other_token = _register_and_login(client, "billing-limits-other@example.com")
    client.post(
        "/api/memorials",
        headers=_auth_headers(other_token),
        json={
            "name": "Someone Else's Memorial",
            "canonical_language": "cs",
            "confirm_canonical_language": True,
        },
    )

    token = _register_and_login(client, "billing-limits-self@example.com")
    response = client.get("/api/billing/limits", headers=_auth_headers(token))

    assert response.json()["current_usage"]["current_profiles"] == 0


def test_user_with_no_subscription_resolves_to_free(client):
    email = "billing-resolve-none@example.com"
    token = _register_and_login(client, email)
    db = app.state.testing_session_local()
    try:
        user = db.query(User).filter(User.email == email).one()
        assert get_effective_plan_code_for_user(db, user) == "free"
    finally:
        db.close()

    me = client.get("/api/billing/me", headers=_auth_headers(token))
    assert me.json()["plan"]["code"] == "free"


@pytest.mark.parametrize(
    ("plan_code", "expected"),
    [
        ("basic", "basic"),
        ("premium", "premium"),
        ("family", "family"),
    ],
)
def test_active_paid_subscription_resolves_to_stored_plan(client, plan_code, expected):
    email = f"billing-active-{plan_code}@example.com"
    token = _register_and_login(client, email)
    _set_subscription(email, plan_code=plan_code, status="active")

    me = client.get("/api/billing/me", headers=_auth_headers(token))
    assert me.status_code == 200
    body = me.json()
    assert body["plan"]["code"] == expected
    assert body["subscription"]["status"] == "active"
    assert body["subscription"]["plan_code"] == plan_code
    assert body["subscription"]["grants_entitlements"] is True

    limits = client.get("/api/billing/limits", headers=_auth_headers(token))
    assert limits.json()["plan_code"] == expected


def test_expired_and_canceled_subscription_fall_back_to_free(client):
    email = "billing-expired@example.com"
    token = _register_and_login(client, email)

    _set_subscription(email, plan_code="premium", status="canceled")
    assert client.get("/api/billing/me", headers=_auth_headers(token)).json()["plan"]["code"] == "free"

    _set_subscription(email, plan_code="premium", status="expired")
    assert client.get("/api/billing/me", headers=_auth_headers(token)).json()["plan"]["code"] == "free"

    _set_subscription(email, plan_code="premium", status="past_due")
    assert client.get("/api/billing/me", headers=_auth_headers(token)).json()["plan"]["code"] == "free"

    past = datetime.now(timezone.utc) - timedelta(days=1)
    _set_subscription(email, plan_code="basic", status="active", period_end=past)
    assert client.get("/api/billing/me", headers=_auth_headers(token)).json()["plan"]["code"] == "free"


def test_invalid_plan_code_cannot_grant_entitlements(client):
    email = "billing-invalid-plan@example.com"
    _register_and_login(client, email)
    db = app.state.testing_session_local()
    try:
        user = db.query(User).filter(User.email == email).one()
        with pytest.raises(Exception):
            apply_subscription_state(
                db,
                user_id=user.id,
                plan_code="not-a-real-plan",
                status="active",
            )
        # Force a bad row past the write guard to prove resolver still falls back.
        from app.modules.billing import repository as billing_repository

        billing_repository.upsert_subscription(
            db,
            user_id=user.id,
            plan_code="not-a-real-plan",
            status="active",
            current_period_end=datetime.now(timezone.utc) + timedelta(days=30),
        )
        db.commit()
        assert get_effective_plan_code_for_user(db, user) == "free"
    finally:
        db.close()


def test_basic_user_can_own_up_to_basic_quota(client):
    email = "billing-basic-quota@example.com"
    token = _register_and_login(client, email)
    _set_subscription(email, plan_code="basic", status="active")

    for index in range(3):
        response = client.post(
            "/api/memorials",
            headers=_auth_headers(token),
            json={
                "name": f"Memorial {index + 1}",
                "canonical_language": "cs",
                "confirm_canonical_language": True,
            },
        )
        assert response.status_code == 201, response.text

    blocked = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={"name": "Memorial 4", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    assert blocked.status_code == 403
    assert blocked.json()["code"] == "profile_limit_exceeded"


def test_premium_unlimited_profile_behavior(client):
    email = "billing-premium-quota@example.com"
    token = _register_and_login(client, email)
    _set_subscription(email, plan_code="premium", status="active")

    for index in range(4):
        response = client.post(
            "/api/memorials",
            headers=_auth_headers(token),
            json={
                "name": f"Premium Memorial {index + 1}",
                "canonical_language": "cs",
                "confirm_canonical_language": True,
            },
        )
        assert response.status_code == 201, response.text

    limits = client.get("/api/billing/limits", headers=_auth_headers(token))
    assert limits.json()["limits"]["max_profiles"] is None
    assert limits.json()["current_usage"]["current_profiles"] == 4


def test_shared_memorials_do_not_consume_owner_quota(client):
    owner_email = "billing-share-owner@example.com"
    contributor_email = "billing-share-contrib@example.com"
    owner_token = _register_and_login(client, owner_email)
    contributor_token = _register_and_login(client, contributor_email)

    create = client.post(
        "/api/memorials",
        headers=_auth_headers(owner_token),
        json={"name": "Shared memorial", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    assert create.status_code == 201
    profile_id = create.json()["id"]

    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": contributor_email, "role": "contributor"},
    )
    assert invite.status_code == 201
    assert (
        client.post(
            "/api/invitations/accept",
            headers=_auth_headers(contributor_token),
            json={"token": invite.json()["token"]},
        ).status_code
        == 200
    )

    contrib_limits = client.get("/api/billing/limits", headers=_auth_headers(contributor_token))
    assert contrib_limits.json()["current_usage"]["current_profiles"] == 0
    assert contrib_limits.json()["plan_code"] == "free"

    # Contributor can still create their own free memorial (quota unused by share).
    own = client.post(
        "/api/memorials",
        headers=_auth_headers(contributor_token),
        json={"name": "Contributor owned", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    assert own.status_code == 201


def test_checkout_stub_does_not_mutate_subscription(client):
    email = "billing-checkout-stub@example.com"
    token = _register_and_login(client, email)

    response = client.post(
        "/api/billing/checkout/premium",
        headers=_auth_headers(token),
        json={"currency": "RUB"},
    )
    assert response.status_code == 501
    body = response.json()
    assert body["available"] is False
    assert body["code"] == "checkout_not_available"
    assert body["currency"] == "RUB"
    assert body["billing_market"] == "RU"
    assert body["plan_code"] == "premium"

    me = client.get("/api/billing/me", headers=_auth_headers(token))
    assert me.json()["plan"]["code"] == "free"
    assert me.json()["subscription"]["status"] is None


def test_billing_limit_checker_returns_allowed_for_unlimited_plans():
    result = check_usage_limit(
        current_usage=999,
        limit=None,
        error="limit_exceeded",
        code="profile_limit_exceeded",
        detail="Memory profile limit exceeded for current plan",
    )

    assert result.is_allowed is True
    assert result.limit is None


def test_basic_plan_profile_limit_logic_supports_3_profiles():
    for current_profiles in (0, 1, 2):
        enforce_memory_profile_limit_for_plan(
            plan_code="basic",
            current_profiles=current_profiles,
        )

    with pytest.raises(BillingLimitExceededError) as exc_info:
        enforce_memory_profile_limit_for_plan(
            plan_code="basic",
            current_profiles=3,
        )

    assert exc_info.value.code == "profile_limit_exceeded"
    assert exc_info.value.error == "limit_exceeded"


def test_premium_plan_profile_limit_logic_supports_unlimited_profiles():
    enforce_memory_profile_limit_for_plan(
        plan_code="premium",
        current_profiles=10_000,
    )


def test_family_plan_profile_limit_logic_supports_unlimited_profiles():
    enforce_memory_profile_limit_for_plan(
        plan_code="family",
        current_profiles=10_000,
    )


def test_free_plan_memory_limit_logic_supports_10_memories():
    for current_memories in range(10):
        enforce_memory_limit_for_plan(
            plan_code="free",
            current_memories=current_memories,
        )

    with pytest.raises(BillingLimitExceededError) as exc_info:
        enforce_memory_limit_for_plan(
            plan_code="free",
            current_memories=10,
        )

    assert exc_info.value.code == "memory_limit_exceeded"
    assert exc_info.value.error == "limit_exceeded"


def test_basic_plan_memory_limit_logic_supports_unlimited_memories():
    enforce_memory_limit_for_plan(
        plan_code="basic",
        current_memories=10_000,
    )


def test_premium_plan_memory_limit_logic_supports_unlimited_memories():
    enforce_memory_limit_for_plan(
        plan_code="premium",
        current_memories=10_000,
    )


def test_family_plan_memory_limit_logic_supports_unlimited_memories():
    enforce_memory_limit_for_plan(
        plan_code="family",
        current_memories=10_000,
    )


def test_no_payment_provider_is_called_and_no_external_api_calls_are_made(client, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for billing foundation")

    monkeypatch.setattr(httpx, "request", fail_http_call)
    monkeypatch.setattr(httpx, "get", fail_http_call)
    monkeypatch.setattr(httpx, "post", fail_http_call)

    token = _register_and_login(client, "billing-no-http@example.com")
    plans_response = client.get("/api/billing/plans")
    me_response = client.get("/api/billing/me", headers=_auth_headers(token))

    assert plans_response.status_code == 200
    assert me_response.status_code == 200


def test_chat_uses_actual_effective_plan_unlimited_flag(client):
    from app.modules.billing.service import get_effective_plan_definition_for_user
    from app.modules.chat.admission import resolve_user_chat_rate_limit

    email = "billing-chat-plan@example.com"
    _register_and_login(client, email)
    db = app.state.testing_session_local()
    try:
        user = db.query(User).filter(User.email == email).one()
        free_plan = get_effective_plan_definition_for_user(db, user)
        assert free_plan.limits.allow_unlimited_chat is False
        free_rate = resolve_user_chat_rate_limit(
            allow_unlimited_chat=free_plan.limits.allow_unlimited_chat
        )

        apply_subscription_state(
            db,
            user_id=user.id,
            plan_code="premium",
            status="active",
            current_period_end=datetime.now(timezone.utc) + timedelta(days=30),
        )
        premium_plan = get_effective_plan_definition_for_user(db, user)
        assert premium_plan.limits.allow_unlimited_chat is True
        premium_rate = resolve_user_chat_rate_limit(
            allow_unlimited_chat=premium_plan.limits.allow_unlimited_chat
        )
        assert premium_rate >= free_rate
        assert premium_rate > free_rate or premium_plan.limits.allow_unlimited_chat is True
    finally:
        db.close()


def test_clear_subscription_restores_free_fallback(client):
    email = "billing-clear@example.com"
    token = _register_and_login(client, email)
    _set_subscription(email, plan_code="family", status="active")
    assert client.get("/api/billing/me", headers=_auth_headers(token)).json()["plan"]["code"] == "family"

    db = app.state.testing_session_local()
    try:
        clear_subscription_for_user(db, user_id=_user_id_for_email(email))
    finally:
        db.close()

    assert client.get("/api/billing/me", headers=_auth_headers(token)).json()["plan"]["code"] == "free"


def test_project_progress_is_updated_for_billing_foundation():
    project_progress_path = None
    for parent in Path(__file__).resolve().parents:
        candidate_path = parent / "PROJECT_PROGRESS.md"
        if candidate_path.exists():
            project_progress_path = candidate_path
            break

    if project_progress_path is None:
        pytest.skip("PROJECT_PROGRESS.md is not available in this test environment")

    content = project_progress_path.read_text(encoding="utf-8")

    assert (
        "Billing / Tariff Foundation" in content
        or "Billing Foundation Summary" in content
        or "Usage Limits / Entitlements Foundation" in content
    )

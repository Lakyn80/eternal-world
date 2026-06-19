import httpx
import pytest
from pathlib import Path

from app.modules.billing.entitlements import check_usage_limit
from app.modules.billing.exceptions import BillingLimitExceededError
from app.modules.billing.service import enforce_memory_limit_for_plan, enforce_memory_profile_limit_for_plan


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Billing Test User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return login_response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def test_list_plans_returns_all_four_plans(client):
    response = client.get("/api/billing/plans")

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 4


def test_plan_codes_are_stable_and_ordered(client):
    response = client.get("/api/billing/plans")

    assert response.status_code == 200
    assert [plan["code"] for plan in response.json()] == [
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
    assert body["plan"]["code"] == "free"
    assert body["plan"]["price_rub_monthly"] == 0


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
    free_plan = response.json()[0]

    assert free_plan["code"] == "free"
    assert free_plan["price_rub_monthly"] == 0
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
    basic_plan = response.json()[1]

    assert basic_plan["code"] == "basic"
    assert basic_plan["price_rub_monthly"] == 499
    assert basic_plan["watermark_enabled"] is False
    assert basic_plan["limits"]["max_profiles"] == 3
    assert basic_plan["limits"]["max_memories"] is None
    assert basic_plan["limits"]["max_audio_minutes"] == 300
    assert basic_plan["limits"]["max_videos_per_month"] == 10
    assert basic_plan["limits"]["max_video_seconds"] == 120
    assert basic_plan["limits"]["allow_watermark_removal"] is True


def test_premium_plan_has_unlimited_values_where_expected(client):
    response = client.get("/api/billing/plans")
    premium_plan = response.json()[2]

    assert premium_plan["code"] == "premium"
    assert premium_plan["price_rub_monthly"] == 999
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
    family_plan = response.json()[3]

    assert family_plan["code"] == "family"
    assert family_plan["price_rub_monthly"] == 1999
    assert family_plan["limits"]["allow_family_members"] is True
    assert family_plan["limits"]["allow_shared_memories"] is True
    assert family_plan["limits"]["allow_family_tree"] is True
    assert family_plan["limits"]["max_family_members"] == 6
    assert family_plan["priority_support_enabled"] is True


def test_billing_limits_returns_free_plan_limits_and_usage_placeholders(client):
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

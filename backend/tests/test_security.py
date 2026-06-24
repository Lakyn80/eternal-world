from datetime import datetime, timedelta, timezone

import jwt
import pytest

from app.core.config import settings
from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    validate_safe_lookup_value,
    verify_password,
)


def test_password_hashing_round_trip():
    password = "Str0ngPassword!42"
    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True
    assert verify_password("wrong-password", hashed_password) is False


def test_access_token_round_trip():
    token = create_access_token("user-123")
    payload = decode_access_token(token)

    assert payload["sub"] == "user-123"
    assert payload["type"] == "access"


def test_access_token_decode_allows_small_clock_skew():
    now = datetime.now(timezone.utc)
    token = jwt.encode(
        {
            "sub": "user-123",
            "type": "access",
            "iat": int(now.timestamp()),
            "nbf": int((now + timedelta(seconds=3)).timestamp()),
            "exp": int((now + timedelta(minutes=30)).timestamp()),
            "iss": settings.jwt_issuer,
            "aud": settings.jwt_audience,
        },
        settings.jwt_secret_key.get_secret_value(),
        algorithm=settings.jwt_algorithm,
    )

    payload = decode_access_token(token)

    assert payload["sub"] == "user-123"


def test_lookup_value_validation_rejects_sql_injection_payload():
    assert validate_safe_lookup_value("valid.user-01", field_name="username") == "valid.user-01"

    with pytest.raises(ValueError):
        validate_safe_lookup_value(
            "admin'; DROP TABLE users; --",
            field_name="username",
        )

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from typing import Any, Mapping

import jwt
from passlib.context import CryptContext

from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SAFE_LOOKUP_VALUE_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.@:-]{0,254}$")


def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password must not be empty")

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not plain_password or not hashed_password:
        return False

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    subject: str,
    expires_delta: timedelta | None = None,
    extra_claims: Mapping[str, Any] | None = None,
) -> str:
    if not subject:
        raise ValueError("Token subject must not be empty")

    now = datetime.now(timezone.utc)
    expires_at = now + (
        expires_delta or timedelta(minutes=settings.jwt_access_token_expire_minutes)
    )
    payload: dict[str, Any] = {
        "sub": subject,
        "type": "access",
        "iat": int(now.timestamp()),
        "nbf": int(now.timestamp()),
        "exp": int(expires_at.timestamp()),
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
    }

    if extra_claims:
        payload.update(dict(extra_claims))

    return jwt.encode(
        payload,
        settings.jwt_secret_key.get_secret_value(),
        algorithm=settings.jwt_algorithm,
    )


def decode_access_token(token: str) -> dict[str, Any]:
    return jwt.decode(
        token,
        settings.jwt_secret_key.get_secret_value(),
        algorithms=[settings.jwt_algorithm],
        audience=settings.jwt_audience,
        issuer=settings.jwt_issuer,
        leeway=5,
    )


def validate_safe_lookup_value(value: str, field_name: str = "value") -> str:
    normalized_value = value.strip()

    if not normalized_value:
        raise ValueError(f"{field_name} must not be empty")

    if not SAFE_LOOKUP_VALUE_PATTERN.fullmatch(normalized_value):
        raise ValueError(f"{field_name} contains unsupported characters")

    return normalized_value

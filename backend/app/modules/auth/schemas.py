from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator


EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def normalize_and_validate_email(value: str) -> str:
    normalized_value = value.strip().lower()

    if not normalized_value:
        raise ValueError("Email must not be empty")

    if len(normalized_value) > 320:
        raise ValueError("Email must be at most 320 characters long")

    if not EMAIL_PATTERN.fullmatch(normalized_value):
        raise ValueError("Enter a valid email address")

    return normalized_value


class RegisterRequest(BaseModel):
    email: str
    password: str
    full_name: str | None = Field(default=None, max_length=255)

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return normalize_and_validate_email(value)

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password must be at most 72 bytes long")

        return value

    @field_validator("full_name")
    @classmethod
    def normalize_full_name(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()
        return normalized_value or None


class LoginRequest(BaseModel):
    email: str
    password: str = Field(min_length=1)

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return normalize_and_validate_email(value)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ErrorResponse(BaseModel):
    detail: str


class TokenPayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    sub: str
    type: str

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "TokenPayload":
        return cls.model_validate(payload)

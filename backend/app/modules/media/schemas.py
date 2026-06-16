from __future__ import annotations

import re
from datetime import datetime

from pydantic import BaseModel, Field, field_validator


SAFE_FILENAME_PATTERN = re.compile(r"[^A-Za-z0-9._-]+")
WINDOWS_ABSOLUTE_PATH_PATTERN = re.compile(r"^[A-Za-z]:\\")


def sanitize_original_filename(value: str | None, *, fallback_extension: str) -> str:
    raw_value = (value or "").replace("\\", "/").split("/")[-1].strip()
    sanitized_value = SAFE_FILENAME_PATTERN.sub("_", raw_value).strip("._")

    if not sanitized_value:
        return f"upload{fallback_extension}"

    if "." not in sanitized_value:
        sanitized_value = f"{sanitized_value}{fallback_extension}"

    if len(sanitized_value) > 255:
        stem, dot, suffix = sanitized_value.rpartition(".")
        if dot:
            max_stem_length = max(1, 255 - len(suffix) - 1)
            sanitized_value = f"{stem[:max_stem_length]}.{suffix}"
        else:
            sanitized_value = sanitized_value[:255]

    return sanitized_value


class MediaUploadRequest(BaseModel):
    profile_id: int | None = Field(default=None, gt=0)


class MediaAssetRead(BaseModel):
    id: int
    owner_id: int
    profile_id: int | None
    media_type: str
    storage_provider: str
    storage_key: str
    original_filename: str
    mime_type: str
    size_bytes: int
    public_url: str
    created_at: datetime

    @field_validator("storage_key")
    @classmethod
    def reject_absolute_storage_keys(cls, value: str) -> str:
        if value.startswith("/") or WINDOWS_ABSOLUTE_PATH_PATTERN.match(value):
            raise ValueError("Absolute filesystem paths are not allowed")

        return value

    @field_validator("public_url")
    @classmethod
    def reject_absolute_filesystem_public_urls(cls, value: str) -> str:
        if value.startswith("/app/") or WINDOWS_ABSOLUTE_PATH_PATTERN.match(value):
            raise ValueError("Absolute filesystem paths are not allowed")

        return value

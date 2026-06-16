from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from app.core.config import settings
from app.modules.media.storage.base import StorageProvider


SAFE_STORAGE_KEY_CHARS = frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_/.")


class LocalStorageProvider(StorageProvider):
    provider_name = "local"

    def __init__(self, media_root: Path | None = None, public_base_url: str | None = None) -> None:
        self.media_root = (media_root or settings.media_root).resolve()
        self.public_base_url = public_base_url or settings.media_public_base_url

    def save_bytes(
        self,
        *,
        content: bytes,
        media_type: str,
        extension: str,
    ) -> str:
        storage_key = self._generate_storage_key(
            media_type=media_type,
            extension=extension,
        )
        destination = self._resolve_storage_path(storage_key)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        return storage_key

    def delete_file(self, *, storage_key: str) -> None:
        destination = self._resolve_storage_path(storage_key)
        if destination.exists():
            destination.unlink()

    def build_public_url(self, *, storage_key: str) -> str:
        return f"{self.public_base_url.rstrip('/')}/{storage_key}"

    def _generate_storage_key(self, *, media_type: str, extension: str) -> str:
        timestamp = datetime.now(UTC)
        normalized_extension = extension if extension.startswith(".") else f".{extension}"
        safe_extension = normalized_extension.lower()
        return (
            f"{media_type}/"
            f"{timestamp:%Y/%m/%d}/"
            f"{uuid4().hex}{safe_extension}"
        )

    def _resolve_storage_path(self, storage_key: str) -> Path:
        if not storage_key or any(character not in SAFE_STORAGE_KEY_CHARS for character in storage_key):
            raise ValueError("Invalid storage key")

        resolved_path = (self.media_root / storage_key).resolve()
        resolved_path.relative_to(self.media_root)
        return resolved_path

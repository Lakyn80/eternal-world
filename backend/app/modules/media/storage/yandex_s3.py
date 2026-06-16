from __future__ import annotations

from app.modules.media.storage.base import StorageProvider


class YandexS3StorageProvider(StorageProvider):
    provider_name = "yandex_s3"

    def save_bytes(
        self,
        *,
        content: bytes,
        media_type: str,
        extension: str,
    ) -> str:
        raise NotImplementedError("Yandex Object Storage integration is not implemented yet")

    def delete_file(self, *, storage_key: str) -> None:
        raise NotImplementedError("Yandex Object Storage integration is not implemented yet")

    def build_public_url(self, *, storage_key: str) -> str:
        raise NotImplementedError("Yandex Object Storage integration is not implemented yet")

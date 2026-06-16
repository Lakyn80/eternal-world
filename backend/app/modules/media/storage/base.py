from __future__ import annotations

from abc import ABC, abstractmethod


class StorageProvider(ABC):
    provider_name: str

    @abstractmethod
    def save_bytes(
        self,
        *,
        content: bytes,
        media_type: str,
        extension: str,
    ) -> str:
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, *, storage_key: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def build_public_url(self, *, storage_key: str) -> str:
        raise NotImplementedError

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


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

    def get_local_file_path(self, *, storage_key: str) -> Path:
        raise NotImplementedError("This storage provider does not expose local files")

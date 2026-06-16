from app.modules.media.storage.base import StorageProvider
from app.modules.media.storage.local import LocalStorageProvider
from app.modules.media.storage.yandex_s3 import YandexS3StorageProvider


def get_storage_provider(storage_provider_name: str) -> StorageProvider:
    if storage_provider_name == LocalStorageProvider.provider_name:
        return LocalStorageProvider()

    if storage_provider_name == YandexS3StorageProvider.provider_name:
        return YandexS3StorageProvider()

    raise ValueError(f"Unsupported media storage provider: {storage_provider_name}")

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import MediaAsset, User
from app.modules.media import repository
from app.modules.media.schemas import MediaAssetRead, MediaUploadRequest, sanitize_original_filename
from app.modules.media.storage import get_storage_provider
from app.modules.memory_profiles import repository as memory_profiles_repository


@dataclass(frozen=True)
class AllowedMimeType:
    media_type: str
    extension: str


@dataclass(frozen=True)
class LocalMediaFile:
    file_path: Path
    mime_type: str
    original_filename: str


ALLOWED_MIME_TYPES: dict[str, AllowedMimeType] = {
    "image/jpeg": AllowedMimeType(media_type="image", extension=".jpg"),
    "image/png": AllowedMimeType(media_type="image", extension=".png"),
    "image/webp": AllowedMimeType(media_type="image", extension=".webp"),
    "audio/mpeg": AllowedMimeType(media_type="audio", extension=".mp3"),
    "audio/wav": AllowedMimeType(media_type="audio", extension=".wav"),
    "video/mp4": AllowedMimeType(media_type="video", extension=".mp4"),
}


class MediaAssetNotFoundError(Exception):
    pass


class MediaProfileNotFoundError(Exception):
    pass


class UnsupportedMediaTypeError(Exception):
    pass


class MediaTooLargeError(Exception):
    pass


class MediaFileNotFoundError(Exception):
    pass


def _get_owned_profile_or_raise(
    db: Session,
    *,
    owner_id: int,
    profile_id: int,
):
    profile = memory_profiles_repository.get_memory_profile_for_user(
        db,
        user_id=owner_id,
        profile_id=profile_id,
    )
    if profile is None:
        raise MediaProfileNotFoundError("Memory profile not found")

    return profile


def _get_owned_media_or_raise(
    db: Session,
    *,
    owner_id: int,
    media_id: int,
) -> MediaAsset:
    media_asset = repository.get_media_asset_for_owner(
        db,
        owner_id=owner_id,
        media_id=media_id,
    )
    if media_asset is None:
        raise MediaAssetNotFoundError("Media not found")

    return media_asset


def _build_media_response(media_asset: MediaAsset) -> MediaAssetRead:
    storage_provider = get_storage_provider(media_asset.storage_provider)
    return MediaAssetRead(
        id=media_asset.id,
        owner_id=media_asset.owner_id,
        profile_id=media_asset.profile_id,
        media_type=media_asset.media_type,
        storage_provider=media_asset.storage_provider,
        storage_key=media_asset.storage_key,
        original_filename=media_asset.original_filename,
        mime_type=media_asset.mime_type,
        size_bytes=media_asset.size_bytes,
        public_url=storage_provider.build_public_url(storage_key=media_asset.storage_key),
        created_at=media_asset.created_at,
    )


def create_media_asset(
    db: Session,
    *,
    current_user: User,
    payload: MediaUploadRequest,
    original_filename: str | None,
    mime_type: str | None,
    content: bytes,
) -> MediaAssetRead:
    mime_spec = ALLOWED_MIME_TYPES.get(mime_type or "")
    if mime_spec is None:
        raise UnsupportedMediaTypeError("Unsupported media type")

    if len(content) > settings.media_max_file_size_bytes:
        raise MediaTooLargeError("File is too large")

    if payload.profile_id is not None:
        _get_owned_profile_or_raise(
            db,
            owner_id=current_user.id,
            profile_id=payload.profile_id,
        )

    storage_provider = get_storage_provider(settings.media_storage_provider)
    sanitized_filename = sanitize_original_filename(
        original_filename,
        fallback_extension=mime_spec.extension,
    )
    storage_key = storage_provider.save_bytes(
        content=content,
        media_type=mime_spec.media_type,
        extension=mime_spec.extension,
    )

    try:
        media_asset = repository.create_media_asset(
            db,
            owner_id=current_user.id,
            profile_id=payload.profile_id,
            media_type=mime_spec.media_type,
            storage_provider=storage_provider.provider_name,
            storage_key=storage_key,
            original_filename=sanitized_filename,
            mime_type=mime_type or "",
            size_bytes=len(content),
        )
        db.commit()
    except Exception:
        db.rollback()
        try:
            storage_provider.delete_file(storage_key=storage_key)
        except Exception:
            pass
        raise

    db.refresh(media_asset)
    return _build_media_response(media_asset)


def list_media_assets(
    db: Session,
    *,
    current_user: User,
) -> list[MediaAssetRead]:
    media_assets = repository.list_media_assets_for_owner(db, current_user.id)
    return [_build_media_response(media_asset) for media_asset in media_assets]


def get_media_asset(
    db: Session,
    *,
    current_user: User,
    media_id: int,
) -> MediaAssetRead:
    media_asset = _get_owned_media_or_raise(
        db,
        owner_id=current_user.id,
        media_id=media_id,
    )
    return _build_media_response(media_asset)


def get_local_media_file(
    db: Session,
    *,
    storage_key: str,
) -> LocalMediaFile:
    media_asset = repository.get_media_asset_by_storage_key(
        db,
        storage_key=storage_key,
    )
    if media_asset is None:
        raise MediaFileNotFoundError("Media file not found")

    storage_provider = get_storage_provider(media_asset.storage_provider)
    try:
        file_path = storage_provider.get_local_file_path(storage_key=media_asset.storage_key)
    except (FileNotFoundError, NotImplementedError, ValueError) as exc:
        raise MediaFileNotFoundError("Media file not found") from exc

    return LocalMediaFile(
        file_path=file_path,
        mime_type=media_asset.mime_type,
        original_filename=media_asset.original_filename,
    )


def delete_media_asset(
    db: Session,
    *,
    current_user: User,
    media_id: int,
) -> None:
    media_asset = _get_owned_media_or_raise(
        db,
        owner_id=current_user.id,
        media_id=media_id,
    )
    storage_provider = get_storage_provider(media_asset.storage_provider)
    storage_provider.delete_file(storage_key=media_asset.storage_key)
    repository.delete_media_asset(db, media_asset)
    db.commit()

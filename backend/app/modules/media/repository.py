from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import MediaAsset


def create_media_asset(
    db: Session,
    *,
    owner_id: int,
    profile_id: int | None,
    media_type: str,
    storage_provider: str,
    storage_key: str,
    original_filename: str,
    mime_type: str,
    size_bytes: int,
) -> MediaAsset:
    media_asset = MediaAsset(
        owner_id=owner_id,
        profile_id=profile_id,
        media_type=media_type,
        storage_provider=storage_provider,
        storage_key=storage_key,
        original_filename=original_filename,
        mime_type=mime_type,
        size_bytes=size_bytes,
    )
    db.add(media_asset)
    return media_asset


def list_media_assets_for_owner(db: Session, owner_id: int) -> list[MediaAsset]:
    statement = (
        select(MediaAsset)
        .where(MediaAsset.owner_id == owner_id)
        .order_by(MediaAsset.id.asc())
    )
    return list(db.scalars(statement))


def get_media_asset_for_owner(
    db: Session,
    *,
    owner_id: int,
    media_id: int,
) -> MediaAsset | None:
    statement = select(MediaAsset).where(
        MediaAsset.id == media_id,
        MediaAsset.owner_id == owner_id,
    )
    return db.scalar(statement)


def get_media_asset_by_storage_key(
    db: Session,
    *,
    storage_key: str,
) -> MediaAsset | None:
    statement = select(MediaAsset).where(MediaAsset.storage_key == storage_key)
    return db.scalar(statement)


def delete_media_asset(db: Session, media_asset: MediaAsset) -> None:
    db.delete(media_asset)

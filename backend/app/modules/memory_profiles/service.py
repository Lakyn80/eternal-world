from __future__ import annotations

from datetime import date

from sqlalchemy.orm import Session

from app.db.models import MemoryProfile, User
from app.modules.billing.service import enforce_memory_profile_creation_limit
from app.modules.media import repository as media_repository
from app.modules.memory_profiles import repository
from app.modules.memory_profiles.schemas import (
    MemoryProfileCreate,
    MemoryProfilePhotoAssign,
    MemoryProfileUpdate,
)


ALLOWED_PROFILE_PHOTO_MIME_TYPES = frozenset(
    {
        "image/jpeg",
        "image/png",
        "image/webp",
    }
)


class MemoryProfileNotFoundError(Exception):
    pass


class MemoryProfilePhotoMediaNotFoundError(Exception):
    pass


class InvalidMemoryProfilePhotoError(Exception):
    pass


def _validate_profile_dates(
    birth_date: date | None,
    death_date: date | None,
) -> None:
    if birth_date is not None and death_date is not None and death_date < birth_date:
        raise ValueError("death_date must be on or after birth_date")


def create_memory_profile(
    db: Session,
    *,
    current_user: User,
    payload: MemoryProfileCreate,
) -> MemoryProfile:
    current_profiles = repository.count_memory_profiles_for_user(db, current_user.id)
    enforce_memory_profile_creation_limit(
        current_user=current_user,
        current_profiles=current_profiles,
    )
    memory_profile = repository.create_memory_profile(
        db,
        user_id=current_user.id,
        **payload.model_dump(),
    )
    db.commit()
    db.refresh(memory_profile)
    return memory_profile


def list_memory_profiles(
    db: Session,
    *,
    current_user: User,
) -> list[MemoryProfile]:
    return repository.list_memory_profiles_for_user(db, current_user.id)


def get_memory_profile(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> MemoryProfile:
    memory_profile = repository.get_memory_profile_for_user(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    if memory_profile is None:
        raise MemoryProfileNotFoundError("Memory profile not found")

    return memory_profile


def update_memory_profile(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: MemoryProfileUpdate,
) -> MemoryProfile:
    memory_profile = get_memory_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    update_data = payload.model_dump(exclude_unset=True)

    if update_data:
        birth_date = update_data.get("birth_date", memory_profile.birth_date)
        death_date = update_data.get("death_date", memory_profile.death_date)
        _validate_profile_dates(birth_date, death_date)

        for field_name, value in update_data.items():
            setattr(memory_profile, field_name, value)

        db.commit()
        db.refresh(memory_profile)

    return memory_profile


def assign_memory_profile_photo(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: MemoryProfilePhotoAssign,
) -> MemoryProfile:
    memory_profile = get_memory_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    media_asset = media_repository.get_media_asset_for_owner(
        db,
        owner_id=current_user.id,
        media_id=payload.media_id,
    )
    if media_asset is None:
        raise MemoryProfilePhotoMediaNotFoundError("Media not found")

    if media_asset.media_type != "image" or media_asset.mime_type not in ALLOWED_PROFILE_PHOTO_MIME_TYPES:
        raise InvalidMemoryProfilePhotoError("Profile photo must be an image")

    if memory_profile.main_photo_media_id != media_asset.id:
        memory_profile.main_photo_media_id = media_asset.id
        db.commit()
        db.refresh(memory_profile)

    return memory_profile


def remove_memory_profile_photo(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> MemoryProfile:
    memory_profile = get_memory_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )

    if memory_profile.main_photo_media_id is not None:
        memory_profile.main_photo_media_id = None
        db.commit()
        db.refresh(memory_profile)

    return memory_profile


def delete_memory_profile(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> None:
    memory_profile = get_memory_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    db.delete(memory_profile)
    db.commit()

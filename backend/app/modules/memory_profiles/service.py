from __future__ import annotations

from datetime import date

from sqlalchemy.orm import Session

from app.db.models import MemoryProfile, User
from app.modules.memory_profiles import repository
from app.modules.memory_profiles.schemas import MemoryProfileCreate, MemoryProfileUpdate


class MemoryProfileNotFoundError(Exception):
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

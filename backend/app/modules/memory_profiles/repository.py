from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.db.models import MemoryProfile


MEMORY_PROFILE_LOAD_OPTIONS = (
    selectinload(MemoryProfile.main_photo_media),
)


def create_memory_profile(
    db: Session,
    *,
    user_id: int,
    name: str,
    birth_date,
    death_date,
    biography: str | None,
    personality: str | None,
    catchphrases: str | None,
    is_public: bool,
) -> MemoryProfile:
    memory_profile = MemoryProfile(
        user_id=user_id,
        name=name,
        birth_date=birth_date,
        death_date=death_date,
        biography=biography,
        personality=personality,
        catchphrases=catchphrases,
        is_public=is_public,
    )
    db.add(memory_profile)
    return memory_profile


def list_memory_profiles_for_user(db: Session, user_id: int) -> list[MemoryProfile]:
    statement = (
        select(MemoryProfile)
        .options(*MEMORY_PROFILE_LOAD_OPTIONS)
        .where(MemoryProfile.user_id == user_id)
        .order_by(MemoryProfile.id.asc())
    )
    return list(db.scalars(statement))


def count_memory_profiles_for_user(db: Session, user_id: int) -> int:
    statement = select(func.count(MemoryProfile.id)).where(MemoryProfile.user_id == user_id)
    return int(db.scalar(statement) or 0)


def get_memory_profile_for_user(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
) -> MemoryProfile | None:
    statement = (
        select(MemoryProfile)
        .options(*MEMORY_PROFILE_LOAD_OPTIONS)
        .where(
            MemoryProfile.id == profile_id,
            MemoryProfile.user_id == user_id,
        )
    )
    return db.scalar(statement)

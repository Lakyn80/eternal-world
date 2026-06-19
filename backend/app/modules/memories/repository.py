from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.db.models import Memory, MemoryProfile


MEMORY_LOAD_OPTIONS = (
    selectinload(Memory.media_asset),
    selectinload(Memory.memory_profile),
)


def create_memory(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
    title: str,
    content: str | None,
    memory_type: str,
    occurred_at,
    occurred_year: int | None,
    media_id: int | None,
) -> Memory:
    memory = Memory(
        user_id=user_id,
        memory_profile_id=profile_id,
        title=title,
        content=content,
        memory_type=memory_type,
        occurred_at=occurred_at,
        occurred_year=occurred_year,
        media_id=media_id,
    )
    db.add(memory)
    return memory


def list_memories_for_profile(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
) -> list[Memory]:
    statement = (
        select(Memory)
        .options(*MEMORY_LOAD_OPTIONS)
        .where(
            Memory.user_id == user_id,
            Memory.memory_profile_id == profile_id,
        )
        .order_by(
            Memory.occurred_at.desc().nullslast(),
            Memory.occurred_year.desc().nullslast(),
            Memory.created_at.desc(),
            Memory.id.desc(),
        )
    )
    return list(db.scalars(statement))


def get_memory_for_user(
    db: Session,
    *,
    user_id: int,
    memory_id: int,
) -> Memory | None:
    statement = (
        select(Memory)
        .options(*MEMORY_LOAD_OPTIONS)
        .join(MemoryProfile, Memory.memory_profile_id == MemoryProfile.id)
        .where(
            Memory.id == memory_id,
            Memory.user_id == user_id,
            MemoryProfile.user_id == user_id,
        )
    )
    return db.scalar(statement)


def count_memories_for_user(db: Session, user_id: int) -> int:
    statement = select(func.count(Memory.id)).where(Memory.user_id == user_id)
    return int(db.scalar(statement) or 0)

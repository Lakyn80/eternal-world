from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models import Memory, MediaAsset, User
from app.modules.billing.service import enforce_memory_creation_limit
from app.modules.media import repository as media_repository
from app.modules.memories import repository
from app.modules.memories.schemas import MemoryCreate, MemoryUpdate
from app.modules.memory_profiles import repository as memory_profiles_repository


ALLOWED_MEMORY_MEDIA_MIME_TYPES: dict[str, frozenset[str]] = {
    "photo": frozenset({"image/jpeg", "image/png", "image/webp"}),
    "audio": frozenset({"audio/mpeg", "audio/wav"}),
    "video": frozenset({"video/mp4"}),
}


class MemoryNotFoundError(Exception):
    pass


class MemoryProfileNotFoundError(Exception):
    pass


class MemoryMediaNotFoundError(Exception):
    pass


class InvalidMemoryMediaError(Exception):
    pass


def _get_owned_profile_or_raise(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
):
    profile = memory_profiles_repository.get_memory_profile_for_user(
        db,
        user_id=user_id,
        profile_id=profile_id,
    )
    if profile is None:
        raise MemoryProfileNotFoundError("Memory profile not found")

    return profile


def _get_owned_media_or_raise(
    db: Session,
    *,
    user_id: int,
    media_id: int,
) -> MediaAsset:
    media_asset = media_repository.get_media_asset_for_owner(
        db,
        owner_id=user_id,
        media_id=media_id,
    )
    if media_asset is None:
        raise MemoryMediaNotFoundError("Media not found")

    return media_asset


def _validate_media_for_memory(
    db: Session,
    *,
    user_id: int,
    memory_type: str,
    media_id: int | None,
) -> None:
    if media_id is None:
        return

    if memory_type == "text":
        raise InvalidMemoryMediaError("Media is not compatible with memory type")

    media_asset = _get_owned_media_or_raise(
        db,
        user_id=user_id,
        media_id=media_id,
    )
    allowed_mime_types = ALLOWED_MEMORY_MEDIA_MIME_TYPES.get(memory_type, frozenset())
    if media_asset.mime_type not in allowed_mime_types:
        raise InvalidMemoryMediaError("Media is not compatible with memory type")


def create_memory(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: MemoryCreate,
) -> Memory:
    _get_owned_profile_or_raise(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    current_memories = repository.count_memories_for_user(db, current_user.id)
    enforce_memory_creation_limit(
        current_user=current_user,
        current_memories=current_memories,
    )
    _validate_media_for_memory(
        db,
        user_id=current_user.id,
        memory_type=payload.memory_type,
        media_id=payload.media_id,
    )
    memory = repository.create_memory(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        title=payload.title,
        content=payload.content,
        memory_type=payload.memory_type,
        occurred_at=payload.occurred_at,
        occurred_year=payload.occurred_year,
        media_id=payload.media_id,
    )
    db.commit()
    db.refresh(memory)
    return memory


def list_memories(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> list[Memory]:
    _get_owned_profile_or_raise(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    return repository.list_memories_for_profile(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )


def get_memory(
    db: Session,
    *,
    current_user: User,
    memory_id: int,
) -> Memory:
    memory = repository.get_memory_for_user(
        db,
        user_id=current_user.id,
        memory_id=memory_id,
    )
    if memory is None:
        raise MemoryNotFoundError("Memory not found")

    return memory


def update_memory(
    db: Session,
    *,
    current_user: User,
    memory_id: int,
    payload: MemoryUpdate,
) -> Memory:
    memory = get_memory(
        db,
        current_user=current_user,
        memory_id=memory_id,
    )
    update_data = payload.model_dump(exclude_unset=True)
    if not update_data:
        return memory

    updated_memory_type = update_data.get("memory_type", memory.memory_type)
    updated_media_id = update_data.get("media_id", memory.media_id)
    _validate_media_for_memory(
        db,
        user_id=current_user.id,
        memory_type=updated_memory_type,
        media_id=updated_media_id,
    )

    for field_name, value in update_data.items():
        setattr(memory, field_name, value)

    db.commit()
    db.refresh(memory)
    return memory


def delete_memory(
    db: Session,
    *,
    current_user: User,
    memory_id: int,
) -> None:
    memory = get_memory(
        db,
        current_user=current_user,
        memory_id=memory_id,
    )
    db.delete(memory)
    db.commit()

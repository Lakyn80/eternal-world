from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models import RagSource, User
from app.modules.memory_profiles import repository as memory_profiles_repository
from app.modules.rag_sources import repository
from app.modules.rag_sources.schemas import (
    READY_FOR_CLEANING_STATUS,
    RagSourceCreate,
    RagSourceUpdate,
)


class RagSourceNotFoundError(Exception):
    pass


class RagSourceProfileNotFoundError(Exception):
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
        raise RagSourceProfileNotFoundError("Memory profile not found")

    return profile


def _normalize_raw_text(raw_text: str) -> str:
    return raw_text


def create_rag_source(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: RagSourceCreate,
) -> RagSource:
    _get_owned_profile_or_raise(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    normalized_text = _normalize_raw_text(payload.raw_text)
    rag_source = repository.create_rag_source(
        db,
        owner_user_id=current_user.id,
        profile_id=profile_id,
        source_type=payload.source_type,
        title=payload.title,
        raw_text=payload.raw_text,
        normalized_text=normalized_text,
        language=payload.language,
        status=READY_FOR_CLEANING_STATUS,
        processing_error=None,
        source_metadata=payload.source_metadata,
    )
    db.commit()
    db.refresh(rag_source)
    return rag_source


def list_rag_sources(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> list[RagSource]:
    _get_owned_profile_or_raise(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    return repository.list_rag_sources_for_profile(
        db,
        owner_user_id=current_user.id,
        profile_id=profile_id,
    )


def get_rag_source(
    db: Session,
    *,
    current_user: User,
    source_id: int,
) -> RagSource:
    rag_source = repository.get_rag_source_for_user(
        db,
        owner_user_id=current_user.id,
        source_id=source_id,
    )
    if rag_source is None:
        raise RagSourceNotFoundError("RAG source not found")

    return rag_source


def update_rag_source(
    db: Session,
    *,
    current_user: User,
    source_id: int,
    payload: RagSourceUpdate,
) -> RagSource:
    rag_source = get_rag_source(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    update_data = payload.model_dump(exclude_unset=True)
    if not update_data:
        return rag_source

    raw_text_changed = False
    if "raw_text" in update_data and update_data["raw_text"] != rag_source.raw_text:
        raw_text_changed = True

    for field_name, value in update_data.items():
        setattr(rag_source, field_name, value)

    if raw_text_changed:
        rag_source.normalized_text = _normalize_raw_text(rag_source.raw_text)
        rag_source.status = READY_FOR_CLEANING_STATUS
        rag_source.processing_error = None

    db.commit()
    db.refresh(rag_source)
    return rag_source


def delete_rag_source(
    db: Session,
    *,
    current_user: User,
    source_id: int,
) -> None:
    rag_source = get_rag_source(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    db.delete(rag_source)
    db.commit()

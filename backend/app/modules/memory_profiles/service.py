from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import date

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.db.models import MemoryProfile, RagChunk, RagEmbedding, RagSource, User
from app.modules.avatar_memory_indexing.qdrant_writer import (
    AvatarMemoryQdrantWriter,
    DefaultAvatarMemoryQdrantWriter,
)
from app.modules.billing.service import enforce_memory_profile_creation_limit
from app.modules.media import repository as media_repository
from app.modules.memory_profiles import repository
from app.modules.memory_profiles.schemas import (
    MemoryProfileCreate,
    MemoryProfilePhotoAssign,
    MemoryProfileUpdate,
)
from app.modules.qdrant_indexing import repository as qdrant_indexing_repository


logger = get_logger(__name__)


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


class MemoryProfileDeletionFailedError(Exception):
    """Raised when one or more indexed Qdrant points for the profile could not
    be deleted - the profile row is deliberately left untouched in this case
    (Task 65.5: never claim a successful deletion if DB data is gone but
    retrievable vectors remain)."""


@dataclass(frozen=True)
class MemoryProfileDeletionResult:
    profile_id: int
    vector_points_removed: int


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
    from app.modules.language_registry.persona_sync import sync_persona_languages_to_canonical, utcnow

    current_profiles = repository.count_memory_profiles_for_user(db, current_user.id)
    enforce_memory_profile_creation_limit(
        current_user=current_user,
        current_profiles=current_profiles,
    )
    profile_fields = payload.model_dump(exclude={"confirm_canonical_language"})
    memory_profile = repository.create_memory_profile(
        db,
        user_id=current_user.id,
        canonical_language_source="creator_preference",
        canonical_language_locked_at=utcnow(),
        **profile_fields,
    )
    db.flush()
    sync_persona_languages_to_canonical(db, profile=memory_profile)
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
    writer: AvatarMemoryQdrantWriter | None = None,
) -> MemoryProfileDeletionResult:
    """Task 65.5: deletes a memorial the owner controls, but only after every
    Qdrant point indexed for it has been confirmed removed.

    `get_memory_profile` already scopes the lookup to `user_id ==
    current_user.id`, so this stays owner-only and cannot touch another
    user's profile. Qdrant cleanup happens strictly before the DB row is
    deleted: the `RagVectorIndex` rows are the only record of which
    `qdrant_point_id`s belong to this profile, so deleting the profile first
    would make the points impossible to find and clean up afterwards.

    If any point fails to delete, the whole operation aborts without
    touching the database - partial success would otherwise leave the DB
    record gone while its vectors remain retrievable, which is explicitly
    disallowed. A retry after a partial failure is safe: points already
    removed simply won't be found again by `list_vector_indexes_for_profile`
    once cleaned up on a following successful attempt, and deleting an
    already-absent Qdrant point is a no-op for the underlying client.

    Most dependent rows (memberships, invitations, biography ingestion jobs,
    RagVectorIndex, Biographer questions, memory candidates, contributions,
    review records, promotions, etc.) are declared with
    `cascade="all, delete-orphan"` on the `MemoryProfile` relationship, so
    the ORM deletes them correctly on `db.delete(memory_profile)` regardless
    of the underlying DB engine. `RagSource`/`RagChunk`/`RagEmbedding` are
    the one exception: their `MemoryProfile` relationship carries no ORM
    cascade, and their `profile_id` column is NOT NULL, so instead of
    relying on the DB's `ON DELETE CASCADE` (which SQLAlchemy's ORM does not
    trust by default - it would try to null the FK instead, which is a
    non-nullable column and violates the constraint), they are explicitly
    bulk-deleted here, child-first, before the profile itself is deleted.
    Chat messages and free-standing `Memory` records intentionally use
    `ON DELETE SET NULL` instead - they belong to the user's account, not
    exclusively to this memorial, so they are meant to outlive it.
    """

    memory_profile = get_memory_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )

    actual_writer = writer or DefaultAvatarMemoryQdrantWriter()
    vector_indexes = qdrant_indexing_repository.list_vector_indexes_for_profile(
        db,
        owner_user_id=current_user.id,
        profile_id=memory_profile.id,
    )

    for vector_index in vector_indexes:
        try:
            actual_writer.delete_point(
                collection_name=vector_index.qdrant_collection,
                point_id=vector_index.qdrant_point_id,
            )
        except Exception as exc:
            log_event(
                logger,
                logging.ERROR,
                "memory_profile_delete_vector_cleanup_failed",
                profile_id=memory_profile.id,
                error_type=exc.__class__.__name__,
            )
            raise MemoryProfileDeletionFailedError(
                "Failed to remove all indexed memory vectors; memorial was not deleted"
            ) from exc

    db.query(RagEmbedding).filter(RagEmbedding.profile_id == memory_profile.id).delete(
        synchronize_session=False
    )
    db.query(RagChunk).filter(RagChunk.profile_id == memory_profile.id).delete(synchronize_session=False)
    db.query(RagSource).filter(RagSource.profile_id == memory_profile.id).delete(synchronize_session=False)

    db.delete(memory_profile)
    db.commit()
    log_event(
        logger,
        logging.INFO,
        "memory_profile_deleted",
        profile_id=profile_id,
        vector_points_removed=len(vector_indexes),
    )
    return MemoryProfileDeletionResult(
        profile_id=profile_id,
        vector_points_removed=len(vector_indexes),
    )

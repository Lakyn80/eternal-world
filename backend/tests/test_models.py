from app.db.base import Base
from app.db.models import ChatMessage, MediaAsset, Memory, MemoryProfile, User


def test_database_models_are_registered():
    assert User.__tablename__ == "users"
    assert MemoryProfile.__tablename__ == "memory_profiles"
    assert ChatMessage.__tablename__ == "chat_messages"
    assert Memory.__tablename__ == "memories"
    assert MediaAsset.__tablename__ == "media_assets"
    assert "full_name" in User.__table__.columns.keys()
    assert {
        "main_photo_media_id",
        "name",
        "birth_date",
        "death_date",
        "biography",
        "personality",
        "catchphrases",
        "is_public",
    }.issubset(
        MemoryProfile.__table__.columns.keys()
    )
    assert {
        "owner_id",
        "profile_id",
        "media_type",
        "storage_provider",
        "storage_key",
        "original_filename",
        "mime_type",
        "size_bytes",
    }.issubset(MediaAsset.__table__.columns.keys())
    assert {
        "user_id",
        "memory_profile_id",
        "title",
        "memory_type",
        "content",
        "occurred_at",
        "occurred_year",
        "media_id",
    }.issubset(Memory.__table__.columns.keys())

    assert {"users", "memory_profiles", "chat_messages", "memories", "media_assets"}.issubset(
        Base.metadata.tables.keys()
    )

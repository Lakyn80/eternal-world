from app.db.base import Base
from app.db.models import ChatMessage, MediaAsset, Memory, MemoryProfile, RagChunk, RagSource, User


def test_database_models_are_registered():
    assert User.__tablename__ == "users"
    assert MemoryProfile.__tablename__ == "memory_profiles"
    assert ChatMessage.__tablename__ == "chat_messages"
    assert Memory.__tablename__ == "memories"
    assert MediaAsset.__tablename__ == "media_assets"
    assert RagSource.__tablename__ == "rag_sources"
    assert RagChunk.__tablename__ == "rag_chunks"
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
    assert {
        "owner_user_id",
        "profile_id",
        "source_type",
        "title",
        "raw_text",
        "normalized_text",
        "language",
        "status",
        "processing_error",
        "source_metadata",
    }.issubset(RagSource.__table__.columns.keys())
    assert {
        "owner_user_id",
        "profile_id",
        "source_id",
        "chunk_index",
        "chunk_text",
        "text_hash",
        "token_estimate",
        "char_count",
        "sentence_count",
        "language",
        "chunk_metadata",
        "validation_status",
        "validation_errors",
    }.issubset(RagChunk.__table__.columns.keys())

    assert {"users", "memory_profiles", "chat_messages", "memories", "media_assets", "rag_sources", "rag_chunks"}.issubset(
        Base.metadata.tables.keys()
    )

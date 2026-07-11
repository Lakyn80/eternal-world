from app.db.base import Base
from app.db.models import (
    ActiveRetrievalConfig,
    BackgroundJob,
    ChatMessage,
    ConversationMemoryCandidate,
    MediaAsset,
    Memory,
    MemoryProfile,
    RagChunk,
    RagEmbedding,
    RagSource,
    RagVectorIndex,
    User,
)


def test_database_models_are_registered():
    assert User.__tablename__ == "users"
    assert MemoryProfile.__tablename__ == "memory_profiles"
    assert ChatMessage.__tablename__ == "chat_messages"
    assert Memory.__tablename__ == "memories"
    assert MediaAsset.__tablename__ == "media_assets"
    assert RagSource.__tablename__ == "rag_sources"
    assert RagChunk.__tablename__ == "rag_chunks"
    assert RagEmbedding.__tablename__ == "rag_embeddings"
    assert RagVectorIndex.__tablename__ == "rag_vector_indexes"
    assert BackgroundJob.__tablename__ == "background_jobs"
    assert ActiveRetrievalConfig.__tablename__ == "active_retrieval_configs"
    assert ConversationMemoryCandidate.__tablename__ == "conversation_memory_candidates"
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
    assert {
        "owner_user_id",
        "profile_id",
        "source_id",
        "chunk_id",
        "model_code",
        "vector",
        "vector_dimension",
        "text_hash",
        "status",
        "error_message",
        "embedding_metadata",
    }.issubset(RagEmbedding.__table__.columns.keys())
    assert {
        "owner_user_id",
        "profile_id",
        "source_id",
        "chunk_id",
        "embedding_id",
        "model_code",
        "qdrant_collection",
        "qdrant_point_id",
        "status",
        "error_message",
        "indexed_at",
    }.issubset(RagVectorIndex.__table__.columns.keys())
    assert {
        "owner_user_id",
        "profile_id",
        "job_type",
        "status",
        "progress_current",
        "progress_total",
        "celery_task_id",
        "input_payload",
        "result_payload",
        "error_payload",
        "error_message",
        "started_at",
        "finished_at",
    }.issubset(BackgroundJob.__table__.columns.keys())
    assert {
        "owner_user_id",
        "avatar_id",
        "conversation_id",
        "trace_id",
        "source",
        "status",
        "confidence",
        "user_message_excerpt",
        "proposed_memory_text",
        "reason",
        "language",
        "reviewed_at",
        "reviewed_by",
        "review_note",
        "rejection_reason",
    }.issubset(ConversationMemoryCandidate.__table__.columns.keys())
    assert {
        "owner_user_id",
        "profile_id",
        "model_code",
        "collection_name",
        "top_k",
        "score_threshold",
        "retrieval_mode",
        "source_eval_job_id",
        "source_eval_dataset_id",
        "selected_metrics",
        "all_config_scores",
        "selection_reason",
        "warnings",
        "is_active",
        "selected_at",
    }.issubset(ActiveRetrievalConfig.__table__.columns.keys())

    assert {
        "users",
        "memory_profiles",
        "chat_messages",
        "memories",
        "media_assets",
        "rag_sources",
        "rag_chunks",
        "rag_embeddings",
        "rag_vector_indexes",
        "background_jobs",
        "active_retrieval_configs",
        "conversation_memory_candidates",
    }.issubset(
        Base.metadata.tables.keys()
    )

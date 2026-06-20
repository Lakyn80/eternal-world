from __future__ import annotations

from datetime import date, datetime
from typing import Any

from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, ForeignKey, Index, Integer, JSON, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default=text("true"),
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text("false"),
    )

    memory_profiles: Mapped[list[MemoryProfile]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
    chat_messages: Mapped[list[ChatMessage]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
    memories: Mapped[list[Memory]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
    rag_sources: Mapped[list[RagSource]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    rag_chunks: Mapped[list[RagChunk]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    rag_embeddings: Mapped[list[RagEmbedding]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    media_assets: Mapped[list[MediaAsset]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )


class MemoryProfile(TimestampMixin, Base):
    __tablename__ = "memory_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    main_photo_media_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "media_assets.id",
            ondelete="SET NULL",
            use_alter=True,
            name="fk_memory_profiles_main_photo_media_id_media_assets",
        ),
        index=True,
        nullable=True,
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    birth_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    death_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    biography: Mapped[str | None] = mapped_column(Text, nullable=True)
    personality: Mapped[str | None] = mapped_column(Text, nullable=True)
    catchphrases: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_public: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text("false"),
    )

    user: Mapped[User] = relationship(back_populates="memory_profiles")
    chat_messages: Mapped[list[ChatMessage]] = relationship(back_populates="memory_profile")
    memories: Mapped[list[Memory]] = relationship(back_populates="memory_profile")
    rag_sources: Mapped[list[RagSource]] = relationship(back_populates="memory_profile")
    rag_chunks: Mapped[list[RagChunk]] = relationship(back_populates="memory_profile")
    rag_embeddings: Mapped[list[RagEmbedding]] = relationship(back_populates="memory_profile")
    media_assets: Mapped[list[MediaAsset]] = relationship(
        back_populates="memory_profile",
        foreign_keys="MediaAsset.profile_id",
    )
    main_photo_media: Mapped[MediaAsset | None] = relationship(
        foreign_keys=[main_photo_media_id],
        post_update=True,
    )


class ChatMessage(TimestampMixin, Base):
    __tablename__ = "chat_messages"
    __table_args__ = (
        CheckConstraint(
            "role IN ('system', 'user', 'assistant')",
            name="chat_messages_role",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    memory_profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    role: Mapped[str] = mapped_column(String(16), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    token_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    message_metadata: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    user: Mapped[User] = relationship(back_populates="chat_messages")
    memory_profile: Mapped[MemoryProfile | None] = relationship(back_populates="chat_messages")


class Memory(TimestampMixin, Base):
    __tablename__ = "memories"
    __table_args__ = (
        CheckConstraint(
            "memory_type IN ('text', 'photo', 'audio', 'video')",
            name="memories_memory_type",
        ),
        CheckConstraint("importance BETWEEN 1 AND 5", name="memories_importance"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    memory_profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    media_id: Mapped[int | None] = mapped_column(
        ForeignKey("media_assets.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    memory_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="text",
        server_default=text("'text'"),
    )
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    occurred_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    occurred_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    importance: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=3,
        server_default=text("3"),
    )
    embedding_status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="pending",
        server_default=text("'pending'"),
    )
    extra_metadata: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    user: Mapped[User] = relationship(back_populates="memories")
    memory_profile: Mapped[MemoryProfile | None] = relationship(back_populates="memories")
    media_asset: Mapped[MediaAsset | None] = relationship(
        back_populates="memories",
        foreign_keys=[media_id],
    )


class RagSource(TimestampMixin, Base):
    __tablename__ = "rag_sources"
    __table_args__ = (
        CheckConstraint(
            (
                "source_type IN ("
                "'manual_text', 'biography', 'timeline_memory', 'document_text', "
                "'chat_export', 'audio_transcript', 'video_transcript', "
                "'letter', 'diary', 'other')"
            ),
            name="rag_sources_source_type",
        ),
        CheckConstraint(
            (
                "status IN ("
                "'pending', 'ready_for_cleaning', 'cleaned', 'ready_for_chunking', "
                "'chunked', 'ready_for_embedding', 'embedded', 'failed')"
            ),
            name="rag_sources_status",
        ),
        Index("ix_rag_sources_created_at", "created_at"),
        Index("ix_rag_sources_owner_user_id_profile_id", "owner_user_id", "profile_id"),
        Index("ix_rag_sources_profile_id_status", "profile_id", "status"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    source_type: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    raw_text: Mapped[str] = mapped_column(Text, nullable=False)
    normalized_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    status: Mapped[str] = mapped_column(
        String(32),
        index=True,
        nullable=False,
        default="ready_for_cleaning",
        server_default=text("'ready_for_cleaning'"),
    )
    processing_error: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_metadata: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    owner: Mapped[User] = relationship(back_populates="rag_sources")
    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="rag_sources")
    rag_chunks: Mapped[list[RagChunk]] = relationship(
        back_populates="source",
        cascade="all, delete-orphan",
    )
    rag_embeddings: Mapped[list[RagEmbedding]] = relationship(
        back_populates="source",
        cascade="all, delete-orphan",
    )


class RagChunk(TimestampMixin, Base):
    __tablename__ = "rag_chunks"
    __table_args__ = (
        CheckConstraint(
            "validation_status IN ('valid', 'warning', 'invalid')",
            name="rag_chunks_validation_status",
        ),
        Index("ix_rag_chunks_owner_user_id_profile_id", "owner_user_id", "profile_id"),
        Index("ix_rag_chunks_profile_id_source_id", "profile_id", "source_id"),
        Index("ix_rag_chunks_source_id_chunk_index", "source_id", "chunk_index"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    source_id: Mapped[int] = mapped_column(
        ForeignKey("rag_sources.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    chunk_text: Mapped[str] = mapped_column(Text, nullable=False)
    text_hash: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    token_estimate: Mapped[int] = mapped_column(Integer, nullable=False)
    char_count: Mapped[int] = mapped_column(Integer, nullable=False)
    sentence_count: Mapped[int] = mapped_column(Integer, nullable=False)
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    chunk_metadata: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    validation_status: Mapped[str] = mapped_column(
        String(16),
        index=True,
        nullable=False,
        default="valid",
        server_default=text("'valid'"),
    )
    validation_errors: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)

    owner: Mapped[User] = relationship(back_populates="rag_chunks")
    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="rag_chunks")
    source: Mapped[RagSource] = relationship(back_populates="rag_chunks")
    rag_embeddings: Mapped[list[RagEmbedding]] = relationship(
        back_populates="chunk",
        cascade="all, delete-orphan",
    )


class RagEmbedding(TimestampMixin, Base):
    __tablename__ = "rag_embeddings"
    __table_args__ = (
        CheckConstraint(
            "status IN ('embedded', 'failed')",
            name="rag_embeddings_status",
        ),
        Index("ix_rag_embeddings_owner_user_id_profile_id", "owner_user_id", "profile_id"),
        Index("ix_rag_embeddings_profile_id_model_code", "profile_id", "model_code"),
        Index("ix_rag_embeddings_chunk_id_model_code", "chunk_id", "model_code", unique=True),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    source_id: Mapped[int] = mapped_column(
        ForeignKey("rag_sources.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    chunk_id: Mapped[int] = mapped_column(
        ForeignKey("rag_chunks.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    model_code: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    vector: Mapped[list[float] | None] = mapped_column(JSON, nullable=True)
    vector_dimension: Mapped[int] = mapped_column(Integer, nullable=False)
    text_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(
        String(16),
        index=True,
        nullable=False,
        default="embedded",
        server_default=text("'embedded'"),
    )
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    embedding_metadata: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    owner: Mapped[User] = relationship(back_populates="rag_embeddings")
    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="rag_embeddings")
    source: Mapped[RagSource] = relationship(back_populates="rag_embeddings")
    chunk: Mapped[RagChunk] = relationship(back_populates="rag_embeddings")


class MediaAsset(TimestampMixin, Base):
    __tablename__ = "media_assets"
    __table_args__ = (
        CheckConstraint(
            "media_type IN ('image', 'audio', 'video')",
            name="media_assets_media_type",
        ),
        CheckConstraint("size_bytes >= 0", name="media_assets_size_bytes_non_negative"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    media_type: Mapped[str] = mapped_column(String(16), nullable=False)
    storage_provider: Mapped[str] = mapped_column(String(32), nullable=False)
    storage_key: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    original_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(255), nullable=False)
    size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)

    owner: Mapped[User] = relationship(back_populates="media_assets")
    memory_profile: Mapped[MemoryProfile | None] = relationship(
        back_populates="media_assets",
        foreign_keys=[profile_id],
    )
    memories: Mapped[list[Memory]] = relationship(
        back_populates="media_asset",
        foreign_keys="Memory.media_id",
    )

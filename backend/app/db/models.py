from __future__ import annotations

from datetime import date, datetime
from typing import Any

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    JSON,
    String,
    Text,
    UniqueConstraint,
    func,
    text,
)
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
    rag_vector_indexes: Mapped[list[RagVectorIndex]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    background_jobs: Mapped[list[BackgroundJob]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    active_retrieval_configs: Mapped[list[ActiveRetrievalConfig]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    media_assets: Mapped[list[MediaAsset]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    conversation_memory_candidates: Mapped[list[ConversationMemoryCandidate]] = relationship(
        foreign_keys="ConversationMemoryCandidate.owner_user_id",
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    reviewed_conversation_memory_candidates: Mapped[list[ConversationMemoryCandidate]] = relationship(
        foreign_keys="ConversationMemoryCandidate.reviewed_by",
        back_populates="reviewed_by_user",
    )
    avatar_memory_promotions: Mapped[list[AvatarMemoryPromotion]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    memorial_memberships: Mapped[list[MemorialMembership]] = relationship(
        foreign_keys="MemorialMembership.user_id",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    created_memorial_invitations: Mapped[list[MemorialInvitation]] = relationship(
        foreign_keys="MemorialInvitation.created_by_user_id",
        back_populates="created_by_user",
    )
    accepted_memorial_invitations: Mapped[list[MemorialInvitation]] = relationship(
        foreign_keys="MemorialInvitation.accepted_by_user_id",
        back_populates="accepted_by_user",
    )
    memorial_contributions: Mapped[list[MemorialContribution]] = relationship(
        foreign_keys="MemorialContribution.author_user_id",
        back_populates="author_user",
    )
    reviewed_memorial_contributions: Mapped[list[MemorialContribution]] = relationship(
        foreign_keys="MemorialContribution.reviewed_by_user_id",
        back_populates="reviewed_by_user",
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
    rag_vector_indexes: Mapped[list[RagVectorIndex]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
    )
    background_jobs: Mapped[list[BackgroundJob]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
    )
    active_retrieval_config: Mapped[ActiveRetrievalConfig | None] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
        single_parent=True,
        uselist=False,
    )
    media_assets: Mapped[list[MediaAsset]] = relationship(
        back_populates="memory_profile",
        foreign_keys="MediaAsset.profile_id",
    )
    conversation_memory_candidates: Mapped[list[ConversationMemoryCandidate]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
    )
    avatar_memory_promotions: Mapped[list[AvatarMemoryPromotion]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
    )
    memorial_memberships: Mapped[list[MemorialMembership]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
    )
    memorial_invitations: Mapped[list[MemorialInvitation]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
    )
    memorial_contributions: Mapped[list[MemorialContribution]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
        foreign_keys="MemorialContribution.profile_id",
    )
    main_photo_media: Mapped[MediaAsset | None] = relationship(
        foreign_keys=[main_photo_media_id],
        post_update=True,
    )


class MemorialMembership(TimestampMixin, Base):
    __tablename__ = "memorial_memberships"
    __table_args__ = (
        CheckConstraint(
            "role IN ('owner', 'trusted_reviewer', 'contributor', 'viewer')",
            name="memorial_memberships_role",
        ),
        CheckConstraint(
            "status IN ('active', 'revoked')",
            name="memorial_memberships_status",
        ),
        UniqueConstraint("profile_id", "user_id", name="uq_memorial_memberships_profile_user"),
        Index("ix_memorial_memberships_profile_role", "profile_id", "role"),
        Index("ix_memorial_memberships_user_status", "user_id", "status"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    role: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    status: Mapped[str] = mapped_column(
        String(32),
        index=True,
        nullable=False,
        default="active",
        server_default=text("'active'"),
    )
    created_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    revoked_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )

    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="memorial_memberships")
    user: Mapped[User] = relationship(foreign_keys=[user_id], back_populates="memorial_memberships")
    created_by_user: Mapped[User | None] = relationship(foreign_keys=[created_by_user_id])
    revoked_by_user: Mapped[User | None] = relationship(foreign_keys=[revoked_by_user_id])


class MemorialInvitation(TimestampMixin, Base):
    __tablename__ = "memorial_invitations"
    __table_args__ = (
        CheckConstraint(
            "role IN ('trusted_reviewer', 'contributor', 'viewer')",
            name="memorial_invitations_role",
        ),
        Index("ix_memorial_invitations_profile_email", "profile_id", "email"),
        Index("ix_memorial_invitations_profile_status", "profile_id", "accepted_at", "revoked_at"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(String(320), index=True, nullable=False)
    role: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    token_hash: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
    accepted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), index=True, nullable=True)
    accepted_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), index=True, nullable=True)
    created_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )

    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="memorial_invitations")
    created_by_user: Mapped[User | None] = relationship(
        foreign_keys=[created_by_user_id],
        back_populates="created_memorial_invitations",
    )
    accepted_by_user: Mapped[User | None] = relationship(
        foreign_keys=[accepted_by_user_id],
        back_populates="accepted_memorial_invitations",
    )


class MemorialContribution(TimestampMixin, Base):
    __tablename__ = "memorial_contributions"
    __table_args__ = (
        CheckConstraint(
            "status IN ('draft', 'needs_review', 'approved', 'rejected', 'archived', 'superseded')",
            name="memorial_contributions_status",
        ),
        CheckConstraint(
            "privacy_scope IN ('private_owner', 'selected_family', 'all_family', 'public_legacy')",
            name="memorial_contributions_privacy_scope",
        ),
        Index("ix_memorial_contributions_profile_status", "profile_id", "status"),
        Index("ix_memorial_contributions_profile_current", "profile_id", "is_current"),
        Index("ix_memorial_contributions_author_status", "author_user_id", "status"),
        Index("ix_memorial_contributions_created_at", "created_at"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    author_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    memory_text: Mapped[str] = mapped_column(Text, nullable=False)
    source_note: Mapped[str | None] = mapped_column(String(500), nullable=True)
    privacy_scope: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="private_owner",
        server_default=text("'private_owner'"),
    )
    status: Mapped[str] = mapped_column(
        String(32),
        index=True,
        nullable=False,
        default="needs_review",
        server_default=text("'needs_review'"),
    )
    is_current: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text("false"),
    )
    supersedes_contribution_id: Mapped[int | None] = mapped_column(
        ForeignKey("memorial_contributions.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    reviewed_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    review_note: Mapped[str | None] = mapped_column(String(500), nullable=True)
    rejection_reason: Mapped[str | None] = mapped_column(String(500), nullable=True)

    memory_profile: Mapped[MemoryProfile] = relationship(
        back_populates="memorial_contributions",
        foreign_keys=[profile_id],
    )
    author_user: Mapped[User] = relationship(
        foreign_keys=[author_user_id],
        back_populates="memorial_contributions",
    )
    reviewed_by_user: Mapped[User | None] = relationship(
        foreign_keys=[reviewed_by_user_id],
        back_populates="reviewed_memorial_contributions",
    )
    supersedes_contribution: Mapped[MemorialContribution | None] = relationship(
        remote_side=[id],
        foreign_keys=[supersedes_contribution_id],
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
                "'letter', 'diary', 'conversation_candidate', 'other')"
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
    rag_vector_indexes: Mapped[list[RagVectorIndex]] = relationship(
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
    rag_vector_indexes: Mapped[list[RagVectorIndex]] = relationship(
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
    rag_vector_indexes: Mapped[list[RagVectorIndex]] = relationship(
        back_populates="embedding",
        cascade="all, delete-orphan",
    )


class RagVectorIndex(TimestampMixin, Base):
    __tablename__ = "rag_vector_indexes"
    __table_args__ = (
        CheckConstraint(
            "status IN ('indexed', 'failed')",
            name="rag_vector_indexes_status",
        ),
        Index("ix_rag_vector_indexes_owner_user_id_profile_id", "owner_user_id", "profile_id"),
        Index("ix_rag_vector_indexes_profile_id_model_code", "profile_id", "model_code"),
        Index(
            "ix_rag_vector_indexes_embedding_id_qdrant_collection",
            "embedding_id",
            "qdrant_collection",
            unique=True,
        ),
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
    embedding_id: Mapped[int] = mapped_column(
        ForeignKey("rag_embeddings.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    model_code: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    qdrant_collection: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    qdrant_point_id: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(
        String(16),
        index=True,
        nullable=False,
        default="indexed",
        server_default=text("'indexed'"),
    )
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    indexed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    owner: Mapped[User] = relationship(back_populates="rag_vector_indexes")
    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="rag_vector_indexes")
    source: Mapped[RagSource] = relationship(back_populates="rag_vector_indexes")
    chunk: Mapped[RagChunk] = relationship(back_populates="rag_vector_indexes")
    embedding: Mapped[RagEmbedding] = relationship(back_populates="rag_vector_indexes")


class BackgroundJob(TimestampMixin, Base):
    __tablename__ = "background_jobs"
    __table_args__ = (
        CheckConstraint(
            (
                "job_type IN ("
                "'smoke_test', 'system_milestone', 'rag_source_ingestion', 'rag_chunking', "
                "'embedding_generation', 'qdrant_indexing', 'rag_retrieval', "
                "'brain_agent_generation', 'media_processing', 'voice_generation', "
                "'video_generation'"
                ")"
            ),
            name="background_jobs_job_type",
        ),
        CheckConstraint(
            "status IN ('queued', 'running', 'succeeded', 'failed', 'cancelled')",
            name="background_jobs_status",
        ),
        Index("ix_background_jobs_created_at", "created_at"),
        Index("ix_background_jobs_owner_user_id_profile_id", "owner_user_id", "profile_id"),
        Index("ix_background_jobs_owner_user_id_status", "owner_user_id", "status"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    job_type: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    status: Mapped[str] = mapped_column(
        String(16),
        index=True,
        nullable=False,
        default="queued",
        server_default=text("'queued'"),
    )
    progress_current: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default=text("0"),
    )
    progress_total: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default=text("0"),
    )
    celery_task_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    input_payload: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False, default=dict)
    result_payload: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    error_payload: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    event_log: Mapped[list[dict[str, Any]]] = mapped_column(
        JSON,
        nullable=False,
        default=list,
        server_default=text("'[]'"),
    )
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    owner: Mapped[User] = relationship(back_populates="background_jobs")
    memory_profile: Mapped[MemoryProfile | None] = relationship(back_populates="background_jobs")
    active_retrieval_configs: Mapped[list[ActiveRetrievalConfig]] = relationship(
        back_populates="source_eval_job",
    )


class ActiveRetrievalConfig(TimestampMixin, Base):
    __tablename__ = "active_retrieval_configs"
    __table_args__ = (
        CheckConstraint(
            "top_k BETWEEN 1 AND 100",
            name="active_retrieval_configs_top_k",
        ),
        Index("ix_active_retrieval_configs_created_at", "created_at"),
        Index(
            "ix_active_retrieval_configs_owner_user_id_profile_id",
            "owner_user_id",
            "profile_id",
        ),
        Index(
            "ix_active_retrieval_configs_profile_id_is_active",
            "profile_id",
            "is_active",
        ),
        Index(
            "ix_active_retrieval_configs_source_eval_job_id",
            "source_eval_job_id",
        ),
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
        unique=True,
    )
    model_code: Mapped[str] = mapped_column(String(120), nullable=False)
    collection_name: Mapped[str] = mapped_column(String(200), nullable=False)
    top_k: Mapped[int] = mapped_column(Integer, nullable=False)
    score_threshold: Mapped[float | None] = mapped_column(Float, nullable=True)
    retrieval_mode: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        default="hybrid",
        server_default=text("'hybrid'"),
    )
    source_eval_job_id: Mapped[int | None] = mapped_column(
        ForeignKey("background_jobs.id", ondelete="SET NULL"),
        nullable=True,
    )
    source_eval_dataset_id: Mapped[str | None] = mapped_column(String(120), nullable=True)
    selected_metrics: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    all_config_scores: Mapped[list[dict[str, Any]] | None] = mapped_column(JSON, nullable=True)
    selection_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    warnings: Mapped[list[dict[str, Any]] | None] = mapped_column(JSON, nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default=text("true"),
    )
    selected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    owner: Mapped[User] = relationship(back_populates="active_retrieval_configs")
    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="active_retrieval_config")
    source_eval_job: Mapped[BackgroundJob | None] = relationship(
        back_populates="active_retrieval_configs"
    )


class ConversationMemoryCandidate(TimestampMixin, Base):
    __tablename__ = "conversation_memory_candidates"
    __table_args__ = (
        CheckConstraint(
            "source IN ('conversation')",
            name="conversation_memory_candidates_source",
        ),
        CheckConstraint(
            "status IN ('needs_review', 'approved', 'rejected', 'archived')",
            name="conversation_memory_candidates_status",
        ),
        CheckConstraint(
            "confidence IN ('unverified')",
            name="conversation_memory_candidates_confidence",
        ),
        CheckConstraint(
            "memory_type IN ('general', 'bedtime_song')",
            name="conversation_memory_candidates_memory_type",
        ),
        CheckConstraint(
            "enrichment_status IN ('draft', 'collecting_details', 'ready_for_owner_review')",
            name="conversation_memory_candidates_enrichment_status",
        ),
        CheckConstraint(
            "privacy_scope IN ('private_owner', 'selected_family', 'all_family', 'public_legacy')",
            name="conversation_memory_candidates_privacy_scope",
        ),
        CheckConstraint(
            "dispute_status IN ('none', 'disputed', 'resolved')",
            name="conversation_memory_candidates_dispute_status",
        ),
        CheckConstraint(
            "unresolved_clarification_count >= 0",
            name="conversation_memory_candidates_unresolved_clarifications_non_negative",
        ),
        CheckConstraint(
            "version >= 1",
            name="conversation_memory_candidates_version_positive",
        ),
        CheckConstraint(
            "workflow_version IN (1, 2)",
            name="conversation_memory_candidates_workflow_version",
        ),
        Index("ix_cmc_created_at", "created_at"),
        Index(
            "ix_cmc_owner_profile_status",
            "owner_user_id",
            "profile_id",
            "status",
        ),
        Index(
            "ix_cmc_avatar_status",
            "avatar_id",
            "status",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    avatar_id: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    conversation_id: Mapped[str | None] = mapped_column(String(120), nullable=True)
    trace_id: Mapped[str | None] = mapped_column(String(120), index=True, nullable=True)
    source: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="conversation",
        server_default=text("'conversation'"),
    )
    status: Mapped[str] = mapped_column(
        String(32),
        index=True,
        nullable=False,
        default="needs_review",
        server_default=text("'needs_review'"),
    )
    confidence: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="unverified",
        server_default=text("'unverified'"),
    )
    user_message_excerpt: Mapped[str] = mapped_column(String(160), nullable=False)
    proposed_memory_text: Mapped[str] = mapped_column(String(500), nullable=False)
    reason: Mapped[str] = mapped_column(String(500), nullable=False)
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    reviewed_by: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    review_note: Mapped[str | None] = mapped_column(String(500), nullable=True)
    rejection_reason: Mapped[str | None] = mapped_column(String(500), nullable=True)
    memory_type: Mapped[str] = mapped_column(
        String(32), nullable=False, default="general", server_default=text("'general'")
    )
    enrichment_status: Mapped[str] = mapped_column(
        String(32), nullable=False, default="draft", server_default=text("'draft'")
    )
    finalized_memory_text: Mapped[str | None] = mapped_column(String(500), nullable=True)
    privacy_scope: Mapped[str] = mapped_column(
        String(32), nullable=False, default="private_owner", server_default=text("'private_owner'")
    )
    dispute_status: Mapped[str] = mapped_column(
        String(32), nullable=False, default="none", server_default=text("'none'")
    )
    finalized_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    finalized_by: Mapped[str | None] = mapped_column(String(120), nullable=True)
    owner_reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    owner_reviewed_by: Mapped[str | None] = mapped_column(String(120), nullable=True)
    owner_review_actor_role: Mapped[str | None] = mapped_column(String(32), nullable=True)
    review_authority_source: Mapped[str | None] = mapped_column(String(32), nullable=True)
    unresolved_clarification_count: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1, server_default=text("1"))
    workflow_version: Mapped[int] = mapped_column(Integer, nullable=False, default=2, server_default=text("2"))

    owner: Mapped[User] = relationship(
        foreign_keys=[owner_user_id],
        back_populates="conversation_memory_candidates",
    )
    memory_profile: Mapped[MemoryProfile | None] = relationship(
        back_populates="conversation_memory_candidates"
    )
    reviewed_by_user: Mapped[User | None] = relationship(
        foreign_keys=[reviewed_by],
        back_populates="reviewed_conversation_memory_candidates",
    )
    avatar_memory_promotion: Mapped[AvatarMemoryPromotion | None] = relationship(
        back_populates="candidate",
        cascade="all, delete-orphan",
        uselist=False,
    )
    family_memory_contributions: Mapped[list[FamilyMemoryContribution]] = relationship(
        back_populates="candidate",
        cascade="all, delete-orphan",
        foreign_keys="FamilyMemoryContribution.candidate_id",
    )
    clarification_questions: Mapped[list[MemoryClarificationQuestion]] = relationship(
        back_populates="candidate",
        cascade="all, delete-orphan",
        foreign_keys="MemoryClarificationQuestion.candidate_id",
    )


class AvatarMemoryPromotion(TimestampMixin, Base):
    __tablename__ = "avatar_memory_promotions"
    __table_args__ = (
        CheckConstraint(
            "source_type IN ('conversation_candidate')",
            name="avatar_memory_promotions_source_type",
        ),
        CheckConstraint(
            "promotion_status IN ('pending_index', 'indexed', 'failed', 'cancelled')",
            name="avatar_memory_promotions_status",
        ),
        CheckConstraint(
            "indexing_attempt_count >= 0",
            name="avatar_memory_promotions_indexing_attempt_count_non_negative",
        ),
        Index("ix_amp_created_at", "created_at"),
        Index("ix_amp_owner_profile_status", "owner_user_id", "profile_id", "promotion_status"),
        Index("ix_amp_avatar_status", "avatar_id", "promotion_status"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("conversation_memory_candidates.id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False,
    )
    owner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    avatar_id: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    source_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="conversation_candidate",
        server_default=text("'conversation_candidate'"),
    )
    promotion_status: Mapped[str] = mapped_column(
        String(32),
        index=True,
        nullable=False,
        default="pending_index",
        server_default=text("'pending_index'"),
    )
    approved_memory_text: Mapped[str] = mapped_column(String(500), nullable=False)
    normalized_memory_text: Mapped[str] = mapped_column(String(500), nullable=False)
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    indexed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    failed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    failure_reason: Mapped[str | None] = mapped_column(String(500), nullable=True)
    target_collection_name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    qdrant_point_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    indexing_attempt_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default=text("0"),
    )
    rag_source_id: Mapped[int | None] = mapped_column(
        ForeignKey("rag_sources.id", ondelete="SET NULL"),
        nullable=True,
    )
    rag_chunk_id: Mapped[int | None] = mapped_column(
        ForeignKey("rag_chunks.id", ondelete="SET NULL"),
        nullable=True,
    )
    rag_embedding_id: Mapped[int | None] = mapped_column(
        ForeignKey("rag_embeddings.id", ondelete="SET NULL"),
        nullable=True,
    )
    trace_id: Mapped[str | None] = mapped_column(String(120), index=True, nullable=True)
    source_candidate_status_snapshot: Mapped[str] = mapped_column(String(32), nullable=False)
    review_note_snapshot: Mapped[str | None] = mapped_column(String(500), nullable=True)

    candidate: Mapped[ConversationMemoryCandidate] = relationship(back_populates="avatar_memory_promotion")
    owner: Mapped[User] = relationship(back_populates="avatar_memory_promotions")
    memory_profile: Mapped[MemoryProfile | None] = relationship(back_populates="avatar_memory_promotions")


class FamilyMemoryContribution(Base):
    __tablename__ = "family_memory_contributions"
    __table_args__ = (
        CheckConstraint(
            "actor_role IN ('owner', 'contributor', 'trusted_reviewer', 'system')",
            name="family_memory_contributions_actor_role",
        ),
        CheckConstraint(
            "contribution_type IN ('initial_claim', 'clarification_answer', 'owner_correction', "
            "'owner_confirmation', 'reviewer_note', 'dispute_statement', 'system_normalization')",
            name="family_memory_contributions_type",
        ),
        CheckConstraint(
            "privacy_scope_snapshot IN ('private_owner', 'selected_family', 'all_family', 'public_legacy')",
            name="family_memory_contributions_privacy_scope",
        ),
        Index("ix_fmc_candidate_created", "candidate_id", "created_at"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("conversation_memory_candidates.id", ondelete="CASCADE"), index=True, nullable=False
    )
    avatar_id: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"), index=True, nullable=True
    )
    actor_id: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    actor_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), index=True, nullable=True
    )
    actor_role: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    relationship_to_owner: Mapped[str | None] = mapped_column(String(120), nullable=True)
    contribution_type: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    contribution_text: Mapped[str] = mapped_column(String(1000), nullable=False)
    structured_details: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    source_message_hash: Mapped[str | None] = mapped_column(String(64), index=True, nullable=True)
    trace_id: Mapped[str | None] = mapped_column(String(120), index=True, nullable=True)
    supersedes_contribution_id: Mapped[int | None] = mapped_column(
        ForeignKey("family_memory_contributions.id", ondelete="SET NULL"), nullable=True
    )
    is_owner_correction: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("false")
    )
    is_disputed: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("false")
    )
    privacy_scope_snapshot: Mapped[str] = mapped_column(String(32), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    candidate: Mapped[ConversationMemoryCandidate] = relationship(
        back_populates="family_memory_contributions",
        foreign_keys=[candidate_id],
    )
    supersedes_contribution: Mapped[FamilyMemoryContribution | None] = relationship(
        remote_side=[id], foreign_keys=[supersedes_contribution_id]
    )


class MemoryClarificationQuestion(TimestampMixin, Base):
    __tablename__ = "memory_clarification_questions"
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'answered', 'skipped', 'cancelled')",
            name="memory_clarification_questions_status",
        ),
        Index("ix_mcq_candidate_status", "candidate_id", "status"),
        Index("ix_mcq_candidate_question_key", "candidate_id", "question_key", unique=True),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("conversation_memory_candidates.id", ondelete="CASCADE"), index=True, nullable=False
    )
    question_key: Mapped[str] = mapped_column(String(64), nullable=False)
    question_text: Mapped[str] = mapped_column(String(500), nullable=False)
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    status: Mapped[str] = mapped_column(
        String(32), nullable=False, default="pending", server_default=text("'pending'")
    )
    required: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True, server_default=text("true")
    )
    asked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    answered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    answered_by: Mapped[str | None] = mapped_column(String(120), nullable=True)
    answer_contribution_id: Mapped[int | None] = mapped_column(
        ForeignKey("family_memory_contributions.id", ondelete="SET NULL"), nullable=True
    )

    candidate: Mapped[ConversationMemoryCandidate] = relationship(
        back_populates="clarification_questions",
        foreign_keys=[candidate_id],
    )
    answer_contribution: Mapped[FamilyMemoryContribution | None] = relationship(
        foreign_keys=[answer_contribution_id]
    )


class MemoryContentTranslation(TimestampMixin, Base):
    """Current backend-computed translation state for one translatable field.

    Task 64.5.1 (Czech/Russian bilingual memory workflow). Holds the source
    text (never overwritten by a translation), the current translated text
    for one target language, and the translation lifecycle status. One row
    represents the *current* translation state for
    ``(entity_type, entity_id, field_name, target_language)`` - it is not a
    full historical log. Historical text itself is already append-only via
    ``FamilyMemoryContribution`` (each edit is a new contribution row); this
    table only needs to track "what is the current translation of the
    current source text", which it does via ``source_hash`` comparison and
    a monotonically increasing ``translation_version``. Re-translations
    update the row in place after first marking it ``stale``.

    A narrow ``entity_type`` + string ``entity_id`` addressing scheme is
    used instead of a generic polymorphic foreign key, because the
    translatable entities are heterogeneous: a candidate's finalized text
    (integer id), an append-only contribution (integer id, immutable after
    creation), or an ephemeral FA-chat turn addressed by ``trace_id``
    (no persistent row at all). ``candidate_id``/``contribution_id``/
    ``clarification_id`` remain real nullable foreign keys wherever the
    entity does have a durable row, purely for efficient lookups/joins.
    """

    __tablename__ = "memory_content_translations"
    __table_args__ = (
        CheckConstraint(
            "entity_type IN ('memory_candidate', 'family_memory_contribution', "
            "'clarification_question', 'fa_chat_turn')",
            name="memory_content_translations_entity_type",
        ),
        CheckConstraint(
            "source_language IN ('cs', 'ru', 'en')",
            name="memory_content_translations_source_language",
        ),
        CheckConstraint(
            "target_language IN ('cs', 'ru', 'en')",
            name="memory_content_translations_target_language",
        ),
        CheckConstraint(
            "translation_status IN ('pending', 'translated', 'failed', 'stale', 'human_reviewed')",
            name="memory_content_translations_status",
        ),
        CheckConstraint(
            "translation_version >= 1",
            name="memory_content_translations_version_positive",
        ),
        Index(
            "ix_mct_entity_field_target_unique",
            "entity_type",
            "entity_id",
            "field_name",
            "target_language",
            unique=True,
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    candidate_id: Mapped[int | None] = mapped_column(
        ForeignKey("conversation_memory_candidates.id", ondelete="CASCADE"),
        index=True,
        nullable=True,
    )
    contribution_id: Mapped[int | None] = mapped_column(
        ForeignKey("family_memory_contributions.id", ondelete="CASCADE"),
        index=True,
        nullable=True,
    )
    clarification_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_clarification_questions.id", ondelete="CASCADE"),
        index=True,
        nullable=True,
    )
    entity_type: Mapped[str] = mapped_column(String(32), nullable=False)
    entity_id: Mapped[str] = mapped_column(String(64), nullable=False)
    field_name: Mapped[str] = mapped_column(String(64), nullable=False)
    source_language: Mapped[str] = mapped_column(String(8), nullable=False)
    target_language: Mapped[str] = mapped_column(String(8), nullable=False)
    source_text: Mapped[str] = mapped_column(Text, nullable=False)
    translated_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    translation_status: Mapped[str] = mapped_column(
        String(32), nullable=False, default="pending", server_default=text("'pending'")
    )
    translation_provider: Mapped[str | None] = mapped_column(String(64), nullable=True)
    translation_model: Mapped[str | None] = mapped_column(String(120), nullable=True)
    translation_version: Mapped[int] = mapped_column(
        Integer, nullable=False, default=1, server_default=text("1")
    )
    translated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    reviewed_by: Mapped[str | None] = mapped_column(String(120), nullable=True)

    candidate: Mapped[ConversationMemoryCandidate | None] = relationship(foreign_keys=[candidate_id])
    contribution: Mapped[FamilyMemoryContribution | None] = relationship(foreign_keys=[contribution_id])
    clarification: Mapped[MemoryClarificationQuestion | None] = relationship(
        foreign_keys=[clarification_id]
    )


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

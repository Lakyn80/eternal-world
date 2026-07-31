from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
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
    Numeric,
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
    #: Mutable account UI chrome language (Task 65.13.1). Independent of any
    #: memorial's immutable ``canonical_language``.
    preferred_ui_language: Mapped[str] = mapped_column(
        String(8),
        nullable=False,
        default="en",
        server_default=text("'en'"),
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
    __table_args__ = (
        CheckConstraint(
            "biography_status IN ('draft', 'ready_for_ingestion', 'ingesting', 'indexed', 'failed', 'stale')",
            name="memory_profiles_biography_status",
        ),
        CheckConstraint(
            "canonical_language IN ('cs', 'en', 'ru')",
            name="memory_profiles_canonical_language",
        ),
        CheckConstraint(
            "canonical_language_source IN ("
            "'existing_profile', 'avatar_persona', 'creator_preference', "
            "'reliable_content_metadata', 'application_fallback', 'manual_review_required'"
            ")",
            name="memory_profiles_canonical_language_source",
        ),
    )

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
    #: Immutable memorial language after create (Task 65.13.1). Avatar / RAG /
    #: Biographer / owner review consume this language; UI chrome does not.
    canonical_language: Mapped[str] = mapped_column(
        String(8),
        nullable=False,
        default="cs",
        server_default=text("'cs'"),
    )
    #: Auditable reason the canonical language was assigned. Never leave
    #: undocumented application defaults unmarked.
    canonical_language_source: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        default="application_fallback",
        server_default=text("'application_fallback'"),
    )
    canonical_language_locked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    is_public: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text("false"),
    )
    biography_status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="draft",
        server_default=text("'draft'"),
    )
    biography_content_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)
    biography_source_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "rag_sources.id",
            ondelete="SET NULL",
            use_alter=True,
            name="fk_memory_profiles_biography_source_id_rag_sources",
        ),
        index=True,
        nullable=True,
    )
    biography_indexed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    biography_ingestion_attempt_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default=text("0"),
    )
    biography_ingestion_failure_reason: Mapped[str | None] = mapped_column(String(500), nullable=True)

    user: Mapped[User] = relationship(back_populates="memory_profiles")
    chat_messages: Mapped[list[ChatMessage]] = relationship(back_populates="memory_profile")
    memories: Mapped[list[Memory]] = relationship(back_populates="memory_profile")
    rag_sources: Mapped[list[RagSource]] = relationship(
        back_populates="memory_profile",
        foreign_keys="RagSource.profile_id",
    )
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
    memorial_contribution_promotions: Mapped[list[MemorialContributionPromotion]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
    )
    avatar_persona_settings: Mapped[AvatarPersonaSettings | None] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
        uselist=False,
    )
    main_photo_media: Mapped[MediaAsset | None] = relationship(
        foreign_keys=[main_photo_media_id],
        post_update=True,
    )
    biography_source: Mapped[RagSource | None] = relationship(
        foreign_keys=[biography_source_id],
        post_update=True,
    )
    biographer_questions: Mapped[list[BiographerQuestion]] = relationship(
        back_populates="memory_profile",
        cascade="all, delete-orphan",
        foreign_keys="BiographerQuestion.profile_id",
    )


class AvatarPersonaSettings(TimestampMixin, Base):
    """Task 65.12 - one-to-one canonical persona settings for a memorial profile.

    Owns shared identity values used by chat, voice adapters, and future
    face/video channels. Distinct from the demo-only in-memory
    ``AvatarPersonaProfile`` (Eva fixture) used by FA demo chat.
    """

    __tablename__ = "avatar_persona_settings"
    __table_args__ = (
        CheckConstraint(
            "voice_mode IN ('original_recording', 'warm_older', 'younger_self')",
            name="avatar_persona_settings_voice_mode",
        ),
        CheckConstraint(
            "voice_style IN ('warm', 'calm', 'older', 'energetic')",
            name="avatar_persona_settings_voice_style",
        ),
        CheckConstraint(
            "remembered_age IS NULL OR (remembered_age >= 1 AND remembered_age <= 120)",
            name="avatar_persona_settings_remembered_age",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False,
    )
    voice_mode: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="warm_older",
        server_default=text("'warm_older'"),
    )
    voice_style: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="warm",
        server_default=text("'warm'"),
    )
    personality_traits: Mapped[list[Any]] = mapped_column(
        JSON,
        nullable=False,
        default=list,
        server_default=text("'[]'"),
    )
    primary_language: Mapped[str] = mapped_column(
        String(8),
        nullable=False,
        default="cs",
        server_default=text("'cs'"),
    )
    supported_languages: Mapped[list[Any]] = mapped_column(
        JSON,
        nullable=False,
        default=list,
        server_default=text("'[\"cs\"]'"),
    )
    remembered_age: Mapped[int | None] = mapped_column(Integer, nullable=True)
    communication_profile: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="",
        server_default=text("''"),
    )

    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="avatar_persona_settings")


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
        CheckConstraint(
            "preferred_locale_hint IS NULL OR preferred_locale_hint IN ('cs', 'en', 'ru')",
            name="memorial_invitations_preferred_locale_hint",
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
    preferred_locale_hint: Mapped[str | None] = mapped_column(String(8), nullable=True)
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
        CheckConstraint(
            "source_language IN ('cs', 'ru', 'en', 'de')",
            name="memorial_contributions_source_language",
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
    #: Exact original language of ``memory_text`` (never overwritten by translation).
    source_language: Mapped[str] = mapped_column(String(8), nullable=False)
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
    promotion: Mapped[MemorialContributionPromotion | None] = relationship(
        back_populates="contribution",
        cascade="all, delete-orphan",
        uselist=False,
    )


class MemorialContributionPromotion(TimestampMixin, Base):
    """Bridges an approved+current `MemorialContribution` into the existing
    canonical memory / embedding / indexing pipeline (`RagSource` ->
    `RagChunk` -> `RagEmbedding` -> Qdrant), mirroring the established
    `AvatarMemoryPromotion` pattern (Task 64.x) rather than introducing a
    second embedding system. One row per contribution (`contribution_id` is
    unique), created idempotently on approval and advanced by the indexing
    step, which is itself idempotent via a deterministic Qdrant point id.

    `promotion_status` values:
      - pending_index: approved, not yet embedded/written to Qdrant.
      - indexed: embedded and searchable as active evidence.
      - failed: an indexing attempt raised; safe to retry.
      - retired: the source contribution was later archived or superseded;
        the Qdrant point has been removed so it can no longer be retrieved
        as active evidence, while the SQL lineage row is kept for audit.
    """

    __tablename__ = "memorial_contribution_promotions"
    __table_args__ = (
        CheckConstraint(
            "promotion_status IN ('pending_index', 'indexed', 'failed', 'retired')",
            name="memorial_contribution_promotions_status",
        ),
        CheckConstraint(
            "indexing_attempt_count >= 0",
            name="memorial_contribution_promotions_indexing_attempt_count_non_negative",
        ),
        Index("ix_mcp_created_at", "created_at"),
        Index("ix_mcp_profile_status", "profile_id", "promotion_status"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    contribution_id: Mapped[int] = mapped_column(
        ForeignKey("memorial_contributions.id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False,
    )
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    promotion_status: Mapped[str] = mapped_column(
        String(32),
        index=True,
        nullable=False,
        default="pending_index",
        server_default=text("'pending_index'"),
    )
    approved_memory_text: Mapped[str] = mapped_column(Text, nullable=False)
    normalized_memory_text: Mapped[str] = mapped_column(Text, nullable=False)
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    indexed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    failed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    retired_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
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
    source_contribution_status_snapshot: Mapped[str] = mapped_column(String(32), nullable=False)

    contribution: Mapped[MemorialContribution] = relationship(back_populates="promotion")
    memory_profile: Mapped[MemoryProfile] = relationship(back_populates="memorial_contribution_promotions")


class ChatMessage(TimestampMixin, Base):
    __tablename__ = "chat_messages"
    __table_args__ = (
        CheckConstraint(
            "role IN ('system', 'user', 'assistant')",
            name="chat_messages_role",
        ),
        CheckConstraint(
            "source_language IS NULL OR source_language IN ('cs', 'ru', 'en', 'de')",
            name="chat_messages_source_language",
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
    #: Durable original for user turns; memorial-canonical text for assistant.
    content: Mapped[str] = mapped_column(Text, nullable=False)
    #: Detected/declared language of the user original (null for assistant).
    source_language: Mapped[str | None] = mapped_column(String(8), nullable=True)
    token_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    message_metadata: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    user: Mapped[User] = relationship(back_populates="chat_messages")
    memory_profile: Mapped[MemoryProfile | None] = relationship(back_populates="chat_messages")


class ChatActiveSession(TimestampMixin, Base):
    """Task 65.7 - durable pointer to which conversation is currently
    "active" for a (user, profile) pair. `chat_messages` itself is never
    schema-changed for this - each message's existing JSON
    `message_metadata` column carries `{"conversation_id": ...}`, so a
    conversation boundary is just a value, not a new foreign key. This
    table exists only so "what is the CURRENT conversation_id" survives a
    Redis restart/cache-miss (`chat.service` rebuilds the Redis snapshot
    from Postgres by filtering `chat_messages` to this `conversation_id`).
    Resetting chat is a plain UPDATE of this one row - no old row is kept,
    since prior conversations remain fully readable through their messages'
    own `conversation_id` metadata regardless.
    """

    __tablename__ = "chat_active_sessions"
    __table_args__ = (UniqueConstraint("user_id", "profile_id", name="uq_chat_active_sessions_user_profile"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"), index=True, nullable=False
    )
    conversation_id: Mapped[str] = mapped_column(String(36), nullable=False)
    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )


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
    memory_profile: Mapped[MemoryProfile] = relationship(
        back_populates="rag_sources",
        foreign_keys=[profile_id],
    )
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
                "'video_generation', 'content_translation'"
                ")"
            ),
            name="background_jobs_job_type",
        ),
        CheckConstraint(
            (
                "status IN ("
                "'pending', 'queued', 'running', 'retry_scheduled', "
                "'recovery_pending', 'succeeded', 'failed', 'cancelled'"
                ")"
            ),
            name="background_jobs_status",
        ),
        Index("ix_background_jobs_created_at", "created_at"),
        Index("ix_background_jobs_owner_user_id_profile_id", "owner_user_id", "profile_id"),
        Index("ix_background_jobs_owner_user_id_status", "owner_user_id", "status"),
        Index("ix_background_jobs_queue_status", "queue", "status"),
        Index("ix_background_jobs_status_next_attempt_at", "status", "next_attempt_at"),
        Index("ix_background_jobs_status_heartbeat_at", "status", "heartbeat_at"),
        #: Partial unique index (Task 65.9, Part D/F): `idempotency_key`
        #: only needs to be unique among still-*active* jobs. Once a job
        #: reaches a terminal state, a later request carrying the exact
        #: same semantic key (e.g. "retry after a previous failed attempt
        #: for this same promotion") must be able to create a brand-new
        #: job rather than being permanently pinned to the old, already-
        #: finished row - a plain (non-partial) unique index would make a
        #: second real attempt impossible after the first one failed.
        Index(
            "uq_background_jobs_idempotency_key",
            "idempotency_key",
            unique=True,
            postgresql_where=text(
                "status NOT IN ('succeeded', 'failed', 'cancelled')"
            ),
            sqlite_where=text("status NOT IN ('succeeded', 'failed', 'cancelled')"),
        ),
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

    #: Task 65.9 (Part D) - asynchronous job platform fields. All additive;
    #: every pre-existing column above keeps its exact prior meaning.
    #: Celery queue name this job's work belongs on (e.g. "embedding",
    #: "maintenance") - a plain descriptive label, never used to select a
    #: raw task/queue from client-controlled input (Part G).
    queue: Mapped[str | None] = mapped_column(String(32), nullable=True)
    #: Deterministic semantic key (job_type + subject identity + content
    #: version + operation) enforced unique at the DB level so repeated
    #: approval/retry/duplicate-delivery can never create a second active
    #: job for the same real-world operation (Part F).
    idempotency_key: Mapped[str | None] = mapped_column(String(255), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    attempt_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    max_attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=3, server_default=text("3"))
    #: Bounded provider self-healing counters (Part M) - persisted so they
    #: survive worker/container restart and duplicate task delivery.
    provider_recovery_count: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    fresh_process_retry_used: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("false")
    )
    worker_recycle_requested: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("false")
    )
    queued_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    #: Updated by the worker while actively processing - used by stale-job
    #: recovery to detect a crashed worker without a permanent lock (Part P).
    heartbeat_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    next_attempt_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    #: Closed-set safe error category (Part L) - never a raw exception
    #: string. `error_message`/`error_payload` above remain the existing,
    #: already-safe human-readable summary fields.
    safe_error_category: Mapped[str | None] = mapped_column(String(64), nullable=True)
    internal_correlation_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    payload_schema_version: Mapped[int] = mapped_column(
        Integer, nullable=False, default=1, server_default=text("1")
    )

    owner: Mapped[User] = relationship(back_populates="background_jobs")
    memory_profile: Mapped[MemoryProfile | None] = relationship(back_populates="background_jobs")
    active_retrieval_configs: Mapped[list[ActiveRetrievalConfig]] = relationship(
        back_populates="source_eval_job",
    )
    outbox_event: Mapped[JobOutboxEvent | None] = relationship(
        back_populates="job",
        uselist=False,
        cascade="all, delete-orphan",
    )


class JobOutboxEvent(TimestampMixin, Base):
    """Transactional outbox row (Task 65.9, Part E). Written in the exact
    same DB transaction as the `BackgroundJob` row and any domain-state
    change it represents (e.g. a promotion moving to `pending_index`), so a
    broker publish failure can never silently lose the job: the row simply
    stays `pending` until a dispatcher (or the recovery sweep) republishes
    it. One row per job (`UniqueConstraint(job_id)`) - a redispatch (self-
    healing recovery, stale-job recovery) resets the same row back to
    `pending` rather than creating a second one, keeping "duplicate
    publication remains harmless" trivially true."""

    __tablename__ = "job_outbox_events"
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'published', 'abandoned')",
            name="job_outbox_events_status",
        ),
        Index("ix_job_outbox_events_status_created_at", "status", "created_at"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    job_id: Mapped[int] = mapped_column(
        ForeignKey("background_jobs.id", ondelete="CASCADE"),
        index=True,
        unique=True,
        nullable=False,
    )
    task_name: Mapped[str] = mapped_column(String(255), nullable=False)
    queue: Mapped[str] = mapped_column(String(32), nullable=False)
    task_args: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False, default=dict)
    status: Mapped[str] = mapped_column(
        String(16),
        nullable=False,
        default="pending",
        server_default=text("'pending'"),
    )
    attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    last_error: Mapped[str | None] = mapped_column(String(255), nullable=True)
    next_attempt_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    job: Mapped[BackgroundJob] = relationship(back_populates="outbox_event")


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
            "memory_type IN ('general', 'bedtime_song', 'childhood_memory')",
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


class BiographerQuestion(TimestampMixin, Base):
    """One AI Biographer top-level question offered to a memorial's members
    (Task 65.2). Distinct from `MemoryClarificationQuestion`: a clarification
    always enriches an *existing* candidate (`candidate_id` is non-null
    there), whereas a biographer question is what *initiates* one - it has
    no candidate yet when asked, only once answered. Profile-scoped (not
    per-actor): once a topic has been asked for a memorial, it stays covered
    regardless of which member answers, so multiple family members curating
    the same memorial never see duplicate topics.
    """

    __tablename__ = "biographer_questions"
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'answered', 'skipped', 'postponed')",
            name="biographer_questions_status",
        ),
        Index("ix_biographer_questions_profile_status", "profile_id", "status"),
        Index("ix_biographer_questions_profile_topic", "profile_id", "topic"),
        Index(
            "uq_biographer_questions_profile_pending",
            "profile_id",
            unique=True,
            # Both dialect kwargs are needed: Postgres backs real
            # deployments (via the Alembic migration), SQLite backs the
            # automated test suite (`Base.metadata.create_all`, which
            # builds tables straight from these models, bypassing Alembic
            # entirely) - without `sqlite_where` this would silently become
            # a full (non-partial) unique index on `profile_id` under
            # SQLite, incorrectly forbidding more than one question ever
            # per profile.
            postgresql_where=text("status = 'pending'"),
            sqlite_where=text("status = 'pending'"),
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"), index=True, nullable=False
    )
    topic: Mapped[str] = mapped_column(String(64), nullable=False)
    locale: Mapped[str] = mapped_column(String(8), nullable=False)
    question_text: Mapped[str] = mapped_column(String(500), nullable=False)
    status: Mapped[str] = mapped_column(
        String(32), nullable=False, default="pending", server_default=text("'pending'")
    )
    asked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    answered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    skipped_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    postponed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    answered_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    resulting_candidate_id: Mapped[int | None] = mapped_column(
        ForeignKey("conversation_memory_candidates.id", ondelete="SET NULL"), nullable=True
    )
    #: Task 65.6 provenance - never stores prompt/answer/source text, only
    #: safe bounded classification and counts (see `avatar_biographer`).
    generation_mode: Mapped[str] = mapped_column(
        String(32), nullable=False, default="deterministic_fallback",
        server_default=text("'deterministic_fallback'"),
    )
    provider: Mapped[str | None] = mapped_column(String(64), nullable=True)
    model: Mapped[str | None] = mapped_column(String(128), nullable=True)
    ai_action_id: Mapped[int | None] = mapped_column(
        ForeignKey("ai_actions.id", ondelete="SET NULL"), nullable=True
    )
    context_source_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    context_chunk_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    question_intent: Mapped[str | None] = mapped_column(String(32), nullable=True)
    validation_result: Mapped[str | None] = mapped_column(String(32), nullable=True)
    fallback_used: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("false")
    )

    memory_profile: Mapped[MemoryProfile] = relationship(
        back_populates="biographer_questions",
        foreign_keys=[profile_id],
    )
    answered_by: Mapped[User | None] = relationship(foreign_keys=[answered_by_user_id])
    resulting_candidate: Mapped[ConversationMemoryCandidate | None] = relationship(
        foreign_keys=[resulting_candidate_id]
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
            "'clarification_question', 'fa_chat_turn', 'memorial_contribution', "
            "'biographer_question', 'biographer_answer', 'chat_message')",
            name="memory_content_translations_entity_type",
        ),
        CheckConstraint(
            "source_language IN ('cs', 'ru', 'en', 'de')",
            name="memory_content_translations_source_language",
        ),
        CheckConstraint(
            "target_language IN ('cs', 'ru', 'en', 'de')",
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
    profile_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=True,
    )
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


class AiAction(TimestampMixin, Base):
    """Task 66.1 provider-cost foundation: one durable row per user-visible
    AI operation (one Chat message+answer, one Biographer question, one
    dynamic translation, etc). Totals (``total_*_tokens``/``total_cost_usd``)
    are always recomputed deterministically from this action's
    ``AiProviderAttempt`` rows rather than incremented in place, so repeated
    finalization (e.g. a Celery task redelivery) can never double-count.

    There is no separate "conversation" entity in this codebase (chat is
    scoped by ``(user_id, memorial_id)``, not a distinct conversation row),
    so ``conversation_id`` is a plain informational integer with no foreign
    key and is not populated by any caller yet - reserved for a future
    conversation entity rather than forced onto an identifier that does not
    exist today.
    """

    __tablename__ = "ai_actions"
    __table_args__ = (
        CheckConstraint(
            "feature IN ("
            "'brain_chat_response', 'avatar_biographer_question', 'dynamic_memory_translation', "
            "'memory_candidate_finalization', 'memory_conflict_analysis', 'memory_summarization', "
            "'evaluation', 'development_test', 'other'"
            ")",
            name="ai_actions_feature",
        ),
        CheckConstraint(
            "execution_source IN ('fastapi', 'celery', 'internal', 'test')",
            name="ai_actions_execution_source",
        ),
        CheckConstraint(
            "status IN ('pending', 'running', 'succeeded', 'failed', 'cancelled')",
            name="ai_actions_status",
        ),
        CheckConstraint(
            "monetary_cost_status IN ('not_applicable', 'calculated', 'partial', 'unknown')",
            name="ai_actions_monetary_cost_status",
        ),
        CheckConstraint("provider_call_count >= 0", name="ai_actions_provider_call_count_non_negative"),
        CheckConstraint("retry_count >= 0", name="ai_actions_retry_count_non_negative"),
        CheckConstraint("total_input_tokens >= 0", name="ai_actions_total_input_tokens_non_negative"),
        CheckConstraint(
            "total_cached_input_tokens >= 0", name="ai_actions_total_cached_input_tokens_non_negative"
        ),
        CheckConstraint("total_output_tokens >= 0", name="ai_actions_total_output_tokens_non_negative"),
        CheckConstraint(
            "total_reasoning_tokens >= 0", name="ai_actions_total_reasoning_tokens_non_negative"
        ),
        CheckConstraint("total_tokens >= 0", name="ai_actions_total_tokens_non_negative"),
        CheckConstraint("total_cost_usd >= 0", name="ai_actions_total_cost_usd_non_negative"),
        CheckConstraint(
            "cached_input_savings_usd >= 0", name="ai_actions_cached_input_savings_usd_non_negative"
        ),
        Index("ix_ai_actions_trace_id", "trace_id"),
        Index("ix_ai_actions_created_at", "created_at"),
        Index("ix_ai_actions_feature_created_at", "feature", "created_at"),
        Index("ix_ai_actions_user_id_created_at", "user_id", "created_at"),
        Index("ix_ai_actions_memorial_id_created_at", "memorial_id", "created_at"),
        Index("ix_ai_actions_status_created_at", "status", "created_at"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    trace_id: Mapped[str] = mapped_column(String(64), nullable=False)
    feature: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="pending", server_default=text("'pending'")
    )
    execution_source: Mapped[str] = mapped_column(String(16), nullable=False)
    requested_locale: Mapped[str | None] = mapped_column(String(8), nullable=True)
    resolved_locale: Mapped[str | None] = mapped_column(String(8), nullable=True)
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), index=True, nullable=True
    )
    memorial_id: Mapped[int | None] = mapped_column(
        ForeignKey("memory_profiles.id", ondelete="SET NULL"), index=True, nullable=True
    )
    conversation_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    message_id: Mapped[int | None] = mapped_column(
        ForeignKey("chat_messages.id", ondelete="SET NULL"), index=True, nullable=True
    )
    celery_task_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    provider_call_count: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    retry_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    total_input_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    total_cached_input_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    total_output_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    total_reasoning_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    total_tokens: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    total_cost_usd: Mapped[Decimal] = mapped_column(
        Numeric(18, 9), nullable=False, default=Decimal("0"), server_default=text("0")
    )
    cached_input_savings_usd: Mapped[Decimal] = mapped_column(
        Numeric(18, 9), nullable=False, default=Decimal("0"), server_default=text("0")
    )
    monetary_cost_status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="not_applicable", server_default=text("'not_applicable'")
    )
    error_category: Mapped[str | None] = mapped_column(String(64), nullable=True)

    steps: Mapped[list[AiActionStep]] = relationship(
        back_populates="action", cascade="all, delete-orphan"
    )
    provider_attempts: Mapped[list[AiProviderAttempt]] = relationship(
        back_populates="action", cascade="all, delete-orphan"
    )


class AiActionStep(TimestampMixin, Base):
    """One processing step within one ``AiAction``. Only
    ``provider_generation``/``provider_translation``/``provider_structured_output``
    steps are expected to carry non-zero ``total_tokens``/``total_cost_usd`` -
    the remaining step types exist for action timing only."""

    __tablename__ = "ai_action_steps"
    __table_args__ = (
        CheckConstraint(
            "step_type IN ("
            "'provider_generation', 'provider_translation', 'provider_structured_output', "
            "'context_preparation', 'retrieval', 'deterministic_postprocessing', 'response_guard'"
            ")",
            name="ai_action_steps_step_type",
        ),
        CheckConstraint(
            "status IN ('pending', 'running', 'succeeded', 'failed', 'cancelled', 'skipped')",
            name="ai_action_steps_status",
        ),
        CheckConstraint(
            "execution_source IN ('fastapi', 'celery', 'internal', 'test')",
            name="ai_action_steps_execution_source",
        ),
        CheckConstraint(
            "cache_status IN ('not_applicable', 'hit', 'miss', 'partial', 'unknown')",
            name="ai_action_steps_cache_status",
        ),
        CheckConstraint(
            "monetary_cost_status IN ('not_applicable', 'calculated', 'partial', 'unknown')",
            name="ai_action_steps_monetary_cost_status",
        ),
        CheckConstraint("sequence_number >= 1", name="ai_action_steps_sequence_number_positive"),
        CheckConstraint("provider_call_count >= 0", name="ai_action_steps_provider_call_count_non_negative"),
        CheckConstraint("retry_count >= 0", name="ai_action_steps_retry_count_non_negative"),
        CheckConstraint("total_tokens >= 0", name="ai_action_steps_total_tokens_non_negative"),
        CheckConstraint("total_cost_usd >= 0", name="ai_action_steps_total_cost_usd_non_negative"),
        UniqueConstraint(
            "action_id", "sequence_number", name="uq_ai_action_steps_action_id_sequence_number"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    action_id: Mapped[int] = mapped_column(
        ForeignKey("ai_actions.id", ondelete="CASCADE"), index=True, nullable=False
    )
    step_type: Mapped[str] = mapped_column(String(64), nullable=False)
    sequence_number: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="pending", server_default=text("'pending'")
    )
    execution_source: Mapped[str] = mapped_column(String(16), nullable=False)
    cache_status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="not_applicable", server_default=text("'not_applicable'")
    )
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    provider_call_count: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, server_default=text("0")
    )
    retry_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    total_tokens: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    total_cost_usd: Mapped[Decimal] = mapped_column(
        Numeric(18, 9), nullable=False, default=Decimal("0"), server_default=text("0")
    )
    monetary_cost_status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="not_applicable", server_default=text("'not_applicable'")
    )
    error_category: Mapped[str | None] = mapped_column(String(64), nullable=True)
    idempotency_key: Mapped[str | None] = mapped_column(String(128), index=True, nullable=True)

    action: Mapped[AiAction] = relationship(back_populates="steps")
    provider_attempts: Mapped[list[AiProviderAttempt]] = relationship(
        back_populates="step", cascade="all, delete-orphan"
    )


class AiProviderAttempt(TimestampMixin, Base):
    """One durable row per individual paid-provider HTTP attempt. A retry
    always creates a *new* row (``attempt_number`` incremented) rather than
    overwriting a failed attempt - ``(step_id, attempt_number)`` is unique,
    which is also what makes a Celery redelivery of the same logical attempt
    safe to re-run: the repository looks up the existing row for that pair
    before creating a new one instead of blindly inserting again."""

    __tablename__ = "ai_provider_attempts"
    __table_args__ = (
        CheckConstraint(
            "status IN ("
            "'pending', 'succeeded', 'timeout', 'rate_limited', 'http_error', 'invalid_response', "
            "'empty_response', 'cancelled', 'audit_error', 'internal_error'"
            ")",
            name="ai_provider_attempts_status",
        ),
        CheckConstraint(
            "monetary_cost_status IN ('not_applicable', 'calculated', 'partial', 'unknown')",
            name="ai_provider_attempts_monetary_cost_status",
        ),
        CheckConstraint("attempt_number >= 1", name="ai_provider_attempts_attempt_number_positive"),
        CheckConstraint(
            "input_tokens IS NULL OR input_tokens >= 0", name="ai_provider_attempts_input_tokens_non_negative"
        ),
        CheckConstraint(
            "cached_input_tokens IS NULL OR cached_input_tokens >= 0",
            name="ai_provider_attempts_cached_input_tokens_non_negative",
        ),
        CheckConstraint(
            "uncached_input_tokens IS NULL OR uncached_input_tokens >= 0",
            name="ai_provider_attempts_uncached_input_tokens_non_negative",
        ),
        CheckConstraint(
            "output_tokens IS NULL OR output_tokens >= 0",
            name="ai_provider_attempts_output_tokens_non_negative",
        ),
        CheckConstraint(
            "reasoning_tokens IS NULL OR reasoning_tokens >= 0",
            name="ai_provider_attempts_reasoning_tokens_non_negative",
        ),
        CheckConstraint(
            "total_tokens IS NULL OR total_tokens >= 0",
            name="ai_provider_attempts_total_tokens_non_negative",
        ),
        UniqueConstraint(
            "step_id", "attempt_number", name="uq_ai_provider_attempts_step_id_attempt_number"
        ),
        UniqueConstraint("provider_call_id", name="uq_ai_provider_attempts_provider_call_id"),
        Index(
            "ix_ai_provider_attempts_provider_model_created_at", "provider", "model", "created_at"
        ),
        Index("ix_ai_provider_attempts_status_created_at", "status", "created_at"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    action_id: Mapped[int] = mapped_column(
        ForeignKey("ai_actions.id", ondelete="CASCADE"), index=True, nullable=False
    )
    step_id: Mapped[int] = mapped_column(
        ForeignKey("ai_action_steps.id", ondelete="CASCADE"), index=True, nullable=False
    )
    provider_call_id: Mapped[str] = mapped_column(String(64), nullable=False)
    provider: Mapped[str] = mapped_column(String(32), nullable=False)
    model: Mapped[str] = mapped_column(String(120), nullable=False)
    provider_request_id: Mapped[str | None] = mapped_column(String(120), nullable=True)
    attempt_number: Mapped[int] = mapped_column(
        Integer, nullable=False, default=1, server_default=text("1")
    )
    retry_reason: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(
        String(24), nullable=False, default="pending", server_default=text("'pending'")
    )
    success: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("false")
    )
    request_started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    request_completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    latency_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    input_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    cached_input_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    uncached_input_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    output_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    reasoning_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    uncached_input_cost_usd: Mapped[Decimal | None] = mapped_column(Numeric(18, 9), nullable=True)
    cached_input_cost_usd: Mapped[Decimal | None] = mapped_column(Numeric(18, 9), nullable=True)
    output_cost_usd: Mapped[Decimal | None] = mapped_column(Numeric(18, 9), nullable=True)
    reasoning_cost_usd: Mapped[Decimal | None] = mapped_column(Numeric(18, 9), nullable=True)
    total_cost_usd: Mapped[Decimal | None] = mapped_column(Numeric(18, 9), nullable=True)
    cached_input_savings_usd: Mapped[Decimal | None] = mapped_column(Numeric(18, 9), nullable=True)
    monetary_cost_status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="not_applicable", server_default=text("'not_applicable'")
    )
    pricing_version: Mapped[str | None] = mapped_column(String(64), nullable=True)
    http_status: Mapped[int | None] = mapped_column(Integer, nullable=True)
    error_category: Mapped[str | None] = mapped_column(String(64), nullable=True)
    raw_usage_redacted: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    action: Mapped[AiAction] = relationship(back_populates="provider_attempts")
    step: Mapped[AiActionStep] = relationship(back_populates="provider_attempts")

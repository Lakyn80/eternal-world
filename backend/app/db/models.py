from __future__ import annotations

from datetime import date
from typing import Any

from sqlalchemy import Boolean, CheckConstraint, Date, ForeignKey, Integer, JSON, String, Text, text
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
            "memory_type IN ('episodic', 'semantic', 'profile', 'system')",
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
    memory_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="episodic",
        server_default=text("'episodic'"),
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
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

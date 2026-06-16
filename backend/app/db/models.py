from __future__ import annotations

from typing import Any

from sqlalchemy import Boolean, CheckConstraint, ForeignKey, Integer, JSON, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
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

    memory_profile: Mapped[MemoryProfile | None] = relationship(
        back_populates="user",
        uselist=False,
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


class MemoryProfile(TimestampMixin, Base):
    __tablename__ = "memory_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False,
    )
    display_name: Mapped[str] = mapped_column(String(120), nullable=False)
    persona_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    long_term_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    preferences: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False, default=dict)

    user: Mapped[User] = relationship(back_populates="memory_profile")
    chat_messages: Mapped[list[ChatMessage]] = relationship(back_populates="memory_profile")
    memories: Mapped[list[Memory]] = relationship(back_populates="memory_profile")


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

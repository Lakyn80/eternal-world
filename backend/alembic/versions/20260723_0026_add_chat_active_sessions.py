"""Add chat_active_sessions table.

Task 65.7 - Redis-backed Chat active-conversation restoration and reset.
Purely additive: one small table tracking which `conversation_id` is
currently "active" per (user, profile) pair, so a Redis cache-miss can be
rebuilt from Postgres by filtering `chat_messages.message_metadata->>
'conversation_id'` (no schema change to `chat_messages` itself - the
existing JSON `message_metadata` column already supports arbitrary keys).

Revision ID: 20260723_0026
Revises: 20260722_0025
Create Date: 2026-07-23 09:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260723_0026"
down_revision = "20260722_0025"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "chat_active_sessions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("conversation_id", sa.String(length=36), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["profile_id"], ["memory_profiles.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "profile_id", name="uq_chat_active_sessions_user_profile"),
    )
    op.create_index("ix_chat_active_sessions_user_id", "chat_active_sessions", ["user_id"])
    op.create_index("ix_chat_active_sessions_profile_id", "chat_active_sessions", ["profile_id"])


def downgrade() -> None:
    op.drop_index("ix_chat_active_sessions_profile_id", table_name="chat_active_sessions")
    op.drop_index("ix_chat_active_sessions_user_id", table_name="chat_active_sessions")
    op.drop_table("chat_active_sessions")

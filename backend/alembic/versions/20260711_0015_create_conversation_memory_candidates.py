"""Create conversation_memory_candidates table.

Revision ID: 20260711_0015
Revises: 20260704_0014
Create Date: 2026-07-11 07:20:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260711_0015"
down_revision = "20260704_0014"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "conversation_memory_candidates",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("avatar_id", sa.String(length=120), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=True),
        sa.Column("conversation_id", sa.String(length=120), nullable=True),
        sa.Column("trace_id", sa.String(length=120), nullable=True),
        sa.Column(
            "source",
            sa.String(length=32),
            server_default=sa.text("'conversation'"),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.String(length=32),
            server_default=sa.text("'needs_review'"),
            nullable=False,
        ),
        sa.Column(
            "confidence",
            sa.String(length=32),
            server_default=sa.text("'unverified'"),
            nullable=False,
        ),
        sa.Column("user_message_excerpt", sa.String(length=160), nullable=False),
        sa.Column("proposed_memory_text", sa.String(length=500), nullable=False),
        sa.Column("reason", sa.String(length=500), nullable=False),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("reviewed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("reviewed_by", sa.Integer(), nullable=True),
        sa.Column("review_note", sa.String(length=500), nullable=True),
        sa.Column("rejection_reason", sa.String(length=500), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "source IN ('conversation')",
            name=op.f("ck_conversation_memory_candidates_conversation_memory_candidates_source"),
        ),
        sa.CheckConstraint(
            "status IN ('needs_review', 'approved', 'rejected', 'archived')",
            name=op.f("ck_conversation_memory_candidates_conversation_memory_candidates_status"),
        ),
        sa.CheckConstraint(
            "confidence IN ('unverified')",
            name=op.f("ck_conversation_memory_candidates_conversation_memory_candidates_confidence"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_conversation_memory_candidates_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_conversation_memory_candidates_profile_id_memory_profiles"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["reviewed_by"],
            ["users.id"],
            name=op.f("fk_conversation_memory_candidates_reviewed_by_users"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_conversation_memory_candidates")),
    )
    op.create_index(
        op.f("ix_conversation_memory_candidates_owner_user_id"),
        "conversation_memory_candidates",
        ["owner_user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_conversation_memory_candidates_avatar_id"),
        "conversation_memory_candidates",
        ["avatar_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_conversation_memory_candidates_profile_id"),
        "conversation_memory_candidates",
        ["profile_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_conversation_memory_candidates_trace_id"),
        "conversation_memory_candidates",
        ["trace_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_conversation_memory_candidates_status"),
        "conversation_memory_candidates",
        ["status"],
        unique=False,
    )
    op.create_index(
        op.f("ix_conversation_memory_candidates_reviewed_by"),
        "conversation_memory_candidates",
        ["reviewed_by"],
        unique=False,
    )
    op.create_index(
        "ix_cmc_created_at",
        "conversation_memory_candidates",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "ix_cmc_owner_profile_status",
        "conversation_memory_candidates",
        ["owner_user_id", "profile_id", "status"],
        unique=False,
    )
    op.create_index(
        "ix_cmc_avatar_status",
        "conversation_memory_candidates",
        ["avatar_id", "status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_cmc_avatar_status", table_name="conversation_memory_candidates")
    op.drop_index(
        "ix_cmc_owner_profile_status",
        table_name="conversation_memory_candidates",
    )
    op.drop_index("ix_cmc_created_at", table_name="conversation_memory_candidates")
    op.drop_index(op.f("ix_conversation_memory_candidates_reviewed_by"), table_name="conversation_memory_candidates")
    op.drop_index(op.f("ix_conversation_memory_candidates_status"), table_name="conversation_memory_candidates")
    op.drop_index(op.f("ix_conversation_memory_candidates_trace_id"), table_name="conversation_memory_candidates")
    op.drop_index(op.f("ix_conversation_memory_candidates_profile_id"), table_name="conversation_memory_candidates")
    op.drop_index(op.f("ix_conversation_memory_candidates_avatar_id"), table_name="conversation_memory_candidates")
    op.drop_index(op.f("ix_conversation_memory_candidates_owner_user_id"), table_name="conversation_memory_candidates")
    op.drop_table("conversation_memory_candidates")

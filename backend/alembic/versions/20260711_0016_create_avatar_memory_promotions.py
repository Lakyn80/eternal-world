"""Create avatar_memory_promotions table.

Revision ID: 20260711_0016
Revises: 20260711_0015
Create Date: 2026-07-11 08:10:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260711_0016"
down_revision = "20260711_0015"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "avatar_memory_promotions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("candidate_id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("avatar_id", sa.String(length=120), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=True),
        sa.Column(
            "source_type",
            sa.String(length=32),
            server_default=sa.text("'conversation_candidate'"),
            nullable=False,
        ),
        sa.Column(
            "promotion_status",
            sa.String(length=32),
            server_default=sa.text("'pending_index'"),
            nullable=False,
        ),
        sa.Column("approved_memory_text", sa.String(length=500), nullable=False),
        sa.Column("normalized_memory_text", sa.String(length=500), nullable=False),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("indexed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("cancelled_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("failure_reason", sa.String(length=500), nullable=True),
        sa.Column("trace_id", sa.String(length=120), nullable=True),
        sa.Column("source_candidate_status_snapshot", sa.String(length=32), nullable=False),
        sa.Column("review_note_snapshot", sa.String(length=500), nullable=True),
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
            "source_type IN ('conversation_candidate')",
            name=op.f("ck_avatar_memory_promotions_avatar_memory_promotions_source_type"),
        ),
        sa.CheckConstraint(
            "promotion_status IN ('pending_index', 'indexed', 'failed', 'cancelled')",
            name=op.f("ck_avatar_memory_promotions_avatar_memory_promotions_status"),
        ),
        sa.ForeignKeyConstraint(
            ["candidate_id"],
            ["conversation_memory_candidates.id"],
            name=op.f("fk_avatar_memory_promotions_candidate_id_conversation_memory_candidates"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_avatar_memory_promotions_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_avatar_memory_promotions_profile_id_memory_profiles"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_avatar_memory_promotions")),
        sa.UniqueConstraint("candidate_id", name=op.f("uq_avatar_memory_promotions_candidate_id")),
    )
    op.create_index(
        op.f("ix_avatar_memory_promotions_candidate_id"),
        "avatar_memory_promotions",
        ["candidate_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_avatar_memory_promotions_owner_user_id"),
        "avatar_memory_promotions",
        ["owner_user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_avatar_memory_promotions_avatar_id"),
        "avatar_memory_promotions",
        ["avatar_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_avatar_memory_promotions_profile_id"),
        "avatar_memory_promotions",
        ["profile_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_avatar_memory_promotions_promotion_status"),
        "avatar_memory_promotions",
        ["promotion_status"],
        unique=False,
    )
    op.create_index(
        op.f("ix_avatar_memory_promotions_trace_id"),
        "avatar_memory_promotions",
        ["trace_id"],
        unique=False,
    )
    op.create_index(
        "ix_amp_created_at",
        "avatar_memory_promotions",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "ix_amp_owner_profile_status",
        "avatar_memory_promotions",
        ["owner_user_id", "profile_id", "promotion_status"],
        unique=False,
    )
    op.create_index(
        "ix_amp_avatar_status",
        "avatar_memory_promotions",
        ["avatar_id", "promotion_status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_amp_avatar_status", table_name="avatar_memory_promotions")
    op.drop_index("ix_amp_owner_profile_status", table_name="avatar_memory_promotions")
    op.drop_index("ix_amp_created_at", table_name="avatar_memory_promotions")
    op.drop_index(op.f("ix_avatar_memory_promotions_trace_id"), table_name="avatar_memory_promotions")
    op.drop_index(op.f("ix_avatar_memory_promotions_promotion_status"), table_name="avatar_memory_promotions")
    op.drop_index(op.f("ix_avatar_memory_promotions_profile_id"), table_name="avatar_memory_promotions")
    op.drop_index(op.f("ix_avatar_memory_promotions_avatar_id"), table_name="avatar_memory_promotions")
    op.drop_index(op.f("ix_avatar_memory_promotions_owner_user_id"), table_name="avatar_memory_promotions")
    op.drop_index(op.f("ix_avatar_memory_promotions_candidate_id"), table_name="avatar_memory_promotions")
    op.drop_table("avatar_memory_promotions")

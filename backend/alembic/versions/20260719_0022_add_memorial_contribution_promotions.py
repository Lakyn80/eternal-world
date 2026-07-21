"""Create memorial_contribution_promotions table.

Task 65.1B - bridges an approved+current MemorialContribution into the
existing canonical memory / embedding / indexing pipeline, mirroring the
avatar_memory_promotions pattern. Purely additive: no existing table is
altered and no data is migrated.

Revision ID: 20260719_0022
Revises: 20260716_0021
Create Date: 2026-07-19 18:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260719_0022"
down_revision = "20260716_0021"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "memorial_contribution_promotions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("contribution_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column(
            "promotion_status",
            sa.String(length=32),
            server_default=sa.text("'pending_index'"),
            nullable=False,
        ),
        sa.Column("approved_memory_text", sa.Text(), nullable=False),
        sa.Column("normalized_memory_text", sa.Text(), nullable=False),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("indexed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("failed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("retired_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("failure_reason", sa.String(length=500), nullable=True),
        sa.Column("target_collection_name", sa.String(length=200), nullable=True),
        sa.Column("qdrant_point_id", sa.String(length=64), nullable=True),
        sa.Column(
            "indexing_attempt_count",
            sa.Integer(),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column("rag_source_id", sa.Integer(), nullable=True),
        sa.Column("rag_chunk_id", sa.Integer(), nullable=True),
        sa.Column("rag_embedding_id", sa.Integer(), nullable=True),
        sa.Column("source_contribution_status_snapshot", sa.String(length=32), nullable=False),
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
            "promotion_status IN ('pending_index', 'indexed', 'failed', 'retired')",
            name=op.f(
                "ck_memorial_contribution_promotions_memorial_contribution_promotions_status"
            ),
        ),
        sa.CheckConstraint(
            "indexing_attempt_count >= 0",
            name=op.f(
                "ck_memorial_contribution_promotions_"
                "memorial_contribution_promotions_indexing_attempt_count_non_negative"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["contribution_id"],
            ["memorial_contributions.id"],
            name=op.f(
                "fk_memorial_contribution_promotions_contribution_id_memorial_contributions"
            ),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_memorial_contribution_promotions_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["rag_source_id"],
            ["rag_sources.id"],
            name=op.f("fk_memorial_contribution_promotions_rag_source_id_rag_sources"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["rag_chunk_id"],
            ["rag_chunks.id"],
            name=op.f("fk_memorial_contribution_promotions_rag_chunk_id_rag_chunks"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["rag_embedding_id"],
            ["rag_embeddings.id"],
            name=op.f("fk_memorial_contribution_promotions_rag_embedding_id_rag_embeddings"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_memorial_contribution_promotions")),
        sa.UniqueConstraint(
            "contribution_id", name=op.f("uq_memorial_contribution_promotions_contribution_id")
        ),
    )
    op.create_index(
        op.f("ix_memorial_contribution_promotions_contribution_id"),
        "memorial_contribution_promotions",
        ["contribution_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_memorial_contribution_promotions_profile_id"),
        "memorial_contribution_promotions",
        ["profile_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_memorial_contribution_promotions_promotion_status"),
        "memorial_contribution_promotions",
        ["promotion_status"],
        unique=False,
    )
    op.create_index(
        "ix_mcp_created_at",
        "memorial_contribution_promotions",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "ix_mcp_profile_status",
        "memorial_contribution_promotions",
        ["profile_id", "promotion_status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_mcp_profile_status", table_name="memorial_contribution_promotions")
    op.drop_index("ix_mcp_created_at", table_name="memorial_contribution_promotions")
    op.drop_index(
        op.f("ix_memorial_contribution_promotions_promotion_status"),
        table_name="memorial_contribution_promotions",
    )
    op.drop_index(
        op.f("ix_memorial_contribution_promotions_profile_id"),
        table_name="memorial_contribution_promotions",
    )
    op.drop_index(
        op.f("ix_memorial_contribution_promotions_contribution_id"),
        table_name="memorial_contribution_promotions",
    )
    op.drop_table("memorial_contribution_promotions")

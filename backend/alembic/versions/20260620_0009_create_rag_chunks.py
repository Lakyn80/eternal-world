"""Create rag_chunks table.

Revision ID: 20260620_0009
Revises: 20260620_0008
Create Date: 2026-06-20 01:15:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260620_0009"
down_revision = "20260620_0008"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "rag_chunks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("chunk_index", sa.Integer(), nullable=False),
        sa.Column("chunk_text", sa.Text(), nullable=False),
        sa.Column("text_hash", sa.String(length=64), nullable=False),
        sa.Column("token_estimate", sa.Integer(), nullable=False),
        sa.Column("char_count", sa.Integer(), nullable=False),
        sa.Column("sentence_count", sa.Integer(), nullable=False),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("chunk_metadata", sa.JSON(), nullable=True),
        sa.Column(
            "validation_status",
            sa.String(length=16),
            server_default=sa.text("'valid'"),
            nullable=False,
        ),
        sa.Column("validation_errors", sa.JSON(), nullable=True),
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
            "validation_status IN ('valid', 'warning', 'invalid')",
            name=op.f("ck_rag_chunks_rag_chunks_validation_status"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_rag_chunks_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_rag_chunks_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["rag_sources.id"],
            name=op.f("fk_rag_chunks_source_id_rag_sources"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rag_chunks")),
    )
    op.create_index(op.f("ix_rag_chunks_owner_user_id"), "rag_chunks", ["owner_user_id"], unique=False)
    op.create_index(op.f("ix_rag_chunks_profile_id"), "rag_chunks", ["profile_id"], unique=False)
    op.create_index(op.f("ix_rag_chunks_source_id"), "rag_chunks", ["source_id"], unique=False)
    op.create_index(op.f("ix_rag_chunks_text_hash"), "rag_chunks", ["text_hash"], unique=False)
    op.create_index(
        op.f("ix_rag_chunks_validation_status"),
        "rag_chunks",
        ["validation_status"],
        unique=False,
    )
    op.create_index(
        "ix_rag_chunks_owner_user_id_profile_id",
        "rag_chunks",
        ["owner_user_id", "profile_id"],
        unique=False,
    )
    op.create_index(
        "ix_rag_chunks_profile_id_source_id",
        "rag_chunks",
        ["profile_id", "source_id"],
        unique=False,
    )
    op.create_index(
        "ix_rag_chunks_source_id_chunk_index",
        "rag_chunks",
        ["source_id", "chunk_index"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_rag_chunks_source_id_chunk_index", table_name="rag_chunks")
    op.drop_index("ix_rag_chunks_profile_id_source_id", table_name="rag_chunks")
    op.drop_index("ix_rag_chunks_owner_user_id_profile_id", table_name="rag_chunks")
    op.drop_index(op.f("ix_rag_chunks_validation_status"), table_name="rag_chunks")
    op.drop_index(op.f("ix_rag_chunks_text_hash"), table_name="rag_chunks")
    op.drop_index(op.f("ix_rag_chunks_source_id"), table_name="rag_chunks")
    op.drop_index(op.f("ix_rag_chunks_profile_id"), table_name="rag_chunks")
    op.drop_index(op.f("ix_rag_chunks_owner_user_id"), table_name="rag_chunks")
    op.drop_table("rag_chunks")

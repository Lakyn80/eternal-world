"""Create rag_embeddings table.

Revision ID: 20260620_0010
Revises: 20260620_0009
Create Date: 2026-06-20 02:10:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260620_0010"
down_revision = "20260620_0009"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "rag_embeddings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("chunk_id", sa.Integer(), nullable=False),
        sa.Column("model_code", sa.String(length=64), nullable=False),
        sa.Column("vector", sa.JSON(), nullable=True),
        sa.Column("vector_dimension", sa.Integer(), nullable=False),
        sa.Column("text_hash", sa.String(length=64), nullable=False),
        sa.Column(
            "status",
            sa.String(length=16),
            server_default=sa.text("'embedded'"),
            nullable=False,
        ),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("embedding_metadata", sa.JSON(), nullable=True),
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
            "status IN ('embedded', 'failed')",
            name=op.f("ck_rag_embeddings_rag_embeddings_status"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_rag_embeddings_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_rag_embeddings_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["rag_sources.id"],
            name=op.f("fk_rag_embeddings_source_id_rag_sources"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["chunk_id"],
            ["rag_chunks.id"],
            name=op.f("fk_rag_embeddings_chunk_id_rag_chunks"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rag_embeddings")),
    )
    op.create_index(op.f("ix_rag_embeddings_owner_user_id"), "rag_embeddings", ["owner_user_id"], unique=False)
    op.create_index(op.f("ix_rag_embeddings_profile_id"), "rag_embeddings", ["profile_id"], unique=False)
    op.create_index(op.f("ix_rag_embeddings_source_id"), "rag_embeddings", ["source_id"], unique=False)
    op.create_index(op.f("ix_rag_embeddings_chunk_id"), "rag_embeddings", ["chunk_id"], unique=False)
    op.create_index(op.f("ix_rag_embeddings_model_code"), "rag_embeddings", ["model_code"], unique=False)
    op.create_index(op.f("ix_rag_embeddings_status"), "rag_embeddings", ["status"], unique=False)
    op.create_index(
        "ix_rag_embeddings_owner_user_id_profile_id",
        "rag_embeddings",
        ["owner_user_id", "profile_id"],
        unique=False,
    )
    op.create_index(
        "ix_rag_embeddings_profile_id_model_code",
        "rag_embeddings",
        ["profile_id", "model_code"],
        unique=False,
    )
    op.create_index(
        "ix_rag_embeddings_chunk_id_model_code",
        "rag_embeddings",
        ["chunk_id", "model_code"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_rag_embeddings_chunk_id_model_code", table_name="rag_embeddings")
    op.drop_index("ix_rag_embeddings_profile_id_model_code", table_name="rag_embeddings")
    op.drop_index("ix_rag_embeddings_owner_user_id_profile_id", table_name="rag_embeddings")
    op.drop_index(op.f("ix_rag_embeddings_status"), table_name="rag_embeddings")
    op.drop_index(op.f("ix_rag_embeddings_model_code"), table_name="rag_embeddings")
    op.drop_index(op.f("ix_rag_embeddings_chunk_id"), table_name="rag_embeddings")
    op.drop_index(op.f("ix_rag_embeddings_source_id"), table_name="rag_embeddings")
    op.drop_index(op.f("ix_rag_embeddings_profile_id"), table_name="rag_embeddings")
    op.drop_index(op.f("ix_rag_embeddings_owner_user_id"), table_name="rag_embeddings")
    op.drop_table("rag_embeddings")

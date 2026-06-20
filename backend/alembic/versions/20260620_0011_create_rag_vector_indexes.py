"""Create rag_vector_indexes table.

Revision ID: 20260620_0011
Revises: 20260620_0010
Create Date: 2026-06-20 03:05:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260620_0011"
down_revision = "20260620_0010"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "rag_vector_indexes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("chunk_id", sa.Integer(), nullable=False),
        sa.Column("embedding_id", sa.Integer(), nullable=False),
        sa.Column("model_code", sa.String(length=64), nullable=False),
        sa.Column("qdrant_collection", sa.String(length=200), nullable=False),
        sa.Column("qdrant_point_id", sa.String(length=64), nullable=False),
        sa.Column(
            "status",
            sa.String(length=16),
            server_default=sa.text("'indexed'"),
            nullable=False,
        ),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("indexed_at", sa.DateTime(timezone=True), nullable=True),
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
            "status IN ('indexed', 'failed')",
            name=op.f("ck_rag_vector_indexes_rag_vector_indexes_status"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_rag_vector_indexes_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_rag_vector_indexes_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["rag_sources.id"],
            name=op.f("fk_rag_vector_indexes_source_id_rag_sources"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["chunk_id"],
            ["rag_chunks.id"],
            name=op.f("fk_rag_vector_indexes_chunk_id_rag_chunks"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["embedding_id"],
            ["rag_embeddings.id"],
            name=op.f("fk_rag_vector_indexes_embedding_id_rag_embeddings"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rag_vector_indexes")),
    )
    op.create_index(op.f("ix_rag_vector_indexes_owner_user_id"), "rag_vector_indexes", ["owner_user_id"], unique=False)
    op.create_index(op.f("ix_rag_vector_indexes_profile_id"), "rag_vector_indexes", ["profile_id"], unique=False)
    op.create_index(op.f("ix_rag_vector_indexes_source_id"), "rag_vector_indexes", ["source_id"], unique=False)
    op.create_index(op.f("ix_rag_vector_indexes_chunk_id"), "rag_vector_indexes", ["chunk_id"], unique=False)
    op.create_index(op.f("ix_rag_vector_indexes_embedding_id"), "rag_vector_indexes", ["embedding_id"], unique=False)
    op.create_index(op.f("ix_rag_vector_indexes_model_code"), "rag_vector_indexes", ["model_code"], unique=False)
    op.create_index(
        op.f("ix_rag_vector_indexes_qdrant_collection"),
        "rag_vector_indexes",
        ["qdrant_collection"],
        unique=False,
    )
    op.create_index(op.f("ix_rag_vector_indexes_status"), "rag_vector_indexes", ["status"], unique=False)
    op.create_index(
        "ix_rag_vector_indexes_owner_user_id_profile_id",
        "rag_vector_indexes",
        ["owner_user_id", "profile_id"],
        unique=False,
    )
    op.create_index(
        "ix_rag_vector_indexes_profile_id_model_code",
        "rag_vector_indexes",
        ["profile_id", "model_code"],
        unique=False,
    )
    op.create_index(
        "ix_rag_vector_indexes_embedding_id_qdrant_collection",
        "rag_vector_indexes",
        ["embedding_id", "qdrant_collection"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_rag_vector_indexes_embedding_id_qdrant_collection", table_name="rag_vector_indexes")
    op.drop_index("ix_rag_vector_indexes_profile_id_model_code", table_name="rag_vector_indexes")
    op.drop_index("ix_rag_vector_indexes_owner_user_id_profile_id", table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_status"), table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_qdrant_collection"), table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_model_code"), table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_embedding_id"), table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_chunk_id"), table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_source_id"), table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_profile_id"), table_name="rag_vector_indexes")
    op.drop_index(op.f("ix_rag_vector_indexes_owner_user_id"), table_name="rag_vector_indexes")
    op.drop_table("rag_vector_indexes")

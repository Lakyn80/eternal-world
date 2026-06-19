"""Create rag_sources table.

Revision ID: 20260620_0008
Revises: 20260619_0007
Create Date: 2026-06-20 00:30:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260620_0008"
down_revision = "20260619_0007"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "rag_sources",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("source_type", sa.String(length=32), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("raw_text", sa.Text(), nullable=False),
        sa.Column("normalized_text", sa.Text(), nullable=True),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column(
            "status",
            sa.String(length=32),
            server_default=sa.text("'ready_for_cleaning'"),
            nullable=False,
        ),
        sa.Column("processing_error", sa.Text(), nullable=True),
        sa.Column("source_metadata", sa.JSON(), nullable=True),
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
            (
                "source_type IN ("
                "'manual_text', 'biography', 'timeline_memory', 'document_text', "
                "'chat_export', 'audio_transcript', 'video_transcript', "
                "'letter', 'diary', 'other')"
            ),
            name=op.f("ck_rag_sources_rag_sources_source_type"),
        ),
        sa.CheckConstraint(
            (
                "status IN ("
                "'pending', 'ready_for_cleaning', 'cleaned', 'ready_for_chunking', "
                "'chunked', 'ready_for_embedding', 'embedded', 'failed')"
            ),
            name=op.f("ck_rag_sources_rag_sources_status"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_rag_sources_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_rag_sources_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rag_sources")),
    )
    op.create_index(op.f("ix_rag_sources_owner_user_id"), "rag_sources", ["owner_user_id"], unique=False)
    op.create_index(op.f("ix_rag_sources_profile_id"), "rag_sources", ["profile_id"], unique=False)
    op.create_index(op.f("ix_rag_sources_source_type"), "rag_sources", ["source_type"], unique=False)
    op.create_index(op.f("ix_rag_sources_status"), "rag_sources", ["status"], unique=False)
    op.create_index("ix_rag_sources_created_at", "rag_sources", ["created_at"], unique=False)
    op.create_index(
        "ix_rag_sources_owner_user_id_profile_id",
        "rag_sources",
        ["owner_user_id", "profile_id"],
        unique=False,
    )
    op.create_index(
        "ix_rag_sources_profile_id_status",
        "rag_sources",
        ["profile_id", "status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_rag_sources_profile_id_status", table_name="rag_sources")
    op.drop_index("ix_rag_sources_owner_user_id_profile_id", table_name="rag_sources")
    op.drop_index("ix_rag_sources_created_at", table_name="rag_sources")
    op.drop_index(op.f("ix_rag_sources_status"), table_name="rag_sources")
    op.drop_index(op.f("ix_rag_sources_source_type"), table_name="rag_sources")
    op.drop_index(op.f("ix_rag_sources_profile_id"), table_name="rag_sources")
    op.drop_index(op.f("ix_rag_sources_owner_user_id"), table_name="rag_sources")
    op.drop_table("rag_sources")

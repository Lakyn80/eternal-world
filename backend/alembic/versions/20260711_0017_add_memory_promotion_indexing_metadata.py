"""Add approved memory promotion indexing metadata.

Revision ID: 20260711_0017
Revises: 20260711_0016
Create Date: 2026-07-11 12:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260711_0017"
down_revision = "20260711_0016"
branch_labels = None
depends_on = None


RAG_SOURCE_TYPES_WITH_CONVERSATION_CANDIDATE = (
    "source_type IN ('manual_text', 'biography', 'timeline_memory', 'document_text', "
    "'chat_export', 'audio_transcript', 'video_transcript', 'letter', 'diary', "
    "'conversation_candidate', 'other')"
)
ORIGINAL_RAG_SOURCE_TYPES = (
    "source_type IN ('manual_text', 'biography', 'timeline_memory', 'document_text', "
    "'chat_export', 'audio_transcript', 'video_transcript', 'letter', 'diary', 'other')"
)


def upgrade() -> None:
    op.drop_constraint(
        op.f("ck_rag_sources_rag_sources_source_type"),
        "rag_sources",
        type_="check",
    )
    op.create_check_constraint(
        op.f("ck_rag_sources_rag_sources_source_type"),
        "rag_sources",
        RAG_SOURCE_TYPES_WITH_CONVERSATION_CANDIDATE,
    )
    op.add_column("avatar_memory_promotions", sa.Column("failed_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column(
        "avatar_memory_promotions",
        sa.Column("target_collection_name", sa.String(length=200), nullable=True),
    )
    op.add_column(
        "avatar_memory_promotions",
        sa.Column("qdrant_point_id", sa.String(length=64), nullable=True),
    )
    op.add_column(
        "avatar_memory_promotions",
        sa.Column("indexing_attempt_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
    )
    op.add_column("avatar_memory_promotions", sa.Column("rag_source_id", sa.Integer(), nullable=True))
    op.add_column("avatar_memory_promotions", sa.Column("rag_chunk_id", sa.Integer(), nullable=True))
    op.add_column("avatar_memory_promotions", sa.Column("rag_embedding_id", sa.Integer(), nullable=True))
    op.create_check_constraint(
        op.f("ck_avatar_memory_promotions_avatar_memory_promotions_indexing_attempt_count_non_negative"),
        "avatar_memory_promotions",
        "indexing_attempt_count >= 0",
    )
    op.create_foreign_key(
        op.f("fk_avatar_memory_promotions_rag_source_id_rag_sources"),
        "avatar_memory_promotions",
        "rag_sources",
        ["rag_source_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        op.f("fk_avatar_memory_promotions_rag_chunk_id_rag_chunks"),
        "avatar_memory_promotions",
        "rag_chunks",
        ["rag_chunk_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        op.f("fk_avatar_memory_promotions_rag_embedding_id_rag_embeddings"),
        "avatar_memory_promotions",
        "rag_embeddings",
        ["rag_embedding_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("ck_avatar_memory_promotions_avatar_memory_promotions_indexing_attempt_count_non_negative"),
        "avatar_memory_promotions",
        type_="check",
    )
    op.drop_constraint(
        op.f("fk_avatar_memory_promotions_rag_embedding_id_rag_embeddings"),
        "avatar_memory_promotions",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_avatar_memory_promotions_rag_chunk_id_rag_chunks"),
        "avatar_memory_promotions",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_avatar_memory_promotions_rag_source_id_rag_sources"),
        "avatar_memory_promotions",
        type_="foreignkey",
    )
    op.drop_column("avatar_memory_promotions", "rag_embedding_id")
    op.drop_column("avatar_memory_promotions", "rag_chunk_id")
    op.drop_column("avatar_memory_promotions", "rag_source_id")
    op.drop_column("avatar_memory_promotions", "indexing_attempt_count")
    op.drop_column("avatar_memory_promotions", "qdrant_point_id")
    op.drop_column("avatar_memory_promotions", "target_collection_name")
    op.drop_column("avatar_memory_promotions", "failed_at")
    op.execute(
        "UPDATE rag_sources SET source_type = 'other' "
        "WHERE source_type = 'conversation_candidate'"
    )
    op.drop_constraint(
        op.f("ck_rag_sources_rag_sources_source_type"),
        "rag_sources",
        type_="check",
    )
    op.create_check_constraint(
        op.f("ck_rag_sources_rag_sources_source_type"),
        "rag_sources",
        ORIGINAL_RAG_SOURCE_TYPES,
    )

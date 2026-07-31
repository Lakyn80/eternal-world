"""Task 65.13.2 - generalize content translation domain.

Revision ID: 20260731_0031
Revises: 20260731_0030
Create Date: 2026-07-31

- Expand ``memory_content_translations`` source/target language CHECKs with
  ``de`` (registry translation capability).
- Add nullable ``profile_id`` for memorial isolation / authorization.
- Allow ``content_translation`` as a ``background_jobs.job_type``.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260731_0031"
down_revision = "20260731_0030"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint(
        "memory_content_translations_source_language",
        "memory_content_translations",
        type_="check",
    )
    op.drop_constraint(
        "memory_content_translations_target_language",
        "memory_content_translations",
        type_="check",
    )
    op.create_check_constraint(
        "memory_content_translations_source_language",
        "memory_content_translations",
        "source_language IN ('cs', 'ru', 'en', 'de')",
    )
    op.create_check_constraint(
        "memory_content_translations_target_language",
        "memory_content_translations",
        "target_language IN ('cs', 'ru', 'en', 'de')",
    )

    op.add_column(
        "memory_content_translations",
        sa.Column("profile_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        "fk_memory_content_translations_profile_id_memory_profiles",
        "memory_content_translations",
        "memory_profiles",
        ["profile_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_index(
        "ix_memory_content_translations_profile_id",
        "memory_content_translations",
        ["profile_id"],
    )

    # Best-effort backfill from candidate / contribution / clarification FKs.
    op.execute(
        """
        UPDATE memory_content_translations AS mct
        SET profile_id = cmc.profile_id
        FROM conversation_memory_candidates AS cmc
        WHERE mct.candidate_id = cmc.id
          AND mct.profile_id IS NULL
        """
    )
    op.execute(
        """
        UPDATE memory_content_translations AS mct
        SET profile_id = fmc.profile_id
        FROM family_memory_contributions AS fmc
        WHERE mct.contribution_id = fmc.id
          AND mct.profile_id IS NULL
        """
    )
    op.execute(
        """
        UPDATE memory_content_translations AS mct
        SET profile_id = cmc.profile_id
        FROM memory_clarification_questions AS mcq
        JOIN conversation_memory_candidates AS cmc ON cmc.id = mcq.candidate_id
        WHERE mct.clarification_id = mcq.id
          AND mct.profile_id IS NULL
        """
    )

    op.drop_constraint("background_jobs_job_type", "background_jobs", type_="check")
    op.create_check_constraint(
        "background_jobs_job_type",
        "background_jobs",
        "job_type IN ("
        "'smoke_test', 'system_milestone', 'rag_source_ingestion', 'rag_chunking', "
        "'embedding_generation', 'qdrant_indexing', 'rag_retrieval', "
        "'brain_agent_generation', 'media_processing', 'voice_generation', "
        "'video_generation', 'content_translation'"
        ")",
    )


def downgrade() -> None:
    op.drop_constraint("background_jobs_job_type", "background_jobs", type_="check")
    op.create_check_constraint(
        "background_jobs_job_type",
        "background_jobs",
        "job_type IN ("
        "'smoke_test', 'system_milestone', 'rag_source_ingestion', 'rag_chunking', "
        "'embedding_generation', 'qdrant_indexing', 'rag_retrieval', "
        "'brain_agent_generation', 'media_processing', 'voice_generation', "
        "'video_generation'"
        ")",
    )

    op.drop_index("ix_memory_content_translations_profile_id", table_name="memory_content_translations")
    op.drop_constraint(
        "fk_memory_content_translations_profile_id_memory_profiles",
        "memory_content_translations",
        type_="foreignkey",
    )
    op.drop_column("memory_content_translations", "profile_id")

    op.drop_constraint(
        "memory_content_translations_source_language",
        "memory_content_translations",
        type_="check",
    )
    op.drop_constraint(
        "memory_content_translations_target_language",
        "memory_content_translations",
        type_="check",
    )
    op.create_check_constraint(
        "memory_content_translations_source_language",
        "memory_content_translations",
        "source_language IN ('cs', 'ru', 'en')",
    )
    op.create_check_constraint(
        "memory_content_translations_target_language",
        "memory_content_translations",
        "target_language IN ('cs', 'ru', 'en')",
    )

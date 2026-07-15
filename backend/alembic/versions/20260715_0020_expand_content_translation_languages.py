"""Expand content translation language constraints to English.

Revision ID: 20260715_0020
Revises: 20260713_0019
Create Date: 2026-07-15 11:30:00

"""
from __future__ import annotations

from alembic import op


revision = "20260715_0020"
down_revision = "20260713_0019"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_source_language"),
        "memory_content_translations",
        type_="check",
    )
    op.drop_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_target_language"),
        "memory_content_translations",
        type_="check",
    )
    op.create_check_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_source_language"),
        "memory_content_translations",
        "source_language IN ('cs', 'ru', 'en')",
    )
    op.create_check_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_target_language"),
        "memory_content_translations",
        "target_language IN ('cs', 'ru', 'en')",
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_target_language"),
        "memory_content_translations",
        type_="check",
    )
    op.drop_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_source_language"),
        "memory_content_translations",
        type_="check",
    )
    op.create_check_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_source_language"),
        "memory_content_translations",
        "source_language IN ('cs', 'ru')",
    )
    op.create_check_constraint(
        op.f("ck_memory_content_translations_memory_content_translations_target_language"),
        "memory_content_translations",
        "target_language IN ('cs', 'ru')",
    )

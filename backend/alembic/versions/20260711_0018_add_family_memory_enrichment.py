"""Add family memory enrichment workflow.

Revision ID: 20260711_0018
Revises: 20260711_0017
Create Date: 2026-07-11 18:30:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260711_0018"
down_revision = "20260711_0017"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("memory_type", sa.String(length=32), server_default=sa.text("'general'"), nullable=False),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("enrichment_status", sa.String(length=32), server_default=sa.text("'draft'"), nullable=False),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("finalized_memory_text", sa.String(length=500), nullable=True),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("privacy_scope", sa.String(length=32), server_default=sa.text("'private_owner'"), nullable=False),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("dispute_status", sa.String(length=32), server_default=sa.text("'none'"), nullable=False),
    )
    op.add_column("conversation_memory_candidates", sa.Column("finalized_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("conversation_memory_candidates", sa.Column("finalized_by", sa.String(length=120), nullable=True))
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("owner_reviewed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("owner_reviewed_by", sa.String(length=120), nullable=True),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("owner_review_actor_role", sa.String(length=32), nullable=True),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("review_authority_source", sa.String(length=32), nullable=True),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("unresolved_clarification_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("version", sa.Integer(), server_default=sa.text("1"), nullable=False),
    )
    op.add_column(
        "conversation_memory_candidates",
        sa.Column("workflow_version", sa.Integer(), server_default=sa.text("2"), nullable=False),
    )
    op.create_check_constraint(
        op.f("ck_conversation_memory_candidates_conversation_memory_candidates_memory_type"),
        "conversation_memory_candidates",
        "memory_type IN ('general', 'bedtime_song')",
    )
    op.create_check_constraint(
        op.f("ck_conversation_memory_candidates_conversation_memory_candidates_enrichment_status"),
        "conversation_memory_candidates",
        "enrichment_status IN ('draft', 'collecting_details', 'ready_for_owner_review')",
    )
    op.create_check_constraint(
        op.f("ck_conversation_memory_candidates_conversation_memory_candidates_privacy_scope"),
        "conversation_memory_candidates",
        "privacy_scope IN ('private_owner', 'selected_family', 'all_family', 'public_legacy')",
    )
    op.create_check_constraint(
        op.f("ck_conversation_memory_candidates_conversation_memory_candidates_dispute_status"),
        "conversation_memory_candidates",
        "dispute_status IN ('none', 'disputed', 'resolved')",
    )
    op.create_check_constraint(
        op.f("ck_conversation_memory_candidates_conversation_memory_candidates_unresolved_clarifications_non_negative"),
        "conversation_memory_candidates",
        "unresolved_clarification_count >= 0",
    )
    op.create_check_constraint(
        op.f("ck_conversation_memory_candidates_conversation_memory_candidates_version_positive"),
        "conversation_memory_candidates",
        "version >= 1",
    )
    op.create_check_constraint(
        op.f("ck_conversation_memory_candidates_conversation_memory_candidates_workflow_version"),
        "conversation_memory_candidates",
        "workflow_version IN (1, 2)",
    )

    # All rows predating this workflow are treated as finalized legacy candidates.
    # Approved rows keep compatibility with already-created/indexed promotions.
    op.execute("UPDATE conversation_memory_candidates SET workflow_version = 1")
    op.execute(
        "UPDATE conversation_memory_candidates c "
        "SET enrichment_status = 'ready_for_owner_review', "
        "finalized_memory_text = COALESCE((SELECT p.approved_memory_text FROM avatar_memory_promotions p WHERE p.candidate_id = c.id), c.proposed_memory_text), "
        "finalized_at = COALESCE(c.reviewed_at, c.updated_at), "
        "finalized_by = 'legacy-system', privacy_scope = 'public_legacy', "
        "unresolved_clarification_count = 0 "
        "WHERE c.status IN ('approved', 'rejected', 'archived') "
        "OR EXISTS (SELECT 1 FROM avatar_memory_promotions p WHERE p.candidate_id = c.id)"
    )
    op.execute(
        "UPDATE conversation_memory_candidates "
        "SET owner_reviewed_at = reviewed_at, "
        "owner_reviewed_by = CASE WHEN reviewed_by IS NULL THEN NULL ELSE CAST(reviewed_by AS VARCHAR) END, "
        "owner_review_actor_role = NULL, review_authority_source = 'legacy_backfill' "
        "WHERE status = 'approved'"
    )

    op.create_table(
        "family_memory_contributions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("candidate_id", sa.Integer(), nullable=False),
        sa.Column("avatar_id", sa.String(length=120), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=True),
        sa.Column("actor_id", sa.String(length=120), nullable=False),
        sa.Column("actor_user_id", sa.Integer(), nullable=True),
        sa.Column("actor_role", sa.String(length=32), nullable=False),
        sa.Column("relationship_to_owner", sa.String(length=120), nullable=True),
        sa.Column("contribution_type", sa.String(length=32), nullable=False),
        sa.Column("contribution_text", sa.String(length=1000), nullable=False),
        sa.Column("structured_details", sa.JSON(), nullable=True),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("source_message_hash", sa.String(length=64), nullable=True),
        sa.Column("trace_id", sa.String(length=120), nullable=True),
        sa.Column("supersedes_contribution_id", sa.Integer(), nullable=True),
        sa.Column("is_owner_correction", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("is_disputed", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("privacy_scope_snapshot", sa.String(length=32), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.CheckConstraint(
            "actor_role IN ('owner', 'contributor', 'trusted_reviewer', 'system')",
            name=op.f("ck_family_memory_contributions_family_memory_contributions_actor_role"),
        ),
        sa.CheckConstraint(
            "contribution_type IN ('initial_claim', 'clarification_answer', 'owner_correction', "
            "'owner_confirmation', 'reviewer_note', 'dispute_statement', 'system_normalization')",
            name=op.f("ck_family_memory_contributions_family_memory_contributions_type"),
        ),
        sa.CheckConstraint(
            "privacy_scope_snapshot IN ('private_owner', 'selected_family', 'all_family', 'public_legacy')",
            name=op.f("ck_family_memory_contributions_family_memory_contributions_privacy_scope"),
        ),
        sa.ForeignKeyConstraint(
            ["actor_user_id"], ["users.id"],
            name=op.f("fk_family_memory_contributions_actor_user_id_users"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["candidate_id"], ["conversation_memory_candidates.id"],
            name=op.f("fk_family_memory_contributions_candidate_id_conversation_memory_candidates"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"], ["memory_profiles.id"],
            name=op.f("fk_family_memory_contributions_profile_id_memory_profiles"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["supersedes_contribution_id"], ["family_memory_contributions.id"],
            name=op.f("fk_family_memory_contributions_supersedes_contribution_id_family_memory_contributions"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_family_memory_contributions")),
    )
    for column in ("candidate_id", "avatar_id", "profile_id", "actor_id", "actor_user_id", "actor_role", "contribution_type", "source_message_hash", "trace_id"):
        op.create_index(op.f(f"ix_family_memory_contributions_{column}"), "family_memory_contributions", [column], unique=False)
    op.create_index("ix_fmc_candidate_created", "family_memory_contributions", ["candidate_id", "created_at"], unique=False)
    op.execute(
        "CREATE FUNCTION prevent_family_memory_contribution_update() RETURNS trigger AS $$ "
        "BEGIN RAISE EXCEPTION 'family_memory_contributions are append-only'; END; "
        "$$ LANGUAGE plpgsql"
    )
    op.execute(
        "CREATE TRIGGER trg_family_memory_contributions_append_only "
        "BEFORE UPDATE ON family_memory_contributions "
        "FOR EACH ROW EXECUTE FUNCTION prevent_family_memory_contribution_update()"
    )

    op.create_table(
        "memory_clarification_questions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("candidate_id", sa.Integer(), nullable=False),
        sa.Column("question_key", sa.String(length=64), nullable=False),
        sa.Column("question_text", sa.String(length=500), nullable=False),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("status", sa.String(length=32), server_default=sa.text("'pending'"), nullable=False),
        sa.Column("required", sa.Boolean(), server_default=sa.text("true"), nullable=False),
        sa.Column("asked_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("answered_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("answered_by", sa.String(length=120), nullable=True),
        sa.Column("answer_contribution_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.CheckConstraint(
            "status IN ('pending', 'answered', 'skipped', 'cancelled')",
            name=op.f("ck_memory_clarification_questions_memory_clarification_questions_status"),
        ),
        sa.ForeignKeyConstraint(
            ["candidate_id"], ["conversation_memory_candidates.id"],
            name=op.f("fk_memory_clarification_questions_candidate_id_conversation_memory_candidates"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["answer_contribution_id"], ["family_memory_contributions.id"],
            name=op.f("fk_memory_clarification_questions_answer_contribution_id_family_memory_contributions"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_memory_clarification_questions")),
    )
    op.create_index(op.f("ix_memory_clarification_questions_candidate_id"), "memory_clarification_questions", ["candidate_id"], unique=False)
    op.create_index("ix_mcq_candidate_status", "memory_clarification_questions", ["candidate_id", "status"], unique=False)
    op.create_index("ix_mcq_candidate_question_key", "memory_clarification_questions", ["candidate_id", "question_key"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_mcq_candidate_question_key", table_name="memory_clarification_questions")
    op.drop_index("ix_mcq_candidate_status", table_name="memory_clarification_questions")
    op.drop_index(op.f("ix_memory_clarification_questions_candidate_id"), table_name="memory_clarification_questions")
    op.drop_table("memory_clarification_questions")
    op.execute(
        "DROP TRIGGER IF EXISTS trg_family_memory_contributions_append_only "
        "ON family_memory_contributions"
    )
    op.execute("DROP FUNCTION IF EXISTS prevent_family_memory_contribution_update()")
    op.drop_index("ix_fmc_candidate_created", table_name="family_memory_contributions")
    for column in reversed(("candidate_id", "avatar_id", "profile_id", "actor_id", "actor_user_id", "actor_role", "contribution_type", "source_message_hash", "trace_id")):
        op.drop_index(op.f(f"ix_family_memory_contributions_{column}"), table_name="family_memory_contributions")
    op.drop_table("family_memory_contributions")

    for name in (
        "conversation_memory_candidates_version_positive",
        "conversation_memory_candidates_workflow_version",
        "conversation_memory_candidates_unresolved_clarifications_non_negative",
        "conversation_memory_candidates_dispute_status",
        "conversation_memory_candidates_privacy_scope",
        "conversation_memory_candidates_enrichment_status",
        "conversation_memory_candidates_memory_type",
    ):
        op.drop_constraint(op.f(f"ck_conversation_memory_candidates_{name}"), "conversation_memory_candidates", type_="check")
    for column in (
        "version",
        "workflow_version",
        "unresolved_clarification_count",
        "owner_review_actor_role",
        "review_authority_source",
        "owner_reviewed_by",
        "owner_reviewed_at",
        "finalized_by",
        "finalized_at",
        "dispute_status",
        "privacy_scope",
        "finalized_memory_text",
        "enrichment_status",
        "memory_type",
    ):
        op.drop_column("conversation_memory_candidates", column)

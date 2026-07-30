"""Add provider usage cost foundation (ai_actions/ai_action_steps/ai_provider_attempts).

Task 66.1 - Provider Usage and Cost Foundation. Purely additive: creates
three new tables durably tracking every paid DeepSeek/OpenAI-compatible
provider attempt (ai_provider_attempts), the processing step it belongs to
(ai_action_steps), and the user-visible operation it belongs to (ai_actions).
No existing table is altered and no data is migrated. Autogenerate also
detected unrelated pre-existing unique-index/unique-constraint
representation drift on active_retrieval_configs/avatar_memory_promotions/
memorial_contribution_promotions/memorial_contributions/memorial_invitations
(out of scope for this task) - that drift is intentionally excluded from
this migration.

Revision ID: 20260721_0024
Revises: 20260721_0023
Create Date: 2026-07-21 14:51:21.424367

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260721_0024"
down_revision = "20260721_0023"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ai_actions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("trace_id", sa.String(length=64), nullable=False),
        sa.Column("feature", sa.String(length=64), nullable=False),
        sa.Column("status", sa.String(length=16), server_default=sa.text("'pending'"), nullable=False),
        sa.Column("execution_source", sa.String(length=16), nullable=False),
        sa.Column("requested_locale", sa.String(length=8), nullable=True),
        sa.Column("resolved_locale", sa.String(length=8), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("memorial_id", sa.Integer(), nullable=True),
        sa.Column("conversation_id", sa.Integer(), nullable=True),
        sa.Column("message_id", sa.Integer(), nullable=True),
        sa.Column("celery_task_id", sa.String(length=255), nullable=True),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("duration_ms", sa.Integer(), nullable=True),
        sa.Column("provider_call_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("retry_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("total_input_tokens", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("total_cached_input_tokens", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("total_output_tokens", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("total_reasoning_tokens", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("total_tokens", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column(
            "total_cost_usd",
            sa.Numeric(precision=18, scale=9),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column(
            "cached_input_savings_usd",
            sa.Numeric(precision=18, scale=9),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column(
            "monetary_cost_status",
            sa.String(length=16),
            server_default=sa.text("'not_applicable'"),
            nullable=False,
        ),
        sa.Column("error_category", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint(
            "execution_source IN ('fastapi', 'celery', 'internal', 'test')",
            name=op.f("ck_ai_actions_ai_actions_execution_source"),
        ),
        sa.CheckConstraint(
            "feature IN ('brain_chat_response', 'avatar_biographer_question', 'dynamic_memory_translation', "
            "'memory_candidate_finalization', 'memory_conflict_analysis', 'memory_summarization', "
            "'evaluation', 'development_test', 'other')",
            name=op.f("ck_ai_actions_ai_actions_feature"),
        ),
        sa.CheckConstraint(
            "monetary_cost_status IN ('not_applicable', 'calculated', 'partial', 'unknown')",
            name=op.f("ck_ai_actions_ai_actions_monetary_cost_status"),
        ),
        sa.CheckConstraint(
            "status IN ('pending', 'running', 'succeeded', 'failed', 'cancelled')",
            name=op.f("ck_ai_actions_ai_actions_status"),
        ),
        sa.CheckConstraint(
            "cached_input_savings_usd >= 0",
            name=op.f("ck_ai_actions_ai_actions_cached_input_savings_usd_non_negative"),
        ),
        sa.CheckConstraint(
            "provider_call_count >= 0", name=op.f("ck_ai_actions_ai_actions_provider_call_count_non_negative")
        ),
        sa.CheckConstraint(
            "retry_count >= 0", name=op.f("ck_ai_actions_ai_actions_retry_count_non_negative")
        ),
        sa.CheckConstraint(
            "total_cached_input_tokens >= 0",
            name=op.f("ck_ai_actions_ai_actions_total_cached_input_tokens_non_negative"),
        ),
        sa.CheckConstraint(
            "total_cost_usd >= 0", name=op.f("ck_ai_actions_ai_actions_total_cost_usd_non_negative")
        ),
        sa.CheckConstraint(
            "total_input_tokens >= 0", name=op.f("ck_ai_actions_ai_actions_total_input_tokens_non_negative")
        ),
        sa.CheckConstraint(
            "total_output_tokens >= 0", name=op.f("ck_ai_actions_ai_actions_total_output_tokens_non_negative")
        ),
        sa.CheckConstraint(
            "total_reasoning_tokens >= 0",
            name=op.f("ck_ai_actions_ai_actions_total_reasoning_tokens_non_negative"),
        ),
        sa.CheckConstraint(
            "total_tokens >= 0", name=op.f("ck_ai_actions_ai_actions_total_tokens_non_negative")
        ),
        sa.ForeignKeyConstraint(
            ["memorial_id"],
            ["memory_profiles.id"],
            name=op.f("fk_ai_actions_memorial_id_memory_profiles"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["message_id"],
            ["chat_messages.id"],
            name=op.f("fk_ai_actions_message_id_chat_messages"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_ai_actions_user_id_users"), ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ai_actions")),
    )
    op.create_index(op.f("ix_ai_actions_celery_task_id"), "ai_actions", ["celery_task_id"], unique=False)
    op.create_index("ix_ai_actions_created_at", "ai_actions", ["created_at"], unique=False)
    op.create_index(
        "ix_ai_actions_feature_created_at", "ai_actions", ["feature", "created_at"], unique=False
    )
    op.create_index(op.f("ix_ai_actions_memorial_id"), "ai_actions", ["memorial_id"], unique=False)
    op.create_index(
        "ix_ai_actions_memorial_id_created_at", "ai_actions", ["memorial_id", "created_at"], unique=False
    )
    op.create_index(op.f("ix_ai_actions_message_id"), "ai_actions", ["message_id"], unique=False)
    op.create_index(
        "ix_ai_actions_status_created_at", "ai_actions", ["status", "created_at"], unique=False
    )
    op.create_index("ix_ai_actions_trace_id", "ai_actions", ["trace_id"], unique=False)
    op.create_index(op.f("ix_ai_actions_user_id"), "ai_actions", ["user_id"], unique=False)
    op.create_index(
        "ix_ai_actions_user_id_created_at", "ai_actions", ["user_id", "created_at"], unique=False
    )

    op.create_table(
        "ai_action_steps",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("action_id", sa.Integer(), nullable=False),
        sa.Column("step_type", sa.String(length=64), nullable=False),
        sa.Column("sequence_number", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=16), server_default=sa.text("'pending'"), nullable=False),
        sa.Column("execution_source", sa.String(length=16), nullable=False),
        sa.Column(
            "cache_status", sa.String(length=16), server_default=sa.text("'not_applicable'"), nullable=False
        ),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("duration_ms", sa.Integer(), nullable=True),
        sa.Column("provider_call_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("retry_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("total_tokens", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column(
            "total_cost_usd",
            sa.Numeric(precision=18, scale=9),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column(
            "monetary_cost_status",
            sa.String(length=16),
            server_default=sa.text("'not_applicable'"),
            nullable=False,
        ),
        sa.Column("error_category", sa.String(length=64), nullable=True),
        sa.Column("idempotency_key", sa.String(length=128), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint(
            "cache_status IN ('not_applicable', 'hit', 'miss', 'partial', 'unknown')",
            name=op.f("ck_ai_action_steps_ai_action_steps_cache_status"),
        ),
        sa.CheckConstraint(
            "execution_source IN ('fastapi', 'celery', 'internal', 'test')",
            name=op.f("ck_ai_action_steps_ai_action_steps_execution_source"),
        ),
        sa.CheckConstraint(
            "monetary_cost_status IN ('not_applicable', 'calculated', 'partial', 'unknown')",
            name=op.f("ck_ai_action_steps_ai_action_steps_monetary_cost_status"),
        ),
        sa.CheckConstraint(
            "status IN ('pending', 'running', 'succeeded', 'failed', 'cancelled', 'skipped')",
            name=op.f("ck_ai_action_steps_ai_action_steps_status"),
        ),
        sa.CheckConstraint(
            "step_type IN ('provider_generation', 'provider_translation', 'provider_structured_output', "
            "'context_preparation', 'retrieval', 'deterministic_postprocessing', 'response_guard')",
            name=op.f("ck_ai_action_steps_ai_action_steps_step_type"),
        ),
        sa.CheckConstraint(
            "provider_call_count >= 0",
            name=op.f("ck_ai_action_steps_ai_action_steps_provider_call_count_non_negative"),
        ),
        sa.CheckConstraint(
            "retry_count >= 0", name=op.f("ck_ai_action_steps_ai_action_steps_retry_count_non_negative")
        ),
        sa.CheckConstraint(
            "sequence_number >= 1",
            name=op.f("ck_ai_action_steps_ai_action_steps_sequence_number_positive"),
        ),
        sa.CheckConstraint(
            "total_cost_usd >= 0", name=op.f("ck_ai_action_steps_ai_action_steps_total_cost_usd_non_negative")
        ),
        sa.CheckConstraint(
            "total_tokens >= 0", name=op.f("ck_ai_action_steps_ai_action_steps_total_tokens_non_negative")
        ),
        sa.ForeignKeyConstraint(
            ["action_id"],
            ["ai_actions.id"],
            name=op.f("fk_ai_action_steps_action_id_ai_actions"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ai_action_steps")),
        sa.UniqueConstraint(
            "action_id", "sequence_number", name="uq_ai_action_steps_action_id_sequence_number"
        ),
    )
    op.create_index("ix_ai_action_steps_action_id", "ai_action_steps", ["action_id"], unique=False)
    op.create_index(
        op.f("ix_ai_action_steps_idempotency_key"), "ai_action_steps", ["idempotency_key"], unique=False
    )

    op.create_table(
        "ai_provider_attempts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("action_id", sa.Integer(), nullable=False),
        sa.Column("step_id", sa.Integer(), nullable=False),
        sa.Column("provider_call_id", sa.String(length=64), nullable=False),
        sa.Column("provider", sa.String(length=32), nullable=False),
        sa.Column("model", sa.String(length=120), nullable=False),
        sa.Column("provider_request_id", sa.String(length=120), nullable=True),
        sa.Column("attempt_number", sa.Integer(), server_default=sa.text("1"), nullable=False),
        sa.Column("retry_reason", sa.String(length=64), nullable=True),
        sa.Column("status", sa.String(length=24), server_default=sa.text("'pending'"), nullable=False),
        sa.Column("success", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("request_started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("request_completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("latency_ms", sa.Integer(), nullable=True),
        sa.Column("input_tokens", sa.Integer(), nullable=True),
        sa.Column("cached_input_tokens", sa.Integer(), nullable=True),
        sa.Column("uncached_input_tokens", sa.Integer(), nullable=True),
        sa.Column("output_tokens", sa.Integer(), nullable=True),
        sa.Column("reasoning_tokens", sa.Integer(), nullable=True),
        sa.Column("total_tokens", sa.Integer(), nullable=True),
        sa.Column("uncached_input_cost_usd", sa.Numeric(precision=18, scale=9), nullable=True),
        sa.Column("cached_input_cost_usd", sa.Numeric(precision=18, scale=9), nullable=True),
        sa.Column("output_cost_usd", sa.Numeric(precision=18, scale=9), nullable=True),
        sa.Column("reasoning_cost_usd", sa.Numeric(precision=18, scale=9), nullable=True),
        sa.Column("total_cost_usd", sa.Numeric(precision=18, scale=9), nullable=True),
        sa.Column("cached_input_savings_usd", sa.Numeric(precision=18, scale=9), nullable=True),
        sa.Column(
            "monetary_cost_status",
            sa.String(length=16),
            server_default=sa.text("'not_applicable'"),
            nullable=False,
        ),
        sa.Column("pricing_version", sa.String(length=64), nullable=True),
        sa.Column("http_status", sa.Integer(), nullable=True),
        sa.Column("error_category", sa.String(length=64), nullable=True),
        sa.Column("raw_usage_redacted", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint(
            "monetary_cost_status IN ('not_applicable', 'calculated', 'partial', 'unknown')",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_monetary_cost_status"),
        ),
        sa.CheckConstraint(
            "status IN ('pending', 'succeeded', 'timeout', 'rate_limited', 'http_error', 'invalid_response', "
            "'empty_response', 'cancelled', 'audit_error', 'internal_error')",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_status"),
        ),
        sa.CheckConstraint(
            "attempt_number >= 1",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_attempt_number_positive"),
        ),
        sa.CheckConstraint(
            "cached_input_tokens IS NULL OR cached_input_tokens >= 0",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_cached_input_tokens_non_negative"),
        ),
        sa.CheckConstraint(
            "input_tokens IS NULL OR input_tokens >= 0",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_input_tokens_non_negative"),
        ),
        sa.CheckConstraint(
            "output_tokens IS NULL OR output_tokens >= 0",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_output_tokens_non_negative"),
        ),
        sa.CheckConstraint(
            "reasoning_tokens IS NULL OR reasoning_tokens >= 0",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_reasoning_tokens_non_negative"),
        ),
        sa.CheckConstraint(
            "total_tokens IS NULL OR total_tokens >= 0",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_total_tokens_non_negative"),
        ),
        sa.CheckConstraint(
            "uncached_input_tokens IS NULL OR uncached_input_tokens >= 0",
            name=op.f("ck_ai_provider_attempts_ai_provider_attempts_uncached_input_tokens_non_negative"),
        ),
        sa.ForeignKeyConstraint(
            ["action_id"],
            ["ai_actions.id"],
            name=op.f("fk_ai_provider_attempts_action_id_ai_actions"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["step_id"],
            ["ai_action_steps.id"],
            name=op.f("fk_ai_provider_attempts_step_id_ai_action_steps"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ai_provider_attempts")),
        sa.UniqueConstraint("provider_call_id", name="uq_ai_provider_attempts_provider_call_id"),
        sa.UniqueConstraint(
            "step_id", "attempt_number", name="uq_ai_provider_attempts_step_id_attempt_number"
        ),
    )
    op.create_index(
        op.f("ix_ai_provider_attempts_action_id"), "ai_provider_attempts", ["action_id"], unique=False
    )
    op.create_index(
        "ix_ai_provider_attempts_provider_model_created_at",
        "ai_provider_attempts",
        ["provider", "model", "created_at"],
        unique=False,
    )
    op.create_index(
        "ix_ai_provider_attempts_status_created_at",
        "ai_provider_attempts",
        ["status", "created_at"],
        unique=False,
    )
    op.create_index(
        "ix_ai_provider_attempts_step_id", "ai_provider_attempts", ["step_id"], unique=False
    )


def downgrade() -> None:
    op.drop_index("ix_ai_provider_attempts_step_id", table_name="ai_provider_attempts")
    op.drop_index("ix_ai_provider_attempts_status_created_at", table_name="ai_provider_attempts")
    op.drop_index("ix_ai_provider_attempts_provider_model_created_at", table_name="ai_provider_attempts")
    op.drop_index(op.f("ix_ai_provider_attempts_action_id"), table_name="ai_provider_attempts")
    op.drop_table("ai_provider_attempts")

    op.drop_index(op.f("ix_ai_action_steps_idempotency_key"), table_name="ai_action_steps")
    op.drop_index("ix_ai_action_steps_action_id", table_name="ai_action_steps")
    op.drop_table("ai_action_steps")

    op.drop_index("ix_ai_actions_user_id_created_at", table_name="ai_actions")
    op.drop_index(op.f("ix_ai_actions_user_id"), table_name="ai_actions")
    op.drop_index("ix_ai_actions_trace_id", table_name="ai_actions")
    op.drop_index("ix_ai_actions_status_created_at", table_name="ai_actions")
    op.drop_index(op.f("ix_ai_actions_message_id"), table_name="ai_actions")
    op.drop_index("ix_ai_actions_memorial_id_created_at", table_name="ai_actions")
    op.drop_index(op.f("ix_ai_actions_memorial_id"), table_name="ai_actions")
    op.drop_index("ix_ai_actions_feature_created_at", table_name="ai_actions")
    op.drop_index("ix_ai_actions_created_at", table_name="ai_actions")
    op.drop_index(op.f("ix_ai_actions_celery_task_id"), table_name="ai_actions")
    op.drop_table("ai_actions")

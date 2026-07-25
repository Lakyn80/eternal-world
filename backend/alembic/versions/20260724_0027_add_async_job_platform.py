"""Add async job platform fields and transactional outbox.

Task 65.9 - Scalable Asynchronous Job Platform, Dedicated Embedding
Workers, Self-Healing Provider Recovery, and 100k-User Readiness
Foundation.

Purely additive to `background_jobs` (no existing column is dropped,
renamed, or narrowed) plus one new `job_outbox_events` table implementing
the transactional-outbox pattern (Part E). The existing `status` values
(`queued`, `running`, `succeeded`, `failed`, `cancelled`) keep their exact
prior meaning; `running` continues to mean "a worker is actively
processing this job" (the spec's "processing" state) - it is not renamed,
to avoid a repository-wide rename across every module that already reads
`background_jobs.status == "running"`. Three new values are ADDED to the
allowed set: `pending` (created but not yet durably queued via the
outbox), `retry_scheduled` (bounded infra-failure backoff), and
`recovery_pending` (bounded provider self-healing in progress, Part M).

Revision ID: 20260724_0027
Revises: 20260723_0026
Create Date: 2026-07-24 09:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260724_0027"
down_revision = "20260723_0026"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "background_jobs",
        sa.Column("queue", sa.String(length=32), nullable=True),
    )
    op.add_column(
        "background_jobs",
        sa.Column("idempotency_key", sa.String(length=255), nullable=True),
    )
    op.add_column(
        "background_jobs",
        sa.Column("priority", sa.Integer(), server_default=sa.text("0"), nullable=False),
    )
    op.add_column(
        "background_jobs",
        sa.Column("attempt_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
    )
    op.add_column(
        "background_jobs",
        sa.Column("max_attempts", sa.Integer(), server_default=sa.text("3"), nullable=False),
    )
    op.add_column(
        "background_jobs",
        sa.Column("provider_recovery_count", sa.Integer(), server_default=sa.text("0"), nullable=False),
    )
    op.add_column(
        "background_jobs",
        sa.Column(
            "fresh_process_retry_used",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )
    op.add_column(
        "background_jobs",
        sa.Column(
            "worker_recycle_requested",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )
    op.add_column(
        "background_jobs",
        sa.Column("queued_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "background_jobs",
        sa.Column("heartbeat_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "background_jobs",
        sa.Column("next_attempt_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "background_jobs",
        sa.Column("safe_error_category", sa.String(length=64), nullable=True),
    )
    op.add_column(
        "background_jobs",
        sa.Column("internal_correlation_id", sa.String(length=36), nullable=True),
    )
    op.add_column(
        "background_jobs",
        sa.Column(
            "payload_schema_version",
            sa.Integer(),
            server_default=sa.text("1"),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_background_jobs_queue_status",
        "background_jobs",
        ["queue", "status"],
        unique=False,
    )
    op.create_index(
        "ix_background_jobs_status_next_attempt_at",
        "background_jobs",
        ["status", "next_attempt_at"],
        unique=False,
    )
    op.create_index(
        "ix_background_jobs_status_heartbeat_at",
        "background_jobs",
        ["status", "heartbeat_at"],
        unique=False,
    )
    #: Partial unique index - see the matching comment on the
    #: `BackgroundJob` model in `app/db/models.py` for the full rationale.
    op.create_index(
        "uq_background_jobs_idempotency_key",
        "background_jobs",
        ["idempotency_key"],
        unique=True,
        postgresql_where=sa.text("status NOT IN ('succeeded', 'failed', 'cancelled')"),
    )

    op.drop_constraint(
        "background_jobs_status",
        "background_jobs",
        type_="check",
    )
    op.create_check_constraint(
        "background_jobs_status",
        "background_jobs",
        (
            "status IN ("
            "'pending', 'queued', 'running', 'retry_scheduled', "
            "'recovery_pending', 'succeeded', 'failed', 'cancelled'"
            ")"
        ),
    )

    op.create_table(
        "job_outbox_events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("job_id", sa.Integer(), nullable=False),
        sa.Column("task_name", sa.String(length=255), nullable=False),
        sa.Column("queue", sa.String(length=32), nullable=False),
        sa.Column("task_args", sa.JSON(), nullable=False),
        sa.Column(
            "status",
            sa.String(length=16),
            server_default=sa.text("'pending'"),
            nullable=False,
        ),
        sa.Column("attempts", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("last_error", sa.String(length=255), nullable=True),
        sa.Column("next_attempt_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
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
            "status IN ('pending', 'published', 'abandoned')",
            name=op.f("ck_job_outbox_events_job_outbox_events_status"),
        ),
        sa.ForeignKeyConstraint(
            ["job_id"],
            ["background_jobs.id"],
            name=op.f("fk_job_outbox_events_job_id_background_jobs"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_job_outbox_events")),
        sa.UniqueConstraint("job_id", name=op.f("uq_job_outbox_events_job_id")),
    )
    op.create_index(
        "ix_job_outbox_events_status_created_at",
        "job_outbox_events",
        ["status", "created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_job_outbox_events_job_id"),
        "job_outbox_events",
        ["job_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_job_outbox_events_job_id", table_name="job_outbox_events")
    op.drop_index("ix_job_outbox_events_status_created_at", table_name="job_outbox_events")
    op.drop_table("job_outbox_events")

    op.drop_constraint(
        "background_jobs_status",
        "background_jobs",
        type_="check",
    )
    op.create_check_constraint(
        "background_jobs_status",
        "background_jobs",
        "status IN ('queued', 'running', 'succeeded', 'failed', 'cancelled')",
    )

    op.drop_index("uq_background_jobs_idempotency_key", table_name="background_jobs")
    op.drop_index("ix_background_jobs_status_heartbeat_at", table_name="background_jobs")
    op.drop_index("ix_background_jobs_status_next_attempt_at", table_name="background_jobs")
    op.drop_index("ix_background_jobs_queue_status", table_name="background_jobs")

    op.drop_column("background_jobs", "payload_schema_version")
    op.drop_column("background_jobs", "internal_correlation_id")
    op.drop_column("background_jobs", "safe_error_category")
    op.drop_column("background_jobs", "next_attempt_at")
    op.drop_column("background_jobs", "heartbeat_at")
    op.drop_column("background_jobs", "queued_at")
    op.drop_column("background_jobs", "worker_recycle_requested")
    op.drop_column("background_jobs", "fresh_process_retry_used")
    op.drop_column("background_jobs", "provider_recovery_count")
    op.drop_column("background_jobs", "max_attempts")
    op.drop_column("background_jobs", "attempt_count")
    op.drop_column("background_jobs", "priority")
    op.drop_column("background_jobs", "idempotency_key")
    op.drop_column("background_jobs", "queue")

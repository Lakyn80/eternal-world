from __future__ import annotations

import uuid
from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.db.models import AiAction, AiActionStep, AiProviderAttempt
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import (
    AiActionStatus,
    AiStepStatus,
    AiStepType,
    CacheStatus,
    ExecutionSource,
    MonetaryCostStatus,
    ProviderAttemptStatus,
)
from app.modules.provider_usage.usage import NormalizedProviderUsage


def _monetary_status_value(status: MonetaryCostStatus | str) -> str:
    return status.value if isinstance(status, MonetaryCostStatus) else str(status)


def _aggregate_monetary_status(statuses: list[str]) -> MonetaryCostStatus:
    """Worst-case aggregation across a set of attempt/step statuses: a
    single UNKNOWN component makes the parent at least PARTIAL (or UNKNOWN
    if nothing at all is known); a single PARTIAL makes the parent PARTIAL;
    otherwise CALCULATED wins over NOT_APPLICABLE."""

    present = set(statuses)
    if not present:
        return MonetaryCostStatus.NOT_APPLICABLE
    if MonetaryCostStatus.UNKNOWN.value in present:
        if MonetaryCostStatus.CALCULATED.value in present or MonetaryCostStatus.PARTIAL.value in present:
            return MonetaryCostStatus.PARTIAL
        return MonetaryCostStatus.UNKNOWN
    if MonetaryCostStatus.PARTIAL.value in present:
        return MonetaryCostStatus.PARTIAL
    if MonetaryCostStatus.CALCULATED.value in present:
        return MonetaryCostStatus.CALCULATED
    return MonetaryCostStatus.NOT_APPLICABLE


def create_action(db: Session, *, context: AiCallContext) -> AiAction:
    action = AiAction(
        trace_id=context.trace_id or uuid.uuid4().hex,
        feature=context.feature.value,
        status=AiActionStatus.RUNNING.value,
        execution_source=context.execution_source.value,
        requested_locale=context.requested_locale,
        resolved_locale=context.resolved_locale,
        user_id=context.user_id,
        memorial_id=context.memorial_id,
        conversation_id=context.conversation_id,
        message_id=context.message_id,
        celery_task_id=context.celery_task_id,
        started_at=datetime.now(timezone.utc),
    )
    db.add(action)
    db.flush()
    return action


def create_step(
    db: Session,
    *,
    action: AiAction,
    step_type: AiStepType,
    sequence_number: int,
    execution_source: ExecutionSource,
    cache_status: CacheStatus = CacheStatus.NOT_APPLICABLE,
    idempotency_key: str | None = None,
) -> AiActionStep:
    existing = db.execute(
        select(AiActionStep).where(
            AiActionStep.action_id == action.id,
            AiActionStep.sequence_number == sequence_number,
        )
    ).scalar_one_or_none()
    if existing is not None:
        return existing

    step = AiActionStep(
        action_id=action.id,
        step_type=step_type.value,
        sequence_number=sequence_number,
        status=AiStepStatus.RUNNING.value,
        execution_source=execution_source.value,
        cache_status=cache_status.value,
        started_at=datetime.now(timezone.utc),
        idempotency_key=idempotency_key,
    )
    db.add(step)
    db.flush()
    return step


def get_or_create_pending_attempt(
    db: Session,
    *,
    action: AiAction,
    step: AiActionStep,
    attempt_number: int,
    provider: str,
    model: str,
    retry_reason: str | None = None,
) -> tuple[AiProviderAttempt, bool]:
    """Returns ``(attempt, is_newly_created)``. If a row already exists for
    ``(step_id, attempt_number)`` - e.g. a Celery task redelivery re-running
    the exact same logical attempt - the existing row is returned instead of
    inserting a duplicate, so a caller can detect an already-terminal
    attempt and skip re-calling the provider entirely."""

    existing = db.execute(
        select(AiProviderAttempt).where(
            AiProviderAttempt.step_id == step.id,
            AiProviderAttempt.attempt_number == attempt_number,
        )
    ).scalar_one_or_none()
    if existing is not None:
        return existing, False

    attempt = AiProviderAttempt(
        action_id=action.id,
        step_id=step.id,
        provider_call_id=uuid.uuid4().hex,
        provider=provider,
        model=model,
        attempt_number=attempt_number,
        retry_reason=retry_reason,
        status=ProviderAttemptStatus.PENDING.value,
        success=False,
        request_started_at=datetime.now(timezone.utc),
    )
    db.add(attempt)
    db.flush()
    return attempt, True


def finalize_attempt_success(
    db: Session,
    attempt: AiProviderAttempt,
    *,
    normalized_usage: NormalizedProviderUsage,
    latency_ms: int,
    http_status: int | None = None,
) -> AiProviderAttempt:
    attempt.status = ProviderAttemptStatus.SUCCEEDED.value
    attempt.success = True
    attempt.request_completed_at = datetime.now(timezone.utc)
    attempt.latency_ms = latency_ms
    attempt.http_status = http_status
    attempt.provider_request_id = normalized_usage.provider_request_id
    attempt.input_tokens = normalized_usage.input_tokens
    attempt.cached_input_tokens = normalized_usage.cached_input_tokens
    attempt.uncached_input_tokens = normalized_usage.uncached_input_tokens
    attempt.output_tokens = normalized_usage.output_tokens
    attempt.reasoning_tokens = normalized_usage.reasoning_tokens
    attempt.total_tokens = normalized_usage.total_tokens
    attempt.uncached_input_cost_usd = normalized_usage.uncached_input_cost_usd
    attempt.cached_input_cost_usd = normalized_usage.cached_input_cost_usd
    attempt.output_cost_usd = normalized_usage.output_cost_usd
    attempt.reasoning_cost_usd = normalized_usage.reasoning_cost_usd
    attempt.total_cost_usd = normalized_usage.total_cost_usd
    attempt.cached_input_savings_usd = normalized_usage.cached_input_savings_usd
    attempt.monetary_cost_status = normalized_usage.monetary_cost_status.value
    attempt.pricing_version = normalized_usage.pricing_version
    attempt.raw_usage_redacted = normalized_usage.raw_usage_redacted
    db.flush()
    return attempt


def finalize_attempt_failure(
    db: Session,
    attempt: AiProviderAttempt,
    *,
    status: ProviderAttemptStatus,
    error_category: str | None,
    http_status: int | None = None,
    latency_ms: int | None = None,
) -> AiProviderAttempt:
    attempt.status = status.value
    attempt.success = False
    attempt.request_completed_at = datetime.now(timezone.utc)
    attempt.latency_ms = latency_ms
    attempt.http_status = http_status
    attempt.error_category = error_category
    attempt.monetary_cost_status = MonetaryCostStatus.NOT_APPLICABLE.value
    db.flush()
    return attempt


def recompute_step_totals(db: Session, step: AiActionStep) -> AiActionStep:
    """Idempotent recompute of ``step``'s totals from its
    ``AiProviderAttempt`` rows. Safe to call repeatedly (e.g. after a Celery
    redelivery re-finalizes the same step) - it always derives the totals
    fresh from the durable attempt rows rather than incrementing counters,
    so repeated finalization can never double-count."""

    attempts = (
        db.execute(select(AiProviderAttempt).where(AiProviderAttempt.step_id == step.id))
        .scalars()
        .all()
    )

    step.provider_call_count = len(attempts)
    step.retry_count = max(0, len(attempts) - 1)
    step.total_tokens = sum((a.total_tokens or 0) for a in attempts)
    step.total_cost_usd = sum((a.total_cost_usd or Decimal("0")) for a in attempts) or Decimal("0")
    step.monetary_cost_status = _aggregate_monetary_status(
        [a.monetary_cost_status for a in attempts]
    ).value

    if attempts and any(a.status == ProviderAttemptStatus.SUCCEEDED.value for a in attempts):
        step.status = AiStepStatus.SUCCEEDED.value
    elif attempts and all(
        a.status not in (ProviderAttemptStatus.PENDING.value, ProviderAttemptStatus.SUCCEEDED.value)
        for a in attempts
    ):
        step.status = AiStepStatus.FAILED.value
        failed_attempt = next((a for a in reversed(attempts) if a.error_category), None)
        step.error_category = failed_attempt.error_category if failed_attempt else step.error_category

    step.completed_at = datetime.now(timezone.utc)
    if step.started_at is not None:
        step.duration_ms = int((step.completed_at - step.started_at).total_seconds() * 1000)
    db.flush()
    return step


def recompute_action_totals(db: Session, action: AiAction) -> AiAction:
    """Idempotent recompute of ``action``'s totals from its
    ``AiProviderAttempt`` rows (not from steps, so it stays correct even if
    a step's own recompute has not run yet)."""

    attempts = (
        db.execute(select(AiProviderAttempt).where(AiProviderAttempt.action_id == action.id))
        .scalars()
        .all()
    )

    action.provider_call_count = len(attempts)
    action.retry_count = max(0, len(attempts) - 1)
    action.total_input_tokens = sum((a.input_tokens or 0) for a in attempts)
    action.total_cached_input_tokens = sum((a.cached_input_tokens or 0) for a in attempts)
    action.total_output_tokens = sum((a.output_tokens or 0) for a in attempts)
    action.total_reasoning_tokens = sum((a.reasoning_tokens or 0) for a in attempts)
    action.total_tokens = sum((a.total_tokens or 0) for a in attempts)
    action.total_cost_usd = sum((a.total_cost_usd or Decimal("0")) for a in attempts) or Decimal("0")
    action.cached_input_savings_usd = sum(
        (a.cached_input_savings_usd or Decimal("0")) for a in attempts
    ) or Decimal("0")
    action.monetary_cost_status = _aggregate_monetary_status(
        [a.monetary_cost_status for a in attempts]
    ).value
    db.flush()
    return action


def finalize_action(
    db: Session,
    action: AiAction,
    *,
    status: AiActionStatus,
    error_category: str | None = None,
) -> AiAction:
    recompute_action_totals(db, action)
    action.status = status.value
    action.error_category = error_category
    action.completed_at = datetime.now(timezone.utc)
    if action.started_at is not None:
        action.duration_ms = int((action.completed_at - action.started_at).total_seconds() * 1000)
    db.flush()
    return action


def get_action_with_details(db: Session, *, action_id: int) -> AiAction | None:
    return db.execute(
        select(AiAction)
        .where(AiAction.id == action_id)
        .options(
            selectinload(AiAction.steps).selectinload(AiActionStep.provider_attempts),
        )
    ).scalar_one_or_none()

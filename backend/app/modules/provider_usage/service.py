from __future__ import annotations

import logging
from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import (
    observe_ai_action_completed,
    observe_ai_audit_failure,
    observe_ai_provider_attempt,
    observe_ai_retry,
    observe_ai_translation_cache,
)
from app.db.models import AiAction, AiActionStep
from app.modules.provider_usage import repository
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import (
    AiActionStatus,
    AiErrorCategory,
    AiStepType,
    CacheStatus,
    ProviderAttemptStatus,
)
from app.modules.provider_usage.usage import (
    NormalizedTokenUsage,
    calculate_provider_usage_cost,
)


logger = get_logger("provider_usage")


class AuditPersistenceError(RuntimeError):
    """Raised when a durable ``AiAction``/``AiActionStep``/``AiProviderAttempt``
    row could not be created *before* the paid provider would have been
    called. Fail-closed: whenever this is raised, the paid provider call
    must never happen."""


class AuditFinalizationError(RuntimeError):
    """Raised when the paid provider call itself succeeded but persisting
    its usage/cost afterward failed. The pre-created pending attempt row is
    left in place (not deleted, not marked succeeded) so it remains visible
    for later reconciliation - this is never converted into a silent
    success."""


@dataclass(frozen=True)
class ProviderCallResult:
    response: Any
    normalized_usage: Any


def _classify_provider_exception(exc: Exception) -> tuple[ProviderAttemptStatus, str]:
    """Generic, class-name-based classification that works for any
    provider's hand-rolled exception hierarchy without importing
    provider-specific modules (avoids a circular import between this shared
    module and ``ai_agents``/``content_translation``). Both existing
    provider implementations already name their exceptions
    ``...RequestError``/``...ResponseError``, which this relies on."""

    name = exc.__class__.__name__
    message = str(exc).lower()
    if "timeout" in name.lower() or "timed out" in message:
        return ProviderAttemptStatus.TIMEOUT, AiErrorCategory.PROVIDER_TIMEOUT.value
    if "rate" in message and "limit" in message:
        return ProviderAttemptStatus.RATE_LIMITED, AiErrorCategory.PROVIDER_RATE_LIMITED.value
    if name.endswith("ValidationError"):
        return ProviderAttemptStatus.INVALID_RESPONSE, AiErrorCategory.VALIDATION_ERROR.value
    if name.endswith("RequestError"):
        return ProviderAttemptStatus.HTTP_ERROR, AiErrorCategory.PROVIDER_HTTP_ERROR.value
    if name.endswith("ResponseError"):
        return ProviderAttemptStatus.INVALID_RESPONSE, AiErrorCategory.PROVIDER_INVALID_RESPONSE.value
    return ProviderAttemptStatus.INTERNAL_ERROR, AiErrorCategory.INTERNAL_ERROR.value


def execute_paid_provider_call(
    db: Session,
    *,
    action: AiAction,
    step: AiActionStep,
    provider: str,
    model: str,
    attempt_number: int,
    operation: Callable[[], Any],
    extract_token_usage: Callable[[Any], NormalizedTokenUsage],
    retry_reason: str | None = None,
) -> ProviderCallResult:
    """The one shared instrumentation wrapper every paid provider call must
    go through. ``action``/``step`` must already be durably persisted
    (created via ``repository.create_action``/``create_step`` and
    committed) before this is called.

    Sequence: (1) durably persist a pending attempt row *before* touching
    the network - if that fails, raise ``AuditPersistenceError`` and never
    call ``operation`` (fail-closed); (2) call ``operation``; (3) on
    failure, classify and persist the failed attempt, then re-raise the
    original exception unchanged; (4) on success, normalize usage, price it,
    persist success, and recompute step totals - if persistence fails here,
    raise ``AuditFinalizationError`` rather than returning a silent success.
    """

    try:
        attempt, is_new = repository.get_or_create_pending_attempt(
            db,
            action=action,
            step=step,
            attempt_number=attempt_number,
            provider=provider,
            model=model,
            retry_reason=retry_reason,
        )
        db.commit()
    except Exception as exc:
        db.rollback()
        log_event(
            logger,
            logging.ERROR,
            "ai_audit_initialization_failed",
            action_id=action.id,
            step_id=step.id,
            trace_id=action.trace_id,
            feature=action.feature,
            attempt_number=attempt_number,
        )
        observe_ai_audit_failure(stage="pre_call", feature=action.feature)
        raise AuditPersistenceError(
            "Failed to durably record a pending provider attempt before the call"
        ) from exc

    if not is_new and attempt.status != ProviderAttemptStatus.PENDING.value:
        # A prior run (e.g. a Celery redelivery) already completed this exact
        # logical attempt - never call the provider again for it.
        log_event(
            logger,
            logging.INFO,
            "ai_provider_attempt_already_finalized",
            action_id=action.id,
            step_id=step.id,
            attempt_number=attempt_number,
            status=attempt.status,
        )
        return ProviderCallResult(response=None, normalized_usage=None)

    log_event(
        logger,
        logging.INFO,
        "ai_provider_attempt_started",
        action_id=action.id,
        step_id=step.id,
        trace_id=action.trace_id,
        feature=action.feature,
        provider=provider,
        model=model,
        attempt_number=attempt_number,
    )
    if attempt_number > 1:
        observe_ai_retry(provider=provider, model=model, feature=action.feature, reason=retry_reason)

    started_at = perf_counter()
    try:
        response = operation()
    except Exception as exc:
        latency_ms = int((perf_counter() - started_at) * 1000)
        status, error_category = _classify_provider_exception(exc)
        try:
            repository.finalize_attempt_failure(
                db,
                attempt,
                status=status,
                error_category=error_category,
                latency_ms=latency_ms,
            )
            repository.recompute_step_totals(db, step)
            db.commit()
        except Exception:
            db.rollback()
            log_event(
                logger,
                logging.ERROR,
                "ai_audit_finalization_failed",
                action_id=action.id,
                step_id=step.id,
                attempt_number=attempt_number,
                stage="failure_path",
            )
            observe_ai_audit_failure(stage="post_call_failure", feature=action.feature)
        log_event(
            logger,
            logging.WARNING,
            "ai_provider_attempt_failed",
            action_id=action.id,
            step_id=step.id,
            trace_id=action.trace_id,
            feature=action.feature,
            provider=provider,
            model=model,
            attempt_number=attempt_number,
            status=status.value,
            error_category=error_category,
            latency_ms=latency_ms,
        )
        observe_ai_provider_attempt(
            provider=provider,
            model=model,
            feature=action.feature,
            status=status.value,
            latency_seconds=latency_ms / 1000,
        )
        raise

    latency_ms = int((perf_counter() - started_at) * 1000)
    try:
        token_usage = extract_token_usage(response)
        normalized_usage = calculate_provider_usage_cost(
            provider=provider, model=model, token_usage=token_usage
        )
        repository.finalize_attempt_success(
            db,
            attempt,
            normalized_usage=normalized_usage,
            latency_ms=latency_ms,
        )
        repository.recompute_step_totals(db, step)
        db.commit()
    except Exception as exc:
        db.rollback()
        log_event(
            logger,
            logging.ERROR,
            "ai_audit_finalization_failed",
            action_id=action.id,
            step_id=step.id,
            attempt_number=attempt_number,
            stage="success_path",
        )
        observe_ai_audit_failure(stage="post_call_success", feature=action.feature)
        raise AuditFinalizationError(
            "Provider call succeeded but usage/cost persistence failed"
        ) from exc

    log_event(
        logger,
        logging.INFO,
        "ai_provider_attempt_succeeded",
        action_id=action.id,
        step_id=step.id,
        trace_id=action.trace_id,
        feature=action.feature,
        provider=provider,
        model=model,
        attempt_number=attempt_number,
        input_tokens=normalized_usage.input_tokens,
        cached_input_tokens=normalized_usage.cached_input_tokens,
        output_tokens=normalized_usage.output_tokens,
        reasoning_tokens=normalized_usage.reasoning_tokens,
        total_cost_usd=str(normalized_usage.total_cost_usd) if normalized_usage.total_cost_usd is not None else None,
        monetary_cost_status=normalized_usage.monetary_cost_status.value,
        pricing_version=normalized_usage.pricing_version,
        latency_ms=latency_ms,
    )
    observe_ai_provider_attempt(
        provider=provider,
        model=model,
        feature=action.feature,
        status=ProviderAttemptStatus.SUCCEEDED.value,
        latency_seconds=latency_ms / 1000,
        token_usage=normalized_usage,
    )
    return ProviderCallResult(response=response, normalized_usage=normalized_usage)


def run_instrumented_single_attempt_action(
    db: Session,
    *,
    context: AiCallContext,
    step_type: AiStepType,
    provider: str,
    model: str,
    operation: Callable[[], Any],
    extract_token_usage: Callable[[Any], NormalizedTokenUsage],
) -> tuple[Any, AiAction]:
    """The single reusable entry point for "one action, one step, one
    provider attempt" operations (a Chat message, one dynamic translation
    call) - the shape shared by every current real paid-call site. Creates
    the action/step, runs ``operation`` through ``execute_paid_provider_call``,
    finalizes the action's totals, and returns ``(operation_result, action)``
    so the caller can attach ``action.id`` to dev-mode response metadata.

    Raises whatever ``operation`` raises (after recording the failed
    attempt), or ``AuditPersistenceError``/``AuditFinalizationError`` if the
    durable audit trail itself could not be written - never silently
    swallows either.
    """

    action = repository.create_action(db, context=context)
    db.commit()
    step = repository.create_step(
        db,
        action=action,
        step_type=step_type,
        sequence_number=1,
        execution_source=context.execution_source,
        cache_status=CacheStatus.NOT_APPLICABLE,
    )
    db.commit()

    log_event(
        logger,
        logging.INFO,
        "ai_action_started",
        action_id=action.id,
        trace_id=action.trace_id,
        feature=action.feature,
        execution_source=action.execution_source,
        requested_locale=action.requested_locale,
    )
    log_event(
        logger,
        logging.INFO,
        "ai_step_started",
        action_id=action.id,
        step_id=step.id,
        step_type=step.step_type,
    )

    try:
        result = execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider=provider,
            model=model,
            attempt_number=1,
            operation=operation,
            extract_token_usage=extract_token_usage,
        )
    except (AuditPersistenceError, AuditFinalizationError):
        _try_finalize_action_failed(db, action, error_category=AiErrorCategory.AUDIT_PERSISTENCE_ERROR.value)
        raise
    except Exception as exc:
        _, error_category = _classify_provider_exception(exc)
        _try_finalize_action_failed(db, action, error_category=error_category)
        raise

    try:
        repository.finalize_action(db, action, status=AiActionStatus.SUCCEEDED)
        db.commit()
    except Exception as exc:
        db.rollback()
        log_event(
            logger,
            logging.ERROR,
            "ai_audit_finalization_failed",
            action_id=action.id,
            stage="action_finalize",
        )
        observe_ai_audit_failure(stage="action_finalize", feature=action.feature)
        raise AuditFinalizationError("Action succeeded but final totals could not be persisted") from exc

    log_event(
        logger,
        logging.INFO,
        "ai_step_completed",
        action_id=action.id,
        step_id=step.id,
        status=step.status,
        total_tokens=step.total_tokens,
        total_cost_usd=str(step.total_cost_usd),
    )
    log_event(
        logger,
        logging.INFO,
        "ai_action_completed",
        action_id=action.id,
        trace_id=action.trace_id,
        feature=action.feature,
        status=action.status,
        provider_call_count=action.provider_call_count,
        total_tokens=action.total_tokens,
        total_cost_usd=str(action.total_cost_usd),
        monetary_cost_status=action.monetary_cost_status,
    )
    observe_ai_action_completed(
        feature=action.feature,
        status=action.status,
        execution_source=action.execution_source,
        duration_seconds=(action.duration_ms or 0) / 1000,
    )
    return result.response, action


def _try_finalize_action_failed(db: Session, action: AiAction, *, error_category: str) -> None:
    try:
        repository.finalize_action(db, action, status=AiActionStatus.FAILED, error_category=error_category)
        db.commit()
    except Exception:
        db.rollback()
        log_event(
            logger,
            logging.ERROR,
            "ai_audit_finalization_failed",
            action_id=action.id,
            stage="action_finalize_failed_path",
        )
        observe_ai_audit_failure(stage="action_finalize_failed_path", feature=action.feature)
    else:
        log_event(
            logger,
            logging.WARNING,
            "ai_action_failed",
            action_id=action.id,
            trace_id=action.trace_id,
            feature=action.feature,
            error_category=error_category,
        )


def record_translation_cache_hit(
    *,
    source_locale: str,
    target_locale: str,
    entity_type: str,
    field_name: str,
) -> None:
    """Zero-provider-call path: an existing, still-current translation was
    reused. No ``AiAction``/``AiProviderAttempt`` row is created - only a
    structured log event and a Prometheus counter, per Task 66.1 scope."""

    log_event(
        logger,
        logging.INFO,
        "ai_translation_cache_hit",
        source_locale=source_locale,
        target_locale=target_locale,
        entity_type=entity_type,
        field_name=field_name,
    )
    observe_ai_translation_cache(source_locale=source_locale, target_locale=target_locale, status="hit")


def record_translation_cache_miss(
    *,
    source_locale: str,
    target_locale: str,
    entity_type: str,
    field_name: str,
) -> None:
    log_event(
        logger,
        logging.INFO,
        "ai_translation_cache_miss",
        source_locale=source_locale,
        target_locale=target_locale,
        entity_type=entity_type,
        field_name=field_name,
    )
    observe_ai_translation_cache(source_locale=source_locale, target_locale=target_locale, status="miss")

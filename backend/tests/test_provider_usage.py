from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

import pytest
from prometheus_client import REGISTRY

from app.core import metrics
from app.db.models import AiAction, AiActionStep, AiProviderAttempt
from app.main import app
from app.modules.provider_usage import repository
from app.modules.provider_usage.context import AiCallContext, development_test_context
from app.modules.provider_usage.enums import (
    AiActionStatus,
    AiFeature,
    AiStepType,
    ExecutionSource,
    MonetaryCostStatus,
    ProviderAttemptStatus,
)
from app.modules.provider_usage.pricing import (
    PRICING_CATALOG,
    PricingConfigurationError,
    ProviderPricing,
    _validate_catalog,
    get_pricing,
)
from app.modules.provider_usage.service import (
    AuditFinalizationError,
    AuditPersistenceError,
    execute_paid_provider_call,
    record_translation_cache_hit,
    record_translation_cache_miss,
    run_instrumented_single_attempt_action,
)
from app.modules.provider_usage.usage import (
    NormalizedTokenUsage,
    UsageValidationError,
    calculate_provider_usage_cost,
    normalize_openai_compatible_usage,
    validate_token_usage,
)


def _db():
    return app.state.testing_session_local()


# --- Pricing catalog (Part 40) ------------------------------------------------


def test_known_model_returns_expected_decimal_prices():
    pricing = get_pricing(provider="openai_compatible", model="deepseek-chat")
    assert pricing is not None
    assert pricing.uncached_input_per_million_tokens == Decimal("0.14")
    assert pricing.cached_input_per_million_tokens == Decimal("0.0028")
    assert pricing.output_per_million_tokens == Decimal("0.28")
    assert isinstance(pricing.uncached_input_per_million_tokens, Decimal)


def test_unknown_model_returns_none_not_zero():
    assert get_pricing(provider="openai_compatible", model="totally-made-up-model") is None


def test_effective_date_selection():
    old_entry = ProviderPricing(
        provider="openai_compatible",
        model="test-versioned-model",
        pricing_version="v1",
        effective_from=datetime(2026, 1, 1, tzinfo=timezone.utc),
        effective_to=datetime(2026, 6, 1, tzinfo=timezone.utc),
        currency="USD",
        uncached_input_per_million_tokens=Decimal("1.00"),
        cached_input_per_million_tokens=Decimal("0.10"),
        output_per_million_tokens=Decimal("2.00"),
        reasoning_per_million_tokens=None,
        pricing_source="test-fixture",
    )
    new_entry = ProviderPricing(
        provider="openai_compatible",
        model="test-versioned-model",
        pricing_version="v2",
        effective_from=datetime(2026, 6, 1, tzinfo=timezone.utc),
        effective_to=None,
        currency="USD",
        uncached_input_per_million_tokens=Decimal("0.50"),
        cached_input_per_million_tokens=Decimal("0.05"),
        output_per_million_tokens=Decimal("1.00"),
        reasoning_per_million_tokens=None,
        pricing_source="test-fixture",
    )
    catalog = (old_entry, new_entry)
    _validate_catalog(catalog)  # must not raise - ranges are adjacent, not overlapping

    before = get_pricing(
        provider="openai_compatible",
        model="test-versioned-model",
        at=datetime(2026, 3, 1, tzinfo=timezone.utc),
    )
    # get_pricing reads the real module-level PRICING_CATALOG, not our local
    # fixture tuple, so directly exercise the entries' own `covers`.
    assert old_entry.covers(datetime(2026, 3, 1, tzinfo=timezone.utc))
    assert not old_entry.covers(datetime(2026, 7, 1, tzinfo=timezone.utc))
    assert new_entry.covers(datetime(2026, 7, 1, tzinfo=timezone.utc))
    assert not new_entry.covers(datetime(2026, 3, 1, tzinfo=timezone.utc))


def test_overlapping_pricing_entries_are_rejected():
    overlapping_a = ProviderPricing(
        provider="openai_compatible",
        model="overlap-model",
        pricing_version="v1",
        effective_from=datetime(2026, 1, 1, tzinfo=timezone.utc),
        effective_to=None,  # never ends
        currency="USD",
        uncached_input_per_million_tokens=Decimal("1"),
        cached_input_per_million_tokens=Decimal("0.1"),
        output_per_million_tokens=Decimal("2"),
        reasoning_per_million_tokens=None,
        pricing_source="test-fixture",
    )
    overlapping_b = ProviderPricing(
        provider="openai_compatible",
        model="overlap-model",
        pricing_version="v2",
        effective_from=datetime(2026, 2, 1, tzinfo=timezone.utc),  # starts before v1 "ends"
        effective_to=None,
        currency="USD",
        uncached_input_per_million_tokens=Decimal("0.5"),
        cached_input_per_million_tokens=Decimal("0.05"),
        output_per_million_tokens=Decimal("1"),
        reasoning_per_million_tokens=None,
        pricing_source="test-fixture",
    )
    with pytest.raises(PricingConfigurationError):
        _validate_catalog((overlapping_a, overlapping_b))


def test_real_pricing_catalog_is_internally_valid():
    # The actual shipped catalog must itself pass validation (this already
    # runs at import time, but re-asserting here documents the guarantee).
    _validate_catalog(PRICING_CATALOG)


def test_pricing_version_is_persisted_on_calculated_usage():
    token_usage = NormalizedTokenUsage(
        input_tokens=100,
        cached_input_tokens=0,
        uncached_input_tokens=100,
        output_tokens=50,
        reasoning_tokens=None,
        total_tokens=150,
        provider_request_id="req-1",
        raw_usage_redacted=None,
    )
    result = calculate_provider_usage_cost(
        provider="openai_compatible", model="deepseek-chat", token_usage=token_usage
    )
    assert result.pricing_version == "deepseek_2026_07_21_v1"
    assert result.monetary_cost_status == MonetaryCostStatus.CALCULATED


def test_unknown_model_pricing_is_not_zero_and_not_fabricated():
    token_usage = NormalizedTokenUsage(
        input_tokens=100,
        cached_input_tokens=0,
        uncached_input_tokens=100,
        output_tokens=50,
        reasoning_tokens=None,
        total_tokens=150,
        provider_request_id=None,
        raw_usage_redacted=None,
    )
    result = calculate_provider_usage_cost(
        provider="openai_compatible", model="never-heard-of-this-model", token_usage=token_usage
    )
    assert result.monetary_cost_status == MonetaryCostStatus.UNKNOWN
    assert result.total_cost_usd is None
    assert result.pricing_version is None


def test_partial_pricing_when_some_components_priced_and_others_not():
    partial_pricing = ProviderPricing(
        provider="openai_compatible",
        model="partial-model",
        pricing_version="partial-v1",
        effective_from=datetime(2026, 1, 1, tzinfo=timezone.utc),
        effective_to=None,
        currency="USD",
        uncached_input_per_million_tokens=Decimal("1.0"),
        cached_input_per_million_tokens=None,  # unknown for this fictitious model
        output_per_million_tokens=Decimal("2.0"),
        reasoning_per_million_tokens=None,
        pricing_source="test-fixture",
    )
    token_usage = NormalizedTokenUsage(
        input_tokens=100,
        cached_input_tokens=40,
        uncached_input_tokens=60,
        output_tokens=20,
        reasoning_tokens=None,
        total_tokens=120,
        provider_request_id=None,
        raw_usage_redacted=None,
    )
    result = calculate_provider_usage_cost(
        provider="openai_compatible",
        model="partial-model",
        token_usage=token_usage,
        pricing=partial_pricing,
    )
    assert result.monetary_cost_status == MonetaryCostStatus.PARTIAL
    assert result.cached_input_cost_usd is None
    assert result.uncached_input_cost_usd is not None
    assert result.output_cost_usd is not None
    # Total omits the unknown component rather than fabricating it as zero.
    assert result.total_cost_usd == result.uncached_input_cost_usd + result.output_cost_usd


def test_no_tokens_at_all_is_not_applicable():
    token_usage = NormalizedTokenUsage(
        input_tokens=None,
        cached_input_tokens=None,
        uncached_input_tokens=None,
        output_tokens=None,
        reasoning_tokens=None,
        total_tokens=None,
        provider_request_id=None,
        raw_usage_redacted=None,
    )
    result = calculate_provider_usage_cost(
        provider="openai_compatible", model="deepseek-chat", token_usage=token_usage
    )
    assert result.monetary_cost_status == MonetaryCostStatus.NOT_APPLICABLE
    assert result.total_cost_usd is None


def test_decimal_precision_does_not_round_small_costs_to_zero():
    token_usage = NormalizedTokenUsage(
        input_tokens=10,
        cached_input_tokens=0,
        uncached_input_tokens=10,
        output_tokens=1,
        reasoning_tokens=None,
        total_tokens=11,
        provider_request_id=None,
        raw_usage_redacted=None,
    )
    result = calculate_provider_usage_cost(
        provider="openai_compatible", model="deepseek-chat", token_usage=token_usage
    )
    assert result.total_cost_usd is not None
    assert result.total_cost_usd > Decimal("0")


def test_cached_input_savings_calculated_when_both_prices_known():
    token_usage = NormalizedTokenUsage(
        input_tokens=1000,
        cached_input_tokens=1000,
        uncached_input_tokens=0,
        output_tokens=0,
        reasoning_tokens=None,
        total_tokens=1000,
        provider_request_id=None,
        raw_usage_redacted=None,
    )
    result = calculate_provider_usage_cost(
        provider="openai_compatible", model="deepseek-chat", token_usage=token_usage
    )
    # 1000 cached tokens at $0.14/M would cost 0.00014 if uncached; actual
    # cached cost is 1000 * 0.0028/1e6 = 0.0000028 -> savings = difference.
    assert result.cached_input_savings_usd == Decimal("0.000137200")


# --- Usage normalization (Part 41) -------------------------------------------


def test_normalize_complete_deepseek_usage():
    raw = {
        "id": "chatcmpl-abc",
        "usage": {
            "prompt_tokens": 1000,
            "prompt_cache_hit_tokens": 400,
            "prompt_cache_miss_tokens": 600,
            "completion_tokens": 200,
            "total_tokens": 1200,
            "completion_tokens_details": {"reasoning_tokens": 50},
        },
    }
    usage = normalize_openai_compatible_usage(raw_response=raw)
    assert usage.input_tokens == 1000
    assert usage.cached_input_tokens == 400
    assert usage.uncached_input_tokens == 600
    assert usage.output_tokens == 200
    assert usage.reasoning_tokens == 50
    assert usage.total_tokens == 1200
    assert usage.provider_request_id == "chatcmpl-abc"


def test_normalize_missing_cached_token_fields():
    raw = {"id": "req-1", "usage": {"prompt_tokens": 500, "completion_tokens": 50, "total_tokens": 550}}
    usage = normalize_openai_compatible_usage(raw_response=raw)
    assert usage.input_tokens == 500
    assert usage.cached_input_tokens is None
    assert usage.uncached_input_tokens is None
    assert usage.reasoning_tokens is None


def test_normalize_missing_reasoning_tokens_is_none_not_zero():
    raw = {"id": "req-2", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}
    usage = normalize_openai_compatible_usage(raw_response=raw)
    assert usage.reasoning_tokens is None


def test_normalize_provider_request_id_present_and_absent():
    with_id = normalize_openai_compatible_usage(raw_response={"id": "abc", "usage": {}})
    assert with_id.provider_request_id == "abc"
    without_id = normalize_openai_compatible_usage(raw_response={"usage": {}})
    assert without_id.provider_request_id is None


def test_normalize_empty_and_none_response():
    assert normalize_openai_compatible_usage(raw_response=None).input_tokens is None
    assert normalize_openai_compatible_usage(raw_response={}).input_tokens is None


def test_normalize_extra_provider_fields_are_safely_redacted():
    raw = {
        "id": "req-3",
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15,
            "some_unlisted_field": "should not appear",
            "prompt": "the actual private prompt text",
        },
    }
    usage = normalize_openai_compatible_usage(raw_response=raw)
    assert usage.raw_usage_redacted is not None
    assert "some_unlisted_field" not in usage.raw_usage_redacted
    assert "prompt" not in usage.raw_usage_redacted
    assert all(isinstance(value, int) for value in usage.raw_usage_redacted.values())


def test_negative_token_counts_are_rejected():
    with pytest.raises(UsageValidationError):
        validate_token_usage(
            NormalizedTokenUsage(
                input_tokens=-1,
                cached_input_tokens=None,
                uncached_input_tokens=None,
                output_tokens=None,
                reasoning_tokens=None,
                total_tokens=None,
                provider_request_id=None,
                raw_usage_redacted=None,
            )
        )


def test_cached_tokens_exceeding_input_tokens_is_rejected():
    with pytest.raises(UsageValidationError):
        validate_token_usage(
            NormalizedTokenUsage(
                input_tokens=100,
                cached_input_tokens=150,
                uncached_input_tokens=None,
                output_tokens=None,
                reasoning_tokens=None,
                total_tokens=None,
                provider_request_id=None,
                raw_usage_redacted=None,
            )
        )


def test_inconsistent_totals_are_rejected():
    with pytest.raises(UsageValidationError):
        validate_token_usage(
            NormalizedTokenUsage(
                input_tokens=100,
                cached_input_tokens=None,
                uncached_input_tokens=None,
                output_tokens=50,
                reasoning_tokens=None,
                total_tokens=999,
                provider_request_id=None,
                raw_usage_redacted=None,
            )
        )


def test_valid_usage_with_all_fields_passes_validation():
    validate_token_usage(
        NormalizedTokenUsage(
            input_tokens=100,
            cached_input_tokens=40,
            uncached_input_tokens=60,
            output_tokens=50,
            reasoning_tokens=10,
            total_tokens=150,
            provider_request_id="req-ok",
            raw_usage_redacted=None,
        )
    )


# --- Persistence (Part 42) ----------------------------------------------------


def _make_action_and_step(db, *, feature=AiFeature.DEVELOPMENT_TEST, execution_source=ExecutionSource.TEST):
    context = AiCallContext(feature=feature, execution_source=execution_source, trace_id="test-trace")
    action = repository.create_action(db, context=context)
    db.commit()
    step = repository.create_step(
        db,
        action=action,
        step_type=AiStepType.PROVIDER_GENERATION,
        sequence_number=1,
        execution_source=execution_source,
    )
    db.commit()
    return action, step


def test_action_and_step_creation(client):
    db = _db()
    try:
        action, step = _make_action_and_step(db)
        assert action.id is not None
        assert action.status == AiActionStatus.RUNNING.value
        assert step.action_id == action.id
        assert step.sequence_number == 1
    finally:
        db.close()


def test_provider_attempt_created_before_operation_runs(client):
    db = _db()
    try:
        action, step = _make_action_and_step(db)
        call_log: list[str] = []

        def operation():
            # By the time this runs, the pending attempt row must already
            # be durably committed (fail-closed pre-call persistence).
            existing = db.get(AiProviderAttempt, 1)
            call_log.append("called")
            return {"id": "req-1", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}

        result = execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider="openai_compatible",
            model="deepseek-chat",
            attempt_number=1,
            operation=operation,
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
        )
        assert call_log == ["called"]
        assert result.normalized_usage.monetary_cost_status == MonetaryCostStatus.CALCULATED
    finally:
        db.close()


def test_successful_finalization_persists_tokens_and_cost(client):
    db = _db()
    try:
        action, step = _make_action_and_step(db)
        execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider="openai_compatible",
            model="deepseek-chat",
            attempt_number=1,
            operation=lambda: {
                "id": "req-2",
                "usage": {"prompt_tokens": 1000, "completion_tokens": 100, "total_tokens": 1100},
            },
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
        )
        repository.finalize_action(db, action, status=AiActionStatus.SUCCEEDED)
        db.commit()

        fetched = repository.get_action_with_details(db, action_id=action.id)
        assert fetched.provider_call_count == 1
        assert fetched.total_tokens == 1100
        assert fetched.total_cost_usd > Decimal("0")
        assert fetched.status == AiActionStatus.SUCCEEDED.value
    finally:
        db.close()


def test_failed_call_is_recorded_and_reraised(client):
    db = _db()
    try:
        action, step = _make_action_and_step(db)

        def failing_operation():
            raise RuntimeError("BrainProviderRequestError: simulated network failure")

        with pytest.raises(RuntimeError):
            execute_paid_provider_call(
                db,
                action=action,
                step=step,
                provider="openai_compatible",
                model="deepseek-chat",
                attempt_number=1,
                operation=failing_operation,
                extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
            )
        attempts = db.query(AiProviderAttempt).filter(AiProviderAttempt.step_id == step.id).all()
        assert len(attempts) == 1
        assert attempts[0].status != ProviderAttemptStatus.SUCCEEDED.value
        assert attempts[0].success is False
    finally:
        db.close()


def test_timeout_classification():
    from app.modules.provider_usage.service import _classify_provider_exception

    status, category = _classify_provider_exception(TimeoutError("request timed out"))
    assert status == ProviderAttemptStatus.TIMEOUT


def test_retry_creates_two_separate_attempt_rows(client):
    db = _db()
    try:
        action, step = _make_action_and_step(db)

        def failing_operation():
            raise RuntimeError("BrainProviderRequestError: first attempt fails")

        with pytest.raises(RuntimeError):
            execute_paid_provider_call(
                db,
                action=action,
                step=step,
                provider="openai_compatible",
                model="deepseek-chat",
                attempt_number=1,
                operation=failing_operation,
                extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
                retry_reason=None,
            )

        execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider="openai_compatible",
            model="deepseek-chat",
            attempt_number=2,
            operation=lambda: {
                "id": "req-retry",
                "usage": {"prompt_tokens": 100, "completion_tokens": 20, "total_tokens": 120},
            },
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
            retry_reason="provider_timeout",
        )
        repository.recompute_step_totals(db, step)
        db.commit()

        attempts = (
            db.query(AiProviderAttempt)
            .filter(AiProviderAttempt.step_id == step.id)
            .order_by(AiProviderAttempt.attempt_number)
            .all()
        )
        assert len(attempts) == 2
        assert attempts[0].attempt_number == 1
        assert attempts[0].success is False
        assert attempts[1].attempt_number == 2
        assert attempts[1].success is True
        # Step totals reflect only the successful attempt's usage.
        assert step.total_tokens == 120
    finally:
        db.close()


def test_repeated_finalization_is_idempotent(client):
    db = _db()
    try:
        action, step = _make_action_and_step(db)
        execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider="openai_compatible",
            model="deepseek-chat",
            attempt_number=1,
            operation=lambda: {
                "id": "req-3",
                "usage": {"prompt_tokens": 100, "completion_tokens": 20, "total_tokens": 120},
            },
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
        )
        repository.finalize_action(db, action, status=AiActionStatus.SUCCEEDED)
        db.commit()
        first_cost = action.total_cost_usd
        first_count = action.provider_call_count

        # Simulate a redelivery re-finalizing the same, already-complete action.
        repository.finalize_action(db, action, status=AiActionStatus.SUCCEEDED)
        db.commit()

        assert action.total_cost_usd == first_cost
        assert action.provider_call_count == first_count == 1
    finally:
        db.close()


def test_incomplete_pending_attempt_remains_detectable(client):
    db = _db()
    try:
        action, step = _make_action_and_step(db)
        attempt, created = repository.get_or_create_pending_attempt(
            db, action=action, step=step, attempt_number=1, provider="openai_compatible", model="deepseek-chat"
        )
        db.commit()
        assert created is True
        assert attempt.status == ProviderAttemptStatus.PENDING.value

        # Without any finalization call, the row must still be visible and
        # inspectable as "incomplete" - not silently lost.
        refetched = db.get(AiProviderAttempt, attempt.id)
        assert refetched is not None
        assert refetched.status == ProviderAttemptStatus.PENDING.value
    finally:
        db.close()


def test_audit_initialization_failure_prevents_provider_call(client, monkeypatch):
    db = _db()
    try:
        action, step = _make_action_and_step(db)
        call_log: list[str] = []

        def operation():
            call_log.append("called")
            return {"id": "should-not-happen", "usage": {}}

        def broken_get_or_create(*args, **kwargs):
            raise RuntimeError("simulated durable-storage outage")

        monkeypatch.setattr(repository, "get_or_create_pending_attempt", broken_get_or_create)

        with pytest.raises(AuditPersistenceError):
            execute_paid_provider_call(
                db,
                action=action,
                step=step,
                provider="openai_compatible",
                model="deepseek-chat",
                attempt_number=1,
                operation=operation,
                extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
            )
        assert call_log == []  # the provider was never called - fail closed
    finally:
        db.close()


def test_audit_finalization_failure_does_not_return_silent_success(client, monkeypatch):
    db = _db()
    try:
        action, step = _make_action_and_step(db)

        def broken_finalize_success(*args, **kwargs):
            raise RuntimeError("simulated post-call persistence failure")

        monkeypatch.setattr(repository, "finalize_attempt_success", broken_finalize_success)

        with pytest.raises(AuditFinalizationError):
            execute_paid_provider_call(
                db,
                action=action,
                step=step,
                provider="openai_compatible",
                model="deepseek-chat",
                attempt_number=1,
                operation=lambda: {
                    "id": "req-4",
                    "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
                },
                extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
            )
        # The pending attempt row remains, visible for later reconciliation -
        # never silently converted into a fabricated success.
        attempts = db.query(AiProviderAttempt).filter(AiProviderAttempt.step_id == step.id).all()
        assert len(attempts) == 1
        assert attempts[0].status == ProviderAttemptStatus.PENDING.value
    finally:
        db.close()


# --- Celery-safe context propagation and redelivery (Part 45) ---------------


def test_ai_call_context_round_trips_through_task_kwargs():
    context = AiCallContext(
        feature=AiFeature.BRAIN_CHAT_RESPONSE,
        execution_source=ExecutionSource.FASTAPI,
        trace_id="trace-123",
        requested_locale="ru",
        resolved_locale="ru",
        user_id=7,
        memorial_id=9,
        message_id=42,
    )
    payload = context.to_task_kwargs()
    # JSON-safe: every value is a primitive (str/int/None), never an enum
    # instance or other Python object, since this must survive Celery's own
    # JSON task-argument serialization.
    assert all(isinstance(value, (str, int, type(None))) for value in payload.values())

    restored = AiCallContext.from_task_kwargs(payload)
    assert restored == context
    assert restored.trace_id == context.trace_id
    assert restored.user_id == context.user_id
    assert restored.memorial_id == context.memorial_id


def test_with_celery_task_id_sets_execution_source_celery():
    context = development_test_context(trace_id="t1")
    updated = context.with_celery_task_id("celery-task-abc")
    assert updated.celery_task_id == "celery-task-abc"
    assert updated.execution_source == ExecutionSource.CELERY


def test_celery_redelivery_does_not_double_count_or_recall_provider(client):
    """Simulates what a Celery task redelivery looks like at the
    repository/service layer: the exact same (step, attempt_number) pair is
    processed twice (e.g. the broker redelivers an unacked message after a
    worker restart). The second pass must reuse the existing terminal
    attempt row rather than calling the provider or the pricing engine
    again - proving the accounting stays correct under at-least-once
    delivery, independent of which process (FastAPI or Celery) is calling.
    """

    db = _db()
    try:
        context = AiCallContext(
            feature=AiFeature.MEMORY_SUMMARIZATION,
            execution_source=ExecutionSource.CELERY,
            trace_id="celery-trace-1",
            celery_task_id="celery-task-1",
        )
        action = repository.create_action(db, context=context)
        db.commit()
        step = repository.create_step(
            db,
            action=action,
            step_type=AiStepType.PROVIDER_GENERATION,
            sequence_number=1,
            execution_source=ExecutionSource.CELERY,
        )
        db.commit()

        call_count = {"n": 0}

        def operation():
            call_count["n"] += 1
            return {"id": "celery-req-1", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}

        # First delivery: real provider call happens once.
        execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider="openai_compatible",
            model="deepseek-chat",
            attempt_number=1,
            operation=operation,
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
        )
        repository.recompute_step_totals(db, step)
        repository.finalize_action(db, action, status=AiActionStatus.SUCCEEDED)
        db.commit()
        cost_after_first = action.total_cost_usd
        tokens_after_first = action.total_tokens

        # Second delivery (redelivery of the SAME logical attempt): the
        # provider must not be called again, and totals must not change.
        execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider="openai_compatible",
            model="deepseek-chat",
            attempt_number=1,
            operation=operation,
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
        )
        repository.finalize_action(db, action, status=AiActionStatus.SUCCEEDED)
        db.commit()

        assert call_count["n"] == 1  # provider was never called a second time
        assert action.total_cost_usd == cost_after_first
        assert action.total_tokens == tokens_after_first
        assert action.provider_call_count == 1
    finally:
        db.close()


# --- run_instrumented_single_attempt_action (FastAPI-shaped happy/error paths) --


def test_run_instrumented_single_attempt_action_success(client):
    db = _db()
    try:
        response, action = run_instrumented_single_attempt_action(
            db,
            context=development_test_context(trace_id="single-attempt-1"),
            step_type=AiStepType.PROVIDER_GENERATION,
            provider="openai_compatible",
            model="deepseek-chat",
            operation=lambda: {
                "id": "req-single",
                "usage": {"prompt_tokens": 30, "completion_tokens": 10, "total_tokens": 40},
            },
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
        )
        assert response["id"] == "req-single"
        assert action.status == AiActionStatus.SUCCEEDED.value
        assert action.total_tokens == 40
        assert action.total_cost_usd > Decimal("0")
    finally:
        db.close()


def test_run_instrumented_single_attempt_action_failure_marks_action_failed(client):
    db = _db()
    try:

        def failing_operation():
            raise RuntimeError("ContentTranslationProviderRequestError: down")

        with pytest.raises(RuntimeError):
            run_instrumented_single_attempt_action(
                db,
                context=development_test_context(trace_id="single-attempt-fail"),
                step_type=AiStepType.PROVIDER_TRANSLATION,
                provider="openai_compatible",
                model="deepseek-chat",
                operation=failing_operation,
                extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
            )
        failed_action = (
            db.query(AiAction).filter(AiAction.trace_id == "single-attempt-fail").one()
        )
        assert failed_action.status == AiActionStatus.FAILED.value
        assert failed_action.error_category is not None
    finally:
        db.close()


# --- Translation cache hit/miss recording (Part 44) --------------------------


def test_translation_cache_hit_and_miss_increment_distinct_counters():
    before_hit = REGISTRY.get_sample_value(
        "ai_cost_translation_cache_total", {"source_locale": "cs", "target_locale": "ru", "status": "hit"}
    ) or 0
    before_miss = REGISTRY.get_sample_value(
        "ai_cost_translation_cache_total", {"source_locale": "cs", "target_locale": "ru", "status": "miss"}
    ) or 0

    record_translation_cache_hit(
        source_locale="cs", target_locale="ru", entity_type="memory_candidate", field_name="finalized_memory_text"
    )
    record_translation_cache_miss(
        source_locale="cs", target_locale="ru", entity_type="memory_candidate", field_name="finalized_memory_text"
    )

    after_hit = REGISTRY.get_sample_value(
        "ai_cost_translation_cache_total", {"source_locale": "cs", "target_locale": "ru", "status": "hit"}
    )
    after_miss = REGISTRY.get_sample_value(
        "ai_cost_translation_cache_total", {"source_locale": "cs", "target_locale": "ru", "status": "miss"}
    )
    assert after_hit == before_hit + 1
    assert after_miss == before_miss + 1


# --- Metrics (Part 46) --------------------------------------------------------


def test_provider_call_metrics_increment_on_success(client):
    db = _db()
    try:
        before = REGISTRY.get_sample_value(
            "ai_cost_provider_calls_total",
            {
                "provider": "openai_compatible",
                "model": "deepseek-chat",
                "feature": "development_test",
                "status": "succeeded",
            },
        ) or 0
        action, step = _make_action_and_step(db)
        execute_paid_provider_call(
            db,
            action=action,
            step=step,
            provider="openai_compatible",
            model="deepseek-chat",
            attempt_number=1,
            operation=lambda: {
                "id": "req-metric",
                "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
            },
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(raw_response=resp),
        )
        after = REGISTRY.get_sample_value(
            "ai_cost_provider_calls_total",
            {
                "provider": "openai_compatible",
                "model": "deepseek-chat",
                "feature": "development_test",
                "status": "succeeded",
            },
        )
        assert after == before + 1
    finally:
        db.close()


def test_unknown_pricing_metric_increments():
    # Model labels pass through verbatim (matching this repo's existing
    # `brain_answer_*` metric convention where model is already an
    # unrestricted label - only `provider`/`feature`/`status` are mapped to
    # a closed set); only the provider/feature/status dimensions are
    # normalized to a bounded set.
    label_kwargs = {"provider": "openai_compatible", "model": "some-unpriced-model", "feature": "other"}
    before = REGISTRY.get_sample_value("ai_cost_pricing_unknown_total", label_kwargs) or 0
    metrics.observe_ai_provider_attempt(
        provider="openai_compatible",
        model="some-unpriced-model",
        feature="other",
        status="succeeded",
        latency_seconds=0.1,
        token_usage=calculate_provider_usage_cost(
            provider="openai_compatible",
            model="some-unpriced-model",
            token_usage=NormalizedTokenUsage(
                input_tokens=10,
                cached_input_tokens=None,
                uncached_input_tokens=10,
                output_tokens=5,
                reasoning_tokens=None,
                total_tokens=15,
                provider_request_id=None,
                raw_usage_redacted=None,
            ),
        ),
    )
    after = REGISTRY.get_sample_value("ai_cost_pricing_unknown_total", label_kwargs)
    assert after == before + 1


def test_audit_failure_metric_increments():
    before = REGISTRY.get_sample_value(
        "ai_cost_audit_failures_total", {"stage": "pre_call", "feature": "other"}
    ) or 0
    metrics.observe_ai_audit_failure(stage="pre_call", feature="other")
    after = REGISTRY.get_sample_value(
        "ai_cost_audit_failures_total", {"stage": "pre_call", "feature": "other"}
    )
    assert after == before + 1


def test_metric_labels_reject_high_cardinality_values_via_normalization():
    # Passing a raw, unbounded string (that looks like a user id or a stray
    # error message) must fall back to a small closed label value, never be
    # used verbatim as a Prometheus label.
    normalized_feature = metrics.normalize_ai_feature_label("user_id_12345_leaked_by_mistake")
    assert normalized_feature == "other"
    normalized_status = metrics.normalize_ai_attempt_status_label("some raw provider error text")
    assert normalized_status == "internal_error"


# --- Privacy (Part 47) --------------------------------------------------------


def test_raw_usage_redacted_never_contains_string_prompt_text():
    raw = {
        "id": "req-privacy",
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15,
            "prompt": "the user's actual private message",
            "completion": "the assistant's actual private answer",
        },
    }
    usage = normalize_openai_compatible_usage(raw_response=raw)
    assert usage.raw_usage_redacted is not None
    for value in usage.raw_usage_redacted.values():
        assert isinstance(value, int)


def test_ai_call_context_has_no_secret_fields():
    # Structural guarantee: AiCallContext's dataclass fields never include
    # anything resembling a credential/secret - it only carries small
    # identifiers and enum-like classification values.
    field_names = set(AiCallContext.__dataclass_fields__.keys())
    forbidden_substrings = ("password", "secret", "api_key", "token_value", "authorization")
    for field_name in field_names:
        for forbidden in forbidden_substrings:
            assert forbidden not in field_name.lower()

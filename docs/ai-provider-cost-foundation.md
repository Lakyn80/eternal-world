# AI Provider Usage and Cost Foundation

Task 66.1. This document explains how every paid DeepSeek/OpenAI-compatible provider call in Eternal World becomes attributable, reproducible, and inspectable. It does not cover analytics/reporting APIs (Task 66.2) or budgets/anomaly detection/admin UI (Task 66.3) - those are separate, later, deferred tasks.

## 1. The trace hierarchy

```text
AiAction        - one user-visible operation (one Chat message+answer, one dynamic translation)
  AiActionStep  - one processing step within that action (provider_generation, provider_translation, ...)
    AiProviderAttempt - one individual HTTP attempt to the paid provider
```

Tables: `ai_actions`, `ai_action_steps`, `ai_provider_attempts` (migration `20260721_0024`). All three are purely additive; no existing table was altered.

- **One action per operation.** A Chat message creates one `AiAction` with `feature="brain_chat_response"`. A dynamic translation call creates one `AiAction` with `feature="dynamic_memory_translation"`.
- **One step per action** in the current implementation (`sequence_number=1`), since every real call site today is "one action, one step, one provider attempt." The schema supports multiple steps per action for future multi-call features (e.g. retrieval + generation + guard as separate steps), but nothing populates more than one step yet.
- **A retry creates a new attempt row**, never overwrites a failed one. `(step_id, attempt_number)` is unique - `attempt_number` increments per retry.

Action/step totals (`total_tokens`, `total_cost_usd`, `provider_call_count`, `monetary_cost_status`, ...) are **always recomputed by summing the action's/step's `AiProviderAttempt` rows** (`repository.recompute_action_totals`/`recompute_step_totals`), never incremented in place. This is what makes repeated finalization (a Celery redelivery, a duplicate call) safe: recomputing from the same underlying attempt rows always yields the same totals.

## 2. How a provider call is traced

Every paid call goes through one shared wrapper: `app.modules.provider_usage.service.execute_paid_provider_call` (or the higher-level `run_instrumented_single_attempt_action` for the common "one action, one step, one attempt" shape used by every current call site).

Sequence:

1. **Before any network request**: a pending `AiProviderAttempt` row is created and *committed* durably. If this fails, `AuditPersistenceError` is raised and the provider is **never called** - fail-closed.
2. The actual provider call runs (`operation()` - whatever the caller passes, e.g. `orchestrator.generate_chat_response(...)` or `active_provider.translate(...)`).
3. **On failure**: the exception is classified (timeout/rate-limited/http-error/invalid-response/validation-error/internal-error, via a class-name heuristic in `_classify_provider_exception` that works for both the Brain and translation provider's hand-rolled exception hierarchies without a circular import), the attempt is marked failed, and the **original exception is re-raised unchanged** - callers see the exact same exception type/behavior as before this task.
4. **On success**: the raw response is normalized into token counts (`normalize_openai_compatible_usage`), priced (`calculate_provider_usage_cost`), and persisted. If persistence fails here, `AuditFinalizationError` is raised - a successful provider call is never silently reported as a success without a durable record.

## 3. Pricing

`app/modules/provider_usage/pricing.py` - one typed, versioned, `Decimal`-based catalog (`PRICING_CATALOG`), keyed by `(provider, model)` with an effective date range per entry.

Current entries (verified live against the official DeepSeek pricing page on 2026-07-21, source: https://api-docs.deepseek.com/quick_start/pricing):

| Provider | Model | Uncached input /1M | Cached input /1M | Output /1M | Reasoning /1M | Pricing version |
|---|---|---|---|---|---|---|
| openai_compatible | deepseek-chat | $0.14 | $0.0028 | $0.28 | unset (non-thinking model) | `deepseek_2026_07_21_v1` |
| openai_compatible | deepseek-reasoner | $0.14 | $0.0028 | $0.28 | unset (no separate published rate) | `deepseek_2026_07_21_v1` |

**Important, time-sensitive note**: DeepSeek's own documentation states `deepseek-chat`/`deepseek-reasoner` will be **deprecated on 2026-07-24 15:59 UTC**, at which point they map to the non-thinking/thinking modes of `deepseek-v4-flash` (already billed at the rates above). This is a real, near-term operational risk for this deployment (`AI_BRAIN_MODEL=deepseek-chat`) that is **out of scope to fix in Task 66.1** (no model switching allowed) - flagged here so it is not missed.

**To add or update a price**: append a new `ProviderPricing` entry to `PRICING_CATALOG` in `pricing.py` with a later `effective_from` (and set the previous entry's `effective_to` to that same instant). Never edit an existing entry in place - that would silently change the meaning of every already-persisted `AiProviderAttempt` row that references its `pricing_version`. `_validate_catalog` (run at import time) rejects overlapping ranges for the same `(provider, model)`.

**Unknown/partial pricing**: a model with no catalog entry prices as `monetary_cost_status="unknown"` with `total_cost_usd=NULL` - never `0`. A model with some priced components and others unset (e.g. no cached-input rate) prices as `"partial"`, summing only the known components.

## 4. Cost calculation

`app/modules/provider_usage/usage.py`:

- `normalize_openai_compatible_usage(raw_response)` reads the real DeepSeek response shape (`id`, `usage.prompt_tokens`, `usage.prompt_cache_hit_tokens`, `usage.prompt_cache_miss_tokens`, `usage.completion_tokens`, `usage.total_tokens`, `usage.completion_tokens_details.reasoning_tokens`) - verified against the official API docs, not guessed. Missing optional fields normalize to `None`, never `0`.
- `validate_token_usage` rejects impossible states (negative counts, cached > input, inconsistent totals) before any cost is computed.
- `calculate_provider_usage_cost` computes each cost component as `Decimal(tokens) * price_per_million / 1_000_000`, summing only known components, and only quantizes (`ROUND_HALF_UP`, 9 decimal places) once at the very end - never rounds intermediate components before summing, so very small per-request costs are never rounded to zero.
- `cached_input_savings_usd` = what the cached tokens *would have cost* at the uncached rate, minus what they actually cost - only computed when both rates are known.

## 5. FastAPI integration

Real call sites (confirmed via a full repo inventory before implementation - see `PROJECT_PROGRESS.md`'s Task 66.1 section for the grounded matrix):

- `chat/service.py: send_chat_message` (authenticated `/api/chat`) - wraps `orchestrator.generate_chat_response(...)` with `run_instrumented_single_attempt_action`, `feature=brain_chat_response`, attributed to `user_id`/`memorial_id` (=`profile_id`)/`message_id`, `trace_id` = the request's own `X-Request-ID`.
- `demo_fa_chat/service.py: run_demo_fa_chat_message` - same wrapper around the same orchestrator call, `execution_source=fastapi` (it's still a real FastAPI request handler, just for the unauthenticated demo persona), `memorial_id` = the demo profile id, `requested_locale`/`resolved_locale` = the FA chat's own `locale`.
- `content_translation/service.py: translate_content_field` - the single shared choke point for **every** dynamic translation call (chat-turn localization, memory-candidate/contribution finalization, explicit retry) - wraps `active_provider.translate(...)` + validation with the same `run_instrumented_single_attempt_action`, `feature=dynamic_memory_translation` or `memory_candidate_finalization` depending on caller.
- `demo_fa_chat/service.py: _localize_review_text` - the cache decision point: `is_translation_current(...) == True` returns the cached text and calls `record_translation_cache_hit(...)` (zero provider calls, zero new `AiAction` rows); otherwise calls `record_translation_cache_miss(...)` then `translate_content_field`.

Direct-locale Chat (Task 64.5.2) is preserved: one Chat message still makes exactly one Brain provider call and zero separate translation calls, in either Czech or Russian - verified live (see below).

Dev-only evaluation scripts (`rag_evaluation/brain_eval_runner.py`, `brain_eval_e2e_runner.py`, reachable only via `scripts/run_brain_rag_eval.py`) call `BrainAgentService` directly and are **not yet instrumented** - documented as a known limitation, since they are manual developer tools, never production traffic, and never exercised by the automated test suite.

## 6. Celery integration

`app/modules/provider_usage/context.py: AiCallContext` is a plain, JSON-serializable dataclass (`to_task_kwargs()`/`from_task_kwargs()`) specifically so it can cross the FastAPI-to-Celery process boundary as ordinary task arguments - it never relies on process-local `contextvars`.

**No Celery task in this codebase currently makes a paid provider call** (confirmed via the Part-A inventory: all 4 existing tasks - `run_rag_source_processing_job`, `run_multi_embedding_eval_job`, `run_memorial_contribution_indexing_job`, `run_biography_indexing_job` - only do embedding/Qdrant work, never Brain/translation). The propagation mechanism and its redelivery-safety are therefore proven at the repository/service layer (`tests/test_provider_usage.py`, the Celery-redelivery test), not through a real production Celery+paid-call path, since none exists yet to wire into. Redelivery safety works identically regardless of process: `get_or_create_pending_attempt` looks up the existing row for `(step_id, attempt_number)` before inserting, so a redelivered/duplicate execution reuses the same terminal row and never re-calls the provider or double-counts cost.

## 7. Translation cache accounting

- **Cache hit**: `is_translation_current(existing_row, current_source_text=...)` is `True` -> the existing translated text is reused, `record_translation_cache_hit(...)` logs `ai_translation_cache_hit` and increments `ai_cost_translation_cache_total{status="hit"}` - **zero** `AiAction`/`AiProviderAttempt` rows are created.
- **Cache miss**: `record_translation_cache_miss(...)` logs/increments `status="miss"`, then `translate_content_field` runs the real provider call through the shared wrapper.

## 8. Structured logs

All events use the existing `app.core.logging.log_event`/`get_logger` convention (`eternal_world.provider_usage` logger, JSON output, automatic `request_id` injection). Events: `ai_action_started`, `ai_step_started`, `ai_provider_attempt_started`, `ai_provider_attempt_succeeded`, `ai_provider_attempt_failed`, `ai_step_completed`, `ai_action_completed`, `ai_action_failed`, `ai_audit_initialization_failed`, `ai_audit_finalization_failed`, `ai_translation_cache_hit`, `ai_translation_cache_miss`.

Never logged: API keys, authorization headers, full prompts/answers, full biography/memory text. Only token counts, cost figures, small identifiers (action/step/attempt/trace ids), and enum-like classification values are logged.

## 9. Prometheus metrics

`app/core/metrics.py`, prefix `ai_cost_*` (matching this repo's existing domain-prefixed-flat-name convention, e.g. `brain_answer_*`, `content_translation_*` - not a global `eternal_world_*` prefix, since none of the pre-existing metrics use one):

`ai_cost_actions_total`, `ai_cost_action_duration_seconds`, `ai_cost_provider_calls_total`, `ai_cost_provider_latency_seconds`, `ai_cost_tokens_total`, `ai_cost_usd_total`, `ai_cost_cached_input_savings_usd_total`, `ai_cost_retries_total`, `ai_cost_translation_cache_total`, `ai_cost_pricing_unknown_total`, `ai_cost_audit_failures_total`.

Every label is a small closed set (`feature`, `execution_source`, `status`, `token_type`, `cost_component`, `monetary_cost_status`, `stage`, `source_locale`/`target_locale`) via dedicated `normalize_ai_*_label` functions - **never** a user id, memorial id, trace/action/step id, or raw error message. `model` passes through verbatim, matching this repo's pre-existing `brain_answer_*{provider,model}` convention (only 1-2 model strings are ever configured server-side in this single-tenant deployment, so it stays low-cardinality in practice even though the type itself is unrestricted).

No Grafana dashboard changes were made - full cost panels are deferred to a later task.

## 10. Inspecting the data

**PostgreSQL** (source of truth):

```sql
select * from ai_actions order by id desc limit 20;
select * from ai_action_steps where action_id = <id>;
select * from ai_provider_attempts where action_id = <id> order by attempt_number;
```

**In Python** (the reusable query seam for a future Task 66.2 admin API):

```python
from app.modules.provider_usage import repository
action = repository.get_action_with_details(db, action_id=<id>)  # eager-loads steps + attempts
```

**No internal/admin HTTP endpoint was added in Task 66.1.** The codebase has no existing admin-authorization pattern (`User.is_superuser` exists as a column but is checked nowhere), and building one from scratch would itself be new-feature scope creep into Task 66.2's admin API. `repository.get_action_with_details` is the documented, ready-to-wrap seam for whenever that authorization pattern exists.

**Metrics**: `GET /metrics` (existing endpoint, unchanged) - the `ai_cost_*` series appear there after any real activity.

## 11. What is deferred

- **Task 66.2**: aggregated analytics API, cost timeseries, per-user/memorial/model reports, CSV/JSON export, admin usage explorer, retention management.
- **Task 66.3**: budget configuration and enforcement, per-action cost denial, anomaly detection, cost recommendations, admin cost frontend, full Grafana cost dashboard.

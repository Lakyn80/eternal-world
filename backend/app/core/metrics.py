from __future__ import annotations

from typing import Any

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, Histogram, generate_latest
from starlette.responses import Response


_NORMALIZED_GUARD_REASONS = {
    None: "none",
    "": "none",
    "forbidden_claim_in_lack_case": "forbidden_claim_in_lack_case",
    "no_evidence_answer_with_extra_detail": "no_evidence_answer_with_extra_detail",
    "avatar_internal_citation_removed": "avatar_internal_citation_removed",
}

_NORMALIZED_BRAIN_PROVIDERS = {
    "mock": "mock",
    "openai_compatible": "openai_compatible",
}


HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests.",
    labelnames=("method", "route", "status_code"),
)
HTTP_REQUEST_DURATION_SECONDS = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds.",
    labelnames=("method", "route", "status_code"),
)
HTTP_ERRORS_TOTAL = Counter(
    "http_errors_total",
    "Total HTTP error responses.",
    labelnames=("method", "route", "status_code"),
)

FA_CHAT_REQUESTS_TOTAL = Counter(
    "fa_chat_requests_total",
    "Total FA demo chat requests.",
    labelnames=("outcome", "retrieval_used", "guard_applied", "guard_reason", "debug"),
)
FA_CHAT_DURATION_SECONDS = Histogram(
    "fa_chat_duration_seconds",
    "FA demo chat duration in seconds.",
    labelnames=("outcome", "retrieval_used", "guard_applied", "guard_reason", "debug"),
)
FA_CHAT_ERRORS_TOTAL = Counter(
    "fa_chat_errors_total",
    "Total FA demo chat errors.",
    labelnames=("outcome", "debug"),
)
FA_CHAT_LACK_OF_EVIDENCE_TOTAL = Counter(
    "fa_chat_lack_of_evidence_total",
    "Total FA demo chat responses marked as lack of evidence.",
    labelnames=("debug",),
)
FA_CHAT_GUARD_APPLIED_TOTAL = Counter(
    "fa_chat_guard_applied_total",
    "Total FA demo chat responses where the output guard was applied.",
    labelnames=("guard_reason", "debug"),
)

RAG_RETRIEVAL_DURATION_SECONDS = Histogram(
    "rag_retrieval_duration_seconds",
    "RAG retrieval duration in seconds.",
    labelnames=("retrieval_mode", "top_k"),
)
RAG_RETRIEVED_CHUNKS_COUNT = Histogram(
    "rag_retrieved_chunks_count",
    "Number of chunks returned by RAG retrieval.",
    labelnames=("retrieval_mode", "top_k"),
    buckets=(0, 1, 2, 3, 5, 10, 20, 50),
)
RAG_RETRIEVAL_ERRORS_TOTAL = Counter(
    "rag_retrieval_errors_total",
    "Total RAG retrieval errors.",
    labelnames=("retrieval_mode", "top_k"),
)

EMBEDDING_CACHE_HITS_TOTAL = Counter(
    "embedding_cache_hits_total",
    "Total embedding cache hits.",
    labelnames=("provider_code", "input_type", "mode"),
)
EMBEDDING_CACHE_MISSES_TOTAL = Counter(
    "embedding_cache_misses_total",
    "Total embedding cache misses.",
    labelnames=("provider_code", "input_type", "mode"),
)
EMBEDDING_CACHE_WRITES_TOTAL = Counter(
    "embedding_cache_writes_total",
    "Total embedding cache writes.",
    labelnames=("provider_code", "input_type", "mode"),
)
EMBEDDING_CACHE_ERRORS_TOTAL = Counter(
    "embedding_cache_errors_total",
    "Total embedding cache errors.",
    labelnames=("provider_code", "input_type", "mode"),
)

BRAIN_ANSWER_DURATION_SECONDS = Histogram(
    "brain_answer_duration_seconds",
    "Brain answer generation duration in seconds.",
    labelnames=("provider", "model"),
)
BRAIN_ANSWER_ERRORS_TOTAL = Counter(
    "brain_answer_errors_total",
    "Total Brain answer generation errors.",
    labelnames=("provider", "model"),
)
MEMORY_CANDIDATE_CREATED_TOTAL = Counter(
    "memory_candidate_created_total",
    "Total conversation-derived memory candidates created.",
    labelnames=("persisted", "status"),
)
MEMORY_CANDIDATE_REVIEWED_TOTAL = Counter(
    "memory_candidate_reviewed_total",
    "Total reviewed conversation-derived memory candidates.",
    labelnames=("status",),
)
MEMORY_PROMOTION_CREATED_TOTAL = Counter(
    "memory_promotion_created_total",
    "Total avatar memory promotion records created.",
)
MEMORY_PROMOTION_STATUS_TOTAL = Counter(
    "memory_promotion_status_total",
    "Total avatar memory promotion status events.",
    labelnames=("status",),
)
MEMORY_INDEXING_STARTED_TOTAL = Counter(
    "memory_indexing_started_total",
    "Total explicit approved memory indexing attempts started.",
)
MEMORY_INDEXING_COMPLETED_TOTAL = Counter(
    "memory_indexing_completed_total",
    "Total explicit approved memory indexing calls completed safely.",
)
MEMORY_INDEXING_FAILED_TOTAL = Counter(
    "memory_indexing_failed_total",
    "Total explicit approved memory indexing calls that failed.",
)
MEMORY_INDEXING_DURATION_SECONDS = Histogram(
    "memory_indexing_duration_seconds",
    "Explicit approved memory indexing duration in seconds.",
    labelnames=("result",),
)
MEMORY_PROMOTION_INDEX_STATUS_TOTAL = Counter(
    "memory_promotion_index_status_total",
    "Total explicit approved memory indexing outcomes.",
    labelnames=("status",),
)
MEMORY_PROMOTIONS_CURRENT = Gauge(
    "memory_promotions_current",
    "Current avatar memory promotions by durable status.",
    labelnames=("status",),
)
MEMORY_CONTRIBUTION_CREATED_TOTAL = Counter(
    "memory_contribution_created_total",
    "Total append-only family memory contributions created.",
    labelnames=("role",),
)
MEMORY_CLARIFICATION_TOTAL = Counter(
    "memory_clarification_total",
    "Total family memory clarification lifecycle events.",
    labelnames=("status",),
)
MEMORY_ENRICHMENT_STATUS_TOTAL = Counter(
    "memory_enrichment_status_total",
    "Total family memory enrichment status events.",
    labelnames=("status",),
)
MEMORY_OWNER_REVIEW_TOTAL = Counter(
    "memory_owner_review_total",
    "Total explicit owner review actions for family memories.",
    labelnames=("action",),
)
MEMORY_DISPUTE_TOTAL = Counter(
    "memory_dispute_total",
    "Total family memory dispute lifecycle events.",
    labelnames=("result",),
)
MEMORY_PROMOTION_BLOCKED_TOTAL = Counter(
    "memory_promotion_blocked_total",
    "Total family memory promotion checks blocked by eligibility policy.",
    labelnames=("reason",),
)
MEMORY_ENRICHMENT_CURRENT = Gauge(
    "memory_enrichment_current",
    "Current family memory candidates by durable enrichment status.",
    labelnames=("status",),
)
MEMORY_DISPUTES_CURRENT = Gauge(
    "memory_disputes_current",
    "Current family memory candidates by durable dispute status.",
    labelnames=("status",),
)
CONTENT_TRANSLATION_TOTAL = Counter(
    "content_translation_total",
    "Total backend content translation attempts (Task 64.5.1 bilingual workflow).",
    labelnames=("source_language", "target_language", "result"),
)
CONTENT_TRANSLATION_DURATION_SECONDS = Histogram(
    "content_translation_duration_seconds",
    "Backend content translation attempt duration in seconds.",
    labelnames=("source_language", "target_language"),
)
CONTENT_TRANSLATION_STATUS_CURRENT = Gauge(
    "content_translation_status_current",
    "Current count of translatable-field rows by translation status.",
    labelnames=("status",),
)
CONTENT_TRANSLATION_RETRY_TOTAL = Counter(
    "content_translation_retry_total",
    "Total explicit content translation retries.",
    labelnames=("result",),
)

AVATAR_EVAL_RUNS_TOTAL = Counter(
    "avatar_eval_runs_total",
    "Total avatar answer-quality evaluation runs.",
    labelnames=("result",),
)
AVATAR_EVAL_CASES_TOTAL = Counter(
    "avatar_eval_cases_total",
    "Total avatar answer-quality evaluation case executions.",
    labelnames=("category", "result"),
)
AVATAR_EVAL_FAILURE_TOTAL = Counter(
    "avatar_eval_failure_total",
    "Total avatar answer-quality evaluation failures by taxonomy type.",
    labelnames=("failure_type",),
)
AVATAR_EVAL_DURATION_SECONDS = Histogram(
    "avatar_eval_duration_seconds",
    "Avatar answer-quality evaluation case duration in seconds.",
)
AVATAR_EVAL_PERSONA_CONSISTENCY_RATIO = Gauge(
    "avatar_eval_persona_consistency_ratio",
    "Last avatar answer-quality evaluation persona consistency ratio.",
)
AVATAR_EVAL_UNSUPPORTED_DETAIL_RATIO = Gauge(
    "avatar_eval_unsupported_detail_ratio",
    "Last avatar answer-quality evaluation unsupported detail ratio.",
)
AVATAR_EVAL_OVER_REFUSAL_RATIO = Gauge(
    "avatar_eval_over_refusal_ratio",
    "Last avatar answer-quality evaluation over-refusal ratio.",
)
AVATAR_EVAL_QUALITY_GATE_TOTAL = Counter(
    "avatar_eval_quality_gate_total",
    "Total avatar answer-quality evaluation runs by overall quality-gate result.",
    labelnames=("result",),
)
AVATAR_EVAL_PROFILE_ISOLATION_TOTAL = Counter(
    "avatar_eval_profile_isolation_total",
    "Total avatar answer-quality evaluation runs by profile-isolation gate result.",
    labelnames=("result",),
)
AVATAR_EVAL_CORRECTED_MEMORY_TOTAL = Counter(
    "avatar_eval_corrected_memory_total",
    "Total avatar answer-quality evaluation runs by corrected-memory-preference gate result.",
    labelnames=("result",),
)
AVATAR_EVAL_PERSPECTIVE_TOTAL = Counter(
    "avatar_eval_perspective_total",
    "Total avatar answer-quality evaluation runs by perspective-preservation gate result.",
    labelnames=("result",),
)
AVATAR_MEMORY_QUERY_INTENT_TOTAL = Counter(
    "avatar_memory_query_intent_total",
    "Total avatar learned-memory chat turns by classified query intent.",
    labelnames=("intent",),
)
AVATAR_CORRECTED_MEMORY_RESOLUTION_TOTAL = Counter(
    "avatar_corrected_memory_resolution_total",
    "Total corrected-memory-intent turns by whether a verified learned memory was found and used.",
    labelnames=("result",),
)

# --- Task 65.10: cross-pipeline evidence prioritization --------------------
# Every label below is a small closed set (a bounded RAG source_type enum,
# true/false, or a fixed drop-reason enum) - never a chunk/candidate/
# promotion/profile/user id and never memory or question text.
EVIDENCE_PRIORITIZATION_CANDIDATE_COUNT = Histogram(
    "evidence_prioritization_candidate_count",
    "Number of already-eligible evidence candidates entering cross-pipeline prioritization.",
    buckets=(0, 1, 2, 3, 5, 10, 20, 50),
)
EVIDENCE_PRIORITIZATION_SELECTED_COUNT = Histogram(
    "evidence_prioritization_selected_count",
    "Number of evidence items selected by cross-pipeline prioritization after the context cap.",
    buckets=(0, 1, 2, 3, 5, 10),
)
EVIDENCE_PRIORITIZATION_DROPPED_TOTAL = Counter(
    "evidence_prioritization_dropped_total",
    "Total evidence items dropped during cross-pipeline prioritization, by safe drop-reason category.",
    labelnames=("reason",),
)
EVIDENCE_PRIORITIZATION_VERIFIED_SELECTED_TOTAL = Counter(
    "evidence_prioritization_verified_selected_total",
    "Total selected evidence items by whether they were recognized as verified (any pipeline).",
    labelnames=("verified",),
)
EVIDENCE_PRIORITIZATION_SOURCE_TYPE_SELECTED_TOTAL = Counter(
    "evidence_prioritization_source_type_selected_total",
    "Total selected evidence items by source_type (bounded RagSource source_type enum).",
    labelnames=("source_type",),
)

# --- Task 65.6: context-aware AI Biographer -------------------------------
# Every label below is a small closed set (topic/coverage-state/result/
# generation-mode/reason/locale) - never a profile/user/question/candidate
# id and never raw question text, matching the AI-cost label convention
# below (see `_AI_COST_FEATURES` and the comment at line ~730).
BIOGRAPHER_QUESTIONS_TOTAL = Counter(
    "biographer_questions_total",
    "Total AI Biographer questions generated, by locale/topic/result/generation_mode.",
    labelnames=("locale", "topic", "result", "generation_mode"),
)
BIOGRAPHER_BLOCKED_TOTAL = Counter(
    "biographer_blocked_total",
    "Total AI Biographer question requests blocked before generation, by reason.",
    labelnames=("reason", "locale"),
)
BIOGRAPHER_TOPIC_SELECTION_TOTAL = Counter(
    "biographer_topic_selection_total",
    "Total AI Biographer topic selections, by topic and coverage state.",
    labelnames=("topic", "coverage_state"),
)
BIOGRAPHER_DUPLICATE_PREVENTED_TOTAL = Counter(
    "biographer_duplicate_prevented_total",
    "Total AI Biographer generated questions rejected by duplicate/known-answer validation.",
    labelnames=("reason", "locale"),
)
BIOGRAPHER_CONTEXT_SOURCES = Histogram(
    "biographer_context_sources",
    "Verified source count used to build one Biographer question's context, by topic.",
    labelnames=("topic",),
    buckets=(0, 1, 2, 3, 5, 8, 13),
)
BIOGRAPHER_GENERATION_DURATION_SECONDS = Histogram(
    "biographer_generation_duration_seconds",
    "Duration of one Biographer question-generation request in seconds, by locale and result.",
    labelnames=("locale", "result"),
)
BIOGRAPHER_FALLBACK_TOTAL = Counter(
    "biographer_fallback_total",
    "Total AI Biographer requests that used the deterministic fallback question template.",
    labelnames=("reason", "locale"),
)

# --- Task 65.11.1: batched Biographer topic query embeddings --------------
# Structural performance observability for the "one batch model invocation,
# one Qdrant request per new-question request" contract. All of these are
# label-free or bounded-label numeric series: they carry counts and durations
# only, and must NEVER carry topic query text, biography excerpts, generated
# question text, answer/candidate text, names or email addresses.
BIOGRAPHER_TOPIC_QUERY_BATCH_SIZE = Histogram(
    "biographer_topic_query_batch_size",
    "Number of Biographer topic query texts encoded together in one batch model invocation.",
    buckets=(0, 1, 2, 4, 8, 16),
)
BIOGRAPHER_QUERY_MODEL_INVOCATIONS = Histogram(
    "biographer_query_model_invocations",
    "Query-embedding model invocations performed per Biographer new-question request.",
    buckets=(0, 1, 2, 4, 8, 16),
)
BIOGRAPHER_QDRANT_REQUESTS = Histogram(
    "biographer_qdrant_requests",
    "Qdrant round trips performed per Biographer new-question request.",
    buckets=(0, 1, 2, 4, 8, 16),
)
BIOGRAPHER_COVERAGE_RETRIEVAL_DURATION_SECONDS = Histogram(
    "biographer_coverage_retrieval_duration_seconds",
    "Duration of the single batched Biographer coverage retrieval, in seconds.",
)
BIOGRAPHER_SELECTED_TOPIC_HYDRATION_DURATION_SECONDS = Histogram(
    "biographer_selected_topic_hydration_duration_seconds",
    "Duration of materializing the selected Biographer topic's prompt context, in seconds.",
)

_BIOGRAPHER_TOPIC_KEYS = frozenset(
    {"childhood", "family", "education", "work", "relationships", "places", "traditions", "values"}
)
_BIOGRAPHER_COVERAGE_STATES = frozenset(
    {"not_started", "weak", "basic", "rich", "skipped", "postponed", "exhausted"}
)
_BIOGRAPHER_BLOCKED_REASONS = frozenset(
    {
        "biography_missing",
        "biography_not_indexed",
        "biography_stale",
        "indexing_in_progress",
        "permission_denied",
        "active_clarification_exists",
        "candidate_waiting_for_review",
    }
)
_BIOGRAPHER_RESULTS = frozenset({"accepted", "regenerated", "fallback_used", "generation_failed"})
_BIOGRAPHER_GENERATION_MODES = frozenset({"llm_generated", "deterministic_fallback"})
_BIOGRAPHER_DUPLICATE_REASONS = frozenset(
    {"exact_duplicate", "high_lexical_overlap", "same_topic_intent", "known_broad_fact"}
)
_BIOGRAPHER_FALLBACK_REASONS = frozenset(
    {"retrieval_unavailable", "provider_unavailable", "validation_failed_twice"}
)


def normalize_biographer_topic_label(topic: str | None) -> str:
    return topic if topic in _BIOGRAPHER_TOPIC_KEYS else "other"


def normalize_biographer_coverage_state_label(state: str | None) -> str:
    return state if state in _BIOGRAPHER_COVERAGE_STATES else "unknown"


def normalize_biographer_blocked_reason_label(reason: str | None) -> str:
    return reason if reason in _BIOGRAPHER_BLOCKED_REASONS else "other"


def normalize_biographer_result_label(result: str | None) -> str:
    return result if result in _BIOGRAPHER_RESULTS else "unknown"


def normalize_biographer_generation_mode_label(mode: str | None) -> str:
    return mode if mode in _BIOGRAPHER_GENERATION_MODES else "unknown"


def normalize_biographer_duplicate_reason_label(reason: str | None) -> str:
    return reason if reason in _BIOGRAPHER_DUPLICATE_REASONS else "other"


def normalize_biographer_fallback_reason_label(reason: str | None) -> str:
    return reason if reason in _BIOGRAPHER_FALLBACK_REASONS else "other"


def observe_biographer_question(*, locale: str | None, topic: str, result: str, generation_mode: str) -> None:
    BIOGRAPHER_QUESTIONS_TOTAL.labels(
        locale=normalize_ai_locale_label(locale),
        topic=normalize_biographer_topic_label(topic),
        result=normalize_biographer_result_label(result),
        generation_mode=normalize_biographer_generation_mode_label(generation_mode),
    ).inc()


def observe_biographer_blocked(*, reason: str, locale: str | None) -> None:
    BIOGRAPHER_BLOCKED_TOTAL.labels(
        reason=normalize_biographer_blocked_reason_label(reason),
        locale=normalize_ai_locale_label(locale),
    ).inc()


def observe_biographer_topic_selection(*, topic: str, coverage_state: str) -> None:
    BIOGRAPHER_TOPIC_SELECTION_TOTAL.labels(
        topic=normalize_biographer_topic_label(topic),
        coverage_state=normalize_biographer_coverage_state_label(coverage_state),
    ).inc()


def observe_biographer_duplicate_prevented(*, reason: str, locale: str | None) -> None:
    BIOGRAPHER_DUPLICATE_PREVENTED_TOTAL.labels(
        reason=normalize_biographer_duplicate_reason_label(reason),
        locale=normalize_ai_locale_label(locale),
    ).inc()


def observe_biographer_context_sources(*, topic: str, source_count: int) -> None:
    BIOGRAPHER_CONTEXT_SOURCES.labels(topic=normalize_biographer_topic_label(topic)).observe(source_count)


def observe_biographer_generation_duration(*, locale: str | None, result: str, duration_seconds: float) -> None:
    BIOGRAPHER_GENERATION_DURATION_SECONDS.labels(
        locale=normalize_ai_locale_label(locale),
        result=normalize_biographer_result_label(result),
    ).observe(duration_seconds)


def observe_biographer_fallback(*, reason: str, locale: str | None) -> None:
    BIOGRAPHER_FALLBACK_TOTAL.labels(
        reason=normalize_biographer_fallback_reason_label(reason),
        locale=normalize_ai_locale_label(locale),
    ).inc()


def observe_biographer_topic_query_batch(
    *,
    topic_query_batch_size: int,
    model_invocation_count: int,
    qdrant_request_count: int,
    coverage_retrieval_duration_seconds: float,
) -> None:
    """Task 65.11.1 - numeric-only. No query text, no excerpt, no identifier."""

    BIOGRAPHER_TOPIC_QUERY_BATCH_SIZE.observe(max(0, int(topic_query_batch_size)))
    BIOGRAPHER_QUERY_MODEL_INVOCATIONS.observe(max(0, int(model_invocation_count)))
    BIOGRAPHER_QDRANT_REQUESTS.observe(max(0, int(qdrant_request_count)))
    BIOGRAPHER_COVERAGE_RETRIEVAL_DURATION_SECONDS.observe(max(0.0, float(coverage_retrieval_duration_seconds)))


def observe_biographer_selected_topic_hydration(*, duration_seconds: float) -> None:
    BIOGRAPHER_SELECTED_TOPIC_HYDRATION_DURATION_SECONDS.observe(max(0.0, float(duration_seconds)))


# --- Task 65.7: authenticated workspace reliability -----------------------
# Every label below is a small closed set - never a user/profile/session/
# candidate/conversation id, never a raw status message.
BROWSER_SESSION_OPERATIONS_TOTAL = Counter(
    "eternal_world_browser_session_operations_total",
    "Total browser session lifecycle operations, by operation and result.",
    labelnames=("operation", "result"),
)
PROFILE_UPDATES_TOTAL = Counter(
    "eternal_world_profile_updates_total",
    "Total memorial/profile metadata update attempts, by result.",
    labelnames=("result",),
)
BIOGRAPHER_RESUME_TOTAL = Counter(
    "eternal_world_biographer_resume_total",
    "Total Biographer resume-state loads, by resolved state and result.",
    labelnames=("state", "result"),
)
BIOGRAPHER_ANSWERS_TOTAL = Counter(
    "eternal_world_biographer_answers_total",
    "Total Biographer direct-answer submissions, by result and locale.",
    labelnames=("result", "locale"),
)
CHAT_OPERATIONS_TOTAL = Counter(
    "eternal_world_chat_operations_total",
    "Total Chat operations (send/reset/restore), by operation and result.",
    labelnames=("operation", "result"),
)
CHAT_REDIS_OPERATIONS_TOTAL = Counter(
    "eternal_world_chat_redis_operations_total",
    "Total Chat Redis snapshot operations, by operation and result.",
    labelnames=("operation", "result"),
)
REVIEW_ACTIONS_TOTAL = Counter(
    "eternal_world_review_actions_total",
    "Total owner-review actions on memory candidates, by action and result.",
    labelnames=("action", "result"),
)
MEMORY_INDEX_OPERATIONS_TOTAL = Counter(
    "eternal_world_memory_index_operations_total",
    "Total explicit memory indexing operations, by result.",
    labelnames=("result",),
)
LOCALIZATION_FALLBACK_TOTAL = Counter(
    "eternal_world_localization_fallback_total",
    "Total times a raw/unknown enum value had to be shown via the generic localization fallback.",
    labelnames=("locale", "category"),
)

_BROWSER_SESSION_OPERATIONS = frozenset({"create", "resume", "revoke"})
_BROWSER_SESSION_RESULTS = frozenset({"success", "expired", "invalid", "error"})
_PROFILE_UPDATE_RESULTS = frozenset({"success", "validation_error", "permission_denied", "error"})
_BIOGRAPHER_RESUME_STATES = frozenset(
    {
        "biography_not_indexed",
        "biography_indexing",
        "question_ready",
        "answer_submitting",
        "candidate_ready_for_review",
        "candidate_needs_owner_action",
        "candidate_pending_index",
        "candidate_indexed",
        # Task 65.10.5 - a permanently failed per-candidate indexing job,
        # tracked distinctly rather than falling into the generic "other"
        # bucket `_normalize_choice` uses for anything unrecognized.
        "candidate_indexing_failed",
        "clarification_pending",
        "generation_failed",
        "blocked",
    }
)
_CHAT_OPERATIONS = frozenset({"send", "restore", "reset"})
_CHAT_REDIS_OPERATIONS = frozenset({"snapshot_restored", "snapshot_rebuilt", "snapshot_written", "reset"})
_REVIEW_ACTIONS = frozenset(
    {"confirm", "edit_and_confirm", "reject", "request_more_details", "mark_disputed", "approve_multiple_perspectives"}
)
_LOCALIZATION_CATEGORIES = frozenset(
    {"privacy_scope", "role", "candidate_status", "dispute_status", "contribution_type", "clarification_status", "history_event", "invitation_status", "job_status"}
)


def _normalize_choice(value: str | None, *, allowed: frozenset[str], fallback: str = "other") -> str:
    return value if value in allowed else fallback


def observe_browser_session_operation(*, operation: str, result: str) -> None:
    BROWSER_SESSION_OPERATIONS_TOTAL.labels(
        operation=_normalize_choice(operation, allowed=_BROWSER_SESSION_OPERATIONS),
        result=_normalize_choice(result, allowed=_BROWSER_SESSION_RESULTS, fallback="error"),
    ).inc()


def observe_profile_update(*, result: str) -> None:
    PROFILE_UPDATES_TOTAL.labels(result=_normalize_choice(result, allowed=_PROFILE_UPDATE_RESULTS, fallback="error")).inc()


def observe_biographer_resume(*, state: str, result: str) -> None:
    BIOGRAPHER_RESUME_TOTAL.labels(
        state=_normalize_choice(state, allowed=_BIOGRAPHER_RESUME_STATES, fallback="other"),
        result=_normalize_choice(result, allowed=frozenset({"success", "error"}), fallback="error"),
    ).inc()


def observe_biographer_direct_answer(*, result: str, locale: str | None) -> None:
    BIOGRAPHER_ANSWERS_TOTAL.labels(
        result=_normalize_choice(result, allowed=frozenset({"accepted", "validation_error", "error"}), fallback="error"),
        locale=normalize_ai_locale_label(locale),
    ).inc()


def observe_chat_operation(*, operation: str, result: str) -> None:
    CHAT_OPERATIONS_TOTAL.labels(
        operation=_normalize_choice(operation, allowed=_CHAT_OPERATIONS),
        result=_normalize_choice(result, allowed=frozenset({"success", "error"}), fallback="error"),
    ).inc()


def observe_chat_redis_operation(*, operation: str, result: str) -> None:
    CHAT_REDIS_OPERATIONS_TOTAL.labels(
        operation=_normalize_choice(operation, allowed=_CHAT_REDIS_OPERATIONS),
        result=_normalize_choice(result, allowed=frozenset({"success", "error"}), fallback="error"),
    ).inc()


def observe_review_action(*, action: str, result: str) -> None:
    REVIEW_ACTIONS_TOTAL.labels(
        action=_normalize_choice(action, allowed=_REVIEW_ACTIONS),
        result=_normalize_choice(result, allowed=frozenset({"success", "error"}), fallback="error"),
    ).inc()


def observe_memory_index_operation(*, result: str) -> None:
    MEMORY_INDEX_OPERATIONS_TOTAL.labels(
        result=_normalize_choice(result, allowed=frozenset({"indexed", "already_indexed", "error"}), fallback="error")
    ).inc()


def observe_localization_fallback(*, locale: str | None, category: str) -> None:
    LOCALIZATION_FALLBACK_TOTAL.labels(
        locale=normalize_ai_locale_label(locale),
        category=_normalize_choice(category, allowed=_LOCALIZATION_CATEGORIES, fallback="other"),
    ).inc()


_AVATAR_EVAL_GATE_RESULTS = frozenset({"pass", "fail"})
_AVATAR_MEMORY_QUERY_INTENTS = frozenset(
    {
        "direct_factual_memory",
        "corrected_memory_fact",
        "correction_history",
        "multiple_perspective_question",
        "unknown_or_ambiguous",
    }
)
_AVATAR_CORRECTED_MEMORY_RESOLUTIONS = frozenset({"resolved", "unresolved"})

_MEMORY_INDEX_RESULTS = frozenset({"indexed", "failed", "skipped"})
_MEMORY_PROMOTION_STATUSES = ("pending_index", "indexed", "failed", "cancelled")
_FAMILY_ACTOR_ROLES = frozenset({"owner", "contributor", "trusted_reviewer", "system"})
_CLARIFICATION_STATUSES = frozenset({"pending", "answered", "skipped", "cancelled"})
_ENRICHMENT_STATUSES = ("draft", "collecting_details", "ready_for_owner_review")
_OWNER_REVIEW_ACTIONS = frozenset({
    "confirm",
    "edit_and_confirm",
    "reject",
    "request_more_details",
    "mark_disputed",
    "approve_multiple_perspectives",
})
_DISPUTE_RESULTS = ("none", "disputed", "resolved")
_PROMOTION_BLOCK_REASONS = frozenset({
    "not_approved",
    "collecting_details",
    "incomplete",
    "unresolved_clarification",
    "privacy_scope",
    "disputed",
    "unauthorized_reviewer",
    "russian_translation_missing",
    "russian_translation_failed",
    "russian_translation_stale",
})
_CONTENT_TRANSLATION_LANGUAGE_PAIRS = frozenset(
    {
        "cs_ru",
        "ru_cs",
        "cs_en",
        "en_cs",
        "ru_en",
        "en_ru",
    }
)
_CONTENT_TRANSLATION_RESULTS = frozenset({"success", "failed"})
_CONTENT_TRANSLATION_STATUSES = frozenset(
    {"pending", "translated", "failed", "stale", "human_reviewed"}
)
_AVATAR_EVAL_RESULTS = frozenset({"passed", "failed"})
_AVATAR_EVAL_CATEGORIES = frozenset({
    "original_seeded_memory",
    "learned_indexed_memory",
    "owner_corrected_memory",
    "multiple_perspectives",
    "pending_unindexed_memory",
    "rejected_memory",
    "private_memory_blocked",
    "unknown_factual_question",
    "emotional_persona_question",
    "sensitive_subject",
    "repeat_answer_stability",
    "profile_isolation",
})
_AVATAR_EVAL_FAILURE_TYPES = frozenset({
    "retrieval_failure",
    "profile_contamination",
    "evidence_present_but_ignored",
    "unsupported_detail",
    "over_refusal",
    "wrong_corrected_version",
    "perspective_collapsed",
    "persona_cold_or_technical",
    "persona_inconsistent",
    "incorrect_lack_of_evidence",
    "guard_regression",
    "evaluator_failure",
    "runtime_failure",
})


def normalize_http_route_label(route_path: str | None) -> str:
    normalized_route = (route_path or "").strip()
    return normalized_route or "__unmatched__"


def normalize_boolean_label(value: bool | None) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    return "unknown"


def normalize_guard_reason_label(reason: str | None) -> str:
    normalized_reason = (reason or "").strip()
    return _NORMALIZED_GUARD_REASONS.get(normalized_reason, "other")


def normalize_top_k_label(top_k: int) -> str:
    return str(max(0, int(top_k)))


def normalize_brain_provider_label(provider_name: str | None) -> str:
    normalized_provider = (provider_name or "").strip().lower()
    return _NORMALIZED_BRAIN_PROVIDERS.get(normalized_provider, "other")


def normalize_brain_model_label(model_name: str | None) -> str:
    normalized_model = (model_name or "").strip()
    return normalized_model or "unset"


# --- Task 65.9: Scalable Async Job Platform and Self-Healing Embedding ----
# Workers. Every label below is a small closed set (queue, job_type,
# result, provider/model code, safe error category, provider state) -
# never a user id, profile id, memorial id, contribution/promotion id, or
# raw exception message (Part W's explicit forbidden-label list).

ASYNC_JOBS_CREATED_TOTAL = Counter(
    "async_jobs_created_total",
    "Total async job platform jobs created.",
    labelnames=("queue", "job_type"),
)
ASYNC_JOBS_COMPLETED_TOTAL = Counter(
    "async_jobs_completed_total",
    "Total async job platform jobs that completed successfully.",
    labelnames=("queue", "job_type"),
)
ASYNC_JOBS_FAILED_TOTAL = Counter(
    "async_jobs_failed_total",
    "Total async job platform jobs that failed permanently.",
    labelnames=("queue", "job_type", "safe_error_category"),
)
ASYNC_JOBS_RETRY_TOTAL = Counter(
    "async_jobs_retry_total",
    "Total async job platform bounded infrastructure retries.",
    labelnames=("queue", "job_type"),
)
ASYNC_JOBS_DUPLICATE_DELIVERY_TOTAL = Counter(
    "async_jobs_duplicate_delivery_total",
    "Total times a job task was delivered/executed more than once (converged safely).",
    labelnames=("queue", "job_type"),
)
ASYNC_JOBS_STALE_RECOVERED_TOTAL = Counter(
    "async_jobs_stale_recovered_total",
    "Total jobs recovered from a stale/crashed-worker processing state.",
    labelnames=("queue",),
)
ASYNC_JOB_DURATION_SECONDS = Histogram(
    "async_job_duration_seconds",
    "Async job platform job duration in seconds, from started_at to a terminal state.",
    labelnames=("queue", "job_type", "result"),
)
ASYNC_QUEUE_DEPTH = Gauge(
    "async_queue_depth",
    "Current number of active (non-terminal) jobs by queue.",
    labelnames=("queue",),
)
ASYNC_OLDEST_JOB_AGE_SECONDS = Gauge(
    "async_oldest_job_age_seconds",
    "Age in seconds of the oldest still-active job by queue.",
    labelnames=("queue",),
)
OUTBOX_PENDING_TOTAL = Gauge(
    "outbox_pending_total",
    "Current number of pending (not yet published) transactional outbox rows.",
)
OUTBOX_PUBLISH_FAILURE_TOTAL = Counter(
    "outbox_publish_failure_total",
    "Total transactional outbox publish attempts that failed (broker unreachable).",
)
ASYNC_QUEUE_METRICS_REFRESH_FAILURE_TOTAL = Counter(
    "async_queue_metrics_refresh_failure_total",
    "Total periodic async queue/job metric refresh attempts that failed (e.g. database unavailable).",
)

EMBEDDING_PROVIDER_HEALTH = Gauge(
    "embedding_provider_health",
    "Current embedding provider state (1 for the currently-set state, 0 otherwise).",
    labelnames=("model_code", "state"),
)
EMBEDDING_PROVIDER_INITIALIZATION_TOTAL = Counter(
    "embedding_provider_initialization_total",
    "Total embedding provider initialization attempts, by result.",
    labelnames=("model_code", "result"),
)
EMBEDDING_PROVIDER_INITIALIZATION_FAILURE_TOTAL = Counter(
    "embedding_provider_initialization_failure_total",
    "Total embedding provider initialization failures.",
    labelnames=("model_code",),
)
EMBEDDING_PROVIDER_META_PARAMETER_TOTAL = Counter(
    "embedding_provider_meta_parameter_total",
    "Total times a meta-device parameter/buffer/output was detected on the embedding provider.",
    labelnames=("model_code",),
)
EMBEDDING_PROVIDER_RELOAD_TOTAL = Counter(
    "embedding_provider_reload_total",
    "Total embedding provider reload attempts (self-healing recovery).",
    labelnames=("model_code",),
)
EMBEDDING_PROVIDER_PROBE_FAILURE_TOTAL = Counter(
    "embedding_provider_probe_failure_total",
    "Total embedding provider integrity probe failures, by safe reason code.",
    labelnames=("model_code", "reason"),
)
EMBEDDING_PROVIDER_RECOVERY_TOTAL = Counter(
    "embedding_provider_recovery_total",
    "Total bounded provider-recovery attempts recorded on a job, by outcome.",
    labelnames=("outcome",),
)
EMBEDDING_WORKER_RECYCLE_REQUEST_TOTAL = Counter(
    "embedding_worker_recycle_request_total",
    "Total times a job requested a fresh embedding-worker process/container.",
)
EMBEDDING_INDEXING_FINAL_FAILURE_TOTAL = Counter(
    "embedding_indexing_final_failure_total",
    "Total jobs that reached permanent failure after the bounded self-healing policy was exhausted.",
)
EMBEDDING_LAST_SUCCESS_TIMESTAMP = Gauge(
    "embedding_last_success_timestamp",
    "Unix timestamp of the last successful embedding provider probe/encode, by model code.",
    labelnames=("model_code",),
)

_PROVIDER_STATES = frozenset(
    {"never_initialized", "initializing", "healthy", "degraded", "recovery_in_progress", "failed"}
)
_PROVIDER_RECOVERY_OUTCOMES = frozenset({"reloaded", "fresh_process_requested", "permanent_failure"})
_SAFE_ERROR_CATEGORIES = frozenset(
    {
        "provider_corrupt",
        "provider_initialization_failed",
        "invalid_embedding_output",
        "temporary_broker_failure",
        "temporary_database_failure",
        "temporary_qdrant_failure",
        "permanent_qdrant_validation_failure",
        "invalid_domain_state",
        "authorization_failure",
        "resource_not_found",
        "content_validation_failure",
        "worker_lost",
        "unknown_internal_failure",
    }
)


def _normalize_queue_label(queue: str | None) -> str:
    normalized = (queue or "").strip().lower()
    return normalized or "unknown"


def _normalize_safe_error_category_label(category: str | None) -> str:
    normalized = (category or "").strip().lower()
    return normalized if normalized in _SAFE_ERROR_CATEGORIES else "unknown_internal_failure"


def observe_async_job_created(*, queue: str | None, job_type: str) -> None:
    ASYNC_JOBS_CREATED_TOTAL.labels(_normalize_queue_label(queue), job_type).inc()


def observe_async_job_completed(*, queue: str | None, job_type: str, duration_seconds: float) -> None:
    normalized_queue = _normalize_queue_label(queue)
    ASYNC_JOBS_COMPLETED_TOTAL.labels(normalized_queue, job_type).inc()
    ASYNC_JOB_DURATION_SECONDS.labels(normalized_queue, job_type, "succeeded").observe(max(0.0, duration_seconds))


def observe_async_job_failed(
    *, queue: str | None, job_type: str, safe_error_category: str | None, duration_seconds: float
) -> None:
    normalized_queue = _normalize_queue_label(queue)
    normalized_category = _normalize_safe_error_category_label(safe_error_category)
    ASYNC_JOBS_FAILED_TOTAL.labels(normalized_queue, job_type, normalized_category).inc()
    ASYNC_JOB_DURATION_SECONDS.labels(normalized_queue, job_type, "failed").observe(max(0.0, duration_seconds))
    if normalized_category == "provider_corrupt":
        EMBEDDING_INDEXING_FINAL_FAILURE_TOTAL.inc()


def observe_async_job_retry(*, queue: str | None, job_type: str) -> None:
    ASYNC_JOBS_RETRY_TOTAL.labels(_normalize_queue_label(queue), job_type).inc()


def observe_async_job_duplicate_delivery(*, queue: str | None, job_type: str) -> None:
    ASYNC_JOBS_DUPLICATE_DELIVERY_TOTAL.labels(_normalize_queue_label(queue), job_type).inc()


def observe_async_job_stale_recovered(*, queue: str | None) -> None:
    ASYNC_JOBS_STALE_RECOVERED_TOTAL.labels(_normalize_queue_label(queue)).inc()


def set_async_queue_depth(*, queue: str, depth: int) -> None:
    ASYNC_QUEUE_DEPTH.labels(_normalize_queue_label(queue)).set(max(0, int(depth)))


def set_async_oldest_job_age_seconds(*, queue: str, age_seconds: float) -> None:
    ASYNC_OLDEST_JOB_AGE_SECONDS.labels(_normalize_queue_label(queue)).set(max(0.0, age_seconds))


def set_outbox_pending_total(*, count: int) -> None:
    OUTBOX_PENDING_TOTAL.set(max(0, int(count)))


def observe_outbox_publish_failure() -> None:
    OUTBOX_PUBLISH_FAILURE_TOTAL.inc()


def observe_async_queue_metrics_refresh_failure() -> None:
    ASYNC_QUEUE_METRICS_REFRESH_FAILURE_TOTAL.inc()


def set_embedding_provider_health(*, model_code: str, state: str) -> None:
    normalized_state = state if state in _PROVIDER_STATES else "failed"
    for candidate_state in _PROVIDER_STATES:
        EMBEDDING_PROVIDER_HEALTH.labels(model_code, candidate_state).set(
            1 if candidate_state == normalized_state else 0
        )
    if normalized_state == "healthy":
        import time

        EMBEDDING_LAST_SUCCESS_TIMESTAMP.labels(model_code).set(time.time())


def observe_embedding_provider_initialization(*, model_code: str, result: str) -> None:
    normalized_result = result if result in {"success", "failure"} else "failure"
    EMBEDDING_PROVIDER_INITIALIZATION_TOTAL.labels(model_code, normalized_result).inc()
    if normalized_result == "failure":
        EMBEDDING_PROVIDER_INITIALIZATION_FAILURE_TOTAL.labels(model_code).inc()


def observe_embedding_provider_reload(*, model_code: str) -> None:
    EMBEDDING_PROVIDER_RELOAD_TOTAL.labels(model_code).inc()


def observe_embedding_provider_probe_failure(*, model_code: str, reason: str) -> None:
    normalized_reason = (reason or "unknown").strip().lower() or "unknown"
    EMBEDDING_PROVIDER_PROBE_FAILURE_TOTAL.labels(model_code, normalized_reason).inc()
    if "meta" in normalized_reason:
        EMBEDDING_PROVIDER_META_PARAMETER_TOTAL.labels(model_code).inc()


def observe_embedding_provider_recovery(*, outcome: str) -> None:
    normalized_outcome = outcome if outcome in _PROVIDER_RECOVERY_OUTCOMES else "permanent_failure"
    EMBEDDING_PROVIDER_RECOVERY_TOTAL.labels(normalized_outcome).inc()


def observe_embedding_worker_recycle_request() -> None:
    EMBEDDING_WORKER_RECYCLE_REQUEST_TOTAL.inc()


def build_metrics_response() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


def observe_http_request(*, method: str, route: str | None, status_code: int, duration_seconds: float) -> None:
    labels = (
        method.upper(),
        normalize_http_route_label(route),
        str(int(status_code)),
    )
    HTTP_REQUESTS_TOTAL.labels(*labels).inc()
    HTTP_REQUEST_DURATION_SECONDS.labels(*labels).observe(duration_seconds)
    if int(status_code) >= 400:
        HTTP_ERRORS_TOTAL.labels(*labels).inc()


def observe_fa_chat_success(
    *,
    duration_seconds: float,
    retrieval_used: bool,
    guard_applied: bool,
    guard_reason: str | None,
    lack_of_evidence: bool,
    debug: bool,
) -> None:
    labels = (
        "success",
        normalize_boolean_label(retrieval_used),
        normalize_boolean_label(guard_applied),
        normalize_guard_reason_label(guard_reason),
        normalize_boolean_label(debug),
    )
    FA_CHAT_REQUESTS_TOTAL.labels(*labels).inc()
    FA_CHAT_DURATION_SECONDS.labels(*labels).observe(duration_seconds)
    if lack_of_evidence:
        FA_CHAT_LACK_OF_EVIDENCE_TOTAL.labels(normalize_boolean_label(debug)).inc()
    if guard_applied:
        FA_CHAT_GUARD_APPLIED_TOTAL.labels(
            normalize_guard_reason_label(guard_reason),
            normalize_boolean_label(debug),
        ).inc()


def observe_fa_chat_error(*, outcome: str, debug: bool, duration_seconds: float) -> None:
    labels = (
        outcome,
        "unknown",
        "unknown",
        "none",
        normalize_boolean_label(debug),
    )
    FA_CHAT_REQUESTS_TOTAL.labels(*labels).inc()
    FA_CHAT_DURATION_SECONDS.labels(*labels).observe(duration_seconds)
    FA_CHAT_ERRORS_TOTAL.labels(outcome, normalize_boolean_label(debug)).inc()


def observe_rag_retrieval_success(
    *,
    retrieval_mode: str,
    top_k: int,
    duration_seconds: float,
    retrieved_chunk_count: int,
) -> None:
    labels = (retrieval_mode, normalize_top_k_label(top_k))
    RAG_RETRIEVAL_DURATION_SECONDS.labels(*labels).observe(duration_seconds)
    RAG_RETRIEVED_CHUNKS_COUNT.labels(*labels).observe(max(0, int(retrieved_chunk_count)))


def observe_rag_retrieval_error(*, retrieval_mode: str, top_k: int) -> None:
    RAG_RETRIEVAL_ERRORS_TOTAL.labels(retrieval_mode, normalize_top_k_label(top_k)).inc()


def observe_embedding_cache_summary(
    *,
    provider_code: str,
    input_type: str,
    mode: str,
    hits: int,
    misses: int,
    writes: int,
    errors: int,
) -> None:
    labels = (provider_code, input_type, mode)
    if hits > 0:
        EMBEDDING_CACHE_HITS_TOTAL.labels(*labels).inc(hits)
    if misses > 0:
        EMBEDDING_CACHE_MISSES_TOTAL.labels(*labels).inc(misses)
    if writes > 0:
        EMBEDDING_CACHE_WRITES_TOTAL.labels(*labels).inc(writes)
    if errors > 0:
        EMBEDDING_CACHE_ERRORS_TOTAL.labels(*labels).inc(errors)


def observe_brain_answer_success(
    *,
    provider: str | None,
    model: str | None,
    duration_seconds: float,
) -> None:
    BRAIN_ANSWER_DURATION_SECONDS.labels(
        normalize_brain_provider_label(provider),
        normalize_brain_model_label(model),
    ).observe(duration_seconds)


def observe_brain_answer_error(*, provider: str | None, model: str | None) -> None:
    BRAIN_ANSWER_ERRORS_TOTAL.labels(
        normalize_brain_provider_label(provider),
        normalize_brain_model_label(model),
    ).inc()


def observe_memory_candidate_created(*, persisted: bool, status: str) -> None:
    MEMORY_CANDIDATE_CREATED_TOTAL.labels(
        normalize_boolean_label(persisted),
        status.strip().lower() or "unknown",
    ).inc()


def observe_memory_candidate_reviewed(*, status: str) -> None:
    MEMORY_CANDIDATE_REVIEWED_TOTAL.labels(status.strip().lower() or "unknown").inc()


def observe_memory_promotion_created() -> None:
    MEMORY_PROMOTION_CREATED_TOTAL.inc()


def observe_memory_promotion_status(*, status: str) -> None:
    MEMORY_PROMOTION_STATUS_TOTAL.labels(status.strip().lower() or "unknown").inc()


def observe_memory_indexing_started() -> None:
    MEMORY_INDEXING_STARTED_TOTAL.inc()


def observe_memory_indexing_finished(*, result: str, duration_seconds: float) -> None:
    normalized_result = result.strip().lower()
    if normalized_result not in _MEMORY_INDEX_RESULTS:
        normalized_result = "other"
    if normalized_result == "failed":
        MEMORY_INDEXING_FAILED_TOTAL.inc()
    else:
        MEMORY_INDEXING_COMPLETED_TOTAL.inc()
    MEMORY_INDEXING_DURATION_SECONDS.labels(normalized_result).observe(max(0.0, duration_seconds))
    MEMORY_PROMOTION_INDEX_STATUS_TOTAL.labels(normalized_result).inc()


def set_memory_promotions_current(*, counts_by_status: dict[str, int]) -> None:
    for status in _MEMORY_PROMOTION_STATUSES:
        MEMORY_PROMOTIONS_CURRENT.labels(status).set(max(0, int(counts_by_status.get(status, 0))))


def observe_memory_contribution_created(*, role: str) -> None:
    normalized = role.strip().lower()
    MEMORY_CONTRIBUTION_CREATED_TOTAL.labels(
        normalized if normalized in _FAMILY_ACTOR_ROLES else "other"
    ).inc()


def observe_memory_clarification(*, status: str) -> None:
    normalized = status.strip().lower()
    MEMORY_CLARIFICATION_TOTAL.labels(
        normalized if normalized in _CLARIFICATION_STATUSES else "other"
    ).inc()


def observe_memory_enrichment_status(*, status: str) -> None:
    normalized = status.strip().lower()
    MEMORY_ENRICHMENT_STATUS_TOTAL.labels(
        normalized if normalized in _ENRICHMENT_STATUSES else "other"
    ).inc()


def observe_memory_owner_review(*, action: str) -> None:
    normalized = action.strip().lower()
    MEMORY_OWNER_REVIEW_TOTAL.labels(
        normalized if normalized in _OWNER_REVIEW_ACTIONS else "other"
    ).inc()


def observe_memory_dispute(*, result: str) -> None:
    normalized = result.strip().lower()
    MEMORY_DISPUTE_TOTAL.labels(
        normalized if normalized in _DISPUTE_RESULTS else "other"
    ).inc()


def observe_memory_promotion_blocked(*, reason: str) -> None:
    normalized = reason.strip().lower()
    MEMORY_PROMOTION_BLOCKED_TOTAL.labels(
        normalized if normalized in _PROMOTION_BLOCK_REASONS else "other"
    ).inc()


def _normalize_content_translation_language_pair(*, source_language: str, target_language: str) -> tuple[str, str]:
    pair_key = f"{source_language.strip().lower()}_{target_language.strip().lower()}"
    if pair_key not in _CONTENT_TRANSLATION_LANGUAGE_PAIRS:
        return "other", "other"
    return source_language.strip().lower(), target_language.strip().lower()


def observe_content_translation_attempt(
    *,
    source_language: str,
    target_language: str,
    result: str,
    duration_seconds: float,
) -> None:
    normalized_source, normalized_target = _normalize_content_translation_language_pair(
        source_language=source_language, target_language=target_language
    )
    normalized_result = result.strip().lower()
    if normalized_result not in _CONTENT_TRANSLATION_RESULTS:
        normalized_result = "other"
    CONTENT_TRANSLATION_TOTAL.labels(normalized_source, normalized_target, normalized_result).inc()
    CONTENT_TRANSLATION_DURATION_SECONDS.labels(normalized_source, normalized_target).observe(
        max(0.0, duration_seconds)
    )


def observe_content_translation_retry(*, result: str) -> None:
    normalized_result = result.strip().lower()
    CONTENT_TRANSLATION_RETRY_TOTAL.labels(
        normalized_result if normalized_result in _CONTENT_TRANSLATION_RESULTS else "other"
    ).inc()


def set_content_translation_status_current(*, counts_by_status: dict[str, int]) -> None:
    for status in _CONTENT_TRANSLATION_STATUSES:
        CONTENT_TRANSLATION_STATUS_CURRENT.labels(status).set(max(0, int(counts_by_status.get(status, 0))))


def set_memory_enrichment_current(
    *,
    counts_by_status: dict[str, int],
    disputes_by_status: dict[str, int],
) -> None:
    for status in _ENRICHMENT_STATUSES:
        MEMORY_ENRICHMENT_CURRENT.labels(status).set(
            max(0, int(counts_by_status.get(status, 0)))
        )
    for status in _DISPUTE_RESULTS:
        MEMORY_DISPUTES_CURRENT.labels(status).set(
            max(0, int(disputes_by_status.get(status, 0)))
        )


def _normalize_avatar_eval_result(value: str) -> str:
    normalized = value.strip().lower()
    return normalized if normalized in _AVATAR_EVAL_RESULTS else "failed"


def _normalize_avatar_eval_category(value: str) -> str:
    normalized = value.strip().lower()
    return normalized if normalized in _AVATAR_EVAL_CATEGORIES else "other"


def _normalize_avatar_eval_failure_type(value: str) -> str:
    normalized = value.strip().lower()
    return normalized if normalized in _AVATAR_EVAL_FAILURE_TYPES else "other"


def observe_avatar_eval_run(*, result: str) -> None:
    AVATAR_EVAL_RUNS_TOTAL.labels(_normalize_avatar_eval_result(result)).inc()


def observe_avatar_eval_case(*, category: str, result: str) -> None:
    AVATAR_EVAL_CASES_TOTAL.labels(
        _normalize_avatar_eval_category(category),
        _normalize_avatar_eval_result(result),
    ).inc()


def observe_avatar_eval_failure(*, failure_type: str) -> None:
    AVATAR_EVAL_FAILURE_TOTAL.labels(
        _normalize_avatar_eval_failure_type(failure_type)
    ).inc()


def observe_avatar_eval_duration(*, duration_seconds: float) -> None:
    AVATAR_EVAL_DURATION_SECONDS.observe(max(0.0, duration_seconds))


def observe_avatar_eval_ratios(
    *,
    persona_consistency: float,
    unsupported_detail: float,
    over_refusal: float,
) -> None:
    AVATAR_EVAL_PERSONA_CONSISTENCY_RATIO.set(
        min(1.0, max(0.0, float(persona_consistency)))
    )
    AVATAR_EVAL_UNSUPPORTED_DETAIL_RATIO.set(
        min(1.0, max(0.0, float(unsupported_detail)))
    )
    AVATAR_EVAL_OVER_REFUSAL_RATIO.set(
        min(1.0, max(0.0, float(over_refusal)))
    )


def _normalize_avatar_eval_gate_result(passed: bool) -> str:
    return "pass" if passed else "fail"


def observe_avatar_eval_quality_gate(*, passed: bool) -> None:
    AVATAR_EVAL_QUALITY_GATE_TOTAL.labels(_normalize_avatar_eval_gate_result(passed)).inc()


def observe_avatar_eval_profile_isolation_gate(*, passed: bool) -> None:
    AVATAR_EVAL_PROFILE_ISOLATION_TOTAL.labels(_normalize_avatar_eval_gate_result(passed)).inc()


def observe_avatar_eval_corrected_memory_gate(*, passed: bool) -> None:
    AVATAR_EVAL_CORRECTED_MEMORY_TOTAL.labels(_normalize_avatar_eval_gate_result(passed)).inc()


def observe_avatar_eval_perspective_gate(*, passed: bool) -> None:
    AVATAR_EVAL_PERSPECTIVE_TOTAL.labels(_normalize_avatar_eval_gate_result(passed)).inc()


def observe_avatar_memory_query_intent(*, intent: str) -> None:
    normalized_intent = intent.strip().lower()
    if normalized_intent not in _AVATAR_MEMORY_QUERY_INTENTS:
        normalized_intent = "unknown_or_ambiguous"
    AVATAR_MEMORY_QUERY_INTENT_TOTAL.labels(normalized_intent).inc()


def observe_avatar_corrected_memory_resolution(*, resolved: bool) -> None:
    result = "resolved" if resolved else "unresolved"
    AVATAR_CORRECTED_MEMORY_RESOLUTION_TOTAL.labels(result).inc()


# Task 65.10: bounded label sets for cross-pipeline evidence prioritization.
# Mirrors the RagSource.source_type check constraint (never a free-form
# string) so the Prometheus label stays low-cardinality even if a new
# archival source_type is added later - an unrecognized value safely buckets
# to "other" instead of creating a new label series.
_EVIDENCE_SOURCE_TYPES = frozenset(
    {
        "manual_text",
        "biography",
        "timeline_memory",
        "document_text",
        "chat_export",
        "audio_transcript",
        "video_transcript",
        "letter",
        "diary",
        "conversation_candidate",
        "other",
    }
)
_EVIDENCE_DROP_REASONS = frozenset(
    {
        "ineligible",
        "superseded",
        "duplicate",
        "context_budget",
        "lower_relevance",
        "privacy_denied",
    }
)


def observe_evidence_prioritization_pool(*, candidate_count: int, selected_count: int) -> None:
    EVIDENCE_PRIORITIZATION_CANDIDATE_COUNT.observe(max(0, candidate_count))
    EVIDENCE_PRIORITIZATION_SELECTED_COUNT.observe(max(0, selected_count))


def observe_evidence_prioritization_dropped(*, reason: str) -> None:
    EVIDENCE_PRIORITIZATION_DROPPED_TOTAL.labels(
        _normalize_choice(reason, allowed=_EVIDENCE_DROP_REASONS, fallback="lower_relevance")
    ).inc()


def observe_evidence_prioritization_selected_item(*, verified: bool, source_type: str) -> None:
    EVIDENCE_PRIORITIZATION_VERIFIED_SELECTED_TOTAL.labels("true" if verified else "false").inc()
    EVIDENCE_PRIORITIZATION_SOURCE_TYPE_SELECTED_TOTAL.labels(
        _normalize_choice(source_type, allowed=_EVIDENCE_SOURCE_TYPES)
    ).inc()


# --- Task 66.1: Provider Usage and Cost Foundation ---------------------------
#
# Every label here is a small closed set of enum-like values (feature,
# execution_source, status, token_type, cost_component, monetary_cost_status,
# locale, error-classification stage) - never a user id, memorial id,
# trace/action/step id, or raw provider error message, per the hard
# cardinality restriction in Task 66.1's scope.

AI_COST_ACTIONS_TOTAL = Counter(
    "ai_cost_actions_total",
    "Total AI actions (one user-visible AI operation each).",
    labelnames=("feature", "status", "execution_source"),
)
AI_COST_ACTION_DURATION_SECONDS = Histogram(
    "ai_cost_action_duration_seconds",
    "AI action duration in seconds.",
    labelnames=("feature", "status", "execution_source"),
)
AI_COST_PROVIDER_CALLS_TOTAL = Counter(
    "ai_cost_provider_calls_total",
    "Total individual paid-provider HTTP attempts.",
    labelnames=("provider", "model", "feature", "status"),
)
AI_COST_PROVIDER_LATENCY_SECONDS = Histogram(
    "ai_cost_provider_latency_seconds",
    "Paid-provider HTTP attempt latency in seconds.",
    labelnames=("provider", "model", "feature", "status"),
)
AI_COST_TOKENS_TOTAL = Counter(
    "ai_cost_tokens_total",
    "Total provider tokens by type.",
    labelnames=("provider", "model", "feature", "token_type"),
)
AI_COST_USD_TOTAL = Counter(
    "ai_cost_usd_total",
    "Total provider cost in USD by component.",
    labelnames=("provider", "model", "feature", "cost_component", "monetary_cost_status"),
)
AI_COST_CACHED_INPUT_SAVINGS_USD_TOTAL = Counter(
    "ai_cost_cached_input_savings_usd_total",
    "Total USD saved via provider prompt caching on input tokens.",
    labelnames=("provider", "model", "feature"),
)
AI_COST_RETRIES_TOTAL = Counter(
    "ai_cost_retries_total",
    "Total paid-provider call retries (attempt_number > 1).",
    labelnames=("provider", "model", "feature", "reason"),
)
AI_COST_TRANSLATION_CACHE_TOTAL = Counter(
    "ai_cost_translation_cache_total",
    "Total dynamic-translation cache hit/miss events.",
    labelnames=("source_locale", "target_locale", "status"),
)
AI_COST_PRICING_UNKNOWN_TOTAL = Counter(
    "ai_cost_pricing_unknown_total",
    "Total successful provider attempts priced as unknown (no catalog entry).",
    labelnames=("provider", "model", "feature"),
)
AI_COST_AUDIT_FAILURES_TOTAL = Counter(
    "ai_cost_audit_failures_total",
    "Total durable audit-trail persistence failures for AI cost accounting.",
    labelnames=("stage", "feature"),
)

_AI_COST_FEATURES = frozenset(
    {
        "brain_chat_response",
        "avatar_biographer_question",
        "dynamic_memory_translation",
        "memory_candidate_finalization",
        "memory_conflict_analysis",
        "memory_summarization",
        "evaluation",
        "development_test",
        "other",
    }
)
_AI_COST_EXECUTION_SOURCES = frozenset({"fastapi", "celery", "internal", "test"})
_AI_COST_ACTION_STATUSES = frozenset({"pending", "running", "succeeded", "failed", "cancelled"})
_AI_COST_ATTEMPT_STATUSES = frozenset(
    {
        "pending",
        "succeeded",
        "timeout",
        "rate_limited",
        "http_error",
        "invalid_response",
        "empty_response",
        "cancelled",
        "audit_error",
        "internal_error",
    }
)
_AI_COST_TOKEN_TYPES = frozenset(
    {"input", "cached_input", "uncached_input", "output", "reasoning", "total"}
)
_AI_COST_COST_COMPONENTS = frozenset(
    {"uncached_input", "cached_input", "output", "reasoning", "total"}
)
_AI_COST_MONETARY_STATUSES = frozenset({"not_applicable", "calculated", "partial", "unknown"})
_AI_COST_TRANSLATION_CACHE_STATUSES = frozenset({"hit", "miss"})
_AI_COST_LOCALES = frozenset({"cs", "ru", "en"})


def normalize_ai_feature_label(feature: str | None) -> str:
    normalized = (feature or "").strip().lower()
    return normalized if normalized in _AI_COST_FEATURES else "other"


def normalize_ai_execution_source_label(execution_source: str | None) -> str:
    normalized = (execution_source or "").strip().lower()
    return normalized if normalized in _AI_COST_EXECUTION_SOURCES else "internal"


def normalize_ai_action_status_label(status: str | None) -> str:
    normalized = (status or "").strip().lower()
    return normalized if normalized in _AI_COST_ACTION_STATUSES else "failed"


def normalize_ai_attempt_status_label(status: str | None) -> str:
    normalized = (status or "").strip().lower()
    return normalized if normalized in _AI_COST_ATTEMPT_STATUSES else "internal_error"


def normalize_ai_monetary_status_label(status: str | None) -> str:
    normalized = (status or "").strip().lower()
    return normalized if normalized in _AI_COST_MONETARY_STATUSES else "unknown"


def normalize_ai_locale_label(locale: str | None) -> str:
    normalized = (locale or "").strip().lower()
    return normalized if normalized in _AI_COST_LOCALES else "other"


def normalize_ai_provider_model_labels(provider: str | None, model: str | None) -> tuple[str, str]:
    normalized_provider = normalize_brain_provider_label(provider)
    normalized_model = normalize_brain_model_label(model)
    return normalized_provider, normalized_model


def observe_ai_action_completed(
    *,
    feature: str,
    status: str,
    execution_source: str,
    duration_seconds: float,
) -> None:
    labels = (
        normalize_ai_feature_label(feature),
        normalize_ai_action_status_label(status),
        normalize_ai_execution_source_label(execution_source),
    )
    AI_COST_ACTIONS_TOTAL.labels(*labels).inc()
    AI_COST_ACTION_DURATION_SECONDS.labels(*labels).observe(max(0.0, duration_seconds))


def observe_ai_provider_attempt(
    *,
    provider: str,
    model: str,
    feature: str,
    status: str,
    latency_seconds: float,
    token_usage: Any | None = None,
) -> None:
    normalized_provider, normalized_model = normalize_ai_provider_model_labels(provider, model)
    normalized_feature = normalize_ai_feature_label(feature)
    normalized_status = normalize_ai_attempt_status_label(status)
    call_labels = (normalized_provider, normalized_model, normalized_feature, normalized_status)
    AI_COST_PROVIDER_CALLS_TOTAL.labels(*call_labels).inc()
    AI_COST_PROVIDER_LATENCY_SECONDS.labels(*call_labels).observe(max(0.0, latency_seconds))

    if token_usage is None:
        return

    token_values = (
        ("input", token_usage.input_tokens),
        ("cached_input", token_usage.cached_input_tokens),
        ("uncached_input", token_usage.uncached_input_tokens),
        ("output", token_usage.output_tokens),
        ("reasoning", token_usage.reasoning_tokens),
        ("total", token_usage.total_tokens),
    )
    for token_type, value in token_values:
        if value:
            AI_COST_TOKENS_TOTAL.labels(
                normalized_provider, normalized_model, normalized_feature, token_type
            ).inc(value)

    monetary_status = normalize_ai_monetary_status_label(
        getattr(token_usage.monetary_cost_status, "value", token_usage.monetary_cost_status)
    )
    cost_values = (
        ("uncached_input", token_usage.uncached_input_cost_usd),
        ("cached_input", token_usage.cached_input_cost_usd),
        ("output", token_usage.output_cost_usd),
        ("reasoning", token_usage.reasoning_cost_usd),
        ("total", token_usage.total_cost_usd),
    )
    for cost_component, value in cost_values:
        if value:
            AI_COST_USD_TOTAL.labels(
                normalized_provider, normalized_model, normalized_feature, cost_component, monetary_status
            ).inc(float(value))

    if token_usage.cached_input_savings_usd:
        AI_COST_CACHED_INPUT_SAVINGS_USD_TOTAL.labels(
            normalized_provider, normalized_model, normalized_feature
        ).inc(float(token_usage.cached_input_savings_usd))

    if monetary_status == "unknown":
        AI_COST_PRICING_UNKNOWN_TOTAL.labels(normalized_provider, normalized_model, normalized_feature).inc()


def observe_ai_retry(*, provider: str, model: str, feature: str, reason: str | None) -> None:
    normalized_provider, normalized_model = normalize_ai_provider_model_labels(provider, model)
    normalized_reason = (reason or "unspecified").strip().lower() or "unspecified"
    AI_COST_RETRIES_TOTAL.labels(
        normalized_provider, normalized_model, normalize_ai_feature_label(feature), normalized_reason
    ).inc()


def observe_ai_translation_cache(*, source_locale: str, target_locale: str, status: str) -> None:
    normalized_status = status.strip().lower()
    if normalized_status not in _AI_COST_TRANSLATION_CACHE_STATUSES:
        normalized_status = "miss"
    AI_COST_TRANSLATION_CACHE_TOTAL.labels(
        normalize_ai_locale_label(source_locale), normalize_ai_locale_label(target_locale), normalized_status
    ).inc()


def observe_ai_audit_failure(*, stage: str, feature: str) -> None:
    normalized_stage = (stage or "unknown").strip().lower() or "unknown"
    AI_COST_AUDIT_FAILURES_TOTAL.labels(normalized_stage, normalize_ai_feature_label(feature)).inc()

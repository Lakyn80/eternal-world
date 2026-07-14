from __future__ import annotations

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
_CONTENT_TRANSLATION_LANGUAGE_PAIRS = frozenset({"cs_ru", "ru_cs"})
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

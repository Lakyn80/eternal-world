from __future__ import annotations

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, Histogram, generate_latest
from starlette.responses import Response


_NORMALIZED_GUARD_REASONS = {
    None: "none",
    "": "none",
    "forbidden_claim_in_lack_case": "forbidden_claim_in_lack_case",
    "no_evidence_answer_with_extra_detail": "no_evidence_answer_with_extra_detail",
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

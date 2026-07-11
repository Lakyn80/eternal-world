from __future__ import annotations

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
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

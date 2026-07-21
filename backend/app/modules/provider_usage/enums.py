from __future__ import annotations

from enum import Enum


class AiFeature(str, Enum):
    """Closed, low-cardinality taxonomy of user-visible/system operations
    that may cause a paid AI provider call. Every ``AiAction`` must be
    tagged with exactly one of these - callers must not invent free-form
    feature strings for persisted rows or Prometheus labels."""

    BRAIN_CHAT_RESPONSE = "brain_chat_response"
    AVATAR_BIOGRAPHER_QUESTION = "avatar_biographer_question"
    DYNAMIC_MEMORY_TRANSLATION = "dynamic_memory_translation"
    MEMORY_CANDIDATE_FINALIZATION = "memory_candidate_finalization"
    MEMORY_CONFLICT_ANALYSIS = "memory_conflict_analysis"
    MEMORY_SUMMARIZATION = "memory_summarization"
    EVALUATION = "evaluation"
    DEVELOPMENT_TEST = "development_test"
    OTHER = "other"


class AiStepType(str, Enum):
    """Processing-step taxonomy within one ``AiAction``. Only
    ``PROVIDER_GENERATION``/``PROVIDER_TRANSLATION``/``PROVIDER_STRUCTURED_OUTPUT``
    steps may carry token/monetary cost; the remaining, provider-free step
    types may be used for action timing but must never carry fabricated
    token/cost values."""

    PROVIDER_GENERATION = "provider_generation"
    PROVIDER_TRANSLATION = "provider_translation"
    PROVIDER_STRUCTURED_OUTPUT = "provider_structured_output"
    CONTEXT_PREPARATION = "context_preparation"
    RETRIEVAL = "retrieval"
    DETERMINISTIC_POSTPROCESSING = "deterministic_postprocessing"
    RESPONSE_GUARD = "response_guard"


class ExecutionSource(str, Enum):
    FASTAPI = "fastapi"
    CELERY = "celery"
    INTERNAL = "internal"
    TEST = "test"


class CacheStatus(str, Enum):
    NOT_APPLICABLE = "not_applicable"
    HIT = "hit"
    MISS = "miss"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class MonetaryCostStatus(str, Enum):
    """Whether a monetary cost figure can be trusted as complete.

    ``NOT_APPLICABLE`` - no paid provider call happened (e.g. a cache hit or
    a deterministic step). ``CALCULATED`` - every priced component had a
    known price. ``PARTIAL`` - some components are known, others are not;
    the total must not be presented as complete. ``UNKNOWN`` - token usage
    exists but no price is known for this provider/model at all; the total
    must never be fabricated as zero.
    """

    NOT_APPLICABLE = "not_applicable"
    CALCULATED = "calculated"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class AiActionStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


class AiStepStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    SKIPPED = "skipped"


class ProviderAttemptStatus(str, Enum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    TIMEOUT = "timeout"
    RATE_LIMITED = "rate_limited"
    HTTP_ERROR = "http_error"
    INVALID_RESPONSE = "invalid_response"
    EMPTY_RESPONSE = "empty_response"
    CANCELLED = "cancelled"
    AUDIT_ERROR = "audit_error"
    INTERNAL_ERROR = "internal_error"


class AiErrorCategory(str, Enum):
    VALIDATION_ERROR = "validation_error"
    AUTHORIZATION_ERROR = "authorization_error"
    PROVIDER_TIMEOUT = "provider_timeout"
    PROVIDER_RATE_LIMITED = "provider_rate_limited"
    PROVIDER_HTTP_ERROR = "provider_http_error"
    PROVIDER_INVALID_RESPONSE = "provider_invalid_response"
    PROVIDER_EMPTY_RESPONSE = "provider_empty_response"
    PRICING_UNKNOWN = "pricing_unknown"
    AUDIT_PERSISTENCE_ERROR = "audit_persistence_error"
    CACHE_ERROR = "cache_error"
    CELERY_ERROR = "celery_error"
    INTERNAL_ERROR = "internal_error"


#: Provider-attempt statuses that represent a successful provider response.
SUCCEEDED_PROVIDER_ATTEMPT_STATUSES = frozenset({ProviderAttemptStatus.SUCCEEDED.value})

#: Provider-attempt statuses considered a genuine failure (as opposed to
#: still-pending). Used to decide whether a retry is being recorded.
FAILED_PROVIDER_ATTEMPT_STATUSES = frozenset(
    {
        ProviderAttemptStatus.TIMEOUT.value,
        ProviderAttemptStatus.RATE_LIMITED.value,
        ProviderAttemptStatus.HTTP_ERROR.value,
        ProviderAttemptStatus.INVALID_RESPONSE.value,
        ProviderAttemptStatus.EMPTY_RESPONSE.value,
        ProviderAttemptStatus.CANCELLED.value,
        ProviderAttemptStatus.AUDIT_ERROR.value,
        ProviderAttemptStatus.INTERNAL_ERROR.value,
    }
)

from __future__ import annotations

from enum import Enum


class BackgroundJobStatus(str, Enum):
    #: Task 65.9 (Part D) - created durably (job + outbox row committed)
    #: but not yet confirmed published to the broker. A job created via
    #: the outbox-aware path starts here, not at QUEUED.
    PENDING = "pending"
    QUEUED = "queued"
    #: "processing" in the spec's vocabulary - kept as the pre-existing
    #: `running` value rather than renamed, to avoid a repository-wide
    #: rename of every existing `status == "running"` check.
    RUNNING = "running"
    #: Task 65.9 (Part M) - bounded provider self-healing is in progress
    #: for this job (a fresh worker process/attempt is required).
    RECOVERY_PENDING = "recovery_pending"
    #: Task 65.9 (Part P) - a normal, bounded infrastructure-failure retry
    #: is scheduled (never used for provider corruption, see Part M).
    RETRY_SCHEDULED = "retry_scheduled"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


#: States in which a job still represents active/outstanding work - used
#: for backpressure counting (Part Q) and stale-job scanning (Part P).
#: Terminal states (succeeded/failed/cancelled) are always excluded.
ACTIVE_BACKGROUND_JOB_STATUSES: tuple[str, ...] = (
    BackgroundJobStatus.PENDING.value,
    BackgroundJobStatus.QUEUED.value,
    BackgroundJobStatus.RUNNING.value,
    BackgroundJobStatus.RETRY_SCHEDULED.value,
    BackgroundJobStatus.RECOVERY_PENDING.value,
)


class BackgroundJobType(str, Enum):
    SMOKE_TEST = "smoke_test"
    SYSTEM_MILESTONE = "system_milestone"
    RAG_SOURCE_INGESTION = "rag_source_ingestion"
    RAG_CHUNKING = "rag_chunking"
    EMBEDDING_GENERATION = "embedding_generation"
    QDRANT_INDEXING = "qdrant_indexing"
    RAG_RETRIEVAL = "rag_retrieval"
    BRAIN_AGENT_GENERATION = "brain_agent_generation"
    MEDIA_PROCESSING = "media_processing"
    VOICE_GENERATION = "voice_generation"
    VIDEO_GENERATION = "video_generation"


#: Job types that perform real embedding-model inference and therefore (a)
#: belong on the dedicated `embedding` queue and (b) are subject to the
#: per-user/per-profile/global backpressure limits in Part Q. Kept as an
#: explicit allow-list rather than "everything except smoke_test" so a
#: future lightweight job type does not silently become rate-limited.
HEAVY_EMBEDDING_JOB_TYPES: frozenset[str] = frozenset(
    {
        BackgroundJobType.RAG_SOURCE_INGESTION.value,
        BackgroundJobType.RAG_CHUNKING.value,
        BackgroundJobType.EMBEDDING_GENERATION.value,
        BackgroundJobType.QDRANT_INDEXING.value,
    }
)


class SafeErrorCategory(str, Enum):
    """Closed set of safe, public-facing error categories (Task 65.9, Part
    L). Never derived from a raw exception message - callers explicitly
    classify into one of these before persisting/returning it."""

    PROVIDER_CORRUPT = "provider_corrupt"
    PROVIDER_INITIALIZATION_FAILED = "provider_initialization_failed"
    INVALID_EMBEDDING_OUTPUT = "invalid_embedding_output"
    TEMPORARY_BROKER_FAILURE = "temporary_broker_failure"
    TEMPORARY_DATABASE_FAILURE = "temporary_database_failure"
    TEMPORARY_QDRANT_FAILURE = "temporary_qdrant_failure"
    PERMANENT_QDRANT_VALIDATION_FAILURE = "permanent_qdrant_validation_failure"
    INVALID_DOMAIN_STATE = "invalid_domain_state"
    AUTHORIZATION_FAILURE = "authorization_failure"
    RESOURCE_NOT_FOUND = "resource_not_found"
    CONTENT_VALIDATION_FAILURE = "content_validation_failure"
    WORKER_LOST = "worker_lost"
    UNKNOWN_INTERNAL_FAILURE = "unknown_internal_failure"


#: Only these categories may ever trigger provider invalidation/reload or a
#: worker-recycle request (Part L: "Only provider health failures may
#: trigger provider reload or worker recycling").
PROVIDER_HEALTH_ERROR_CATEGORIES: frozenset[str] = frozenset(
    {
        SafeErrorCategory.PROVIDER_CORRUPT.value,
        SafeErrorCategory.PROVIDER_INITIALIZATION_FAILED.value,
        SafeErrorCategory.INVALID_EMBEDDING_OUTPUT.value,
    }
)

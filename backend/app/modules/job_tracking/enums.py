from __future__ import annotations

from enum import Enum


class BackgroundJobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


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

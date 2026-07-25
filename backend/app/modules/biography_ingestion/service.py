"""Turns a memorial owner's free-text `MemoryProfile.biography` field into
verified, searchable avatar memory (Task 65.2).

Mirrors the established `avatar_memory_indexing`/`memorial_contribution_indexing`
pattern (embed -> RagSource/RagChunk/RagEmbedding -> Qdrant, deterministic
point ids, idempotent retry) rather than inventing a new embedding system.
`RagSource.source_type == "biography"` was already reserved by the
`rag_sources_source_type` check constraint before this task; this module is
the first code path that actually creates one.

Two phases, same split as the reference implementations:
  * `start_biography_ingestion` - lightweight, DB-only: validates and flips
    `MemoryProfile.biography_status` to `ready_for_ingestion`, then enqueues
    the heavy step on the existing Celery worker (biography text can be
    thousands of characters / many chunks, unlike a single short approved
    contribution, so this one is asynchronous where the two existing
    reference pipelines are synchronous demo-button calls).
  * `index_biography` - the heavy step (chunk + embed + Qdrant upsert).
    Idempotent: retrying with the *same* biography text reuses the existing
    `RagSource`/chunks/embeddings; re-ingesting *edited* (stale) biography
    text creates a fresh `RagSource` and retires the previous one's Qdrant
    points so stale content stops being retrievable, per the task's explicit
    "do not silently keep old content as current" requirement.
"""

from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from time import perf_counter
from typing import Protocol

from sqlalchemy.orm import Session
from uuid import NAMESPACE_URL, uuid5

from app.core.logging import get_logger, log_event
from app.db.models import MemoryProfile, RagChunk, RagEmbedding, RagSource, RagVectorIndex, User
from app.modules.active_retrieval_config.service import resolve_runtime_active_retrieval_config
from app.modules.avatar_memory_indexing.qdrant_writer import (
    AvatarMemoryQdrantWriter,
    DefaultAvatarMemoryQdrantWriter,
)
from app.modules.biography_ingestion import repository
from app.modules.biography_ingestion.chunking import chunk_biography_text
from app.modules.biography_ingestion.schemas import BiographyStatusRead
from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.providers import build_embedding_provider
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.embeddings.providers.bge_m3_hybrid import BgeM3HybridEmbeddingAdapter
from app.modules.embeddings.runtime import assert_real_embedding_runtime_for_e2e
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.qdrant_indexing import repository as qdrant_index_repository
from app.modules.rag_chunks.validation import estimate_token_count


INDEX_MODEL_CODE = "bge_m3_dense_sparse"
SOURCE_TYPE = "biography"
PROVENANCE = "owner_confirmed_initial_biography"
MEMORY_STATUS = "verified"
MAX_BIOGRAPHY_LENGTH = 20000
SAFE_FAILURE_MESSAGE = "Biography indexing failed"
RETRYABLE_STATUSES = {"ready_for_ingestion", "ingesting", "failed"}

logger = get_logger("biography_ingestion")


class BiographyIngestionNotFoundError(Exception):
    pass


class BiographyIngestionEligibilityError(Exception):
    pass


class BiographyIngestionConflictError(Exception):
    pass


class BiographyIngestionExecutionError(Exception):
    pass


class BiographyEmbeddingEncoder(Protocol):
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector: ...


class DefaultBiographyEmbeddingEncoder:
    """Task 65.9 (Part M): see `avatar_memory_indexing.service.
    DefaultAvatarMemoryEmbeddingEncoder` for the full rationale."""

    def __init__(self, *, self_healing_encoder: object | None = None) -> None:
        self._self_healing_encoder = self_healing_encoder

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        if self._self_healing_encoder is not None:
            from app.modules.embeddings.self_healing import ProviderRecoveryExhaustedError

            try:
                return self._self_healing_encoder.encode(text=text, model_code=model_code)
            except ProviderRecoveryExhaustedError as exc:
                raise BiographyIngestionExecutionError(SAFE_FAILURE_MESSAGE) from exc

        provider = build_embedding_provider(model_code=model_code)
        if not isinstance(provider, BgeM3HybridEmbeddingAdapter):
            raise BiographyIngestionExecutionError("Real BGE-M3 passage embedding provider is unavailable")
        return provider.embed_passage(text, model_code)


def normalize_biography_text(text: str) -> str:
    normalized = (text or "").strip()
    if not normalized:
        raise BiographyIngestionEligibilityError("Biography text is empty")
    if len(normalized) > MAX_BIOGRAPHY_LENGTH:
        raise BiographyIngestionEligibilityError("Biography text is too long")
    return normalized


def compute_content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_deterministic_point_id(*, source_id: int, chunk_index: int) -> str:
    identity = f"biography-source:{source_id}:{chunk_index}"
    return str(uuid5(NAMESPACE_URL, identity))


def update_biography(db: Session, *, profile: MemoryProfile, biography: str) -> MemoryProfile:
    """Save edited biography text. Never indexes automatically. If the
    profile's biography was already `indexed`, editing the text makes that
    index stale (a distinct state from `draft`, so the UI/owner can tell
    "never indexed" apart from "indexed, but no longer matches the current
    text") - either way, a fresh explicit ingestion action is required."""

    normalized = biography.strip()
    if normalized == (profile.biography or "").strip():
        return profile

    profile.biography = normalized
    profile.biography_status = "stale" if profile.biography_status == "indexed" else "draft"
    db.commit()
    db.refresh(profile)
    return profile


def clear_biography(
    db: Session,
    *,
    profile: MemoryProfile,
    writer: AvatarMemoryQdrantWriter | None = None,
) -> MemoryProfile:
    """Task 65.5: a less-destructive alternative to deleting the whole
    memorial - removes only the biography text and whatever it has indexed,
    leaving membership, invitations, contributions, and other approved
    (non-biography) memories untouched.

    Reuses the exact same safe-partial-failure Qdrant cleanup pattern as
    `_retire_previous_source` (re-indexing an edited biography already had
    to solve "remove the previous version's points without losing the DB
    audit trail" - clearing is the same operation, just without a new
    source to replace the old one with). A point that fails to delete is
    logged and skipped rather than aborting the whole clear - the
    corresponding `RagVectorIndex` bookkeeping row is only removed once its
    Qdrant point is confirmed gone, so a failed point remains discoverable
    (not silently forgotten) and a repeat clear is safe to retry.

    The underlying `RagSource`/`RagChunk`/`RagEmbedding` rows are
    intentionally left in place (never hard-deleted here) - they are the
    existing audit trail of what was previously indexed, exactly like a
    normal stale-then-reindex cycle already preserves.
    """

    actual_writer = writer or DefaultAvatarMemoryQdrantWriter()
    if profile.biography_source_id is not None:
        records = repository.list_vector_indexes_for_source(
            db, source_id=profile.biography_source_id
        )
        for record in records:
            try:
                actual_writer.delete_point(
                    collection_name=record.qdrant_collection, point_id=record.qdrant_point_id
                )
            except Exception as exc:
                log_event(
                    logger,
                    logging.ERROR,
                    "biography_clear_delete_point_failed",
                    profile_id=profile.id,
                    source_id=profile.biography_source_id,
                    error_type=exc.__class__.__name__,
                )
                continue
            db.delete(record)

    profile.biography = None
    profile.biography_status = "draft"
    profile.biography_content_hash = None
    profile.biography_indexed_at = None
    profile.biography_source_id = None
    profile.biography_ingestion_attempt_count = 0
    profile.biography_ingestion_failure_reason = None
    db.commit()
    db.refresh(profile)
    log_event(
        logger,
        logging.INFO,
        "biography_cleared",
        profile_id=profile.id,
    )
    return profile


def get_biography_status(profile: MemoryProfile) -> BiographyStatusRead:
    return BiographyStatusRead(
        profile_id=profile.id,
        status=profile.biography_status,
        content_hash=profile.biography_content_hash,
        indexed_at=profile.biography_indexed_at,
        attempt_count=profile.biography_ingestion_attempt_count,
        failure_reason=profile.biography_ingestion_failure_reason,
    )


def start_biography_ingestion(db: Session, *, profile: MemoryProfile):
    """Enqueue the heavy ingestion step. Raises if there is no biography text
    yet or a job is already in flight; safe to call again after `failed` or
    `stale` to retry/re-ingest.

    Task 65.9 (Part E/F/I): creates the persistent job and its
    transactional outbox record, then returns - the encoder/Qdrant write
    happens only inside the Celery embedding-worker task, never here. The
    idempotency key is `job_type + profile_id + content_hash + operation`
    (Part F's exact prescribed shape): a duplicate request for the exact
    same biography text reuses the same job instead of creating a second
    one; a request after the text changed (different `content_hash`) gets
    its own new job, matching "stale -> re-index" already being a
    supported, intentional flow.
    """

    if not (profile.biography or "").strip():
        raise BiographyIngestionEligibilityError("Biography text is empty")
    if profile.biography_status == "ingesting":
        raise BiographyIngestionConflictError("Biography ingestion is already in progress")

    content_hash = compute_content_hash(normalize_biography_text(profile.biography or ""))
    idempotency_key = f"biography_indexing:{profile.id}:{content_hash}:index"

    profile.biography_status = "ready_for_ingestion"
    db.commit()

    background_job = create_job(
        db,
        owner_user_id=profile.user_id,
        profile_id=profile.id,
        job_type=BackgroundJobType.QDRANT_INDEXING,
        input_payload={"workflow": "biography_indexing", "profile_id": profile.id},
        queue="embedding",
        idempotency_key=idempotency_key,
    )

    from app.modules.job_outbox.service import enqueue_job_with_outbox

    return enqueue_job_with_outbox(
        db,
        job=background_job,
        task_name="app.worker.tasks.run_biography_indexing_job",
        queue="embedding",
    )


@dataclass(frozen=True)
class _IndexingPlan:
    profile: MemoryProfile
    owner: User
    text: str
    content_hash: str
    model_code: str
    collection_name: str
    vector_dimension: int


def _build_plan(db: Session, *, profile: MemoryProfile, writer: AvatarMemoryQdrantWriter) -> _IndexingPlan:
    text = normalize_biography_text(profile.biography or "")
    owner = db.get(User, profile.user_id)
    if owner is None:
        raise BiographyIngestionEligibilityError("Memorial owner account is invalid")
    runtime = resolve_runtime_active_retrieval_config(db, current_user=owner, profile_id=profile.id)
    if runtime.model_code != INDEX_MODEL_CODE:
        raise BiographyIngestionEligibilityError("Target profile is not configured for BGE-M3 memory retrieval")
    model = get_embedding_model(runtime.model_code)
    collection_dimension = writer.collection_vector_size(collection_name=runtime.collection_name)
    if collection_dimension is None:
        raise BiographyIngestionEligibilityError("Target memory collection does not exist")
    if collection_dimension != model.dimension:
        raise BiographyIngestionEligibilityError("Target memory collection has an incompatible dimension")
    return _IndexingPlan(
        profile=profile,
        owner=owner,
        text=text,
        content_hash=compute_content_hash(text),
        model_code=runtime.model_code,
        collection_name=runtime.collection_name,
        vector_dimension=model.dimension,
    )


def _get_or_create_source(db: Session, *, plan: _IndexingPlan) -> RagSource:
    existing = repository.get_reusable_biography_source(
        db,
        profile_id=plan.profile.id,
        content_hash=plan.content_hash,
    )
    if existing is not None:
        return existing

    source = RagSource(
        owner_user_id=plan.owner.id,
        profile_id=plan.profile.id,
        source_type=SOURCE_TYPE,
        title=f"{plan.profile.name} — initial biography",
        raw_text=plan.text,
        normalized_text=plan.text,
        language=None,
        status="ready_for_cleaning",
        processing_error=None,
        source_metadata={
            "content_hash": plan.content_hash,
            "provenance": PROVENANCE,
            "memory_status": MEMORY_STATUS,
        },
    )
    db.add(source)
    db.flush()
    return source


def _get_or_create_chunk_and_embedding(
    db: Session,
    *,
    plan: _IndexingPlan,
    source: RagSource,
    chunk_index: int,
    chunk_text: str,
    encoder: BiographyEmbeddingEncoder,
) -> tuple[RagChunk, RagEmbedding]:
    text_hash = hashlib.sha256(chunk_text.encode("utf-8")).hexdigest()
    existing_chunk = next(
        (
            chunk
            for chunk in source.rag_chunks
            if chunk.chunk_index == chunk_index and chunk.text_hash == text_hash
        ),
        None,
    )
    if existing_chunk is not None:
        existing_embedding = next(
            (
                embedding
                for embedding in source.rag_embeddings
                if embedding.chunk_id == existing_chunk.id
                and embedding.model_code == plan.model_code
                and embedding.status == "embedded"
                and isinstance(embedding.vector, list)
                and len(embedding.vector) == plan.vector_dimension
            ),
            None,
        )
        if existing_embedding is not None:
            return existing_chunk, existing_embedding

    metadata = {
        "content_hash": plan.content_hash,
        "provenance": PROVENANCE,
        "memory_status": MEMORY_STATUS,
        "chunk_id": f"biography-source:{source.id}:{chunk_index}",
    }
    chunk = existing_chunk
    if chunk is None:
        chunk = RagChunk(
            owner_user_id=plan.owner.id,
            profile_id=plan.profile.id,
            source_id=source.id,
            chunk_index=chunk_index,
            chunk_text=chunk_text,
            text_hash=text_hash,
            token_estimate=estimate_token_count(chunk_text),
            char_count=len(chunk_text),
            sentence_count=max(1, chunk_text.count(".") + chunk_text.count("!") + chunk_text.count("?") or 1),
            language=None,
            chunk_metadata=metadata,
            validation_status="valid",
            validation_errors=[],
        )
        db.add(chunk)
        db.flush()

    encoded = encoder.encode(text=chunk_text, model_code=plan.model_code)
    if encoded.dimension != plan.vector_dimension or len(encoded.values) != plan.vector_dimension:
        raise BiographyIngestionExecutionError("Biography embedding dimension is invalid")
    embedding = RagEmbedding(
        owner_user_id=plan.owner.id,
        profile_id=plan.profile.id,
        source_id=source.id,
        chunk_id=chunk.id,
        model_code=plan.model_code,
        vector=list(encoded.values),
        vector_dimension=encoded.dimension,
        text_hash=text_hash,
        status="embedded",
        error_message=None,
        embedding_metadata={**encoded.metadata, **metadata, "input_type": "passage"},
    )
    db.add(embedding)
    db.flush()
    return chunk, embedding


def _upsert_point(
    db: Session,
    *,
    plan: _IndexingPlan,
    source: RagSource,
    chunk: RagChunk,
    embedding: RagEmbedding,
    writer: AvatarMemoryQdrantWriter,
    indexed_at: datetime,
) -> str:
    point_id = build_deterministic_point_id(source_id=source.id, chunk_index=chunk.chunk_index)
    payload = {
        "owner_user_id": plan.owner.id,
        "profile_id": plan.profile.id,
        "source_id": source.id,
        "chunk_id": chunk.id,
        "embedding_id": embedding.id,
        "model_code": plan.model_code,
        "text_hash": chunk.text_hash,
        "source_type": SOURCE_TYPE,
        "chunk_index": chunk.chunk_index,
        "indexed_at": indexed_at.isoformat(),
        "memory_status": MEMORY_STATUS,
        "provenance": PROVENANCE,
    }
    existing_point = writer.get_point(collection_name=plan.collection_name, point_id=point_id)
    if existing_point is None:
        if not embedding.vector:
            raise BiographyIngestionExecutionError("Stored biography embedding is unavailable")
        writer.upsert_point(
            collection_name=plan.collection_name,
            point_id=point_id,
            vector=list(embedding.vector),
            payload=payload,
        )

    record = qdrant_index_repository.get_vector_index_for_embedding_and_collection(
        db,
        embedding_id=embedding.id,
        qdrant_collection=plan.collection_name,
    )
    if record is None:
        qdrant_index_repository.create_rag_vector_index(
            db,
            owner_user_id=plan.owner.id,
            profile_id=plan.profile.id,
            source_id=source.id,
            chunk_id=chunk.id,
            embedding_id=embedding.id,
            model_code=plan.model_code,
            qdrant_collection=plan.collection_name,
            qdrant_point_id=point_id,
            status="indexed",
            error_message=None,
            indexed_at=indexed_at,
        )
    else:
        record.status = "indexed"
        record.error_message = None
        record.indexed_at = indexed_at
        record.qdrant_point_id = point_id
    return point_id


def _retire_previous_source(
    db: Session,
    *,
    profile: MemoryProfile,
    new_source_id: int,
    writer: AvatarMemoryQdrantWriter,
) -> None:
    previous_source_id = profile.biography_source_id
    if previous_source_id is None or previous_source_id == new_source_id:
        return
    previous_source = repository.get_source_by_id(db, source_id=previous_source_id)
    if previous_source is None:
        return
    records = repository.list_vector_indexes_for_source(db, source_id=previous_source_id)
    for record in records:
        try:
            writer.delete_point(collection_name=record.qdrant_collection, point_id=record.qdrant_point_id)
        except Exception as exc:
            log_event(
                logger,
                logging.ERROR,
                "biography_retire_delete_failed",
                profile_id=profile.id,
                previous_source_id=previous_source_id,
                error_type=exc.__class__.__name__,
            )
            continue
        # No "retired" value exists in `rag_vector_indexes_status` - the
        # bookkeeping row's only job is tracking "is this point currently in
        # Qdrant", so once the point is gone the row is deleted outright
        # rather than marked with an invalid status; the RagSource/RagChunk/
        # RagEmbedding rows themselves are untouched, preserving the audit
        # trail of what the previous biography version contained.
        db.delete(record)


def index_biography(
    db: Session,
    *,
    profile_id: int,
    writer: AvatarMemoryQdrantWriter | None = None,
    encoder: BiographyEmbeddingEncoder | None = None,
    validate_runtime: bool = True,
) -> BiographyStatusRead:
    """Embed and index the profile's current biography text. Idempotent:
    calling again with unchanged text and an already-`indexed` status
    reuses the existing source/chunks/embeddings and re-validates the
    Qdrant points rather than writing duplicates."""

    started_at = perf_counter()
    actual_writer = writer or DefaultAvatarMemoryQdrantWriter()
    profile = repository.get_profile_for_update(db, profile_id=profile_id)
    if profile is None:
        raise BiographyIngestionNotFoundError("Memory profile not found")
    if profile.biography_status not in RETRYABLE_STATUSES:
        raise BiographyIngestionEligibilityError(
            f"Biography status `{profile.biography_status}` is not eligible for indexing"
        )

    try:
        plan = _build_plan(db, profile=profile, writer=actual_writer)
        if validate_runtime:
            assert_real_embedding_runtime_for_e2e(
                model_code=plan.model_code,
                collection_name=plan.collection_name,
            )
        actual_encoder = encoder or DefaultBiographyEmbeddingEncoder()

        source = _get_or_create_source(db, plan=plan)
        chunks_text = chunk_biography_text(plan.text)
        if not chunks_text:
            raise BiographyIngestionEligibilityError("Biography text produced no chunks")

        indexed_at = datetime.now(timezone.utc)
        for chunk_index, chunk_text in enumerate(chunks_text):
            chunk, embedding = _get_or_create_chunk_and_embedding(
                db,
                plan=plan,
                source=source,
                chunk_index=chunk_index,
                chunk_text=chunk_text,
                encoder=actual_encoder,
            )
            _upsert_point(
                db,
                plan=plan,
                source=source,
                chunk=chunk,
                embedding=embedding,
                writer=actual_writer,
                indexed_at=indexed_at,
            )

        _retire_previous_source(db, profile=profile, new_source_id=source.id, writer=actual_writer)

        source.status = "embedded"
        profile.biography_status = "indexed"
        profile.biography_indexed_at = indexed_at
        profile.biography_content_hash = plan.content_hash
        profile.biography_source_id = source.id
        profile.biography_ingestion_failure_reason = None
        db.commit()
        db.refresh(profile)
        log_event(
            logger,
            logging.INFO,
            "biography_indexing_completed",
            profile_id=profile.id,
            source_id=source.id,
            chunk_count=len(chunks_text),
            duration_ms=round((perf_counter() - started_at) * 1000, 2),
        )
        return get_biography_status(profile)
    except (BiographyIngestionEligibilityError, BiographyIngestionNotFoundError):
        raise
    except Exception as exc:
        db.rollback()
        failed_profile = repository.get_profile_for_update(db, profile_id=profile_id)
        if failed_profile is not None:
            failed_profile.biography_status = "failed"
            failed_profile.biography_ingestion_failure_reason = SAFE_FAILURE_MESSAGE
            db.commit()
        log_event(
            logger,
            logging.ERROR,
            "biography_indexing_failed",
            profile_id=profile_id,
            error_type=exc.__class__.__name__,
        )
        if isinstance(exc, BiographyIngestionExecutionError):
            raise
        raise BiographyIngestionExecutionError(SAFE_FAILURE_MESSAGE) from exc

from __future__ import annotations

import hashlib
import logging
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from time import perf_counter
from typing import Protocol
from uuid import NAMESPACE_URL, uuid5

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import (
    observe_memory_indexing_finished,
    observe_memory_indexing_started,
    observe_memory_promotion_status,
)
from app.db.models import (
    AvatarMemoryPromotion,
    MemoryProfile,
    RagChunk,
    RagEmbedding,
    RagSource,
    User,
)
from app.modules.active_retrieval_config.service import resolve_runtime_active_retrieval_config
from app.modules.avatar_memory_indexing import repository
from app.modules.avatar_memory_indexing.qdrant_writer import (
    AvatarMemoryQdrantWriter,
    DefaultAvatarMemoryQdrantWriter,
)
from app.modules.avatar_memory_indexing.schemas import (
    AvatarMemoryIndexingPreview,
    AvatarMemoryIndexingRead,
)
from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.providers import build_embedding_provider
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.embeddings.providers.bge_m3_hybrid import BgeM3HybridEmbeddingAdapter
from app.modules.embeddings.runtime import assert_real_embedding_runtime_for_e2e
from app.modules.qdrant_indexing import repository as qdrant_index_repository
from app.modules.rag_chunks.validation import estimate_token_count
from app.modules.family_memory_enrichment.eligibility import (
    FINALIZED_MEMORY_FIELD_NAME,
    REQUIRED_TRANSLATION_SOURCE_LANGUAGE,
    REQUIRED_TRANSLATION_TARGET_LANGUAGE,
    FamilyMemoryEligibilityError,
    assert_candidate_eligible_for_promotion,
)
from app.modules.content_translation import repository as content_translation_repository


INDEX_MODEL_CODE = "bge_m3_dense_sparse"
SOURCE_TYPE = "conversation_candidate"
PROVENANCE = "review_approved_conversation_candidate"
MEMORY_STATUS = "verified"
MAX_MEMORY_TEXT_LENGTH = 500
SAFE_FAILURE_MESSAGE = "Approved memory indexing failed"
IMMUTABLE_PAYLOAD_KEYS = (
    "owner_user_id",
    "profile_id",
    "source_id",
    "chunk_id",
    "embedding_id",
    "model_code",
    "text_hash",
    "source_type",
    "avatar_id",
    "candidate_id",
    "promotion_id",
    "memory_status",
    "provenance",
)

logger = get_logger("avatar_memory_indexing")


class AvatarMemoryIndexingNotFoundError(Exception):
    pass


class AvatarMemoryIndexingEligibilityError(Exception):
    pass


class AvatarMemoryIndexingConflictError(Exception):
    pass


class AvatarMemoryIndexingExecutionError(Exception):
    pass


class AvatarMemoryEmbeddingEncoder(Protocol):
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector: ...


class DefaultAvatarMemoryEmbeddingEncoder:
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        provider = build_embedding_provider(model_code=model_code)
        if not isinstance(provider, BgeM3HybridEmbeddingAdapter):
            raise AvatarMemoryIndexingExecutionError(
                "Real BGE-M3 passage embedding provider is unavailable"
            )
        return provider.embed_passage(text, model_code)


@dataclass(frozen=True)
class _IndexingPlan:
    promotion: AvatarMemoryPromotion
    owner: User
    profile: MemoryProfile
    text: str
    model_code: str
    collection_name: str
    point_id: str
    vector_dimension: int


def normalize_memory_text(text: str) -> str:
    normalized = " ".join((text or "").split()).strip()
    if not normalized:
        raise AvatarMemoryIndexingEligibilityError("Approved memory text is empty")
    if len(normalized) > MAX_MEMORY_TEXT_LENGTH:
        raise AvatarMemoryIndexingEligibilityError("Approved memory text is too long")
    return normalized


def build_deterministic_point_id(*, promotion: AvatarMemoryPromotion) -> str:
    identity = (
        f"avatar-memory-promotion:{promotion.id}:{promotion.avatar_id}:"
        f"{promotion.profile_id}:{promotion.source_type}"
    )
    return str(uuid5(NAMESPACE_URL, identity))


def _validate_promotion_identity(db: Session, promotion: AvatarMemoryPromotion) -> tuple[User, MemoryProfile]:
    candidate = promotion.candidate
    if (
        candidate.status != "approved"
        or promotion.source_candidate_status_snapshot != "approved"
    ):
        raise AvatarMemoryIndexingEligibilityError("Promotion source candidate is not approved")
    if candidate.id != promotion.candidate_id or candidate.owner_user_id != promotion.owner_user_id:
        raise AvatarMemoryIndexingEligibilityError("Promotion source identity is invalid")
    if candidate.avatar_id != promotion.avatar_id or candidate.profile_id != promotion.profile_id:
        raise AvatarMemoryIndexingEligibilityError("Promotion target identity is invalid")
    try:
        assert_candidate_eligible_for_promotion(db, candidate=candidate)
    except FamilyMemoryEligibilityError as exc:
        raise AvatarMemoryIndexingEligibilityError("Promotion source candidate is not enrichment-eligible") from exc
    if normalize_memory_text(candidate.finalized_memory_text or "") != normalize_memory_text(
        promotion.approved_memory_text
    ):
        raise AvatarMemoryIndexingConflictError("Finalized candidate text does not match promotion snapshot")
    if promotion.cancelled_at is not None:
        raise AvatarMemoryIndexingEligibilityError("Cancelled promotion cannot be indexed")
    if promotion.profile_id is None:
        raise AvatarMemoryIndexingEligibilityError("Promotion has no target profile")

    owner = db.get(User, promotion.owner_user_id)
    profile = db.get(MemoryProfile, promotion.profile_id)
    if owner is None or profile is None or profile.user_id != promotion.owner_user_id:
        raise AvatarMemoryIndexingEligibilityError("Promotion target profile is invalid")
    return owner, profile


def _build_plan(
    db: Session,
    *,
    promotion: AvatarMemoryPromotion,
    writer: AvatarMemoryQdrantWriter,
) -> _IndexingPlan:
    owner, profile = _validate_promotion_identity(db, promotion)
    text = normalize_memory_text(promotion.normalized_memory_text or promotion.approved_memory_text)
    runtime = resolve_runtime_active_retrieval_config(
        db,
        current_user=owner,
        profile_id=profile.id,
    )
    if runtime.model_code != INDEX_MODEL_CODE:
        raise AvatarMemoryIndexingEligibilityError("Target profile is not configured for BGE-M3 memory retrieval")
    model = get_embedding_model(runtime.model_code)
    if (
        promotion.target_collection_name is not None
        and promotion.target_collection_name != runtime.collection_name
    ):
        raise AvatarMemoryIndexingConflictError("Stored target collection does not match active retrieval")
    collection_dimension = writer.collection_vector_size(collection_name=runtime.collection_name)
    if collection_dimension is None:
        raise AvatarMemoryIndexingEligibilityError("Target memory collection does not exist")
    if collection_dimension != model.dimension:
        raise AvatarMemoryIndexingEligibilityError("Target memory collection has an incompatible dimension")
    return _IndexingPlan(
        promotion=promotion,
        owner=owner,
        profile=profile,
        text=text,
        model_code=runtime.model_code,
        collection_name=runtime.collection_name,
        point_id=build_deterministic_point_id(promotion=promotion),
        vector_dimension=model.dimension,
    )


def preview_promotion_indexing(
    db: Session,
    *,
    owner_user_id: int,
    promotion_id: int,
    writer: AvatarMemoryQdrantWriter | None = None,
) -> AvatarMemoryIndexingPreview:
    promotion = repository.get_promotion_for_owner(
        db,
        owner_user_id=owner_user_id,
        promotion_id=promotion_id,
    )
    if promotion is None:
        raise AvatarMemoryIndexingNotFoundError("Avatar memory promotion not found")
    if promotion.promotion_status != "pending_index":
        raise AvatarMemoryIndexingEligibilityError(
            f"Promotion status `{promotion.promotion_status}` is not eligible for indexing"
        )
    plan = _build_plan(db, promotion=promotion, writer=writer or DefaultAvatarMemoryQdrantWriter())
    return AvatarMemoryIndexingPreview(
        promotion_id=promotion.id,
        candidate_id=promotion.candidate_id,
        avatar_id=promotion.avatar_id,
        profile_id=plan.profile.id,
        target_collection_name=plan.collection_name,
        qdrant_point_id=plan.point_id,
        model_code=plan.model_code,
        text_length=len(plan.text),
    )


def _create_evidence_records(
    db: Session,
    *,
    plan: _IndexingPlan,
    embedding: EmbeddingVector,
) -> tuple[RagSource, RagChunk, RagEmbedding]:
    promotion = plan.promotion
    existing = repository.get_evidence_records(db, promotion=promotion)
    if existing is not None:
        source, chunk, rag_embedding = existing
        expected_text_hash = hashlib.sha256(plan.text.encode("utf-8")).hexdigest()
        if (
            source.owner_user_id != promotion.owner_user_id
            or source.profile_id != plan.profile.id
            or source.source_type != SOURCE_TYPE
            or chunk.owner_user_id != promotion.owner_user_id
            or chunk.profile_id != plan.profile.id
            or chunk.source_id != source.id
            or chunk.chunk_text != plan.text
            or chunk.text_hash != expected_text_hash
            or rag_embedding.owner_user_id != promotion.owner_user_id
            or rag_embedding.profile_id != plan.profile.id
            or rag_embedding.source_id != source.id
            or rag_embedding.chunk_id != chunk.id
            or rag_embedding.model_code != plan.model_code
            or rag_embedding.text_hash != expected_text_hash
            or rag_embedding.status != "embedded"
            or rag_embedding.vector_dimension != plan.vector_dimension
            or not isinstance(rag_embedding.vector, list)
            or len(rag_embedding.vector) != plan.vector_dimension
        ):
            raise AvatarMemoryIndexingConflictError("Stored promotion evidence does not match approved memory")
        return existing

    text_hash = hashlib.sha256(plan.text.encode("utf-8")).hexdigest()
    metadata = {
        "avatar_id": promotion.avatar_id,
        "candidate_id": promotion.candidate_id,
        "promotion_id": promotion.id,
        "memory_status": MEMORY_STATUS,
        "provenance": PROVENANCE,
    }
    source = RagSource(
        owner_user_id=promotion.owner_user_id,
        profile_id=plan.profile.id,
        source_type=SOURCE_TYPE,
        title="Approved conversation memory",
        raw_text=plan.text,
        normalized_text=plan.text,
        language=promotion.language,
        status="embedded",
        processing_error=None,
        source_metadata=metadata,
    )
    db.add(source)
    db.flush()
    sentence_count = max(1, len(re.findall(r"[.!?…]+", plan.text)))
    chunk = RagChunk(
        owner_user_id=promotion.owner_user_id,
        profile_id=plan.profile.id,
        source_id=source.id,
        chunk_index=0,
        chunk_text=plan.text,
        text_hash=text_hash,
        token_estimate=estimate_token_count(plan.text),
        char_count=len(plan.text),
        sentence_count=sentence_count,
        language=promotion.language,
        chunk_metadata={**metadata, "chunk_id": f"promotion:{promotion.id}:0"},
        validation_status="valid",
        validation_errors=[],
    )
    db.add(chunk)
    db.flush()
    rag_embedding = RagEmbedding(
        owner_user_id=promotion.owner_user_id,
        profile_id=plan.profile.id,
        source_id=source.id,
        chunk_id=chunk.id,
        model_code=plan.model_code,
        vector=list(embedding.values),
        vector_dimension=embedding.dimension,
        text_hash=text_hash,
        status="embedded",
        error_message=None,
        embedding_metadata={**embedding.metadata, **metadata, "input_type": "passage"},
    )
    db.add(rag_embedding)
    db.flush()
    promotion.rag_source_id = source.id
    promotion.rag_chunk_id = chunk.id
    promotion.rag_embedding_id = rag_embedding.id
    return source, chunk, rag_embedding


def _build_payload(
    db: Session,
    *,
    plan: _IndexingPlan,
    source: RagSource,
    chunk: RagChunk,
    embedding: RagEmbedding,
    indexed_at: datetime,
) -> dict[str, object]:
    promotion = plan.promotion
    payload: dict[str, object] = {
        "owner_user_id": promotion.owner_user_id,
        "profile_id": plan.profile.id,
        "source_id": source.id,
        "chunk_id": chunk.id,
        "embedding_id": embedding.id,
        "model_code": plan.model_code,
        "text_hash": chunk.text_hash,
        "language": promotion.language,
        "validation_status": "valid",
        "source_type": SOURCE_TYPE,
        "chunk_index": 0,
        "indexed_at": indexed_at.isoformat(),
        "avatar_id": promotion.avatar_id,
        "candidate_id": promotion.candidate_id,
        "promotion_id": promotion.id,
        "memory_status": MEMORY_STATUS,
        "provenance": PROVENANCE,
        "created_at": promotion.created_at.isoformat(),
        "approved_at": (
            promotion.candidate.reviewed_at.isoformat()
            if promotion.candidate.reviewed_at is not None
            else None
        ),
        "chunk_source_id": f"promotion:{promotion.id}:0",
        "source_title": source.title,
        "privacy_scope": promotion.candidate.privacy_scope,
        "workflow_version": promotion.candidate.workflow_version,
        "dispute_status": promotion.candidate.dispute_status,
    }
    if promotion.candidate.language == REQUIRED_TRANSLATION_SOURCE_LANGUAGE:
        # Czech-origin memory: the Russian avatar pipeline indexes the
        # translated text (see _resolve_normalized_memory_text), so the
        # payload records both the Czech source language and translation
        # provenance - without embedding the full private Czech source text
        # itself in the Qdrant payload (Part 25).
        payload["source_language"] = REQUIRED_TRANSLATION_SOURCE_LANGUAGE
        payload["indexed_language"] = REQUIRED_TRANSLATION_TARGET_LANGUAGE
        translation_row = content_translation_repository.get_current(
            db,
            entity_type="memory_candidate",
            entity_id=str(promotion.candidate_id),
            field_name=FINALIZED_MEMORY_FIELD_NAME,
            target_language=REQUIRED_TRANSLATION_TARGET_LANGUAGE,
        )
        if translation_row is not None:
            payload["translation_status"] = translation_row.translation_status
            payload["translation_version"] = translation_row.translation_version
            payload["source_text_hash"] = translation_row.source_hash
    sparse_vector = (embedding.embedding_metadata or {}).get("sparse_vector")
    if isinstance(sparse_vector, dict):
        payload["sparse_vector"] = sparse_vector
    return payload


def _point_payload(point: dict[str, object] | None) -> dict[str, object] | None:
    if point is None:
        return None
    payload = point.get("payload")
    return payload if isinstance(payload, dict) else None


def _payload_matches(existing: dict[str, object], expected: dict[str, object]) -> bool:
    return all(existing.get(key) == expected.get(key) for key in IMMUTABLE_PAYLOAD_KEYS)


def _upsert_vector_index_record(
    db: Session,
    *,
    plan: _IndexingPlan,
    source: RagSource,
    chunk: RagChunk,
    embedding: RagEmbedding,
    indexed_at: datetime,
) -> None:
    record = qdrant_index_repository.get_vector_index_for_embedding_and_collection(
        db,
        embedding_id=embedding.id,
        qdrant_collection=plan.collection_name,
    )
    if record is None:
        record = qdrant_index_repository.create_rag_vector_index(
            db,
            owner_user_id=plan.promotion.owner_user_id,
            profile_id=plan.profile.id,
            source_id=source.id,
            chunk_id=chunk.id,
            embedding_id=embedding.id,
            model_code=plan.model_code,
            qdrant_collection=plan.collection_name,
            qdrant_point_id=plan.point_id,
            status="indexed",
            error_message=None,
            indexed_at=indexed_at,
        )
    else:
        record.status = "indexed"
        record.error_message = None
        record.indexed_at = indexed_at
        record.qdrant_point_id = plan.point_id


def _mark_failed(
    db: Session,
    *,
    promotion_id: int,
    collection_name: str | None,
    point_id: str | None,
    error: Exception,
    increment_attempt: bool,
    preserve_if_indexed: bool,
) -> None:
    db.rollback()
    promotion = db.scalar(
        select(AvatarMemoryPromotion)
        .where(AvatarMemoryPromotion.id == promotion_id)
        .with_for_update()
    )
    if promotion is None:
        return
    if promotion.promotion_status == "cancelled" or (
        preserve_if_indexed and promotion.promotion_status == "indexed"
    ):
        db.rollback()
        return
    if increment_attempt:
        promotion.indexing_attempt_count += 1
    promotion.promotion_status = "failed"
    promotion.failed_at = datetime.now(timezone.utc)
    promotion.indexed_at = None
    promotion.failure_reason = SAFE_FAILURE_MESSAGE
    promotion.target_collection_name = collection_name
    promotion.qdrant_point_id = point_id
    db.commit()
    observe_memory_promotion_status(status="failed")
    log_event(
        logger,
        logging.ERROR,
        "avatar_memory_indexing_failed",
        trace_id=promotion.trace_id,
        promotion_id=promotion.id,
        candidate_id=promotion.candidate_id,
        target_collection_name=collection_name,
        qdrant_point_id=point_id,
        status="failed",
        error_type=error.__class__.__name__,
    )


def _build_read(promotion: AvatarMemoryPromotion, *, result: str) -> AvatarMemoryIndexingRead:
    return AvatarMemoryIndexingRead(
        promotion_id=promotion.id,
        promotion_status=promotion.promotion_status,
        indexed_at=promotion.indexed_at,
        target_collection_name=promotion.target_collection_name,
        qdrant_point_id=promotion.qdrant_point_id,
        searchable_as_fact=promotion.promotion_status == "indexed",
        result=result,
    )


def index_promotion(
    db: Session,
    *,
    owner_user_id: int,
    promotion_id: int,
    writer: AvatarMemoryQdrantWriter | None = None,
    encoder: AvatarMemoryEmbeddingEncoder | None = None,
    validate_runtime: bool = True,
) -> AvatarMemoryIndexingRead:
    started_at = perf_counter()
    observe_memory_indexing_started()
    actual_writer = writer or DefaultAvatarMemoryQdrantWriter()
    promotion = repository.get_promotion_for_owner(
        db,
        owner_user_id=owner_user_id,
        promotion_id=promotion_id,
        for_update=True,
    )
    if promotion is None:
        observe_memory_indexing_finished(result="skipped", duration_seconds=perf_counter() - started_at)
        raise AvatarMemoryIndexingNotFoundError("Avatar memory promotion not found")
    if promotion.promotion_status not in {"pending_index", "indexed"}:
        observe_memory_indexing_finished(result="skipped", duration_seconds=perf_counter() - started_at)
        raise AvatarMemoryIndexingEligibilityError(
            f"Promotion status `{promotion.promotion_status}` is not eligible for indexing"
        )
    started_status = promotion.promotion_status

    collection_name: str | None = promotion.target_collection_name
    point_id: str | None = promotion.qdrant_point_id
    wrote_new_point = False
    try:
        plan = _build_plan(db, promotion=promotion, writer=actual_writer)
        collection_name = plan.collection_name
        point_id = plan.point_id
        existing_records = repository.get_evidence_records(db, promotion=promotion)

        if promotion.promotion_status == "pending_index":
            promotion.indexing_attempt_count += 1
            promotion.target_collection_name = plan.collection_name
            promotion.qdrant_point_id = plan.point_id

        if promotion.promotion_status == "indexed" and existing_records is None:
            raise AvatarMemoryIndexingConflictError("Indexed promotion evidence is missing")

        if existing_records is None:
            if validate_runtime:
                assert_real_embedding_runtime_for_e2e(
                    model_code=plan.model_code,
                    collection_name=plan.collection_name,
                )
            encoded = (encoder or DefaultAvatarMemoryEmbeddingEncoder()).encode(
                text=plan.text,
                model_code=plan.model_code,
            )
            if encoded.dimension != plan.vector_dimension or len(encoded.values) != plan.vector_dimension:
                raise AvatarMemoryIndexingExecutionError("Memory embedding dimension is invalid")
            source, chunk, rag_embedding = _create_evidence_records(
                db,
                plan=plan,
                embedding=encoded,
            )
        else:
            source, chunk, rag_embedding = existing_records

        indexed_at = promotion.indexed_at or datetime.now(timezone.utc)
        payload = _build_payload(
            db,
            plan=plan,
            source=source,
            chunk=chunk,
            embedding=rag_embedding,
            indexed_at=indexed_at,
        )
        existing_point = actual_writer.get_point(
            collection_name=plan.collection_name,
            point_id=plan.point_id,
        )
        existing_payload = _point_payload(existing_point)
        if existing_point is not None and existing_payload is None:
            raise AvatarMemoryIndexingConflictError("Deterministic Qdrant point payload is invalid")
        if existing_payload is not None and not _payload_matches(existing_payload, payload):
            raise AvatarMemoryIndexingConflictError("Deterministic Qdrant point payload conflicts")
        if existing_payload is None:
            if not rag_embedding.vector:
                raise AvatarMemoryIndexingExecutionError("Stored memory embedding is unavailable")
            actual_writer.upsert_point(
                collection_name=plan.collection_name,
                point_id=plan.point_id,
                vector=list(rag_embedding.vector),
                payload=payload,
            )
            wrote_new_point = True
            result = "indexed"
        else:
            stored_indexed_at = existing_payload.get("indexed_at")
            if isinstance(stored_indexed_at, str):
                try:
                    indexed_at = datetime.fromisoformat(stored_indexed_at)
                except ValueError:
                    pass
            result = "already_indexed"

        promotion.promotion_status = "indexed"
        promotion.indexed_at = indexed_at
        promotion.failed_at = None
        promotion.failure_reason = None
        promotion.target_collection_name = plan.collection_name
        promotion.qdrant_point_id = plan.point_id
        _upsert_vector_index_record(
            db,
            plan=plan,
            source=source,
            chunk=chunk,
            embedding=rag_embedding,
            indexed_at=indexed_at,
        )
        try:
            db.commit()
        except Exception:
            db.rollback()
            if wrote_new_point:
                try:
                    actual_writer.delete_point(
                        collection_name=plan.collection_name,
                        point_id=plan.point_id,
                    )
                except Exception as compensation_error:
                    log_event(
                        logger,
                        logging.ERROR,
                        "avatar_memory_indexing_compensation_failed",
                        promotion_id=promotion_id,
                        target_collection_name=plan.collection_name,
                        qdrant_point_id=plan.point_id,
                        error_type=compensation_error.__class__.__name__,
                    )
            raise
        db.refresh(promotion)
        if started_status != "indexed":
            observe_memory_promotion_status(status="indexed")
        metric_result = "indexed" if started_status != "indexed" or wrote_new_point else "skipped"
        observe_memory_indexing_finished(
            result=metric_result,
            duration_seconds=perf_counter() - started_at,
        )
        log_event(
            logger,
            logging.INFO,
            "avatar_memory_indexing_completed",
            trace_id=promotion.trace_id,
            promotion_id=promotion.id,
            candidate_id=promotion.candidate_id,
            target_collection_name=plan.collection_name,
            qdrant_point_id=plan.point_id,
            status="indexed",
            duration_ms=round((perf_counter() - started_at) * 1000, 2),
            result=result,
        )
        return _build_read(promotion, result=result)
    except (AvatarMemoryIndexingEligibilityError, AvatarMemoryIndexingNotFoundError):
        observe_memory_indexing_finished(result="skipped", duration_seconds=perf_counter() - started_at)
        raise
    except AvatarMemoryIndexingConflictError as exc:
        _mark_failed(
            db,
            promotion_id=promotion_id,
            collection_name=collection_name,
            point_id=point_id,
            error=exc,
            increment_attempt=started_status == "pending_index",
            preserve_if_indexed=started_status == "pending_index",
        )
        observe_memory_indexing_finished(result="failed", duration_seconds=perf_counter() - started_at)
        raise
    except Exception as exc:
        _mark_failed(
            db,
            promotion_id=promotion_id,
            collection_name=collection_name,
            point_id=point_id,
            error=exc,
            increment_attempt=started_status == "pending_index",
            preserve_if_indexed=started_status == "pending_index",
        )
        observe_memory_indexing_finished(result="failed", duration_seconds=perf_counter() - started_at)
        if isinstance(exc, AvatarMemoryIndexingExecutionError):
            raise
        raise AvatarMemoryIndexingExecutionError(SAFE_FAILURE_MESSAGE) from exc

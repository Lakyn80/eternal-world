"""Bridges an approved+current `MemorialContribution` into the existing
canonical memory / embedding / indexing pipeline.

This intentionally mirrors `app.modules.avatar_memory_indexing.service`
(the established "approved candidate -> promotion -> RagSource/RagChunk/
RagEmbedding -> Qdrant" pattern for this codebase) rather than inventing a
second embedding system. Two phases, same split as the avatar pipeline:

  * `promote_contribution` - lightweight, DB-only, idempotent get-or-create
    of a `MemorialContributionPromotion` row. Safe to call from inside the
    same request that just committed the approval.
  * `index_contribution_promotion` - the heavy step (embedding provider +
    Qdrant write). Idempotent via a deterministic Qdrant point id and by
    reusing already-created RagSource/RagChunk/RagEmbedding rows on retry.
    Never performs a blocking model load inside the *approval* transaction -
    callers invoke it as a separate step after the approval commit.

`retire_contribution_promotion` removes the Qdrant point (and stops the
promotion from being retryable as "indexed") when the source contribution
is later archived or superseded, without deleting the historical SQL
lineage rows - satisfying the "old evidence must not remain retrievable"
requirement while preserving an audit trail.
"""

from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from time import perf_counter
from typing import Protocol
from uuid import NAMESPACE_URL, uuid5

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_logger, log_event
from app.db.models import (
    MemorialContribution,
    MemorialContributionPromotion,
    MemoryProfile,
    RagChunk,
    RagEmbedding,
    RagSource,
    User,
)
from app.modules.active_retrieval_config.service import resolve_runtime_active_retrieval_config
from app.modules.content_translation.enums import CURRENT_USABLE_TRANSLATION_STATUSES
from app.modules.content_translation.repository import get_current as get_current_translation
from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.providers import build_embedding_provider
from app.modules.language_registry import (
    assert_canonical_memorial_language,
    assert_translation_language,
)
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.embeddings.providers.bge_m3_hybrid import BgeM3HybridEmbeddingAdapter
from app.modules.embeddings.runtime import assert_real_embedding_runtime_for_e2e
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.memorial_contribution_indexing import repository
from app.modules.memorial_contribution_indexing.schemas import ContributionIndexingRead
from app.modules.avatar_memory_indexing.qdrant_writer import (
    AvatarMemoryQdrantWriter as MemorialContributionQdrantWriter,
    DefaultAvatarMemoryQdrantWriter as DefaultMemorialContributionQdrantWriter,
)
from app.modules.qdrant_indexing import repository as qdrant_index_repository
from app.modules.qdrant_indexing.memory_collection import resolve_or_create_collection_dimension
from app.modules.rag_chunks.validation import estimate_token_count


INDEXING_JOB_WORKFLOW = "memorial_contribution_indexing"


INDEX_MODEL_CODE = "bge_m3_dense_sparse"
SOURCE_TYPE = "manual_text"
PROVENANCE = "review_approved_memorial_contribution"
MEMORY_STATUS = "verified"
MAX_MEMORY_TEXT_LENGTH = 5000
SAFE_FAILURE_MESSAGE = "Contribution indexing failed"
IMMUTABLE_PAYLOAD_KEYS = (
    "owner_user_id",
    "profile_id",
    "source_id",
    "chunk_id",
    "embedding_id",
    "model_code",
    "text_hash",
    "source_type",
    "contribution_id",
    "promotion_id",
    "memory_status",
    "provenance",
)

logger = get_logger("memorial_contribution_indexing")


class ContributionIndexingNotFoundError(Exception):
    pass


class ContributionIndexingEligibilityError(Exception):
    pass


class ContributionIndexingConflictError(Exception):
    pass


class ContributionIndexingExecutionError(Exception):
    pass


class ContributionIndexingEmbeddingEncoder(Protocol):
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector: ...


class DefaultContributionIndexingEmbeddingEncoder:
    """Task 65.9 (Part M): see `avatar_memory_indexing.service.
    DefaultAvatarMemoryEmbeddingEncoder` for the full rationale - identical
    pattern, kept independent per module rather than sharing a base class,
    matching this codebase's existing convention of small parallel encoder
    classes per pipeline."""

    def __init__(self, *, self_healing_encoder: object | None = None) -> None:
        self._self_healing_encoder = self_healing_encoder

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        if self._self_healing_encoder is not None:
            from app.modules.embeddings.self_healing import ProviderRecoveryExhaustedError

            try:
                return self._self_healing_encoder.encode(text=text, model_code=model_code)
            except ProviderRecoveryExhaustedError as exc:
                raise ContributionIndexingExecutionError(SAFE_FAILURE_MESSAGE) from exc

        provider = build_embedding_provider(model_code=model_code)
        if not isinstance(provider, BgeM3HybridEmbeddingAdapter):
            raise ContributionIndexingExecutionError(
                "Real BGE-M3 passage embedding provider is unavailable"
            )
        return provider.embed_passage(text, model_code)


@dataclass(frozen=True)
class PromotionCreateOutcome:
    promotion: MemorialContributionPromotion
    created: bool


@dataclass(frozen=True)
class _IndexingPlan:
    promotion: MemorialContributionPromotion
    profile: MemoryProfile
    owner: User
    text: str
    model_code: str
    collection_name: str
    point_id: str
    vector_dimension: int


def normalize_memory_text(text: str) -> str:
    normalized = " ".join((text or "").split()).strip()
    if not normalized:
        raise ContributionIndexingEligibilityError("Approved contribution text is empty")
    if len(normalized) > MAX_MEMORY_TEXT_LENGTH:
        raise ContributionIndexingEligibilityError("Approved contribution text is too long")
    return normalized


def resolve_indexable_contribution_text(
    db: Session,
    *,
    contribution: MemorialContribution,
    profile: MemoryProfile,
) -> tuple[str, str]:
    """Return ``(text, language)`` that may be embedded into RAG.

    Task 65.13.6: with ``canonical_only_rag_indexing`` enabled (default),
    only memorial-canonical text is indexable. Same-language contributions
    use the durable original; cross-language contributions require a usable
    MCT canonical translation (fail closed — never index a foreign original).
    """

    if not settings.canonical_only_rag_indexing:
        # Emergency rollback path: legacy original-text indexing.
        return contribution.memory_text, contribution.source_language

    # Lazy import: contribution_translations → content_translation.service, and
    # memorial_access.service already imports this module at startup.
    from app.modules.memorial_access.contribution_translations import (
        ENTITY_MEMORIAL_CONTRIBUTION,
        FIELD_MEMORY_TEXT,
        ensure_contribution_translation,
    )

    canonical = assert_canonical_memorial_language(profile.canonical_language)
    source = assert_translation_language(contribution.source_language)
    if source == canonical:
        return contribution.memory_text, canonical

    row = get_current_translation(
        db,
        entity_type=ENTITY_MEMORIAL_CONTRIBUTION,
        entity_id=str(contribution.id),
        field_name=FIELD_MEMORY_TEXT,
        target_language=canonical,
    )
    if row is None:
        owner = db.get(User, profile.user_id)
        if owner is None:
            raise ContributionIndexingEligibilityError(
                "Canonical translation is required before indexing foreign-language contributions"
            )
        row = ensure_contribution_translation(
            db,
            contribution=contribution,
            target_language=canonical,
            actor=owner,
        )
        db.flush()

    if (
        row is not None
        and row.translation_status in CURRENT_USABLE_TRANSLATION_STATUSES
        and row.translated_text
        and str(row.translated_text).strip()
    ):
        return row.translated_text, canonical

    raise ContributionIndexingEligibilityError(
        "Canonical translation is required before indexing foreign-language contributions"
    )


def build_deterministic_point_id(*, promotion: MemorialContributionPromotion) -> str:
    identity = f"memorial-contribution-promotion:{promotion.id}:{promotion.profile_id}"
    return str(uuid5(NAMESPACE_URL, identity))


def promote_contribution(
    db: Session,
    *,
    contribution: MemorialContribution,
) -> PromotionCreateOutcome:
    """Idempotently create the promotion row for an approved+current
    contribution. Safe to call multiple times (e.g. on repeated approval
    requests) - always returns the same row for the same contribution."""

    if contribution.status != "approved" or not contribution.is_current:
        raise ContributionIndexingEligibilityError(
            "Only approved, current contributions can be promoted for indexing"
        )

    existing = repository.get_promotion_by_contribution_id(db, contribution_id=contribution.id)
    if existing is not None:
        return PromotionCreateOutcome(promotion=existing, created=False)

    profile = db.get(MemoryProfile, contribution.profile_id)
    if profile is None:
        raise ContributionIndexingEligibilityError("Promotion target profile is invalid")

    index_text, index_language = resolve_indexable_contribution_text(
        db,
        contribution=contribution,
        profile=profile,
    )
    normalized_text = normalize_memory_text(index_text)
    promotion = repository.create_promotion(
        db,
        contribution_id=contribution.id,
        profile_id=contribution.profile_id,
        promotion_status="pending_index",
        approved_memory_text=index_text,
        normalized_memory_text=normalized_text,
        language=index_language,
        source_contribution_status_snapshot=contribution.status,
    )
    db.flush()
    return PromotionCreateOutcome(promotion=promotion, created=True)


def enqueue_indexing_job(
    db: Session,
    *,
    profile: MemoryProfile,
    promotion: MemorialContributionPromotion,
):
    """Create the persistent job and its transactional outbox record for
    the heavy embedding/Qdrant step, instead of running it inline inside
    the HTTP request that just approved the contribution (Task 65.9, Part
    E/F/I) - satisfies "no large blocking model load inside the approval
    transaction" while still making indexing happen automatically, and
    guarantees it is never silently lost if the broker publish itself
    fails. Reuses the existing `background_jobs` job-tracking
    infrastructure (`job_type="qdrant_indexing"`, the closest existing
    enum value to what this job actually does) rather than inventing a
    parallel job model.

    Idempotency key mirrors `avatar_memory_indexing.service.
    enqueue_indexing_job`: one `MemorialContributionPromotion` row is
    always exactly one approved content version, so repeated approval,
    the explicit retry-indexing action, and duplicate delivery all
    converge on the same job.
    """

    idempotency_key = f"{INDEXING_JOB_WORKFLOW}:{promotion.id}:index"
    background_job = create_job(
        db,
        owner_user_id=profile.user_id,
        profile_id=profile.id,
        job_type=BackgroundJobType.QDRANT_INDEXING,
        input_payload={
            "workflow": INDEXING_JOB_WORKFLOW,
            "contribution_id": promotion.contribution_id,
            "promotion_id": promotion.id,
        },
        queue="embedding",
        idempotency_key=idempotency_key,
    )

    from app.modules.job_outbox.service import enqueue_job_with_outbox

    return enqueue_job_with_outbox(
        db,
        job=background_job,
        task_name="app.worker.tasks.run_memorial_contribution_indexing_job",
        queue="embedding",
    )


def _validate_promotion_identity(
    db: Session,
    promotion: MemorialContributionPromotion,
) -> tuple[MemoryProfile, User]:
    contribution = promotion.contribution
    if contribution is None or contribution.id != promotion.contribution_id:
        raise ContributionIndexingEligibilityError("Promotion source identity is invalid")
    if contribution.profile_id != promotion.profile_id:
        raise ContributionIndexingEligibilityError("Promotion target identity is invalid")
    if contribution.status != "approved" or not contribution.is_current:
        # A later archive/supersede must retire the promotion instead of
        # indexing it - see retire_contribution_promotion.
        raise ContributionIndexingEligibilityError("Source contribution is no longer approved/current")

    profile = db.get(MemoryProfile, promotion.profile_id)
    if profile is None:
        raise ContributionIndexingEligibilityError("Promotion target profile is invalid")

    # Task 65.13.6: approved_memory_text is the index snapshot (canonical when
    # enabled), not necessarily the durable contribution original.
    expected_text, _expected_language = resolve_indexable_contribution_text(
        db,
        contribution=contribution,
        profile=profile,
    )
    if normalize_memory_text(expected_text) != normalize_memory_text(promotion.approved_memory_text):
        raise ContributionIndexingConflictError("Contribution text does not match promotion snapshot")

    owner = db.get(User, profile.user_id)
    if owner is None:
        raise ContributionIndexingEligibilityError("Promotion target profile owner is invalid")
    return profile, owner


def _build_plan(
    db: Session,
    *,
    promotion: MemorialContributionPromotion,
    writer: MemorialContributionQdrantWriter,
) -> _IndexingPlan:
    profile, owner = _validate_promotion_identity(db, promotion)
    text = normalize_memory_text(promotion.normalized_memory_text or promotion.approved_memory_text)
    runtime = resolve_runtime_active_retrieval_config(
        db,
        current_user=owner,
        profile_id=profile.id,
    )
    if runtime.model_code != INDEX_MODEL_CODE:
        raise ContributionIndexingEligibilityError(
            "Target profile is not configured for BGE-M3 memory retrieval"
        )
    model = get_embedding_model(runtime.model_code)
    if (
        promotion.target_collection_name is not None
        and promotion.target_collection_name != runtime.collection_name
    ):
        raise ContributionIndexingConflictError("Stored target collection does not match active retrieval")
    collection_dimension = resolve_or_create_collection_dimension(
        writer,
        collection_name=runtime.collection_name,
        vector_size=model.dimension,
    )
    if collection_dimension is None:
        raise ContributionIndexingEligibilityError("Target memory collection does not exist")
    if collection_dimension != model.dimension:
        raise ContributionIndexingEligibilityError("Target memory collection has an incompatible dimension")
    return _IndexingPlan(
        promotion=promotion,
        profile=profile,
        owner=owner,
        text=text,
        model_code=runtime.model_code,
        collection_name=runtime.collection_name,
        point_id=build_deterministic_point_id(promotion=promotion),
        vector_dimension=model.dimension,
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
            source.owner_user_id != plan.owner.id
            or source.profile_id != plan.profile.id
            or chunk.source_id != source.id
            or chunk.chunk_text != plan.text
            or chunk.text_hash != expected_text_hash
            or rag_embedding.source_id != source.id
            or rag_embedding.chunk_id != chunk.id
            or rag_embedding.model_code != plan.model_code
            or rag_embedding.text_hash != expected_text_hash
            or rag_embedding.status != "embedded"
            or rag_embedding.vector_dimension != plan.vector_dimension
            or not isinstance(rag_embedding.vector, list)
            or len(rag_embedding.vector) != plan.vector_dimension
        ):
            raise ContributionIndexingConflictError("Stored promotion evidence does not match approved memory")
        return existing

    text_hash = hashlib.sha256(plan.text.encode("utf-8")).hexdigest()
    metadata = {
        "contribution_id": promotion.contribution_id,
        "promotion_id": promotion.id,
        "memory_status": MEMORY_STATUS,
        "provenance": PROVENANCE,
        "contribution_author_user_id": promotion.contribution.author_user_id,
        "contribution_reviewed_by_user_id": promotion.contribution.reviewed_by_user_id,
    }
    source = RagSource(
        owner_user_id=plan.owner.id,
        profile_id=plan.profile.id,
        source_type=SOURCE_TYPE,
        title=promotion.contribution.title,
        raw_text=plan.text,
        normalized_text=plan.text,
        language=promotion.language,
        status="embedded",
        processing_error=None,
        source_metadata=metadata,
    )
    db.add(source)
    db.flush()
    chunk = RagChunk(
        owner_user_id=plan.owner.id,
        profile_id=plan.profile.id,
        source_id=source.id,
        chunk_index=0,
        chunk_text=plan.text,
        text_hash=text_hash,
        token_estimate=estimate_token_count(plan.text),
        char_count=len(plan.text),
        sentence_count=max(1, plan.text.count(".") + plan.text.count("!") + plan.text.count("?") or 1),
        language=promotion.language,
        chunk_metadata={**metadata, "chunk_id": f"contribution-promotion:{promotion.id}:0"},
        validation_status="valid",
        validation_errors=[],
    )
    db.add(chunk)
    db.flush()
    rag_embedding = RagEmbedding(
        owner_user_id=plan.owner.id,
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
    *,
    plan: _IndexingPlan,
    source: RagSource,
    chunk: RagChunk,
    embedding: RagEmbedding,
    indexed_at: datetime,
) -> dict[str, object]:
    promotion = plan.promotion
    contribution = promotion.contribution
    payload: dict[str, object] = {
        "owner_user_id": plan.owner.id,
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
        "contribution_id": promotion.contribution_id,
        "promotion_id": promotion.id,
        "memory_status": MEMORY_STATUS,
        "provenance": PROVENANCE,
        "created_at": promotion.created_at.isoformat(),
        "approved_at": contribution.reviewed_at.isoformat() if contribution.reviewed_at else None,
        "chunk_source_id": f"contribution-promotion:{promotion.id}:0",
        "source_title": source.title,
        "privacy_scope": contribution.privacy_scope,
        "contribution_author_user_id": contribution.author_user_id,
        "contribution_reviewed_by_user_id": contribution.reviewed_by_user_id,
    }
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
        qdrant_index_repository.create_rag_vector_index(
            db,
            owner_user_id=plan.owner.id,
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
) -> None:
    db.rollback()
    promotion = db.scalar(
        select(MemorialContributionPromotion)
        .where(MemorialContributionPromotion.id == promotion_id)
        .with_for_update()
    )
    if promotion is None:
        return
    if promotion.promotion_status in {"retired", "indexed"}:
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
    log_event(
        logger,
        logging.ERROR,
        "memorial_contribution_indexing_failed",
        promotion_id=promotion.id,
        contribution_id=promotion.contribution_id,
        profile_id=promotion.profile_id,
        target_collection_name=collection_name,
        qdrant_point_id=point_id,
        status="failed",
        error_type=error.__class__.__name__,
    )


def _build_read(promotion: MemorialContributionPromotion, *, result: str) -> ContributionIndexingRead:
    return ContributionIndexingRead(
        promotion_id=promotion.id,
        contribution_id=promotion.contribution_id,
        promotion_status=promotion.promotion_status,
        indexed_at=promotion.indexed_at,
        target_collection_name=promotion.target_collection_name,
        qdrant_point_id=promotion.qdrant_point_id,
        searchable_as_fact=promotion.promotion_status == "indexed",
        result=result,
    )


def index_contribution_promotion(
    db: Session,
    *,
    profile_id: int,
    promotion_id: int,
    writer: MemorialContributionQdrantWriter | None = None,
    encoder: ContributionIndexingEmbeddingEncoder | None = None,
    validate_runtime: bool = True,
) -> ContributionIndexingRead:
    """Embed and index one contribution promotion. Idempotent: calling this
    again for an already-`indexed` promotion re-validates and returns
    `result="already_indexed"` without writing a duplicate point, chunk,
    embedding, or vector-index row."""

    started_at = perf_counter()
    actual_writer = writer or DefaultMemorialContributionQdrantWriter()
    promotion = repository.get_promotion_for_profile(
        db,
        profile_id=profile_id,
        promotion_id=promotion_id,
        for_update=True,
    )
    if promotion is None:
        raise ContributionIndexingNotFoundError("Contribution promotion not found")
    if promotion.promotion_status not in {"pending_index", "indexed", "failed"}:
        raise ContributionIndexingEligibilityError(
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

        if promotion.promotion_status in {"pending_index", "failed"}:
            promotion.indexing_attempt_count += 1
            promotion.target_collection_name = plan.collection_name
            promotion.qdrant_point_id = plan.point_id

        if promotion.promotion_status == "indexed" and existing_records is None:
            raise ContributionIndexingConflictError("Indexed promotion evidence is missing")

        if existing_records is None:
            if validate_runtime:
                assert_real_embedding_runtime_for_e2e(
                    model_code=plan.model_code,
                    collection_name=plan.collection_name,
                )
            encoded = (encoder or DefaultContributionIndexingEmbeddingEncoder()).encode(
                text=plan.text,
                model_code=plan.model_code,
            )
            if encoded.dimension != plan.vector_dimension or len(encoded.values) != plan.vector_dimension:
                raise ContributionIndexingExecutionError("Contribution embedding dimension is invalid")
            source, chunk, rag_embedding = _create_evidence_records(db, plan=plan, embedding=encoded)
        else:
            source, chunk, rag_embedding = existing_records

        indexed_at = promotion.indexed_at or datetime.now(timezone.utc)
        payload = _build_payload(plan=plan, source=source, chunk=chunk, embedding=rag_embedding, indexed_at=indexed_at)
        existing_point = actual_writer.get_point(collection_name=plan.collection_name, point_id=plan.point_id)
        existing_payload = _point_payload(existing_point)
        if existing_point is not None and existing_payload is None:
            raise ContributionIndexingConflictError("Deterministic Qdrant point payload is invalid")
        if existing_payload is not None and not _payload_matches(existing_payload, payload):
            raise ContributionIndexingConflictError("Deterministic Qdrant point payload conflicts")

        if existing_payload is None:
            if not rag_embedding.vector:
                raise ContributionIndexingExecutionError("Stored contribution embedding is unavailable")
            actual_writer.upsert_point(
                collection_name=plan.collection_name,
                point_id=plan.point_id,
                vector=list(rag_embedding.vector),
                payload=payload,
            )
            wrote_new_point = True
            result = "indexed"
        else:
            result = "already_indexed"

        promotion.promotion_status = "indexed"
        promotion.indexed_at = indexed_at
        promotion.failed_at = None
        promotion.failure_reason = None
        promotion.target_collection_name = plan.collection_name
        promotion.qdrant_point_id = plan.point_id
        _upsert_vector_index_record(db, plan=plan, source=source, chunk=chunk, embedding=rag_embedding, indexed_at=indexed_at)
        try:
            db.commit()
        except Exception:
            db.rollback()
            if wrote_new_point:
                try:
                    actual_writer.delete_point(collection_name=plan.collection_name, point_id=plan.point_id)
                except Exception as compensation_error:
                    log_event(
                        logger,
                        logging.ERROR,
                        "memorial_contribution_indexing_compensation_failed",
                        promotion_id=promotion_id,
                        target_collection_name=plan.collection_name,
                        qdrant_point_id=plan.point_id,
                        error_type=compensation_error.__class__.__name__,
                    )
            raise
        db.refresh(promotion)
        log_event(
            logger,
            logging.INFO,
            "memorial_contribution_indexing_completed",
            promotion_id=promotion.id,
            contribution_id=promotion.contribution_id,
            profile_id=promotion.profile_id,
            target_collection_name=plan.collection_name,
            qdrant_point_id=plan.point_id,
            status="indexed",
            duration_ms=round((perf_counter() - started_at) * 1000, 2),
            result=result,
        )
        return _build_read(promotion, result=result)
    except (ContributionIndexingEligibilityError, ContributionIndexingNotFoundError):
        raise
    except ContributionIndexingConflictError as exc:
        _mark_failed(
            db,
            promotion_id=promotion_id,
            collection_name=collection_name,
            point_id=point_id,
            error=exc,
            increment_attempt=started_status in {"pending_index", "failed"},
        )
        raise
    except Exception as exc:
        _mark_failed(
            db,
            promotion_id=promotion_id,
            collection_name=collection_name,
            point_id=point_id,
            error=exc,
            increment_attempt=started_status in {"pending_index", "failed"},
        )
        if isinstance(exc, ContributionIndexingExecutionError):
            raise
        raise ContributionIndexingExecutionError(SAFE_FAILURE_MESSAGE) from exc


def retire_contribution_promotion(
    db: Session,
    *,
    contribution: MemorialContribution,
    writer: MemorialContributionQdrantWriter | None = None,
) -> None:
    """Deactivate the promotion (if any) for a contribution that has just
    become archived or superseded. Idempotent and safe to call even when no
    promotion exists yet (e.g. a contribution that was archived before ever
    being approved). Removes the Qdrant point so it can no longer surface as
    active evidence, while keeping the SQL lineage row for audit."""

    promotion = repository.get_promotion_by_contribution_id(
        db,
        contribution_id=contribution.id,
        for_update=True,
    )
    if promotion is None or promotion.promotion_status == "retired":
        return

    actual_writer = writer or DefaultMemorialContributionQdrantWriter()
    if promotion.target_collection_name and promotion.qdrant_point_id:
        try:
            actual_writer.delete_point(
                collection_name=promotion.target_collection_name,
                point_id=promotion.qdrant_point_id,
            )
        except Exception as exc:
            log_event(
                logger,
                logging.ERROR,
                "memorial_contribution_retire_delete_failed",
                promotion_id=promotion.id,
                contribution_id=promotion.contribution_id,
                profile_id=promotion.profile_id,
                error_type=exc.__class__.__name__,
            )
            raise ContributionIndexingExecutionError(
                "Retiring the indexed contribution failed"
            ) from exc

    promotion.promotion_status = "retired"
    promotion.retired_at = datetime.now(timezone.utc)
    db.commit()
    log_event(
        logger,
        logging.INFO,
        "memorial_contribution_retired",
        promotion_id=promotion.id,
        contribution_id=promotion.contribution_id,
        profile_id=promotion.profile_id,
    )


_PROMOTION_STATUS_TO_INDEXING_STATE = {
    "pending_index": "pending",
    "indexed": "indexed",
    "failed": "failed",
    "retired": "retired",
}


def get_indexing_status_for_contribution(
    contribution: MemorialContribution,
    promotion: MemorialContributionPromotion | None,
) -> tuple[str, MemorialContributionPromotion | None]:
    """Pure projection used by the API schema layer - never infer
    "searchable" purely from `contribution.status`. Returned state is one of
    `not_applicable | pending | indexed | failed | retired`."""

    if promotion is None:
        if contribution.status == "approved" and contribution.is_current:
            return "pending", None
        return "not_applicable", None
    return _PROMOTION_STATUS_TO_INDEXING_STATE[promotion.promotion_status], promotion


def get_active_indexing_job_id_for_promotion(db: Session, *, promotion_id: int) -> int | None:
    """Task 65.9.1 (Part F/I) - resolves the currently-active (non-terminal)
    background job id for a contribution's indexing promotion, if any, so
    the frontend can poll `GET /api/jobs/{job_id}` immediately after
    approval/retry rather than only after a full page reload. Uses the
    exact same deterministic idempotency key `enqueue_indexing_job` creates
    the job with (`INDEXING_JOB_WORKFLOW:{promotion_id}:index`) - never
    guesses/searches by other criteria, so this can never surface a
    different promotion's or a different profile's job."""

    from app.modules.job_tracking import repository as job_tracking_repository

    idempotency_key = f"{INDEXING_JOB_WORKFLOW}:{promotion_id}:index"
    job = job_tracking_repository.get_active_background_job_by_idempotency_key(db, idempotency_key=idempotency_key)
    return job.id if job is not None else None

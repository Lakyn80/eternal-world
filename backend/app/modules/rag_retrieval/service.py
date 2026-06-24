from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import User
from app.modules.active_retrieval_config.service import resolve_active_retrieval_config
from app.modules.embedding_models.exceptions import EmbeddingModelNotFoundError
from app.modules.embedding_models.service import get_default_embedding_model, get_embedding_model
from app.modules.embeddings.providers.mock import MockEmbeddingProvider
from app.modules.memory_profiles.service import MemoryProfileNotFoundError, get_memory_profile
from app.modules.qdrant_indexing.client import build_qdrant_client
from app.modules.qdrant_indexing.exceptions import QdrantClientError, QdrantCollectionConfigurationError
from app.modules.rag_retrieval import repository
from app.modules.rag_retrieval.exceptions import (
    RagRetrievalDisabledError,
    RagRetrievalModelUnavailableError,
    RagRetrievalProfileNotFoundError,
)
from app.modules.rag_retrieval.ranking import rank_retrieval_results
from app.modules.rag_retrieval.schemas import (
    RagRetrievalRequest,
    RagRetrievalResponseRead,
    RagRetrievalResultRead,
)


def _ensure_retrieval_enabled() -> None:
    if not settings.qdrant_indexing_enabled:
        raise RagRetrievalDisabledError("Qdrant retrieval is disabled")


def _resolve_model(model_code: str | None):
    try:
        model = get_default_embedding_model() if model_code is None else get_embedding_model(model_code)
    except EmbeddingModelNotFoundError as exc:
        raise RagRetrievalModelUnavailableError("Embedding model not found") from exc

    if not model.enabled:
        raise RagRetrievalModelUnavailableError("Embedding model not available")

    return model


def _build_provider():
    return MockEmbeddingProvider()


def build_retrieval_collection_name(
    model_code: str,
    *,
    collection_name: str | None = None,
) -> str:
    if collection_name is not None:
        return collection_name

    return f"{settings.qdrant_collection_name}__{model_code}"


def _build_search_filter(
    *,
    owner_user_id: int,
    profile_id: int,
    language: str | None,
    source_type: str | None,
) -> dict[str, object]:
    must_filters: list[dict[str, object]] = [
        {
            "key": "owner_user_id",
            "match": {"value": owner_user_id},
        },
        {
            "key": "profile_id",
            "match": {"value": profile_id},
        },
    ]
    if language is not None:
        must_filters.append(
            {
                "key": "language",
                "match": {"value": language},
            }
        )
    if source_type is not None:
        must_filters.append(
            {
                "key": "source_type",
                "match": {"value": source_type},
            }
        )

    return {"must": must_filters}


def _get_owned_profile_or_raise(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
):
    try:
        return get_memory_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except MemoryProfileNotFoundError as exc:
        raise RagRetrievalProfileNotFoundError("Memory profile not found") from exc


def retrieve_profile_rag(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: RagRetrievalRequest,
) -> RagRetrievalResponseRead:
    collection_name = None
    effective_limit = payload.limit
    effective_score_threshold = payload.score_threshold
    effective_model_code = payload.model_code
    payload_fields_set = set(payload.model_fields_set)
    active_config = resolve_active_retrieval_config(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    if active_config is not None:
        explicit_model_override = "model_code" in payload_fields_set and payload.model_code is not None
        if not explicit_model_override:
            effective_model_code = active_config.model_code
            collection_name = active_config.collection_name
        if "limit" not in payload_fields_set:
            effective_limit = active_config.top_k
        if "score_threshold" not in payload_fields_set:
            effective_score_threshold = active_config.score_threshold

    effective_payload = payload.model_copy(
        update={
            "model_code": effective_model_code,
            "limit": effective_limit,
            "score_threshold": effective_score_threshold,
        }
    )
    return retrieve_profile_rag_for_collection(
        db,
        current_user=current_user,
        profile_id=profile_id,
        payload=effective_payload,
        collection_name=collection_name,
    )


def retrieve_profile_rag_for_collection(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: RagRetrievalRequest,
    collection_name: str | None = None,
) -> RagRetrievalResponseRead:
    _ensure_retrieval_enabled()
    _get_owned_profile_or_raise(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    model = _resolve_model(payload.model_code)
    provider = _build_provider()
    query_embedding = provider.embed_text(payload.query, model.code)

    if query_embedding.dimension != model.dimension or len(query_embedding.values) != model.dimension:
        raise QdrantCollectionConfigurationError("Query embedding dimension is invalid")

    qdrant_collection = build_retrieval_collection_name(
        model.code,
        collection_name=collection_name,
    )
    qdrant_client = build_qdrant_client()
    raw_results = qdrant_client.search_points(
        collection_name=qdrant_collection,
        vector=query_embedding.values,
        limit=payload.limit,
        search_filter=_build_search_filter(
            owner_user_id=current_user.id,
            profile_id=profile_id,
            language=payload.language,
            source_type=payload.source_type,
        ),
        score_threshold=payload.score_threshold,
    )

    if not raw_results:
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code=model.code,
            results=[],
        )

    result_rows: list[dict[str, object]] = []
    embedding_ids: list[int] = []
    for item in raw_results:
        payload_metadata = item.get("payload")
        if not isinstance(payload_metadata, dict):
            continue

        embedding_id = payload_metadata.get("embedding_id")
        chunk_id = payload_metadata.get("chunk_id")
        if not isinstance(embedding_id, int) or not isinstance(chunk_id, int):
            continue

        embedding_ids.append(embedding_id)
        result_rows.append(
            {
                "embedding_id": embedding_id,
                "chunk_id": chunk_id,
                "score": item.get("score", 0.0),
                "payload_metadata": payload_metadata,
            }
        )

    if not embedding_ids:
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code=model.code,
            results=[],
        )

    evidence_records = repository.list_retrieval_evidence_for_embeddings(
        db,
        owner_user_id=current_user.id,
        profile_id=profile_id,
        embedding_ids=embedding_ids,
    )
    evidence_by_embedding_id = {
        record.embedding_id: record for record in evidence_records
    }

    hydrated_results: list[dict[str, object]] = []
    for item in result_rows:
        embedding_id = int(item["embedding_id"])
        evidence_record = evidence_by_embedding_id.get(embedding_id)
        if evidence_record is None:
            continue
        if payload.language is not None and evidence_record.language != payload.language:
            continue
        if payload.source_type is not None and evidence_record.source_type != payload.source_type:
            continue

        hydrated_results.append(
            {
                "chunk_id": evidence_record.chunk_id,
                "source_id": evidence_record.source_id,
                "embedding_id": evidence_record.embedding_id,
                "score": item["score"],
                "text": evidence_record.chunk_text,
                "chunk_index": evidence_record.chunk_index,
                "language": evidence_record.language,
                "source_type": evidence_record.source_type,
                "validation_status": evidence_record.validation_status,
                "text_hash": evidence_record.text_hash,
                "qdrant_collection": qdrant_collection,
                "payload_metadata": item["payload_metadata"],
            }
        )

    ranked_results = rank_retrieval_results(
        hydrated_results,
        limit=payload.limit,
        score_threshold=payload.score_threshold,
    )
    return RagRetrievalResponseRead(
        profile_id=profile_id,
        query=payload.query,
        model_code=model.code,
        results=[RagRetrievalResultRead(**result) for result in ranked_results],
    )

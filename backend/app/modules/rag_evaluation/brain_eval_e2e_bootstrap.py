from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

from sqlalchemy.orm import Session

from app.modules.active_retrieval_config.schemas import ActiveRetrievalConfigUpsertRequest
from app.modules.active_retrieval_config.service import (
    get_production_recommended_active_retrieval_config,
    upsert_active_retrieval_config,
)
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import DuplicateEmailError, register_user
from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.service import embed_source_chunks
from app.modules.memories.repository import create_memory as create_memory_record
from app.modules.memories.repository import list_memories_for_profile
from app.modules.memory_profiles.repository import list_memory_profiles_for_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.embeddings.runtime import (
    build_embedding_runtime_fingerprint,
    resolve_embedding_runtime_diagnostics,
)
from app.modules.qdrant_indexing.client import build_qdrant_client
from app.modules.qdrant_indexing.repository import list_source_embeddings_for_user
from app.modules.qdrant_indexing.service import index_source_embeddings
from app.modules.rag_chunks.service import chunk_rag_source, list_rag_chunks
from app.modules.rag_evaluation.fixtures.family_novak_facts import FamilyNovakFact
from app.modules.rag_evaluation.fixtures.family_novak_facts_ru import FAMILY_NOVAK_FACTS_RU
from app.modules.rag_evaluation.fixtures.family_novak_ru import (
    EVA_NOVAK_PROFILE_RU,
    build_corpus_text_ru,
)
from app.modules.rag_sources.repository import list_rag_sources_for_profile
from app.modules.rag_sources.schemas import RagSourceCreate, RagSourceUpdate
from app.modules.rag_sources.service import create_rag_source, update_rag_source
from app.modules.users.repository import get_user_by_email


FAMILY_AVATAR_RU_E2E_EMAIL = "family.avatar.ru.e2e@example.test"
FAMILY_AVATAR_RU_E2E_PASSWORD = "FamilyAvatarRuE2e123"
FAMILY_AVATAR_RU_E2E_PROFILE_NAME = "Ева Новакова (RU E2E Eval)"
FAMILY_AVATAR_RU_E2E_SOURCE_TITLE = "Family Novak RU E2E Corpus"
FAMILY_AVATAR_RU_E2E_SOURCE_KEY = "family_novak_ru_e2e_v3_bge_m3_real_cpu"
FAMILY_AVATAR_RU_E2E_COLLECTION_SUFFIX = "family_novak_ru_e2e_v3_bge_m3_real_cpu"
FAMILY_AVATAR_RU_E2E_CORPUS_LANGUAGE = "ru"

_MEMORY_FACT_ID_PATTERN = re.compile(r"^\[(f\d{3})\]\s+")


@dataclass(frozen=True)
class FamilyAvatarRuE2EBootstrapResult:
    user_id: int
    profile_id: int
    source_id: int
    model_code: str
    collection_name: str
    retrieval_mode: str
    top_k: int
    corpus_text_hash: str
    embedding_runtime_fingerprint: str
    collection_rebuilt: bool = False
    memory_ids_by_fact_id: dict[str, int] = field(default_factory=dict)
    chunk_ids_by_fact_id: dict[str, int] = field(default_factory=dict)


def _corpus_text_hash(corpus_text: str) -> str:
    return hashlib.sha256(corpus_text.encode("utf-8")).hexdigest()


def _memory_title_for_fact(fact: FamilyNovakFact) -> str:
    title = fact.memory_title or fact.fact_id
    return f"[{fact.fact_id}] {title}"


def _parse_memory_fact_id(title: str) -> str | None:
    match = _MEMORY_FACT_ID_PATTERN.match(title.strip())
    if match is None:
        return None
    return match.group(1)


def _normalize_match_text(value: str) -> str:
    return " ".join(value.split()).lower()


def _find_chunk_id_for_fact_text(*, chunks, fact_text: str) -> int | None:
    normalized_fact = _normalize_match_text(fact_text)
    if not normalized_fact:
        return None

    for chunk in chunks:
        normalized_chunk = _normalize_match_text(chunk.chunk_text)
        if normalized_fact in normalized_chunk or normalized_chunk in normalized_fact:
            return chunk.id

    return None


def _delete_qdrant_collection_if_exists(*, collection_name: str) -> bool:
    qdrant_client = build_qdrant_client()
    return qdrant_client.delete_collection(collection_name=collection_name)


def build_family_avatar_ru_e2e_collection_name(*, base_collection_name: str) -> str:
    return f"{base_collection_name}__{FAMILY_AVATAR_RU_E2E_COLLECTION_SUFFIX}"


def _build_qdrant_source_filter(
    *,
    owner_user_id: int,
    profile_id: int,
    source_id: int,
) -> dict[str, object]:
    return {
        "must": [
            {"key": "owner_user_id", "match": {"value": owner_user_id}},
            {"key": "profile_id", "match": {"value": profile_id}},
            {"key": "source_id", "match": {"value": source_id}},
        ]
    }


def _count_qdrant_points_for_source(
    *,
    collection_name: str,
    owner_user_id: int,
    profile_id: int,
    source_id: int,
) -> int:
    qdrant_client = build_qdrant_client()
    return qdrant_client.count_points(
        collection_name=collection_name,
        search_filter=_build_qdrant_source_filter(
            owner_user_id=owner_user_id,
            profile_id=profile_id,
            source_id=source_id,
        ),
    )


def _build_e2e_source_metadata(
    *,
    corpus_hash: str,
    collection_name: str,
    model_code: str,
    retrieval_mode: str,
    embedding_runtime_fingerprint: str,
) -> dict[str, object]:
    model = get_embedding_model(model_code)
    runtime_diagnostics = resolve_embedding_runtime_diagnostics(
        model_code=model_code,
        collection_name=collection_name,
    )
    snapshot_revision = None
    if runtime_diagnostics.bge_m3_snapshot_path:
        snapshot_revision = runtime_diagnostics.bge_m3_snapshot_path.rstrip("/").split("/")[-1]

    return {
        "family_avatar_ru_e2e_key": FAMILY_AVATAR_RU_E2E_SOURCE_KEY,
        "corpus_text_hash": corpus_hash,
        "corpus_language": FAMILY_AVATAR_RU_E2E_CORPUS_LANGUAGE,
        "embedding_runtime_fingerprint": embedding_runtime_fingerprint,
        "embedding_provider_setting": runtime_diagnostics.embedding_provider_setting,
        "resolved_indexing_provider_name": runtime_diagnostics.resolved_indexing_provider_name,
        "resolved_query_provider_name": runtime_diagnostics.resolved_query_provider_name,
        "model_code": model.code,
        "provider_model_name": model.provider_model_name,
        "retrieval_mode": retrieval_mode,
        "collection_name": collection_name,
        "bge_m3_snapshot_path": runtime_diagnostics.bge_m3_snapshot_path,
        "bge_m3_snapshot_revision": snapshot_revision,
        "safe_fictional_data": True,
    }


def _source_needs_embedding_pipeline(
    *,
    stored_hash: str | None,
    corpus_hash: str,
    stored_fingerprint: str | None,
    embedding_runtime_fingerprint: str,
    chunk_count: int,
    embedding_count: int,
    qdrant_point_count: int,
) -> bool:
    if stored_hash != corpus_hash:
        return True
    if stored_fingerprint != embedding_runtime_fingerprint:
        return True
    if chunk_count == 0:
        return True
    if embedding_count != chunk_count:
        return True
    if qdrant_point_count != chunk_count:
        return True
    return False


def ensure_family_avatar_ru_e2e_bootstrap(db: Session) -> FamilyAvatarRuE2EBootstrapResult:
    recommendation = get_production_recommended_active_retrieval_config()
    e2e_collection_name = build_family_avatar_ru_e2e_collection_name(
        base_collection_name=recommendation.collection_name,
    )
    corpus_text = build_corpus_text_ru()
    corpus_hash = _corpus_text_hash(corpus_text)
    embedding_runtime_fingerprint = build_embedding_runtime_fingerprint(
        model_code=recommendation.model_code,
    )

    user = get_user_by_email(db, FAMILY_AVATAR_RU_E2E_EMAIL)
    if user is None:
        try:
            user = register_user(
                db,
                RegisterRequest(
                    email=FAMILY_AVATAR_RU_E2E_EMAIL,
                    password=FAMILY_AVATAR_RU_E2E_PASSWORD,
                    full_name="Family Avatar RU E2E Eval User",
                ),
            )
        except DuplicateEmailError:
            user = get_user_by_email(db, FAMILY_AVATAR_RU_E2E_EMAIL)
    if user is None:
        raise RuntimeError("Family Avatar RU E2E user could not be created or reused")

    profiles = list_memory_profiles_for_user(db, user.id)
    profile = next(
        (item for item in profiles if item.name == FAMILY_AVATAR_RU_E2E_PROFILE_NAME),
        None,
    )
    if profile is None:
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name=FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
                birth_date=EVA_NOVAK_PROFILE_RU.birth_date,
                death_date=EVA_NOVAK_PROFILE_RU.death_date,
                biography=EVA_NOVAK_PROFILE_RU.biography,
                personality=EVA_NOVAK_PROFILE_RU.personality,
                catchphrases=EVA_NOVAK_PROFILE_RU.catchphrases,
            ),
        )

    upsert_active_retrieval_config(
        db,
        current_user=user,
        profile_id=profile.id,
        payload=ActiveRetrievalConfigUpsertRequest(
            model_code=recommendation.model_code,
            collection_name=e2e_collection_name,
            top_k=recommendation.top_k,
            score_threshold=recommendation.score_threshold,
            retrieval_mode=recommendation.retrieval_mode,
            selection_reason=recommendation.selection_reason,
        ),
    )

    existing_memories = list_memories_for_profile(
        db,
        user_id=user.id,
        profile_id=profile.id,
    )
    memory_ids_by_fact_id: dict[str, int] = {}
    for memory in existing_memories:
        fact_id = _parse_memory_fact_id(memory.title)
        if fact_id is not None:
            memory_ids_by_fact_id[fact_id] = memory.id

    for fact in FAMILY_NOVAK_FACTS_RU:
        if fact.source_type != "memory":
            continue
        if fact.fact_id in memory_ids_by_fact_id:
            continue
        created_memory = create_memory_record(
            db,
            user_id=user.id,
            profile_id=profile.id,
            title=_memory_title_for_fact(fact),
            content=fact.text,
            memory_type="text",
            occurred_at=None,
            occurred_year=fact.occurred_year,
            media_id=None,
        )
        db.flush()
        memory_ids_by_fact_id[fact.fact_id] = created_memory.id

    sources = list_rag_sources_for_profile(
        db,
        owner_user_id=user.id,
        profile_id=profile.id,
    )
    metadata = _build_e2e_source_metadata(
        corpus_hash=corpus_hash,
        collection_name=e2e_collection_name,
        model_code=recommendation.model_code,
        retrieval_mode=recommendation.retrieval_mode,
        embedding_runtime_fingerprint=embedding_runtime_fingerprint,
    )
    source = next(
        (
            item
            for item in sources
            if item.title == FAMILY_AVATAR_RU_E2E_SOURCE_TITLE
            and isinstance(item.source_metadata, dict)
            and item.source_metadata.get("family_avatar_ru_e2e_key") == FAMILY_AVATAR_RU_E2E_SOURCE_KEY
        ),
        None,
    )
    if source is None:
        source = create_rag_source(
            db,
            current_user=user,
            profile_id=profile.id,
            payload=RagSourceCreate(
                title=FAMILY_AVATAR_RU_E2E_SOURCE_TITLE,
                raw_text=corpus_text,
                source_type="manual_text",
                language="ru",
                source_metadata=metadata,
            ),
        )
    elif source.raw_text != corpus_text or source.source_metadata != metadata:
        source = update_rag_source(
            db,
            current_user=user,
            source_id=source.id,
            payload=RagSourceUpdate(
                title=FAMILY_AVATAR_RU_E2E_SOURCE_TITLE,
                raw_text=corpus_text,
                source_type="manual_text",
                language="ru",
                source_metadata=metadata,
            ),
        )

    stored_hash = None
    stored_fingerprint = None
    if isinstance(source.source_metadata, dict):
        stored_hash = source.source_metadata.get("corpus_text_hash")
        stored_fingerprint = source.source_metadata.get("embedding_runtime_fingerprint")
    existing_chunks = list_rag_chunks(db, current_user=user, source_id=source.id)
    existing_embeddings = list_source_embeddings_for_user(
        db,
        owner_user_id=user.id,
        source_id=source.id,
        model_code=recommendation.model_code,
    )
    qdrant_point_count = _count_qdrant_points_for_source(
        collection_name=e2e_collection_name,
        owner_user_id=user.id,
        profile_id=profile.id,
        source_id=source.id,
    )
    collection_rebuilt = False
    needs_pipeline = _source_needs_embedding_pipeline(
        stored_hash=stored_hash,
        corpus_hash=corpus_hash,
        stored_fingerprint=stored_fingerprint,
        embedding_runtime_fingerprint=embedding_runtime_fingerprint,
        chunk_count=len(existing_chunks),
        embedding_count=len(existing_embeddings),
        qdrant_point_count=qdrant_point_count,
    )

    if needs_pipeline:
        _delete_qdrant_collection_if_exists(collection_name=e2e_collection_name)
        chunk_rag_source(db, current_user=user, source_id=source.id)
        embed_source_chunks(
            db,
            current_user=user,
            source_id=source.id,
            model_code=recommendation.model_code,
        )
        index_source_embeddings(
            db,
            current_user=user,
            source_id=source.id,
            model_code=recommendation.model_code,
            collection_name=e2e_collection_name,
        )
        db.refresh(source)
        collection_rebuilt = True

    chunks = list_rag_chunks(db, current_user=user, source_id=source.id)
    chunk_ids_by_fact_id: dict[str, int] = {}
    for fact in FAMILY_NOVAK_FACTS_RU:
        chunk_id = _find_chunk_id_for_fact_text(chunks=chunks, fact_text=fact.text)
        if chunk_id is not None:
            chunk_ids_by_fact_id[fact.fact_id] = chunk_id

    db.commit()

    return FamilyAvatarRuE2EBootstrapResult(
        user_id=user.id,
        profile_id=profile.id,
        source_id=source.id,
        model_code=recommendation.model_code,
        collection_name=e2e_collection_name,
        retrieval_mode=recommendation.retrieval_mode,
        top_k=recommendation.top_k,
        corpus_text_hash=corpus_hash,
        embedding_runtime_fingerprint=embedding_runtime_fingerprint,
        collection_rebuilt=collection_rebuilt,
        memory_ids_by_fact_id=memory_ids_by_fact_id,
        chunk_ids_by_fact_id=chunk_ids_by_fact_id,
    )

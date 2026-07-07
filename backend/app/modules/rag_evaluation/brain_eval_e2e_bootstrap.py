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
from app.modules.embeddings.service import embed_source_chunks
from app.modules.memories.repository import create_memory as create_memory_record
from app.modules.memories.repository import list_memories_for_profile
from app.modules.memory_profiles.repository import list_memory_profiles_for_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.embeddings.runtime import build_embedding_runtime_fingerprint
from app.modules.qdrant_indexing.client import build_qdrant_client
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
FAMILY_AVATAR_RU_E2E_SOURCE_KEY = "family_novak_ru_e2e_v2_real_embeddings"

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


def ensure_family_avatar_ru_e2e_bootstrap(db: Session) -> FamilyAvatarRuE2EBootstrapResult:
    recommendation = get_production_recommended_active_retrieval_config()
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
            collection_name=recommendation.collection_name,
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
    metadata = {
        "family_avatar_ru_e2e_key": FAMILY_AVATAR_RU_E2E_SOURCE_KEY,
        "corpus_text_hash": corpus_hash,
        "embedding_runtime_fingerprint": embedding_runtime_fingerprint,
        "safe_fictional_data": True,
    }
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
    collection_rebuilt = False
    needs_pipeline = (
        stored_hash != corpus_hash
        or stored_fingerprint != embedding_runtime_fingerprint
        or not existing_chunks
        or source.status not in {"chunked", "embedded", "indexed"}
    )

    if needs_pipeline and stored_fingerprint != embedding_runtime_fingerprint:
        collection_rebuilt = _delete_qdrant_collection_if_exists(
            collection_name=recommendation.collection_name,
        )

    if needs_pipeline:
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
        )
        db.refresh(source)

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
        collection_name=recommendation.collection_name,
        retrieval_mode=recommendation.retrieval_mode,
        top_k=recommendation.top_k,
        corpus_text_hash=corpus_hash,
        embedding_runtime_fingerprint=embedding_runtime_fingerprint,
        collection_rebuilt=collection_rebuilt,
        memory_ids_by_fact_id=memory_ids_by_fact_id,
        chunk_ids_by_fact_id=chunk_ids_by_fact_id,
    )

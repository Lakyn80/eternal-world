from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import and_, or_, select
from sqlalchemy.orm import Session

from app.db.models import AvatarMemoryPromotion, MemoryProfile, RagChunk, RagEmbedding, RagSource


@dataclass(frozen=True)
class RetrievalEvidenceRecord:
    chunk_id: int
    source_id: int
    source_title: str
    embedding_id: int
    owner_user_id: int
    profile_id: int
    chunk_text: str
    chunk_index: int
    language: str | None
    source_type: str
    validation_status: str
    text_hash: str
    model_code: str


def list_retrieval_evidence_for_embeddings(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
    embedding_ids: list[int],
) -> list[RetrievalEvidenceRecord]:
    if not embedding_ids:
        return []

    statement = (
        select(RagEmbedding, RagChunk, RagSource)
        .join(RagChunk, RagEmbedding.chunk_id == RagChunk.id)
        .join(RagSource, RagEmbedding.source_id == RagSource.id)
        .join(MemoryProfile, RagEmbedding.profile_id == MemoryProfile.id)
        .outerjoin(
            AvatarMemoryPromotion,
            AvatarMemoryPromotion.rag_embedding_id == RagEmbedding.id,
        )
        .where(
            RagEmbedding.id.in_(embedding_ids),
            RagEmbedding.owner_user_id == owner_user_id,
            RagEmbedding.profile_id == profile_id,
            RagChunk.owner_user_id == owner_user_id,
            RagChunk.profile_id == profile_id,
            RagSource.owner_user_id == owner_user_id,
            RagSource.profile_id == profile_id,
            MemoryProfile.user_id == owner_user_id,
            MemoryProfile.id == profile_id,
            or_(
                RagSource.source_type != "conversation_candidate",
                and_(
                    AvatarMemoryPromotion.promotion_status == "indexed",
                    AvatarMemoryPromotion.owner_user_id == owner_user_id,
                    AvatarMemoryPromotion.profile_id == profile_id,
                ),
            ),
        )
    )

    rows = db.execute(statement).all()
    return [
        RetrievalEvidenceRecord(
            chunk_id=rag_chunk.id,
            source_id=rag_source.id,
            source_title=rag_source.title,
            embedding_id=rag_embedding.id,
            owner_user_id=rag_embedding.owner_user_id,
            profile_id=rag_embedding.profile_id,
            chunk_text=rag_chunk.chunk_text,
            chunk_index=rag_chunk.chunk_index,
            language=rag_chunk.language,
            source_type=rag_source.source_type,
            validation_status=rag_chunk.validation_status,
            text_hash=rag_chunk.text_hash,
            model_code=rag_embedding.model_code,
        )
        for rag_embedding, rag_chunk, rag_source in rows
    ]

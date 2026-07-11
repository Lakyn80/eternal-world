from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import AvatarMemoryPromotion, RagChunk, RagEmbedding, RagSource


def list_promotions_for_indexing(
    db: Session,
    *,
    promotion_id: int | None = None,
    avatar_id: str | None = None,
    profile_id: int | None = None,
    limit: int = 100,
) -> list[AvatarMemoryPromotion]:
    statement = select(AvatarMemoryPromotion).where(
        AvatarMemoryPromotion.promotion_status == "pending_index"
    )
    if promotion_id is not None:
        statement = statement.where(AvatarMemoryPromotion.id == promotion_id)
    if avatar_id is not None:
        statement = statement.where(AvatarMemoryPromotion.avatar_id == avatar_id)
    if profile_id is not None:
        statement = statement.where(AvatarMemoryPromotion.profile_id == profile_id)
    statement = statement.order_by(
        AvatarMemoryPromotion.created_at.asc(),
        AvatarMemoryPromotion.id.asc(),
    ).limit(limit)
    return list(db.scalars(statement))


def list_selected_promotions(
    db: Session,
    *,
    promotion_id: int | None = None,
    avatar_id: str | None = None,
    profile_id: int | None = None,
    limit: int = 100,
) -> list[AvatarMemoryPromotion]:
    statement = select(AvatarMemoryPromotion)
    if promotion_id is not None:
        statement = statement.where(AvatarMemoryPromotion.id == promotion_id)
    if avatar_id is not None:
        statement = statement.where(AvatarMemoryPromotion.avatar_id == avatar_id)
    if profile_id is not None:
        statement = statement.where(AvatarMemoryPromotion.profile_id == profile_id)
    statement = statement.order_by(
        AvatarMemoryPromotion.created_at.asc(),
        AvatarMemoryPromotion.id.asc(),
    ).limit(limit)
    return list(db.scalars(statement))


def get_promotion_for_owner(
    db: Session,
    *,
    owner_user_id: int,
    promotion_id: int,
    for_update: bool = False,
) -> AvatarMemoryPromotion | None:
    statement = select(AvatarMemoryPromotion).where(
        AvatarMemoryPromotion.id == promotion_id,
        AvatarMemoryPromotion.owner_user_id == owner_user_id,
    )
    if for_update:
        statement = statement.with_for_update()
    return db.scalar(statement)


def get_evidence_records(
    db: Session,
    *,
    promotion: AvatarMemoryPromotion,
) -> tuple[RagSource, RagChunk, RagEmbedding] | None:
    if not promotion.rag_source_id or not promotion.rag_chunk_id or not promotion.rag_embedding_id:
        return None
    source = db.get(RagSource, promotion.rag_source_id)
    chunk = db.get(RagChunk, promotion.rag_chunk_id)
    embedding = db.get(RagEmbedding, promotion.rag_embedding_id)
    if source is None or chunk is None or embedding is None:
        return None
    return source, chunk, embedding

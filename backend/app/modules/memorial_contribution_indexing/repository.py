from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import MemorialContributionPromotion, RagChunk, RagEmbedding, RagSource


def create_promotion(
    db: Session,
    *,
    contribution_id: int,
    profile_id: int,
    promotion_status: str,
    approved_memory_text: str,
    normalized_memory_text: str,
    language: str | None,
    source_contribution_status_snapshot: str,
) -> MemorialContributionPromotion:
    promotion = MemorialContributionPromotion(
        contribution_id=contribution_id,
        profile_id=profile_id,
        promotion_status=promotion_status,
        approved_memory_text=approved_memory_text,
        normalized_memory_text=normalized_memory_text,
        language=language,
        source_contribution_status_snapshot=source_contribution_status_snapshot,
    )
    db.add(promotion)
    return promotion


def get_promotion_by_contribution_id(
    db: Session,
    *,
    contribution_id: int,
    for_update: bool = False,
) -> MemorialContributionPromotion | None:
    statement = select(MemorialContributionPromotion).where(
        MemorialContributionPromotion.contribution_id == contribution_id,
    )
    if for_update:
        statement = statement.with_for_update()
    return db.scalar(statement)


def get_promotion_for_profile(
    db: Session,
    *,
    profile_id: int,
    promotion_id: int,
    for_update: bool = False,
) -> MemorialContributionPromotion | None:
    statement = select(MemorialContributionPromotion).where(
        MemorialContributionPromotion.id == promotion_id,
        MemorialContributionPromotion.profile_id == profile_id,
    )
    if for_update:
        statement = statement.with_for_update()
    return db.scalar(statement)


def list_promotions_for_contributions(
    db: Session,
    *,
    contribution_ids: list[int],
) -> dict[int, MemorialContributionPromotion]:
    if not contribution_ids:
        return {}
    statement = select(MemorialContributionPromotion).where(
        MemorialContributionPromotion.contribution_id.in_(contribution_ids),
    )
    return {row.contribution_id: row for row in db.scalars(statement)}


def get_evidence_records(
    db: Session,
    *,
    promotion: MemorialContributionPromotion,
) -> tuple[RagSource, RagChunk, RagEmbedding] | None:
    if not promotion.rag_source_id or not promotion.rag_chunk_id or not promotion.rag_embedding_id:
        return None
    source = db.get(RagSource, promotion.rag_source_id)
    chunk = db.get(RagChunk, promotion.rag_chunk_id)
    embedding = db.get(RagEmbedding, promotion.rag_embedding_id)
    if source is None or chunk is None or embedding is None:
        return None
    return source, chunk, embedding

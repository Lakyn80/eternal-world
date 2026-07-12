from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.models import (
    ConversationMemoryCandidate,
    FamilyMemoryContribution,
    MemoryClarificationQuestion,
)


def get_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    for_update: bool = False,
) -> ConversationMemoryCandidate | None:
    statement = select(ConversationMemoryCandidate).where(
        ConversationMemoryCandidate.id == candidate_id,
        ConversationMemoryCandidate.owner_user_id == owner_user_id,
    )
    if for_update:
        statement = statement.with_for_update()
    return db.scalar(statement)


def create_contribution(db: Session, **values) -> FamilyMemoryContribution:
    contribution = FamilyMemoryContribution(**values)
    db.add(contribution)
    return contribution


def list_contributions(
    db: Session,
    *,
    candidate_id: int,
) -> list[FamilyMemoryContribution]:
    statement = (
        select(FamilyMemoryContribution)
        .where(FamilyMemoryContribution.candidate_id == candidate_id)
        .order_by(FamilyMemoryContribution.created_at.asc(), FamilyMemoryContribution.id.asc())
    )
    return list(db.scalars(statement))


def count_contributions(db: Session, *, candidate_id: int) -> int:
    statement = select(func.count(FamilyMemoryContribution.id)).where(
        FamilyMemoryContribution.candidate_id == candidate_id
    )
    return int(db.scalar(statement) or 0)


def get_contribution(
    db: Session,
    *,
    candidate_id: int,
    contribution_id: int,
) -> FamilyMemoryContribution | None:
    statement = select(FamilyMemoryContribution).where(
        FamilyMemoryContribution.id == contribution_id,
        FamilyMemoryContribution.candidate_id == candidate_id,
    )
    return db.scalar(statement)


def create_clarification(db: Session, **values) -> MemoryClarificationQuestion:
    clarification = MemoryClarificationQuestion(**values)
    db.add(clarification)
    return clarification


def get_clarification(
    db: Session,
    *,
    candidate_id: int,
    clarification_id: int,
    for_update: bool = False,
) -> MemoryClarificationQuestion | None:
    statement = select(MemoryClarificationQuestion).where(
        MemoryClarificationQuestion.id == clarification_id,
        MemoryClarificationQuestion.candidate_id == candidate_id,
    )
    if for_update:
        statement = statement.with_for_update()
    return db.scalar(statement)


def get_clarification_by_key(
    db: Session,
    *,
    candidate_id: int,
    question_key: str,
) -> MemoryClarificationQuestion | None:
    statement = select(MemoryClarificationQuestion).where(
        MemoryClarificationQuestion.candidate_id == candidate_id,
        MemoryClarificationQuestion.question_key == question_key,
    )
    return db.scalar(statement)


def list_clarifications(
    db: Session,
    *,
    candidate_id: int,
) -> list[MemoryClarificationQuestion]:
    statement = (
        select(MemoryClarificationQuestion)
        .where(MemoryClarificationQuestion.candidate_id == candidate_id)
        .order_by(MemoryClarificationQuestion.created_at.asc(), MemoryClarificationQuestion.id.asc())
    )
    return list(db.scalars(statement))


def list_pending_required_clarifications(
    db: Session,
    *,
    candidate_id: int,
) -> list[MemoryClarificationQuestion]:
    statement = select(MemoryClarificationQuestion).where(
        MemoryClarificationQuestion.candidate_id == candidate_id,
        MemoryClarificationQuestion.status == "pending",
        MemoryClarificationQuestion.required.is_(True),
    )
    return list(db.scalars(statement))


def get_next_pending_clarification(
    db: Session,
    *,
    candidate_id: int,
    for_update: bool = False,
) -> MemoryClarificationQuestion | None:
    statement = (
        select(MemoryClarificationQuestion)
        .where(
            MemoryClarificationQuestion.candidate_id == candidate_id,
            MemoryClarificationQuestion.status == "pending",
        )
        .order_by(
            MemoryClarificationQuestion.created_at.asc(),
            MemoryClarificationQuestion.id.asc(),
        )
        .limit(1)
    )
    if for_update:
        statement = statement.with_for_update()
    return db.scalar(statement)

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import BiographerQuestion


def list_questions_for_profile(db: Session, *, profile_id: int) -> list[BiographerQuestion]:
    statement = (
        select(BiographerQuestion)
        .where(BiographerQuestion.profile_id == profile_id)
        .order_by(BiographerQuestion.id.asc())
    )
    return list(db.scalars(statement))


def get_pending_question(db: Session, *, profile_id: int) -> BiographerQuestion | None:
    statement = select(BiographerQuestion).where(
        BiographerQuestion.profile_id == profile_id,
        BiographerQuestion.status == "pending",
    )
    return db.scalar(statement)


def get_question_for_profile(db: Session, *, profile_id: int, question_id: int) -> BiographerQuestion | None:
    statement = select(BiographerQuestion).where(
        BiographerQuestion.id == question_id,
        BiographerQuestion.profile_id == profile_id,
    )
    return db.scalar(statement)


def create_question(
    db: Session,
    *,
    profile_id: int,
    topic: str,
    locale: str,
    question_text: str,
) -> BiographerQuestion:
    question = BiographerQuestion(
        profile_id=profile_id,
        topic=topic,
        locale=locale,
        question_text=question_text,
        status="pending",
        asked_at=datetime.now(timezone.utc),
    )
    db.add(question)
    db.flush()
    return question


def mark_answered(
    db: Session,
    *,
    question: BiographerQuestion,
    answered_by_user_id: int,
    resulting_candidate_id: int | None,
) -> BiographerQuestion:
    question.status = "answered"
    question.answered_at = datetime.now(timezone.utc)
    question.answered_by_user_id = answered_by_user_id
    question.resulting_candidate_id = resulting_candidate_id
    db.flush()
    return question


def mark_skipped(db: Session, *, question: BiographerQuestion) -> BiographerQuestion:
    question.status = "skipped"
    question.skipped_at = datetime.now(timezone.utc)
    db.flush()
    return question

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import BiographerQuestion, ConversationMemoryCandidate


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


def get_unresolved_candidate_topic_keys(db: Session, *, profile_id: int) -> set[str]:
    """Topics whose most recent resulting candidate is still `needs_review`
    - these must not be re-selected while the owner review is outstanding
    (Part D.15 of the task spec), independent of the separate
    unresolved-clarification eligibility gate in `service.get_eligibility`."""

    statement = (
        select(BiographerQuestion.topic)
        .join(ConversationMemoryCandidate, ConversationMemoryCandidate.id == BiographerQuestion.resulting_candidate_id)
        .where(
            BiographerQuestion.profile_id == profile_id,
            ConversationMemoryCandidate.status == "needs_review",
        )
    )
    return {row[0] for row in db.execute(statement).all()}


def create_question(
    db: Session,
    *,
    profile_id: int,
    topic: str,
    locale: str,
    question_text: str,
    generation_mode: str = "deterministic_fallback",
    provider: str | None = None,
    model: str | None = None,
    ai_action_id: int | None = None,
    context_source_count: int | None = None,
    context_chunk_count: int | None = None,
    question_intent: str | None = None,
    validation_result: str | None = None,
    fallback_used: bool = False,
) -> BiographerQuestion:
    question = BiographerQuestion(
        profile_id=profile_id,
        topic=topic,
        locale=locale,
        question_text=question_text,
        status="pending",
        asked_at=datetime.now(timezone.utc),
        generation_mode=generation_mode,
        provider=provider,
        model=model,
        ai_action_id=ai_action_id,
        context_source_count=context_source_count,
        context_chunk_count=context_chunk_count,
        question_intent=question_intent,
        validation_result=validation_result,
        fallback_used=fallback_used,
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


def mark_postponed(db: Session, *, question: BiographerQuestion) -> BiographerQuestion:
    question.status = "postponed"
    question.postponed_at = datetime.now(timezone.utc)
    db.flush()
    return question

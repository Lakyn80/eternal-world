from __future__ import annotations

from app.modules.avatar_persona import build_memory_candidate, should_create_memory_candidate


def test_memory_candidate_is_created_for_unverified_personal_lullaby_memory():
    candidate = build_memory_candidate(
        user_message="Ты помнишь, как пела мне песню перед сном?",
        lack_of_evidence=True,
    )

    assert candidate is not None
    assert candidate.status == "needs_review"
    assert candidate.confidence == "unverified"
    assert "песню перед сном" in candidate.proposed_memory_text


def test_memory_candidate_is_not_created_for_grounded_fact_question():
    assert (
        build_memory_candidate(
            user_message="Где ты жила в детстве?",
            lack_of_evidence=False,
        )
        is None
    )


def test_memory_candidate_is_not_created_for_emotional_support_message():
    assert should_create_memory_candidate(
        user_message="Бабушка, мне сегодня тяжело.",
        lack_of_evidence=True,
    ) is False

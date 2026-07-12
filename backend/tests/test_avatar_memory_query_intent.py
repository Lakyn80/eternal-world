from __future__ import annotations

from app.modules.avatar_persona.memory_query_intent import (
    CORRECTED_MEMORY_EXPANSION_RULE_ID,
    MemoryQueryIntent,
    build_expanded_retrieval_query,
    classify_memory_query_intent,
)


def test_ordinary_factual_question_is_direct_intent():
    result = classify_memory_query_intent("Какую песню ты пела мне перед сном?")

    assert result is MemoryQueryIntent.DIRECT_FACTUAL_MEMORY


def test_correction_question_is_corrected_memory_fact_intent():
    result = classify_memory_query_intent(
        "Ты помнишь, какую песню я называл, а владелец потом исправил?"
    )

    assert result is MemoryQueryIntent.CORRECTED_MEMORY_FACT


def test_disagreement_question_is_multiple_perspective_intent():
    result = classify_memory_query_intent(
        "А если мы по-разному помним песню перед сном, что ты скажешь?"
    )

    assert result is MemoryQueryIntent.MULTIPLE_PERSPECTIVE_QUESTION


def test_unrelated_question_is_not_classified_as_correction_intent():
    result = classify_memory_query_intent("Где ты жила в детстве?")

    assert result is MemoryQueryIntent.DIRECT_FACTUAL_MEMORY


def test_empty_question_falls_back_safely():
    result = classify_memory_query_intent("   ")

    assert result is MemoryQueryIntent.UNKNOWN_OR_AMBIGUOUS


def test_classifier_has_no_case_specific_content():
    # Regression guard: the classifier must generalize to any corrected
    # memory, not just the frozen dataset's bedtime-song case. A question
    # about a completely different topic phrased the same way must still be
    # recognized as correction intent.
    result = classify_memory_query_intent(
        "Ты помнишь, где мы гуляли, а потом бабушка исправила это воспоминание?"
    )

    assert result is MemoryQueryIntent.CORRECTED_MEMORY_FACT


def test_expanded_query_preserves_original_and_stays_generic():
    question = "Ты помнишь, какую песню я называл, а владелец потом исправил?"
    intent = classify_memory_query_intent(question)

    expanded = build_expanded_retrieval_query(question, intent)

    assert expanded is not None
    assert question.casefold() in expanded.casefold()
    # The expansion must never leak the dataset's expected answer or any
    # specific fact — only generic, fact-agnostic retrieval-shaping terms.
    assert "спят усталые игрушки" not in expanded.casefold()
    assert "катюш" not in expanded.casefold()


def test_expanded_query_is_none_for_direct_factual_intent():
    question = "Какую песню ты пела мне перед сном?"
    intent = classify_memory_query_intent(question)

    assert build_expanded_retrieval_query(question, intent) is None


def test_expanded_query_is_none_for_multiple_perspective_intent():
    question = "А если мы по-разному помним песню перед сном, что ты скажешь?"
    intent = classify_memory_query_intent(question)

    assert build_expanded_retrieval_query(question, intent) is None


def test_expansion_rule_id_is_a_stable_safe_identifier():
    assert CORRECTED_MEMORY_EXPANSION_RULE_ID == "corrected_memory_intent_expansion_v1"

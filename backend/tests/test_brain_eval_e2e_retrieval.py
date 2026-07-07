from __future__ import annotations

from types import SimpleNamespace

from app.modules.ai_agents.brain.context import (
    _extract_query_tokens,
    _extract_unicode_tokens,
    build_vector_retrieval_grounded_context,
    select_memory_evidence,
)


def _memory(*, memory_id: int, title: str, content: str) -> SimpleNamespace:
    return SimpleNamespace(
        id=memory_id,
        title=title,
        content=content,
        memory_type="text",
        occurred_at=None,
        occurred_year=None,
    )


def test_russian_query_tokens_are_not_empty():
    tokens = _extract_query_tokens("Где ты выросла в детстве?")
    assert tokens
    assert "выросла" in tokens
    assert "детстве" in tokens


def test_cyrillic_names_are_preserved_in_tokens():
    tokens = _extract_unicode_tokens("Павел Новак жил в Брно")
    assert "павел" in tokens
    assert "новак" in tokens
    assert "брно" in tokens


def test_czech_diacritics_are_tokenized():
    tokens = _extract_unicode_tokens("Kde jsi vyrůstala jako malá v Popicích?")
    assert "vyrůstala" in tokens
    assert "popicích" in tokens


def test_english_tokens_still_work():
    tokens = _extract_query_tokens("Where did you grow up as a child?")
    assert "where" in tokens
    assert "grow" in tokens
    assert "child" in tokens


def test_cyrillic_query_does_not_fallback_to_first_memories():
    memories = [
        _memory(
            memory_id=1,
            title="[f002] Mikulov market",
            content="На рынке в Микулове она покупала абрикосы.",
        ),
        _memory(
            memory_id=2,
            title="[f001] Popice childhood",
            content="В детстве Ева жила в домике у села Попице на южной Мораве.",
        ),
    ]

    selected = select_memory_evidence(
        memories=memories,
        user_message="Где ты выросла в детстве?",
    )

    assert selected
    assert all(item.selection_reason.startswith("keyword_overlap:") for item in selected)
    assert selected[0].source_id == 2
    assert "latest_timeline_fallback" not in {item.selection_reason for item in selected}


def test_cyrillic_query_without_overlap_returns_no_memory_fallback():
    memories = [
        _memory(
            memory_id=1,
            title="First unrelated memory",
            content="На рынке в Микулове она покупала абрикосы.",
        ),
        _memory(
            memory_id=2,
            title="Second unrelated memory",
            content="В Брно она преподавала литературу.",
        ),
    ]

    selected = select_memory_evidence(
        memories=memories,
        user_message="Где ты выросла в детстве?",
    )

    assert selected == []


def test_popice_childhood_query_prefers_popice_memory_over_mikulov():
    memories = [
        _memory(
            memory_id=10,
            title="[f002] Mikulov",
            content="На рынке в Микулове она покупала абрикосы каждое лето.",
        ),
        _memory(
            memory_id=11,
            title="[f001] Popice",
            content="В детстве Ева жила с родителями в домике у села Попице со сливовым садом.",
        ),
    ]

    selected = select_memory_evidence(
        memories=memories,
        user_message="Где ты выросла в детстве?",
    )

    assert len(selected) == 1
    assert selected[0].source_id == 11
    assert "Попице" in (selected[0].content_preview or "")


def test_vector_only_grounded_context_has_no_memory_evidence():
    profile = SimpleNamespace(
        id=42,
        name="Ева Новакова",
        birth_date=None,
        death_date=None,
        biography=None,
        personality=None,
        catchphrases=None,
    )

    grounded_context = build_vector_retrieval_grounded_context(profile=profile)

    assert grounded_context.evidence_items == []
    assert grounded_context.profile_context.profile_id == 42


def test_no_ascii_only_token_pattern_in_context_module():
    from pathlib import Path

    context_source = Path(__file__).resolve().parents[1] / "app/modules/ai_agents/brain/context.py"
    source_text = context_source.read_text(encoding="utf-8")

    assert "QUERY_TOKEN_PATTERN" not in source_text
    assert "[A-Za-z0-9]" not in source_text
    assert "latest_timeline_fallback" not in source_text

from __future__ import annotations

from app.modules.avatar_persona import (
    derive_avatar_response_directives,
    evaluate_avatar_response_style,
    load_demo_avatar_persona,
)


def test_load_demo_avatar_persona_returns_seeded_eva_profile():
    persona = load_demo_avatar_persona()

    assert persona.avatar_id == "eva_novakova_demo"
    assert persona.display_name == "Ева Новакова"
    assert persona.language == "ru"
    assert "не выдумывать факты" in persona.boundaries


def test_derive_avatar_response_directives_returns_supportive_tone_for_emotional_message():
    persona = load_demo_avatar_persona()

    directives = derive_avatar_response_directives(
        persona=persona,
        user_message="Бабушка, мне сегодня тяжело.",
        lack_of_evidence=False,
    )

    assert directives.emotion.primary == "supportive_warm"
    assert directives.face_directives.expression == "gentle_compassion"
    assert directives.voice_directives.volume == "soft"


def test_evaluate_avatar_response_style_flags_forbidden_client_phrase():
    persona = load_demo_avatar_persona()

    evaluation = evaluate_avatar_response_style(
        answer_text="Как ИИ, я не могу помнить этого.",
        persona=persona,
    )

    assert evaluation["contains_forbidden_client_phrase"] is True
    assert evaluation["mentions_ai_identity"] is True

from __future__ import annotations

from app.modules.ai_agents.brain.prompt_builder import build_brain_prompt_messages
from app.modules.ai_agents.schemas import MemoryProfileContext, OrchestratorChatRequest
from app.modules.avatar_persona import compose_avatar_persona_prompt, load_demo_avatar_persona


def test_compose_avatar_persona_prompt_includes_identity_style_and_boundaries():
    persona = load_demo_avatar_persona()

    prompt = compose_avatar_persona_prompt(persona)

    assert "AVATAR PERSONA (authoritative for character and tone)" in prompt
    assert "- Display name: Ева Новакова" in prompt
    assert "- Role: бабушка" in prompt
    assert "не использовать технические слова вроде RAG, retrieval, chunk" in prompt
    assert persona.lack_of_evidence_style.template in prompt


def test_brain_prompt_messages_include_avatar_persona_section_when_provided():
    persona = load_demo_avatar_persona()

    messages = build_brain_prompt_messages(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=8, name="Ева Новакова"),
            avatar_persona=persona,
            user_message="Бабушка, мне сегодня тяжело.",
            recent_history=[],
        )
    )

    assert "AVATAR PERSONA (authoritative for character and tone)" in messages.system_prompt
    assert "Ева Новакова" in messages.system_prompt
    assert "Preferred wording template" in messages.system_prompt

from __future__ import annotations

from app.modules.avatar_persona.schemas import AvatarPersonaProfile


def compose_avatar_persona_prompt(persona: AvatarPersonaProfile) -> str:
    speaking_style = persona.speaking_style
    emotional_style = persona.emotional_style

    return "\n".join(
        [
            "AVATAR PERSONA (authoritative for character and tone)",
            f"- Avatar ID: {persona.avatar_id}",
            f"- Display name: {persona.display_name}",
            f"- Role: {persona.role}",
            f"- Language: {persona.language}",
            "- Core traits: " + ", ".join(persona.core_traits),
            "- Life background: " + ", ".join(persona.life_background),
            "- Values: " + ", ".join(persona.values),
            "",
            "SPEAKING STYLE",
            f"- Tone: {speaking_style.tone}",
            f"- Sentence length: {speaking_style.sentence_length}",
            "- Addressing examples: " + ", ".join(speaking_style.addressing),
            "- Avoid: " + ", ".join(speaking_style.avoid),
            "",
            "EMOTIONAL STYLE",
            f"- Default emotion: {emotional_style.default_emotion}",
            f"- Sad-user response: {emotional_style.sad_user_response}",
            f"- Trauma-topic response: {emotional_style.trauma_topic_response}",
            f"- Family-topic response: {emotional_style.family_topic_response}",
            "",
            "BOUNDARIES",
            *[f"- {boundary}" for boundary in persona.boundaries],
            "",
            "LACK-OF-EVIDENCE STYLE",
            f"- Preferred wording template: {persona.lack_of_evidence_style.template}",
            "- Persona shapes warmth, tone, and relational style only.",
            "- Persona must never create or upgrade facts without evidence.",
        ]
    )

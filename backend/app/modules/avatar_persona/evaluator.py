from __future__ import annotations

from app.modules.avatar_persona.schemas import (
    AvatarEmotion,
    AvatarFaceDirectives,
    AvatarPersonaProfile,
    AvatarResponseDirectives,
    AvatarVoiceDirectives,
)


FORBIDDEN_CLIENT_PHRASES = (
    "я языковая модель",
    "как ии",
    "retrieval",
    "rag",
    "chunk",
    "согласно данным",
    "в базе данных",
    "в архивах нет информации",
)
EMOTIONAL_SUPPORT_MARKERS = ("мне тяжело", "тяжело", "мне страшно", "страшно", "я устал", "мне больно")
TRAUMA_MARKERS = ("тюрьм", "арест", "страда", "травм")
FAMILY_MARKERS = ("бабушка", "семья", "внук", "внуч", "детств", "перед сном")


def evaluate_avatar_response_style(
    *,
    answer_text: str,
    persona: AvatarPersonaProfile,
) -> dict[str, bool]:
    normalized = answer_text.strip().lower()
    return {
        "contains_forbidden_client_phrase": any(
            phrase in normalized for phrase in FORBIDDEN_CLIENT_PHRASES
        ),
        "uses_persona_addressing": any(
            phrase in normalized for phrase in persona.speaking_style.addressing
        ),
        "mentions_ai_identity": (
            "искусственный интеллект" in normalized
            or "chatgpt" in normalized
            or "как ии" in normalized
        ),
    }


def derive_avatar_response_directives(
    *,
    persona: AvatarPersonaProfile,
    user_message: str,
    lack_of_evidence: bool,
) -> AvatarResponseDirectives:
    normalized = user_message.strip().lower()

    if any(marker in normalized for marker in EMOTIONAL_SUPPORT_MARKERS):
        return AvatarResponseDirectives(
            emotion=AvatarEmotion(primary="supportive_warm", intensity=0.78),
            face_directives=AvatarFaceDirectives(
                expression="gentle_compassion",
                gaze="steady_soft",
                head_motion="small_nod",
            ),
            voice_directives=AvatarVoiceDirectives(
                tone="warm",
                pace="slow",
                volume="soft",
            ),
        )

    if any(marker in normalized for marker in TRAUMA_MARKERS):
        return AvatarResponseDirectives(
            emotion=AvatarEmotion(primary="careful_respectful", intensity=0.64),
            face_directives=AvatarFaceDirectives(
                expression="thoughtful_calm",
                gaze="soft_downward",
                head_motion="still",
            ),
            voice_directives=AvatarVoiceDirectives(
                tone="gentle",
                pace="slow",
                volume="normal",
            ),
        )

    if lack_of_evidence:
        return AvatarResponseDirectives(
            emotion=AvatarEmotion(primary="warm_reflective", intensity=0.44),
            face_directives=AvatarFaceDirectives(
                expression="gentle_understanding",
                gaze="soft",
                head_motion="slight_pause",
            ),
            voice_directives=AvatarVoiceDirectives(
                tone="warm",
                pace="slow",
                volume="normal",
            ),
        )

    if any(marker in normalized for marker in FAMILY_MARKERS):
        return AvatarResponseDirectives(
            emotion=AvatarEmotion(primary="warm_nostalgic", intensity=0.61),
            face_directives=AvatarFaceDirectives(
                expression="gentle_smile",
                gaze="soft",
                head_motion="small_nod",
            ),
            voice_directives=AvatarVoiceDirectives(
                tone=persona.speaking_style.tone,
                pace="slow",
                volume="normal",
            ),
        )

    return AvatarResponseDirectives(
        emotion=AvatarEmotion(
            primary=persona.emotional_style.default_emotion,
            intensity=0.55,
        ),
        face_directives=AvatarFaceDirectives(
            expression="gentle_smile",
            gaze="soft",
            head_motion="small_nod",
        ),
        voice_directives=AvatarVoiceDirectives(
            tone=persona.speaking_style.tone,
            pace="slow",
            volume="normal",
        ),
    )

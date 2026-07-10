from __future__ import annotations

from app.modules.avatar_persona.schemas import AvatarMemoryCandidate


MEMORY_CANDIDATE_SIGNAL_MARKERS = (
    "ты помнишь",
    "помнишь ли",
    "как ты мне",
    "ты мне",
    "пела мне",
    "рассказывала мне",
    "говорила мне",
    "мы с тобой",
    "перед сном",
)
NON_CANDIDATE_SUPPORT_MARKERS = (
    "мне тяжело",
    "мне страшно",
    "ты меня любишь",
    "что бы ты мне посоветовала",
)


def _truncate_text(value: str, *, limit: int = 220) -> str:
    normalized = " ".join(value.split())
    if len(normalized) <= limit:
        return normalized
    return f"{normalized[: limit - 3].rstrip()}..."


def should_create_memory_candidate(*, user_message: str, lack_of_evidence: bool) -> bool:
    if not lack_of_evidence:
        return False

    normalized = user_message.strip().lower()
    if not normalized:
        return False
    if any(marker in normalized for marker in NON_CANDIDATE_SUPPORT_MARKERS):
        return False
    return any(marker in normalized for marker in MEMORY_CANDIDATE_SIGNAL_MARKERS)


def _build_proposed_memory_text(user_message: str) -> str:
    normalized = user_message.strip()
    lowered = normalized.lower()

    if "пела" in lowered and "пес" in lowered and "перед сном" in lowered:
        return "Пользователь предполагает, что Ева пела ему песню перед сном."

    return (
        "Пользователь сообщил о возможном личном воспоминании, которого нет в текущих "
        f"подтверждённых материалах: {_truncate_text(normalized, limit=160)}"
    )


def build_memory_candidate(
    *,
    user_message: str,
    lack_of_evidence: bool,
) -> AvatarMemoryCandidate | None:
    if not should_create_memory_candidate(
        user_message=user_message,
        lack_of_evidence=lack_of_evidence,
    ):
        return None

    return AvatarMemoryCandidate(
        proposed_memory_text=_build_proposed_memory_text(user_message),
        user_message_excerpt=_truncate_text(user_message, limit=160),
        reason=(
            "User introduced a possible personal memory that is not confirmed by the current "
            "grounded evidence for the avatar."
        ),
    )

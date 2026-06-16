from __future__ import annotations

from app.modules.ai_agents.schemas import OrchestratorChatRequest


def build_brain_prompt(request: OrchestratorChatRequest) -> str:
    profile = request.profile
    profile_facts = [
        f"Profile name: {profile.name}",
        f"Biography: {profile.biography or 'unknown'}",
        f"Personality: {profile.personality or 'unknown'}",
        f"Catchphrases: {profile.catchphrases or 'none'}",
        f"Birth date: {profile.birth_date.isoformat() if profile.birth_date else 'unknown'}",
        f"Death date: {profile.death_date.isoformat() if profile.death_date else 'unknown'}",
    ]

    if request.recent_history:
        history_lines = [
            f"{entry.role}: {entry.content}" for entry in request.recent_history
        ]
        formatted_history = "\n".join(history_lines)
    else:
        formatted_history = "No recent chat history."

    return "\n".join(
        [
            "You are the Brain Agent for a memory profile text chat.",
            *profile_facts,
            "Recent conversation:",
            formatted_history,
            f"Current user message: {request.user_message}",
            "Respond in plain text only.",
        ]
    )

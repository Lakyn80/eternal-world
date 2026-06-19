from __future__ import annotations

from app.modules.ai_agents.schemas import OrchestratorChatRequest


def build_brain_prompt(request: OrchestratorChatRequest) -> str:
    grounded_context = request.grounded_context
    profile = grounded_context.profile_context if grounded_context is not None else request.profile

    identity_lines = [
        "A. Avatar identity and style",
        f"- Name: {profile.name}",
        f"- Birth date: {profile.birth_date.isoformat() if profile.birth_date else 'unknown'}",
        f"- Death date: {profile.death_date.isoformat() if profile.death_date else 'unknown'}",
        f"- Biography: {profile.biography or 'unknown'}",
        f"- Personality style hint: {profile.personality or 'unknown'}",
        f"- Catchphrases style hint: {profile.catchphrases or 'none'}",
    ]

    evidence_lines = ["B. Verified memory evidence"]
    if grounded_context is not None and grounded_context.evidence_items:
        for evidence_item in grounded_context.evidence_items:
            evidence_date = (
                evidence_item.occurred_at.isoformat()
                if evidence_item.occurred_at is not None
                else str(evidence_item.occurred_year or "unknown")
            )
            evidence_lines.extend(
                [
                    (
                        f"- [memory:{evidence_item.source_id}] {evidence_date} | "
                        f"{evidence_item.title} | type={evidence_item.memory_type}"
                    ),
                    f"  Preview: {evidence_item.content_preview or 'none'}",
                    f"  Selection reason: {evidence_item.selection_reason}",
                ]
            )
    else:
        evidence_lines.append("- No verified memory evidence is currently available in stored memories.")

    grounding_lines = [
        "C. Grounding instructions",
        "- Answer factual questions only from the verified evidence and profile facts provided above.",
        "- Do not invent unknown facts, dates, places, people, relationships, or events.",
        "- If an answer is not present in the stored memories/context, say that it is not available in the stored memories/context.",
        "- Do not pretend to remember something that is not in evidence.",
        "- Style, personality, and catchphrases may influence tone, but must not create facts.",
        "- Keep responses warm, respectful, and emotionally safe.",
        "- When using a memory fact, stay close to the evidence.",
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
            *identity_lines,
            *evidence_lines,
            *grounding_lines,
            "Recent conversation:",
            formatted_history,
            f"Current user message: {request.user_message}",
            "Respond in plain text only.",
        ]
    )

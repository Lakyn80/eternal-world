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
    memory_evidence_items = grounded_context.evidence_items if grounded_context is not None else []
    rag_evidence_items = grounded_context.retrieved_evidence_items if grounded_context is not None else []

    if memory_evidence_items or rag_evidence_items:
        if memory_evidence_items:
            evidence_lines.append("B1. Timeline memory evidence (curated personal memories)")
            for evidence_item in memory_evidence_items:
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
                        f"  Excerpt: {evidence_item.content_preview or 'none'}",
                        f"  Selection reason: {evidence_item.selection_reason}",
                    ]
                )

        if rag_evidence_items:
            evidence_lines.append("B2. Retrieved archival RAG evidence (document chunks)")
            for evidence_item in rag_evidence_items:
                evidence_lines.extend(
                    [
                        (
                            f"- [rag:{evidence_item.chunk_id}] score={evidence_item.score:.4f} | "
                            f"source_id={evidence_item.source_id} | type={evidence_item.source_document_type}"
                        ),
                        f"  Excerpt: {evidence_item.content_preview or 'none'}",
                        (
                            "  Metadata: "
                            f"embedding_id={evidence_item.embedding_id}, "
                            f"language={evidence_item.language or 'unknown'}, "
                            f"validation={evidence_item.validation_status}, "
                            f"text_hash={evidence_item.text_hash}"
                        ),
                    ]
                )
    else:
        evidence_lines.append("- No verified memory evidence is currently available in stored memories/context.")

    grounding_lines = [
        "C. Grounding instructions",
        "- Answer factual questions only from the verified evidence and profile facts provided above.",
        "- Do not invent unknown facts, dates, places, people, relationships, or events.",
        "- If an answer is not present in the stored memories/context, say that it is not available in the stored memories/context.",
        "- Do not pretend to remember something that is not in evidence.",
        "- When stating a factual claim, cite the source inline using [memory:id] or [rag:chunk_id].",
        "- Respond in the same language as the user's current message when the evidence allows.",
        "- Use B1 timeline memories for personal recollection; use B2 RAG archival evidence for document facts.",
        "- If B1 and B2 conflict, do not merge them silently; acknowledge uncertainty and cite both sources.",
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

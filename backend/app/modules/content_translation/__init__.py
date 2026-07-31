"""Backend content translation module (Task 64.5.1 / 65.13.2).

Translates dynamic, user-authored bilingual/multilingual content on the
backend only. This module never approves memory, never indexes memory,
and never overwrites the human-authored source text. It is deliberately
separate from ``frontend`` static UI localization (see
``frontend/lib/i18n``), which handles labels/buttons/navigation only.

Task 65.13.2 generalized the store (Decision B): language capability is
sourced from ``language_registry``, ``de`` is a supported translation
language, same-language requests persist as identity results, human
overrides are first-class, and async work uses the job/outbox contract on
the ``ai_generation`` queue.

Responsibilities:
    - preserve the exact source text and its language
    - request a faithful, non-creative translation from the configured
      OpenAI-compatible provider (DeepSeek by default), reusing the same
      provider architecture as ``app.modules.ai_agents.brain``
    - validate the structured provider response (non-empty, no invented
      claims heuristics)
    - track translation status (pending/translated/failed/stale/human_reviewed)
    - detect staleness whenever the source text changes
    - expose safe, idempotent retry and authorized human overrides

Explicitly out of scope here: retrieval, ranking, embeddings, Qdrant,
Redis cache semantics, and any change to BGE-M3 or top_k. Those remain
untouched per the Eternal World avatar quality protocol.
"""

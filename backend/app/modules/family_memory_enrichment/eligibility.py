from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.metrics import observe_memory_promotion_blocked
from app.modules.content_translation import service as content_translation_service
from app.modules.family_memory_enrichment import repository


INDEXABLE_PRIVACY_SCOPES = frozenset({"all_family", "public_legacy"})

#: Only Czech-origin candidates require a current Russian translation before
#: promotion/indexing - the Russian avatar pipeline remains the canonical
#: retrieval/answer-generation language (Task 64.5.1). Russian-origin
#: candidates are unaffected and never require a translation to be indexed.
REQUIRED_TRANSLATION_TARGET_LANGUAGE = "ru"
REQUIRED_TRANSLATION_SOURCE_LANGUAGE = "cs"
FINALIZED_MEMORY_FIELD_NAME = "finalized_memory_text"


class FamilyMemoryEligibilityError(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__("Family memory is not eligible")
        self.reason = reason


def get_finalized_memory_translation_block_reason(db: Session, *, candidate) -> str | None:
    """Russian-translation eligibility gate for Czech-origin candidates.

    Returns ``None`` when no translation is required (Russian-origin
    candidates) or when a current, successful Russian translation of the
    *current* ``finalized_memory_text`` exists. Otherwise returns one of
    ``russian_translation_missing`` / ``russian_translation_failed`` /
    ``russian_translation_stale``. Staleness is derived from a source-hash
    comparison against the live ``finalized_memory_text``, not merely the
    stored status, so an edit that changed the source without triggering a
    fresh translation is always caught.
    """
    if candidate.language != REQUIRED_TRANSLATION_SOURCE_LANGUAGE:
        return None
    finalized_text = (candidate.finalized_memory_text or "").strip()
    if not finalized_text:
        return None
    return content_translation_service.resolve_required_translation_block_reason(
        db,
        entity_type="memory_candidate",
        entity_id=str(candidate.id),
        field_name=FINALIZED_MEMORY_FIELD_NAME,
        target_language=REQUIRED_TRANSLATION_TARGET_LANGUAGE,
        current_source_text=finalized_text,
    )


def get_promotion_block_reason(db: Session, *, candidate) -> str | None:
    if candidate.status != "approved":
        return "not_approved"
    if candidate.enrichment_status != "ready_for_owner_review":
        return "collecting_details" if candidate.enrichment_status == "collecting_details" else "incomplete"
    if not (candidate.finalized_memory_text or "").strip():
        return "incomplete"
    if candidate.unresolved_clarification_count > 0:
        return "unresolved_clarification"
    if repository.list_pending_required_clarifications(db, candidate_id=candidate.id):
        return "unresolved_clarification"
    if candidate.privacy_scope not in INDEXABLE_PRIVACY_SCOPES:
        return "privacy_scope"
    if candidate.dispute_status == "disputed":
        return "disputed"
    if candidate.workflow_version >= 2 and candidate.owner_review_actor_role != "owner":
        return "unauthorized_reviewer"
    translation_block_reason = get_finalized_memory_translation_block_reason(db, candidate=candidate)
    if translation_block_reason is not None:
        return translation_block_reason
    return None


def assert_candidate_eligible_for_promotion(db: Session, *, candidate) -> None:
    reason = get_promotion_block_reason(db, candidate=candidate)
    if reason is not None:
        observe_memory_promotion_blocked(reason=reason)
        raise FamilyMemoryEligibilityError(reason)

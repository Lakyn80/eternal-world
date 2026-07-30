from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.metrics import observe_memory_promotion_blocked
from app.modules.content_translation import service as content_translation_service
from app.modules.family_memory_enrichment import repository
from app.modules.family_memory_enrichment.enums import PrivacyScope


#: Privacy scopes eligible for promotion into the canonical
#: avatar-memory/indexing pipeline at all. This gate answers "may this ever
#: be embedded and written to Qdrant?" - it does NOT answer "who may
#: retrieve it once indexed?"; that second question is enforced separately,
#: at retrieval time, by `rag_retrieval.service` filtering
#: `private_owner`-scoped evidence to the memorial's own owning account
#: (Task 65.6.1).
#:
#: `PRIVATE_OWNER` is included here because an owner-only memory is still a
#: real, approved, authoritative fact about the memorial that the owner's
#: own avatar chat must be able to recall - excluding it entirely (as this
#: set used to do) silently discarded every approved AI-Biographer memory,
#: which is always created with `privacy_scope=private_owner`
#: (`avatar_biographer.service`), since Biographer conversations are
#: inherently 1:1 with the memorial owner. `SELECTED_FAMILY` is
#: deliberately left out for now - no retrieval-time enforcement exists yet
#: for the "named subset of family members" scope, and adding it without
#: that enforcement would be a real privacy regression rather than a fix.
INDEXABLE_PRIVACY_SCOPES = frozenset(
    {PrivacyScope.PRIVATE_OWNER.value, "all_family", "public_legacy"}
)

#: Deliberately UNCHANGED from before Task 65.6.1 and DISTINCT from
#: `INDEXABLE_PRIVACY_SCOPES` above, even though the two sets used to be
#: identical. This one answers a different question: "should a non-owner
#: actor (contributor/trusted_reviewer) be able to view this candidate
#: record / its full contribution history at all?" -
#: `family_memory_enrichment.service._can_view_candidate` and
#: `list_contributions` are the only callers. Broadening
#: `INDEXABLE_PRIVACY_SCOPES` to include `private_owner` for promotion
#: eligibility must NOT also broaden who may see a `private_owner`-scoped
#: candidate's own contribution history - that would be a real visibility
#: regression, not a fix. Keep these two constants independent even if a
#: future change makes one of them diverge further.
BROAD_VISIBILITY_PRIVACY_SCOPES = frozenset({"all_family", "public_legacy"})

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

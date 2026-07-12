from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.metrics import observe_memory_promotion_blocked
from app.modules.family_memory_enrichment import repository


INDEXABLE_PRIVACY_SCOPES = frozenset({"all_family", "public_legacy"})


class FamilyMemoryEligibilityError(Exception):
    def __init__(self, reason: str) -> None:
        super().__init__("Family memory is not eligible")
        self.reason = reason


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
    return None


def assert_candidate_eligible_for_promotion(db: Session, *, candidate) -> None:
    reason = get_promotion_block_reason(db, candidate=candidate)
    if reason is not None:
        observe_memory_promotion_blocked(reason=reason)
        raise FamilyMemoryEligibilityError(reason)

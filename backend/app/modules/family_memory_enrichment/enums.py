from enum import Enum


class FamilyMemoryActorRole(str, Enum):
    OWNER = "owner"
    CONTRIBUTOR = "contributor"
    TRUSTED_REVIEWER = "trusted_reviewer"
    SYSTEM = "system"


class MemoryType(str, Enum):
    GENERAL = "general"
    BEDTIME_SONG = "bedtime_song"


class EnrichmentStatus(str, Enum):
    DRAFT = "draft"
    COLLECTING_DETAILS = "collecting_details"
    READY_FOR_OWNER_REVIEW = "ready_for_owner_review"


class DisputeStatus(str, Enum):
    NONE = "none"
    DISPUTED = "disputed"
    RESOLVED = "resolved"


class PrivacyScope(str, Enum):
    PRIVATE_OWNER = "private_owner"
    SELECTED_FAMILY = "selected_family"
    ALL_FAMILY = "all_family"
    PUBLIC_LEGACY = "public_legacy"


class ContributionType(str, Enum):
    INITIAL_CLAIM = "initial_claim"
    CLARIFICATION_ANSWER = "clarification_answer"
    OWNER_CORRECTION = "owner_correction"
    OWNER_CONFIRMATION = "owner_confirmation"
    REVIEWER_NOTE = "reviewer_note"
    DISPUTE_STATEMENT = "dispute_statement"
    SYSTEM_NORMALIZATION = "system_normalization"


class ClarificationStatus(str, Enum):
    PENDING = "pending"
    ANSWERED = "answered"
    SKIPPED = "skipped"
    CANCELLED = "cancelled"


class OwnerReviewAction(str, Enum):
    CONFIRM = "confirm"
    EDIT_AND_CONFIRM = "edit_and_confirm"
    REJECT = "reject"
    REQUEST_MORE_DETAILS = "request_more_details"
    MARK_DISPUTED = "mark_disputed"
    APPROVE_MULTIPLE_PERSPECTIVES = "approve_multiple_perspectives"

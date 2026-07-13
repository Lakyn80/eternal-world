export type FamilyMemoryActorRole = "owner" | "contributor" | "trusted_reviewer";

export type MemoryType = "general" | "bedtime_song";

export type EnrichmentStatus = "draft" | "collecting_details" | "ready_for_owner_review";

export type DisputeStatus = "none" | "disputed" | "resolved";

export type PrivacyScope = "private_owner" | "selected_family" | "all_family" | "public_legacy";

export type ContributionType =
  | "initial_claim"
  | "clarification_answer"
  | "owner_correction"
  | "owner_confirmation"
  | "reviewer_note"
  | "dispute_statement"
  | "system_normalization";

export type ClarificationStatus = "pending" | "answered" | "skipped" | "cancelled";

export type OwnerReviewAction =
  | "confirm"
  | "edit_and_confirm"
  | "reject"
  | "request_more_details"
  | "mark_disputed"
  | "approve_multiple_perspectives";

export type ReviewStatus = "needs_review" | "approved" | "rejected" | "archived";

export type PromotionStatus = "pending_index" | "indexed" | "failed" | "cancelled";

export type MemoryCandidateSource = "conversation";

export type MemoryCandidateConfidence = "unverified";

export type ActorContext = {
  actorId: string;
  actorRole: FamilyMemoryActorRole;
  relationshipToOwner?: string | null;
};

export type MemoryCandidateRead = {
  candidate_id: number;
  owner_user_id: number;
  avatar_id: string;
  profile_id: number | null;
  conversation_id: string | null;
  trace_id: string | null;
  source: MemoryCandidateSource;
  status: ReviewStatus;
  confidence: MemoryCandidateConfidence;
  user_message_excerpt: string;
  proposed_memory_text: string;
  reason: string;
  language: string | null;
  created_at: string;
  updated_at: string;
  reviewed_at: string | null;
  reviewed_by: number | null;
  review_note: string | null;
  rejection_reason: string | null;
  memory_type: MemoryType;
  enrichment_status: EnrichmentStatus;
  finalized_memory_text: string | null;
  privacy_scope: PrivacyScope;
  dispute_status: DisputeStatus;
  finalized_at: string | null;
  finalized_by: string | null;
  owner_reviewed_at: string | null;
  owner_reviewed_by: string | null;
  owner_review_actor_role: string | null;
  unresolved_clarification_count: number;
  version: number;
  workflow_version: number;
};

export type MemoryCandidateSummary = {
  candidate_id: number;
  status: ReviewStatus;
  workflow_version: number;
  memory_type: MemoryType;
  enrichment_status: EnrichmentStatus;
  privacy_scope: PrivacyScope;
  dispute_status: DisputeStatus;
  unresolved_clarification_count: number;
  finalized_memory_text: string | null;
  user_message_excerpt: string;
  created_at: string;
  updated_at: string;
  contributor_actor_id: string | null;
  contributor_actor_role: FamilyMemoryActorRole | null;
  contributor_relationship_to_owner: string | null;
  promotion_id: number | null;
  promotion_status: PromotionStatus | null;
  searchable_as_fact: boolean;
};

export type MemoryCandidateSummaryListResponse = {
  items: MemoryCandidateSummary[];
  total: number;
};

export type FamilyMemoryContributionRead = {
  contribution_id: number;
  candidate_id: number;
  avatar_id: string;
  profile_id: number | null;
  actor_id: string;
  actor_role: FamilyMemoryActorRole;
  relationship_to_owner: string | null;
  contribution_type: ContributionType;
  contribution_text: string;
  structured_details: Record<string, unknown> | null;
  language: string | null;
  source_message_hash: string | null;
  trace_id: string | null;
  supersedes_contribution_id: number | null;
  is_owner_correction: boolean;
  is_disputed: boolean;
  privacy_scope_snapshot: PrivacyScope;
  created_at: string;
};

export type ClarificationQuestionRead = {
  clarification_id: number;
  candidate_id: number;
  question_key: string;
  question_text: string;
  language: string | null;
  status: ClarificationStatus;
  required: boolean;
  asked_at: string;
  answered_at: string | null;
  answered_by: string | null;
  answer_contribution_id: number | null;
};

export type CandidateEnrichmentRead = {
  candidate_id: number;
  avatar_id: string;
  profile_id: number | null;
  memory_type: MemoryType;
  enrichment_status: EnrichmentStatus;
  review_status: ReviewStatus;
  dispute_status: DisputeStatus;
  privacy_scope: PrivacyScope;
  unresolved_clarification_count: number;
  finalized_memory_text: string | null;
  finalized_at: string | null;
  finalized_by: string | null;
  owner_reviewed_at: string | null;
  owner_reviewed_by: string | null;
  contribution_count: number;
  next_clarification_question: ClarificationQuestionRead | null;
  promotion_id: number | null;
  promotion_status: PromotionStatus | null;
  searchable_as_fact: boolean;
  explicit_indexing_required: boolean;
};

export type AvatarMemoryPromotionRead = {
  promotion_id: number;
  candidate_id: number;
  owner_user_id: number;
  avatar_id: string;
  profile_id: number | null;
  source_type: "conversation_candidate";
  promotion_status: PromotionStatus;
  approved_memory_text: string;
  normalized_memory_text: string;
  language: string | null;
  searchable_as_fact: boolean;
  created_at: string;
  updated_at: string;
  indexed_at: string | null;
  failed_at: string | null;
  cancelled_at: string | null;
  failure_reason: string | null;
  target_collection_name: string | null;
  qdrant_point_id: string | null;
  indexing_attempt_count: number;
  trace_id: string | null;
  source_candidate_status_snapshot: string;
  review_note_snapshot: string | null;
};

export type AvatarMemoryIndexingRead = {
  promotion_id: number;
  promotion_status: PromotionStatus;
  indexed_at: string | null;
  target_collection_name: string | null;
  qdrant_point_id: string | null;
  searchable_as_fact: boolean;
  result: "indexed" | "already_indexed";
};

export type MemoryCandidateReviewDetail = {
  candidate: MemoryCandidateRead;
  enrichment: CandidateEnrichmentRead | null;
  contributions: FamilyMemoryContributionRead[];
  clarifications: ClarificationQuestionRead[];
  promotion: AvatarMemoryPromotionRead | null;
  is_owner_actor: boolean;
  can_confirm: boolean;
  can_edit_and_confirm: boolean;
  can_reject: boolean;
  can_request_more_details: boolean;
  can_mark_disputed: boolean;
  can_approve_multiple_perspectives: boolean;
  can_index: boolean;
  blocked_reasons: string[];
};

export type OwnerReviewRequestPayload = {
  actor_id: string;
  actor_role: FamilyMemoryActorRole;
  relationship_to_owner?: string | null;
  action: OwnerReviewAction;
  finalized_memory_text?: string | null;
  privacy_scope?: PrivacyScope | null;
  review_note?: string | null;
  rejection_reason?: string | null;
};

export type OwnerReviewResponse = CandidateEnrichmentRead & {
  promotion_created: boolean;
};

export type ApiErrorInfo = {
  status: number;
  detail: string;
};

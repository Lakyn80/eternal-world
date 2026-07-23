export type MemorialRole = 'owner' | 'trusted_reviewer' | 'contributor' | 'viewer';
export type InvitableMemorialRole = 'trusted_reviewer' | 'contributor' | 'viewer';
export type ContributionStatus = 'draft' | 'needs_review' | 'approved' | 'rejected' | 'archived' | 'superseded';
export type PrivacyScope = 'private_owner' | 'selected_family' | 'all_family' | 'public_legacy';

export type AuthSession = {
  accessToken: string;
  email: string;
};

export type MemorialRead = {
  id: number;
  owner_user_id: number;
  name: string;
  birth_date: string | null;
  death_date: string | null;
  biography: string | null;
  personality: string | null;
  catchphrases: string | null;
  is_public: boolean;
  current_user_role: MemorialRole;
  created_at: string;
  updated_at: string;
};

export type MembershipRead = {
  id: number;
  profile_id: number;
  user_id: number;
  email: string;
  full_name: string | null;
  role: MemorialRole;
  status: 'active' | 'revoked';
  created_at: string;
  updated_at: string;
};

export type InvitationCreateResponse = {
  id: number;
  profile_id: number;
  email: string;
  role: InvitableMemorialRole;
  expires_at: string;
  accepted_at: string | null;
  revoked_at: string | null;
  created_at: string;
  token?: string;
  accept_url?: string;
};

export type ContributionRead = {
  id: number;
  profile_id: number;
  author_user_id: number;
  author_email: string;
  title: string;
  memory_text: string;
  source_note: string | null;
  privacy_scope: PrivacyScope;
  status: ContributionStatus;
  is_current: boolean;
  supersedes_contribution_id: number | null;
  reviewed_at: string | null;
  reviewed_by_user_id: number | null;
  review_note: string | null;
  rejection_reason: string | null;
  active_memory_eligible: boolean;
  indexing_status: ContributionIndexingStatus;
  created_at: string;
  updated_at: string;
};

export type WorkspaceTab = 'overview' | 'biography' | 'biographer' | 'chat' | 'contributions' | 'review' | 'members' | 'invitations';

export type ChatMessageRead = {
  id: number;
  profile_id: number | null;
  role: string;
  content: string;
  created_at: string;
};

export type ChatSendResponse = {
  message_id: number;
  profile_id: number;
  conversation_id: string;
  user_message: string;
  ai_response_text: string;
  audio_url: string | null;
  video_url: string | null;
  created_at: string;
};

export type ChatRestoredFrom = 'redis' | 'database' | 'empty';

export type ChatActiveRead = {
  profile_id: number;
  conversation_id: string;
  messages: ChatMessageRead[];
  restored_from: ChatRestoredFrom;
};

export type ContributionIndexingState = 'not_applicable' | 'pending' | 'indexed' | 'failed' | 'retired';

export type ContributionIndexingStatus = {
  state: ContributionIndexingState;
  indexed_at: string | null;
  attempt_count: number;
  failure_reason: string | null;
};

export type BiographyStatusState = 'draft' | 'ready_for_ingestion' | 'ingesting' | 'indexed' | 'failed' | 'stale';

export type BiographyStatusRead = {
  profile_id: number;
  status: BiographyStatusState;
  content_hash: string | null;
  indexed_at: string | null;
  attempt_count: number;
  failure_reason: string | null;
  background_job_status: string | null;
  background_job_id: number | null;
};

export type BiographyIngestionStartResponse = {
  profile_id: number;
  status: BiographyStatusState;
  background_job_id: number;
  background_job_status: string;
};

export type BiographerBlockedReason =
  | 'biography_missing'
  | 'biography_not_indexed'
  | 'biography_stale'
  | 'indexing_in_progress'
  | 'permission_denied'
  | 'active_clarification_exists'
  | 'candidate_waiting_for_review';

export type BiographerEligibilityRead = {
  eligible: boolean;
  blocked_reason: BiographerBlockedReason | null;
};

export type BiographerQuestionStatus = 'pending' | 'answered' | 'skipped' | 'postponed';

export type BiographerGenerationMode = 'llm_generated' | 'deterministic_fallback';

export type BiographerQuestionRead = {
  id: number;
  profile_id: number;
  topic: string;
  locale: 'cs' | 'ru';
  question_text: string;
  status: BiographerQuestionStatus;
  asked_at: string;
  answered_at: string | null;
  resulting_candidate_id: number | null;
  generation_mode: BiographerGenerationMode;
  fallback_used: boolean;
};

export type BiographerAnswerResponse = {
  question: BiographerQuestionRead;
  candidate_id: number | null;
  enrichment_status: string | null;
  unresolved_clarification_count: number | null;
};

export type BiographerResumeNextAction =
  | 'biography_not_indexed'
  | 'biography_indexing'
  | 'question_ready'
  | 'candidate_ready_for_review'
  | 'candidate_needs_owner_action'
  | 'candidate_pending_index'
  | 'candidate_indexed'
  | 'blocked';

export type BiographerResumeRead = {
  profile_id: number;
  biography_status: string;
  eligible: boolean;
  blocked_reason: BiographerBlockedReason | null;
  active_question: BiographerQuestionRead | null;
  candidate_id: number | null;
  review_status: string | null;
  enrichment_status: string | null;
  unresolved_clarification_count: number | null;
  promotion_status: string | null;
  next_action: BiographerResumeNextAction;
};

export type ClarificationStatus = 'pending' | 'answered' | 'skipped';

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

export type MemoryCandidateEnrichmentRead = {
  candidate_id: number;
  avatar_id: string;
  profile_id: number | null;
  memory_type: string;
  enrichment_status: 'draft' | 'collecting_details' | 'ready_for_owner_review';
  review_status: 'needs_review' | 'approved' | 'rejected' | 'archived';
  dispute_status: 'none' | 'disputed' | 'resolved';
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
  promotion_status: string | null;
  searchable_as_fact: boolean;
  explicit_indexing_required: boolean;
};

export type OwnerReviewCandidateAction =
  | 'confirm'
  | 'edit_and_confirm'
  | 'reject'
  | 'request_more_details'
  | 'mark_disputed'
  | 'approve_multiple_perspectives';

export type FamilyContributionType =
  | 'initial_claim'
  | 'clarification_answer'
  | 'owner_correction'
  | 'owner_confirmation'
  | 'reviewer_note'
  | 'dispute_statement'
  | 'system_normalization';

export type FamilyMemoryContributionRead = {
  contribution_id: number;
  candidate_id: number;
  avatar_id: string;
  profile_id: number | null;
  actor_id: string;
  actor_role: 'owner' | 'contributor' | 'trusted_reviewer' | 'system';
  relationship_to_owner: string | null;
  contribution_type: FamilyContributionType;
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

export type CandidateHistoryRead = {
  candidate: MemoryCandidateEnrichmentRead;
  contributions: FamilyMemoryContributionRead[];
  clarifications: ClarificationQuestionRead[];
};

export type AvatarMemoryIndexingRead = {
  promotion_id: number;
  promotion_status: string;
  indexed_at: string | null;
  target_collection_name: string | null;
  qdrant_point_id: string | null;
  searchable_as_fact: boolean;
  result: 'indexed' | 'already_indexed';
};

export type BillingPlanLimits = {
  max_profiles: number | null;
  max_memories: number | null;
  max_audio_minutes: number | null;
  max_videos_per_month: number | null;
  max_video_seconds: number | null;
  allow_watermark_removal: boolean;
  allow_unlimited_chat: boolean;
  allow_priority_support: boolean;
  allow_family_members: boolean;
  allow_shared_memories: boolean;
  allow_family_tree: boolean;
  max_family_members: number | null;
  max_video_quality: string;
};

export type BillingUsageSnapshot = {
  current_profiles: number;
  current_memories: number;
  current_audio_minutes: number;
  current_videos_month: number;
  current_family_members: number;
};

export type BillingLimitsRead = {
  user_id: number;
  plan_code: string;
  limits: BillingPlanLimits;
  current_usage: BillingUsageSnapshot;
};

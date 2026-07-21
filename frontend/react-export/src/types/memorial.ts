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

export type WorkspaceTab = 'overview' | 'chat' | 'contributions' | 'review' | 'members' | 'invitations';

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
  user_message: string;
  ai_response_text: string;
  audio_url: string | null;
  video_url: string | null;
  created_at: string;
};

export type ContributionIndexingState = 'not_applicable' | 'pending' | 'indexed' | 'failed' | 'retired';

export type ContributionIndexingStatus = {
  state: ContributionIndexingState;
  indexed_at: string | null;
  attempt_count: number;
  failure_reason: string | null;
};

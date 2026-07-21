import type {
  BiographerAnswerResponse,
  BiographerEligibilityRead,
  BiographerQuestionRead,
  BiographyStatusRead,
  ChatMessageRead,
  ChatSendResponse,
  ContributionRead,
  InvitationCreateResponse,
  InvitableMemorialRole,
  MembershipRead,
  MemoryCandidateEnrichmentRead,
  MemorialRead,
  OwnerReviewCandidateAction,
  PrivacyScope
} from '../types/memorial';

const API_BASE_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8033';

type LoginResponse = {
  access_token: string;
  token_type: string;
};

type RegisterResponse = {
  email: string;
};

export type MemorialCreatePayload = {
  name: string;
  biography?: string | null;
  personality?: string | null;
  catchphrases?: string | null;
};

export type ContributionCreatePayload = {
  title: string;
  memory_text: string;
  source_note?: string | null;
  privacy_scope: PrivacyScope;
};

export type InvitationCreatePayload = {
  email: string;
  role: InvitableMemorialRole;
};

export class MemorialApiError extends Error {
  readonly status: number;
  readonly detail: string;

  constructor(status: number, detail: string) {
    super(detail);
    this.name = 'MemorialApiError';
    this.status = status;
    this.detail = detail;
  }
}

function buildApiUrl(path: string): string {
  return `${API_BASE_URL.replace(/\/$/, '')}${path}`;
}

async function parseError(response: Response): Promise<string> {
  try {
    const payload = (await response.json()) as { detail?: unknown };
    if (typeof payload.detail === 'string' && payload.detail.trim()) return payload.detail;
    if (Array.isArray(payload.detail)) return 'Submitted data did not pass validation.';
  } catch {
    // Non-JSON responses are intentionally collapsed into a safe message.
  }

  if (response.status === 401) return 'Authentication is required.';
  if (response.status === 403) return 'You do not have permission to perform this action.';
  if (response.status === 404) return 'The memorial or invitation was not found.';
  return 'The request could not be completed.';
}

async function requestJson<T>(path: string, init: RequestInit | undefined = {}, accessToken?: string): Promise<T> {
  const requestInit = init ?? {};
  const headers = new Headers(requestInit.headers);

  if (!headers.has('Content-Type') && requestInit.body) {
    headers.set('Content-Type', 'application/json');
  }
  if (accessToken) {
    headers.set('Authorization', `Bearer ${accessToken}`);
  }

  let response: Response;
  try {
    response = await fetch(buildApiUrl(path), { ...requestInit, headers });
  } catch {
    throw new MemorialApiError(0, 'The server could not be reached.');
  }

  if (!response.ok) {
    throw new MemorialApiError(response.status, await parseError(response));
  }

  return (await response.json()) as T;
}

export async function login(email: string, password: string): Promise<string> {
  const response = await requestJson<LoginResponse>('/api/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password })
  });
  return response.access_token;
}

export async function register(email: string, password: string, fullName: string | null): Promise<RegisterResponse> {
  return requestJson<RegisterResponse>('/api/auth/register', {
    method: 'POST',
    body: JSON.stringify({ email, password, full_name: fullName })
  });
}

export async function listMemorials(accessToken: string): Promise<MemorialRead[]> {
  return requestJson<MemorialRead[]>('/api/memorials', undefined, accessToken);
}

export async function createMemorial(accessToken: string, payload: MemorialCreatePayload): Promise<MemorialRead> {
  return requestJson<MemorialRead>('/api/memorials', { method: 'POST', body: JSON.stringify(payload) }, accessToken);
}

export async function fetchMemorial(accessToken: string, profileId: number): Promise<MemorialRead> {
  return requestJson<MemorialRead>(`/api/memorials/${profileId}`, undefined, accessToken);
}

export async function listMembers(accessToken: string, profileId: number): Promise<MembershipRead[]> {
  return requestJson<MembershipRead[]>(`/api/memorials/${profileId}/members`, undefined, accessToken);
}

export async function inviteParticipant(
  accessToken: string,
  profileId: number,
  payload: InvitationCreatePayload
): Promise<InvitationCreateResponse> {
  return requestJson<InvitationCreateResponse>(
    `/api/memorials/${profileId}/invitations`,
    { method: 'POST', body: JSON.stringify(payload) },
    accessToken
  );
}

export async function acceptInvitation(accessToken: string, token: string): Promise<MembershipRead> {
  return requestJson<MembershipRead>(
    '/api/invitations/accept',
    { method: 'POST', body: JSON.stringify({ token }) },
    accessToken
  );
}

export async function submitContribution(
  accessToken: string,
  profileId: number,
  payload: ContributionCreatePayload
): Promise<ContributionRead> {
  return requestJson<ContributionRead>(
    `/api/memorials/${profileId}/contributions`,
    { method: 'POST', body: JSON.stringify(payload) },
    accessToken
  );
}

export async function updateBiography(accessToken: string, profileId: number, biography: string): Promise<BiographyStatusRead> {
  return requestJson<BiographyStatusRead>(
    `/api/memorials/${profileId}/biography`,
    { method: 'PATCH', body: JSON.stringify({ biography }) },
    accessToken
  );
}

export async function getBiographyStatus(accessToken: string, profileId: number): Promise<BiographyStatusRead> {
  return requestJson<BiographyStatusRead>(`/api/memorials/${profileId}/biography/status`, undefined, accessToken);
}

export async function startBiographyIngestion(accessToken: string, profileId: number): Promise<BiographyStatusRead> {
  return requestJson<BiographyStatusRead>(
    `/api/memorials/${profileId}/biography/ingest`,
    { method: 'POST' },
    accessToken
  );
}

export async function getBiographerEligibility(accessToken: string, profileId: number): Promise<BiographerEligibilityRead> {
  return requestJson<BiographerEligibilityRead>(
    `/api/memorials/${profileId}/biographer/eligibility`,
    undefined,
    accessToken
  );
}

export async function getNextBiographerQuestion(
  accessToken: string,
  profileId: number,
  locale: 'cs' | 'ru'
): Promise<BiographerQuestionRead | null> {
  return requestJson<BiographerQuestionRead | null>(
    `/api/memorials/${profileId}/biographer/next-question?locale=${locale}`,
    undefined,
    accessToken
  );
}

export async function answerBiographerQuestion(
  accessToken: string,
  profileId: number,
  questionId: number,
  locale: 'cs' | 'ru',
  answerText: string
): Promise<BiographerAnswerResponse> {
  return requestJson<BiographerAnswerResponse>(
    `/api/memorials/${profileId}/biographer/questions/${questionId}/answer`,
    { method: 'POST', body: JSON.stringify({ locale, answer_text: answerText }) },
    accessToken
  );
}

export async function skipBiographerQuestion(
  accessToken: string,
  profileId: number,
  questionId: number
): Promise<BiographerQuestionRead> {
  return requestJson<BiographerQuestionRead>(
    `/api/memorials/${profileId}/biographer/questions/${questionId}/skip`,
    { method: 'POST' },
    accessToken
  );
}

export async function listMemoryCandidates(accessToken: string, profileId: number): Promise<MemoryCandidateEnrichmentRead[]> {
  return requestJson<MemoryCandidateEnrichmentRead[]>(`/api/memorials/${profileId}/candidates`, undefined, accessToken);
}

export async function getMemoryCandidate(
  accessToken: string,
  profileId: number,
  candidateId: number
): Promise<MemoryCandidateEnrichmentRead> {
  return requestJson<MemoryCandidateEnrichmentRead>(
    `/api/memorials/${profileId}/candidates/${candidateId}`,
    undefined,
    accessToken
  );
}

export async function answerCandidateClarification(
  accessToken: string,
  profileId: number,
  candidateId: number,
  answerText: string
): Promise<MemoryCandidateEnrichmentRead> {
  return requestJson<MemoryCandidateEnrichmentRead>(
    `/api/memorials/${profileId}/candidates/${candidateId}/clarifications/answer`,
    { method: 'POST', body: JSON.stringify({ answer_text: answerText }) },
    accessToken
  );
}

export async function ownerReviewCandidate(
  accessToken: string,
  profileId: number,
  candidateId: number,
  action: OwnerReviewCandidateAction,
  extra: { finalized_memory_text?: string; privacy_scope?: PrivacyScope; review_note?: string; rejection_reason?: string } = {}
): Promise<MemoryCandidateEnrichmentRead> {
  return requestJson<MemoryCandidateEnrichmentRead>(
    `/api/memorials/${profileId}/candidates/${candidateId}/owner-review`,
    { method: 'POST', body: JSON.stringify({ action, ...extra }) },
    accessToken
  );
}

export async function indexCandidateMemory(
  accessToken: string,
  profileId: number,
  candidateId: number
): Promise<{ result: string; searchable_as_fact: boolean; promotion_status: string }> {
  return requestJson(
    `/api/memorials/${profileId}/candidates/${candidateId}/index`,
    { method: 'POST' },
    accessToken
  );
}

export async function listChatMessages(accessToken: string, profileId: number): Promise<ChatMessageRead[]> {
  return requestJson<ChatMessageRead[]>(`/api/chat/${profileId}/messages`, undefined, accessToken);
}

export async function sendChatMessage(accessToken: string, profileId: number, message: string): Promise<ChatSendResponse> {
  return requestJson<ChatSendResponse>(
    `/api/chat/${profileId}/messages`,
    { method: 'POST', body: JSON.stringify({ message }) },
    accessToken
  );
}

export async function listContributions(accessToken: string, profileId: number): Promise<ContributionRead[]> {
  return requestJson<ContributionRead[]>(`/api/memorials/${profileId}/contributions`, undefined, accessToken);
}

export async function listReviewQueue(accessToken: string, profileId: number): Promise<ContributionRead[]> {
  return requestJson<ContributionRead[]>(`/api/memorials/${profileId}/review-queue`, undefined, accessToken);
}

export async function reviewContribution(
  accessToken: string,
  profileId: number,
  contributionId: number,
  action: 'approve' | 'reject' | 'archive',
  note: string | null = null
): Promise<ContributionRead> {
  const payload = action === 'approve' ? { review_note: note } : { reason: note };
  return requestJson<ContributionRead>(
    `/api/memorials/${profileId}/contributions/${contributionId}/${action}`,
    { method: 'POST', body: JSON.stringify(payload) },
    accessToken
  );
}

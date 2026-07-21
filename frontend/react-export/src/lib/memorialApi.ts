import type {
  ChatMessageRead,
  ChatSendResponse,
  ContributionRead,
  InvitationCreateResponse,
  InvitableMemorialRole,
  MembershipRead,
  MemorialRead,
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

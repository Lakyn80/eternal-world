import type {
  AvatarMemoryIndexingRead,
  AvatarPersonaSettingsRead,
  AvatarPersonaSettingsUpdate,
  BackgroundJobRead,
  BiographerAnswerResponse,
  BiographerEligibilityRead,
  BiographerQuestionRead,
  BiographerResumeRead,
  BillingLimitsRead,
  BiographyIngestionStartResponse,
  BiographyMemoryEntryRead,
  BiographyStatusRead,
  CandidateHistoryRead,
  ChatActiveRead,
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

/** Empty ``VITE_API_URL`` = same-origin relative paths (required for one
 * production image serving both eternalworld.lukiora.ru and
 * eternal.world.lukiora.com behind nginx ``/api`` proxy). Local/dev keeps
 * the localhost default when the env var is unset. */
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
  canonical_language: 'cs' | 'en' | 'ru';
  confirm_canonical_language: true;
};

export type ContributionCreatePayload = {
  title: string;
  memory_text: string;
  source_note?: string | null;
  privacy_scope: PrivacyScope;
  source_language?: string | null;
};

export type InvitationCreatePayload = {
  email: string;
  role: InvitableMemorialRole;
  preferred_locale_hint?: string | null;
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

let onUnauthorized: (() => void) | null = null;

/** Registers a single app-wide callback fired whenever any authenticated
 * request comes back 401 (expired/invalid token) - lets the top-level
 * workspace clear its session once, without every leaf component needing
 * its own expiry-detection logic. Pass `null` to unregister. */
export function setUnauthorizedHandler(handler: (() => void) | null): void {
  onUnauthorized = handler;
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

  if (response.status === 400) return 'The request was rejected as invalid.';
  if (response.status === 401) return 'Authentication is required.';
  if (response.status === 403) return 'You do not have permission to perform this action.';
  if (response.status === 404) return 'The memorial or invitation was not found.';
  if (response.status === 409) return 'This action conflicts with something already in progress.';
  if (response.status === 422) return 'Submitted data did not pass validation.';
  if (response.status === 503) return 'The background worker or search index is temporarily unavailable.';
  return 'The request could not be completed.';
}

// Task 65.7: these three paths are called specifically to CHECK/ESTABLISH
// authentication state, not to perform an already-authenticated action - a
// 401 from any of them is an expected, silent outcome (e.g. "no session
// cookie yet on first visit"), never a sign of a session that WAS active
// suddenly expiring. Every other call goes through the shared
// onUnauthorized wiring below regardless of whether it happens to carry a
// bearer token or relies purely on the browser-session cookie (Part B) -
// unlike the previous accessToken-truthiness check, this also correctly
// signs out a cookie-only (no in-memory token) session on a genuine 401.
const ANONYMOUS_TOLERANT_PATHS = new Set(['/api/auth/login', '/api/auth/register', '/api/auth/session']);

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
    response = await fetch(buildApiUrl(path), {
      ...requestInit,
      headers,
      // Task 65.7: the browser-session cookie is the fallback (and, after
      // a fresh page load, primary) auth channel - it must always ride
      // along, including cross-origin (the Vite dev server and the API
      // are different origins/ports).
      credentials: 'include'
    });
  } catch {
    throw new MemorialApiError(0, 'The server could not be reached.');
  }

  if (!response.ok) {
    const detail = await parseError(response);
    if (response.status === 401 && !ANONYMOUS_TOLERANT_PATHS.has(path)) {
      onUnauthorized?.();
    }
    throw new MemorialApiError(response.status, detail);
  }

  if (response.status === 204) {
    return undefined as T;
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

export type SessionUser = {
  id: number;
  email: string;
  preferred_ui_language?: 'cs' | 'en' | 'ru';
};

export async function updatePreferredUiLanguage(
  accessToken: string,
  preferred_ui_language: 'cs' | 'en' | 'ru'
): Promise<SessionUser> {
  return requestJson<SessionUser>(
    '/api/auth/me/preferences',
    { method: 'PATCH', body: JSON.stringify({ preferred_ui_language }) },
    accessToken
  );
}

/** Task 65.7 (Part B.13): the startup rehydration probe - resolves the
 * browser-session cookie (set by `login`) into the current user, with no
 * bearer token at all. Throws `MemorialApiError(401, ...)` for "no/expired
 * session", which the caller treats as "show the login form", never as a
 * sign-out-with-message event (see `ANONYMOUS_TOLERANT_PATHS` above). */
export async function getSession(): Promise<SessionUser> {
  return requestJson<SessionUser>('/api/auth/session');
}

/** Revokes the browser-session cookie server-side. Safe to call even if no
 * session exists (the backend treats it as a no-op, never an error). */
export async function logoutSession(): Promise<void> {
  await requestJson<void>('/api/auth/logout', { method: 'POST' });
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

export async function getBillingLimits(accessToken: string): Promise<BillingLimitsRead> {
  return requestJson<BillingLimitsRead>('/api/billing/limits', undefined, accessToken);
}

export type MemorialMetadataUpdatePayload = {
  name?: string;
  personality?: string | null;
  catchphrases?: string | null;
};

/** Reuses `/api/memory-profiles/{id}` (ownership-scoped PATCH) rather than
 * `/api/memorials` (which has no update endpoint at all) - both operate on
 * the same underlying `MemoryProfile` row (Task 65.5). Never sends
 * `biography` through this path: that field has its own dedicated
 * save/index/clear lifecycle and must not be touched by a plain metadata
 * edit, or `biography_status` would desync from the actual saved text. */
export async function updateMemorialMetadata(
  accessToken: string,
  profileId: number,
  payload: MemorialMetadataUpdatePayload
): Promise<MemorialRead> {
  return requestJson<MemorialRead>(
    `/api/memory-profiles/${profileId}`,
    { method: 'PATCH', body: JSON.stringify(payload) },
    accessToken
  );
}

/** Removes only the biography text and its indexed vectors - membership,
 * invitations, contributions, and other approved memories are untouched.
 * Distinct from `deleteMemorial`, which removes the whole memorial. */
export async function clearBiography(accessToken: string, profileId: number): Promise<BiographyStatusRead> {
  return requestJson<BiographyStatusRead>(
    `/api/memorials/${profileId}/biography/clear`,
    { method: 'POST' },
    accessToken
  );
}

/** Deletes the whole memorial (owner-only, enforced server-side). Reuses
 * `/api/memory-profiles/{id}` since `/api/memorials` has no delete
 * endpoint. */
export async function deleteMemorial(accessToken: string, profileId: number): Promise<void> {
  await requestJson<unknown>(`/api/memory-profiles/${profileId}`, { method: 'DELETE' }, accessToken);
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

export async function startBiographyIngestion(
  accessToken: string,
  profileId: number
): Promise<BiographyIngestionStartResponse> {
  return requestJson<BiographyIngestionStartResponse>(
    `/api/memorials/${profileId}/biography/ingest`,
    { method: 'POST' },
    accessToken
  );
}

/** Task 65.6.1 (Part E) - approved, promoted candidate memories projected
 * into the Biography tab. Read-only; separate from the free-text
 * `biography` field and its own `getBiographyStatus`/indexing state. */
export async function listBiographyMemoryEntries(
  accessToken: string,
  profileId: number
): Promise<BiographyMemoryEntryRead[]> {
  return requestJson<BiographyMemoryEntryRead[]>(
    `/api/memorials/${profileId}/biography/memory-entries`,
    undefined,
    accessToken
  );
}

export async function getBiographerResume(
  accessToken: string,
  profileId: number,
  locale: 'cs' | 'ru'
): Promise<BiographerResumeRead> {
  return requestJson<BiographerResumeRead>(
    `/api/memorials/${profileId}/biographer/resume?locale=${locale}`,
    undefined,
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

export async function postponeBiographerQuestion(
  accessToken: string,
  profileId: number,
  questionId: number
): Promise<BiographerQuestionRead> {
  return requestJson<BiographerQuestionRead>(
    `/api/memorials/${profileId}/biographer/questions/${questionId}/postpone`,
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
): Promise<AvatarMemoryIndexingRead> {
  return requestJson<AvatarMemoryIndexingRead>(
    `/api/memorials/${profileId}/candidates/${candidateId}/index`,
    { method: 'POST' },
    accessToken
  );
}

export async function getCandidateHistory(
  accessToken: string,
  profileId: number,
  candidateId: number
): Promise<CandidateHistoryRead> {
  return requestJson<CandidateHistoryRead>(
    `/api/memorials/${profileId}/candidates/${candidateId}/history`,
    undefined,
    accessToken
  );
}

export async function listChatMessages(accessToken: string, profileId: number): Promise<ChatMessageRead[]> {
  return requestJson<ChatMessageRead[]>(`/api/chat/${profileId}/messages`, undefined, accessToken);
}

export async function sendChatMessage(
  accessToken: string,
  profileId: number,
  message: string,
  options?: { locale?: 'cs' | 'en' | 'ru' | 'de' }
): Promise<ChatSendResponse> {
  const body: { message: string; locale?: string } = { message };
  if (options?.locale) {
    body.locale = options.locale;
  }
  return requestJson<ChatSendResponse>(
    `/api/chat/${profileId}/messages`,
    { method: 'POST', body: JSON.stringify(body) },
    accessToken
  );
}

/** Task 65.7 (Part E.35) - restores the active conversation transcript
 * (Redis fast-path, Postgres fallback/rebuild on a cache miss). */
export async function getActiveChat(accessToken: string, profileId: number): Promise<ChatActiveRead> {
  return requestJson<ChatActiveRead>(`/api/chat/${profileId}/active`, undefined, accessToken);
}

/** "Obnovit chat" - starts a brand-new empty active conversation. Prior
 * messages are preserved (never deleted), just no longer active. */
export async function resetChat(accessToken: string, profileId: number): Promise<ChatActiveRead> {
  return requestJson<ChatActiveRead>(`/api/chat/${profileId}/reset`, { method: 'POST' }, accessToken);
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

/** Task 65.8 (Part I) - authorized reviewer retry of a failed contribution
 * indexing attempt. Only valid once the contribution is approved+current
 * and its indexing status is `failed`; the backend re-derives and returns
 * the resulting content + indexing status, it is never inferred here. */
/** Task 65.9.1 (Part F) - authorization-scoped async job status read, used
 * by the frontend job-status poller for both "Index memory" and
 * retry-indexing. A 404 here means either the job never existed or (Part N)
 * belongs to a different account - the backend deliberately returns the
 * same 404 for both so this call can never be used to probe for another
 * user's job ids. */
export async function getBackgroundJob(accessToken: string, jobId: number): Promise<BackgroundJobRead> {
  return requestJson<BackgroundJobRead>(`/api/jobs/${jobId}`, undefined, accessToken);
}

export async function retryContributionIndexing(
  accessToken: string,
  profileId: number,
  contributionId: number
): Promise<ContributionRead> {
  return requestJson<ContributionRead>(
    `/api/memorials/${profileId}/contributions/${contributionId}/retry-indexing`,
    { method: 'POST' },
    accessToken
  );
}

/** Task 65.12 - canonical avatar persona settings for a memorial. */
export async function getAvatarPersonaSettings(
  accessToken: string,
  profileId: number
): Promise<AvatarPersonaSettingsRead> {
  return requestJson(`/api/memorials/${profileId}/avatar-persona`, undefined, accessToken);
}

export async function updateAvatarPersonaSettings(
  accessToken: string,
  profileId: number,
  payload: AvatarPersonaSettingsUpdate
): Promise<AvatarPersonaSettingsRead> {
  return requestJson(
    `/api/memorials/${profileId}/avatar-persona`,
    { method: 'PATCH', body: JSON.stringify(payload) },
    accessToken
  );
}

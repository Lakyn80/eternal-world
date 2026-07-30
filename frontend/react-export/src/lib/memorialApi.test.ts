import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  MemorialApiError,
  getAvatarPersonaSettings,
  getCandidateHistory,
  indexCandidateMemory,
  login,
  ownerReviewCandidate,
  setUnauthorizedHandler,
  startBiographyIngestion,
  updateAvatarPersonaSettings,
  updateBiography
} from './memorialApi';

function jsonResponse(status: number, body: unknown): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

describe('memorialApi', () => {
  let fetchMock: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    fetchMock = vi.fn();
    vi.stubGlobal('fetch', fetchMock);
    setUnauthorizedHandler(null);
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it('login posts credentials and returns the access token', async () => {
    fetchMock.mockResolvedValueOnce(jsonResponse(200, { access_token: 'tok-123', token_type: 'bearer' }));

    const token = await login('owner@example.com', 'pw');

    expect(token).toBe('tok-123');
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('http://localhost:8033/api/auth/login');
    expect(init?.method).toBe('POST');
    expect(JSON.parse(init?.body as string)).toEqual({ email: 'owner@example.com', password: 'pw' });
  });

  it('attaches the bearer token on authenticated requests', async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(200, {
        profile_id: 7,
        status: 'draft',
        content_hash: null,
        indexed_at: null,
        attempt_count: 0,
        failure_reason: null,
        background_job_status: null,
        background_job_id: null
      })
    );

    await updateBiography('secret-token', 7, 'Once upon a time.');

    const [, init] = fetchMock.mock.calls[0];
    const headers = init?.headers as Headers;
    expect(headers.get('Authorization')).toBe('Bearer secret-token');
    expect(headers.get('Content-Type')).toBe('application/json');
  });

  it('starting biography ingestion posts to the ingest endpoint with no body', async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(202, { profile_id: 7, status: 'ingesting', background_job_id: 42, background_job_status: 'queued' })
    );

    const result = await startBiographyIngestion('secret-token', 7);

    expect(result.background_job_id).toBe(42);
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('http://localhost:8033/api/memorials/7/biography/ingest');
    expect(init?.method).toBe('POST');
    expect(init?.body).toBeUndefined();
  });

  it('owner review forwards privacy scope and finalized text extras', async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(200, {
        candidate_id: 5,
        avatar_id: 'a',
        profile_id: 7,
        memory_type: 'general',
        enrichment_status: 'ready_for_owner_review',
        review_status: 'approved',
        dispute_status: 'none',
        privacy_scope: 'selected_family',
        unresolved_clarification_count: 0,
        finalized_memory_text: 'Edited text',
        finalized_at: null,
        finalized_by: null,
        owner_reviewed_at: null,
        owner_reviewed_by: null,
        contribution_count: 1,
        next_clarification_question: null,
        promotion_id: 9,
        promotion_status: 'pending_index',
        searchable_as_fact: false,
        explicit_indexing_required: true
      })
    );

    await ownerReviewCandidate('secret-token', 7, 5, 'edit_and_confirm', {
      finalized_memory_text: 'Edited text',
      privacy_scope: 'selected_family'
    });

    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('http://localhost:8033/api/memorials/7/candidates/5/owner-review');
    expect(JSON.parse(init?.body as string)).toEqual({
      action: 'edit_and_confirm',
      finalized_memory_text: 'Edited text',
      privacy_scope: 'selected_family'
    });
  });

  it('fetches candidate history from the dedicated endpoint', async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(200, {
        candidate: { candidate_id: 5 },
        contributions: [],
        clarifications: []
      })
    );

    await getCandidateHistory('secret-token', 7, 5);

    const [url] = fetchMock.mock.calls[0];
    expect(url).toBe('http://localhost:8033/api/memorials/7/candidates/5/history');
  });

  it('index result distinguishes indexed from already_indexed', async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(200, {
        promotion_id: 9,
        promotion_status: 'indexed',
        indexed_at: '2026-01-01T00:00:00Z',
        target_collection_name: 'col',
        qdrant_point_id: 'pt',
        searchable_as_fact: true,
        result: 'already_indexed'
      })
    );

    const result = await indexCandidateMemory('secret-token', 7, 5);
    expect(result.result).toBe('already_indexed');
  });

  it('normalizes a 409 conflict into a MemorialApiError carrying the status', async () => {
    fetchMock.mockResolvedValueOnce(jsonResponse(409, { detail: 'A job is already running' }));

    await expect(startBiographyIngestion('secret-token', 7)).rejects.toMatchObject({
      status: 409,
      detail: 'A job is already running'
    });
  });

  it('fires the registered unauthorized handler exactly once on a 401', async () => {
    const handler = vi.fn();
    setUnauthorizedHandler(handler);
    fetchMock.mockResolvedValueOnce(jsonResponse(401, { detail: 'Authentication is required.' }));

    await expect(updateBiography('stale-token', 7, 'x')).rejects.toBeInstanceOf(MemorialApiError);
    expect(handler).toHaveBeenCalledTimes(1);
  });

  it('does not fire the unauthorized handler for anonymous (no-token) 401 responses', async () => {
    const handler = vi.fn();
    setUnauthorizedHandler(handler);
    fetchMock.mockResolvedValueOnce(jsonResponse(401, { detail: 'Invalid credentials' }));

    await expect(login('nobody@example.com', 'wrong')).rejects.toBeInstanceOf(MemorialApiError);
    expect(handler).not.toHaveBeenCalled();
  });

  it('collapses a network failure into a safe, bounded error', async () => {
    fetchMock.mockRejectedValueOnce(new TypeError('network down'));

    await expect(login('owner@example.com', 'pw')).rejects.toMatchObject({
      status: 0,
      detail: 'The server could not be reached.'
    });
  });

  it('gets avatar persona settings for a memorial', async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(200, {
        profile_id: 7,
        voice_mode: 'warm_older',
        voice_style: 'warm',
        personality_traits: ['gentle'],
        primary_language: 'cs',
        supported_languages: ['cs', 'en'],
        remembered_age: 62,
        communication_profile: 'Calm.',
        created_at: null,
        updated_at: null,
        original_recording_available: false,
        voice_provider_supports_style: false,
        voice_provider_supports_age: false
      })
    );

    const result = await getAvatarPersonaSettings('secret-token', 7);

    expect(result.remembered_age).toBe(62);
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('http://localhost:8033/api/memorials/7/avatar-persona');
    expect((init?.headers as Headers).get('Authorization')).toBe('Bearer secret-token');
  });

  it('patches avatar persona settings', async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(200, {
        profile_id: 7,
        voice_mode: 'younger_self',
        voice_style: 'warm',
        personality_traits: ['funny'],
        primary_language: 'en',
        supported_languages: ['en'],
        remembered_age: null,
        communication_profile: '',
        created_at: null,
        updated_at: null,
        original_recording_available: false,
        voice_provider_supports_style: false,
        voice_provider_supports_age: false
      })
    );

    const result = await updateAvatarPersonaSettings('secret-token', 7, {
      voice_mode: 'younger_self',
      personality_traits: ['funny'],
      primary_language: 'en',
      supported_languages: ['en']
    });

    expect(result.voice_mode).toBe('younger_self');
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('http://localhost:8033/api/memorials/7/avatar-persona');
    expect(init?.method).toBe('PATCH');
    expect(JSON.parse(init?.body as string)).toEqual({
      voice_mode: 'younger_self',
      personality_traits: ['funny'],
      primary_language: 'en',
      supported_languages: ['en']
    });
  });
});

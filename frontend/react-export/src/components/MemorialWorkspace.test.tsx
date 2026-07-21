import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  BiographerPanel,
  BiographyPanel,
  CandidatesReviewSection,
  COPY,
  biographerLocale,
  biographyStatusLabel,
  isBiographyJobActive,
  privacyScopeLabel
} from './MemorialWorkspace';
import type { BiographyStatusRead, MemoryCandidateEnrichmentRead } from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    getBiographyStatus: vi.fn(),
    updateBiography: vi.fn(),
    startBiographyIngestion: vi.fn(),
    getBiographerEligibility: vi.fn(),
    getNextBiographerQuestion: vi.fn(),
    answerBiographerQuestion: vi.fn(),
    skipBiographerQuestion: vi.fn(),
    answerCandidateClarification: vi.fn(),
    listMemoryCandidates: vi.fn(),
    ownerReviewCandidate: vi.fn(),
    indexCandidateMemory: vi.fn(),
    getCandidateHistory: vi.fn()
  };
});

const t = COPY.en;

function baseBiographyStatus(overrides: Partial<BiographyStatusRead> = {}): BiographyStatusRead {
  return {
    profile_id: 7,
    status: 'draft',
    content_hash: null,
    indexed_at: null,
    attempt_count: 0,
    failure_reason: null,
    background_job_status: null,
    background_job_id: null,
    ...overrides
  };
}

function baseCandidate(overrides: Partial<MemoryCandidateEnrichmentRead> = {}): MemoryCandidateEnrichmentRead {
  return {
    candidate_id: 5,
    avatar_id: 'avatar-1',
    profile_id: 7,
    memory_type: 'general',
    enrichment_status: 'ready_for_owner_review',
    review_status: 'needs_review',
    dispute_status: 'none',
    privacy_scope: 'all_family',
    unresolved_clarification_count: 0,
    finalized_memory_text: 'Grandma loved gardening.',
    finalized_at: null,
    finalized_by: null,
    owner_reviewed_at: null,
    owner_reviewed_by: null,
    contribution_count: 1,
    next_clarification_question: null,
    promotion_id: null,
    promotion_status: null,
    searchable_as_fact: false,
    explicit_indexing_required: false,
    ...overrides
  };
}

describe('pure helpers', () => {
  it('biographerLocale falls back to Czech for the marketing "en" locale', () => {
    expect(biographerLocale('ru')).toBe('ru');
    expect(biographerLocale('cs')).toBe('cs');
    expect(biographerLocale('en')).toBe('cs');
  });

  it('biographyStatusLabel covers every backend status', () => {
    expect(biographyStatusLabel(t, 'draft')).toBe(t.biographyStatusDraft);
    expect(biographyStatusLabel(t, 'indexed')).toBe(t.biographyStatusIndexed);
    expect(biographyStatusLabel(t, 'stale')).toBe(t.biographyStatusStale);
  });

  it('isBiographyJobActive is true only while a job is genuinely running', () => {
    expect(isBiographyJobActive(baseBiographyStatus({ status: 'ready_for_ingestion' }))).toBe(false);
    expect(isBiographyJobActive(baseBiographyStatus({ status: 'ingesting' }))).toBe(true);
    expect(isBiographyJobActive(baseBiographyStatus({ status: 'draft', background_job_status: 'queued' }))).toBe(true);
    expect(isBiographyJobActive(baseBiographyStatus({ status: 'indexed' }))).toBe(false);
  });

  it('privacyScopeLabel maps every backend scope', () => {
    expect(privacyScopeLabel(t, 'private_owner')).toBe(t.candidatePrivacyPrivateOwner);
    expect(privacyScopeLabel(t, 'public_legacy')).toBe(t.candidatePrivacyPublicLegacy);
  });
});

describe('localization', () => {
  it('Czech and Russian copy are both populated and distinct from each other', () => {
    expect(COPY.cs.biographyStartIngestion).not.toBe('');
    expect(COPY.ru.biographyStartIngestion).not.toBe('');
    expect(COPY.cs.biographyStartIngestion).not.toBe(COPY.ru.biographyStartIngestion);
    expect(COPY.cs.candidateIndexButton).not.toBe(COPY.ru.candidateIndexButton);
  });
});

describe('BiographyPanel', () => {
  beforeEach(() => {
    vi.mocked(api.getBiographyStatus).mockResolvedValue(baseBiographyStatus());
  });

  afterEach(() => {
    vi.clearAllMocks();
  });

  it('seeds the editor with the existing biography text (not empty)', async () => {
    render(
      <BiographyPanel initialBiography="Already written life story." lang="en" profileId={7} t={t} token="tok" />
    );

    const textarea = await screen.findByLabelText(t.biographyTextLabel);
    expect(textarea).toHaveValue('Already written life story.');
  });

  it('saving calls updateBiography but never startBiographyIngestion', async () => {
    vi.mocked(api.updateBiography).mockResolvedValue(baseBiographyStatus({ status: 'ready_for_ingestion' }));
    const user = userEvent.setup();

    render(<BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByLabelText(t.biographyTextLabel);

    await user.click(screen.getByRole('button', { name: t.biographySave }));

    await waitFor(() => expect(api.updateBiography).toHaveBeenCalledWith('tok', 7, 'Text.'));
    expect(api.startBiographyIngestion).not.toHaveBeenCalled();
    expect(await screen.findByText(t.biographySavedNotIndexed)).toBeInTheDocument();
  });

  it('starting indexing requires an explicit confirmation click before calling the backend', async () => {
    vi.mocked(api.getBiographyStatus).mockResolvedValue(baseBiographyStatus({ status: 'ready_for_ingestion' }));
    vi.mocked(api.startBiographyIngestion).mockResolvedValue({
      profile_id: 7,
      status: 'ingesting',
      background_job_id: 1,
      background_job_status: 'queued'
    });
    const user = userEvent.setup();

    render(<BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />);
    const startButton = await screen.findByRole('button', { name: t.biographyStartIngestion });

    await user.click(startButton);
    expect(api.startBiographyIngestion).not.toHaveBeenCalled();
    expect(screen.getByText(t.biographyConfirmStartTitle)).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: t.biographyConfirmStartYes }));
    await waitFor(() => expect(api.startBiographyIngestion).toHaveBeenCalledTimes(1));
  });

  it('shows the failure reason and a retry action when indexing failed', async () => {
    vi.mocked(api.getBiographyStatus).mockResolvedValue(
      baseBiographyStatus({ status: 'failed', failure_reason: 'Worker unavailable', attempt_count: 2 })
    );

    render(<BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />);

    expect(await screen.findByText(/Worker unavailable/)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: t.biographyRetry })).toBeInTheDocument();
  });
});

describe('BiographerPanel', () => {
  afterEach(() => {
    vi.clearAllMocks();
  });

  it('shows the active question with its topic and lets the owner answer it', async () => {
    vi.mocked(api.getBiographerEligibility).mockResolvedValue({ eligible: true, blocked_reason: null });
    vi.mocked(api.getNextBiographerQuestion).mockResolvedValue({
      id: 1,
      profile_id: 7,
      topic: 'childhood',
      locale: 'cs',
      question_text: 'Where did you grow up?',
      status: 'pending',
      asked_at: '2026-01-01T00:00:00Z',
      answered_at: null,
      resulting_candidate_id: null
    });
    vi.mocked(api.answerBiographerQuestion).mockResolvedValue({
      question: {
        id: 1,
        profile_id: 7,
        topic: 'childhood',
        locale: 'cs',
        question_text: 'Where did you grow up?',
        status: 'answered',
        asked_at: '2026-01-01T00:00:00Z',
        answered_at: '2026-01-01T00:01:00Z',
        resulting_candidate_id: 5
      },
      candidate_id: 5,
      enrichment_status: 'ready_for_owner_review',
      unresolved_clarification_count: 0
    });
    vi.mocked(api.getBiographerEligibility).mockResolvedValue({ eligible: true, blocked_reason: null });

    const user = userEvent.setup();
    const onNavigateToReview = vi.fn();
    render(
      <BiographerPanel lang="cs" onNavigateToReview={onNavigateToReview} profileId={7} t={t} token="tok" />
    );

    expect(await screen.findByText('Where did you grow up?')).toBeInTheDocument();
    expect(screen.getByText(new RegExp(t.biographerTopicLabel))).toBeInTheDocument();

    await user.type(screen.getByLabelText(t.biographerAnswerPlaceholder), 'In a small village.');
    await user.click(screen.getByRole('button', { name: t.biographerSubmit }));

    await waitFor(() => expect(api.answerBiographerQuestion).toHaveBeenCalledWith('tok', 7, 1, 'cs', 'In a small village.'));
    expect(await screen.findByText(t.biographerReadyForReview)).toBeInTheDocument();
  });

  it('skip calls the skip endpoint, not the answer endpoint', async () => {
    vi.mocked(api.getBiographerEligibility).mockResolvedValue({ eligible: true, blocked_reason: null });
    vi.mocked(api.getNextBiographerQuestion).mockResolvedValue({
      id: 2,
      profile_id: 7,
      topic: 'family',
      locale: 'ru',
      question_text: 'Расскажи о своей семье.',
      status: 'pending',
      asked_at: '2026-01-01T00:00:00Z',
      answered_at: null,
      resulting_candidate_id: null
    });
    vi.mocked(api.skipBiographerQuestion).mockResolvedValue({
      id: 2,
      profile_id: 7,
      topic: 'family',
      locale: 'ru',
      question_text: 'Расскажи о своей семье.',
      status: 'skipped',
      asked_at: '2026-01-01T00:00:00Z',
      answered_at: null,
      resulting_candidate_id: null
    });

    const user = userEvent.setup();
    render(<BiographerPanel lang="ru" onNavigateToReview={vi.fn()} profileId={7} t={t} token="tok" />);

    await screen.findByText('Расскажи о своей семье.');
    await user.click(screen.getByRole('button', { name: t.biographerSkip }));

    await waitFor(() => expect(api.skipBiographerQuestion).toHaveBeenCalledWith('tok', 7, 2));
    expect(api.answerBiographerQuestion).not.toHaveBeenCalled();
  });
});

describe('CandidatesReviewSection', () => {
  afterEach(() => {
    vi.clearAllMocks();
  });

  it('a contributor (isOwner=false) sees the candidate but no review actions', async () => {
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([baseCandidate()]);

    render(<CandidatesReviewSection isOwner={false} lang="en" profileId={7} t={t} token="tok" />);

    expect(await screen.findByText('Grandma loved gardening.')).toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.candidateConfirm })).not.toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.candidateReject })).not.toBeInTheDocument();
  });

  it('edit and confirm sends the edited text and the selected privacy scope', async () => {
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([baseCandidate()]);
    vi.mocked(api.ownerReviewCandidate).mockResolvedValue(
      baseCandidate({ review_status: 'approved', promotion_id: 9, promotion_status: 'pending_index', explicit_indexing_required: true })
    );
    const user = userEvent.setup();

    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');

    await user.click(screen.getByRole('button', { name: t.candidateEditAndConfirm }));
    const textarea = screen.getByLabelText(t.candidateEditTextareaLabel);
    await user.clear(textarea);
    await user.type(textarea, 'Grandma loved gardening roses.');
    await user.click(screen.getByRole('button', { name: t.candidateEditAndConfirm }));

    await waitFor(() =>
      expect(api.ownerReviewCandidate).toHaveBeenCalledWith(
        'tok',
        7,
        5,
        'edit_and_confirm',
        expect.objectContaining({ finalized_memory_text: 'Grandma loved gardening roses.', privacy_scope: 'all_family' })
      )
    );
    expect(await screen.findByText(t.candidatePendingIndexNotice)).toBeInTheDocument();
  });

  it('reject requires opening the reason field and sends the typed reason', async () => {
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([baseCandidate()]);
    vi.mocked(api.ownerReviewCandidate).mockResolvedValue(baseCandidate({ review_status: 'rejected' }));
    const user = userEvent.setup();

    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');

    await user.click(screen.getByRole('button', { name: t.candidateReject }));
    await user.type(screen.getByLabelText(t.candidateRejectReasonLabel), 'Not accurate');
    await user.click(screen.getByRole('button', { name: t.candidateReject }));

    await waitFor(() =>
      expect(api.ownerReviewCandidate).toHaveBeenCalledWith(
        'tok',
        7,
        5,
        'reject',
        expect.objectContaining({ rejection_reason: 'Not accurate' })
      )
    );
  });

  it('multiple perspectives is only offered when the candidate is disputed', async () => {
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([baseCandidate({ dispute_status: 'none' })]);
    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');
    expect(screen.queryByRole('button', { name: t.candidateApproveMultiplePerspectives })).not.toBeInTheDocument();
  });

  it('indexing requires confirmation, then calls the index endpoint exactly once', async () => {
    const approvedCandidate = baseCandidate({
      review_status: 'approved',
      promotion_id: 9,
      promotion_status: 'pending_index',
      explicit_indexing_required: true
    });
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([approvedCandidate]);
    vi.mocked(api.indexCandidateMemory).mockResolvedValue({
      promotion_id: 9,
      promotion_status: 'indexed',
      indexed_at: '2026-01-01T00:00:00Z',
      target_collection_name: 'col',
      qdrant_point_id: 'pt',
      searchable_as_fact: true,
      result: 'indexed'
    });
    const user = userEvent.setup();

    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');

    await user.click(screen.getByRole('button', { name: t.candidateIndexButton }));
    expect(api.indexCandidateMemory).not.toHaveBeenCalled();
    expect(screen.getByText(t.candidateIndexConfirmTitle)).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: t.candidateIndexConfirmYes }));
    await waitFor(() => expect(api.indexCandidateMemory).toHaveBeenCalledTimes(1));
    expect(api.indexCandidateMemory).toHaveBeenCalledWith('tok', 7, 5);
  });

  it('shows a distinct message when the backend reports already_indexed', async () => {
    const approvedCandidate = baseCandidate({
      review_status: 'approved',
      promotion_id: 9,
      promotion_status: 'indexed',
      explicit_indexing_required: true,
      searchable_as_fact: false
    });
    vi.mocked(api.listMemoryCandidates)
      .mockResolvedValueOnce([approvedCandidate])
      .mockResolvedValueOnce([{ ...approvedCandidate, searchable_as_fact: true }]);
    vi.mocked(api.indexCandidateMemory).mockResolvedValue({
      promotion_id: 9,
      promotion_status: 'indexed',
      indexed_at: '2026-01-01T00:00:00Z',
      target_collection_name: 'col',
      qdrant_point_id: 'pt',
      searchable_as_fact: true,
      result: 'already_indexed'
    });
    const user = userEvent.setup();

    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');
    await user.click(screen.getByRole('button', { name: t.candidateIndexButton }));
    await user.click(screen.getByRole('button', { name: t.candidateIndexConfirmYes }));

    expect(await screen.findByText(t.candidateAlreadyIndexed)).toBeInTheDocument();
  });
});

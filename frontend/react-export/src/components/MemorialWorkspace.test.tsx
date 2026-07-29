import { act, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  BiographerPanel,
  BiographyPanel,
  CandidatesReviewSection,
  ContributionList,
  COPY,
  biographerLocale,
  biographerTopicLabel,
  biographyStatusLabel,
  isBiographyJobActive,
  privacyScopeLabel,
  resetBiographerPanelTestGuards
} from './MemorialWorkspace';
import type {
  BiographerQuestionRead,
  BiographerResumeRead,
  BiographyMemoryEntryRead,
  BiographyStatusRead,
  ClarificationQuestionRead,
  ContributionRead,
  MemoryCandidateEnrichmentRead
} from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    getBiographyStatus: vi.fn(),
    updateBiography: vi.fn(),
    startBiographyIngestion: vi.fn(),
    getBiographerEligibility: vi.fn(),
    getBiographerResume: vi.fn(),
    getNextBiographerQuestion: vi.fn(),
    answerBiographerQuestion: vi.fn(),
    skipBiographerQuestion: vi.fn(),
    postponeBiographerQuestion: vi.fn(),
    answerCandidateClarification: vi.fn(),
    listMemoryCandidates: vi.fn(),
    listBiographyMemoryEntries: vi.fn(),
    ownerReviewCandidate: vi.fn(),
    indexCandidateMemory: vi.fn(),
    getCandidateHistory: vi.fn(),
    getActiveChat: vi.fn(),
    resetChat: vi.fn(),
    sendChatMessage: vi.fn(),
    getSession: vi.fn(),
    logoutSession: vi.fn(),
    retryContributionIndexing: vi.fn(),
    // Task 65.9.1 (Part F/G): defaults to an immediate, harmless 404 so any
    // test that triggers a job-tracking JobStatusBadge (via a `job_id` in
    // an indexCandidateMemory/retryContributionIndexing mock response)
    // without itself caring about live polling never makes a real fetch()
    // call or spins up a real-timer retry loop; tests that DO care about
    // the polling lifecycle override this per-test.
    getBackgroundJob: vi.fn().mockRejectedValue(new actual.MemorialApiError(404, 'Background job not found'))
  };
});

function baseBiographerQuestion(overrides: Partial<BiographerQuestionRead> = {}): BiographerQuestionRead {
  return {
    id: 1,
    profile_id: 7,
    topic: 'childhood',
    locale: 'cs',
    question_text: 'Where did you grow up?',
    status: 'pending',
    asked_at: '2026-01-01T00:00:00Z',
    answered_at: null,
    resulting_candidate_id: null,
    generation_mode: 'llm_generated',
    fallback_used: false,
    ...overrides
  };
}

function baseResume(overrides: Partial<BiographerResumeRead> = {}): BiographerResumeRead {
  return {
    profile_id: 7,
    biography_status: 'indexed',
    eligible: true,
    blocked_reason: null,
    active_question: baseBiographerQuestion(),
    candidate_id: null,
    review_status: null,
    enrichment_status: null,
    unresolved_clarification_count: null,
    promotion_status: null,
    next_action: 'question_ready',
    next_clarification_question: null,
    ...overrides
  };
}

function baseClarificationQuestion(overrides: Partial<ClarificationQuestionRead> = {}): ClarificationQuestionRead {
  return {
    clarification_id: 21,
    candidate_id: 5,
    question_key: 'place',
    question_text: 'Kde se to obvykle odehrávalo?',
    language: 'ru',
    status: 'pending',
    required: true,
    asked_at: '2026-01-01T00:00:00Z',
    answered_at: null,
    answered_by: null,
    answer_contribution_id: null,
    ...overrides
  };
}

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

function baseMemoryEntry(overrides: Partial<BiographyMemoryEntryRead> = {}): BiographyMemoryEntryRead {
  return {
    promotion_id: 1,
    candidate_id: 5,
    text: 'Early childhood was spent in a specific approved place.',
    privacy_scope: 'private_owner',
    promotion_status: 'pending_index',
    searchable_as_fact: false,
    created_at: '2026-07-22T18:48:28.021Z',
    indexed_at: null,
    ...overrides
  };
}

function baseContribution(overrides: Partial<ContributionRead> = {}): ContributionRead {
  return {
    id: 11,
    profile_id: 7,
    author_user_id: 1,
    author_email: 'author@example.com',
    title: 'A recollection',
    memory_text: 'A specific family recollection.',
    source_note: null,
    privacy_scope: 'all_family',
    status: 'approved',
    is_current: true,
    supersedes_contribution_id: null,
    reviewed_at: '2026-07-23T00:00:00Z',
    reviewed_by_user_id: 1,
    review_note: null,
    rejection_reason: null,
    active_memory_eligible: true,
    indexing_status: { state: 'failed', indexed_at: null, attempt_count: 1, failure_reason: 'Contribution indexing failed' },
    created_at: '2026-07-22T00:00:00Z',
    updated_at: '2026-07-23T00:00:00Z',
    ...overrides
  };
}

describe('pure helpers', () => {
  it('biographerLocale falls back to Czech for the marketing "en" locale', () => {
    expect(biographerLocale('ru')).toBe('ru');
    expect(biographerLocale('cs')).toBe('cs');
    expect(biographerLocale('en')).toBe('cs');
  });

  it('biographerTopicLabel localizes every known topic and falls back for unknown ones', () => {
    expect(biographerTopicLabel(t, 'childhood')).toBe(t.biographerTopicChildhood);
    expect(biographerTopicLabel(t, 'values')).toBe(t.biographerTopicValues);
    expect(biographerTopicLabel(t, 'childhood')).not.toBe('childhood');
    expect(biographerTopicLabel(t, 'some_future_topic')).toBe('some future topic');
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
    vi.mocked(api.listBiographyMemoryEntries).mockResolvedValue([]);
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

  it('shows an empty state when no candidate memory has been approved yet', async () => {
    render(<BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />);
    expect(await screen.findByText(t.confirmedMemoriesEmpty)).toBeInTheDocument();
  });

  it('shows a pending-index badge for an approved-but-not-yet-searchable memory, never a searchable one', async () => {
    vi.mocked(api.listBiographyMemoryEntries).mockResolvedValue([
      baseMemoryEntry({ promotion_status: 'pending_index', searchable_as_fact: false })
    ]);

    render(<BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />);

    expect(await screen.findByText('Early childhood was spent in a specific approved place.')).toBeInTheDocument();
    expect(screen.getByText(t.confirmedMemoriesPendingBadge)).toBeInTheDocument();
    expect(screen.queryByText(t.confirmedMemoriesIndexedBadge)).not.toBeInTheDocument();
  });

  it('shows a searchable badge once the promoted memory has been indexed', async () => {
    vi.mocked(api.listBiographyMemoryEntries).mockResolvedValue([
      baseMemoryEntry({ promotion_status: 'indexed', searchable_as_fact: true })
    ]);

    render(<BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />);

    expect(await screen.findByText(t.confirmedMemoriesIndexedBadge)).toBeInTheDocument();
    expect(screen.queryByText(t.confirmedMemoriesPendingBadge)).not.toBeInTheDocument();
  });

  it('shows a failed-indexing badge, distinct from the pending/searchable states', async () => {
    vi.mocked(api.listBiographyMemoryEntries).mockResolvedValue([
      baseMemoryEntry({ promotion_status: 'failed', searchable_as_fact: false })
    ]);

    render(<BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />);

    expect(await screen.findByText(t.confirmedMemoriesFailedBadge)).toBeInTheDocument();
    expect(screen.queryByText(t.confirmedMemoriesPendingBadge)).not.toBeInTheDocument();
    expect(screen.queryByText(t.confirmedMemoriesIndexedBadge)).not.toBeInTheDocument();
  });

  it('re-fetches confirmed memories when the memorial (profileId) switches, never keeping the previous one\'s entries', async () => {
    vi.mocked(api.listBiographyMemoryEntries).mockImplementation(async (_token, profileId) =>
      profileId === 7 ? [baseMemoryEntry({ promotion_id: 1, text: 'Memorial seven memory.' })] : []
    );

    const { rerender } = render(
      <BiographyPanel initialBiography="Text." lang="en" profileId={7} t={t} token="tok" />
    );
    expect(await screen.findByText('Memorial seven memory.')).toBeInTheDocument();

    rerender(<BiographyPanel initialBiography="Other text." lang="en" profileId={8} t={t} token="tok" />);

    await waitFor(() => expect(screen.queryByText('Memorial seven memory.')).not.toBeInTheDocument());
    expect(await screen.findByText(t.confirmedMemoriesEmpty)).toBeInTheDocument();
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

  it(
    'keeps polling after starting indexing until the job actually settles (regression: the panel used to freeze forever after a single bonus check, even while the job was still running)',
    async () => {
      vi.mocked(api.getBiographyStatus)
        .mockResolvedValueOnce(baseBiographyStatus({ status: 'ready_for_ingestion' })) // mount
        .mockResolvedValueOnce(baseBiographyStatus({ status: 'ingesting', background_job_status: 'queued' })) // post-start refresh
        .mockResolvedValueOnce(baseBiographyStatus({ status: 'ingesting', background_job_status: 'running' })) // loop's own immediate tick
        .mockResolvedValueOnce(baseBiographyStatus({ status: 'ingesting', background_job_status: 'running' })) // never reached under the old bug
        .mockResolvedValue(
          baseBiographyStatus({ status: 'indexed', background_job_status: 'succeeded', indexed_at: '2026-07-28T11:12:40Z' })
        );
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
      await user.click(screen.getByRole('button', { name: t.biographyConfirmStartYes }));

      // Call #2 (the immediate post-start refresh) and call #3 (the poll
      // loop's own immediate tick) both land within the first 3s poll
      // interval - this is exactly as far as the old one-shot-bonus-timer
      // code ever got, and it never called again after this regardless of
      // whether the job was still running.
      await waitFor(() => expect(api.getBiographyStatus).toHaveBeenCalledTimes(3));

      // The real poll interval is 3s; waiting past two more real intervals
      // must still keep polling while the job remains active, proving the
      // loop survived past the point the old code died at.
      await waitFor(() => expect(api.getBiographyStatus).toHaveBeenCalledTimes(5), { timeout: 9000, interval: 200 });
      expect(await screen.findByText(t.biographyUpToDate)).toBeInTheDocument();
    },
    12000
  );

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
    resetBiographerPanelTestGuards();
    vi.clearAllMocks();
  });

  function renderPanel(overrides: { lang?: 'cs' | 'ru' | 'en'; onNavigateToBiography?: (() => void) | null } = {}) {
    const onNavigateToReview = vi.fn();
    // `??` would treat an explicitly-passed `null` the same as "not
    // provided" and silently substitute a spy - checking key presence
    // keeps "hides the CTA when the callback is null" actually testable.
    const onNavigateToBiography = Object.prototype.hasOwnProperty.call(overrides, 'onNavigateToBiography')
      ? (overrides.onNavigateToBiography as (() => void) | null)
      : vi.fn();
    const utils = render(
      <BiographerPanel
        email="panel-test@example.com"
        lang={overrides.lang ?? 'cs'}
        onNavigateToBiography={onNavigateToBiography}
        onNavigateToReview={onNavigateToReview}
        profileId={7}
        t={t}
        token="tok"
      />
    );
    return { ...utils, onNavigateToReview, onNavigateToBiography };
  }

  it('shows the active question with a localized topic label and lets the owner answer it', async () => {
    // `load()` (called both on mount and again after a successful answer)
    // calls `getBiographerResume` each time - the second call must reflect
    // the post-answer backend state, exactly like the real API would.
    vi.mocked(api.getBiographerResume)
      .mockResolvedValueOnce(baseResume())
      .mockResolvedValue(baseResume({ active_question: null, candidate_id: 5, next_action: 'candidate_ready_for_review' }));
    vi.mocked(api.answerBiographerQuestion).mockResolvedValue({
      question: baseBiographerQuestion({ status: 'answered', answered_at: '2026-01-01T00:01:00Z', resulting_candidate_id: 5 }),
      candidate_id: 5,
      enrichment_status: 'ready_for_owner_review',
      unresolved_clarification_count: 0
    });

    const user = userEvent.setup();
    renderPanel();

    expect(await screen.findByText('Where did you grow up?')).toBeInTheDocument();
    // Both the topic badge and the relevance sentence mention the topic
    // name, so match the badge's distinct "Topic: <name>" shape specifically.
    expect(screen.getByText(new RegExp(`${t.biographerTopicLabel}.*${t.biographerTopicChildhood}`))).toBeInTheDocument();

    await user.type(screen.getByLabelText(t.biographerAnswerPlaceholder), 'In a small village.');
    await user.click(screen.getByRole('button', { name: t.biographerSubmit }));

    await waitFor(() => expect(api.answerBiographerQuestion).toHaveBeenCalledWith('tok', 7, 1, 'cs', 'In a small village.'));
    expect(await screen.findByText(t.biographerReadyForReview)).toBeInTheDocument();
  });

  it('skip calls the skip endpoint, not the answer or postpone endpoint', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({
        active_question: baseBiographerQuestion({ id: 2, topic: 'family', locale: 'ru', question_text: 'Расскажи о своей семье.' })
      })
    );
    vi.mocked(api.skipBiographerQuestion).mockResolvedValue(
      baseBiographerQuestion({ id: 2, topic: 'family', locale: 'ru', question_text: 'Расскажи о своей семье.', status: 'skipped' })
    );

    const user = userEvent.setup();
    renderPanel({ lang: 'ru' });

    await screen.findByText('Расскажи о своей семье.');
    await user.click(screen.getByRole('button', { name: t.biographerSkip }));

    await waitFor(() => expect(api.skipBiographerQuestion).toHaveBeenCalledWith('tok', 7, 2));
    expect(api.answerBiographerQuestion).not.toHaveBeenCalled();
    expect(api.postponeBiographerQuestion).not.toHaveBeenCalled();
  });

  it('postpone calls the postpone endpoint, not skip or answer', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(baseResume({ active_question: baseBiographerQuestion({ id: 3 }) }));
    vi.mocked(api.postponeBiographerQuestion).mockResolvedValue(baseBiographerQuestion({ id: 3, status: 'postponed' }));

    const user = userEvent.setup();
    renderPanel();

    await screen.findByText('Where did you grow up?');
    await user.click(screen.getByRole('button', { name: t.biographerPostpone }));

    await waitFor(() => expect(api.postponeBiographerQuestion).toHaveBeenCalledWith('tok', 7, 3));
    expect(api.skipBiographerQuestion).not.toHaveBeenCalled();
    expect(api.answerBiographerQuestion).not.toHaveBeenCalled();
  });

  it('shows a blocked message with no question when the biography is not indexed, and never a generic question', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ eligible: false, blocked_reason: 'biography_not_indexed', active_question: null, next_action: 'biography_not_indexed' })
    );

    renderPanel();

    expect(await screen.findByText(t.biographerBlockedNotIndexed)).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
    expect(screen.queryByLabelText(t.biographerAnswerPlaceholder)).not.toBeInTheDocument();
  });

  it('shows an indexing-in-progress message distinct from not-indexed', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ eligible: false, blocked_reason: 'indexing_in_progress', active_question: null, next_action: 'biography_indexing' })
    );

    renderPanel();

    expect(await screen.findByText(t.biographerBlockedIndexing)).toBeInTheDocument();
    expect(screen.queryByText(t.biographerBlockedNotIndexed)).not.toBeInTheDocument();
  });

  it('shows a stale-biography message with a re-index call to action for the owner', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ eligible: false, blocked_reason: 'biography_stale', active_question: null, next_action: 'biography_not_indexed' })
    );

    const { onNavigateToBiography } = renderPanel();

    expect(await screen.findByText(t.biographerBlockedStale)).toBeInTheDocument();
    const cta = screen.getByRole('button', { name: t.biographerGoToBiography });
    await userEvent.setup().click(cta);
    expect(onNavigateToBiography).toHaveBeenCalledTimes(1);
  });

  it('hides the biography call to action for non-owners (onNavigateToBiography=null)', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ eligible: false, blocked_reason: 'biography_not_indexed', active_question: null, next_action: 'biography_not_indexed' })
    );

    renderPanel({ onNavigateToBiography: null });

    await screen.findByText(t.biographerBlockedNotIndexed);
    expect(screen.queryByRole('button', { name: t.biographerGoToBiography })).not.toBeInTheDocument();
  });

  it('shows the candidate-waiting-for-review blocked reason distinctly', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ eligible: false, blocked_reason: 'candidate_waiting_for_review', active_question: null, next_action: 'blocked' })
    );

    renderPanel();

    expect(await screen.findByText(t.biographerBlockedWaitingReview)).toBeInTheDocument();
  });

  // --- Task 65.10.1: the missing clarification question -------------------

  it('shows the blocking notice with the actual clarification question rendered below it, and lets the owner answer it', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({
        eligible: false,
        blocked_reason: 'active_clarification_exists',
        active_question: null,
        candidate_id: 5,
        next_action: 'clarification_pending',
        next_clarification_question: baseClarificationQuestion()
      })
    );
    vi.mocked(api.answerCandidateClarification).mockResolvedValue({
      candidate_id: 5,
      avatar_id: 'avatar-1',
      profile_id: 7,
      memory_type: 'childhood_memory',
      enrichment_status: 'collecting_details',
      review_status: 'needs_review',
      dispute_status: 'none',
      privacy_scope: 'all_family',
      unresolved_clarification_count: 0,
      finalized_memory_text: null,
      finalized_at: null,
      finalized_by: null,
      owner_reviewed_at: null,
      owner_reviewed_by: null,
      contribution_count: 2,
      next_clarification_question: null,
      promotion_id: null,
      promotion_status: null,
      searchable_as_fact: false,
      explicit_indexing_required: false
    });

    const user = userEvent.setup();
    renderPanel();

    // Both the blocking notice AND the real question text must be visible
    // together - the reported bug was the notice with nothing underneath.
    expect(await screen.findByText(t.biographerBlockedActive)).toBeInTheDocument();
    expect(screen.getByText('Kde se to obvykle odehrávalo?')).toBeInTheDocument();

    await user.type(screen.getByLabelText(t.candidateClarificationPlaceholder), 'Na vesnici.');
    await user.click(screen.getByRole('button', { name: t.candidateClarificationSubmit }));

    await waitFor(() => expect(api.answerCandidateClarification).toHaveBeenCalledWith('tok', 7, 5, 'Na vesnici.'));
  });

  it('a session left mid-clarification and resumed later (fresh mount, no prior client state) still renders the real question, not just the notice', async () => {
    // `renderPanel()` always starts from a completely fresh component mount
    // (no `activeCandidateId`/`activeClarificationQuestion` carried over
    // from a previous session) - exactly like reloading the page or
    // navigating back to the workspace tab.
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({
        eligible: false,
        blocked_reason: 'active_clarification_exists',
        active_question: null,
        candidate_id: 9,
        next_action: 'clarification_pending',
        next_clarification_question: baseClarificationQuestion({ clarification_id: 30, candidate_id: 9, question_key: 'approximate_period', question_text: 'Kdy to bylo — přibližně v jakém věku, roce nebo období?' })
      })
    );

    renderPanel();

    expect(await screen.findByText(t.biographerBlockedActive)).toBeInTheDocument();
    expect(screen.getByText('Kdy to bylo — přibližně v jakém věku, roce nebo období?')).toBeInTheDocument();
    expect(screen.getByLabelText(t.candidateClarificationPlaceholder)).toBeInTheDocument();
  });

  it('never shows the active-clarification blocking notice when there is no real question behind it (repaired/inconsistent state)', async () => {
    // The backend repairs a stale `active_clarification_exists` block
    // before resume ever returns it (Task 65.10.1), but the frontend must
    // also never show the notice on its own if it somehow ever received
    // this shape - the notice must only ever accompany the actual question.
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({
        eligible: false,
        blocked_reason: 'active_clarification_exists',
        active_question: null,
        candidate_id: 5,
        next_action: 'clarification_pending',
        next_clarification_question: null
      })
    );

    renderPanel();

    await waitFor(() => expect(api.getBiographerResume).toHaveBeenCalled());
    expect(screen.queryByText(t.biographerBlockedActive)).not.toBeInTheDocument();
  });

  it('does not show the active-clarification notice for an unrelated blocked reason', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ eligible: false, blocked_reason: 'biography_not_indexed', active_question: null, next_action: 'biography_not_indexed' })
    );

    renderPanel();

    await screen.findByText(t.biographerBlockedNotIndexed);
    expect(screen.queryByText(t.biographerBlockedActive)).not.toBeInTheDocument();
  });

  it('resume restores the ready-for-review state without generating a new question after navigating back', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_ready_for_review' })
    );

    renderPanel();

    expect(await screen.findByText(t.biographerReadyForReview)).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
    expect(screen.queryByLabelText(t.biographerAnswerPlaceholder)).not.toBeInTheDocument();
  });

  it('resume shows the pending-index state with a Review CTA', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_pending_index' })
    );

    renderPanel();

    expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();
  });

  it('resume shows the indexed state', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_indexed' })
    );

    renderPanel();

    expect(await screen.findByText(t.biographerCandidateIndexed)).toBeInTheDocument();
  });

  it('restores an unsubmitted draft answer for the same question after remounting', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(baseResume());
    const user = userEvent.setup();
    const { unmount } = renderPanel();

    await screen.findByText('Where did you grow up?');
    await user.type(screen.getByLabelText(t.biographerAnswerPlaceholder), 'A draft in progress');
    unmount();

    renderPanel();
    await screen.findByText('Where did you grow up?');
    expect(screen.getByLabelText(t.biographerAnswerPlaceholder)).toHaveValue('A draft in progress');
  });

  it('does not restore a draft onto a different question', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(baseResume());
    const user = userEvent.setup();
    const { unmount } = renderPanel();
    await screen.findByText('Where did you grow up?');
    await user.type(screen.getByLabelText(t.biographerAnswerPlaceholder), 'A draft in progress');
    unmount();

    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: baseBiographerQuestion({ id: 99, question_text: 'A different question?' }) })
    );
    renderPanel();
    await screen.findByText('A different question?');
    expect(screen.getByLabelText(t.biographerAnswerPlaceholder)).toHaveValue('');
  });

  // --- Task 65.10.5: continue the AI Biographer immediately after an
  // indexed answer, instead of freezing on "Tato vzpomínka byla
  // zaindexována." forever (the panel used to have no way to notice the
  // per-candidate indexing job finishing on its own, and even a fresh
  // resume call kept reporting the same terminal state - fixed on both the
  // backend, `avatar_biographer.resume`, and here). --------------------

  describe('continues the interview automatically after an answer is indexed (Task 65.10.5)', () => {
    it(
      'keeps polling while indexing is pending across multiple intervals, then renders the next real question automatically once the job succeeds - with an empty answer and no duplicate requests',
      async () => {
        const newQuestion = baseBiographerQuestion({
          id: 55,
          topic: 'family',
          question_text: 'Tell me more about your family traditions.'
        });
        vi.mocked(api.getBiographerResume)
          .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_pending_index' })) // mount
          .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_pending_index' })) // poll tick 1 - job still running
          .mockResolvedValueOnce(
            baseResume({ active_question: newQuestion, candidate_id: null, promotion_status: 'indexed', next_action: 'question_ready' })
          ); // poll tick 2 - job succeeded, backend already selected the next question

        renderPanel();

        expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();
        expect(screen.queryByLabelText(t.biographerAnswerPlaceholder)).not.toBeInTheDocument();

        // The real poll interval is 3s; two intervals must elapse for the
        // 3rd (terminal-success) resume call to happen on its own, with no
        // page reload, tab switch, or manual action.
        await waitFor(() => expect(api.getBiographerResume).toHaveBeenCalledTimes(3), { timeout: 9000, interval: 200 });

        expect(await screen.findByText('Tell me more about your family traditions.')).toBeInTheDocument();
        expect(screen.queryByText(t.biographerCandidatePendingIndex)).not.toBeInTheDocument();
        expect(screen.queryByText(t.biographerCandidateIndexed)).not.toBeInTheDocument();
        const textarea = screen.getByLabelText(t.biographerAnswerPlaceholder);
        expect(textarea).toHaveValue('');
        expect(screen.getByRole('button', { name: t.biographerSubmit })).toBeDisabled();

        // The resume response already carried the new question - no extra
        // round trip, and (Required behavior #11) no duplicate resume call
        // sneaks in once the state has settled on `question_ready`.
        expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
        expect(api.getBiographerResume).toHaveBeenCalledTimes(3);
      },
      12000
    );

    it(
      'fetches a freshly generated next question via next-question when resume says question_ready without already including one',
      async () => {
        const generated = baseBiographerQuestion({ id: 61, topic: 'work', question_text: 'What was your first job like?' });
        vi.mocked(api.getBiographerResume)
          .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_pending_index' }))
          .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: null, promotion_status: 'indexed', next_action: 'question_ready' }));
        vi.mocked(api.getNextBiographerQuestion).mockResolvedValue(generated);

        renderPanel();
        expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();

        await waitFor(() => expect(api.getBiographerResume).toHaveBeenCalledTimes(2), { timeout: 9000, interval: 200 });
        expect(await screen.findByText('What was your first job like?')).toBeInTheDocument();
        expect(api.getNextBiographerQuestion).toHaveBeenCalledTimes(1);
      },
      12000
    );

    it(
      'terminal indexing failure stops polling and shows the failure state without ever advancing to another question',
      async () => {
        vi.mocked(api.getBiographerResume)
          .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_pending_index' }))
          .mockResolvedValueOnce(
            baseResume({ active_question: null, candidate_id: 42, promotion_status: 'failed', next_action: 'candidate_indexing_failed' })
          );

        const { onNavigateToReview } = renderPanel();
        expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();

        await waitFor(() => expect(api.getBiographerResume).toHaveBeenCalledTimes(2), { timeout: 9000, interval: 200 });
        expect(await screen.findByText(t.biographerCandidateIndexingFailed)).toBeInTheDocument();
        expect(screen.queryByLabelText(t.biographerAnswerPlaceholder)).not.toBeInTheDocument();
        expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();

        // Manual recovery stays possible via the same Review CTA used for
        // the pending-index state.
        const user = userEvent.setup();
        await user.click(screen.getByRole('button', { name: t.biographerGoToReview }));
        expect(onNavigateToReview).toHaveBeenCalledTimes(1);

        // Polling must have stopped - no further resume calls arrive on
        // their own past the terminal failure.
        expect(api.getBiographerResume).toHaveBeenCalledTimes(2);
      },
      12000
    );

    it('a pending-index poll that resolves into a genuine clarification requirement renders the clarification, never a fabricated question', async () => {
      vi.mocked(api.getBiographerResume)
        .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_pending_index' }))
        .mockResolvedValueOnce(
          baseResume({
            eligible: false,
            blocked_reason: 'active_clarification_exists',
            active_question: null,
            candidate_id: 42,
            next_action: 'clarification_pending',
            next_clarification_question: baseClarificationQuestion({ candidate_id: 42 })
          })
        );

      renderPanel();
      expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();

      await waitFor(() => expect(api.getBiographerResume).toHaveBeenCalledTimes(2), { timeout: 9000, interval: 200 });
      expect(await screen.findByText(t.biographerBlockedActive)).toBeInTheDocument();
      expect(screen.getByText('Kde se to obvykle odehrávalo?')).toBeInTheDocument();
      expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
    });

    it('a pending-index poll that resolves into a genuine owner-review requirement (a different candidate) renders that state, never a fabricated question', async () => {
      vi.mocked(api.getBiographerResume)
        .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_pending_index' }))
        .mockResolvedValueOnce(baseResume({ active_question: null, candidate_id: 43, next_action: 'candidate_ready_for_review' }));

      renderPanel();
      expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();

      await waitFor(() => expect(api.getBiographerResume).toHaveBeenCalledTimes(2), { timeout: 9000, interval: 200 });
      expect(await screen.findByText(t.biographerReadyForReview)).toBeInTheDocument();
      expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
    });

    it('a late-resolving stale resume response (e.g. from a memorial the owner already switched away from) never clobbers a newer question already loaded, or text the owner is mid-typing', async () => {
      let resolveStale: (value: BiographerResumeRead) => void = () => {};
      const stalePromise = new Promise<BiographerResumeRead>((resolve) => {
        resolveStale = resolve;
      });
      let callCount = 0;
      vi.mocked(api.getBiographerResume).mockImplementation(() => {
        callCount += 1;
        if (callCount === 1) return stalePromise;
        return Promise.resolve(
          baseResume({
            active_question: baseBiographerQuestion({ id: 20, question_text: 'New question after switch?' })
          })
        );
      });

      const { rerender } = render(
        <BiographerPanel
          email="panel-test@example.com"
          lang="cs"
          onNavigateToBiography={vi.fn()}
          onNavigateToReview={vi.fn()}
          profileId={7}
          t={t}
          token="tok"
        />
      );

      // The owner switches to a different memorial before the first
      // request ever resolves - a real second `load()` call starts
      // (a new `token`/`profileId`/`locale` mount effect), while the first
      // one is still in flight.
      rerender(
        <BiographerPanel
          email="panel-test@example.com"
          lang="cs"
          onNavigateToBiography={vi.fn()}
          onNavigateToReview={vi.fn()}
          profileId={8}
          t={t}
          token="tok"
        />
      );

      expect(await screen.findByText('New question after switch?')).toBeInTheDocument();

      const user = userEvent.setup();
      await user.type(screen.getByLabelText(t.biographerAnswerPlaceholder), 'typed answer');

      await act(async () => {
        resolveStale(baseResume({ active_question: baseBiographerQuestion({ id: 10, question_text: 'Old question?' }) }));
        await Promise.resolve();
        await Promise.resolve();
      });

      expect(screen.getByText('New question after switch?')).toBeInTheDocument();
      expect(screen.queryByText('Old question?')).not.toBeInTheDocument();
      expect(screen.getByLabelText(t.biographerAnswerPlaceholder)).toHaveValue('typed answer');
    });
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

  it('a failed indexing attempt shows a distinct failed badge and a retry button, never a pending/searchable badge', async () => {
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([
      baseCandidate({
        review_status: 'approved',
        promotion_id: 9,
        promotion_status: 'failed',
        searchable_as_fact: false,
        explicit_indexing_required: false
      })
    ]);

    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');

    expect(screen.getByText(t.candidateIndexingFailedLabel)).toBeInTheDocument();
    expect(screen.queryByText(t.candidatePendingIndexLabel)).not.toBeInTheDocument();
    expect(screen.queryByText(t.candidateIndexedLabel)).not.toBeInTheDocument();
    expect(screen.getByRole('button', { name: t.candidateIndexRetryButton })).toBeInTheDocument();
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

  it('Task 65.9 (Part V): shows a pending notice, never "Indexed", for a freshly-queued async job', async () => {
    const approvedCandidate = baseCandidate({
      review_status: 'approved',
      promotion_id: 9,
      promotion_status: 'pending_index',
      explicit_indexing_required: true,
      searchable_as_fact: false
    });
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([approvedCandidate]);
    vi.mocked(api.indexCandidateMemory).mockResolvedValue({
      promotion_id: 9,
      promotion_status: 'pending_index',
      indexed_at: null,
      target_collection_name: null,
      qdrant_point_id: null,
      searchable_as_fact: false,
      result: 'queued',
      job_id: 42
    });
    const user = userEvent.setup();

    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');
    await user.click(screen.getByRole('button', { name: t.candidateIndexButton }));
    await user.click(screen.getByRole('button', { name: t.candidateIndexConfirmYes }));

    // The status badge already shows this same "pending, not yet indexed"
    // label before the click; after the click, the result notice repeats
    // it (never "Indexed and searchable") - so two occurrences is the
    // correct, expected outcome here, not zero and not a single stale one.
    await waitFor(() => expect(screen.getAllByText(t.candidatePendingIndexLabel).length).toBeGreaterThanOrEqual(2));
    expect(screen.queryByText(t.candidateIndexedLabel)).not.toBeInTheDocument();
  });

  it('Task 65.9.1 (Part F/G): polls the queued job to a terminal state and then reconciles the list', async () => {
    const approvedCandidate = baseCandidate({
      review_status: 'approved',
      promotion_id: 9,
      promotion_status: 'pending_index',
      explicit_indexing_required: true,
      searchable_as_fact: false
    });
    const indexedCandidate = { ...approvedCandidate, promotion_status: 'indexed', searchable_as_fact: true };
    // Called three times: initial mount, the `await load()` immediately
    // after the queued 202 response, and once more when the poller
    // observes the job's terminal `succeeded` state.
    vi.mocked(api.listMemoryCandidates)
      .mockResolvedValueOnce([approvedCandidate])
      .mockResolvedValueOnce([approvedCandidate])
      .mockResolvedValueOnce([indexedCandidate]);
    vi.mocked(api.indexCandidateMemory).mockResolvedValue({
      promotion_id: 9,
      promotion_status: 'pending_index',
      indexed_at: null,
      target_collection_name: null,
      qdrant_point_id: null,
      searchable_as_fact: false,
      result: 'queued',
      job_id: 42
    });
    vi.mocked(api.getBackgroundJob).mockResolvedValue({
      id: 42,
      owner_user_id: 1,
      profile_id: 7,
      job_type: 'qdrant_indexing',
      status: 'succeeded',
      progress_current: 1,
      progress_total: 1,
      celery_task_id: null,
      result_payload: null,
      error_payload: null,
      error_message: null,
      queue: 'embedding',
      attempt_count: 0,
      max_attempts: 3,
      safe_error_category: null,
      created_at: '2026-01-01T00:00:00Z',
      updated_at: '2026-01-01T00:00:00Z'
    });
    const user = userEvent.setup();

    render(<CandidatesReviewSection isOwner lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText('Grandma loved gardening.');
    await user.click(screen.getByRole('button', { name: t.candidateIndexButton }));
    await user.click(screen.getByRole('button', { name: t.candidateIndexConfirmYes }));

    // The poller observes the terminal `succeeded` status (never displayed
    // as "indexed" from the queued response itself, only from the
    // backend-confirmed job) and reconciles by reloading the candidate
    // list, which now reports the promotion as actually indexed.
    await waitFor(() => expect(api.getBackgroundJob).toHaveBeenCalledWith('tok', 42));
    await waitFor(() => expect(api.listMemoryCandidates).toHaveBeenCalledTimes(3));
    expect(await screen.findByText(t.candidateIndexedLabel)).toBeInTheDocument();
  });

  it('Task 65.9.1 (Part G): job-status labels exist for cs/en/ru', () => {
    for (const lang of ['en', 'cs', 'ru'] as const) {
      const copy = COPY[lang];
      expect(copy.jobStatusPending).toBeTruthy();
      expect(copy.jobStatusQueued).toBeTruthy();
      expect(copy.jobStatusProcessing).toBeTruthy();
      expect(copy.jobStatusRetryScheduled).toBeTruthy();
      expect(copy.jobStatusRecoveryPending).toBeTruthy();
      expect(copy.jobStatusSucceeded).toBeTruthy();
      expect(copy.jobStatusFailed).toBeTruthy();
      expect(copy.jobStatusCancelled).toBeTruthy();
      expect(copy.jobStatusUnauthorized).toBeTruthy();
      expect(copy.jobStatusNetworkRetrying).toBeTruthy();
    }
  });
});

describe('ContributionList - Task 65.8 retry / start indexing', () => {
  afterEach(() => {
    vi.mocked(api.retryContributionIndexing).mockReset();
  });

  it('shows the failed badge and a retry button to an authorized reviewer', () => {
    render(
      <ContributionList
        contributions={[baseContribution()]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={vi.fn()}
        profileId={7}
        token="tok"
      />
    );

    expect(screen.getByText(t.indexingFailed)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: t.retryIndexing })).toBeInTheDocument();
  });

  it('shows Index memory for pending indexing without an active job', () => {
    render(
      <ContributionList
        contributions={[
          baseContribution({
            indexing_status: {
              state: 'pending',
              indexed_at: null,
              attempt_count: 0,
              failure_reason: null,
              job_id: null
            }
          })
        ]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={vi.fn()}
        profileId={7}
        token="tok"
      />
    );

    expect(screen.getByText(t.indexingPending)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: t.startIndexing })).toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.retryIndexing })).not.toBeInTheDocument();
  });

  it('hides Index memory while a pending contribution already has an active job', () => {
    render(
      <ContributionList
        contributions={[
          baseContribution({
            indexing_status: {
              state: 'pending',
              indexed_at: null,
              attempt_count: 0,
              failure_reason: null,
              job_id: 42
            }
          })
        ]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={vi.fn()}
        profileId={7}
        token="tok"
      />
    );

    expect(screen.getByText(t.indexingPending)).toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.startIndexing })).not.toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.retryIndexing })).not.toBeInTheDocument();
  });

  it('polls a pending contribution job to succeeded and reconciles via onIndexingSettled', async () => {
    const onIndexingSettled = vi.fn();
    vi.mocked(api.getBackgroundJob).mockResolvedValue({
      id: 42,
      owner_user_id: 1,
      profile_id: 7,
      job_type: 'qdrant_indexing',
      status: 'succeeded',
      progress_current: 1,
      progress_total: 1,
      celery_task_id: null,
      result_payload: null,
      error_payload: null,
      error_message: null,
      queue: 'embedding',
      attempt_count: 0,
      max_attempts: 3,
      safe_error_category: null,
      created_at: '2026-01-01T00:00:00Z',
      updated_at: '2026-01-01T00:00:00Z'
    });

    render(
      <ContributionList
        contributions={[
          baseContribution({
            indexing_status: {
              state: 'pending',
              indexed_at: null,
              attempt_count: 0,
              failure_reason: null,
              job_id: 42
            }
          })
        ]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={vi.fn()}
        onIndexingSettled={onIndexingSettled}
        profileId={7}
        token="tok"
      />
    );

    await waitFor(() => expect(api.getBackgroundJob).toHaveBeenCalledWith('tok', 42));
    await waitFor(() => expect(onIndexingSettled).toHaveBeenCalledTimes(1));
  });

  it('polls pending contribution indexing with an empty cookie-session token', async () => {
    const onIndexingSettled = vi.fn();
    vi.mocked(api.getBackgroundJob).mockResolvedValue({
      id: 42,
      owner_user_id: 1,
      profile_id: 7,
      job_type: 'qdrant_indexing',
      status: 'succeeded',
      progress_current: 1,
      progress_total: 1,
      celery_task_id: null,
      result_payload: null,
      error_payload: null,
      error_message: null,
      queue: 'embedding',
      attempt_count: 0,
      max_attempts: 3,
      safe_error_category: null,
      created_at: '2026-01-01T00:00:00Z',
      updated_at: '2026-01-01T00:00:00Z'
    });

    render(
      <ContributionList
        contributions={[
          baseContribution({
            indexing_status: {
              state: 'pending',
              indexed_at: null,
              attempt_count: 0,
              failure_reason: null,
              job_id: 42
            }
          })
        ]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={vi.fn()}
        onIndexingSettled={onIndexingSettled}
        profileId={7}
        token=""
      />
    );

    await waitFor(() => expect(api.getBackgroundJob).toHaveBeenCalledWith('', 42));
    await waitFor(() => expect(onIndexingSettled).toHaveBeenCalledTimes(1));
  });

  it('never offers indexing actions to a contributor/viewer even for failed indexing', () => {
    render(
      <ContributionList
        contributions={[baseContribution()]}
        lang="en"
        t={t}
        canRetryIndexing={false}
        onIndexingRetried={vi.fn()}
        profileId={7}
        token="tok"
      />
    );

    expect(screen.queryByRole('button', { name: t.retryIndexing })).not.toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.startIndexing })).not.toBeInTheDocument();
  });

  it('never offers indexing actions for an already-indexed contribution', () => {
    render(
      <ContributionList
        contributions={[baseContribution({ indexing_status: { state: 'indexed', indexed_at: '2026-07-23T00:00:00Z', attempt_count: 1, failure_reason: null } })]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={vi.fn()}
        profileId={7}
        token="tok"
      />
    );

    expect(screen.queryByRole('button', { name: t.retryIndexing })).not.toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.startIndexing })).not.toBeInTheDocument();
    expect(screen.getByText(t.indexingIndexed)).toBeInTheDocument();
  });

  it('Index memory calls the same retry-indexing API and reports the updated state upward', async () => {
    const onIndexingRetried = vi.fn();
    vi.mocked(api.retryContributionIndexing).mockResolvedValue(
      baseContribution({
        indexing_status: {
          state: 'pending',
          indexed_at: null,
          attempt_count: 0,
          failure_reason: null,
          job_id: 99
        }
      })
    );
    const user = userEvent.setup();

    render(
      <ContributionList
        contributions={[
          baseContribution({
            indexing_status: {
              state: 'pending',
              indexed_at: null,
              attempt_count: 0,
              failure_reason: null,
              job_id: null
            }
          })
        ]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={onIndexingRetried}
        profileId={7}
        token="tok"
      />
    );

    await user.click(screen.getByRole('button', { name: t.startIndexing }));

    expect(api.retryContributionIndexing).toHaveBeenCalledTimes(1);
    expect(api.retryContributionIndexing).toHaveBeenCalledWith('tok', 7, 11);
    await waitFor(() => expect(onIndexingRetried).toHaveBeenCalledTimes(1));
    expect(onIndexingRetried.mock.calls[0][0].indexing_status.job_id).toBe(99);
  });

  it('retrying calls the API exactly once, disables the button meanwhile, and reports the updated state upward', async () => {
    const onIndexingRetried = vi.fn();
    let resolveRetry: (value: ContributionRead) => void = () => {};
    vi.mocked(api.retryContributionIndexing).mockImplementation(
      () =>
        new Promise((resolve) => {
          resolveRetry = resolve;
        })
    );
    const user = userEvent.setup();

    render(
      <ContributionList
        contributions={[baseContribution()]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={onIndexingRetried}
        profileId={7}
        token="tok"
      />
    );

    const retryButton = screen.getByRole('button', { name: t.retryIndexing });
    await user.click(retryButton);

    expect(api.retryContributionIndexing).toHaveBeenCalledTimes(1);
    expect(api.retryContributionIndexing).toHaveBeenCalledWith('tok', 7, 11);
    expect(retryButton).toBeDisabled();

    // A second click while the request is still in flight must not fire a
    // second API call - the button being disabled already prevents this,
    // asserted explicitly so a future regression (e.g. removing `disabled`)
    // is caught here rather than only in a real double-submit.
    await user.click(retryButton);
    expect(api.retryContributionIndexing).toHaveBeenCalledTimes(1);

    resolveRetry({
      ...baseContribution({ indexing_status: { state: 'indexed', indexed_at: '2026-07-23T01:00:00Z', attempt_count: 2, failure_reason: null } })
    });

    await waitFor(() => expect(onIndexingRetried).toHaveBeenCalledTimes(1));
    expect(onIndexingRetried.mock.calls[0][0].indexing_status.state).toBe('indexed');
  });

  it('shows a safe error message and leaves the button re-clickable when the API call fails', async () => {
    vi.mocked(api.retryContributionIndexing).mockRejectedValue(new Error('boom'));
    const user = userEvent.setup();

    render(
      <ContributionList
        contributions={[baseContribution()]}
        lang="en"
        t={t}
        canRetryIndexing
        onIndexingRetried={vi.fn()}
        profileId={7}
        token="tok"
      />
    );

    await user.click(screen.getByRole('button', { name: t.retryIndexing }));

    await waitFor(() => expect(screen.getByRole('button', { name: t.retryIndexing })).not.toBeDisabled());
    expect(screen.queryByText(/boom|stack|Traceback/i)).not.toBeInTheDocument();
  });

  it('never labels non-indexed contributions as searchable', () => {
    render(
      <ContributionList
        contributions={[
          baseContribution({ id: 1, status: 'needs_review', active_memory_eligible: false, indexing_status: { state: 'not_applicable', indexed_at: null, attempt_count: 0, failure_reason: null } }),
          baseContribution({ id: 2, status: 'rejected', active_memory_eligible: false, indexing_status: { state: 'not_applicable', indexed_at: null, attempt_count: 0, failure_reason: null } }),
          baseContribution({ id: 3, status: 'archived', is_current: false, active_memory_eligible: false, indexing_status: { state: 'retired', indexed_at: null, attempt_count: 1, failure_reason: null } }),
          baseContribution({ id: 4, status: 'superseded', is_current: false, active_memory_eligible: false, indexing_status: { state: 'retired', indexed_at: null, attempt_count: 1, failure_reason: null } })
        ]}
        lang="en"
        t={t}
      />
    );

    expect(screen.queryByText(t.indexingIndexed)).not.toBeInTheDocument();
  });
});

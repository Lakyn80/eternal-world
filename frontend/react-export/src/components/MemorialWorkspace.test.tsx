import { render, screen, waitFor } from '@testing-library/react';
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
  privacyScopeLabel
} from './MemorialWorkspace';
import type {
  BiographerQuestionRead,
  BiographerResumeRead,
  BiographyMemoryEntryRead,
  BiographyStatusRead,
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

describe('ContributionList - Task 65.8 retry indexing', () => {
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

  it('never offers retry to a contributor/viewer even for failed indexing', () => {
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
  });

  it('never offers retry for a contribution that is not currently failed', () => {
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
    expect(screen.getByText(t.indexingIndexed)).toBeInTheDocument();
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

/**
 * Task 65.11.4 — Passive AI Biographer loading vs active question generation.
 *
 * Opening / remounting / tabbing the panel must only resume persisted state.
 * Active next-question generation is a separate operation (manual prepare or
 * exactly-once post-index continuation).
 */
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { StrictMode, type ReactElement } from 'react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import {
  BiographerPanel,
  COPY,
  resetBiographerPanelTestGuards
} from './MemorialWorkspace';
import type { BiographerQuestionRead, BiographerResumeRead } from '../types/memorial';
import * as api from '../lib/memorialApi';
import { MemorialApiError } from '../lib/memorialApi';

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
    getBackgroundJob: vi.fn().mockRejectedValue(new actual.MemorialApiError(404, 'Background job not found'))
  };
});

const t = COPY.en;

function baseQuestion(overrides: Partial<BiographerQuestionRead> = {}): BiographerQuestionRead {
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
    active_question: null,
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

function renderPanel(ui?: ReactElement) {
  return render(
    ui ?? (
      <BiographerPanel
        email="task-65-11-4@example.com"
        lang="en"
        onNavigateToBiography={vi.fn()}
        onNavigateToReview={vi.fn()}
        profileId={7}
        t={t}
        token="tok"
      />
    )
  );
}

afterEach(() => {
  resetBiographerPanelTestGuards();
  vi.clearAllMocks();
});

describe('Task 65.11.4 — passive AI Biographer loading', () => {
  it('1. EXISTING QUESTION LOADS PASSIVELY', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: baseQuestion(), next_action: 'question_ready' })
    );

    renderPanel();

    expect(await screen.findByText('Where did you grow up?')).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
    expect(screen.queryByText(t.working)).not.toBeInTheDocument();
  });

  it('2. READY STATE LOADS PASSIVELY — Opening AI Biographer must never trigger active question generation', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, next_action: 'question_ready' })
    );
    vi.mocked(api.getNextBiographerQuestion).mockResolvedValue(baseQuestion());

    renderPanel();

    await waitFor(() => expect(api.getBiographerResume).toHaveBeenCalled());
    await waitFor(() => expect(screen.queryByText(t.working)).not.toBeInTheDocument());

    expect(await screen.findByText(t.biographerReadyForNextQuestion)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: t.biographerPrepareNextQuestion })).toBeInTheDocument();
    expect(
      api.getNextBiographerQuestion,
      'Opening AI Biographer must never trigger active question generation'
    ).not.toHaveBeenCalled();
  });

  it('3. TAB / REMOUNT ACTIVATION IS PASSIVE', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, next_action: 'question_ready' })
    );

    const { unmount } = renderPanel();
    await screen.findByText(t.biographerReadyForNextQuestion);
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();

    unmount();
    renderPanel();
    await screen.findByText(t.biographerReadyForNextQuestion);
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
  });

  it('4. PAGE REMOUNT WITH PERSISTED QUESTION STAYS PASSIVE', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: baseQuestion(), next_action: 'question_ready' })
    );

    const { unmount } = renderPanel();
    await screen.findByText('Where did you grow up?');
    unmount();
    renderPanel();
    expect(await screen.findByText('Where did you grow up?')).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
  });

  it('5. INDEXING SUCCESS TRIGGERS EXACTLY ONE GENERATION (polling + StrictMode)', async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    try {
      let indexingDone = false;
      vi.mocked(api.getBiographerResume).mockImplementation(async () => {
        if (!indexingDone) {
          return baseResume({
            active_question: null,
            candidate_id: 42,
            promotion_status: 'pending_index',
            next_action: 'candidate_pending_index'
          });
        }
        return baseResume({
          active_question: null,
          candidate_id: null,
          promotion_status: 'indexed',
          next_action: 'question_ready'
        });
      });
      vi.mocked(api.getNextBiographerQuestion).mockResolvedValue(
        baseQuestion({ id: 55, question_text: 'Post-index generated question' })
      );

      render(
        <StrictMode>
          <BiographerPanel
            email="task-65-11-4@example.com"
            lang="en"
            onNavigateToBiography={vi.fn()}
            onNavigateToReview={vi.fn()}
            profileId={7}
            t={t}
            token="tok"
          />
        </StrictMode>
      );

      expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();
      expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();

      indexingDone = true;
      await vi.advanceTimersByTimeAsync(3500);
      await waitFor(() => expect(api.getNextBiographerQuestion).toHaveBeenCalledTimes(1));
      expect(await screen.findByText('Post-index generated question')).toBeInTheDocument();

      // Repeated terminal polls must not start another generation.
      await vi.advanceTimersByTimeAsync(10000);
      expect(api.getNextBiographerQuestion).toHaveBeenCalledTimes(1);
    } finally {
      vi.useRealTimers();
    }
  });

  it('6. SLOW QUESTION GENERATION keeps the panel visible', async () => {
    let resolveNext!: (value: BiographerQuestionRead | null) => void;
    const pending = new Promise<BiographerQuestionRead | null>((resolve) => {
      resolveNext = resolve;
    });

    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, next_action: 'question_ready' })
    );
    vi.mocked(api.getNextBiographerQuestion).mockReturnValue(pending);

    const user = userEvent.setup();
    renderPanel();

    await screen.findByText(t.biographerReadyForNextQuestion);
    await user.click(screen.getByRole('button', { name: t.biographerPrepareNextQuestion }));

    expect(screen.getByText(t.biographer)).toBeInTheDocument();
    expect(screen.getByText(t.biographerIntro)).toBeInTheDocument();
    expect(await screen.findByText(t.biographerPreparingQuestion)).toBeInTheDocument();
    // Whole-panel spinner must not blank the panel during generation.
    expect(screen.queryByText(t.working)).not.toBeInTheDocument();

    resolveNext(baseQuestion({ id: 99, question_text: 'Late generated question' }));
    expect(await screen.findByText('Late generated question')).toBeInTheDocument();
  });

  it('7. GENERATION SUCCESS then subsequent passive load does not regenerate', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, next_action: 'question_ready' })
    );
    vi.mocked(api.getNextBiographerQuestion).mockResolvedValue(
      baseQuestion({ id: 77, question_text: 'Freshly prepared question' })
    );

    const user = userEvent.setup();
    const { unmount } = renderPanel();
    await screen.findByText(t.biographerReadyForNextQuestion);
    await user.click(screen.getByRole('button', { name: t.biographerPrepareNextQuestion }));
    expect(await screen.findByText('Freshly prepared question')).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).toHaveBeenCalledTimes(1);

    unmount();
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({
        active_question: baseQuestion({ id: 77, question_text: 'Freshly prepared question' }),
        next_action: 'question_ready'
      })
    );
    renderPanel();
    expect(await screen.findByText('Freshly prepared question')).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).toHaveBeenCalledTimes(1);
  });

  it('8. GENERATION FAILURE is recoverable and does not loop', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, next_action: 'question_ready' })
    );
    vi.mocked(api.getNextBiographerQuestion).mockRejectedValue(new MemorialApiError(503, 'unavailable'));

    const user = userEvent.setup();
    renderPanel();
    await screen.findByText(t.biographerReadyForNextQuestion);
    await user.click(screen.getByRole('button', { name: t.biographerPrepareNextQuestion }));

    expect(await screen.findByText(t.biographerGenerationFailed)).toBeInTheDocument();
    expect(screen.getByText(t.biographer)).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).toHaveBeenCalledTimes(1);

    await waitFor(() => expect(api.getNextBiographerQuestion).toHaveBeenCalledTimes(1));
  });

  it('9. STALE RESPONSE PROTECTION across profile change', async () => {
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
          active_question: baseQuestion({ id: 20, question_text: 'New question after switch?' })
        })
      );
    });

    const { rerender } = render(
      <BiographerPanel
        email="task-65-11-4@example.com"
        lang="en"
        onNavigateToBiography={vi.fn()}
        onNavigateToReview={vi.fn()}
        profileId={7}
        t={t}
        token="tok"
      />
    );

    rerender(
      <BiographerPanel
        email="task-65-11-4@example.com"
        lang="en"
        onNavigateToBiography={vi.fn()}
        onNavigateToReview={vi.fn()}
        profileId={8}
        t={t}
        token="tok"
      />
    );

    expect(await screen.findByText('New question after switch?')).toBeInTheDocument();
    resolveStale(baseResume({ active_question: baseQuestion({ id: 1, question_text: 'Stale old question' }) }));
    await waitFor(() => expect(screen.queryByText('Stale old question')).not.toBeInTheDocument());
    expect(screen.getByText('New question after switch?')).toBeInTheDocument();
  });

  it('10. CLARIFICATION AND REVIEW BLOCKS do not trigger next-question', async () => {
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({
        eligible: false,
        blocked_reason: 'active_clarification_exists',
        candidate_id: 5,
        next_action: 'clarification_pending',
        next_clarification_question: {
          clarification_id: 21,
          candidate_id: 5,
          question_key: 'place',
          question_text: 'Where did this usually happen?',
          language: 'en',
          status: 'pending',
          required: true,
          asked_at: '2026-01-01T00:00:00Z',
          answered_at: null,
          answered_by: null,
          answer_contribution_id: null
        }
      })
    );
    renderPanel();
    expect(await screen.findByText('Where did this usually happen?')).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();

    resetBiographerPanelTestGuards();
    vi.clearAllMocks();
    vi.mocked(api.getBiographerResume).mockResolvedValue(
      baseResume({ active_question: null, candidate_id: 42, next_action: 'candidate_ready_for_review' })
    );
    renderPanel();
    expect(await screen.findByText(t.biographerReadyForReview)).toBeInTheDocument();
    expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
  });

  it('11. INDEXING FAILURE never continues into generation', async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    try {
      vi.mocked(api.getBiographerResume)
        .mockResolvedValueOnce(
          baseResume({
            active_question: null,
            candidate_id: 42,
            next_action: 'candidate_pending_index'
          })
        )
        .mockResolvedValue(
          baseResume({
            active_question: null,
            candidate_id: 42,
            promotion_status: 'failed',
            next_action: 'candidate_indexing_failed'
          })
        );

      renderPanel();
      expect(await screen.findByText(t.biographerCandidatePendingIndex)).toBeInTheDocument();
      await vi.advanceTimersByTimeAsync(3500);
      expect(await screen.findByText(t.biographerCandidateIndexingFailed)).toBeInTheDocument();
      expect(api.getNextBiographerQuestion).not.toHaveBeenCalled();
    } finally {
      vi.useRealTimers();
    }
  });
});

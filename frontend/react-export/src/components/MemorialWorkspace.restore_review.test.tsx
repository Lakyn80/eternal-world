import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { ContributionList, COPY, Overview } from './MemorialWorkspace';
import type { ContributionRead, MemorialRead, MemoryCandidateEnrichmentRead } from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    restoreContribution: vi.fn(),
    getBiographyStatus: vi.fn(),
    listBiographyMemoryEntries: vi.fn(),
    updateMemorialMetadata: vi.fn(),
    deleteMemorial: vi.fn(),
  };
});

const t = COPY.en;

function baseMemorial(overrides: Partial<MemorialRead> = {}): MemorialRead {
  return {
    id: 7,
    owner_user_id: 1,
    name: 'Marfuša',
    birth_date: null,
    death_date: null,
    biography: 'A short biography.',
    personality: null,
    catchphrases: null,
    is_public: false,
    canonical_language: 'cs',
    canonical_language_source: 'owner_confirmed',
    canonical_language_locked_at: '2026-01-01T00:00:00Z',
    current_user_role: 'owner',
    created_at: '2026-01-01T00:00:00Z',
    updated_at: '2026-01-01T00:00:00Z',
    ...overrides,
  };
}

function baseContribution(overrides: Partial<ContributionRead> = {}): ContributionRead {
  return {
    id: 11,
    profile_id: 7,
    author_user_id: 2,
    author_email: 'contrib@example.com',
    title: 'Poslední den ve škole',
    memory_text: 'Memory text',
    source_language: 'cs',
    source_note: null,
    privacy_scope: 'all_family',
    status: 'archived',
    is_current: false,
    supersedes_contribution_id: null,
    reviewed_at: '2026-09-23T00:00:00Z',
    reviewed_by_user_id: 1,
    review_note: null,
    rejection_reason: null,
    active_memory_eligible: false,
    indexing_status: {
      state: 'not_applicable',
      indexed_at: null,
      attempt_count: 0,
      failure_reason: null,
      job_id: null,
    },
    created_at: '2026-09-23T00:00:00Z',
    updated_at: '2026-09-23T00:00:00Z',
    ...overrides,
  };
}

describe('ContributionList archive restore', () => {
  beforeEach(() => {
    vi.mocked(api.restoreContribution).mockReset();
  });

  it('shows Restore for authorized reviewers on archived contributions', () => {
    render(
      <ContributionList
        canRestore
        contributions={[baseContribution()]}
        lang="en"
        onRestored={vi.fn()}
        profileId={7}
        t={t}
        token="tok"
      />
    );
    expect(screen.getByText(t.statusArchived)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: t.restoreForReview })).toBeInTheDocument();
  });

  it('hides Restore for non-reviewers', () => {
    render(
      <ContributionList
        canRestore={false}
        contributions={[baseContribution()]}
        lang="en"
        t={t}
      />
    );
    expect(screen.queryByRole('button', { name: t.restoreForReview })).not.toBeInTheDocument();
  });

  it('restores successfully and keeps archived UI on API failure', async () => {
    const user = userEvent.setup();
    const onRestored = vi.fn();
    vi.mocked(api.restoreContribution).mockResolvedValueOnce(
      baseContribution({
        status: 'needs_review',
        reviewed_at: null,
        reviewed_by_user_id: null,
      })
    );

    const { rerender } = render(
      <ContributionList
        canRestore
        contributions={[baseContribution()]}
        lang="en"
        onRestored={onRestored}
        profileId={7}
        t={t}
        token="tok"
      />
    );

    await user.click(screen.getByRole('button', { name: t.restoreForReview }));
    await waitFor(() => expect(api.restoreContribution).toHaveBeenCalledWith('tok', 7, 11));
    expect(onRestored).toHaveBeenCalledTimes(1);

    vi.mocked(api.restoreContribution).mockRejectedValueOnce(new api.MemorialApiError(403, 'forbidden'));
    onRestored.mockClear();
    rerender(
      <ContributionList
        canRestore
        contributions={[baseContribution()]}
        lang="en"
        onRestored={onRestored}
        profileId={7}
        t={t}
        token="tok"
      />
    );
    await user.click(screen.getByRole('button', { name: t.restoreForReview }));
    await waitFor(() => expect(screen.getByText('forbidden')).toBeInTheDocument());
    expect(onRestored).not.toHaveBeenCalled();
    expect(screen.getByText(t.statusArchived)).toBeInTheDocument();
  });
});

describe('Overview memorial-scoped family review count', () => {
  beforeEach(() => {
    vi.mocked(api.listBiographyMemoryEntries).mockResolvedValue([]);
  });

  it('shows family contribution pending count even when AI candidate counts are zero', () => {
    const candidates: MemoryCandidateEnrichmentRead[] = [];
    render(
      <Overview
        biographerEligible={false}
        biographerQuestion={null}
        biographyStatus={null}
        candidates={candidates}
        canReviewHere
        canSubmitHere={false}
        familyPendingReviewCount={1}
        isOwner
        lang="en"
        memorial={baseMemorial()}
        onMemorialDeleted={vi.fn()}
        onMemorialUpdated={vi.fn()}
        onNavigate={vi.fn()}
        t={t}
        token="tok"
      />
    );
    expect(screen.getByText(`1 ${t.overviewReviewContributions}`)).toBeInTheDocument();
    expect(screen.getByText(`0 ${t.overviewReviewCandidates}`)).toBeInTheDocument();
  });
});

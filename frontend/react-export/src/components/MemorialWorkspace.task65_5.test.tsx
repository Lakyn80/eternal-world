/**
 * Task 65.5 - existing memorial editing, legacy biography binding, safe
 * indexing CTA, and safe deletion. Covers the regressions and new controls
 * reported for an owner who has already reached the plan's memorial limit.
 */
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { BiographyPanel, COPY, CreateMemorialForm, MemorialList, Overview, shortTextPreview } from './MemorialWorkspace';
import type { BillingLimitsRead, BiographyStatusRead, MemorialRead } from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    createMemorial: vi.fn(),
    getBiographyStatus: vi.fn(),
    updateBiography: vi.fn(),
    clearBiography: vi.fn(),
    updateMemorialMetadata: vi.fn(),
    deleteMemorial: vi.fn(),
    listBiographyMemoryEntries: vi.fn()
  };
});

const t = COPY.en;

beforeEach(() => {
  vi.mocked(api.listBiographyMemoryEntries).mockResolvedValue([]);
});

/** The plan-limit message is a two-line string (`\n`-joined); RTL's default
 * text normalizer collapses DOM whitespace to single spaces, so a literal
 * `\n` in the expected string never matches `getByText`'s normalized
 * comparison. Compare with the same whitespace normalization applied to
 * both sides instead of relying on the DOM-only normalizer. */
function findByNormalizedText(expected: string) {
  const normalize = (value: string) => value.replace(/\s+/g, ' ').trim();
  return screen.getByText((_, element) => normalize(element?.textContent ?? '') === normalize(expected));
}

function baseMemorial(overrides: Partial<MemorialRead> = {}): MemorialRead {
  return {
    id: 7,
    owner_user_id: 1,
    name: 'Lukas Krumpach',
    birth_date: null,
    death_date: null,
    biography: 'A short biography.',
    personality: null,
    catchphrases: null,
    is_public: false,
    current_user_role: 'owner',
    created_at: '2026-01-01T00:00:00Z',
    updated_at: '2026-01-01T00:00:00Z',
    ...overrides
  };
}

function baseBillingLimits(overrides: Partial<BillingLimitsRead> = {}): BillingLimitsRead {
  return {
    user_id: 1,
    plan_code: 'free',
    limits: {
      max_profiles: 1,
      max_memories: null,
      max_audio_minutes: null,
      max_videos_per_month: null,
      max_video_seconds: null,
      allow_watermark_removal: false,
      allow_unlimited_chat: false,
      allow_priority_support: false,
      allow_family_members: false,
      allow_shared_memories: false,
      allow_family_tree: false,
      max_family_members: null,
      max_video_quality: 'sd'
    },
    current_usage: {
      current_profiles: 1,
      current_memories: 0,
      current_audio_minutes: 0,
      current_videos_month: 0,
      current_family_members: 0
    },
    ...overrides
  };
}

function overviewProps(overrides: Partial<Parameters<typeof Overview>[0]> = {}) {
  return {
    memorial: baseMemorial(),
    t,
    lang: 'en' as const,
    isOwner: true,
    canSubmitHere: false,
    canReviewHere: false,
    biographyStatus: null,
    biographerEligible: false,
    biographerQuestion: null,
    candidates: [],
    onNavigate: vi.fn(),
    token: 'tok',
    onMemorialUpdated: vi.fn(),
    onMemorialDeleted: vi.fn(),
    ...overrides
  };
}

afterEach(() => {
  vi.clearAllMocks();
});

describe('shortTextPreview', () => {
  it('returns short text unchanged', () => {
    expect(shortTextPreview('Short text.')).toBe('Short text.');
  });

  it('truncates long text with an ellipsis rather than rendering it in full', () => {
    const long = 'A'.repeat(500);
    const preview = shortTextPreview(long);
    expect(preview.length).toBeLessThan(500);
    expect(preview.endsWith('…')).toBe(true);
  });

  it('handles null/undefined safely', () => {
    expect(shortTextPreview(null)).toBe('');
    expect(shortTextPreview(undefined)).toBe('');
  });
});

describe('Overview next-action (Task 65.4 regression fix)', () => {
  it('shows "Start biography indexing" (never "Everything is up to date") for a saved-but-draft biography', () => {
    const biographyStatus: BiographyStatusRead = {
      profile_id: 7,
      status: 'draft',
      content_hash: 'hash',
      indexed_at: null,
      attempt_count: 0,
      failure_reason: null,
      background_job_status: null,
      background_job_id: null
    };
    render(<Overview {...overviewProps({ biographyStatus })} />);

    expect(screen.getByText(t.overviewNextActionStartIndexing)).toBeInTheDocument();
    expect(screen.queryByText(t.overviewAllCaughtUp)).not.toBeInTheDocument();
  });

  it('never renders the full biography text in the Overview body', () => {
    const longBiography = 'B'.repeat(1000);
    render(<Overview {...overviewProps({ memorial: baseMemorial({ biography: longBiography }) })} />);

    expect(screen.queryByText(longBiography)).not.toBeInTheDocument();
  });
});

describe('Overview - edit memorial (owner only)', () => {
  it('owner can edit and save the memorial name without touching biography', async () => {
    const onMemorialUpdated = vi.fn();
    const updated = baseMemorial({ name: 'New Name' });
    vi.mocked(api.updateMemorialMetadata).mockResolvedValue(updated);
    const user = userEvent.setup();

    render(<Overview {...overviewProps({ onMemorialUpdated })} />);

    await user.click(screen.getByRole('button', { name: t.editMemorial }));
    const nameField = screen.getByLabelText(t.name);
    await user.clear(nameField);
    await user.type(nameField, 'New Name');
    await user.click(screen.getByRole('button', { name: t.saveChanges }));

    await waitFor(() => expect(api.updateMemorialMetadata).toHaveBeenCalledWith('tok', 7, { name: 'New Name' }));
    expect(onMemorialUpdated).toHaveBeenCalledWith(updated);
  });

  it('a non-owner never sees the edit-memorial control', () => {
    render(<Overview {...overviewProps({ isOwner: false })} />);
    expect(screen.queryByRole('button', { name: t.editMemorial })).not.toBeInTheDocument();
  });
});

describe('Overview - delete memorial (owner only, typed confirmation)', () => {
  it('a non-owner never sees the delete-memorial control', () => {
    render(<Overview {...overviewProps({ isOwner: false })} />);
    expect(screen.queryByRole('button', { name: t.deleteMemorial })).not.toBeInTheDocument();
  });

  it('the destructive button stays disabled until the memorial name is typed exactly', async () => {
    const user = userEvent.setup();
    render(<Overview {...overviewProps()} />);

    await user.click(screen.getByRole('button', { name: t.deleteMemorial }));
    const confirmButton = screen.getByRole('button', { name: t.deleteMemorialConfirmButton });
    expect(confirmButton).toBeDisabled();

    const confirmField = screen.getByLabelText(t.deleteMemorialConfirmLabel);
    await user.type(confirmField, 'wrong name');
    expect(confirmButton).toBeDisabled();

    await user.clear(confirmField);
    await user.type(confirmField, 'Lukas Krumpach');
    expect(confirmButton).not.toBeDisabled();
  });

  it('confirming deletion calls deleteMemorial exactly once and reports completion', async () => {
    vi.mocked(api.deleteMemorial).mockResolvedValue(undefined);
    const onMemorialDeleted = vi.fn();
    const user = userEvent.setup();

    render(<Overview {...overviewProps({ onMemorialDeleted })} />);
    await user.click(screen.getByRole('button', { name: t.deleteMemorial }));
    await user.type(screen.getByLabelText(t.deleteMemorialConfirmLabel), 'Lukas Krumpach');
    await user.click(screen.getByRole('button', { name: t.deleteMemorialConfirmButton }));

    await waitFor(() => expect(api.deleteMemorial).toHaveBeenCalledTimes(1));
    expect(api.deleteMemorial).toHaveBeenCalledWith('tok', 7);
    expect(onMemorialDeleted).toHaveBeenCalledTimes(1);
  });

  it('a partial-failure (409) response never claims success', async () => {
    vi.mocked(api.deleteMemorial).mockRejectedValue(new api.MemorialApiError(409, 'vectors not fully removed'));
    const onMemorialDeleted = vi.fn();
    const user = userEvent.setup();

    render(<Overview {...overviewProps({ onMemorialDeleted })} />);
    await user.click(screen.getByRole('button', { name: t.deleteMemorial }));
    await user.type(screen.getByLabelText(t.deleteMemorialConfirmLabel), 'Lukas Krumpach');
    await user.click(screen.getByRole('button', { name: t.deleteMemorialConfirmButton }));

    expect(await screen.findByText(t.deleteMemorialPartialFailure)).toBeInTheDocument();
    expect(onMemorialDeleted).not.toHaveBeenCalled();
  });
});

describe('CreateMemorialForm - plan limit gating', () => {
  it('shows the full create form when the plan allows another memorial', () => {
    render(
      <CreateMemorialForm
        billingLimits={baseBillingLimits({ current_usage: { current_profiles: 0, current_memories: 0, current_audio_minutes: 0, current_videos_month: 0, current_family_members: 0 } })}
        existingMemorials={[]}
        onCreated={vi.fn()}
        onOpenExisting={vi.fn()}
        t={t}
        token="tok"
      />
    );
    expect(screen.getByLabelText(t.name)).toBeInTheDocument();
  });

  it('replaces the create form with the localized limit message and an Open-existing action once the plan limit is reached', async () => {
    const onOpenExisting = vi.fn();
    const existing = baseMemorial();
    const user = userEvent.setup();

    render(
      <CreateMemorialForm
        billingLimits={baseBillingLimits()}
        existingMemorials={[existing]}
        onCreated={vi.fn()}
        onOpenExisting={onOpenExisting}
        t={t}
        token="tok"
      />
    );

    expect(screen.queryByLabelText(t.name)).not.toBeInTheDocument();
    expect(findByNormalizedText(t.planLimitReachedMessage)).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: t.openExistingMemorial }));
    expect(onOpenExisting).toHaveBeenCalledWith(existing.id);
  });

  it('never calls createMemorial while the form is in the blocked state', () => {
    render(
      <CreateMemorialForm
        billingLimits={baseBillingLimits()}
        existingMemorials={[baseMemorial()]}
        onCreated={vi.fn()}
        onOpenExisting={vi.fn()}
        t={t}
        token="tok"
      />
    );
    expect(api.createMemorial).not.toHaveBeenCalled();
  });

  it('normalizes a concurrent 403 profile_limit_exceeded response on submit into the same friendly message', async () => {
    vi.mocked(api.createMemorial).mockRejectedValue(
      new api.MemorialApiError(403, 'Memory profile limit exceeded for current plan')
    );
    const user = userEvent.setup();

    render(
      <CreateMemorialForm
        billingLimits={null}
        existingMemorials={[baseMemorial()]}
        onCreated={vi.fn()}
        onOpenExisting={vi.fn()}
        t={t}
        token="tok"
      />
    );

    await user.type(screen.getByLabelText(t.name), 'Second Memorial');
    await user.click(screen.getByRole('button', { name: t.createMemorial }));

    await waitFor(() => expect(findByNormalizedText(t.planLimitReachedMessage)).toBeInTheDocument());
    expect(screen.queryByText('Memory profile limit exceeded for current plan')).not.toBeInTheDocument();
  });
});

function baseBiographyStatus(overrides: Partial<BiographyStatusRead> = {}): BiographyStatusRead {
  return {
    profile_id: 7,
    status: 'draft',
    content_hash: 'hash',
    indexed_at: null,
    attempt_count: 0,
    failure_reason: null,
    background_job_status: null,
    background_job_id: null,
    ...overrides
  };
}

describe('BiographyPanel - save() does not contradict an already-indexed state', () => {
  it('re-saving unchanged, already-indexed text never shows "saved, not indexed yet"', async () => {
    // Reported live by the real account owner: saving the exact same
    // already-indexed biography text is a no-op on the backend
    // (`update_biography` short-circuits when the normalized text matches
    // what is already stored), so `status` stays 'indexed' - but the
    // frontend used to unconditionally show "Biography saved. It has not
    // been indexed yet." after every save click, directly contradicting
    // the still-correct "Indexed / up to date" badges shown above it.
    const indexedStatus = baseBiographyStatus({
      status: 'indexed',
      indexed_at: '2026-07-22T07:39:41Z'
    });
    vi.mocked(api.getBiographyStatus).mockResolvedValue(indexedStatus);
    vi.mocked(api.updateBiography).mockResolvedValue(indexedStatus);
    const user = userEvent.setup();

    render(<BiographyPanel initialBiography="Already indexed text." lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByText(t.biographyUpToDate);

    await user.click(screen.getByRole('button', { name: t.biographySave }));

    await waitFor(() => expect(api.updateBiography).toHaveBeenCalledTimes(1));
    expect(screen.queryByText(t.biographySavedNotIndexed)).not.toBeInTheDocument();
    expect(screen.getByText(t.biographyUpToDate)).toBeInTheDocument();
  });

  it('editing an already-indexed biography (now stale) shows a distinct "saved, needs re-indexing" notice', async () => {
    vi.mocked(api.getBiographyStatus).mockResolvedValue(
      baseBiographyStatus({ status: 'indexed', indexed_at: '2026-07-22T07:39:41Z' })
    );
    vi.mocked(api.updateBiography).mockResolvedValue(baseBiographyStatus({ status: 'stale' }));
    const user = userEvent.setup();

    render(<BiographyPanel initialBiography="Original text." lang="en" profileId={7} t={t} token="tok" />);
    const textarea = await screen.findByLabelText(t.biographyTextLabel);
    await user.type(textarea, ' Edited.');
    await user.click(screen.getByRole('button', { name: t.biographySave }));

    // Distinct from the never-indexed-yet notice (Task 65.4 bug report):
    // this correction WAS previously indexed, so "not indexed yet" would
    // wrongly read as "never indexed" - the new-version-saved wording makes
    // clear the save itself succeeded and is visible, while flagging that
    // re-indexing is still required to make it the active version.
    expect(await screen.findByText(t.biographySavedNowStale)).toBeInTheDocument();
    expect(screen.queryByText(t.biographySavedNotIndexed)).not.toBeInTheDocument();
  });
});

describe('BiographyPanel - clear biography (separate from deleting the memorial)', () => {
  it('shows the indexing explanation once the biography can be indexed', async () => {
    vi.mocked(api.getBiographyStatus).mockResolvedValue(baseBiographyStatus());
    render(<BiographyPanel initialBiography="Existing text." lang="en" profileId={7} t={t} token="tok" />);

    expect(await screen.findByText(t.biographyIndexingExplanation)).toBeInTheDocument();
  });

  it('offers Clear biography only when there is saved content, and requires confirmation', async () => {
    vi.mocked(api.getBiographyStatus).mockResolvedValue(baseBiographyStatus());
    vi.mocked(api.clearBiography).mockResolvedValue(
      baseBiographyStatus({ status: 'draft', content_hash: null })
    );
    const user = userEvent.setup();

    render(<BiographyPanel initialBiography="Existing text." lang="en" profileId={7} t={t} token="tok" />);
    await screen.findByLabelText(t.biographyTextLabel);

    const clearButton = screen.getByRole('button', { name: t.clearBiography });
    await user.click(clearButton);
    expect(api.clearBiography).not.toHaveBeenCalled();
    expect(screen.getByText(t.clearBiographyConfirmTitle)).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: t.clearBiographyConfirmYes }));
    await waitFor(() => expect(api.clearBiography).toHaveBeenCalledWith('tok', 7));
    expect(screen.getByLabelText(t.biographyTextLabel)).toHaveValue('');
  });

  it('does not offer Clear biography for an empty, never-saved biography', async () => {
    vi.mocked(api.getBiographyStatus).mockResolvedValue(baseBiographyStatus({ content_hash: null }));
    render(<BiographyPanel initialBiography="" lang="en" profileId={7} t={t} token="tok" />);
    await waitFor(() => expect(api.getBiographyStatus).toHaveBeenCalled());

    expect(screen.queryByRole('button', { name: t.clearBiography })).not.toBeInTheDocument();
  });
});

describe('MemorialList - single Open workspace button, truncated preview', () => {
  it('renders exactly one Open-workspace button per memorial and never the full biography text', () => {
    const longBiography = 'C'.repeat(600);
    render(
      <MemorialList
        lang="en"
        loading={false}
        memorials={[baseMemorial({ biography: longBiography }), baseMemorial({ id: 8, name: 'Second' })]}
        onOpen={vi.fn()}
        t={t}
      />
    );

    expect(screen.getAllByRole('button', { name: t.openWorkspace })).toHaveLength(2);
    expect(screen.queryByText(longBiography)).not.toBeInTheDocument();
  });
});

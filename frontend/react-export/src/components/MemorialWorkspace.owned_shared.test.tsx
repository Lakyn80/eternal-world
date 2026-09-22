import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it, vi } from 'vitest';
import { COPY, CreateMemorialForm, MemorialList } from './MemorialWorkspace';
import type { BillingLimitsRead, MemorialRead } from '../types/memorial';

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
      max_video_quality: 'sd',
    },
    current_usage: {
      current_profiles: 1,
      current_memories: 0,
      current_audio_minutes: 0,
      current_videos_month: 0,
      current_family_members: 0,
    },
    ...overrides,
  };
}

describe('MemorialList owned vs shared grouping', () => {
  it('places an owner-only memorial under My memorials', () => {
    render(
      <MemorialList
        lang="en"
        loading={false}
        memorials={[baseMemorial()]}
        onOpen={vi.fn()}
        t={t}
      />
    );
    expect(screen.getByRole('heading', { name: t.myMemorials })).toBeInTheDocument();
    expect(screen.queryByRole('heading', { name: t.sharedWithMe })).not.toBeInTheDocument();
    expect(screen.getByText('Marfuša')).toBeInTheDocument();
    expect(screen.getByText(t.roleOwner)).toBeInTheDocument();
  });

  it('places contributor memorials under Shared with me', () => {
    render(
      <MemorialList
        lang="en"
        loading={false}
        memorials={[baseMemorial({ id: 8, name: 'Lukas Krumpach', current_user_role: 'contributor' })]}
        onOpen={vi.fn()}
        t={t}
      />
    );
    expect(screen.getByRole('heading', { name: t.sharedWithMe })).toBeInTheDocument();
    expect(screen.queryByRole('heading', { name: t.myMemorials })).not.toBeInTheDocument();
    expect(screen.getByText('Lukas Krumpach')).toBeInTheDocument();
    expect(screen.getByText(t.roleContributor)).toBeInTheDocument();
  });

  it('shows each memorial in exactly one section when both owned and shared exist', () => {
    render(
      <MemorialList
        lang="en"
        loading={false}
        memorials={[
          baseMemorial({ id: 1, name: 'Marfuša', current_user_role: 'owner' }),
          baseMemorial({ id: 2, name: 'Lukas Krumpach', current_user_role: 'contributor' }),
        ]}
        onOpen={vi.fn()}
        t={t}
      />
    );
    expect(screen.getByRole('heading', { name: t.myMemorials })).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: t.sharedWithMe })).toBeInTheDocument();
    expect(screen.getAllByText('Marfuša')).toHaveLength(1);
    expect(screen.getAllByText('Lukas Krumpach')).toHaveLength(1);
    expect(screen.getAllByRole('button', { name: t.openWorkspace })).toHaveLength(2);
  });

  it('places trusted reviewer and viewer under Shared with me', () => {
    render(
      <MemorialList
        lang="en"
        loading={false}
        memorials={[
          baseMemorial({ id: 3, name: 'Review memorial', current_user_role: 'trusted_reviewer' }),
          baseMemorial({ id: 4, name: 'View memorial', current_user_role: 'viewer' }),
        ]}
        onOpen={vi.fn()}
        t={t}
      />
    );
    expect(screen.getByRole('heading', { name: t.sharedWithMe })).toBeInTheDocument();
    expect(screen.getByText(t.roleTrustedReviewer)).toBeInTheDocument();
    expect(screen.getByText(t.roleViewer)).toBeInTheDocument();
    expect(screen.getAllByRole('button', { name: t.openWorkspace })).toHaveLength(2);
  });

  it('opens a shared memorial through the existing Open workspace action', async () => {
    const onOpen = vi.fn();
    const user = userEvent.setup();
    render(
      <MemorialList
        lang="en"
        loading={false}
        memorials={[baseMemorial({ id: 42, name: 'Shared memorial', current_user_role: 'contributor' })]}
        onOpen={onOpen}
        t={t}
      />
    );
    await user.click(screen.getByRole('button', { name: t.openWorkspace }));
    expect(onOpen).toHaveBeenCalledWith(42);
  });

  it('renders localized section labels in EN / CS / RU', () => {
    for (const lang of ['en', 'cs', 'ru'] as const) {
      const copy = COPY[lang];
      const { unmount } = render(
        <MemorialList
          lang={lang}
          loading={false}
          memorials={[
            baseMemorial({ id: 1, name: 'Owned', current_user_role: 'owner' }),
            baseMemorial({ id: 2, name: 'Shared', current_user_role: 'viewer' }),
          ]}
          onOpen={vi.fn()}
          t={copy}
        />
      );
      expect(screen.getByRole('heading', { name: copy.myMemorials })).toBeInTheDocument();
      expect(screen.getByRole('heading', { name: copy.sharedWithMe })).toBeInTheDocument();
      unmount();
    }
  });
});

describe('CreateMemorialForm owned-only open-existing', () => {
  it('opens the owned memorial when plan limit is reached even if a shared memorial is listed first', async () => {
    const onOpenExisting = vi.fn();
    const user = userEvent.setup();
    render(
      <CreateMemorialForm
        billingLimits={baseBillingLimits()}
        existingMemorials={[
          baseMemorial({ id: 99, name: 'Shared first', current_user_role: 'contributor' }),
          baseMemorial({ id: 7, name: 'Marfuša', current_user_role: 'owner' }),
        ]}
        onCreated={vi.fn()}
        onOpenExisting={onOpenExisting}
        t={t}
        token="tok"
      />
    );
    await user.click(screen.getByRole('button', { name: t.openExistingMemorial }));
    expect(onOpenExisting).toHaveBeenCalledWith(7);
  });
});

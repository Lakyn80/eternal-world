import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { COPY, InvitationSection } from './MemorialWorkspace';
import type { InvitationCreateResponse, InvitationRead } from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    inviteParticipant: vi.fn(),
    listInvitations: vi.fn(),
    revokeInvitation: vi.fn()
  };
});

function inviteFixture(overrides: Partial<InvitationCreateResponse> = {}): InvitationCreateResponse {
  return {
    id: 1,
    profile_id: 7,
    email: 'invitee@example.com',
    role: 'contributor',
    expires_at: '2030-01-01T00:00:00Z',
    accepted_at: null,
    revoked_at: null,
    created_at: '2026-09-22T00:00:00Z',
    status: 'pending',
    ...overrides
  };
}

function pendingFixture(overrides: Partial<InvitationRead> = {}): InvitationRead {
  return {
    id: 11,
    profile_id: 7,
    email: 'pending@example.com',
    role: 'viewer',
    expires_at: '2030-06-01T00:00:00Z',
    accepted_at: null,
    revoked_at: null,
    created_at: '2026-09-22T00:00:00Z',
    status: 'pending',
    ...overrides
  };
}

describe('InvitationSection pending list + revoke', () => {
  const t = COPY.en;

  beforeEach(() => {
    vi.clearAllMocks();
    vi.mocked(api.listInvitations).mockResolvedValue([pendingFixture()]);
  });

  it('renders pending invitations and lets the owner revoke', async () => {
    const user = userEvent.setup();
    const onRevoked = vi.fn();
    vi.mocked(api.revokeInvitation).mockResolvedValue(
      pendingFixture({ status: 'revoked', revoked_at: '2026-09-23T00:00:00Z' })
    );

    render(
      <InvitationSection
        lang="en"
        onInvitationRevoked={onRevoked}
        onInvited={() => {}}
        profileId={7}
        t={t}
        token="tok"
      />
    );

    expect(await screen.findByText(t.pendingInvitations)).toBeInTheDocument();
    expect(screen.getByText('pending@example.com')).toBeInTheDocument();
    expect(screen.getByText(t.invitationStatusPending)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: t.revokeInvitation })).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: t.revokeInvitation }));
    await waitFor(() => expect(api.revokeInvitation).toHaveBeenCalledWith('tok', 7, 11));
    expect(onRevoked).toHaveBeenCalledTimes(1);
    await waitFor(() => expect(screen.queryByText('pending@example.com')).not.toBeInTheDocument());
  });

  it('hides Revoke when canRevoke is false', async () => {
    render(
      <InvitationSection
        canRevoke={false}
        lang="en"
        onInvited={() => {}}
        profileId={7}
        t={t}
        token="tok"
      />
    );
    expect(await screen.findByText('pending@example.com')).toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.revokeInvitation })).not.toBeInTheDocument();
  });

  it('keeps the invitation visible when revoke fails', async () => {
    const user = userEvent.setup();
    vi.mocked(api.revokeInvitation).mockRejectedValue(new api.MemorialApiError(403, 'forbidden'));

    render(
      <InvitationSection lang="en" onInvited={() => {}} profileId={7} t={t} token="tok" />
    );
    expect(await screen.findByText('pending@example.com')).toBeInTheDocument();
    await user.click(screen.getByRole('button', { name: t.revokeInvitation }));
    expect(await screen.findByText(t.revokeInvitationFailed)).toBeInTheDocument();
    expect(screen.getByText('pending@example.com')).toBeInTheDocument();
  });

  it('renders EN / CS / RU pending labels', async () => {
    for (const lang of ['en', 'cs', 'ru'] as const) {
      const copy = COPY[lang];
      const { unmount } = render(
        <InvitationSection lang={lang} onInvited={() => {}} profileId={7} t={copy} token="tok" />
      );
      expect(await screen.findByText(copy.pendingInvitations)).toBeInTheDocument();
      expect(screen.getByText(copy.invitationStatusPending)).toBeInTheDocument();
      unmount();
    }
  });

  it('refreshes pending list after a successful invite', async () => {
    const user = userEvent.setup();
    vi.mocked(api.inviteParticipant).mockResolvedValue(inviteFixture({ email: 'new@example.com' }));
    vi.mocked(api.listInvitations)
      .mockResolvedValueOnce([pendingFixture()])
      .mockResolvedValueOnce([
        pendingFixture(),
        pendingFixture({ id: 12, email: 'new@example.com' })
      ]);

    render(
      <InvitationSection lang="en" onInvited={() => {}} profileId={7} t={t} token="tok" />
    );
    await screen.findByText('pending@example.com');
    await user.type(screen.getByLabelText(t.email), 'new@example.com');
    await user.click(screen.getByRole('button', { name: t.inviteParticipant }));
    await waitFor(() => expect(api.listInvitations).toHaveBeenCalledTimes(2));
    expect(await screen.findByText('new@example.com')).toBeInTheDocument();
  });
});

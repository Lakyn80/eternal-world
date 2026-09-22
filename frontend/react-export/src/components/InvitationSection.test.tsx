import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { COPY, InvitationSection } from './MemorialWorkspace';
import type { InvitationCreateResponse } from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    inviteParticipant: vi.fn()
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
    ...overrides
  };
}

describe('InvitationSection development invite link', () => {
  const t = COPY.en;

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders a clickable absolute accept_url from the API and copies it', async () => {
    const user = userEvent.setup();
    const acceptUrl = 'http://localhost:8017/invitations/accept?token=dev-token-value-abcdefghijklmnopqrst';
    vi.mocked(api.inviteParticipant).mockResolvedValue(
      inviteFixture({
        token: 'dev-token-value-abcdefghijklmnopqrst',
        accept_url: acceptUrl,
        email_sent: false
      })
    );
    const writeText = vi.fn().mockResolvedValue(undefined);
    Object.defineProperty(navigator, 'clipboard', {
      configurable: true,
      value: { writeText }
    });

    render(<InvitationSection token="access" profileId={7} t={t} onInvited={() => {}} />);

    await user.type(screen.getByLabelText(t.email), 'invitee@example.com');
    await user.click(screen.getByRole('button', { name: t.inviteParticipant }));

    const link = await screen.findByRole('link', { name: acceptUrl });
    expect(link).toHaveAttribute('href', acceptUrl);
    expect(link).toHaveAttribute('target', '_blank');
    expect(screen.getByText(t.devToken)).toBeInTheDocument();
    expect(screen.getByText(t.tokenNote)).toBeInTheDocument();
    // Raw secret must not appear as a standalone line outside the URL.
    expect(screen.queryByText(/^dev-token-value-abcdefghijklmnopqrst$/)).not.toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: t.copyInviteLink }));
    await waitFor(() => expect(writeText).toHaveBeenCalledWith(acceptUrl));
  });

  it('does not render a development link for production-style emailed invitations', async () => {
    const user = userEvent.setup();
    vi.mocked(api.inviteParticipant).mockResolvedValue(
      inviteFixture({
        token: undefined,
        accept_url: null,
        email_sent: true
      })
    );

    render(<InvitationSection token="access" profileId={7} t={t} onInvited={() => {}} />);

    await user.type(screen.getByLabelText(t.email), 'invitee@example.com');
    await user.click(screen.getByRole('button', { name: t.inviteParticipant }));

    await screen.findByText(t.inviteSent.replace('{email}', 'invitee@example.com'));
    expect(screen.queryByRole('link')).not.toBeInTheDocument();
    expect(screen.queryByText(t.devToken)).not.toBeInTheDocument();
    expect(screen.queryByRole('button', { name: t.copyInviteLink })).not.toBeInTheDocument();
  });
});

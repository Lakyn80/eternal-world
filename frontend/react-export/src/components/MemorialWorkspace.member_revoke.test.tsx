import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { COPY, MembersSection } from './MemorialWorkspace';
import type { MembershipRead } from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    revokeMember: vi.fn(),
  };
});

const t = COPY.en;

const members: MembershipRead[] = [
  {
    id: 1,
    profile_id: 7,
    user_id: 10,
    email: 'owner@example.com',
    full_name: 'Owner',
    role: 'owner',
    status: 'active',
    created_at: '2026-01-01T00:00:00Z',
    updated_at: '2026-01-01T00:00:00Z',
  },
  {
    id: 2,
    profile_id: 7,
    user_id: 20,
    email: 'contrib@example.com',
    full_name: 'Contributor',
    role: 'contributor',
    status: 'active',
    created_at: '2026-01-01T00:00:00Z',
    updated_at: '2026-01-01T00:00:00Z',
  },
];

describe('MembersSection soft-revoke', () => {
  beforeEach(() => {
    vi.mocked(api.revokeMember).mockReset();
  });

  it('owner sees Remove on non-owner members but not on the owner row', () => {
    render(<MembersSection canManageMembers members={members} t={t} />);
    const removeButtons = screen.getAllByRole('button', { name: t.removeMember });
    expect(removeButtons).toHaveLength(1);
    expect(screen.getByText('owner@example.com').closest('article')).not.toHaveTextContent(t.removeMember);
    expect(screen.getByText('contrib@example.com').closest('article')).toHaveTextContent(t.removeMember);
  });

  it('contributor/viewer does not see Remove controls', () => {
    render(<MembersSection canManageMembers={false} members={members} t={t} />);
    expect(screen.queryByRole('button', { name: t.removeMember })).not.toBeInTheDocument();
  });

  it('requires confirmation before calling revokeMember and updates after success', async () => {
    const user = userEvent.setup();
    const onMemberRevoked = vi.fn();
    vi.mocked(api.revokeMember).mockResolvedValue({
      ...members[1],
      status: 'revoked',
    });

    const { rerender } = render(
      <MembersSection
        canManageMembers
        members={members}
        onMemberRevoked={onMemberRevoked}
        profileId={7}
        t={t}
        token="tok"
      />
    );

    await user.click(screen.getByRole('button', { name: t.removeMember }));
    expect(api.revokeMember).not.toHaveBeenCalled();
    expect(screen.getByText(t.removeMemberConfirmTitle)).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: t.removeMemberConfirmYes }));
    await waitFor(() => expect(api.revokeMember).toHaveBeenCalledTimes(1));
    expect(api.revokeMember).toHaveBeenCalledWith('tok', 7, 20);
    await waitFor(() => expect(onMemberRevoked).toHaveBeenCalledTimes(1));

    rerender(
      <MembersSection
        canManageMembers
        members={[members[0]]}
        onMemberRevoked={onMemberRevoked}
        profileId={7}
        t={t}
        token="tok"
      />
    );
    expect(screen.queryByText('contrib@example.com')).not.toBeInTheDocument();
    expect(screen.getByText('owner@example.com')).toBeInTheDocument();
  });

  it('API failure does not remove the member from the UI', async () => {
    const user = userEvent.setup();
    const onMemberRevoked = vi.fn();
    vi.mocked(api.revokeMember).mockRejectedValue(new api.MemorialApiError(403, 'forbidden'));

    render(
      <MembersSection
        canManageMembers
        members={members}
        onMemberRevoked={onMemberRevoked}
        profileId={7}
        t={t}
        token="tok"
      />
    );

    await user.click(screen.getByRole('button', { name: t.removeMember }));
    await user.click(screen.getByRole('button', { name: t.removeMemberConfirmYes }));

    expect(await screen.findByText(t.removeMemberFailed)).toBeInTheDocument();
    expect(onMemberRevoked).not.toHaveBeenCalled();
    expect(screen.getByText('contrib@example.com')).toBeInTheDocument();
  });
});

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  PENDING_INVITATION_STORAGE_KEY,
  captureOrRestoreInvitationToken,
  clearPendingInvitationToken,
  readPendingInvitationToken,
  writePendingInvitationToken
} from './pendingInvitation';

describe('pendingInvitation sessionStorage handoff', () => {
  beforeEach(() => {
    sessionStorage.clear();
    window.history.replaceState({}, '', '/invitations/accept');
  });

  afterEach(() => {
    vi.restoreAllMocks();
    sessionStorage.clear();
    window.history.replaceState({}, '', '/');
  });

  it('writes and reads a token payload', () => {
    writePendingInvitationToken('  abc.token  ');
    expect(readPendingInvitationToken()).toBe('abc.token');
    expect(JSON.parse(sessionStorage.getItem(PENDING_INVITATION_STORAGE_KEY) || '{}')).toEqual({
      token: 'abc.token'
    });
  });

  it('clears the pending invitation', () => {
    writePendingInvitationToken('tok');
    clearPendingInvitationToken();
    expect(readPendingInvitationToken()).toBeNull();
    expect(sessionStorage.getItem(PENDING_INVITATION_STORAGE_KEY)).toBeNull();
  });

  it('captures token from the URL, persists it, and strips the query param', () => {
    window.history.replaceState({}, '', '/invitations/accept?token=SECRET_TOKEN&x=1');
    const token = captureOrRestoreInvitationToken();
    expect(token).toBe('SECRET_TOKEN');
    expect(readPendingInvitationToken()).toBe('SECRET_TOKEN');
    expect(window.location.pathname).toBe('/invitations/accept');
    expect(window.location.search).toBe('?x=1');
  });

  it('restores the token from sessionStorage when the URL has no token', () => {
    writePendingInvitationToken('restored-token');
    window.history.replaceState({}, '', '/app/memorials/12');
    expect(captureOrRestoreInvitationToken()).toBe('restored-token');
  });

  it('ignores corrupt storage payloads', () => {
    sessionStorage.setItem(PENDING_INVITATION_STORAGE_KEY, '{not-json');
    expect(readPendingInvitationToken()).toBeNull();
    sessionStorage.setItem(PENDING_INVITATION_STORAGE_KEY, JSON.stringify({ token: 42 }));
    expect(readPendingInvitationToken()).toBeNull();
  });

  it('survives sessionStorage write failures (private mode)', () => {
    const setItem = vi.spyOn(Storage.prototype, 'setItem').mockImplementation(() => {
      throw new Error('quota');
    });
    expect(() => writePendingInvitationToken('tok')).not.toThrow();
    setItem.mockRestore();
  });
});

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  PENDING_INVITATION_STORAGE_KEY,
  captureOrRestoreInvitationToken,
  clearPendingInvitationToken,
  normalizeInvitationToken,
  readPendingInvitationToken,
  toAbsoluteAppUrl,
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

  it('normalizes raw tokens, query fragments, and full accept URLs', () => {
    expect(normalizeInvitationToken('  abcdefghijklmnopqrstuvwxyz12  ')).toBe('abcdefghijklmnopqrstuvwxyz12');
    expect(
      normalizeInvitationToken('http://localhost:8017/invitations/accept?token=abcdefghijklmnopqrstuvwxyz12')
    ).toBe('abcdefghijklmnopqrstuvwxyz12');
    expect(normalizeInvitationToken('/invitations/accept?token=abcdefghijklmnopqrstuvwxyz12&x=1')).toBe(
      'abcdefghijklmnopqrstuvwxyz12'
    );
    expect(normalizeInvitationToken('short')).toBeNull();
    expect(normalizeInvitationToken('http://localhost:8017/invitations/accept')).toBeNull();
  });

  it('writes and reads a token payload', () => {
    writePendingInvitationToken('  abcdefghijklmnopqrstuvwxyz12  ');
    expect(readPendingInvitationToken()).toBe('abcdefghijklmnopqrstuvwxyz12');
    expect(JSON.parse(sessionStorage.getItem(PENDING_INVITATION_STORAGE_KEY) || '{}')).toEqual({
      token: 'abcdefghijklmnopqrstuvwxyz12'
    });
  });

  it('clears the pending invitation', () => {
    writePendingInvitationToken('abcdefghijklmnopqrstuvwxyz12');
    clearPendingInvitationToken();
    expect(readPendingInvitationToken()).toBeNull();
    expect(sessionStorage.getItem(PENDING_INVITATION_STORAGE_KEY)).toBeNull();
  });

  it('captures token from the URL, persists it, and strips the query param', () => {
    window.history.replaceState({}, '', '/invitations/accept?token=SECRET_TOKEN_VALUE_12345&x=1');
    const token = captureOrRestoreInvitationToken();
    expect(token).toBe('SECRET_TOKEN_VALUE_12345');
    expect(readPendingInvitationToken()).toBe('SECRET_TOKEN_VALUE_12345');
    expect(window.location.pathname).toBe('/invitations/accept');
    expect(window.location.search).toBe('?x=1');
  });

  it('restores the token from sessionStorage when the URL has no token', () => {
    writePendingInvitationToken('restored-token-value-12345');
    window.history.replaceState({}, '', '/app/memorials/12');
    expect(captureOrRestoreInvitationToken()).toBe('restored-token-value-12345');
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
    expect(() => writePendingInvitationToken('abcdefghijklmnopqrstuvwxyz12')).not.toThrow();
    setItem.mockRestore();
  });

  it('resolves relative accept paths to absolute app URLs', () => {
    expect(toAbsoluteAppUrl('/invitations/accept?token=abc', 'http://localhost:8017')).toBe(
      'http://localhost:8017/invitations/accept?token=abc'
    );
    expect(toAbsoluteAppUrl('http://example.test/invitations/accept?token=abc')).toBe(
      'http://example.test/invitations/accept?token=abc'
    );
  });
});

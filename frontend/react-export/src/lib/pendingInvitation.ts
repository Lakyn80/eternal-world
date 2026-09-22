/**
 * Tab-scoped handoff for memorial invitation tokens.
 *
 * Accept links strip `?token=` from the address bar (anti-leak). Without a
 * durable handoff, a refresh before Accept loses the token. sessionStorage
 * keeps the raw token for this tab until Accept succeeds.
 *
 * Necessary for completing the invite flow — not gated on functional cookie
 * consent (unlike chat/biographer drafts).
 */

export const PENDING_INVITATION_STORAGE_KEY = 'eternal_world:pending_invitation';

export type PendingInvitation = {
  token: string;
};

function isNonEmptyToken(value: unknown): value is string {
  return typeof value === 'string' && value.trim().length > 0;
}

export function readPendingInvitationToken(): string | null {
  try {
    const raw = window.sessionStorage.getItem(PENDING_INVITATION_STORAGE_KEY);
    if (!raw) return null;
    const parsed: unknown = JSON.parse(raw);
    if (!parsed || typeof parsed !== 'object') return null;
    const token = (parsed as { token?: unknown }).token;
    return isNonEmptyToken(token) ? token.trim() : null;
  } catch {
    return null;
  }
}

export function writePendingInvitationToken(token: string): void {
  const trimmed = token.trim();
  if (!trimmed) return;
  try {
    const payload: PendingInvitation = { token: trimmed };
    window.sessionStorage.setItem(PENDING_INVITATION_STORAGE_KEY, JSON.stringify(payload));
  } catch {
    // Private browsing / quota — caller still holds the token in React state.
  }
}

export function clearPendingInvitationToken(): void {
  try {
    window.sessionStorage.removeItem(PENDING_INVITATION_STORAGE_KEY);
  } catch {
    // Storage may be unavailable.
  }
}

/** Capture from `?token=`, persist, strip from the URL; else restore from storage. */
export function captureOrRestoreInvitationToken(currentHref = window.location.href): string | null {
  const url = new URL(currentHref);
  const fromUrl = url.searchParams.get('token');
  if (isNonEmptyToken(fromUrl)) {
    const token = fromUrl.trim();
    writePendingInvitationToken(token);
    url.searchParams.delete('token');
    const next = `${url.pathname}${url.search}${url.hash}`;
    window.history.replaceState({}, document.title, next);
    return token;
  }
  return readPendingInvitationToken();
}

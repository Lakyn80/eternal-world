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

/**
 * Accept URL query values, pasted full links, or raw tokens all normalize to
 * the bare invitation secret. Never hash a full URL by mistake.
 */
export function normalizeInvitationToken(raw: string | null | undefined): string | null {
  if (!isNonEmptyToken(raw)) return null;
  let value = raw.trim();

  // Full or relative accept URL / query fragment pasted into the field or storage.
  if (/token=/i.test(value)) {
    try {
      const asUrl = new URL(value, 'http://local.invalid');
      const fromQuery = asUrl.searchParams.get('token');
      if (isNonEmptyToken(fromQuery)) {
        value = fromQuery.trim();
      }
    } catch {
      const match = /(?:^|[?&#])token=([^&?#]+)/i.exec(value);
      if (match?.[1]) {
        try {
          value = decodeURIComponent(match[1]).trim();
        } catch {
          value = match[1].trim();
        }
      }
    }
  }

  // Guard against accidentally persisting an entire URL as the token.
  if (/^https?:\/\//i.test(value) || value.includes('/')) {
    return null;
  }

  return value.length >= 20 ? value : null;
}

export function readPendingInvitationToken(): string | null {
  try {
    const raw = window.sessionStorage.getItem(PENDING_INVITATION_STORAGE_KEY);
    if (!raw) return null;
    const parsed: unknown = JSON.parse(raw);
    if (!parsed || typeof parsed !== 'object') return null;
    return normalizeInvitationToken((parsed as { token?: unknown }).token as string);
  } catch {
    return null;
  }
}

export function writePendingInvitationToken(token: string): void {
  const normalized = normalizeInvitationToken(token);
  if (!normalized) return;
  try {
    const payload: PendingInvitation = { token: normalized };
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

/** Turn a relative accept path into an absolute URL for clipboard/open. */
export function toAbsoluteAppUrl(pathOrUrl: string, origin = window.location.origin): string {
  const trimmed = pathOrUrl.trim();
  if (!trimmed) return trimmed;
  if (/^https?:\/\//i.test(trimmed)) return trimmed;
  const path = trimmed.startsWith('/') ? trimmed : `/${trimmed}`;
  return `${origin.replace(/\/$/, '')}${path}`;
}

function stripTokenFromAddressBar(currentHref: string): void {
  const url = new URL(currentHref);
  if (!url.searchParams.has('token')) return;
  url.searchParams.delete('token');
  const next = `${url.pathname}${url.search}${url.hash}`;
  window.history.replaceState({}, document.title, next);
}

/**
 * Capture from `?token=` (or a pasted accept URL), persist, strip from the
 * address bar; else restore from sessionStorage.
 */
export function captureOrRestoreInvitationToken(currentHref = window.location.href): string | null {
  const url = new URL(currentHref);
  const fromUrl = normalizeInvitationToken(url.searchParams.get('token'));
  if (fromUrl) {
    writePendingInvitationToken(fromUrl);
    stripTokenFromAddressBar(currentHref);
    return fromUrl;
  }
  return readPendingInvitationToken();
}

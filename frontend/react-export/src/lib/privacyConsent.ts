import { LANG_PREFERENCE_STORAGE_KEY } from './langPreference';
import { disableOptionalPwaStorage } from './pwa';

export const COOKIE_CONSENT_STORAGE_KEY = 'eternal-world.cookie-consent';
export const COOKIE_CONSENT_VERSION = 1 as const;
export const COOKIE_CONSENT_CHANGED_EVENT = 'eternal-world:cookie-consent-changed';
export const OPEN_COOKIE_SETTINGS_EVENT = 'eternal-world:open-cookie-settings';

const CHAT_DRAFT_STORAGE_PREFIX = 'eternal_world:chat_draft:';
const BIOGRAPHER_DRAFT_STORAGE_PREFIX = 'eternal_world:biographer_draft:';
const ACCEPTED_CONSENT_LIFETIME_DAYS = 365;
const REJECTED_CONSENT_LIFETIME_DAYS = 183;

export type CookieConsentRecord = {
  version: typeof COOKIE_CONSENT_VERSION;
  decidedAt: string;
  expiresAt: string;
  categories: {
    necessary: true;
    functional: boolean;
  };
};

function isValidDate(value: unknown): value is string {
  return typeof value === 'string' && Number.isFinite(Date.parse(value));
}

function isCookieConsentRecord(value: unknown): value is CookieConsentRecord {
  if (!value || typeof value !== 'object') return false;
  const record = value as Partial<CookieConsentRecord>;
  return (
    record.version === COOKIE_CONSENT_VERSION &&
    isValidDate(record.decidedAt) &&
    isValidDate(record.expiresAt) &&
    record.categories?.necessary === true &&
    typeof record.categories.functional === 'boolean'
  );
}

function removeStoredConsent(): void {
  try {
    localStorage.removeItem(COOKIE_CONSENT_STORAGE_KEY);
  } catch {
    // Storage may be unavailable. The safe fallback is no optional storage.
  }
}

export function readCookieConsent(now = new Date()): CookieConsentRecord | null {
  try {
    const raw = localStorage.getItem(COOKIE_CONSENT_STORAGE_KEY);
    if (!raw) return null;
    const parsed: unknown = JSON.parse(raw);
    if (!isCookieConsentRecord(parsed) || Date.parse(parsed.expiresAt) <= now.getTime()) {
      removeStoredConsent();
      return null;
    }
    return parsed;
  } catch {
    removeStoredConsent();
    return null;
  }
}

export function saveCookieConsent(functional: boolean, now = new Date()): CookieConsentRecord {
  const lifetimeDays = functional ? ACCEPTED_CONSENT_LIFETIME_DAYS : REJECTED_CONSENT_LIFETIME_DAYS;
  const expiresAt = new Date(now.getTime() + lifetimeDays * 24 * 60 * 60 * 1000);
  const record: CookieConsentRecord = {
    version: COOKIE_CONSENT_VERSION,
    decidedAt: now.toISOString(),
    expiresAt: expiresAt.toISOString(),
    categories: {
      necessary: true,
      functional
    }
  };
  try {
    localStorage.setItem(COOKIE_CONSENT_STORAGE_KEY, JSON.stringify(record));
  } catch {
    // The UI still applies the choice for this page view via its React state.
  }
  window.dispatchEvent(new CustomEvent(COOKIE_CONSENT_CHANGED_EVENT, { detail: record }));
  return record;
}

function removeSessionDrafts(): void {
  try {
    const keys = Array.from({ length: sessionStorage.length }, (_, index) => sessionStorage.key(index));
    for (const key of keys) {
      if (key?.startsWith(CHAT_DRAFT_STORAGE_PREFIX) || key?.startsWith(BIOGRAPHER_DRAFT_STORAGE_PREFIX)) {
        sessionStorage.removeItem(key);
      }
    }
  } catch {
    // Storage may be unavailable; there is nothing else to revoke client-side.
  }
}

export async function clearFunctionalBrowserStorage(): Promise<void> {
  try {
    localStorage.removeItem(LANG_PREFERENCE_STORAGE_KEY);
  } catch {
    // Storage may be unavailable.
  }
  removeSessionDrafts();
  await disableOptionalPwaStorage();
}

export async function applyCookieConsent(functional: boolean): Promise<CookieConsentRecord> {
  const record = saveCookieConsent(functional);
  if (!functional) await clearFunctionalBrowserStorage();
  return record;
}

export function openCookieSettings(): void {
  window.dispatchEvent(new CustomEvent(OPEN_COOKIE_SETTINGS_EVENT));
}

export function isFunctionalStorageAllowed(
  lang: 'en' | 'cs' | 'ru',
  consent: CookieConsentRecord | null
): boolean {
  return lang !== 'cs' || consent?.categories.functional === true;
}

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { LANG_PREFERENCE_STORAGE_KEY } from './langPreference';
import {
  applyCookieConsent,
  clearFunctionalBrowserStorage,
  COOKIE_CONSENT_CHANGED_EVENT,
  COOKIE_CONSENT_STORAGE_KEY,
  COOKIE_CONSENT_VERSION,
  isFunctionalStorageAllowed,
  openCookieSettings,
  OPEN_COOKIE_SETTINGS_EVENT,
  readCookieConsent,
  saveCookieConsent
} from './privacyConsent';

describe('Czech privacy consent storage', () => {
  beforeEach(() => {
    localStorage.clear();
    sessionStorage.clear();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('starts with no consent and therefore no Czech functional permission', () => {
    expect(readCookieConsent()).toBeNull();
    expect(isFunctionalStorageAllowed('cs', null)).toBe(false);
  });

  it('stores version, timestamp, categories and a 12 month acceptance lifetime', () => {
    const now = new Date('2026-09-22T08:00:00.000Z');
    const record = saveCookieConsent(true, now);

    expect(record).toEqual({
      version: COOKIE_CONSENT_VERSION,
      decidedAt: now.toISOString(),
      expiresAt: '2027-09-22T08:00:00.000Z',
      categories: { necessary: true, functional: true }
    });
    expect(readCookieConsent(now)).toEqual(record);
  });

  it('stores rejection for 183 days with optional storage disabled', () => {
    const now = new Date('2026-09-22T08:00:00.000Z');
    const record = saveCookieConsent(false, now);

    expect(record.expiresAt).toBe('2027-03-24T08:00:00.000Z');
    expect(record.categories).toEqual({ necessary: true, functional: false });
  });

  it('rejects records from an obsolete consent version', () => {
    localStorage.setItem(COOKIE_CONSENT_STORAGE_KEY, JSON.stringify({
      version: 0,
      decidedAt: '2026-09-22T08:00:00.000Z',
      expiresAt: '2027-09-22T08:00:00.000Z',
      categories: { necessary: true, functional: true }
    }));

    expect(readCookieConsent()).toBeNull();
    expect(localStorage.getItem(COOKIE_CONSENT_STORAGE_KEY)).toBeNull();
  });

  it('expires a consent record and requests a new choice', () => {
    saveCookieConsent(true, new Date('2025-09-20T08:00:00.000Z'));

    expect(readCookieConsent(new Date('2026-09-22T08:00:00.000Z'))).toBeNull();
  });

  it('does not change existing English or Russian storage behavior', () => {
    expect(isFunctionalStorageAllowed('en', null)).toBe(true);
    expect(isFunctionalStorageAllowed('ru', null)).toBe(true);
  });

  it('removes only optional browser data when consent is revoked', async () => {
    localStorage.setItem(LANG_PREFERENCE_STORAGE_KEY, 'cs');
    localStorage.setItem('unrelated', 'keep');
    sessionStorage.setItem('eternal_world:chat_draft:user:1', 'draft');
    sessionStorage.setItem('eternal_world:biographer_draft:user:1:2', 'answer');
    sessionStorage.setItem('unrelated-session', 'keep');

    await clearFunctionalBrowserStorage();

    expect(localStorage.getItem(LANG_PREFERENCE_STORAGE_KEY)).toBeNull();
    expect(localStorage.getItem('unrelated')).toBe('keep');
    expect(sessionStorage.getItem('eternal_world:chat_draft:user:1')).toBeNull();
    expect(sessionStorage.getItem('eternal_world:biographer_draft:user:1:2')).toBeNull();
    expect(sessionStorage.getItem('unrelated-session')).toBe('keep');
  });

  it('keeps the necessary consent record while applying rejection', async () => {
    await applyCookieConsent(false);

    expect(readCookieConsent()?.categories).toEqual({ necessary: true, functional: false });
  });

  it('announces consent changes and settings requests', () => {
    const consentListener = vi.fn();
    const settingsListener = vi.fn();
    window.addEventListener(COOKIE_CONSENT_CHANGED_EVENT, consentListener);
    window.addEventListener(OPEN_COOKIE_SETTINGS_EVENT, settingsListener);

    saveCookieConsent(true);
    openCookieSettings();

    expect(consentListener).toHaveBeenCalledOnce();
    expect(settingsListener).toHaveBeenCalledOnce();
    window.removeEventListener(COOKIE_CONSENT_CHANGED_EVENT, consentListener);
    window.removeEventListener(OPEN_COOKIE_SETTINGS_EVENT, settingsListener);
  });
});

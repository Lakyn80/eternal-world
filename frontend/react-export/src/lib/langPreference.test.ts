import { afterEach, describe, expect, it } from 'vitest';
import {
  DEFAULT_LANG,
  LANG_PREFERENCE_STORAGE_KEY,
  hasExplicitStoredLang,
  isLang,
  readStoredLang,
  resolveLangAfterSessionRestore,
  writeStoredLang
} from './langPreference';

afterEach(() => {
  localStorage.removeItem(LANG_PREFERENCE_STORAGE_KEY);
});

describe('langPreference', () => {
  it('accepts only en/cs/ru', () => {
    expect(isLang('cs')).toBe(true);
    expect(isLang('en')).toBe(true);
    expect(isLang('ru')).toBe(true);
    expect(isLang('de')).toBe(false);
    expect(isLang('')).toBe(false);
    expect(isLang(null)).toBe(false);
  });

  it('defaults when nothing is stored', () => {
    expect(readStoredLang()).toBe(DEFAULT_LANG);
    expect(hasExplicitStoredLang()).toBe(false);
  });

  it('round-trips an explicit Czech choice across read/write', () => {
    writeStoredLang('cs');
    expect(localStorage.getItem(LANG_PREFERENCE_STORAGE_KEY)).toBe('cs');
    expect(readStoredLang()).toBe('cs');
    expect(hasExplicitStoredLang()).toBe(true);
  });

  it('ignores corrupt stored values', () => {
    localStorage.setItem(LANG_PREFERENCE_STORAGE_KEY, 'not-a-lang');
    expect(readStoredLang()).toBe(DEFAULT_LANG);
    expect(hasExplicitStoredLang()).toBe(false);
  });

  it('session restore keeps local RU over account default EN', () => {
    writeStoredLang('ru');
    expect(resolveLangAfterSessionRestore('en')).toEqual({
      lang: 'ru',
      source: 'local',
      syncAccount: true
    });
  });

  it('session restore uses account language only when local is empty', () => {
    expect(resolveLangAfterSessionRestore('cs')).toEqual({
      lang: 'cs',
      source: 'account',
      syncAccount: false
    });
  });

  it('session restore does not sync when local and account already match', () => {
    writeStoredLang('ru');
    expect(resolveLangAfterSessionRestore('ru')).toEqual({
      lang: 'ru',
      source: 'local',
      syncAccount: false
    });
  });
});

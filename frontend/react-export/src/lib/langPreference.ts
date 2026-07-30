import type { Lang } from '../i18n';

/** UI language preference only - never auth tokens or private memorial data. */
export const LANG_PREFERENCE_STORAGE_KEY = 'eternal-world.ui.lang';

const SUPPORTED_LANGS: ReadonlySet<string> = new Set(['en', 'cs', 'ru']);

export const DEFAULT_LANG: Lang = 'en';

export function isLang(value: unknown): value is Lang {
  return typeof value === 'string' && SUPPORTED_LANGS.has(value);
}

/** Reads the last manually chosen UI language. Invalid/missing values fall
 * back to `DEFAULT_LANG` - never throws (localStorage may be unavailable). */
export function readStoredLang(): Lang {
  try {
    if (typeof localStorage === 'undefined') return DEFAULT_LANG;
    const stored = localStorage.getItem(LANG_PREFERENCE_STORAGE_KEY);
    return isLang(stored) ? stored : DEFAULT_LANG;
  } catch {
    return DEFAULT_LANG;
  }
}

/** Persists an explicit UI language choice across reloads. */
export function writeStoredLang(lang: Lang): void {
  if (!isLang(lang)) return;
  try {
    if (typeof localStorage === 'undefined') return;
    localStorage.setItem(LANG_PREFERENCE_STORAGE_KEY, lang);
  } catch {
    // Quota / private mode - UI still works for this session.
  }
}

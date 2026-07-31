import type { Lang } from '../i18n';

/** UI language preference only - never auth tokens or private memorial data. */
export const LANG_PREFERENCE_STORAGE_KEY = 'eternal-world.ui.lang';

const SUPPORTED_LANGS: ReadonlySet<string> = new Set(['en', 'cs', 'ru']);

export const DEFAULT_LANG: Lang = 'en';

export function isLang(value: unknown): value is Lang {
  return typeof value === 'string' && SUPPORTED_LANGS.has(value);
}

/** True when the user (or a prior restore) has an explicit valid local choice. */
export function hasExplicitStoredLang(): boolean {
  try {
    if (typeof localStorage === 'undefined') return false;
    return isLang(localStorage.getItem(LANG_PREFERENCE_STORAGE_KEY));
  } catch {
    return false;
  }
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

/**
 * Decide UI language after cookie session restore.
 *
 * Explicit localStorage choice always wins. Account
 * ``preferred_ui_language`` is only applied when nothing is stored yet —
 * otherwise returning to ``/app`` from marketing would force the account
 * default (often ``en``) over a Russian/Czech UI the user just used.
 */
export function resolveLangAfterSessionRestore(
  preferredUiLanguage: string | null | undefined
): { lang: Lang; source: 'local' | 'account' | 'default'; syncAccount: boolean } {
  if (hasExplicitStoredLang()) {
    const lang = readStoredLang();
    const account = isLang(preferredUiLanguage) ? preferredUiLanguage : null;
    return {
      lang,
      source: 'local',
      // Keep account preference aligned when marketing Nav only wrote localStorage.
      syncAccount: account !== lang
    };
  }
  if (isLang(preferredUiLanguage)) {
    return { lang: preferredUiLanguage, source: 'account', syncAccount: false };
  }
  return { lang: DEFAULT_LANG, source: 'default', syncAccount: false };
}

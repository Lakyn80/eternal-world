/**
 * Task 64.5.1 - Czech/Russian bilingual test UI.
 *
 * Narrow, typed locale support for this application's two supported
 * interface languages. Deliberately not a broad `string` locale type and
 * not an external i18n package - this app has exactly two locales and a
 * small, enumerable set of static UI strings (see ./dictionaries).
 */
export type AppLocale = "cs" | "ru";

export const SUPPORTED_LOCALES: readonly AppLocale[] = ["cs", "ru"];

export const DEFAULT_LOCALE: AppLocale = "cs";

export function isAppLocale(value: string | null | undefined): value is AppLocale {
  return value === "cs" || value === "ru";
}

/** Normalize an arbitrary route segment to a supported locale, or `null`
 * if it isn't one - callers should treat `null` as "unsupported locale"
 * (safe 404/redirect), never silently coerce it. */
export function parseAppLocale(value: string | null | undefined): AppLocale | null {
  return isAppLocale(value) ? value : null;
}

/** BCP-47 tag for `<html lang>` / `Intl`/`toLocaleString` formatting. */
export function toIntlLocaleTag(locale: AppLocale): string {
  return locale === "cs" ? "cs-CZ" : "ru-RU";
}

export const OTHER_LOCALE: Record<AppLocale, AppLocale> = {
  cs: "ru",
  ru: "cs",
};

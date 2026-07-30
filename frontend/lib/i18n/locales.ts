/**
 * Narrow, typed locale support for the current product UI. Deliberately not
 * a broad `string` locale type and not an external i18n package - the app
 * has a small, enumerable set of supported interface languages.
 */
export type AppLocale = "cs" | "ru" | "en";

export const SUPPORTED_LOCALES: readonly AppLocale[] = ["cs", "ru", "en"];

export const DEFAULT_LOCALE: AppLocale = "cs";

export function isAppLocale(value: string | null | undefined): value is AppLocale {
  return value === "cs" || value === "ru" || value === "en";
}

/** Normalize an arbitrary route segment to a supported locale, or `null`
 * if it isn't one - callers should treat `null` as "unsupported locale"
 * (safe 404/redirect), never silently coerce it. */
export function parseAppLocale(value: string | null | undefined): AppLocale | null {
  return isAppLocale(value) ? value : null;
}

/** BCP-47 tag for `<html lang>` / `Intl`/`toLocaleString` formatting. */
export function toIntlLocaleTag(locale: AppLocale): string {
  switch (locale) {
    case "cs":
      return "cs-CZ";
    case "ru":
      return "ru-RU";
    case "en":
      return "en-US";
    default:
      return "cs-CZ";
  }
}

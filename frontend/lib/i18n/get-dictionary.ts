import type { AppLocale } from "./locales";
import cs from "./dictionaries/cs";
import en from "./dictionaries/en";
import ru, { type Dictionary } from "./dictionaries/ru";

export type { Dictionary } from "./dictionaries/ru";

const DICTIONARIES: Record<AppLocale, Dictionary> = { cs, ru, en };

/** Synchronous by design: both dictionaries are small, statically-typed
 * modules bundled with the app - there is no network/database lookup here,
 * so server and client components can call this directly. */
export function getDictionary(locale: AppLocale): Dictionary {
  return DICTIONARIES[locale];
}

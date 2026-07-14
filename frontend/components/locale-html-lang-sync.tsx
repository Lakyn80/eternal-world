"use client";

import { useEffect } from "react";

import type { AppLocale } from "../lib/i18n/locales";

/**
 * Keeps `<html lang>` in sync with the active route locale.
 *
 * The single App Router root layout (`app/layout.tsx`) owns the `<html>`
 * tag with a static default; Next.js does not allow a nested layout to
 * re-emit it. This tiny client-side sync is the standard workaround so
 * `<html lang>` still reflects the real per-request locale (Part B.8).
 */
export function LocaleHtmlLangSync({ locale }: { locale: AppLocale }) {
  useEffect(() => {
    document.documentElement.lang = locale;
  }, [locale]);
  return null;
}

export default LocaleHtmlLangSync;

import { headers } from "next/headers";
import type { Viewport } from "next";

import { DEFAULT_LOCALE, parseAppLocale } from "../lib/i18n/locales";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
};

/**
 * Task 64.5.1: this is the single top-level App Router root layout (it owns
 * <html>/<body>, as required - Next.js does not allow a nested layout to
 * re-emit it). The active locale reaches this layout via the `x-app-locale`
 * request header that `middleware.ts` sets for every `/{locale}/...`
 * request, so `<html lang>` is already correct in the very first
 * server-rendered response (not just after client-side hydration).
 * `components/locale-html-lang-sync.tsx` remains as a defensive client-side
 * double-check. Falls back to the default locale for the legacy
 * (pre-locale) routes below, which now just redirect to their `/cs/...`
 * equivalent - see middleware.ts for the primary redirect path.
 */
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const headerLocale = headers().get("x-app-locale");
  const locale = parseAppLocale(headerLocale) ?? DEFAULT_LOCALE;

  return (
    <html lang={locale}>
      <body>{children}</body>
    </html>
  );
}

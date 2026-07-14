import type { ReactNode } from "react";
import { notFound } from "next/navigation";

import { LocaleHtmlLangSync } from "../../components/locale-html-lang-sync";
import { parseAppLocale } from "../../lib/i18n/locales";

/**
 * Task 64.5.1 locale layout, nested under the single App Router root
 * layout (`app/layout.tsx`, which owns `<html>`/`<body>`). Validates
 * `params.locale` (an unsupported segment renders the app's 404 page
 * instead of silently falling back to a default) and keeps `<html lang>`
 * in sync with the active locale via a small client-side effect.
 */
export default function LocaleLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: { locale: string };
}) {
  const locale = parseAppLocale(params.locale);
  if (locale === null) {
    notFound();
  }

  return (
    <>
      <LocaleHtmlLangSync locale={locale} />
      {children}
    </>
  );
}

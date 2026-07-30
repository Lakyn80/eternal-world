"use client";

import Link from "next/link";
import { usePathname, useSearchParams } from "next/navigation";

import { SUPPORTED_LOCALES, type AppLocale } from "../lib/i18n/locales";
import styles from "./language-switcher.module.css";

const LOCALE_LABELS: Record<AppLocale, string> = {
  cs: "Čeština",
  ru: "Русский",
  en: "English",
};

/**
 * Task 64.5.1 language switcher. Rewrites only the leading `/{locale}`
 * route segment, preserves the rest of the path and every query parameter
 * (e.g. `?candidate=14`), and never calls any API or mutates stored data -
 * it is a pure client-side navigation link.
 */
export function LanguageSwitcher({
  currentLocale,
  variant = "light",
}: {
  currentLocale: AppLocale;
  /** "dark" is for use on a dark background (e.g. the fa-chat hero panel). */
  variant?: "light" | "dark";
}) {
  const pathname = usePathname() ?? `/${currentLocale}`;
  const searchParams = useSearchParams();
  const queryString = searchParams?.toString();

  function buildHrefForLocale(locale: AppLocale): string {
    const segments = pathname.split("/").filter(Boolean);
    if (segments.length > 0 && (segments[0] === "cs" || segments[0] === "ru" || segments[0] === "en")) {
      segments[0] = locale;
    } else {
      segments.unshift(locale);
    }
    const path = `/${segments.join("/")}`;
    return queryString ? `${path}?${queryString}` : path;
  }

  return (
    <nav
      aria-label="Language switcher / Přepínač jazyka / Переключение языка"
      className={variant === "dark" ? `${styles.switcher} ${styles.switcherOnDark}` : styles.switcher}
    >
      {SUPPORTED_LOCALES.map((locale, index) => (
        <span key={locale}>
          {index > 0 ? <span className={styles.separator}>|</span> : null}
          {locale === currentLocale ? (
            <span aria-current="true" className={styles.activeLocale}>
              {LOCALE_LABELS[locale]}
            </span>
          ) : (
            <Link className={styles.localeLink} href={buildHrefForLocale(locale)}>
              {LOCALE_LABELS[locale]}
            </Link>
          )}
        </span>
      ))}
    </nav>
  );
}

export default LanguageSwitcher;

"use client";

import Link from "next/link";

import { getExperienceContent } from "../lib/experience-content";
import type { AppLocale } from "../lib/i18n/locales";
import { useUiTheme } from "../lib/use-ui-theme";
import { LanguageSwitcher } from "./language-switcher";
import PresentationDeck from "./presentation-deck";
import styles from "./presentation-page.module.css";

function themeLabel(locale: AppLocale, theme: "light" | "dark"): string {
  if (locale === "cs") {
    return theme === "light" ? "Tmavý režim" : "Světlý režim";
  }
  if (locale === "ru") {
    return theme === "light" ? "Тёмный режим" : "Светлый режим";
  }
  return theme === "light" ? "Dark mode" : "Light mode";
}

export function PresentationPage({ locale }: { locale: AppLocale }) {
  const content = getExperienceContent(locale);
  const [theme, toggleTheme] = useUiTheme();

  return (
    <main className={styles.page} data-theme={theme}>
      <header className={styles.header}>
        <div className={styles.headerLinks}>
          <Link className={styles.backLink} href={`/${locale}`}>
            {content.presentation.backHome}
          </Link>
          <Link className={styles.backLink} href={`/${locale}/fa-chat`}>
            {content.header.chat}
          </Link>
          <Link className={styles.backLink} href={`/${locale}/family-memory-review`}>
            {content.header.review}
          </Link>
        </div>
        <div className={styles.headerTools}>
          <LanguageSwitcher currentLocale={locale} variant="dark" />
          <button className={styles.themeButton} onClick={toggleTheme} type="button">
            {themeLabel(locale, theme)}
          </button>
        </div>
      </header>
      <PresentationDeck content={content} fullScreen locale={locale} />
    </main>
  );
}

export default PresentationPage;

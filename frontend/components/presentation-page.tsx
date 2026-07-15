"use client";

import { getExperienceContent } from "../lib/experience-content";
import type { AppLocale } from "../lib/i18n/locales";
import { useUiTheme } from "../lib/use-ui-theme";
import ProductNav from "./product-nav";
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
      <ProductNav
        activeHref={`/${locale}/presentation`}
        items={[
          { href: `/${locale}`, label: content.presentation.backHome },
          { href: `/${locale}/fa-chat`, label: content.header.chat },
          { href: `/${locale}/family-memory-review`, label: content.header.review },
        ]}
        locale={locale}
        onToggleTheme={toggleTheme}
        subtitle={content.presentation.title}
        theme={theme}
        themeLabel={themeLabel(locale, theme)}
      />
      <PresentationDeck content={content} fullScreen locale={locale} />
    </main>
  );
}

export default PresentationPage;

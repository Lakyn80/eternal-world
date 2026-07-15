"use client";

import Link from "next/link";
import { useEffect } from "react";

import { getExperienceContent } from "../lib/experience-content";
import type { AppLocale } from "../lib/i18n/locales";
import { useUiTheme } from "../lib/use-ui-theme";
import { LanguageSwitcher } from "./language-switcher";
import PresentationDeck from "./presentation-deck";
import styles from "./marketing-home.module.css";

function themeButtonLabel(locale: AppLocale, theme: "light" | "dark"): string {
  if (locale === "cs") {
    return theme === "light" ? "Tmavý režim" : "Světlý režim";
  }
  if (locale === "ru") {
    return theme === "light" ? "Тёмный режим" : "Светлый режим";
  }
  return theme === "light" ? "Dark mode" : "Light mode";
}

function getSectionLabels(locale: AppLocale) {
  if (locale === "cs") {
    return {
      problem: "Problém",
      process: "Proces",
      showcase: "Ukázka",
      trust: "Důvěra",
      languages: "Jazyky",
      presentation: "Prezentace",
      mission: "Mise",
      workspace: "Pracovní prostor",
    };
  }
  if (locale === "ru") {
    return {
      problem: "Проблема",
      process: "Процесс",
      showcase: "Демонстрация",
      trust: "Доверие",
      languages: "Языки",
      presentation: "Презентация",
      mission: "Миссия",
      workspace: "Рабочее пространство",
    };
  }
  return {
    problem: "Problem",
    process: "Process",
    showcase: "Showcase",
    trust: "Trust",
    languages: "Languages",
    presentation: "Presentation",
    mission: "Mission",
    workspace: "Workspace",
  };
}

export function MarketingHome({ locale }: { locale: AppLocale }) {
  const content = getExperienceContent(locale);
  const sectionLabels = getSectionLabels(locale);
  const [theme, toggleTheme] = useUiTheme();

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            entry.target.setAttribute("data-visible", "true");
          }
        }
      },
      { threshold: 0.18 }
    );

    const elements = document.querySelectorAll("[data-reveal]");
    elements.forEach((element) => observer.observe(element));
    return () => observer.disconnect();
  }, []);

  return (
    <main className={styles.page} data-theme={theme}>
      <div className={styles.backgroundPaper} />
      <header className={styles.header}>
        <Link className={styles.brand} href={`/${locale}`}>
          <span className={styles.brandMark}>EW</span>
          <span>{content.brand}</span>
        </Link>
        <nav className={styles.nav}>
          <a href="#story">{content.header.story}</a>
          <a href="#process">{content.header.process}</a>
          <a href="#trust">{content.header.trust}</a>
          <a href="#presentation">{content.header.presentation}</a>
        </nav>
        <div className={styles.headerTools}>
          <LanguageSwitcher currentLocale={locale} />
          <button className={styles.themeButton} onClick={toggleTheme} type="button">
            {themeButtonLabel(locale, theme)}
          </button>
        </div>
      </header>

      <section className={`${styles.hero} ${styles.revealBlock}`} data-reveal id="story">
        <div className={styles.heroCopy}>
          <p className={styles.eyebrow}>{content.hero.eyebrow}</p>
          <h1 className={styles.heroTitle}>{content.hero.title}</h1>
          <p className={styles.heroLead}>{content.hero.lead}</p>
          <div className={styles.heroActions}>
            <Link className={styles.primaryCta} href={`/${locale}/fa-chat`}>
              {content.hero.primaryCta}
            </Link>
            <Link className={styles.secondaryCta} href={`/${locale}/presentation`}>
              {content.hero.secondaryCta}
            </Link>
          </div>
          <p className={styles.trustLine}>{content.hero.trustLine}</p>
        </div>

        <div className={styles.heroVisual}>
          <div className={styles.avatarCard}>
            <div className={styles.avatarAura} />
            <div className={styles.avatarOrb}>
              <span>Eva</span>
            </div>
            <div className={styles.voiceBars} aria-hidden="true">
              <span />
              <span />
              <span />
              <span />
              <span />
            </div>
            <div className={styles.evidencePanel}>
              <p className={styles.panelLabel}>{content.hero.evidenceTitle}</p>
              <ul className={styles.evidenceList}>
                {content.hero.evidenceSources.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
            <div className={styles.noEvidenceCard}>
              <div className={styles.noEvidenceTitle}>{content.hero.noEvidenceTitle}</div>
              <p>{content.hero.noEvidenceBody}</p>
            </div>
          </div>
        </div>
      </section>

      <section className={`${styles.section} ${styles.revealBlock}`} data-reveal>
        <div className={styles.sectionHeading}>
          <p className={styles.sectionKicker}>{sectionLabels.problem}</p>
          <h2>{content.problem.title}</h2>
          <p>{content.problem.intro}</p>
        </div>
        <div className={styles.lossGrid}>
          {content.problem.losses.map((item) => (
            <article className={styles.lossCard} key={item}>
              <span className={styles.lossPulse} aria-hidden="true" />
              <p>{item}</p>
            </article>
          ))}
        </div>
      </section>

      <section className={`${styles.section} ${styles.revealBlock}`} data-reveal id="process">
        <div className={styles.sectionHeading}>
          <p className={styles.sectionKicker}>{sectionLabels.process}</p>
          <h2>{content.steps.title}</h2>
        </div>
        <div className={styles.stepGrid}>
          {content.steps.items.map((item) => (
            <article className={styles.stepCard} key={item.title}>
              <div className={styles.stepBadge}>{item.step}</div>
              <h3>{item.title}</h3>
              <p>{item.body}</p>
              <ul className={styles.inlineList}>
                {item.bullets.map((bullet) => (
                  <li key={bullet}>{bullet}</li>
                ))}
              </ul>
            </article>
          ))}
        </div>
      </section>

      <section className={`${styles.section} ${styles.revealBlock}`} data-reveal>
        <div className={styles.sectionHeading}>
          <p className={styles.sectionKicker}>{sectionLabels.showcase}</p>
          <h2>{content.showcase.title}</h2>
          <p>{content.showcase.intro}</p>
        </div>
        <div className={styles.showcaseGrid}>
          <article className={styles.showcaseCard}>
            <div className={styles.cardHeader}>{content.showcase.chat.title}</div>
            <p className={styles.mockLabel}>{content.showcase.chat.questionLabel}</p>
            <div className={styles.chatBubble}>{content.showcase.chat.question}</div>
            <p className={styles.mockLabel}>{content.showcase.chat.answerLabel}</p>
            <div className={`${styles.chatBubble} ${styles.chatBubbleWarm}`}>{content.showcase.chat.answer}</div>
            <p className={styles.mockLabel}>{content.showcase.chat.evidenceLabel}</p>
            <ul className={styles.inlineList}>
              {content.showcase.chat.evidence.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
            <div className={styles.noEvidenceCard}>
              <strong>{content.showcase.chat.unknownQuestion}</strong>
              <p>{content.showcase.chat.unknownAnswer}</p>
            </div>
          </article>

          <article className={styles.showcaseCard}>
            <div className={styles.cardHeader}>{content.showcase.review.title}</div>
            <div className={styles.queueTable}>
              <div className={styles.queueHead}>
                {content.showcase.review.columns.map((item) => (
                  <span key={item}>{item}</span>
                ))}
              </div>
              {content.showcase.review.rows.map((row) => (
                <div className={styles.queueRow} key={row.join("-")}>
                  {row.map((cell) => (
                    <span key={cell}>{cell}</span>
                  ))}
                </div>
              ))}
            </div>
            <p className={styles.cardNote}>{content.showcase.review.footer}</p>
          </article>

          <article className={styles.showcaseCard}>
            <div className={styles.cardHeader}>{content.showcase.directives.title}</div>
            <div className={styles.directiveGrid}>
              {content.showcase.directives.values.map((item) => (
                <div className={styles.directiveCard} key={item.label}>
                  <span>{item.label}</span>
                  <strong>{item.value}</strong>
                </div>
              ))}
            </div>
            <p className={styles.cardNote}>{content.showcase.directives.note}</p>
          </article>
        </div>
      </section>

      <section className={`${styles.section} ${styles.revealBlock}`} data-reveal id="trust">
        <div className={styles.sectionHeading}>
          <p className={styles.sectionKicker}>{sectionLabels.trust}</p>
          <h2>{content.trust.title}</h2>
        </div>
        <div className={styles.trustGrid}>
          {content.trust.cards.map((card) => (
            <article className={styles.trustCard} key={card.title}>
              <h3>{card.title}</h3>
              <p>{card.body}</p>
            </article>
          ))}
        </div>
      </section>

      <section className={`${styles.section} ${styles.revealBlock}`} data-reveal>
        <div className={styles.sectionHeading}>
          <p className={styles.sectionKicker}>{sectionLabels.languages}</p>
          <h2>{content.multilingual.title}</h2>
          <p>{content.multilingual.body}</p>
        </div>
        <div className={styles.languageConversation}>
          {content.multilingual.cards.map((card) => (
            <article className={styles.languageCard} key={card.language}>
              <span>{card.language}</span>
              <p>{card.line}</p>
            </article>
          ))}
        </div>
        <p className={styles.sectionNote}>{content.multilingual.note}</p>
      </section>

      <section className={`${styles.section} ${styles.revealBlock}`} data-reveal id="presentation">
        <div className={styles.sectionHeading}>
          <p className={styles.sectionKicker}>{sectionLabels.presentation}</p>
          <h2>{content.presentation.title}</h2>
          <p>{content.presentation.body}</p>
        </div>
        <PresentationDeck content={content} locale={locale} />
        <div className={styles.presentationActions}>
          <span>{content.presentation.usage}</span>
          <Link className={styles.secondaryCta} href={`/${locale}/presentation`}>
            {content.presentation.openFullScreen}
          </Link>
        </div>
      </section>

      <section className={`${styles.section} ${styles.missionSection} ${styles.revealBlock}`} data-reveal>
        <div className={styles.missionCopy}>
          <p className={styles.sectionKicker}>{sectionLabels.mission}</p>
          <h2>{content.mission.title}</h2>
          <p>{content.mission.body}</p>
          <div className={styles.heroActions}>
            <Link className={styles.primaryCta} href={`/${locale}/fa-chat`}>
              {content.mission.waitlist}
            </Link>
            <Link className={styles.secondaryCta} href={`/${locale}/family-memory-review`}>
              {content.mission.contact}
            </Link>
          </div>
          <p className={styles.trustLine}>{content.mission.trustLine}</p>
        </div>
        <div className={styles.ctaPanel}>
          <div className={styles.ctaLabel}>{sectionLabels.workspace}</div>
          <Link className={styles.workspaceLink} href={`/${locale}/fa-chat`}>
            {content.header.chat}
          </Link>
          <Link className={styles.workspaceLink} href={`/${locale}/family-memory-review`}>
            {content.header.review}
          </Link>
        </div>
      </section>
    </main>
  );
}

export default MarketingHome;

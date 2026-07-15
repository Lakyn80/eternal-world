"use client";

import type { AppLocale } from "../../lib/i18n/locales";
import { getV2ExperienceContent, type V2SectionId } from "../../lib/v2-experience/content";
import V2Architecture from "./v2-architecture";
import V2AvatarStudio from "./v2-avatar-studio";
import V2ConversationDemo from "./v2-conversation-demo";
import V2Features from "./v2-features";
import V2Footer from "./v2-footer";
import V2Hero from "./v2-hero";
import V2Moments from "./v2-moments";
import V2Nav from "./v2-nav";
import V2Timeline from "./v2-timeline";

type V2ExperiencePageProps = {
  locale: AppLocale;
};

export default function V2ExperiencePage({ locale }: V2ExperiencePageProps) {
  const content = getV2ExperienceContent(locale);

  function scrollToSection(sectionId: V2SectionId) {
    const element = document.getElementById(sectionId);
    if (!element) {
      return;
    }

    element.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  }

  return (
    <main
      className="min-h-screen overflow-x-hidden bg-ink font-sans text-fg selection:bg-cyan/30"
      style={{
        backgroundImage:
          "linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0)), radial-gradient(circle at top, rgba(44,55,120,0.16), transparent 42%)",
      }}
    >
      <V2Nav content={content} locale={locale} onNavigate={scrollToSection} />
      <V2Hero content={content.hero} locale={locale} onShowDemo={() => scrollToSection("demo")} />
      <V2ConversationDemo content={content.conversation} locale={locale} />
      <V2Features content={content.features} />
      <V2Architecture content={content.architecture} />
      <V2Timeline content={content.timeline} locale={locale} />
      <V2AvatarStudio content={content.studio} locale={locale} />
      <V2Moments content={content.moments} locale={locale} />
      <V2Footer content={content.footer} locale={locale} />
    </main>
  );
}

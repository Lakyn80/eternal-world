import Link from "next/link";

import type { AppLocale } from "../../lib/i18n/locales";
import { getV2Route, type V2ExperienceContent, type V2SectionId } from "../../lib/v2-experience/content";

type V2NavProps = {
  locale: AppLocale;
  content: V2ExperienceContent;
  onNavigate: (sectionId: V2SectionId) => void;
};

export default function V2Nav({ locale, content, onNavigate }: V2NavProps) {
  return (
    <nav className="fixed inset-x-0 top-0 z-50 border-b border-white/10 bg-ink/75 backdrop-blur-xl">
      <div className="mx-auto max-w-7xl px-4 py-3 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center justify-between gap-3 sm:flex-nowrap sm:gap-4">
          <button
            className="flex items-center gap-3 text-left"
            onClick={() => onNavigate("story")}
            type="button"
          >
            <span
              className="block h-10 w-10 rounded-full shadow-[0_0_28px_rgba(96,180,255,0.45)]"
              style={{
                background: "radial-gradient(circle at 35% 30%, #d4f1ff, #65b4f4 50%, #4f3ec9 92%)",
              }}
            />
            <span className="hidden min-w-0 sm:block">
              <span className="block text-sm font-semibold tracking-[0.08em] text-fg">{content.brand.name}</span>
              <span className="block text-xs uppercase tracking-[0.24em] text-fg/45">{content.brand.accent}</span>
            </span>
          </button>

          <div className="hidden items-center gap-2 xl:flex">
            {content.navigation.links.map((link) => (
              <button
                className="rounded-full px-4 py-2 text-sm text-fg/70 transition-colors hover:bg-white/6 hover:text-fg"
                key={link.id}
                onClick={() => onNavigate(link.id)}
                type="button"
              >
                {link.label}
              </button>
            ))}
          </div>

          <div className="ml-auto flex items-center gap-2">
            <div
              aria-label={content.navigation.switchLanguage}
              className="hidden rounded-full border border-white/12 bg-white/5 p-1 sm:flex"
            >
              {(["cs", "ru", "en"] as const).map((candidateLocale) => {
                const active = candidateLocale === locale;
                return (
                  <Link
                    aria-current={active ? "page" : undefined}
                    className={`rounded-full px-3 py-1.5 text-xs font-medium transition-colors ${
                      active ? "bg-cyan/18 text-fg" : "text-fg/55 hover:text-fg"
                    }`}
                    href={getV2Route(candidateLocale)}
                    key={candidateLocale}
                  >
                    {content.localeNames[candidateLocale]}
                  </Link>
                );
              })}
            </div>

            <Link
              className="inline-flex max-w-[10.5rem] items-center justify-center rounded-full bg-[linear-gradient(135deg,#8fd6f5,#8b7cf6)] px-3 py-2 text-center text-xs font-semibold leading-4 text-ink shadow-[0_0_28px_rgba(96,180,255,0.28)] transition-transform hover:-translate-y-0.5 sm:max-w-none sm:px-4 sm:text-sm sm:leading-5"
              href={`/${locale}/fa-chat`}
            >
              {content.navigation.openWorkspace}
            </Link>
          </div>
        </div>

        <div className="mt-3 flex gap-2 overflow-x-auto pb-1 xl:hidden">
          {content.navigation.links.map((link) => (
            <button
              className="shrink-0 rounded-full border border-white/10 bg-white/[0.04] px-3 py-1.5 text-xs text-fg/70 transition-colors hover:border-cyan/35 hover:text-fg"
              key={link.id}
              onClick={() => onNavigate(link.id)}
              type="button"
            >
              {link.label}
            </button>
          ))}
        </div>
      </div>
    </nav>
  );
}

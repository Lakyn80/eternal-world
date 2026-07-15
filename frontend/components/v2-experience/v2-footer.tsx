import Link from "next/link";

import type { AppLocale } from "../../lib/i18n/locales";
import type { V2ExperienceContent } from "../../lib/v2-experience/content";

type V2FooterProps = {
  locale: AppLocale;
  content: V2ExperienceContent["footer"];
};

export default function V2Footer({ locale, content }: V2FooterProps) {
  return (
    <section className="relative overflow-hidden px-4 pb-16 pt-28 sm:px-6 lg:px-8">
      <div
        className="absolute inset-0"
        style={{
          background: "radial-gradient(ellipse 55% 60% at 50% 100%, rgba(63, 76, 187, 0.25), transparent 70%)",
        }}
      />

      <div className="relative mx-auto max-w-5xl text-center">
        <h2 className="mx-auto max-w-[18ch] font-serif text-[clamp(2.3rem,5vw,4.2rem)] leading-[1.04] text-fg">
          {content.title}
        </h2>
        <p className="mx-auto mt-5 max-w-3xl text-base leading-8 text-fg/65 md:text-lg">{content.body}</p>

        <div className="mt-10 flex flex-wrap justify-center gap-4">
          <Link
            className="inline-flex w-full items-center justify-center rounded-full bg-[linear-gradient(135deg,#8fd6f5,#8b7cf6)] px-6 py-3.5 text-base font-semibold text-ink sm:w-auto"
            href={`/${locale}/fa-chat`}
          >
            {content.primaryCta}
          </Link>
          <Link
            className="inline-flex w-full items-center justify-center rounded-full border border-white/15 bg-white/5 px-6 py-3.5 text-base font-medium text-fg transition-colors hover:border-cyan/40 hover:bg-cyan/10 sm:w-auto"
            href={`/${locale}/family-memory-review`}
          >
            {content.secondaryCta}
          </Link>
        </div>

        <div className="mt-20 border-t border-white/10 pt-6 text-sm text-fg/42">{content.note}</div>
      </div>
    </section>
  );
}

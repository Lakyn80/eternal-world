import type { Lang } from '../i18n';
import { T } from '../i18n';

export default function Footer({ lang, onGoStudio }: { lang: Lang; onGoStudio: () => void }) {
  const t = T[lang];
  return (
    <section
      className="relative py-32 pb-16 px-6 text-center overflow-hidden"
    >
      <div
        className="absolute inset-0"
        style={{ background: 'radial-gradient(ellipse 55% 60% at 50% 100%, rgba(63,76,187,.25), transparent 70%)' }}
      />
      <div className="relative">
        <h2 className="mx-auto font-serif font-normal text-[clamp(34px,4.4vw,60px)] max-w-[18ch] leading-[1.12] text-balance">
          {t.footTitle}
        </h2>
        <p className="mt-5.5 mx-auto text-fg/60 font-light max-w-[48ch] leading-relaxed">{t.footSub}</p>
        <button
          onClick={onGoStudio}
          className="mt-9 font-sans text-[15px] font-medium text-ink rounded-full px-10 py-4 shadow-[0_0_50px_rgba(110,150,255,.5)]"
          style={{ background: 'linear-gradient(135deg,#8fd6f5,#8b7cf6)' }}
        >
          {t.btnCreate}
        </button>
        <div className="mt-24 pt-6.5 border-t border-white/[0.07] flex justify-between flex-wrap gap-3 text-xs text-fg/40 max-w-[1100px] mx-auto">
          <div>Memorial World · Věčný svět</div>
          <div>{t.footNote}</div>
        </div>
      </div>
    </section>
  );
}

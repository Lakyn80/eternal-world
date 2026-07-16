import type { Lang } from '../i18n';
import { T, MOMENTS } from '../i18n';
import ImageSlot from './ImageSlot';

export default function Moments({ lang }: { lang: Lang }) {
  const t = T[lang];
  const moments = MOMENTS[lang];

  return (
    <section
      id="moments"
      className="py-24 px-6"
      style={{ background: 'radial-gradient(ellipse 70% 50% at 50% 60%, rgba(120,90,40,.10), transparent 70%)' }}
    >
      <div className="text-center mb-14">
        <div className="text-xs tracking-[.3em] uppercase text-gold mb-3.5">{t.momKicker}</div>
        <h2 className="font-serif font-normal text-[clamp(30px,3.6vw,48px)]">{t.momTitle}</h2>
      </div>
      <div className="grid gap-5.5 max-w-[1180px] mx-auto" style={{ gridTemplateColumns: 'repeat(auto-fit,minmax(300px,1fr))' }}>
        {moments.map((m) => (
          <div key={m.slot} className="flex flex-col bg-white/[0.035] border border-white/[0.08] rounded-[22px] overflow-hidden backdrop-blur-md">
            <div className="h-[230px]">
              <ImageSlot id={m.slot} placeholder={m.ph} className="w-full h-full rounded-none" />
            </div>
            <div className="p-6.5 pt-6.5 pb-7.5 flex flex-col gap-3">
              <div className="font-serif italic text-[21px] leading-snug text-gold text-pretty">{m.quote}</div>
              <div className="text-[13px] leading-relaxed font-light text-fg/60">{m.caption}</div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

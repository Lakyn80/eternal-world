import type { Lang } from '../i18n';
import { T, BRAIN } from '../i18n';

export default function Brain({ lang }: { lang: Lang }) {
  const t = T[lang];
  const brain = BRAIN[lang];

  return (
    <section
      id="brain"
      className="py-24 px-6 text-center"
      style={{ background: 'radial-gradient(ellipse 60% 60% at 50% 50%, rgba(58,54,140,.16), transparent 70%)' }}
    >
      <div className="text-xs tracking-[.3em] uppercase text-cyan mb-3.5">{t.brainKicker}</div>
      <h2 className="font-serif font-normal text-[clamp(30px,3.6vw,48px)] mb-14">{t.brainTitle}</h2>
      <div className="flex items-center justify-center flex-wrap max-w-[1100px] mx-auto">
        {brain.map((b, i) => (
          <div key={b.name} className="flex items-center">
            <div
              className="flex flex-col gap-1.5 px-6.5 py-5 bg-white/[0.04] border border-white/[0.12] rounded-2xl backdrop-blur-sm animate-floaty"
              style={{ animationDelay: `${i * 0.5}s` }}
            >
              <div className="text-[15px] font-medium">{b.name}</div>
              <div className="text-[11.5px] text-fg/50">{b.sub}</div>
            </div>
            {i < brain.length - 1 && (
              <div
                className="w-[54px] h-0.5 animate-flowlight"
                style={{
                  background: 'linear-gradient(90deg,transparent,#7fd8f7,#8b7cf6,transparent)',
                  backgroundSize: '200% 100%'
                }}
              />
            )}
          </div>
        ))}
      </div>
    </section>
  );
}

import type { Lang } from '../i18n';
import { T, FEATURES } from '../i18n';

const GLOWS = [
  { bg: 'radial-gradient(circle at 35% 30%,#bfe9ff,#59a8f0 60%,#2a2a7a)', shadow: 'rgba(89,168,240,.4)' },
  { bg: 'radial-gradient(circle at 35% 30%,#e4d4ff,#8b7cf6 60%,#3a2a7a)', shadow: 'rgba(139,124,246,.4)' },
  { bg: 'radial-gradient(circle at 35% 30%,#ffe9c0,#e8c37a 60%,#7a5a2a)', shadow: 'rgba(232,195,122,.35)' }
];

export default function Features({ lang }: { lang: Lang }) {
  const t = T[lang];
  const features = FEATURES[lang];

  return (
    <section id="features" className="w-full max-w-[1180px] mx-auto overflow-hidden px-4 py-24 sm:px-6">
      <div className="text-center mb-14">
        <div className="text-xs tracking-[.3em] uppercase text-cyan mb-3.5">{t.featKicker}</div>
        <h2 className="font-serif font-normal text-[clamp(30px,3.6vw,48px)]">{t.featTitle}</h2>
      </div>
      <div className="grid min-w-0 gap-4.5" style={{ gridTemplateColumns: 'repeat(auto-fit,minmax(min(100%,280px),1fr))' }}>
        {features.map((f, i) => {
          const glow = GLOWS[i % 3];
          return (
            <div
              key={f.title}
              className="relative min-w-0 p-5 bg-white/[0.035] border border-white/[0.08] rounded-[20px] backdrop-blur-md transition-transform duration-500 hover:-translate-y-1.5 hover:border-cyan/35 sm:p-7"
            >
              <div
                className="w-9 h-9 rounded-xl mb-5"
                style={{ background: glow.bg, boxShadow: `0 0 22px ${glow.shadow}` }}
              />
              <div className="break-words text-[17.5px] font-medium mb-2">{f.title}</div>
              <div className="break-words text-sm leading-relaxed font-light text-fg/60 text-pretty">{f.desc}</div>
              <div className="flex flex-wrap gap-1.5 mt-4.5">
                {f.points.map((p) => (
                  <span key={p} className="text-[11.5px] text-fg/55 border border-white/10 rounded-full px-2.5 py-1">
                    {p}
                  </span>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}

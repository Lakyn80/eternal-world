import { useState, useEffect } from 'react';
import type { Lang } from '../i18n';
import { T, EVENTS } from '../i18n';
import ImageSlot from './ImageSlot';

export default function Timeline({ lang }: { lang: Lang }) {
  const t = T[lang];
  const events = EVENTS[lang];
  const [selected, setSelected] = useState(5);

  useEffect(() => setSelected(5), [lang]);
  const sel = events[selected];

  return (
    <section id="timeline" className="py-24 overflow-hidden">
      <div className="text-center mb-12 px-6">
        <div className="text-xs tracking-[.3em] uppercase text-cyan mb-3.5">{t.tlKicker}</div>
        <h2 className="font-serif font-normal text-[clamp(30px,3.6vw,48px)]">{t.tlTitle}</h2>
      </div>

      <div className="grid gap-2 px-4 md:hidden">
        {events.map((e, i) => {
          const active = i === selected;
          return (
            <button
              key={e.year}
              onClick={() => setSelected(i)}
              className={`flex min-w-0 items-center justify-between gap-3 rounded-2xl border px-4 py-3 text-left ${
                active ? 'border-gold/45 bg-gold/10 text-gold' : 'border-white/10 bg-white/[.035] text-fg/70'
              }`}
            >
              <span className="shrink-0 text-sm font-semibold">{e.year}</span>
              <span className="min-w-0 flex-1 break-words text-sm">{e.title}</span>
            </button>
          );
        })}
      </div>

      <div className="relative hidden overflow-x-auto py-7 px-14 md:block">
        <div className="relative flex items-start" style={{ minWidth: 'max-content' }}>
          <div
            className="absolute left-0 right-0 top-[9px] h-px"
            style={{ background: 'linear-gradient(90deg,transparent,rgba(127,216,247,.4) 8%,rgba(139,124,246,.4) 92%,transparent)' }}
          />
          {events.map((e, i) => {
            const active = i === selected;
            return (
              <button
                key={e.year}
                onClick={() => setSelected(i)}
                className="relative flex flex-col items-center gap-3 w-[140px] bg-transparent border-none cursor-pointer font-sans text-inherit p-0"
              >
                <div
                  className="rounded-full"
                  style={
                    active
                      ? { width: 18, height: 18, background: 'radial-gradient(circle at 35% 30%,#fff,#e8c37a 55%,#7a5a2a)', boxShadow: '0 0 24px rgba(232,195,122,.8)' }
                      : { width: 12, height: 12, marginTop: 3, background: 'radial-gradient(circle at 35% 30%,#bfe9ff,#59a8f0 60%,#2a2a7a)', boxShadow: '0 0 14px rgba(96,180,255,.55)' }
                  }
                />
                <div className="text-[15px] font-semibold" style={{ color: active ? '#e8c37a' : '#e9ecf5' }}>
                  {e.year}
                </div>
                <div className="text-xs leading-snug text-fg/55 max-w-[120px] text-center">{e.title}</div>
              </button>
            );
          })}
        </div>
      </div>

      <div className="flex w-[min(880px,calc(100%-32px))] flex-col gap-5 items-stretch mx-auto mt-6.5 p-5 bg-white/[0.035] border border-white/[0.09] rounded-[22px] backdrop-blur-lg animate-fadein sm:w-[min(880px,calc(100%-48px))] sm:p-7 md:flex-row md:gap-6.5">
        <div className="h-[190px] w-full flex-none md:w-[240px]">
          <ImageSlot id={`tl-${sel.year}`} placeholder={t.tlDrop} className="w-full h-full" />
        </div>
        <div className="min-w-0 flex-1 flex flex-col justify-center gap-2.5">
          <div className="font-serif text-[42px] text-gold leading-none">{sel.year}</div>
          <div className="break-words text-[18px] font-medium">{sel.title}</div>
          <div className="break-words text-sm leading-relaxed font-light text-fg/65 text-pretty">{sel.desc}</div>
          <div className="flex flex-wrap gap-2 mt-1.5">
            {sel.media.map((m) => (
              <span key={m} className="text-[11.5px] text-cyan border border-cyan/30 rounded-full px-2.5 py-1">
                {m}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

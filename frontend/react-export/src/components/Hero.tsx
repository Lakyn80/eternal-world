import { useEffect, useRef } from 'react';
import type { Lang } from '../i18n';
import { T } from '../i18n';
import { useParticles } from '../hooks/useParticles';

interface Props {
  lang: Lang;
  onGoStudio: () => void;
  onGoDemo: () => void;
  particles: boolean;
}

export default function Hero({ lang, onGoStudio, onGoDemo, particles }: Props) {
  const t = T[lang];
  const canvasRef = useParticles(particles);
  const orbRef = useRef<HTMLDivElement>(null);
  const irisRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const onMove = (e: MouseEvent) => {
      const orb = orbRef.current, iris = irisRef.current;
      if (!orb || !iris) return;
      const r = orb.getBoundingClientRect();
      const dx = e.clientX - (r.left + r.width / 2), dy = e.clientY - (r.top + r.height / 2);
      const d = Math.max(1, Math.hypot(dx, dy));
      const k = Math.min(18, d / 22);
      iris.style.transform = `translate(${(dx / d) * k}px, ${(dy / d) * k}px)`;
    };
    window.addEventListener('mousemove', onMove);
    return () => window.removeEventListener('mousemove', onMove);
  }, []);

  return (
    <section
      id="hero"
      className="relative min-h-screen flex flex-col items-center justify-center text-center px-6 pt-32 pb-20 overflow-hidden"
    >
      <canvas ref={canvasRef} className="absolute inset-0 w-full h-full" />
      <div
        className="absolute inset-0"
        style={{
          background:
            'radial-gradient(ellipse 70% 55% at 50% 42%, rgba(63,76,187,.22), transparent 65%), radial-gradient(ellipse 40% 30% at 50% 46%, rgba(127,216,247,.10), transparent 70%)'
        }}
      />
      <div className="relative z-10 flex flex-col items-center">
        <div ref={orbRef} className="relative w-[230px] h-[230px] mb-11 animate-breathe">
          <div
            className="absolute -inset-9 rounded-full animate-halo"
            style={{ background: 'radial-gradient(circle, rgba(110,160,255,.28), transparent 70%)' }}
          />
          <div
            className="absolute inset-0 rounded-full"
            style={{
              background:
                'radial-gradient(circle at 36% 30%, rgba(210,238,255,.95), rgba(110,170,246,.85) 38%, rgba(88,72,214,.9) 72%, rgba(20,18,60,.95))',
              boxShadow: '0 0 60px rgba(100,160,255,.45), inset 0 0 44px rgba(255,255,255,.18)'
            }}
          />
          <div className="absolute inset-3.5 rounded-full border border-white/25" />
          <div
            ref={irisRef}
            className="absolute left-1/2 top-1/2 w-14 h-14 -ml-7 -mt-7 rounded-full transition-transform duration-300"
            style={{
              background: 'radial-gradient(circle at 40% 35%, #fff, #bfe9ff 30%, #1b2a6e 75%)',
              boxShadow: '0 0 26px rgba(190,230,255,.8)'
            }}
          />
        </div>
        <div className="text-[12.5px] tracking-[.34em] uppercase text-fg/50 mb-5">{t.kicker}</div>
        <h1 className="font-serif font-normal text-[clamp(44px,6.4vw,84px)] leading-[1.04] tracking-tight max-w-[14ch] text-balance">
          {t.heroTitle}
        </h1>
        <p className="mt-6 max-w-[56ch] text-[17px] leading-[1.65] font-light text-fg/65 text-pretty">
          {t.heroSub}
        </p>
        <div className="flex gap-4 mt-10 flex-wrap justify-center">
          <button
            onClick={onGoStudio}
            className="font-sans text-[15px] font-medium text-ink rounded-full px-8 py-4 shadow-[0_0_44px_rgba(110,150,255,.45)] hover:shadow-[0_0_64px_rgba(130,170,255,.65)] transition-shadow"
            style={{ background: 'linear-gradient(135deg,#8fd6f5,#8b7cf6)' }}
          >
            {t.btnCreate}
          </button>
          <button
            onClick={onGoDemo}
            className="font-sans text-[15px] font-light text-fg rounded-full px-8 py-4 bg-white/5 border border-white/[0.18] backdrop-blur hover:bg-white/10 transition-colors"
          >
            {t.btnDemo}
          </button>
        </div>
      </div>
    </section>
  );
}

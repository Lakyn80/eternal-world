import { useEffect, useRef } from "react";
import Link from "next/link";

import { useV2Particles } from "../../hooks/use-v2-particles";
import type { AppLocale } from "../../lib/i18n/locales";
import type { V2ExperienceContent } from "../../lib/v2-experience/content";

type V2HeroProps = {
  locale: AppLocale;
  content: V2ExperienceContent["hero"];
  onShowDemo: () => void;
};

export default function V2Hero({ locale, content, onShowDemo }: V2HeroProps) {
  const canvasRef = useV2Particles(true);
  const orbRef = useRef<HTMLDivElement>(null);
  const irisRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const mediaQuery = window.matchMedia("(pointer: fine)");
    if (!mediaQuery.matches) {
      return;
    }

    const handlePointerMove = (event: MouseEvent) => {
      const orb = orbRef.current;
      const iris = irisRef.current;
      if (!orb || !iris) {
        return;
      }

      const bounds = orb.getBoundingClientRect();
      const deltaX = event.clientX - (bounds.left + bounds.width / 2);
      const deltaY = event.clientY - (bounds.top + bounds.height / 2);
      const distance = Math.max(1, Math.hypot(deltaX, deltaY));
      const travel = Math.min(18, distance / 22);

      iris.style.transform = `translate(${(deltaX / distance) * travel}px, ${(deltaY / distance) * travel}px)`;
    };

    window.addEventListener("mousemove", handlePointerMove);
    return () => window.removeEventListener("mousemove", handlePointerMove);
  }, []);

  return (
    <section className="relative overflow-hidden px-4 pb-20 pt-36 sm:px-6 lg:px-8" id="story">
      <canvas className="absolute inset-0 h-full w-full" ref={canvasRef} />
      <div
        className="absolute inset-0"
        style={{
          background:
            "radial-gradient(ellipse 70% 58% at 50% 36%, rgba(63, 76, 187, 0.24), transparent 65%), radial-gradient(ellipse 40% 32% at 50% 48%, rgba(127, 216, 247, 0.12), transparent 70%)",
        }}
      />

      <div className="relative mx-auto grid max-w-7xl items-center gap-12 lg:grid-cols-[1.15fr_0.85fr]">
        <div className="max-w-3xl">
          <p className="text-xs uppercase tracking-[0.36em] text-cyan">{content.kicker}</p>
          <h1 className="mt-6 max-w-[14ch] font-serif text-[clamp(3.15rem,7vw,6.5rem)] leading-[0.95] text-fg">
            {content.title}
          </h1>
          <p className="mt-6 max-w-2xl text-base leading-7 text-fg/70 sm:text-lg sm:leading-8">{content.lead}</p>

          <div className="mt-10 flex flex-wrap gap-4">
            <Link
              className="inline-flex w-full items-center justify-center rounded-full bg-[linear-gradient(135deg,#8fd6f5,#8b7cf6)] px-5 py-3.5 text-sm font-semibold text-ink shadow-[0_0_36px_rgba(96,180,255,0.35)] transition-transform hover:-translate-y-0.5 sm:w-auto sm:px-7 sm:py-4 sm:text-base"
              href={`/${locale}/fa-chat`}
            >
              {content.primaryCta}
            </Link>
            <button
              className="inline-flex w-full items-center justify-center rounded-full border border-white/15 bg-white/5 px-5 py-3.5 text-sm font-medium text-fg transition-colors hover:border-cyan/40 hover:bg-cyan/10 sm:w-auto sm:px-7 sm:py-4 sm:text-base"
              onClick={onShowDemo}
              type="button"
            >
              {content.secondaryCta}
            </button>
          </div>

          <p className="mt-6 max-w-2xl text-sm leading-6 text-fg/55">{content.trustLine}</p>

          <div className="mt-10 grid gap-4 md:grid-cols-3">
            {content.workspaceLinks.map((link) => (
              <Link
                className="min-w-0 rounded-[1.5rem] border border-white/10 bg-white/[0.04] p-5 transition-colors hover:border-cyan/35 hover:bg-white/[0.06]"
                href={`/${locale}${link.href}`}
                key={link.href}
              >
                <p className="text-xs uppercase tracking-[0.24em] text-fg/45">{content.routeLabel}</p>
                <h2 className="mt-3 text-xl font-semibold text-fg">{link.label}</h2>
                <p className="mt-2 text-sm leading-6 text-fg/60">{link.description}</p>
              </Link>
            ))}
          </div>
        </div>

        <div className="flex items-center justify-center">
          <div
            className="relative flex h-[82vw] w-[82vw] max-h-[21rem] max-w-[21rem] items-center justify-center rounded-full sm:h-[27rem] sm:w-[27rem] sm:max-h-none sm:max-w-none"
            ref={orbRef}
          >
            <div
              className="absolute inset-[-2rem] animate-halo rounded-full"
              style={{ background: "radial-gradient(circle, rgba(110, 160, 255, 0.28), transparent 70%)" }}
            />
            <div
              className="absolute inset-0 animate-breathe rounded-full"
              style={{
                background:
                  "radial-gradient(circle at 36% 30%, rgba(210, 238, 255, 0.96), rgba(110, 170, 246, 0.88) 40%, rgba(88, 72, 214, 0.92) 75%, rgba(20, 18, 60, 0.98))",
                boxShadow: "0 0 68px rgba(100, 160, 255, 0.42), inset 0 0 44px rgba(255, 255, 255, 0.18)",
              }}
            />
            <div className="absolute inset-4 rounded-full border border-white/20 sm:inset-5" />
            <div
              className="absolute left-1/2 top-1/2 h-20 w-20 -translate-x-1/2 -translate-y-1/2 rounded-full transition-transform duration-300 sm:h-24 sm:w-24"
              ref={irisRef}
              style={{
                background: "radial-gradient(circle at 40% 35%, #fff, #bfe9ff 30%, #1b2a6e 75%)",
                boxShadow: "0 0 30px rgba(190, 230, 255, 0.82)",
              }}
            />
          </div>
        </div>
      </div>
    </section>
  );
}

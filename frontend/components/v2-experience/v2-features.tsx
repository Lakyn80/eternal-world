import type { V2ExperienceContent } from "../../lib/v2-experience/content";
import V2SectionHeading from "./v2-section-heading";

type V2FeaturesProps = {
  content: V2ExperienceContent["features"];
};

const iconGlows = [
  {
    background: "radial-gradient(circle at 35% 30%, #bfe9ff, #59a8f0 60%, #2a2a7a)",
    shadow: "rgba(89, 168, 240, 0.38)",
  },
  {
    background: "radial-gradient(circle at 35% 30%, #e4d4ff, #8b7cf6 60%, #3a2a7a)",
    shadow: "rgba(139, 124, 246, 0.36)",
  },
  {
    background: "radial-gradient(circle at 35% 30%, #ffe9c0, #e8c37a 60%, #7a5a2a)",
    shadow: "rgba(232, 195, 122, 0.34)",
  },
];

export default function V2Features({ content }: V2FeaturesProps) {
  return (
    <section className="scroll-mt-32 px-4 py-24 sm:px-6 lg:px-8" id="features">
      <div className="mx-auto max-w-7xl">
        <V2SectionHeading eyebrow={content.kicker} title={content.title} />

        <div className="mt-14 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {content.items.map((feature, index) => {
            const glow = iconGlows[index % iconGlows.length];
            return (
              <article
                className="rounded-[1.6rem] border border-white/8 bg-white/[0.035] p-6 transition-transform duration-300 hover:-translate-y-1 hover:border-cyan/32"
                key={feature.title}
              >
                <div
                  className="h-10 w-10 rounded-2xl"
                  style={{ background: glow.background, boxShadow: `0 0 26px ${glow.shadow}` }}
                />
                <h3 className="mt-5 text-xl font-semibold text-fg">{feature.title}</h3>
                <p className="mt-3 text-sm leading-7 text-fg/62">{feature.description}</p>
                <div className="mt-5 flex flex-wrap gap-2">
                  {feature.points.map((point) => (
                    <span
                      className="rounded-full border border-white/10 bg-white/[0.03] px-3 py-1 text-[11px] uppercase tracking-[0.18em] text-fg/52"
                      key={point}
                    >
                      {point}
                    </span>
                  ))}
                </div>
              </article>
            );
          })}
        </div>
      </div>
    </section>
  );
}

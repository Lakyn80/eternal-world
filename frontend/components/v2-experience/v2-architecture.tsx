import type { V2ExperienceContent } from "../../lib/v2-experience/content";
import V2SectionHeading from "./v2-section-heading";

type V2ArchitectureProps = {
  content: V2ExperienceContent["architecture"];
};

export default function V2Architecture({ content }: V2ArchitectureProps) {
  return (
    <section
      className="scroll-mt-32 px-4 py-24 sm:px-6 lg:px-8"
      id="architecture"
      style={{
        background: "radial-gradient(ellipse 70% 60% at 50% 50%, rgba(58, 54, 140, 0.14), transparent 72%)",
      }}
    >
      <div className="mx-auto max-w-7xl">
        <V2SectionHeading eyebrow={content.kicker} title={content.title} />

        <div className="mt-14 grid gap-4 md:grid-cols-2 xl:flex xl:flex-wrap xl:items-center xl:justify-center">
          {content.items.map((node, index) => (
            <div className="contents xl:flex xl:items-center" key={node.name}>
              <article
                className="rounded-[1.6rem] border border-white/12 bg-white/[0.04] px-6 py-5 backdrop-blur-sm animate-floaty xl:w-48"
                style={{ animationDelay: `${index * 0.4}s` }}
              >
                <h3 className="text-lg font-semibold text-fg">{node.name}</h3>
                <p className="mt-2 text-sm leading-6 text-fg/55">{node.detail}</p>
              </article>

              {index < content.items.length - 1 ? (
                <div
                  className="hidden h-px w-14 animate-flowlight xl:block"
                  style={{
                    background: "linear-gradient(90deg, transparent, #7fd8f7, #8b7cf6, transparent)",
                    backgroundSize: "200% 100%",
                  }}
                />
              ) : null}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

import { useEffect, useState } from "react";

import Link from "next/link";

import type { AppLocale } from "../../lib/i18n/locales";
import type { V2ExperienceContent } from "../../lib/v2-experience/content";
import V2MediaSlot from "./v2-media-slot";
import V2SectionHeading from "./v2-section-heading";

type V2TimelineProps = {
  locale: AppLocale;
  content: V2ExperienceContent["timeline"];
};

export default function V2Timeline({ locale, content }: V2TimelineProps) {
  const initialIndex = Math.max(0, content.items.length - 2);
  const [selectedIndex, setSelectedIndex] = useState(initialIndex);

  useEffect(() => {
    setSelectedIndex(initialIndex);
  }, [initialIndex]);

  const selectedItem = content.items[selectedIndex];

  return (
    <section className="scroll-mt-32 px-4 py-24 sm:px-6 lg:px-8" id="timeline">
      <div className="mx-auto max-w-7xl">
        <V2SectionHeading eyebrow={content.kicker} title={content.title} />

        <div className="relative mt-14 overflow-x-auto pb-3">
          <div className="relative min-w-max px-2">
            <div
              className="absolute left-0 right-0 top-[0.6rem] h-px"
              style={{
                background:
                  "linear-gradient(90deg, transparent, rgba(127, 216, 247, 0.38) 8%, rgba(139, 124, 246, 0.38) 92%, transparent)",
              }}
            />

            <div className="flex gap-4">
              {content.items.map((item, index) => {
                const active = index === selectedIndex;
                return (
                  <button
                    className="relative flex w-36 shrink-0 flex-col items-center gap-3 rounded-3xl bg-transparent px-2 pb-2 pt-0 text-center"
                    key={item.year}
                    onClick={() => setSelectedIndex(index)}
                    type="button"
                  >
                    <span
                      className="block rounded-full"
                      style={
                        active
                          ? {
                              width: 18,
                              height: 18,
                              background:
                                "radial-gradient(circle at 35% 30%, #fff, #e8c37a 56%, #7a5a2a)",
                              boxShadow: "0 0 24px rgba(232, 195, 122, 0.82)",
                            }
                          : {
                              width: 12,
                              height: 12,
                              marginTop: 3,
                              background:
                                "radial-gradient(circle at 35% 30%, #bfe9ff, #59a8f0 60%, #2a2a7a)",
                              boxShadow: "0 0 14px rgba(96, 180, 255, 0.56)",
                            }
                      }
                    />
                    <span className={`text-xl font-semibold ${active ? "text-gold" : "text-fg"}`}>{item.year}</span>
                    <span className="text-sm leading-6 text-fg/58">{item.title}</span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        <div className="mt-8 grid gap-6 lg:grid-cols-[minmax(0,20rem)_minmax(0,1fr)]">
          <V2MediaSlot
            actionLabel={content.actionLabel}
            badgeLabel={content.badgeLabel}
            body={selectedItem.slotBody}
            href="/family-memory-review"
            locale={locale}
            title={selectedItem.slotTitle}
          />

          <article className="rounded-[1.8rem] border border-white/10 bg-white/[0.04] p-6 sm:p-8">
            <div className="flex flex-wrap items-start justify-between gap-4">
              <div>
                <div className="font-serif text-[clamp(3rem,7vw,4.5rem)] leading-none text-gold">{selectedItem.year}</div>
                <h3 className="mt-2 text-2xl font-semibold text-fg">{selectedItem.title}</h3>
              </div>

              <Link
                className="inline-flex rounded-full border border-white/15 bg-white/5 px-4 py-2 text-sm text-fg/72 transition-colors hover:border-cyan/35 hover:text-fg"
                href={`/${locale}/family-memory-review`}
              >
                {content.actionLabel}
              </Link>
            </div>

            <p className="mt-5 max-w-3xl text-base leading-8 text-fg/65">{selectedItem.description}</p>

            <div className="mt-6 flex flex-wrap gap-2">
              {selectedItem.media.map((item) => (
                <span
                  className="rounded-full border border-cyan/24 bg-cyan/10 px-3 py-1 text-[11px] uppercase tracking-[0.18em] text-cyan"
                  key={item}
                >
                  {item}
                </span>
              ))}
            </div>
          </article>
        </div>
      </div>
    </section>
  );
}

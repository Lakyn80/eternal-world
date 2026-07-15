import type { AppLocale } from "../../lib/i18n/locales";
import type { V2ExperienceContent } from "../../lib/v2-experience/content";
import V2MediaSlot from "./v2-media-slot";
import V2SectionHeading from "./v2-section-heading";

type V2MomentsProps = {
  locale: AppLocale;
  content: V2ExperienceContent["moments"];
};

export default function V2Moments({ locale, content }: V2MomentsProps) {
  return (
    <section
      className="scroll-mt-32 px-4 py-24 sm:px-6 lg:px-8"
      id="moments"
      style={{
        background: "radial-gradient(ellipse 70% 50% at 50% 60%, rgba(120, 90, 40, 0.11), transparent 70%)",
      }}
    >
      <div className="mx-auto max-w-7xl">
        <V2SectionHeading accent="gold" eyebrow={content.kicker} title={content.title} />

        <div className="mt-14 grid gap-5 xl:grid-cols-3">
          {content.items.map((item) => (
            <article className="overflow-hidden rounded-[1.8rem] border border-white/10 bg-white/[0.035]" key={item.id}>
              <V2MediaSlot
                actionLabel={content.actionLabel}
                badgeLabel={content.badgeLabel}
                body={item.slotBody}
                className="rounded-b-none border-x-0 border-t-0"
                href="/fa-chat"
                locale={locale}
                title={item.slotTitle}
              />

              <div className="p-6">
                <div className="font-serif text-[1.6rem] leading-tight text-gold">{item.quote}</div>
                <p className="mt-4 text-sm leading-7 text-fg/62">{item.caption}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

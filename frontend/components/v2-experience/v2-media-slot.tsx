import Link from "next/link";

import type { AppLocale } from "../../lib/i18n/locales";

type V2MediaSlotProps = {
  locale: AppLocale;
  href: "/fa-chat" | "/family-memory-review" | "/presentation";
  badgeLabel: string;
  title: string;
  body: string;
  actionLabel: string;
  className?: string;
};

export default function V2MediaSlot({
  locale,
  href,
  badgeLabel,
  title,
  body,
  actionLabel,
  className = "",
}: V2MediaSlotProps) {
  return (
    <div
      className={`relative overflow-hidden rounded-[1.75rem] border border-white/10 bg-white/[0.04] ${className}`}
      style={{
        background:
          "radial-gradient(circle at 24% 18%, rgba(143, 214, 245, 0.18), transparent 42%), radial-gradient(circle at 80% 78%, rgba(139, 124, 246, 0.14), transparent 38%), rgba(255, 255, 255, 0.03)",
      }}
    >
      <div
        className="absolute inset-0 opacity-80"
        style={{
          backgroundImage:
            "repeating-linear-gradient(135deg, rgba(255,255,255,0.02) 0 10px, rgba(255,255,255,0.045) 10px 20px)",
        }}
      />
      <div className="relative flex h-full min-h-48 flex-col justify-between gap-6 p-6">
        <div>
          <div className="inline-flex rounded-full border border-cyan/25 bg-cyan/10 px-3 py-1 text-[11px] uppercase tracking-[0.2em] text-cyan">
            {badgeLabel}
          </div>
          <h3 className="mt-4 font-serif text-[1.6rem] leading-tight text-fg">{title}</h3>
          <p className="mt-3 text-sm leading-6 text-fg/65">{body}</p>
        </div>

        <Link
          className="inline-flex max-w-full items-center rounded-full border border-white/15 bg-white/5 px-4 py-2 text-center text-sm font-medium text-fg transition-colors hover:border-cyan/45 hover:bg-cyan/10"
          href={`/${locale}${href}`}
        >
          {actionLabel}
        </Link>
      </div>
    </div>
  );
}

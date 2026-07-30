type V2SectionHeadingProps = {
  eyebrow: string;
  title: string;
  description?: string;
  align?: "left" | "center";
  accent?: "cyan" | "gold";
};

const accentClassName: Record<NonNullable<V2SectionHeadingProps["accent"]>, string> = {
  cyan: "text-cyan",
  gold: "text-gold",
};

export default function V2SectionHeading({
  eyebrow,
  title,
  description,
  align = "center",
  accent = "cyan",
}: V2SectionHeadingProps) {
  return (
    <div className={align === "center" ? "mx-auto max-w-3xl text-center" : "max-w-3xl"}>
      <p className={`text-xs uppercase tracking-[0.32em] ${accentClassName[accent]}`}>{eyebrow}</p>
      <h2 className="mt-4 font-serif text-[clamp(2rem,4vw,3.5rem)] leading-[1.04] text-fg">{title}</h2>
      {description ? <p className="mt-4 text-base leading-7 text-fg/65 md:text-lg">{description}</p> : null}
    </div>
  );
}

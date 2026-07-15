import { useMemo, useState } from "react";

import Link from "next/link";

import type { AppLocale } from "../../lib/i18n/locales";
import type { V2ExperienceContent } from "../../lib/v2-experience/content";
import V2SectionHeading from "./v2-section-heading";

type V2AvatarStudioProps = {
  locale: AppLocale;
  content: V2ExperienceContent["studio"];
};

type ChipGroupProps = {
  label: string;
  options: string[];
  selectedIndex: number;
  onSelect: (index: number) => void;
};

function ChipGroup({ label, options, selectedIndex, onSelect }: ChipGroupProps) {
  return (
    <div>
      <div className="text-xs uppercase tracking-[0.22em] text-fg/45">{label}</div>
      <div className="mt-3 flex flex-wrap gap-2">
        {options.map((option, index) => (
          <button
            className={`rounded-full border px-4 py-2 text-sm transition-colors ${
              index === selectedIndex
                ? "border-cyan/45 bg-cyan/12 text-fg"
                : "border-white/12 bg-white/[0.04] text-fg/72 hover:border-cyan/28 hover:text-fg"
            }`}
            key={option}
            onClick={() => onSelect(index)}
            type="button"
          >
            {option}
          </button>
        ))}
      </div>
    </div>
  );
}

export default function V2AvatarStudio({ locale, content }: V2AvatarStudioProps) {
  const [voiceIndex, setVoiceIndex] = useState(0);
  const [temperamentIndex, setTemperamentIndex] = useState(0);
  const [languageIndex, setLanguageIndex] = useState(0);
  const [age, setAge] = useState(content.presets.defaultAge);

  const hueRotation = [0, 38, -42][temperamentIndex] + (age - content.presets.defaultAge) * 0.45;
  const summary = useMemo(
    () =>
      [
        content.presets.voices[voiceIndex],
        content.presets.temperaments[temperamentIndex],
        content.presets.languages[languageIndex],
        String(age),
      ].join(" · "),
    [age, content.presets.languages, content.presets.temperaments, content.presets.voices, languageIndex, temperamentIndex, voiceIndex]
  );

  return (
    <section className="scroll-mt-32 px-4 py-24 sm:px-6 lg:px-8" id="studio">
      <div className="mx-auto max-w-7xl">
        <V2SectionHeading
          description={content.lead}
          eyebrow={content.kicker}
          title={content.title}
        />

        <div className="mt-14 grid gap-6 xl:grid-cols-[minmax(0,24rem)_minmax(0,1fr)]">
          <article
            className="rounded-[1.5rem] border border-white/10 p-5 sm:rounded-[2rem] sm:p-8"
            style={{
              background:
                "radial-gradient(circle at 50% 30%, rgba(70, 90, 200, 0.22), transparent 70%), rgba(255, 255, 255, 0.03)",
            }}
          >
            <div className="flex flex-col items-center text-center">
              <div
                className="relative h-40 w-40 animate-breathe sm:h-52 sm:w-52"
                style={{ filter: `hue-rotate(${hueRotation}deg)` }}
              >
                <div
                  className="absolute inset-[-1.25rem] animate-halo rounded-full"
                  style={{ background: "radial-gradient(circle, rgba(110, 160, 255, 0.3), transparent 70%)" }}
                />
                <div
                  className="absolute inset-0 rounded-full"
                  style={{
                    background:
                      "radial-gradient(circle at 36% 30%, rgba(210, 238, 255, 0.95), rgba(110, 170, 246, 0.85) 40%, rgba(88, 72, 214, 0.9) 75%, rgba(20, 18, 60, 0.95))",
                    boxShadow: "0 0 44px rgba(100, 160, 255, 0.48)",
                  }}
                />
                <div className="absolute inset-4 rounded-full border border-white/22" />
              </div>

              <h3 className="mt-8 text-2xl font-semibold text-fg">{content.presets.previewName}</h3>
              <p className="mt-2 text-sm leading-6 text-fg/55">{summary}</p>
              <p className="mt-4 max-w-sm text-sm leading-6 text-fg/62">{content.presets.previewTagline}</p>

              <Link
                className="mt-8 inline-flex w-full items-center justify-center rounded-full bg-[linear-gradient(135deg,#8fd6f5,#8b7cf6)] px-5 py-3 text-sm font-semibold text-ink sm:w-auto"
                href={`/${locale}/fa-chat`}
              >
                {content.launchLabel}
              </Link>
            </div>
          </article>

          <article className="rounded-[1.5rem] border border-white/10 bg-white/[0.035] p-5 sm:rounded-[2rem] sm:p-8">
            <div className="space-y-7">
              <ChipGroup
                label={content.voiceLabel}
                onSelect={setVoiceIndex}
                options={content.presets.voices}
                selectedIndex={voiceIndex}
              />
              <ChipGroup
                label={content.temperamentLabel}
                onSelect={setTemperamentIndex}
                options={content.presets.temperaments}
                selectedIndex={temperamentIndex}
              />
              <ChipGroup
                label={content.languageLabel}
                onSelect={setLanguageIndex}
                options={content.presets.languages}
                selectedIndex={languageIndex}
              />

              <div>
                <div className="flex items-center justify-between gap-3">
                  <div className="text-xs uppercase tracking-[0.22em] text-fg/45">{content.ageLabel}</div>
                  <div className="text-lg font-semibold text-cyan">{age}</div>
                </div>
                <input
                  className="mt-4 w-full accent-cyan"
                  max={90}
                  min={30}
                  onChange={(event) => setAge(Number(event.target.value))}
                  type="range"
                  value={age}
                />
                <p className="mt-3 text-sm leading-6 text-fg/55">{content.ageHint}</p>
              </div>

              <div className="rounded-[1.5rem] border border-dashed border-white/12 bg-white/[0.03] p-5 text-sm leading-7 text-fg/58">
                {content.previewNote}
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>
  );
}

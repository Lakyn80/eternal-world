import { useState } from 'react';
import type { Lang } from '../i18n';
import { T, VOICES, PERSONALITIES, AVATAR_LANGS } from '../i18n';

function ChipRow({ options, value, onPick }: { options: string[]; value: number; onPick: (i: number) => void }) {
  return (
    <div className="flex gap-2 flex-wrap">
      {options.map((name, i) => (
        <button
          key={name}
          onClick={() => onPick(i)}
          className={`font-sans text-[13px] rounded-full px-4 py-2 border transition-colors ${
            i === value ? 'bg-cyan/[0.14] border-cyan/50 text-[#bfe9fa]' : 'bg-white/[0.04] border-white/[0.13] text-fg/70'
          }`}
        >
          {name}
        </button>
      ))}
    </div>
  );
}

export default function AvatarStudio({ lang }: { lang: Lang }) {
  const t = T[lang];
  const [voice, setVoice] = useState(0);
  const [pers, setPers] = useState(0);
  const [alang, setAlang] = useState(0);
  const [age, setAge] = useState(62);

  const hue = [0, 45, -50][pers] + (age - 62) * 0.4;
  const summary = `${VOICES[lang][voice]} · ${PERSONALITIES[lang][pers]} · ${AVATAR_LANGS[lang][alang]} · ${age}`;

  return (
    <section id="studio" className="py-24 px-6 max-w-[1100px] mx-auto">
      <div className="text-center mb-14">
        <div className="text-xs tracking-[.3em] uppercase text-cyan mb-3.5">{t.stKicker}</div>
        <h2 className="font-serif font-normal text-[clamp(30px,3.6vw,48px)] mb-2.5">{t.stTitle}</h2>
        <p className="mx-auto text-fg/60 font-light max-w-[50ch] leading-relaxed">{t.stSub}</p>
      </div>

      <div className="flex gap-6.5 flex-wrap">
        <div
          className="flex-1 min-w-[320px] flex flex-col items-center justify-center gap-6 p-11 bg-white/[0.03] border border-white/[0.09] rounded-3xl"
          style={{ background: 'radial-gradient(circle at 50% 38%, rgba(70,90,200,.22), transparent 72%), rgba(255,255,255,.03)' }}
        >
          <div
            className="relative w-[170px] h-[170px] animate-breathe transition-[filter] duration-500"
            style={{ filter: `hue-rotate(${hue}deg)` }}
          >
            <div
              className="absolute -inset-6 rounded-full animate-halo"
              style={{ background: 'radial-gradient(circle, rgba(110,160,255,.3), transparent 70%)' }}
            />
            <div
              className="absolute inset-0 rounded-full"
              style={{
                background:
                  'radial-gradient(circle at 36% 30%, rgba(210,238,255,.95), rgba(110,170,246,.85) 40%, rgba(88,72,214,.9) 75%, rgba(20,18,60,.95))',
                boxShadow: '0 0 44px rgba(100,160,255,.5)'
              }}
            />
            <div className="absolute inset-3 rounded-full border border-white/[0.22]" />
          </div>
          <div className="text-center">
            <div className="font-medium text-[16px]">Josef</div>
            <div className="text-[13px] text-fg/55 mt-1.5">{summary}</div>
          </div>
        </div>

        <div className="flex-[1_1_420px] flex flex-col gap-6.5 p-9 bg-white/[0.035] border border-white/[0.09] rounded-3xl backdrop-blur-md">
          <div className="flex flex-col gap-2.5">
            <div className="text-xs tracking-[.2em] uppercase text-fg/50">{t.stVoice}</div>
            <ChipRow options={VOICES[lang]} value={voice} onPick={setVoice} />
          </div>
          <div className="flex flex-col gap-2.5">
            <div className="text-xs tracking-[.2em] uppercase text-fg/50">{t.stPers}</div>
            <ChipRow options={PERSONALITIES[lang]} value={pers} onPick={setPers} />
          </div>
          <div className="flex flex-col gap-2.5">
            <div className="text-xs tracking-[.2em] uppercase text-fg/50">{t.stLang}</div>
            <ChipRow options={AVATAR_LANGS[lang]} value={alang} onPick={setAlang} />
          </div>
          <div className="flex flex-col gap-2.5">
            <div className="flex justify-between items-baseline">
              <div className="text-xs tracking-[.2em] uppercase text-fg/50">{t.stAge}</div>
              <div className="text-[15px] font-semibold text-cyan">{age}</div>
            </div>
            <input type="range" min={30} max={90} value={age} onChange={(e) => setAge(+e.target.value)} className="w-full" />
            <div className="text-xs text-fg/45">{t.stAgeHint}</div>
          </div>
        </div>
      </div>
    </section>
  );
}

import type { Lang } from '../i18n';
import { T } from '../i18n';

interface Props {
  lang: Lang;
  setLang: (l: Lang) => void;
  onGoHero: () => void;
  onGoStudio: () => void;
}

export default function Nav({ lang, setLang, onGoHero, onGoStudio }: Props) {
  const t = T[lang];
  const langBtn = (l: Lang) =>
    `font-sans text-xs font-medium rounded-full px-3 py-1.5 transition-colors ${
      lang === l ? 'bg-cyan/20 text-[#bfe9fa]' : 'text-fg/50 hover:text-fg/70'
    }`;

  return (
    <nav className="fixed top-0 inset-x-0 z-50 flex items-center justify-between px-9 py-3.5 bg-ink/55 backdrop-blur-xl border-b border-white/[0.06]">
      <div className="flex items-center gap-2.5 cursor-pointer" onClick={onGoHero}>
        <div
          className="w-[22px] h-[22px] rounded-full"
          style={{
            background: 'radial-gradient(circle at 35% 30%, #bfe9ff, #59a8f0 45%, #4f3ec9 90%)',
            boxShadow: '0 0 18px rgba(96,180,255,.6)'
          }}
        />
        <div className="font-semibold tracking-wide text-[15px]">
          Memorial World <span className="font-light text-fg/45 text-[13px]">· Věčný svět</span>
        </div>
      </div>
      <div className="flex items-center gap-4">
        <div className="flex gap-1 p-[3px] border border-white/[0.12] rounded-full">
          <button className={langBtn('en')} onClick={() => setLang('en')}>EN</button>
          <button className={langBtn('cs')} onClick={() => setLang('cs')}>CS</button>
          <button className={langBtn('ru')} onClick={() => setLang('ru')}>RU</button>
        </div>
        <button
          onClick={onGoStudio}
          className="font-sans text-[13px] font-medium text-ink rounded-full px-5 py-2.5 shadow-[0_0_26px_rgba(110,150,255,.35)]"
          style={{ background: 'linear-gradient(135deg,#8fd6f5,#8b7cf6)' }}
        >
          {t.navCta}
        </button>
      </div>
    </nav>
  );
}

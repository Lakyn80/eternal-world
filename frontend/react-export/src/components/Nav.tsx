import type { Lang } from '../i18n';
import { T } from '../i18n';

interface Props {
  lang: Lang;
  setLang: (l: Lang) => void;
  onGoHero: () => void;
  onGoMemorial: () => void;
  onGoStudio: () => void;
}

export default function Nav({ lang, setLang, onGoHero, onGoMemorial, onGoStudio }: Props) {
  const t = T[lang];
  const langBtn = (l: Lang) =>
    `font-sans text-xs font-medium rounded-full px-3 py-1.5 transition-colors ${
      lang === l ? 'bg-cyan/20 text-[#bfe9fa]' : 'text-fg/50 hover:text-fg/70'
    }`;

  return (
    <nav className="fixed top-0 inset-x-0 z-50 flex items-center justify-between gap-3 px-4 py-3 bg-ink/70 backdrop-blur-xl border-b border-white/[0.06] sm:px-6 lg:px-9">
      <div className="flex items-center gap-2.5 cursor-pointer" onClick={onGoHero}>
        <div
          className="h-[22px] w-[22px] shrink-0 rounded-full"
          style={{
            background: 'radial-gradient(circle at 35% 30%, #bfe9ff, #59a8f0 45%, #4f3ec9 90%)',
            boxShadow: '0 0 18px rgba(96,180,255,.6)'
          }}
        />
        <div className="min-w-0 truncate font-semibold tracking-wide text-[14px] sm:text-[15px]">
          Memorial World <span className="hidden font-light text-fg/45 text-[13px] sm:inline">· Věčný svět</span>
        </div>
      </div>
      <div className="flex min-w-0 items-center justify-end gap-2 sm:gap-4">
        <button
          onClick={onGoStudio}
          className="hidden rounded-full border border-white/[0.12] px-4 py-2 text-[13px] text-fg/65 transition hover:bg-white/10 md:block"
        >
          Studio
        </button>
        <div className="flex shrink-0 gap-1 p-[3px] border border-white/[0.12] rounded-full">
          <button className={langBtn('en')} onClick={() => setLang('en')}>EN</button>
          <button className={langBtn('cs')} onClick={() => setLang('cs')}>CS</button>
          <button className={langBtn('ru')} onClick={() => setLang('ru')}>RU</button>
        </div>
        <button
          onClick={onGoMemorial}
          className="shrink-0 font-sans text-[12px] font-medium text-ink rounded-full px-3 py-2.5 shadow-[0_0_26px_rgba(110,150,255,.35)] sm:px-5 sm:text-[13px]"
          style={{ background: 'linear-gradient(135deg,#8fd6f5,#8b7cf6)' }}
        >
          {t.navCta}
        </button>
      </div>
    </nav>
  );
}

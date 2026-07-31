import type { Lang } from '../i18n';
import { navigate } from '../lib/router';
import { updatePreferredUiLanguage } from '../lib/memorialApi';
import MemorialWorkspace from './MemorialWorkspace';

const LANGS: Lang[] = ['en', 'cs', 'ru'];

/**
 * The authenticated application shell (Task 65.1B). Deliberately mounts
 * only account/memorial-workspace UI - never the public marketing sections
 * (`ConversationDemo`, `AvatarStudio`, and their locale-scoped marketing
 * demo personas from `src/demo/` live exclusively in `App.tsx`'s public tree,
 * see that file's comment).
 */
export default function AuthenticatedApp({ lang, setLang }: { lang: Lang; setLang: (next: Lang) => void }) {
  const langButtonClassName = (candidate: Lang) =>
    `font-sans text-xs font-medium rounded-full px-3 py-1.5 transition-colors ${
      lang === candidate ? 'bg-cyan/20 text-[#bfe9ff]' : 'text-fg/50 hover:text-fg/70'
    }`;

  const onSetLang = (next: Lang) => {
    setLang(next);
    void updatePreferredUiLanguage('', next).catch(() => {
      // Cookie session may be absent on public shell; local preference still applies.
    });
  };

  return (
    <div className="min-h-screen bg-ink text-fg font-sans">
      <nav className="fixed top-0 inset-x-0 z-50 flex items-center justify-between gap-3 px-4 py-3 bg-ink/70 backdrop-blur-xl border-b border-white/[0.06] sm:px-6 lg:px-9">
        <button
          className="flex min-w-0 items-center gap-2.5"
          onClick={() => navigate('/')}
          type="button"
        >
          <div
            className="h-[22px] w-[22px] shrink-0 rounded-full"
            style={{
              background: 'radial-gradient(circle at 35% 30%, #bfe9ff, #59a8f0 45%, #4f3ec9 90%)',
              boxShadow: '0 0 18px rgba(96,180,255,.6)'
            }}
          />
          <span className="min-w-0 truncate font-semibold tracking-wide text-[14px] sm:text-[15px]">
            Memorial World <span className="hidden font-light text-fg/45 text-[13px] sm:inline">· Věčný svět</span>
          </span>
        </button>
        <div className="flex shrink-0 items-center gap-1 p-[3px] border border-white/[0.12] rounded-full">
          {LANGS.map((candidate) => (
            <button className={langButtonClassName(candidate)} key={candidate} onClick={() => onSetLang(candidate)} type="button">
              {candidate.toUpperCase()}
            </button>
          ))}
        </div>
      </nav>
      <main className="pt-16">
        <MemorialWorkspace lang={lang} setLang={onSetLang} />
      </main>
    </div>
  );
}

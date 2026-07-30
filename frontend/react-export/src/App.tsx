import { useCallback, useState } from 'react';
import type { Lang } from './i18n';
import Nav from './components/Nav';
import Hero from './components/Hero';
import ConversationDemo from './components/ConversationDemo';
import Features from './components/Features';
import Brain from './components/Brain';
import Timeline from './components/Timeline';
import AvatarStudio from './components/AvatarStudio';
import Moments from './components/Moments';
import Footer from './components/Footer';
import AuthenticatedApp from './components/AuthenticatedApp';
import { readStoredLang, writeStoredLang } from './lib/langPreference';
import { isAuthenticatedAppPath, navigate, usePathname } from './lib/router';

const scrollTo = (id: string) => {
  const el = document.getElementById(id);
  if (el) window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 60, behavior: 'smooth' });
};

/**
 * Task 65.1B route boundary: the public marketing page (this component,
 * everything below) and the authenticated application (`AuthenticatedApp`)
 * are two structurally separate trees. The public tree may keep the static
 * `ConversationDemo`/`AvatarStudio` demo sections (locale-scoped marketing
 * personas from `src/demo/`) - that content is legitimate marketing copy.
 * The authenticated tree never mounts those components at all, so an
 * authenticated user never sees the homepage demo persona inside their own
 * memorial workspace (Task 65.1A's root-cause finding).
 */
export default function App() {
  // Restore the last explicit EN/CS/RU choice across reloads. Default remains
  // English only when nothing valid is stored yet.
  const [lang, setLangState] = useState<Lang>(() => readStoredLang());
  const setLang = useCallback((next: Lang) => {
    writeStoredLang(next);
    setLangState(next);
  }, []);
  const pathname = usePathname();

  if (isAuthenticatedAppPath(pathname)) {
    return <AuthenticatedApp lang={lang} setLang={setLang} />;
  }

  return (
    <div className="min-h-screen bg-ink text-fg font-sans">
      <Nav lang={lang} setLang={setLang} onGoHero={() => scrollTo('hero')} onGoMemorial={() => navigate('/app')} onGoStudio={() => scrollTo('studio')} />
      <Hero lang={lang} onGoStudio={() => navigate('/app')} onGoDemo={() => scrollTo('demo')} particles />
      <ConversationDemo lang={lang} autoplay />
      <Features lang={lang} />
      <Brain lang={lang} />
      <Timeline lang={lang} />
      <AvatarStudio lang={lang} />
      <Moments lang={lang} />
      <Footer lang={lang} onGoStudio={() => navigate('/app')} />
    </div>
  );
}

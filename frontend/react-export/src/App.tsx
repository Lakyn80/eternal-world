import { useCallback, useEffect, useRef, useState } from 'react';
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
import CookieConsent from './components/CookieConsent';
import CzechLegalPage from './components/CzechLegalPage';
import { clearStoredLang, readStoredLang, writeStoredLang } from './lib/langPreference';
import { disableOptionalPwaStorage, registerServiceWorker } from './lib/pwa';
import {
  clearFunctionalBrowserStorage,
  COOKIE_CONSENT_STORAGE_KEY,
  isFunctionalStorageAllowed,
  readCookieConsent,
  type CookieConsentRecord
} from './lib/privacyConsent';
import { isAuthenticatedAppPath, navigate, parseCzechLegalPath, usePathname } from './lib/router';

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
  const [cookieConsent, setCookieConsent] = useState<CookieConsentRecord | null>(() => readCookieConsent());
  const setLang = useCallback((next: Lang) => {
    if (next === 'cs' && !cookieConsent?.categories.functional) {
      clearStoredLang();
    } else {
      writeStoredLang(next);
    }
    setLangState(next);
  }, [cookieConsent]);
  const pathname = usePathname();
  const legalPage = parseCzechLegalPath(pathname);
  const consentLang: Lang = legalPage ? 'cs' : lang;
  const functionalStorageAllowed = isFunctionalStorageAllowed(consentLang, cookieConsent);
  const functionalStorageAllowedRef = useRef(functionalStorageAllowed);
  functionalStorageAllowedRef.current = functionalStorageAllowed;

  useEffect(() => {
    if (functionalStorageAllowed) {
      void registerServiceWorker()
        .then((registration) => {
          if (!functionalStorageAllowedRef.current && registration) void disableOptionalPwaStorage();
        })
        .catch(() => {
          // Offline support is optional and must never block the application.
        });
    } else {
      void (lang === 'cs' ? clearFunctionalBrowserStorage() : disableOptionalPwaStorage());
    }
  }, [functionalStorageAllowed, lang]);

  useEffect(() => {
    const syncConsentAcrossTabs = (event: StorageEvent) => {
      if (event.key !== COOKIE_CONSENT_STORAGE_KEY) return;
      const next = readCookieConsent();
      setCookieConsent(next);
      if (lang === 'cs' && next?.categories.functional) writeStoredLang('cs');
    };
    window.addEventListener('storage', syncConsentAcrossTabs);
    return () => window.removeEventListener('storage', syncConsentAcrossTabs);
  }, [lang]);

  const onConsentChange = useCallback((next: CookieConsentRecord) => {
    setCookieConsent(next);
    if (lang === 'cs' && next.categories.functional) writeStoredLang('cs');
  }, [lang]);

  let content;

  if (legalPage) {
    content = <CzechLegalPage kind={legalPage} />;
  } else if (isAuthenticatedAppPath(pathname)) {
    content = (
      <AuthenticatedApp
        functionalStorageAllowed={functionalStorageAllowed}
        lang={lang}
        setLang={setLang}
      />
    );
  } else {
    content = (
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

  return (
    <>
      {content}
      <CookieConsent consent={cookieConsent} lang={consentLang} onConsentChange={onConsentChange} />
    </>
  );
}

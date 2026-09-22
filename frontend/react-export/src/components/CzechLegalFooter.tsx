import { openCookieSettings } from '../lib/privacyConsent';
import { CZECH_COOKIES_PATH, CZECH_PRIVACY_PATH } from '../lib/router';

export default function CzechLegalFooter({ compact = false }: { compact?: boolean }) {
  return (
    <footer className={`${compact ? 'px-5 py-6' : 'pt-6.5'} border-t border-white/[0.07] text-xs text-fg/55`}>
      <div className="mx-auto flex max-w-[1100px] flex-col items-center justify-between gap-4 text-center lg:flex-row lg:text-left">
        <div>© 2026 Eternal World</div>
        <nav aria-label="Právní informace" className="flex flex-wrap items-center justify-center gap-x-5 gap-y-2">
          <a className="text-fg/60 transition hover:text-fg" href={CZECH_PRIVACY_PATH}>
            Zásady ochrany osobních údajů
          </a>
          <a className="text-fg/60 transition hover:text-fg" href={CZECH_COOKIES_PATH}>
            Cookies
          </a>
          <button
            className="text-fg/60 transition hover:text-fg"
            onClick={openCookieSettings}
            type="button"
          >
            Nastavení cookies
          </button>
        </nav>
        <div>
          Vytvořila{' '}
          <a
            className="text-fg/70 transition hover:text-fg"
            href="https://lukiora.com"
            rel="noopener noreferrer"
            target="_blank"
          >
            Lukiora.com
          </a>
        </div>
      </div>
    </footer>
  );
}

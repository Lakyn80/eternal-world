import { useEffect, useRef, useState } from 'react';
import type { Lang } from '../i18n';
import {
  applyCookieConsent,
  OPEN_COOKIE_SETTINGS_EVENT,
  type CookieConsentRecord
} from '../lib/privacyConsent';
import { CZECH_COOKIES_PATH, CZECH_PRIVACY_PATH } from '../lib/router';

type Props = {
  lang: Lang;
  consent: CookieConsentRecord | null;
  onConsentChange: (next: CookieConsentRecord) => void;
};

const choiceButtonClass =
  'min-h-11 rounded-md border border-white/25 bg-white/[0.08] px-5 py-2.5 text-sm font-medium text-fg transition hover:border-cyan/60 hover:bg-cyan/10 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-cyan disabled:cursor-wait disabled:opacity-60';

export default function CookieConsent({ lang, consent, onConsentChange }: Props) {
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [functional, setFunctional] = useState(consent?.categories.functional ?? false);
  const [busy, setBusy] = useState(false);
  const dialogRef = useRef<HTMLDivElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    const openSettings = () => {
      setFunctional(consent?.categories.functional ?? false);
      setSettingsOpen(true);
    };
    window.addEventListener(OPEN_COOKIE_SETTINGS_EVENT, openSettings);
    return () => window.removeEventListener(OPEN_COOKIE_SETTINGS_EVENT, openSettings);
  }, [consent]);

  useEffect(() => {
    if (!settingsOpen) return;
    previousFocusRef.current = document.activeElement as HTMLElement | null;
    const firstControl = dialogRef.current?.querySelector<HTMLElement>('button, input, a[href]');
    firstControl?.focus();
    return () => previousFocusRef.current?.focus();
  }, [settingsOpen]);

  if (lang !== 'cs') return null;

  const choose = async (allowFunctional: boolean) => {
    setBusy(true);
    try {
      const next = await applyCookieConsent(allowFunctional);
      onConsentChange(next);
      setSettingsOpen(false);
    } finally {
      setBusy(false);
    }
  };

  const onDialogKeyDown = (event: React.KeyboardEvent<HTMLDivElement>) => {
    if (event.key === 'Escape') {
      event.preventDefault();
      setSettingsOpen(false);
      return;
    }
    if (event.key !== 'Tab' || !dialogRef.current) return;
    const controls = Array.from(
      dialogRef.current.querySelectorAll<HTMLElement>('button:not(:disabled), input:not(:disabled), a[href]')
    );
    if (controls.length === 0) return;
    const first = controls[0];
    const last = controls[controls.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  };

  return (
    <>
      {!consent && !settingsOpen && (
        <section
          aria-labelledby="cookie-consent-title"
          aria-live="polite"
          className="fixed inset-x-3 bottom-3 z-[80] mx-auto max-h-[calc(100vh-1.5rem)] max-w-[980px] overflow-y-auto rounded-md border border-white/20 bg-[#111521]/[0.98] p-5 shadow-2xl backdrop-blur-xl sm:p-6"
          role="dialog"
        >
          <div className="grid items-end gap-5 lg:grid-cols-[1fr_auto]">
            <div>
              <h2 className="font-serif text-2xl" id="cookie-consent-title">Vaše soukromí a nastavení webu</h2>
              <p className="mt-2 max-w-[68ch] text-sm leading-6 text-fg/75">
                Nezbytné úložiště používáme pro přihlášení a zapamatování této volby. Se souhlasem můžeme navíc
                uložit jazyk, rozepsané odpovědi a veřejnou offline část aplikace. Analytické ani marketingové
                cookies nepoužíváme.
              </p>
              <div className="mt-2 flex gap-4 text-xs">
                <a href={CZECH_PRIVACY_PATH}>Ochrana osobních údajů</a>
                <a href={CZECH_COOKIES_PATH}>Podrobnosti o cookies</a>
              </div>
            </div>
            <div className="grid gap-2 sm:grid-cols-3 lg:w-[510px]">
              <button className={choiceButtonClass} disabled={busy} onClick={() => void choose(true)} type="button">
                Přijmout vše
              </button>
              <button className={choiceButtonClass} disabled={busy} onClick={() => void choose(false)} type="button">
                Odmítnout volitelné
              </button>
              <button className={choiceButtonClass} disabled={busy} onClick={() => setSettingsOpen(true)} type="button">
                Nastavit
              </button>
            </div>
          </div>
        </section>
      )}

      {settingsOpen && (
        <div className="fixed inset-0 z-[90] flex items-center justify-center bg-black/70 p-3 sm:p-6">
          <div
            aria-describedby="cookie-settings-description"
            aria-labelledby="cookie-settings-title"
            aria-modal="true"
            className="max-h-[calc(100vh-1.5rem)] w-full max-w-[680px] overflow-y-auto rounded-md border border-white/20 bg-[#111521] p-5 shadow-2xl sm:p-7"
            onKeyDown={onDialogKeyDown}
            ref={dialogRef}
            role="dialog"
          >
            <div className="flex items-start justify-between gap-5">
              <div>
                <h2 className="font-serif text-3xl" id="cookie-settings-title">Nastavení cookies</h2>
                <p className="mt-2 text-sm leading-6 text-fg/65" id="cookie-settings-description">
                  Volitelné ukládání je ve výchozím stavu vypnuté. Volbu můžete kdykoli změnit v patičce.
                </p>
              </div>
              <button
                aria-label="Zavřít nastavení cookies"
                className="shrink-0 text-sm text-fg/65 hover:text-fg"
                onClick={() => setSettingsOpen(false)}
                type="button"
              >
                Zavřít
              </button>
            </div>

            <div className="mt-7 divide-y divide-white/10 border-y border-white/10">
              <label className="flex cursor-not-allowed items-start justify-between gap-5 py-5">
                <span>
                  <span className="block font-medium">Nezbytné</span>
                  <span className="mt-1 block text-sm leading-6 text-fg/60">
                    Přihlášení, zabezpečení relace a záznam vaší volby. Bez této kategorie služba nemůže fungovat.
                  </span>
                </span>
                <span className="flex shrink-0 items-center gap-2 text-xs text-fg/60">
                  Vždy aktivní
                  <input aria-label="Nezbytné cookies, vždy aktivní" checked disabled readOnly type="checkbox" />
                </span>
              </label>
              <label className="flex cursor-pointer items-start justify-between gap-5 py-5">
                <span>
                  <span className="block font-medium">Funkční</span>
                  <span className="mt-1 block text-sm leading-6 text-fg/60">
                    Zapamatují český jazyk, lokálně uchovají rozepsané texty a povolí veřejnou offline cache.
                  </span>
                </span>
                <input
                  aria-label="Povolit funkční úložiště"
                  checked={functional}
                  className="mt-1 h-5 w-5 shrink-0 accent-cyan"
                  onChange={(event) => setFunctional(event.target.checked)}
                  type="checkbox"
                />
              </label>
            </div>

            <div className="mt-6 flex flex-col gap-2 sm:flex-row sm:justify-end">
              <button className={choiceButtonClass} disabled={busy} onClick={() => void choose(false)} type="button">
                Odmítnout volitelné
              </button>
              <button className={choiceButtonClass} disabled={busy} onClick={() => void choose(functional)} type="button">
                Uložit nastavení
              </button>
            </div>
            <p className="mt-5 text-xs leading-5 text-fg/50">
              Přehled všech používaných identifikátorů, dob uložení a poskytovatelů najdete na stránce{' '}
              <a href={CZECH_COOKIES_PATH}>Cookies</a>.
            </p>
          </div>
        </div>
      )}
    </>
  );
}

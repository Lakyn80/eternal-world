/**
 * Privacy-safe PWA helpers (Task 65.13.9).
 * Never stores tokens, cookies, or memorial payloads.
 */

export const EW_PWA_UPDATE_AVAILABLE_EVENT = 'ew-pwa-update-available';

export type BeforeInstallPromptLike = Event & {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
};

let deferredInstallPrompt: BeforeInstallPromptLike | null = null;
let installListenerBound = false;

export function isStandaloneDisplay(): boolean {
  if (typeof window === 'undefined') return false;
  const media = window.matchMedia?.('(display-mode: standalone)')?.matches;
  const iosStandalone = Boolean((window.navigator as Navigator & { standalone?: boolean }).standalone);
  return Boolean(media || iosStandalone);
}

export function bindInstallPromptListener(): void {
  if (typeof window === 'undefined' || installListenerBound) return;
  installListenerBound = true;
  window.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    deferredInstallPrompt = event as BeforeInstallPromptLike;
  });
  window.addEventListener('appinstalled', () => {
    deferredInstallPrompt = null;
  });
}

export function canPromptInstall(): boolean {
  return deferredInstallPrompt !== null && !isStandaloneDisplay();
}

export async function requestPwaInstall(): Promise<'accepted' | 'dismissed' | 'unavailable'> {
  if (!deferredInstallPrompt) return 'unavailable';
  const promptEvent = deferredInstallPrompt;
  deferredInstallPrompt = null;
  await promptEvent.prompt();
  const choice = await promptEvent.userChoice;
  return choice.outcome;
}

export function shouldRegisterServiceWorker(env: { PROD?: boolean; MODE?: string } = import.meta.env): boolean {
  return Boolean(env.PROD);
}

export async function registerServiceWorker(): Promise<ServiceWorkerRegistration | null> {
  if (typeof window === 'undefined' || !('serviceWorker' in navigator)) return null;
  if (!shouldRegisterServiceWorker()) return null;
  const registration = await navigator.serviceWorker.register('/sw.js', { scope: '/' });
  if (registration.waiting) {
    window.dispatchEvent(new CustomEvent(EW_PWA_UPDATE_AVAILABLE_EVENT));
  }
  registration.addEventListener('updatefound', () => {
    const worker = registration.installing;
    if (!worker) return;
    worker.addEventListener('statechange', () => {
      if (worker.state === 'installed' && navigator.serviceWorker.controller) {
        window.dispatchEvent(new CustomEvent(EW_PWA_UPDATE_AVAILABLE_EVENT));
      }
    });
  });
  return registration;
}

/** Privacy-safe shell-cache cleanup. Does NOT revoke server sessions/JWTs. */
export async function notifyServiceWorkerLogoutCleanup(): Promise<void> {
  if (typeof window === 'undefined' || !('serviceWorker' in navigator)) return;
  const registration = await navigator.serviceWorker.getRegistration();
  registration?.active?.postMessage({ type: 'EW_PWA_CLEAR_SHELL_CACHE' });
}

export async function applyWaitingServiceWorkerUpdate(): Promise<void> {
  if (typeof window === 'undefined' || !('serviceWorker' in navigator)) return;
  const registration = await navigator.serviceWorker.getRegistration();
  registration?.waiting?.postMessage({ type: 'EW_PWA_SKIP_WAITING' });
}

/** Pure helpers exported for unit tests (mirror sw.js policy). */
export function pwaMustNeverCacheUrl(pathname: string): boolean {
  return pathname === '/api' || pathname.startsWith('/api/');
}

export function pwaMayCachePublicAsset(pathname: string): boolean {
  if (pwaMustNeverCacheUrl(pathname)) return false;
  if (pathname.startsWith('/assets/')) return true;
  if (pathname.startsWith('/icons/')) return true;
  return pathname === '/manifest.webmanifest' || pathname === '/offline.html';
}

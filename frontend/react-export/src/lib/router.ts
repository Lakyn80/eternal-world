import { useSyncExternalStore } from 'react';

/**
 * Minimal, explicit History-API router. This app has no route boundary at
 * all today (see MemorialWorkspace.tsx history) and does not currently use
 * URL-based locale routing, so pulling in a full router dependency for two
 * top-level route trees (public marketing vs. authenticated app) is not
 * justified - this is the smallest thing that gives Task 65.1B a real,
 * URL-addressable boundary between them, subscribed via `useSyncExternalStore`
 * so route changes (including back/forward) re-render consistently.
 */

type Listener = () => void;

const listeners = new Set<Listener>();

function emitChange(): void {
  for (const listener of listeners) listener();
}

function subscribe(listener: Listener): () => void {
  listeners.add(listener);
  window.addEventListener('popstate', listener);
  return () => {
    listeners.delete(listener);
    window.removeEventListener('popstate', listener);
  };
}

function getSnapshot(): string {
  return window.location.pathname;
}

export function navigate(path: string): void {
  if (window.location.pathname === path) return;
  window.history.pushState({}, '', path);
  emitChange();
}

export function replace(path: string): void {
  if (window.location.pathname === path) return;
  window.history.replaceState({}, '', path);
  emitChange();
}

export function usePathname(): string {
  return useSyncExternalStore(subscribe, getSnapshot, () => '/');
}

const APP_ROOT = '/app';

export type AppRoute =
  | { name: 'public' }
  | { name: 'app-root' }
  | { name: 'app-memorial'; profileId: number }
  | { name: 'app-invitations-accept' };

export function isAuthenticatedAppPath(pathname: string): boolean {
  return (
    pathname === APP_ROOT ||
    pathname.startsWith(`${APP_ROOT}/`) ||
    // The backend issues invitation accept links as a bare
    // `/invitations/accept?token=...` path (see
    // memorial_access.router._build_invitation_response). Treating that
    // exact bare path as an authenticated-app route too keeps those
    // existing backend-generated links working without requiring a
    // backend change, which is out of scope for this task.
    pathname === '/invitations/accept'
  );
}

export function parseAppRoute(pathname: string): AppRoute {
  if (pathname === '/invitations/accept') {
    return { name: 'app-invitations-accept' };
  }
  if (pathname !== APP_ROOT && !pathname.startsWith(`${APP_ROOT}/`)) {
    return { name: 'public' };
  }
  const rest = pathname.slice(APP_ROOT.length).replace(/\/+$/, '');
  if (rest === '' || rest === '/memorials') {
    return { name: 'app-root' };
  }
  if (rest === '/invitations/accept') {
    return { name: 'app-invitations-accept' };
  }
  const memorialMatch = rest.match(/^\/memorials\/(\d+)$/);
  if (memorialMatch) {
    const profileId = Number(memorialMatch[1]);
    if (Number.isInteger(profileId) && profileId > 0) {
      return { name: 'app-memorial', profileId };
    }
  }
  // An unrecognized /app/... path is still "the app", not the marketing
  // site - fall back to the app root (memorial list/onboarding) rather than
  // silently rendering public marketing content under an /app URL.
  return { name: 'app-root' };
}

export function buildMemorialPath(profileId: number): string {
  return `${APP_ROOT}/memorials/${profileId}`;
}

export const APP_ROOT_PATH = APP_ROOT;

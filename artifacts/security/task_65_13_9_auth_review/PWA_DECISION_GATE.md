# PWA_DECISION_GATE — Task 65.13.9 Part I

1. Framework/build: Vite 5.3 + React 18 (`frontend/react-export`); production Docker builds this app only.
2. Manifest status: none before this task.
3. Service worker status: none before this task.
4. Credential storage: in-memory bearer after login; HttpOnly Redis session cookie; UI lang in localStorage only.
5. API paths: `/api/**` same-origin in production (`VITE_API_URL` empty).
6. Private-data persistence: no IndexedDB/private caches; React state only for memorial payloads.
7. Logout cleanup: clears React state + `POST /api/auth/logout` (Redis+cookie); JWT not denylisted.
8. Icons/branding: no prior assets; generated solid-color PNG icons under `public/icons/`.
9. Offline behavior: none before this task.
10. Update behavior: none before this task.
11. SW↔auth interaction: SW must never read storage/tokens; must bypass `/api` and Authorization.
12. Expected PWA files: manifest, sw.js, offline.html, icons, `src/lib/pwa.ts`, index.html/main.tsx hooks, tests.
13. Expected tests: `src/lib/pwa.test.ts` (+ existing auth FE tests unchanged in behavior).

## DECISION C
Add a new PWA foundation using the existing Vite frontend build architecture (no vite-plugin-pwa dependency; native `public/` assets + manual SW).

No authentication production behavior changes. No critical auth blocker prevents a privacy-safe shell-only PWA.

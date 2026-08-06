/* Eternal World PWA service worker — Task 65.13.9
 * Versioned app-shell cache only. NEVER cache /api or credentialed private data.
 */
const EW_PWA_VERSION = 'ew-pwa-v1';
const APP_SHELL_CACHE = `eternal-world-shell-${EW_PWA_VERSION}`;

/** Explicit allowlist prefixes/paths for cacheable public assets only. */
const CACHEABLE_PATH_PREFIXES = [
  '/assets/',
  '/icons/',
];
const CACHEABLE_EXACT_PATHS = new Set([
  '/manifest.webmanifest',
  '/offline.html',
  '/icons/favicon-32.png',
]);

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(APP_SHELL_CACHE).then((cache) => cache.addAll(['/offline.html', '/manifest.webmanifest']))
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(
        keys
          .filter((key) => key.startsWith('eternal-world-shell-') && key !== APP_SHELL_CACHE)
          .map((key) => caches.delete(key))
      );
      await self.clients.claim();
    })()
  );
});

function isApiRequest(url) {
  return url.pathname === '/api' || url.pathname.startsWith('/api/');
}

function hasAuthorizationHeader(request) {
  return request.headers.has('Authorization') || request.headers.has('authorization');
}

function isCacheableAsset(url) {
  if (CACHEABLE_EXACT_PATHS.has(url.pathname)) return true;
  return CACHEABLE_PATH_PREFIXES.some((prefix) => url.pathname.startsWith(prefix));
}

function shouldBypassCache(request, url) {
  if (request.method !== 'GET') return true;
  if (isApiRequest(url)) return true;
  if (hasAuthorizationHeader(request)) return true;
  if (request.cache === 'no-store') return true;
  if (url.searchParams.has('token')) return true;
  return false;
}

self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  if (url.origin !== self.location.origin) {
    return;
  }

  if (shouldBypassCache(request, url)) {
    event.respondWith(fetch(request));
    return;
  }

  if (request.mode === 'navigate') {
    event.respondWith(
      (async () => {
        try {
          return await fetch(request);
        } catch (_err) {
          const cache = await caches.open(APP_SHELL_CACHE);
          const offline = await cache.match('/offline.html');
          return offline || new Response('Connection required', { status: 503, headers: { 'Content-Type': 'text/plain' } });
        }
      })()
    );
    return;
  }

  if (!isCacheableAsset(url)) {
    event.respondWith(fetch(request));
    return;
  }

  event.respondWith(
    (async () => {
      const cache = await caches.open(APP_SHELL_CACHE);
      const cached = await cache.match(request);
      if (cached) return cached;
      const response = await fetch(request);
      const cacheControl = response.headers.get('Cache-Control') || '';
      if (response.ok && !cacheControl.includes('no-store')) {
        await cache.put(request, response.clone());
      }
      return response;
    })()
  );
});

self.addEventListener('message', (event) => {
  const data = event.data || {};
  if (data.type === 'EW_PWA_SKIP_WAITING') {
    self.skipWaiting();
    return;
  }
  if (data.type === 'EW_PWA_CLEAR_SHELL_CACHE') {
    event.waitUntil(
      (async () => {
        const keys = await caches.keys();
        await Promise.all(keys.filter((k) => k.startsWith('eternal-world-shell-')).map((k) => caches.delete(k)));
      })()
    );
  }
});

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';
import {
  canPromptInstall,
  isStandaloneDisplay,
  pwaMayCachePublicAsset,
  pwaMustNeverCacheUrl,
  shouldRegisterServiceWorker
} from './pwa';

const here = dirname(fileURLToPath(import.meta.url));
const publicDir = join(here, '../../public');

describe('PWA privacy-safe foundation (Task 65.13.9)', () => {
  it('links a manifest with required installability fields', () => {
    const html = readFileSync(join(here, '../../index.html'), 'utf8');
    expect(html).toContain('rel="manifest"');
    expect(html).toContain('/manifest.webmanifest');

    const manifest = JSON.parse(readFileSync(join(publicDir, 'manifest.webmanifest'), 'utf8')) as {
      name: string;
      short_name: string;
      start_url: string;
      scope: string;
      display: string;
      icons: Array<{ src: string; sizes: string; purpose?: string }>;
    };
    expect(manifest.name).toBe('Eternal World');
    expect(manifest.short_name).toBe('Eternal World');
    expect(manifest.start_url).toBe('/app');
    expect(manifest.scope).toBe('/');
    expect(manifest.display).toBe('standalone');
    expect(manifest.icons.some((i) => i.sizes === '192x192')).toBe(true);
    expect(manifest.icons.some((i) => i.sizes === '512x512')).toBe(true);
    expect(manifest.icons.some((i) => i.purpose === 'maskable')).toBe(true);
  });

  it('ships required icon files declared by the manifest', () => {
    for (const name of ['icon-192.png', 'icon-512.png', 'icon-maskable-512.png', 'apple-touch-icon.png', 'favicon-32.png']) {
      const bytes = readFileSync(join(publicDir, 'icons', name));
      expect(bytes.subarray(0, 8).toString('binary')).toBe('\x89PNG\r\n\x1a\n');
    }
  });

  it('registers the service worker only in production builds', () => {
    expect(shouldRegisterServiceWorker({ PROD: true })).toBe(true);
    expect(shouldRegisterServiceWorker({ PROD: false })).toBe(false);
    expect(shouldRegisterServiceWorker({ MODE: 'development' })).toBe(false);
  });

  it('never caches API, auth, or private route prefixes', () => {
    for (const path of [
      '/api/auth/login',
      '/api/auth/register',
      '/api/auth/logout',
      '/api/auth/session',
      '/api/memorials',
      '/api/memorials/1/chat',
      '/api/invitations/accept',
      '/api/health/runtime'
    ]) {
      expect(pwaMustNeverCacheUrl(path)).toBe(true);
      expect(pwaMayCachePublicAsset(path)).toBe(false);
    }
  });

  it('may cache only public shell assets', () => {
    expect(pwaMayCachePublicAsset('/assets/index-abc123.js')).toBe(true);
    expect(pwaMayCachePublicAsset('/icons/icon-192.png')).toBe(true);
    expect(pwaMayCachePublicAsset('/manifest.webmanifest')).toBe(true);
    expect(pwaMayCachePublicAsset('/offline.html')).toBe(true);
    expect(pwaMayCachePublicAsset('/app')).toBe(false);
  });

  it('service worker source encodes deny rules for /api and Authorization', () => {
    const sw = readFileSync(join(publicDir, 'sw.js'), 'utf8');
    expect(sw).toContain("pathname.startsWith('/api/')");
    expect(sw).toContain('Authorization');
    expect(sw).toContain("request.method !== 'GET'");
    expect(sw).toContain('no-store');
    expect(sw).toContain('EW_PWA_CLEAR_SHELL_CACHE');
    expect(sw).not.toMatch(/localStorage|sessionStorage|access_token|refresh_token/i);
  });

  it('offline page is privacy-safe and does not claim memorial access', () => {
    const offline = readFileSync(join(publicDir, 'offline.html'), 'utf8');
    expect(offline.toLowerCase()).toContain('connection required');
    expect(offline.toLowerCase()).not.toContain('memorial content available offline');
    expect(offline).not.toMatch(/access_token|Authorization|Bearer/i);
  });

  it('install helpers do not nag when already standalone or prompt missing', () => {
    expect(canPromptInstall()).toBe(false);
    expect(typeof isStandaloneDisplay()).toBe('boolean');
  });
});

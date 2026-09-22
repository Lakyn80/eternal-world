import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  timeout: 120_000,
  retries: 0,
  use: {
    headless: true,
    baseURL: process.env.E2E_APP_URL ?? 'http://127.0.0.1:8017',
    trace: 'on-first-retry'
  }
});

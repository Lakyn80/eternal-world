import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/setupTests.ts'],
    globals: true,
    css: false,
    // Playwright specs live under e2e/ and must not be collected by Vitest.
    exclude: ['**/node_modules/**', '**/dist/**', '**/e2e/**']
  }
});

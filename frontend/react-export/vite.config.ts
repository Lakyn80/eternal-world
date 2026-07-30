import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  // Staging serves this app behind nginx with Host: eternalworld.lukiora.ru.
  // Vite preview (used by Dockerfile.prod) rejects unknown Host headers with
  // plain 403 unless listed here — that is what broke Deploy Staging public
  // healthchecks after the image rebuild.
  preview: {
    host: '0.0.0.0',
    port: 3000,
    // Explicit staging domain + lukiora.ru suffix. Must ship inside the
    // production image (see Dockerfile.prod COPY of vite.config.ts).
    allowedHosts: ['eternalworld.lukiora.ru', '.lukiora.ru'],
  },
});

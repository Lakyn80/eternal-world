# Memorial World — React + TypeScript + Tailwind

Full implementation of the Memorial World landing page, converted from the HTML/DC prototype into a real Vite + React + TypeScript + Tailwind app.

## Setup

```bash
cd react-export
npm install
npm run dev
```

Open the printed localhost URL. `npm run build` produces a production build.

## Structure

- `src/App.tsx` — page composition, language state, scroll-to helpers.
- `src/i18n.ts` — all copy (EN/CS/RU), typed dictionaries for features, timeline events, avatar-studio options, and the chat reply-matcher.
- `src/components/` — one component per section: `Nav`, `Hero` (particle canvas + eye-tracking orb), `ConversationDemo` (typeable fake chat), `Features`, `Brain`, `Timeline` (interactive, clickable events), `AvatarStudio` (voice/personality/language chips + age slider), `Moments`, `Footer`.
- `src/components/ImageSlot.tsx` — placeholder drop target for family photos; wire `onDrop` up to your real upload/asset pipeline.
- `src/hooks/useParticles.ts` — canvas particle background used in the hero.

## Notes / TODO for a real backend

- The conversation demo's AI replies are pattern-matched from a small hardcoded dictionary (`matchReply` in `i18n.ts`) — swap this for a real API call to your AI backend.
- `ImageSlot` is a static placeholder — hook it to real file upload / family archive storage.
- No routing library is included; everything is a single scrolling page. Add React Router if you split into multiple routes (e.g. a real `/studio` or `/conversation` app view).
- Pricing section was intentionally deferred per the original design brief.
- Tailwind config extends the palette (`ink`, `fg`, `cyan`, `violet`, `gold`) and keyframes (`breathe`, `halo`, `wavebar`, `flowlight`, `floaty`, `fadein`) used throughout — check `tailwind.config.js`.

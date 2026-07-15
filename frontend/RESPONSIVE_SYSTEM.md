# Responsive Frontend System

The frontend uses shared design tokens in `styles/tokens.css` and shared layout primitives in `styles/layout.css`.

Core rules:

- Use `var(--ew-page-gutter)` and `width: min(calc(100vw - (2 * var(--ew-page-gutter))), var(--ew-content-wide))` for page-level containers.
- Use `minmax(0, 1fr)`, `min-width: 0`, and `max-width: 100%` for grid children that can contain long localized copy.
- Collapse two-column product layouts at or before `1100px`; mobile-specific stacking starts at `720px` or `640px`.
- Buttons and form controls must be at least `2.75rem` high and become full-width on narrow mobile when they appear in rows.
- Decorative glow/orb layers may be clipped by their local container, but content, controls, cards, and route shells must not create root horizontal scroll.

Verification:

```bash
cd frontend
npm run typecheck
npm test
npm run build
npm run test:e2e
```

To run the same responsive checks against production after deployment:

```bash
cd frontend
$env:PLAYWRIGHT_BASE_URL = "https://eternalworld.lukiora.ru"
npm run test:e2e
Remove-Item Env:\PLAYWRIGHT_BASE_URL
```

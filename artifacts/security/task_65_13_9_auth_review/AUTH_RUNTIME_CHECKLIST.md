# AUTH_RUNTIME_CHECKLIST — cannot be proven by static review alone

Starting SHA: `df5fd85e7a9ecce980c1494ada665fa9d4229df8`

Verify in each production environment (Russia + Hetzner) before public launch:

1. TLS certificates valid; HSTS considered.
2. `BROWSER_SESSION_COOKIE_SECURE=true` behind HTTPS.
3. `BROWSER_SESSION_COOKIE_DOMAIN` empty or correctly scoped (prefer host-only).
4. `BACKEND_CORS_ORIGINS` exact allowlist matching the public origin(s).
5. `JWT_SECRET_KEY` unique, high entropy, not default `unsafe-dev-jwt-secret-change-me`.
6. Postgres/Redis not exposed on public interfaces.
7. Nginx does not forward unexpected `X-Forwarded-*` from clients without trust.
8. Rate limiting at Nginx/WAF or app layer for `/api/auth/login` and `/api/auth/register`.
9. Application logs redaction for Authorization and cookies.
10. Backup encryption and access control for Postgres dumps.
11. Secret rotation procedure documented and tested.
12. Email provider (when added) SPF/DKIM/DMARC and template injection review.
13. Independent penetration test after Task 65.13.10 remediations.
14. PWA: installed standalone still requires online auth; DevTools Application→Cache shows no `/api` entries after browsing authenticated pages.
15. Confirm demo `/api/demo/**` routes are not relied upon in production UX.

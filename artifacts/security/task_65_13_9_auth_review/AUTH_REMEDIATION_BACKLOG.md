# AUTH_REMEDIATION_BACKLOG — provisional (Task 65.13.9)

No authentication production code was modified in 65.13.9. Implement after CodeRabbit in **Task 65.13.10**.

## P0 Critical
- Enable `BROWSER_SESSION_COOKIE_SECURE=true` in HTTPS production envs (Russia + Hetzner).
- Add rate limiting / abuse controls for `/api/auth/login` and `/api/auth/register` (and invitation accept).
- Do not launch public self-serve accounts without password-reset **or** an explicit product decision + compensating controls.

## P1 High
- Reduce registration email enumeration (anti-enumeration responses / timing).
- Email verification before trusting account for sensitive memorial operations.
- JWT invalidation strategy on logout/password change (denylist/version or stop returning long-lived bearer to browsers).
- Logout-all-devices (enumerate/revoke Redis sessions per user).
- CSRF defense for cookie-authenticated state-changing requests (or stricter SameSite/header checks).
- Ensure demo `/api/demo/**` actor-impersonation cannot be reached in production deployments.
- Breached-password checks on register/password change.

## P2 Medium
- Explicit bcrypt cost configuration and rehash-on-login.
- `__Host-` cookie prefix where compatible.
- Invitation accept rate limits; avoid returning raw tokens in production responses (email-only delivery).
- Authentication audit events (success/failure) without high-cardinality PII labels.
- Design User model extensions for WebAuthn/passkeys + recovery codes.

## P3 Defense-in-depth
- CSP on frontend responses.
- Absolute session max lifetime in addition to sliding TTL.
- Step-up authentication for membership role changes / account email change.

## Runtime verification
- See `AUTH_RUNTIME_CHECKLIST.md` for both production hosts.

## Independent penetration testing
- Required before public production launch after 65.13.10 remediations land.

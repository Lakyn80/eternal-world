# AUTH_THREAT_MODEL — Task 65.13.9

Starting SHA: `df5fd85e7a9ecce980c1494ada665fa9d4229df8`  
Scope: evidence-based; controls not present are marked missing.

| Threat | Asset | Attacker | Entry | Current control | Missing | L | I | Evidence | Remediation task |
|---|---|---|---|---|---|---|---|---|---|
| Account enumeration | User emails | Internet | POST /register 409 | Login uses generic errors | Register reveals existence | M | M | auth.service DuplicateEmailError | 65.13.10 |
| Password spraying / brute force | Credentials | Internet | POST /login | bcrypt verify; generic errors | No rate limit/lockout/CAPTCHA | H | H | No limiter in routers/middleware | 65.13.10 |
| Credential stuffing | Accounts | Botnet | /login | Same as above | No breached-password check; no MFA | H | H | No HaveIBeenPwned/MFA | 65.13.10 |
| Stolen access JWT | API access | XSS/theft | Bearer header | Short TTL 30m; FE keeps JWT in memory only | No denylist; logout does not kill JWT | M | H | security.create_access_token; logout only Redis | 65.13.10 |
| Stolen browser session cookie | Session | Network/XSS-less theft | Cookie | HttpOnly; Redis revoke on logout; rotation on login | Secure default false; no __Host-; no absolute lifetime beyond Redis TTL | M | H | auth.router cookie flags; config default | 65.13.10 + runtime |
| XSS token theft | In-memory JWT | XSS | JS memory | Prefer cookie path after restore (empty bearer) | CSP not proven in FE; JWT still issued to JS on login | M | H | memorialApi login stores token in state | 65.13.10 |
| CSRF | Cookie session | Evil site | credentialed POST | SameSite=Lax | No CSRF token; credentials:include always | M | H | router samesite=lax; memorialApi credentials | 65.13.10 |
| Session fixation | Session | Attacker cookie plant | /login | rotate_browser_session on login | — | L | M | browser_session.rotate | maintain |
| Refresh reuse | Refresh token | N/A | N/A | N/A — no refresh tokens | Refresh design when added | — | — | inventory | design in 65.13.10 |
| Password-reset abuse | Account | Internet | N/A | Feature absent | Safe reset flow needed before public launch | H | H | no endpoints | 65.13.10 |
| Email-verification abuse | Account | Internet | N/A | Feature absent | Verify-before-trust for sensitive ops | H | H | register activates immediately | 65.13.10 |
| Invitation theft/replay | Membership | Email interceptor | accept token | sha256 store; single-use; expiry; email bind | Raw token in API response (dev); no rate limit on accept | M | H | memorial_access.service | 65.13.10 |
| Unauthorized memorial access / BOLA | Memorial data | Auth user | /api/memorials/{id}/* | resolve_authorized_profile 404/403 | Legacy demo actor query path | L | H | capabilities.py; family_memory_enrichment demo | keep demo isolated; pen-test |
| Role escalation | Capabilities | Member | APIs | Role matrix server-side | Mass-assignment review on patch schemas | L | H | capabilities + schemas | 65.13.10 review |
| Cross-profile leakage | Chat/RAG | Member | chat/RAG | membership + per-user chat isolation tests | Continuous regression | L | H | test_memorial_capabilities | maintain |
| Compromised email | Account recovery | Attacker inbox | future reset | N/A | MFA/passkeys; notify old email | H | H | no MFA | later |
| Compromised device | Session | Physical | browser | Logout revokes Redis session | Logout-all; JWT linger | M | H | logout path | 65.13.10 |
| Malicious family member | Memorial | Insider role | member APIs | Role capabilities | Step-up for destructive ops | M | H | role matrix | product+65.13.10 |
| Secret leakage | JWT secret | Misconfig | env/logs | SecretStr in settings | Runtime secret rotation evidence | M | C | config.py | runtime checklist |
| PWA cache leakage | Private data | Shared device | SW cache | Deny /api/** + auth headers; offline shell only | Must keep allowlist strict | M | H | public/sw.js contract | maintain + tests |
| Shared-device logout failure | Session | Next user | browser | Logout clears cookie+Redis+FE state | User education; auto-lock | M | H | logout flows | UX |

Likelihood/Impact: L/M/H/C qualitative for prioritization, not a formal FAIR score.

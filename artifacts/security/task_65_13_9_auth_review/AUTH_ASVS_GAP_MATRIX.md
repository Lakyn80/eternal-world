# AUTH_ASVS_GAP_MATRIX — OWASP ASVS 5.0.0 oriented (Task 65.13.9)

This is an evidence matrix for review, **not** a claim of ASVS certification.

Legend: PASS | PARTIAL | FAIL | N/A | UNVERIFIED

## Passwords
| Control | Status | Evidence | Severity |
|---|---|---|---|
| Hashing algorithm bcrypt | PASS | `security.py` CryptContext schemes=["bcrypt"] | — |
| Unique salt | PASS | bcrypt via Passlib | — |
| Work factor explicit | PARTIAL | No rounds configured; library default | P2 |
| Min length ≥8 | PASS | RegisterRequest validator | — |
| Max length / bcrypt 72-byte cap | PASS | rejects >72 UTF-8 bytes | — |
| Breached-password detection | FAIL | absent | P1 |
| Transparent rehash | PARTIAL | deprecated="auto" but no verify+upgrade path observed | P3 |
| Password not logged | PASS (static) | no logging of password fields found in auth service | UNVERIFIED runtime |

## Registration / Login
| Control | Status | Evidence | Severity |
|---|---|---|---|
| Email normalization | PASS | strip+lower | — |
| Email verification | FAIL | immediate active account | P1 |
| Duplicate enumeration | FAIL | HTTP 409 explicit | P1 |
| Generic login errors | PASS | InvalidCredentialsError message | — |
| Rate limiting / lockout | FAIL | none on /login /register | P0 |
| Disabled account handling | PASS | is_active checked | — |
| Timing hardening | PARTIAL | missing user short-circuits before verify | P2 |

## Tokens / Sessions
| Control | Status | Evidence | Severity |
|---|---|---|---|
| Access token lifetime | PASS | default 30 minutes | — |
| Refresh tokens | FAIL / N/A feature | not implemented | P1 product |
| JWT alg pinning | PASS | algorithms=[settings.jwt_algorithm] | — |
| iss/aud/iat/nbf/exp | PASS | create+decode | — |
| Session fixation defense | PASS | rotate on login | — |
| Session id entropy | PASS | token_urlsafe(32) | — |
| Logout revokes server session | PASS | Redis delete | — |
| Logout revokes JWT | FAIL | no denylist | P1 |
| Logout-all devices | FAIL | absent | P1 |
| Password-change invalidation | FAIL | no password-change endpoint | P1 |

## Cookies / CSRF / CORS
| Control | Status | Evidence | Severity |
|---|---|---|---|
| HttpOnly | PASS | set_cookie httponly=True | — |
| SameSite=Lax | PASS | hardcoded lax | — |
| Secure flag | PARTIAL | configurable; default False | P0 prod |
| __Host- cookie | FAIL | not used | P2 |
| CSRF token | FAIL | not present | P1 |
| CORS credentials + allowlist | PARTIAL | allow_credentials + explicit origins; must be correct in prod | UNVERIFIED runtime |
| Wildcard CORS | PASS (static) | list parser rejects non-list | — |

## Recovery / Invitations / AuthZ
| Control | Status | Evidence | Severity |
|---|---|---|---|
| Password recovery | FAIL | absent | P0 before public |
| Invitation hashed storage | PASS | sha256 | — |
| Invitation single-use/expiry/email bind | PASS | service checks | — |
| Invitation rate limit | FAIL | absent | P2 |
| Object-level memorial auth | PASS | resolve_authorized_profile | — |
| Frontend-only authZ rejected | PASS | backend enforced; FE tabs cosmetic | — |
| Demo unauthenticated actor path | FAIL (isolation risk) | family_memory_enrichment query actor | P1 keep off prod exposure |

## MFA / Passkeys readiness
| Control | Status | Evidence | Severity |
|---|---|---|---|
| Extensible authenticator model | FAIL | User model has password only | P2 design |
| WebAuthn tables/endpoints | FAIL | absent | expected later |
| Step-up auth | FAIL | absent | P2 |

## Counts (approx.)
- PASS: 18
- PARTIAL: 6
- FAIL: 14
- N/A: 1
- UNVERIFIED: 2

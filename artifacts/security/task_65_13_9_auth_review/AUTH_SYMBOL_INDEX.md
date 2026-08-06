# AUTH_SYMBOL_INDEX — Task 65.13.9

Starting SHA: `df5fd85e7a9ecce980c1494ada665fa9d4229df8`

## backend/app/core/security.py
- Symbols: `pwd_context`, `hash_password`, `verify_password`, `create_access_token`, `decode_access_token`, `validate_safe_lookup_value`
- Responsibility: bcrypt hashing (Passlib), JWT HS256 issue/validate with iss/aud/iat/nbf/exp
- Callers: `auth.service`, `auth.dependencies`, invitation token hashing elsewhere uses hashlib separately
- Tests: `tests/test_security.py`, `tests/test_auth.py`

## backend/app/modules/auth/service.py
- Symbols: `register_user`, `login_user`, `DuplicateEmailError`, `InvalidCredentialsError`
- Responsibility: email-normalized register/login; issues access JWT only
- Callers: `auth.router`
- Tests: `tests/test_auth.py`

## backend/app/modules/auth/router.py
- Symbols: `register`, `login`, `get_me`, `get_session`, `update_my_preferences`, `logout`, `_set_session_cookie`, `_clear_session_cookie`
- Responsibility: `/api/auth/*` HTTP surface; sets/clears HttpOnly session cookie on login/logout
- Callers: FastAPI app via `main.py`
- Tests: `tests/test_auth.py`, `tests/test_authenticated_workspace_reliability.py`

## backend/app/modules/auth/browser_session.py
- Symbols: `create_browser_session`, `resolve_browser_session`, `rotate_browser_session`, `revoke_browser_session`
- Responsibility: Redis opaque session ID, sliding TTL, fixation rotation on login
- Callers: `auth.router`, `auth.dependencies`
- Tests: `tests/test_authenticated_workspace_reliability.py`
- Data stores: Redis keys `eternal_world:auth:session:*`

## backend/app/modules/auth/dependencies.py
- Symbols: `get_current_user`
- Responsibility: Bearer JWT first, then cookie session; requires active user row
- Callers: nearly all protected routers
- Tests: auth + memorial capability suites

## backend/app/modules/memorial_access/capabilities.py
- Symbols: `MemorialCapability`, `resolve_authorized_profile`, role→capability matrix
- Responsibility: object-level memorial authorization; non-members get 404
- Callers: memorial/chat/RAG/biographer/persona routers
- Tests: `tests/test_memorial_capabilities.py`, `tests/test_memorial_access.py`

## backend/app/modules/memorial_access/service.py
- Symbols: invitation create/accept, contribution submit/review
- Responsibility: hashed invitation tokens, email binding, single-use/expiry, membership creation
- Tests: `tests/test_memorial_access.py`

## frontend/react-export/src/lib/memorialApi.ts
- Symbols: `login`, `register`, `getSession`, `logoutSession`, `requestJson`, `setUnauthorizedHandler`
- Responsibility: credentials:include; optional Bearer; relative `/api` in production
- Storage: no token persistence; only UI lang uses localStorage via `langPreference.ts`
- Tests: `memorialApi.test.ts`

## frontend/react-export/src/components/MemorialWorkspace.tsx
- Symbols: `AuthPanel`, `signOut`, in-memory `session`
- Responsibility: login/register UI; session memory; logout clears state + calls logout API
- Tests: `MemorialWorkspace.test.tsx`

## frontend/react-export/src/lib/pwa.ts (Task 65.13.9)
- Symbols: `registerServiceWorker`, `requestPwaInstall`, `notifyServiceWorkerLogoutCleanup`, installability helpers
- Responsibility: privacy-safe SW registration + install UX; never stores credentials
- Tests: `pwa.test.ts`

## Absent modules (confirmed missing)
- Refresh-token issuance/rotation
- Password-reset / forgot-password
- Email verification
- MFA / WebAuthn / passkeys
- HTTP auth rate limiting / lockout
- WebSocket/SSE authentication

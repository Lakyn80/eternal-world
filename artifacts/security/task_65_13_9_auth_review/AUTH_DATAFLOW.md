# AUTH_DATAFLOW — Task 65.13.9

Starting SHA: `df5fd85e7a9ecce980c1494ada665fa9d4229df8`

Trust boundaries: Browser ↔ Nginx TLS ↔ FastAPI ↔ PostgreSQL / Redis.

## 1. Registration
```
AuthPanel (FE)
→ POST /api/auth/register (memorialApi.register)
→ auth.router.register
→ RegisterRequest validators (email normalize, password 8..72 bytes)
→ auth.service.register_user
→ users_repository.get_user_by_email / create_user
→ security.hash_password (bcrypt)
→ PostgreSQL users row (is_active=true immediately)
→ UserRead JSON
→ FE immediately calls login with same credentials
```
Writes: Postgres user. No email verification. No Redis. Enumeration: 409 DuplicateEmailError.

## 2. Login
```
AuthPanel
→ POST /api/auth/login (credentials:include)
→ auth.service.login_user (generic InvalidCredentialsError)
→ security.verify_password + create_access_token (type=access, 30m default)
→ browser_session.rotate_browser_session (opaque token_urlsafe(32) → Redis TTL)
→ Set-Cookie HttpOnly SameSite=Lax Path=/ (+ Secure when configured)
→ TokenResponse {access_token} JSON
→ FE stores accessToken only in React useState (optional for subsequent calls)
```
Stores: Postgres read; Redis session write; cookie set. JWT not revoked on logout.

## 3. Access-token / session validation
```
Request
→ Depends(get_current_user)
→ If Authorization Bearer present: decode_access_token (alg/iss/aud/exp) → load User by sub
→ Else cookie eternal_world_session: resolve_browser_session (Redis + sliding expire) → load User
→ Require user.is_active
→ Else 401
```

## 4. Refresh
**NOT IMPLEMENTED.** No refresh token, no refresh endpoint, no rotation/reuse detection.
Browser path relies on sliding Redis session TTL (default 14 days). API clients rely on 30-minute JWT re-login.

## 5. Logout
```
signOut (FE) clears React state
→ POST /api/auth/logout (best-effort, no auth required)
→ revoke_browser_session (delete Redis key)
→ delete_cookie
→ FE navigate /app; optional SW cache cleanup message (PWA shell only)
```
JWT access tokens remain valid until exp (no denylist). No logout-all-devices.

## 6. Password reset
**NOT IMPLEMENTED.** No forgot/reset endpoints, tokens, or email flow.

## 7. Email verification
**NOT IMPLEMENTED.** Registration activates account immediately.

## 8. Invitation acceptance
```
Owner POST /api/memorials/{id}/invitations (MANAGE/invite capability)
→ service generates raw token; stores sha256(token); returns accept URL (dev/test)
→ Invitee registers/logs in
→ POST /api/invitations/accept {token}
→ hash lookup; email must match invitation email; not expired; not used
→ create membership; mark invitation accepted
→ FE reads ?token= from URL then history.replaceState removes it
```

## 9. Memorial authorization
```
Authenticated User
→ resolve_authorized_profile(db, user, profile_id, capability)
→ active membership row (or legacy owner self-heal)
→ missing membership → 404; missing capability → 403
→ resource handler
```
Frontend tabs are UX only; backend enforces.

## 10. WebSocket / SSE
**NOT PRESENT.** N/A.

## Error / abuse notes
- Login errors are generic ("Invalid email or password") — good.
- Registration duplicate returns explicit 409 — account enumeration.
- No login rate limit / lockout.
- CORS: configured origin list + allow_credentials=True.
- Demo FA enrichment routes accept query actor context without JWT — must stay non-production.

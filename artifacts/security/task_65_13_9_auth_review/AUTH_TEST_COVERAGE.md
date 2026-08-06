# AUTH_TEST_COVERAGE — Task 65.13.9

| Production path | Existing tests | Gap |
|---|---|---|
| Register success | test_auth.py | consent/version evidence |
| Duplicate email 409 | test_auth.py | anti-enumeration alternative UX |
| Login success + bearer /me | test_auth.py | — |
| Invalid credentials | test_auth.py | brute-force/rate-limit tests absent |
| Password hash/verify helpers | test_security.py | cost-factor assertion |
| JWT claims iss/aud/exp | test_security.py | key rotation tests absent |
| Browser cookie session create/resume/logout | test_authenticated_workspace_reliability.py | Secure flag prod assertion |
| Redis outage login still returns JWT | test_authenticated_workspace_reliability.py | — |
| Invitation lifecycle | test_memorial_access.py | accept rate-limit |
| Capability matrix / BOLA 404 | test_memorial_capabilities.py | continuous fuzz IDOR |
| Chat per-user isolation | test_memorial_capabilities / test_chat | — |
| FE login/register API client | memorialApi.test.ts | cookie-only restore E2E limited |
| FE logout | MemorialWorkspace tests (mocked) | SW cleanup after PWA |
| Password reset | none | feature missing |
| Email verification | none | feature missing |
| Refresh tokens | none | feature missing |
| MFA/passkeys | none | feature missing |
| Auth rate limiting | none | feature missing |
| PWA never caches /api | pwa.test.ts (Task 65.13.9) | Lighthouse installability optional |

Missing tests should be added in Task 65.13.10 alongside remediations, not as silent auth behavior changes here.

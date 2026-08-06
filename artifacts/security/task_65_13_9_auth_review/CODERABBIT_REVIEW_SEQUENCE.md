# CODERABBIT_REVIEW_SEQUENCE

1. Authentication primitives — `security.py`, `auth/schemas.py`, `auth/service.py`
2. Session/token lifecycle — `auth/router.py`, `browser_session.py`, `dependencies.py`
3. Resource authorization — `memorial_access/capabilities.py` + protected routers
4. Recovery/invitations — confirm recovery gaps; review invitation hashing/accept
5. Frontend credential handling — `memorialApi.ts`, `MemorialWorkspace.tsx`
6. Infrastructure — CORS in `main.py`/`config.py`, Nginx TLS/proxy, Compose ports
7. PWA boundaries — `sw.js` deny rules vs auth storage
8. Tests — map each P0/P1 to a missing or existing test

Stop if a finding implies PWA caching of credentials; escalate before merge of PWA changes.

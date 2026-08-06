# CODERABBIT_AUTH_REVIEW_PROMPT — Task 65.13.9

Copy-paste for CodeRabbit (or equivalent reviewer):

---

You are performing a focused authentication, session-management, and authorization review of Eternal World.

## Constraints
- Review **only** paths listed in `artifacts/security/task_65_13_9_auth_review/AUTH_REVIEW_FILE_SCOPE.txt` plus their direct imports required to understand control flow.
- Map findings to **OWASP ASVS 5.0.0** (Level 2 target; Level 3 where memorial/family data justifies).
- For every finding: exact file + line, exploit scenario, severity (P0–P3), false-positive likelihood, and whether proof is static vs runtime-only.
- **Never** output secrets, tokens, password hashes, cookie values, or `.env` contents.
- Distinguish production code from tests and demo routes.
- Frontend route guards are **not** authorization; reject FE-only access control.
- Do not propose rewriting the stack; prefer minimal safe remediations.
- Authentication production behavior must not be assumed fixed by PWA files; review PWA only for cache/credential boundaries.

## Required coverage
Registration; login; refresh (confirm absence); logout/revocation; recovery (confirm absence); email verification (confirm absence); invitations; roles/permissions/object-level memorial isolation; cookies/tokens/JWT; CSRF; CORS; rate limiting; WebSocket auth (confirm absence); PWA service-worker boundaries (`public/sw.js`, `src/lib/pwa.ts`).

## Inputs already prepared
- `AUTH_DATAFLOW.md`
- `AUTH_THREAT_MODEL.md`
- `AUTH_ASVS_GAP_MATRIX.md`
- `AUTH_TEST_COVERAGE.md`
- `AUTH_RUNTIME_CHECKLIST.md`

Validate, extend, or correct these documents with evidence. Do not invent controls that are not in code.

## Output format
1. Executive summary
2. Confirmed strengths
3. Findings table (ID, ASVS ref, severity, evidence, exploit, remediation)
4. Test gaps
5. Runtime verification still required
6. Explicit statement if any PWA change could weaken auth

---

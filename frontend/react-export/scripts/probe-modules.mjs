import { chromium } from 'playwright';

const API = 'http://127.0.0.1:8033';
const PASSWORD = 'StrongPass123!';
const stamp = Date.now();
const ownerEmail = `fix-owner-${stamp}@example.com`;
const inviteeEmail = `fix-invitee-${stamp}@example.com`;

await fetch(`${API}/api/auth/register`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: ownerEmail, password: PASSWORD, full_name: 'E2E' })
});
const ownerTok = (
  await (
    await fetch(`${API}/api/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: ownerEmail, password: PASSWORD })
    })
  ).json()
).access_token;
const mem = await (
  await fetch(`${API}/api/memorials`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${ownerTok}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: 'Fix',
      biography: 'b',
      canonical_language: 'cs',
      confirm_canonical_language: true
    })
  })
).json();
const inv = await (
  await fetch(`${API}/api/memorials/${mem.id}/invitations`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${ownerTok}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: inviteeEmail, role: 'contributor' })
  })
).json();

const browser = await chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage();
page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
page.on('console', (m) => {
  if (m.type() === 'error') console.log('CONSOLE_ERR', m.text());
});
await page.goto(inv.accept_url, { waitUntil: 'networkidle' });
await page.waitForTimeout(2000);

const info = await page.evaluate(async (token) => {
  const pending = await import('/src/lib/pendingInvitation.ts');
  const router = await import('/src/lib/router.ts');
  return {
    pathname: location.pathname,
    search: location.search,
    storage: sessionStorage.getItem(pending.PENDING_INVITATION_STORAGE_KEY),
    normalizeRaw: pending.normalizeInvitationToken(token),
    normalizeFromUrl: pending.normalizeInvitationToken(location.href.includes('token=') ? location.href : `http://x/?token=${token}`),
    route: router.parseAppRoute(location.pathname),
    isAuthPath: router.isAuthenticatedAppPath(location.pathname),
    bodyHasAccept: /Accept invitation|Přijmout pozvánku/i.test(document.body.innerText)
  };
}, inv.token);

console.log(JSON.stringify(info, null, 2));
await browser.close();

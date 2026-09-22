import { chromium } from 'playwright';

const API = 'http://127.0.0.1:8033';
const PASSWORD = 'StrongPass123!';
const KEY = 'eternal_world:pending_invitation';
const stamp = Date.now();
const ownerEmail = `probe-owner-${stamp}@example.com`;
const inviteeEmail = `probe-invitee-${stamp}@example.com`;

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
      name: 'Probe',
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
console.log('accept_url', inv.accept_url);
console.log('token', inv.token);

const browser = await chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage();
await page.goto(inv.accept_url, { waitUntil: 'networkidle' });
await page.waitForTimeout(2500);
const probe = await page.evaluate((key) => {
  const text = document.body.innerText;
  return {
    href: location.href,
    search: location.search,
    storage: sessionStorage.getItem(key),
    hasAcceptTitle: /Accept invitation|Přijmout pozvánku/i.test(text),
    hasPaste: /Paste invite|Vložte odkaz/i.test(text),
    hasSignIn: /Sign in to continue|Přihlaste se/i.test(text) || /SIGN IN TO CONTINUE/i.test(text)
  };
}, KEY);
console.log('probe', JSON.stringify(probe, null, 2));

// Force-set token via paste UI if present, else via evaluate storage + reload
if (!probe.hasAcceptTitle) {
  console.log('Accept panel missing — injecting token into sessionStorage and reloading');
  await page.evaluate(
    ({ key, token }) => {
      sessionStorage.setItem(key, JSON.stringify({ token }));
      location.href = '/invitations/accept';
    },
    { key: KEY, token: inv.token }
  );
  await page.waitForTimeout(3000);
  const probe2 = await page.evaluate((key) => {
    const text = document.body.innerText;
    return {
      href: location.href,
      storage: sessionStorage.getItem(key),
      hasAcceptTitle: /Accept invitation|Přijmout pozvánku/i.test(text),
      snippet: text.slice(0, 600)
    };
  }, KEY);
  console.log('probe2', JSON.stringify(probe2, null, 2));
}
await browser.close();

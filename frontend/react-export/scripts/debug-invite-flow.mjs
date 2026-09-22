import { chromium } from 'playwright';

const API = 'http://127.0.0.1:8033';
const PASSWORD = 'StrongPass123!';

async function register(email) {
  await fetch(`${API}/api/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password: PASSWORD, full_name: 'E2E' })
  });
  const login = await fetch(`${API}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password: PASSWORD })
  });
  return (await login.json()).access_token;
}

const stamp = Date.now();
const ownerEmail = `dbg-owner-${stamp}@example.com`;
const inviteeEmail = `dbg-invitee-${stamp}@example.com`;
const ownerTok = await register(ownerEmail);
const mem = await (
  await fetch(`${API}/api/memorials`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${ownerTok}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: 'Dbg',
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
console.log('url', inv.accept_url);

const browser = await chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage();
page.on('console', (m) => console.log('CONSOLE', m.type(), m.text()));
page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
page.on('response', (r) => {
  if (r.url().includes('/api/')) console.log('API', r.status(), r.request().method(), r.url());
});
await page.goto(inv.accept_url, { waitUntil: 'networkidle' });
for (const label of ['Přijmout vše', 'Accept all', 'Souhlasím', 'Pouze nezbytné', 'Only necessary']) {
  const b = page.getByRole('button', { name: new RegExp(label, 'i') });
  if ((await b.count()) > 0) {
    try {
      await b.first().click({ timeout: 2000 });
      console.log('clicked consent', label);
    } catch {
      /* ignore */
    }
  }
}
console.log('BODY1', (await page.locator('body').innerText()).slice(0, 1000));
const createTab = page.getByRole('button', { name: /Vytvořit účet|Create account/i });
console.log('createTab', await createTab.count());
if ((await createTab.count()) > 0) await createTab.first().click();
await page.locator('input[type="email"]').fill(inviteeEmail);
const texts = page.locator('input[type="text"]');
if ((await texts.count()) > 0) await texts.first().fill('Invitee');
await page.locator('input[type="password"]').fill(PASSWORD);
await page.locator('form button[type="submit"]').click();
await page.waitForTimeout(6000);
console.log('BODY2', (await page.locator('body').innerText()).slice(0, 1500));
console.log('url2', page.url());
await page.screenshot({ path: 'scripts/debug-invite.png', fullPage: true });
await browser.close();

import { chromium } from 'playwright';

const API = process.env.E2E_API_URL ?? 'http://127.0.0.1:8033';
const PASSWORD = 'StrongPass123!';

async function registerAndLogin(email) {
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
  if (!login.ok) throw new Error(`login failed ${login.status}`);
  return (await login.json()).access_token;
}

const stamp = Date.now();
const ownerEmail = `chrome-owner-${stamp}@example.com`;
const inviteeEmail = `chrome-invitee-${stamp}@example.com`;
const ownerToken = await registerAndLogin(ownerEmail);

const memorialRes = await fetch(`${API}/api/memorials`, {
  method: 'POST',
  headers: { Authorization: `Bearer ${ownerToken}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'Chrome Memorial',
    biography: 'bio',
    canonical_language: 'cs',
    confirm_canonical_language: true
  })
});
if (!memorialRes.ok) throw new Error(`memorial ${memorialRes.status}`);
const memorial = await memorialRes.json();

const inviteRes = await fetch(`${API}/api/memorials/${memorial.id}/invitations`, {
  method: 'POST',
  headers: { Authorization: `Bearer ${ownerToken}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: inviteeEmail, role: 'contributor' })
});
if (!inviteRes.ok) throw new Error(`invite ${inviteRes.status} ${await inviteRes.text()}`);
const invite = await inviteRes.json();
console.log('accept_url', invite.accept_url);

const browser = await chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage();
page.setDefaultTimeout(60_000);
page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
await page.goto(invite.accept_url, { waitUntil: 'networkidle' });
console.log('url_after_load', page.url());

await page.getByText(/Accept invitation|Přijmout pozvánku/i).first().waitFor();

const createTab = page.getByRole('button', { name: /Vytvořit účet|Create account/i });
if ((await createTab.count()) > 0) await createTab.first().click();
await page.locator('input[type="email"]').fill(inviteeEmail);
const texts = page.locator('input[type="text"]');
if ((await texts.count()) > 0) await texts.first().fill('Invitee');
await page.locator('input[type="password"]').fill(PASSWORD);
await page.locator('form').filter({ hasText: /Email/i }).getByRole('button', { name: /Create account|Vytvořit účet|Sign in|Přihlásit/i }).click();

const acceptBtn = page.getByRole('button', { name: /Přijmout pozvánku|Accept invitation/i });
await acceptBtn.waitFor();
await acceptBtn.click();
await page.getByText(/Pozvánka přijata|Invitation accepted/i).waitFor();
console.log('BROWSER_ACCEPT_OK');

const login2 = await fetch(`${API}/api/auth/login`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: inviteeEmail, password: PASSWORD })
});
const tok = (await login2.json()).access_token;
const members = await fetch(`${API}/api/memorials/${memorial.id}/members`, {
  headers: { Authorization: `Bearer ${ownerToken}` }
});
if (!members.ok) throw new Error(`members ${members.status} ${await members.text()}`);
const list = await members.json();
console.log(
  'members',
  JSON.stringify(list.map((m) => ({ email: m.email, role: m.role })))
);
if (!list.some((m) => m.email === inviteeEmail && m.role === 'contributor')) {
  throw new Error('membership missing after browser accept');
}
await browser.close();
console.log('PHYSICAL_E2E_PASSED');

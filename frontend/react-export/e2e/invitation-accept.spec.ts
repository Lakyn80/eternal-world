/**
 * Physical browser E2E: invite → open accept URL → register/login invitee → Accept.
 * Run: npx playwright test (from this folder after `npx playwright install chromium`)
 */
import { expect, test } from '@playwright/test';

const API = process.env.E2E_API_URL ?? 'http://127.0.0.1:8033';
const APP = process.env.E2E_APP_URL ?? 'http://127.0.0.1:8017';
const PASSWORD = 'StrongPass123!';

async function registerAndLogin(email: string): Promise<string> {
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
  expect(login.status).toBe(200);
  const body = (await login.json()) as { access_token: string };
  return body.access_token;
}

test('invitee can accept invitation via accept URL in the browser', async ({ page }) => {
  const stamp = Date.now();
  const ownerEmail = `pw-owner-${stamp}@example.com`;
  const inviteeEmail = `pw-invitee-${stamp}@example.com`;

  const ownerToken = await registerAndLogin(ownerEmail);
  const memorialRes = await fetch(`${API}/api/memorials`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${ownerToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: 'PW Memorial',
      biography: 'bio',
      canonical_language: 'cs',
      confirm_canonical_language: true
    })
  });
  expect(memorialRes.status).toBe(201);
  const memorial = (await memorialRes.json()) as { id: number };

  const inviteRes = await fetch(`${API}/api/memorials/${memorial.id}/invitations`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${ownerToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email: inviteeEmail, role: 'contributor' })
  });
  expect(inviteRes.status).toBe(201);
  const invite = (await inviteRes.json()) as { token: string; accept_url: string };
  expect(invite.token.length).toBeGreaterThanOrEqual(20);
  expect(invite.accept_url).toContain('/invitations/accept?token=');

  // Fresh browser context — no stale sessionStorage from prior attempts.
  await page.goto(invite.accept_url, { waitUntil: 'networkidle' });
  await expect(page.getByText(/Accept invitation|Přijmout pozvánku|Принять приглашение/i).first()).toBeVisible({
    timeout: 30_000
  });

  // Create account as the invited email (register tab).
  const createAccount = page.getByRole('button', { name: /Create account|Vytvořit účet|Создать аккаунт/i });
  if (await createAccount.isVisible()) {
    await createAccount.click();
  }
  await page.locator('input[type="email"]').fill(inviteeEmail);
  const nameField = page.locator('input[type="text"]').first();
  if (await nameField.isVisible()) {
    await nameField.fill('Invitee');
  }
  await page.locator('input[type="password"]').fill(PASSWORD);
  await page.getByRole('button', { name: /Create account|Vytvořit účet|Создать аккаунт|Sign in|Přihlásit|Войти/i }).last().click();

  const acceptBtn = page.getByRole('button', { name: /Accept invitation|Přijmout pozvánku|Принять приглашение/i });
  await expect(acceptBtn).toBeVisible({ timeout: 30_000 });
  await acceptBtn.click();

  await expect(page.getByText(/Invitation accepted|Pozvánka přijata|Приглашение принято/i)).toBeVisible({
    timeout: 30_000
  });

  // Verify membership via API.
  const inviteeLogin = await fetch(`${API}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: inviteeEmail, password: PASSWORD })
  });
  const inviteeTok = ((await inviteeLogin.json()) as { access_token: string }).access_token;
  const members = await fetch(`${API}/api/memorials/${memorial.id}/members`, {
    headers: { Authorization: `Bearer ${inviteeTok}` }
  });
  expect(members.status).toBe(200);
  const list = (await members.json()) as Array<{ email: string; role: string }>;
  expect(list.some((m) => m.email === inviteeEmail && m.role === 'contributor')).toBe(true);
});

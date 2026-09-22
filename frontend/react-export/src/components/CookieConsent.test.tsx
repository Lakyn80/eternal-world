import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import CookieConsent from './CookieConsent';
import CzechLegalPage from './CzechLegalPage';
import Footer from './Footer';
import { COOKIE_CONSENT_STORAGE_KEY, readCookieConsent, saveCookieConsent } from '../lib/privacyConsent';

describe('Czech consent experience', () => {
  beforeEach(() => {
    localStorage.clear();
    sessionStorage.clear();
    window.history.replaceState({}, '', '/');
    window.scrollTo = vi.fn();
  });

  it('shows equal first-layer choices on a first Czech visit', () => {
    render(<CookieConsent consent={null} lang="cs" onConsentChange={vi.fn()} />);

    const accept = screen.getByRole('button', { name: 'Přijmout vše' });
    const reject = screen.getByRole('button', { name: 'Odmítnout volitelné' });
    const settings = screen.getByRole('button', { name: 'Nastavit' });
    expect(accept.className).toBe(reject.className);
    expect(reject.className).toBe(settings.className);
  });

  it('does not render the Czech consent UI in the Russian branch', () => {
    render(<CookieConsent consent={null} lang="ru" onConsentChange={vi.fn()} />);

    expect(screen.queryByRole('button', { name: 'Přijmout vše' })).not.toBeInTheDocument();
  });

  it('accepts all categories and persists the active choice', async () => {
    const onChange = vi.fn();
    render(<CookieConsent consent={null} lang="cs" onConsentChange={onChange} />);

    await userEvent.click(screen.getByRole('button', { name: 'Přijmout vše' }));

    await waitFor(() => expect(onChange).toHaveBeenCalledOnce());
    expect(readCookieConsent()?.categories.functional).toBe(true);
  });

  it('rejects optional storage from the first layer', async () => {
    const onChange = vi.fn();
    render(<CookieConsent consent={null} lang="cs" onConsentChange={onChange} />);

    await userEvent.click(screen.getByRole('button', { name: 'Odmítnout volitelné' }));

    await waitFor(() => expect(onChange).toHaveBeenCalledOnce());
    expect(readCookieConsent()?.categories.functional).toBe(false);
  });

  it('opens detailed settings with functional storage disabled by default', async () => {
    render(<CookieConsent consent={null} lang="cs" onConsentChange={vi.fn()} />);

    await userEvent.click(screen.getByRole('button', { name: 'Nastavit' }));

    expect(screen.getByRole('checkbox', { name: 'Nezbytné cookies, vždy aktivní' })).toBeChecked();
    expect(screen.getByRole('checkbox', { name: 'Nezbytné cookies, vždy aktivní' })).toBeDisabled();
    expect(screen.getByRole('checkbox', { name: 'Povolit funkční úložiště' })).not.toBeChecked();
  });

  it('persists a custom functional choice', async () => {
    const onChange = vi.fn();
    render(<CookieConsent consent={null} lang="cs" onConsentChange={onChange} />);
    await userEvent.click(screen.getByRole('button', { name: 'Nastavit' }));
    await userEvent.click(screen.getByRole('checkbox', { name: 'Povolit funkční úložiště' }));

    await userEvent.click(screen.getByRole('button', { name: 'Uložit nastavení' }));

    await waitFor(() => expect(onChange).toHaveBeenCalledOnce());
    expect(readCookieConsent()?.categories.functional).toBe(true);
  });

  it('does not ask again after a valid stored decision is supplied on reload', () => {
    const stored = saveCookieConsent(false);
    render(<CookieConsent consent={stored} lang="cs" onConsentChange={vi.fn()} />);

    expect(screen.queryByRole('button', { name: 'Přijmout vše' })).not.toBeInTheDocument();
  });

  it('opens consent settings from the Czech footer after a prior decision', async () => {
    const stored = saveCookieConsent(true);
    render(
      <>
        <Footer lang="cs" onGoStudio={vi.fn()} />
        <CookieConsent consent={stored} lang="cs" onConsentChange={vi.fn()} />
      </>
    );

    await userEvent.click(screen.getByRole('button', { name: 'Nastavení cookies' }));

    expect(screen.getByRole('heading', { name: 'Nastavení cookies' })).toBeInTheDocument();
    expect(screen.getByRole('checkbox', { name: 'Povolit funkční úložiště' })).toBeChecked();
  });

  it('lets the user revoke a previously granted functional consent from the footer', async () => {
    const stored = saveCookieConsent(true);
    const onChange = vi.fn();
    localStorage.setItem('eternal-world.ui.lang', 'cs');
    sessionStorage.setItem('eternal_world:chat_draft:user:1', 'draft');
    render(
      <>
        <Footer lang="cs" onGoStudio={vi.fn()} />
        <CookieConsent consent={stored} lang="cs" onConsentChange={onChange} />
      </>
    );
    await userEvent.click(screen.getByRole('button', { name: 'Nastavení cookies' }));

    await userEvent.click(screen.getByRole('button', { name: 'Odmítnout volitelné' }));

    await waitFor(() => expect(onChange).toHaveBeenCalledOnce());
    expect(onChange.mock.calls[0][0].categories.functional).toBe(false);
    expect(localStorage.getItem('eternal-world.ui.lang')).toBeNull();
    expect(sessionStorage.getItem('eternal_world:chat_draft:user:1')).toBeNull();
  });

  it('renders Czech legal links and safe Lukiora attribution only in the Czech footer', () => {
    const { rerender } = render(<Footer lang="cs" onGoStudio={vi.fn()} />);

    expect(screen.getByRole('link', { name: 'Zásady ochrany osobních údajů' })).toHaveAttribute('href', '/cs/zasady-ochrany-osobnich-udaju');
    expect(screen.getByRole('link', { name: 'Cookies' })).toHaveAttribute('href', '/cs/cookies');
    expect(screen.getByRole('link', { name: 'Lukiora.com' })).toHaveAttribute('href', 'https://lukiora.com');
    expect(screen.getByRole('link', { name: 'Lukiora.com' })).toHaveAttribute('rel', 'noopener noreferrer');
    expect(screen.getByRole('link', { name: 'Lukiora.com' })).toHaveAttribute('target', '_blank');

    rerender(<Footer lang="ru" onGoStudio={vi.fn()} />);
    expect(screen.queryByRole('link', { name: 'Zásady ochrany osobních údajů' })).not.toBeInTheDocument();
  });

  it('provides the Czech privacy notice with explicit operator placeholders', () => {
    render(<CzechLegalPage kind="privacy" />);

    expect(screen.getByRole('heading', { name: 'Zásady ochrany osobních údajů' })).toBeInTheDocument();
    expect(screen.getByText(/Údaj musí provozovatel doplnit před zveřejněním/)).toBeInTheDocument();
    expect(screen.getByText(/DOPLNIT KONTAKT PRO OCHRANU OSOBNÍCH ÚDAJŮ/)).toBeInTheDocument();
  });

  it('lists only actual necessary and functional browser technologies', () => {
    render(<CzechLegalPage kind="cookies" />);

    expect(screen.getByText('eternal_world_session')).toBeInTheDocument();
    expect(screen.getByText('eternal-world.cookie-consent')).toBeInTheDocument();
    expect(screen.getByText('eternal-world.ui.lang')).toBeInTheDocument();
    expect(screen.getByText('eternal_world:chat_draft:*')).toBeInTheDocument();
    expect(screen.getByText('eternal_world:biographer_draft:*')).toBeInTheDocument();
    expect(screen.getByText('eternal-world-shell-*')).toBeInTheDocument();
  });

  it('does not initialize analytics before consent', () => {
    render(<CookieConsent consent={null} lang="cs" onConsentChange={vi.fn()} />);

    expect(document.querySelector('script[src*="google-analytics"], script[src*="googletagmanager"]')).toBeNull();
  });

  it('does not initialize marketing scripts before consent', () => {
    render(<CookieConsent consent={null} lang="cs" onConsentChange={vi.fn()} />);

    expect(document.querySelector('script[src*="facebook"], script[src*="connect.facebook"]')).toBeNull();
  });

  it('does not initialize analytics or marketing scripts after rejection', async () => {
    render(<CookieConsent consent={null} lang="cs" onConsentChange={vi.fn()} />);
    await userEvent.click(screen.getByRole('button', { name: 'Odmítnout volitelné' }));

    expect(document.querySelector('script[src*="google-analytics"], script[src*="googletagmanager"], script[src*="facebook"]')).toBeNull();
    expect(JSON.parse(localStorage.getItem(COOKIE_CONSENT_STORAGE_KEY) || '{}').categories.functional).toBe(false);
  });

  it('shows a new consent choice when the stored version is obsolete', () => {
    localStorage.setItem(COOKIE_CONSENT_STORAGE_KEY, JSON.stringify({
      version: 0,
      decidedAt: '2026-09-22T08:00:00.000Z',
      expiresAt: '2027-09-22T08:00:00.000Z',
      categories: { necessary: true, functional: true }
    }));

    render(<CookieConsent consent={readCookieConsent()} lang="cs" onConsentChange={vi.fn()} />);

    expect(screen.getByRole('button', { name: 'Přijmout vše' })).toBeInTheDocument();
  });
});

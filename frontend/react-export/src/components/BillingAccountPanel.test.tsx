import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { BillingAccountPanel } from './BillingAccountPanel';
import * as billingApi from '../lib/billingApi';
import type { BillingCatalogRead, BillingCurrentPlanRead, BillingPlanRead } from '../types/memorial';

vi.mock('../lib/billingApi', () => ({
  getBillingAccount: vi.fn(),
  getBillingPlans: vi.fn(),
  startCheckout: vi.fn()
}));

const t = {
  billing: 'Billing',
  billingCurrentPlan: 'Current plan',
  billingUsage: 'Current usage',
  billingMemorialsUsage: 'Memorials',
  billingMemoriesUsage: 'Memories',
  billingUnlimited: 'Unlimited',
  billingSubscriptionStatus: 'Subscription status',
  billingPeriodEnd: 'Current period ends',
  billingCancelAtPeriodEnd: 'Cancels at period end',
  billingViewPlans: 'View plans',
  billingPlansTitle: 'Available plans',
  billingUpgrade: 'Choose plan',
  billingCheckoutUnavailable: 'Paid checkout is not available yet. Your plan was not changed.',
  billingPerMonth: 'month',
  billingCurrency: 'Currency',
  billingPricePending: 'Price coming soon',
  working: 'Working'
};

const freeLimits = {
  max_profiles: 1,
  max_memories: 10,
  max_audio_minutes: 30,
  max_videos_per_month: 3,
  max_video_seconds: 30,
  allow_watermark_removal: false,
  allow_unlimited_chat: false,
  allow_priority_support: false,
  allow_family_members: false,
  allow_shared_memories: false,
  allow_family_tree: false,
  max_family_members: 0,
  max_video_quality: 'standard'
};

function plan(
  code: string,
  name: string,
  prices: BillingPlanRead['prices'],
  limits = freeLimits
): BillingPlanRead {
  return {
    code,
    name,
    billing_interval: 'month',
    features: [`${name} feature`],
    limits,
    watermark_enabled: code === 'free',
    priority_support_enabled: false,
    prices
  };
}

function freeAccount(
  overrides: Partial<BillingCurrentPlanRead> = {},
  market: { billing_market: string; default_currency: string; allowed_currencies: string[] } = {
    billing_market: 'RU',
    default_currency: 'RUB',
    allowed_currencies: ['RUB']
  }
): BillingCurrentPlanRead {
  return {
    user_id: 1,
    billing_market: market.billing_market,
    default_currency: market.default_currency,
    allowed_currencies: market.allowed_currencies,
    locale: null,
    plan: plan('free', 'FREE', [
      { currency: market.default_currency, amount: 0, availability: 'priced', billing_interval: 'month' }
    ]),
    subscription: {
      status: null,
      plan_code: null,
      currency: null,
      current_period_start: null,
      current_period_end: null,
      cancel_at_period_end: false,
      grants_entitlements: false
    },
    limits: freeLimits,
    current_usage: {
      current_profiles: 1,
      current_memories: 0,
      current_audio_minutes: 0,
      current_videos_month: 0,
      current_family_members: 0
    },
    ...overrides
  };
}

function catalogFrom(
  market: { billing_market: string; default_currency: string; allowed_currencies: string[]; locale?: string | null },
  plans: BillingPlanRead[]
): BillingCatalogRead {
  return {
    billing_market: market.billing_market,
    default_currency: market.default_currency,
    allowed_currencies: market.allowed_currencies,
    locale: market.locale ?? null,
    plans
  };
}

const ruCatalog = catalogFrom(
  { billing_market: 'RU', default_currency: 'RUB', allowed_currencies: ['RUB'] },
  [
    plan('free', 'FREE', [{ currency: 'RUB', amount: 0, availability: 'priced', billing_interval: 'month' }]),
    plan(
      'basic',
      'BASIC',
      [{ currency: 'RUB', amount: 499, availability: 'priced', billing_interval: 'month' }],
      { ...freeLimits, max_profiles: 3, max_memories: null }
    ),
    plan(
      'premium',
      'PREMIUM',
      [{ currency: 'RUB', amount: 999, availability: 'priced', billing_interval: 'month' }],
      { ...freeLimits, max_profiles: null, max_memories: null, allow_unlimited_chat: true }
    )
  ]
);

describe('BillingAccountPanel', () => {
  afterEach(() => {
    vi.mocked(billingApi.getBillingAccount).mockReset();
    vi.mocked(billingApi.getBillingPlans).mockReset();
    vi.mocked(billingApi.startCheckout).mockReset();
  });

  it('renders current plan and usage from backend account payload', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(ruCatalog);

    render(<BillingAccountPanel lang="en" t={t} token="tok" />);

    expect(await screen.findByText(/Current plan/i)).toBeInTheDocument();
    expect(screen.getByText('Free')).toBeInTheDocument();
    expect(screen.getByText(/Memorials:\s*1 \/ 1/i)).toBeInTheDocument();
    expect(screen.getByText(/Memories:\s*0 \/ 10/i)).toBeInTheDocument();
  });

  it('RU English UI still renders RUB and has no currency selector', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(ruCatalog);
    const user = userEvent.setup();

    render(<BillingAccountPanel lang="en" showPlansInitially t={t} token="tok" />);
    await screen.findByText('Basic');
    expect(screen.getByText(/499 RUB/)).toBeInTheDocument();
    expect(screen.queryByTestId('billing-currency-selector')).not.toBeInTheDocument();
    expect(billingApi.getBillingPlans).toHaveBeenCalledWith('en');

    await user.click(screen.getAllByRole('button', { name: t.billingUpgrade })[0]);
    await waitFor(() =>
      expect(billingApi.startCheckout).toHaveBeenCalledWith('tok', 'basic', {
        currency: 'RUB',
        locale: 'en'
      })
    );
  });

  it('RU Czech UI still renders RUB without currency selector and localizes plan copy', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(ruCatalog);

    render(<BillingAccountPanel lang="cs" showPlansInitially t={t} token="tok" />);
    expect(await screen.findByText(/499 RUB/)).toBeInTheDocument();
    expect(screen.getByText('Basic')).toBeInTheDocument();
    expect(screen.getByText('až 3 memoriály')).toBeInTheDocument();
    expect(screen.queryByTestId('billing-currency-selector')).not.toBeInTheDocument();
    expect(billingApi.getBillingPlans).toHaveBeenCalledWith('cs');
  });

  it('CZ Czech renders CZK only and no unnecessary currency selector', async () => {
    const czCsMarket = {
      billing_market: 'CZ',
      default_currency: 'CZK',
      allowed_currencies: ['CZK']
    };
    const czCatalog = catalogFrom({ ...czCsMarket, locale: 'cs' }, [
      plan('free', 'FREE', [{ currency: 'CZK', amount: 0, availability: 'priced', billing_interval: 'month' }]),
      plan('basic', 'BASIC', [
        { currency: 'CZK', amount: null, availability: 'pending_price', billing_interval: 'month' }
      ])
    ]);
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount({}, czCsMarket));
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(czCatalog);

    render(<BillingAccountPanel lang="cs" showPlansInitially t={t} token="tok" />);
    expect(await screen.findByText(t.billingPricePending)).toBeInTheDocument();
    expect(screen.queryByTestId('billing-currency-selector')).not.toBeInTheDocument();
    expect(screen.queryByText(/EUR|USD|RUB/)).not.toBeInTheDocument();
  });

  it('CZ English defaults to EUR and can select USD from backend-allowed list only', async () => {
    const czEnMarket = {
      billing_market: 'CZ',
      default_currency: 'EUR',
      allowed_currencies: ['EUR', 'USD']
    };
    const czCatalog = catalogFrom({ ...czEnMarket, locale: 'en' }, [
      plan('free', 'FREE', [
        { currency: 'EUR', amount: 0, availability: 'priced', billing_interval: 'month' },
        { currency: 'USD', amount: 0, availability: 'priced', billing_interval: 'month' }
      ]),
      plan('basic', 'BASIC', [
        { currency: 'EUR', amount: null, availability: 'pending_price', billing_interval: 'month' },
        { currency: 'USD', amount: null, availability: 'pending_price', billing_interval: 'month' }
      ])
    ]);
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount({}, czEnMarket));
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(czCatalog);
    const user = userEvent.setup();

    render(<BillingAccountPanel lang="en" showPlansInitially t={t} token="tok" />);
    expect(await screen.findByTestId('billing-currency-selector')).toBeInTheDocument();
    const select = screen.getByLabelText(t.billingCurrency);
    expect(select).toHaveValue('EUR');
    expect(screen.queryByRole('option', { name: 'CZK' })).not.toBeInTheDocument();
    expect(screen.queryByRole('option', { name: 'RUB' })).not.toBeInTheDocument();

    await user.selectOptions(select, 'USD');
    expect(select).toHaveValue('USD');
  });

  it('language change refetches catalog so market rules stay backend-driven', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(ruCatalog);

    const { rerender } = render(<BillingAccountPanel lang="en" t={t} token="tok" />);
    await screen.findByText('Free');
    expect(billingApi.getBillingPlans).toHaveBeenCalledWith('en');

    rerender(<BillingAccountPanel lang="cs" t={t} token="tok" />);
    await waitFor(() => expect(billingApi.getBillingPlans).toHaveBeenCalledWith('cs'));
  });

  it('shows View plans entry point for free users and loads catalog from backend', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(ruCatalog);
    const user = userEvent.setup();

    render(<BillingAccountPanel lang="en" t={t} token="tok" />);
    await screen.findByText('Free');
    await user.click(screen.getByRole('button', { name: t.billingViewPlans }));

    expect(await screen.findByText(t.billingPlansTitle)).toBeInTheDocument();
    expect(screen.getByText('Basic')).toBeInTheDocument();
    expect(screen.getByText('Premium')).toBeInTheDocument();
    expect(billingApi.getBillingPlans).toHaveBeenCalled();
  });

  it('renders paid plan status and period end when available', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(
      freeAccount({
        plan: ruCatalog.plans[2],
        limits: ruCatalog.plans[2].limits,
        subscription: {
          status: 'active',
          plan_code: 'premium',
          currency: 'RUB',
          current_period_start: '2026-01-01T00:00:00Z',
          current_period_end: '2026-02-01T00:00:00Z',
          cancel_at_period_end: true,
          grants_entitlements: true
        }
      })
    );
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(ruCatalog);

    render(<BillingAccountPanel lang="en" showPlansInitially t={t} token="tok" />);

    expect(await screen.findByText(/Current plan/i)).toBeInTheDocument();
    expect(screen.getAllByText('Premium').length).toBeGreaterThanOrEqual(1);
    expect(screen.getByText(/Subscription status:\s*active/i)).toBeInTheDocument();
    expect(screen.getByText(new RegExp(t.billingCancelAtPeriodEnd))).toBeInTheDocument();
    expect(screen.getByText(new RegExp(t.billingPeriodEnd))).toBeInTheDocument();
  });

  it('checkout action never reports success in Phase 6A', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(ruCatalog);
    vi.mocked(billingApi.startCheckout).mockResolvedValue({
      available: false,
      detail: 'Checkout is not available yet',
      code: 'checkout_not_available'
    });
    const user = userEvent.setup();

    render(<BillingAccountPanel lang="en" showPlansInitially t={t} token="tok" />);
    await screen.findByText('Basic');
    await user.click(screen.getAllByRole('button', { name: t.billingUpgrade })[0]);

    await waitFor(() =>
      expect(billingApi.startCheckout).toHaveBeenCalledWith('tok', 'basic', {
        currency: 'RUB',
        locale: 'en'
      })
    );
    expect(await screen.findByText(/Checkout is not available yet/i)).toBeInTheDocument();
    expect(screen.queryByText(/payment successful|upgraded/i)).not.toBeInTheDocument();
  });
});

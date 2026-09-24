import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { BillingAccountPanel } from './BillingAccountPanel';
import * as billingApi from '../lib/billingApi';
import type { BillingCurrentPlanRead, BillingPlanRead } from '../types/memorial';

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
  working: 'Working'
};

function freeAccount(overrides: Partial<BillingCurrentPlanRead> = {}): BillingCurrentPlanRead {
  return {
    user_id: 1,
    plan: {
      code: 'free',
      name: 'FREE',
      price_rub_monthly: 0,
      currency: 'RUB',
      billing_interval: 'month',
      features: ['1 profile'],
      limits: {
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
      },
      watermark_enabled: true,
      priority_support_enabled: false
    },
    subscription: {
      status: null,
      plan_code: null,
      current_period_start: null,
      current_period_end: null,
      cancel_at_period_end: false,
      grants_entitlements: false
    },
    limits: {
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
    },
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

const catalog: BillingPlanRead[] = [
  freeAccount().plan,
  {
    ...freeAccount().plan,
    code: 'basic',
    name: 'BASIC',
    price_rub_monthly: 499,
    features: ['up to 3 profiles'],
    limits: { ...freeAccount().limits, max_profiles: 3, max_memories: null }
  },
  {
    ...freeAccount().plan,
    code: 'premium',
    name: 'PREMIUM',
    price_rub_monthly: 999,
    features: ['unlimited profiles'],
    limits: { ...freeAccount().limits, max_profiles: null, max_memories: null, allow_unlimited_chat: true }
  }
];

describe('BillingAccountPanel', () => {
  afterEach(() => {
    vi.mocked(billingApi.getBillingAccount).mockReset();
    vi.mocked(billingApi.getBillingPlans).mockReset();
    vi.mocked(billingApi.startCheckout).mockReset();
  });

  it('renders current plan and usage from backend account payload', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(catalog);

    render(<BillingAccountPanel t={t} token="tok" />);

    expect(await screen.findByText(/Current plan/i)).toBeInTheDocument();
    expect(screen.getByText('FREE')).toBeInTheDocument();
    expect(screen.getByText(/Memorials:\s*1 \/ 1/i)).toBeInTheDocument();
    expect(screen.getByText(/Memories:\s*0 \/ 10/i)).toBeInTheDocument();
  });

  it('shows View plans entry point for free users and loads catalog from backend', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(catalog);
    const user = userEvent.setup();

    render(<BillingAccountPanel t={t} token="tok" />);
    await screen.findByText('FREE');
    await user.click(screen.getByRole('button', { name: t.billingViewPlans }));

    expect(await screen.findByText(t.billingPlansTitle)).toBeInTheDocument();
    expect(screen.getByText('BASIC')).toBeInTheDocument();
    expect(screen.getByText('PREMIUM')).toBeInTheDocument();
    expect(billingApi.getBillingPlans).toHaveBeenCalled();
  });

  it('renders paid plan status and period end when available', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(
      freeAccount({
        plan: catalog[2],
        limits: catalog[2].limits,
        subscription: {
          status: 'active',
          plan_code: 'premium',
          current_period_start: '2026-01-01T00:00:00Z',
          current_period_end: '2026-02-01T00:00:00Z',
          cancel_at_period_end: true,
          grants_entitlements: true
        }
      })
    );
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(catalog);

    render(<BillingAccountPanel showPlansInitially t={t} token="tok" />);

    expect(await screen.findByText(/Current plan/i)).toBeInTheDocument();
    expect(screen.getAllByText('PREMIUM').length).toBeGreaterThanOrEqual(1);
    expect(screen.getByText(/Subscription status:\s*active/i)).toBeInTheDocument();
    expect(screen.getByText(new RegExp(t.billingCancelAtPeriodEnd))).toBeInTheDocument();
    expect(screen.getByText(new RegExp(t.billingPeriodEnd))).toBeInTheDocument();
  });

  it('checkout action never reports success in Phase 6A', async () => {
    vi.mocked(billingApi.getBillingAccount).mockResolvedValue(freeAccount());
    vi.mocked(billingApi.getBillingPlans).mockResolvedValue(catalog);
    vi.mocked(billingApi.startCheckout).mockResolvedValue({
      available: false,
      detail: 'Checkout is not available yet',
      code: 'checkout_not_available'
    });
    const user = userEvent.setup();

    render(<BillingAccountPanel showPlansInitially t={t} token="tok" />);
    await screen.findByText('BASIC');
    await user.click(screen.getAllByRole('button', { name: t.billingUpgrade })[0]);

    await waitFor(() => expect(billingApi.startCheckout).toHaveBeenCalledWith('tok', 'basic'));
    expect(await screen.findByText(/Checkout is not available yet/i)).toBeInTheDocument();
    expect(screen.queryByText(/payment successful|upgraded/i)).not.toBeInTheDocument();
  });
});

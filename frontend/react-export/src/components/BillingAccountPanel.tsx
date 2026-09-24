import { useEffect, useState } from 'react';
import { getBillingAccount, getBillingPlans, startCheckout } from '../lib/billingApi';
import type { BillingCurrentPlanRead, BillingPlanRead } from '../types/memorial';

export type BillingCopy = {
  billing: string;
  billingCurrentPlan: string;
  billingUsage: string;
  billingMemorialsUsage: string;
  billingMemoriesUsage: string;
  billingUnlimited: string;
  billingSubscriptionStatus: string;
  billingPeriodEnd: string;
  billingCancelAtPeriodEnd: string;
  billingViewPlans: string;
  billingPlansTitle: string;
  billingUpgrade: string;
  billingCheckoutUnavailable: string;
  billingPerMonth: string;
  working: string;
};

function formatLimit(value: number | null, unlimitedLabel: string): string {
  return value === null ? unlimitedLabel : String(value);
}

function formatMoney(plan: BillingPlanRead): string {
  if (plan.price_rub_monthly === 0) return '0';
  return `${plan.price_rub_monthly} ${plan.currency}`;
}

export function BillingAccountPanel({
  token,
  t,
  showPlansInitially = false
}: {
  token: string;
  t: BillingCopy;
  showPlansInitially?: boolean;
}) {
  const [account, setAccount] = useState<BillingCurrentPlanRead | null>(null);
  const [plans, setPlans] = useState<BillingPlanRead[]>([]);
  const [showPlans, setShowPlans] = useState(showPlansInitially);
  const [busyPlan, setBusyPlan] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    void Promise.all([getBillingAccount(token), getBillingPlans()])
      .then(([nextAccount, nextPlans]) => {
        if (cancelled) return;
        setAccount(nextAccount);
        setPlans(nextPlans);
      })
      .catch((loadError: unknown) => {
        if (cancelled) return;
        setError(loadError instanceof Error ? loadError.message : 'Could not load billing.');
      });
    return () => {
      cancelled = true;
    };
  }, [token]);

  useEffect(() => {
    if (showPlansInitially) setShowPlans(true);
  }, [showPlansInitially]);

  async function onChoosePlan(planCode: string) {
    if (planCode === 'free') return;
    setBusyPlan(planCode);
    setMessage(null);
    setError(null);
    try {
      const result = await startCheckout(token, planCode);
      if (result.available) {
        // Phase 6C will redirect; Phase 6A never reaches available=true from the stub.
        setMessage(t.billingCheckoutUnavailable);
      } else {
        setMessage(result.detail || t.billingCheckoutUnavailable);
      }
    } catch (checkoutError) {
      setError(checkoutError instanceof Error ? checkoutError.message : t.billingCheckoutUnavailable);
    } finally {
      setBusyPlan(null);
    }
  }

  if (error && !account) {
    return <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>;
  }

  if (!account) {
    return <p className="text-sm text-fg/55">{t.working}</p>;
  }

  const memorialsLimit = formatLimit(account.limits.max_profiles, t.billingUnlimited);
  const memoriesLimit = formatLimit(account.limits.max_memories, t.billingUnlimited);
  const statusLabel = account.subscription.status;
  const periodEnd = account.subscription.current_period_end;

  return (
    <div className="min-w-0 space-y-5" data-testid="billing-account-panel">
      <div>
        <h3 className="font-serif text-3xl">{t.billing}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">
          {t.billingCurrentPlan}: <strong className="text-fg">{account.plan.name}</strong>
        </p>
      </div>

      <div className="rounded-3xl border border-white/10 bg-black/20 p-4">
        <p className="text-xs uppercase tracking-[.18em] text-fg/40">{t.billingUsage}</p>
        <ul className="mt-3 space-y-2 text-sm text-fg/75">
          <li>
            {t.billingMemorialsUsage}: {account.current_usage.current_profiles} / {memorialsLimit}
          </li>
          <li>
            {t.billingMemoriesUsage}: {account.current_usage.current_memories} / {memoriesLimit}
          </li>
        </ul>
        {statusLabel && (
          <p className="mt-3 text-sm text-fg/60">
            {t.billingSubscriptionStatus}: {statusLabel}
            {account.subscription.cancel_at_period_end ? ` · ${t.billingCancelAtPeriodEnd}` : ''}
          </p>
        )}
        {periodEnd && (
          <p className="mt-1 text-sm text-fg/60">
            {t.billingPeriodEnd}: {new Date(periodEnd).toLocaleString()}
          </p>
        )}
      </div>

      {!showPlans ? (
        <button
          className="rounded-full border border-white/15 px-5 py-3 text-sm text-fg/80 transition hover:bg-white/10"
          onClick={() => setShowPlans(true)}
          type="button"
        >
          {t.billingViewPlans}
        </button>
      ) : (
        <div className="space-y-4">
          <h4 className="text-lg font-semibold text-fg">{t.billingPlansTitle}</h4>
          <div className="grid min-w-0 gap-3">
            {plans.map((plan) => {
              const isCurrent = plan.code === account.plan.code;
              const isPaid = plan.price_rub_monthly > 0;
              return (
                <article className="rounded-3xl border border-white/10 bg-black/20 p-4" key={plan.code}>
                  <div className="flex min-w-0 flex-wrap items-start justify-between gap-3">
                    <div>
                      <h5 className="text-lg font-semibold">{plan.name}</h5>
                      <p className="mt-1 text-sm text-fg/55">
                        {formatMoney(plan)}
                        {isPaid ? ` / ${t.billingPerMonth}` : ''}
                      </p>
                      <ul className="mt-3 list-disc space-y-1 pl-5 text-sm text-fg/65">
                        {plan.features.map((feature) => (
                          <li key={feature}>{feature}</li>
                        ))}
                      </ul>
                    </div>
                    {isPaid && !isCurrent && (
                      <button
                        className="rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-2.5 text-sm font-semibold text-ink disabled:opacity-55"
                        disabled={busyPlan === plan.code}
                        onClick={() => void onChoosePlan(plan.code)}
                        type="button"
                      >
                        {busyPlan === plan.code ? t.working : t.billingUpgrade}
                      </button>
                    )}
                    {isCurrent && (
                      <span className="rounded-full border border-cyan/40 px-3 py-1 text-xs uppercase tracking-[.16em] text-cyan">
                        {account.plan.name}
                      </span>
                    )}
                  </div>
                </article>
              );
            })}
          </div>
        </div>
      )}

      {message && <p className="rounded-2xl border border-cyan/30 bg-cyan/10 px-4 py-3 text-sm text-cyan">{message}</p>}
      {error && account && (
        <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>
      )}
    </div>
  );
}

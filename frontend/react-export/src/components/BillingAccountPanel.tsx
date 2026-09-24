import { useEffect, useState } from 'react';
import { getBillingAccount, getBillingPlans, startCheckout } from '../lib/billingApi';
import { getBillingPlanLocaleCopy } from '../lib/billingPlanCopy';
import type { BillingCatalogRead, BillingCurrentPlanRead, BillingPlanRead, BillingPriceRead } from '../types/memorial';
import type { Lang } from '../i18n';

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
  billingCurrency: string;
  billingPricePending: string;
  working: string;
};

function formatLimit(value: number | null, unlimitedLabel: string): string {
  return value === null ? unlimitedLabel : String(value);
}

function priceForCurrency(plan: BillingPlanRead, currency: string): BillingPriceRead | undefined {
  return plan.prices.find((price) => price.currency === currency);
}

function formatMoney(price: BillingPriceRead | undefined, pendingLabel: string): string {
  if (!price) return pendingLabel;
  if (price.availability === 'pending_price' || price.amount === null) return pendingLabel;
  if (price.amount === 0) return `0 ${price.currency}`;
  return `${price.amount} ${price.currency}`;
}

function isPaidPlan(plan: BillingPlanRead, currency: string): boolean {
  const price = priceForCurrency(plan, currency);
  if (!price) return false;
  if (price.availability === 'pending_price' || price.amount === null) return true;
  return price.amount > 0;
}

export function BillingAccountPanel({
  token,
  t,
  lang,
  showPlansInitially = false
}: {
  token: string;
  t: BillingCopy;
  lang: Lang;
  showPlansInitially?: boolean;
}) {
  const [account, setAccount] = useState<BillingCurrentPlanRead | null>(null);
  const [catalog, setCatalog] = useState<BillingCatalogRead | null>(null);
  const [selectedCurrency, setSelectedCurrency] = useState<string | null>(null);
  const [showPlans, setShowPlans] = useState(showPlansInitially);
  const [busyPlan, setBusyPlan] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    void Promise.all([getBillingAccount(token, lang), getBillingPlans(lang)])
      .then(([nextAccount, nextCatalog]) => {
        if (cancelled) return;
        setAccount(nextAccount);
        setCatalog(nextCatalog);
        setSelectedCurrency(
          typeof nextCatalog.default_currency === 'string' ? nextCatalog.default_currency : null
        );
        setError(null);
      })
      .catch((loadError: unknown) => {
        if (cancelled) return;
        setError(loadError instanceof Error ? loadError.message : 'Could not load billing.');
      });
    return () => {
      cancelled = true;
    };
  }, [token, lang]);

  useEffect(() => {
    if (showPlansInitially) setShowPlans(true);
  }, [showPlansInitially]);

  const allowedCurrencies = catalog?.allowed_currencies ?? account?.allowed_currencies ?? [];
  const activeCurrency =
    selectedCurrency && allowedCurrencies.includes(selectedCurrency)
      ? selectedCurrency
      : (catalog?.default_currency ?? account?.default_currency ?? allowedCurrencies[0] ?? '');

  async function onChoosePlan(planCode: string) {
    if (planCode === 'free' || !activeCurrency) return;
    setBusyPlan(planCode);
    setMessage(null);
    setError(null);
    try {
      const result = await startCheckout(token, planCode, {
        currency: activeCurrency,
        locale: lang
      });
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

  if (!account || !catalog) {
    return <p className="text-sm text-fg/55">{t.working}</p>;
  }

  const memorialsLimit = formatLimit(account.limits.max_profiles, t.billingUnlimited);
  const memoriesLimit = formatLimit(account.limits.max_memories, t.billingUnlimited);
  const statusLabel = account.subscription.status;
  const periodEnd = account.subscription.current_period_end;
  const plans = Array.isArray(catalog.plans) ? catalog.plans : [];
  const showCurrencySelector = allowedCurrencies.length > 1;
  const currentPlanLabel = getBillingPlanLocaleCopy(
    lang,
    account.plan.code,
    account.plan.name,
    account.plan.features
  ).name;

  return (
    <div className="min-w-0 space-y-5" data-testid="billing-account-panel">
      <div>
        <h3 className="font-serif text-3xl">{t.billing}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">
          {t.billingCurrentPlan}: <strong className="text-fg">{currentPlanLabel}</strong>
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

      {showCurrencySelector && (
        <div className="flex min-w-0 flex-wrap items-center gap-3" data-testid="billing-currency-selector">
          <label className="text-sm text-fg/60" htmlFor="billing-currency">
            {t.billingCurrency}
          </label>
          <select
            className="rounded-full border border-white/15 bg-black/30 px-4 py-2 text-sm text-fg"
            id="billing-currency"
            onChange={(event) => setSelectedCurrency(event.target.value)}
            value={activeCurrency}
          >
            {allowedCurrencies.map((currency) => (
              <option key={currency} value={currency}>
                {currency}
              </option>
            ))}
          </select>
        </div>
      )}

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
              const price = priceForCurrency(plan, activeCurrency);
              const isPaid = isPaidPlan(plan, activeCurrency);
              const priceReady = price?.availability === 'priced' && price.amount !== null;
              const localized = getBillingPlanLocaleCopy(lang, plan.code, plan.name, plan.features);
              return (
                <article className="rounded-3xl border border-white/10 bg-black/20 p-4" key={plan.code}>
                  <div className="flex min-w-0 flex-wrap items-start justify-between gap-3">
                    <div>
                      <h5 className="text-lg font-semibold">{localized.name}</h5>
                      <p className="mt-1 text-sm text-fg/55">
                        {formatMoney(price, t.billingPricePending)}
                        {isPaid && priceReady ? ` / ${t.billingPerMonth}` : ''}
                      </p>
                      <ul className="mt-3 list-disc space-y-1 pl-5 text-sm text-fg/65">
                        {localized.features.map((feature) => (
                          <li key={feature}>{feature}</li>
                        ))}
                      </ul>
                    </div>
                    {isPaid && !isCurrent && priceReady && (
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
                        {currentPlanLabel}
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

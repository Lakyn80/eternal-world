/**
 * Frontend billing API boundary (Phase 6A).
 *
 * Components import from here - not from payment SDKs. Re-exports the
 * memorialApi implementations so provider checkout (Phase 6C) only needs to
 * change the backend endpoint behind `startCheckout`.
 */

export {
  getBillingAccount,
  getBillingPlans,
  startCheckout,
  type CheckoutStartResult
} from './memorialApi';

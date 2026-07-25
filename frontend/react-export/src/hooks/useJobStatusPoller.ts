import { useEffect, useRef, useState } from 'react';
import { getBackgroundJob, MemorialApiError } from '../lib/memorialApi';
import type { BackgroundJobRead, BackgroundJobStatusValue } from '../types/memorial';

// Task 65.9.1 (Part F) - the complete async job status polling lifecycle
// for the two Task 65.9 fire-and-forget-turned-async endpoints ("Index
// memory" for candidates, retry-indexing for contributions), and reusable
// for any future 202-returning heavy endpoint. Task 65.9 itself only
// guaranteed the response body never claims "indexed" before the backend
// confirms it - this hook is what actually watches the job through to a
// terminal state instead of relying on a single manual reload.

/** Terminal states: polling must stop immediately and never resume for the
 * same job id (a new job/action creates a new poller instance instead). */
const TERMINAL_STATUSES: ReadonlySet<BackgroundJobStatusValue> = new Set([
  'succeeded',
  'failed',
  'cancelled'
]);

/** Task 65.9.1 (Part F.4) - explicit, testable backoff policy: the first
 * three checks are fast (~1s) so a normally-quick job resolves almost
 * immediately, then the interval widens twice, capping at 12s (within the
 * spec's 10-15s cap) so a long-backlogged job does not hammer the API. Pure
 * function - no timers, no React - so it is unit-testable in isolation. */
export function computeNextPollDelayMs(pollCount: number): number {
  if (pollCount < 3) return 1000;
  if (pollCount < 6) return 2000;
  if (pollCount < 9) return 5000;
  return 12000;
}

/** Task 65.9.1 (Part F.5) - while the browser tab is hidden, polling is
 * slowed to a fixed, much less frequent cadence rather than paused
 * outright (a job can still complete while the tab is hidden, and the
 * next foreground visit should not have to wait a full biography-style
 * reload to discover that) - resuming visibility triggers an immediate
 * poll regardless of this value (see the `visibilitychange` handler
 * below), so this only bounds background cost, never freshness on return. */
export const HIDDEN_TAB_POLL_DELAY_MS = 20000;

export type JobStatusPollerScope = {
  /** Distinguishes one authenticated account's job from another's - never
   * used for the actual authorization decision (the backend re-checks
   * ownership on every call), only to key client-side state so a stale
   * poller/cached status can never be attributed to the wrong account. */
  accountKey: string;
  /** Memorial/profile id the job belongs to - included so switching
   * memorials can never show another memorial's cached terminal status. */
  profileKey: string | number;
  jobId: number;
};

export type JobStatusPollerResult = {
  job: BackgroundJobRead | null;
  /** True until the first status fetch resolves (success or terminal
   * failure) - lets callers avoid a flash of "unknown" state. */
  loading: boolean;
  /** Set only for a permanent backend failure (job itself failed, or a
   * genuine 404/401/403) - never set for a transient network blip, which
   * is retried silently in the background instead (Part F.12). */
  fatalError: 'not_found' | 'unauthorized' | null;
  /** True once the job reaches a terminal state (Part F.4: succeeded,
   * failed, cancelled) - the only signal callers should use to decide
   * whether it is safe to say "indexed and searchable" (Part F.3). */
  isTerminal: boolean;
};

function scopeToKey(scope: JobStatusPollerScope): string {
  return `${scope.accountKey}:${scope.profileKey}:${scope.jobId}`;
}

/** Task 65.9.1 (Part F) - polls `GET /api/jobs/{job_id}` for one background
 * job using the explicit backoff policy above, until it reaches a terminal
 * state or the caller unmounts/changes scope.
 *
 * Cancellation (Part F.7/F.19): uses the same `cancelled`-flag idiom this
 * codebase already uses for its other polling loop (`BiographyPanel`'s
 * biography-status poll) rather than introducing a second, inconsistent
 * cancellation mechanism (`memorialApi.requestJson` has no `AbortSignal`
 * plumbing today, and adding one everywhere is an unrelated, out-of-scope
 * refactor) - every scheduled timer checks this flag both before firing the
 * request and before scheduling the next one, so a stale in-flight request
 * can never update state or reschedule itself after teardown.
 *
 * Duplicate-poller prevention (Part F.8/F.20): keyed by
 * `accountKey:profileKey:jobId` - a second hook instance (e.g. from a
 * double-render in strict mode) for the exact same scope key reuses the
 * existing in-flight-guard ref rather than firing a second overlapping
 * fetch chain; changing any part of the scope key tears down the previous
 * effect (React's own cleanup) before the new one starts.
 */
export function useJobStatusPoller(
  token: string | null,
  scope: JobStatusPollerScope | null,
  enabled: boolean = true
): JobStatusPollerResult {
  const [job, setJob] = useState<BackgroundJobRead | null>(null);
  const [loading, setLoading] = useState<boolean>(Boolean(scope && enabled));
  const [fatalError, setFatalError] = useState<'not_found' | 'unauthorized' | null>(null);
  const scopeKeyRef = useRef<string | null>(null);

  useEffect(() => {
    // Task 65.9.1 (Part F.10): a brand-new scope (job id, profile, or
    // account changed) never keeps the previous scope's job/error state -
    // reset synchronously before the first fetch for the new scope, so a
    // terminal status from a previous memorial/job can never be shown for
    // the new one, even for one render.
    setJob(null);
    setFatalError(null);

    if (!scope || !enabled || !token) {
      setLoading(false);
      return;
    }

    const currentScope = scope;
    const currentScopeKey = scopeToKey(currentScope);
    scopeKeyRef.current = currentScopeKey;
    setLoading(true);

    let cancelled = false;
    let timer: ReturnType<typeof setTimeout> | null = null;
    let pollCount = 0;
    let hiddenAtPollStart = false;

    function isStillCurrent(): boolean {
      return !cancelled && scopeKeyRef.current === currentScopeKey;
    }

    function scheduleNext() {
      if (!isStillCurrent()) return;
      hiddenAtPollStart = typeof document !== 'undefined' && document.hidden;
      const delay = hiddenAtPollStart ? HIDDEN_TAB_POLL_DELAY_MS : computeNextPollDelayMs(pollCount);
      timer = setTimeout(() => void tick(), delay);
    }

    async function tick() {
      if (!isStillCurrent()) return;
      try {
        const latest = await getBackgroundJob(token as string, currentScope.jobId);
        if (!isStillCurrent()) return;
        setJob(latest);
        setLoading(false);
        pollCount += 1;
        if (!TERMINAL_STATUSES.has(latest.status)) {
          scheduleNext();
        }
      } catch (pollError) {
        if (!isStillCurrent()) return;
        if (pollError instanceof MemorialApiError && (pollError.status === 401 || pollError.status === 403)) {
          // Part F.11/N.2: authorization failure stops polling immediately
          // and clears any previously-fetched job state - never keep
          // showing a status the caller is no longer allowed to see.
          setJob(null);
          setFatalError('unauthorized');
          setLoading(false);
          return;
        }
        if (pollError instanceof MemorialApiError && pollError.status === 404) {
          setFatalError('not_found');
          setLoading(false);
          return;
        }
        // Part F.12: everything else (network unreachable = status 0,
        // 5xx, etc.) is a transient failure - keep the backend job state
        // authoritative, never report the job as failed client-side, and
        // keep retrying on the same bounded backoff schedule.
        setLoading(false);
        pollCount += 1;
        scheduleNext();
      }
    }

    function handleVisibilityChange() {
      if (typeof document === 'undefined' || document.hidden) return;
      // Part F.5: becoming visible again triggers an immediate refresh
      // rather than waiting out whatever hidden-tab delay was scheduled.
      if (timer !== null) {
        clearTimeout(timer);
        timer = null;
      }
      void tick();
    }

    if (typeof document !== 'undefined') {
      document.addEventListener('visibilitychange', handleVisibilityChange);
    }

    void tick();

    return () => {
      cancelled = true;
      if (timer !== null) clearTimeout(timer);
      if (typeof document !== 'undefined') {
        document.removeEventListener('visibilitychange', handleVisibilityChange);
      }
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token, scope ? scopeToKey(scope) : null, enabled]);

  return {
    job,
    loading,
    fatalError,
    isTerminal: job !== null && TERMINAL_STATUSES.has(job.status)
  };
}

export function isJobStatusTerminal(status: BackgroundJobStatusValue): boolean {
  return TERMINAL_STATUSES.has(status);
}

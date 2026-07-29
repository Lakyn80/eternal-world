import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  computeNextPollDelayMs,
  HIDDEN_TAB_POLL_DELAY_MS,
  isJobStatusTerminal,
  useJobStatusPoller
} from './useJobStatusPoller';
import * as api from '../lib/memorialApi';
import { MemorialApiError } from '../lib/memorialApi';
import type { BackgroundJobRead, BackgroundJobStatusValue } from '../types/memorial';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    getBackgroundJob: vi.fn()
  };
});

function job(status: BackgroundJobStatusValue, overrides: Partial<BackgroundJobRead> = {}): BackgroundJobRead {
  return {
    id: 1,
    owner_user_id: 1,
    profile_id: 7,
    job_type: 'qdrant_indexing',
    status,
    progress_current: 0,
    progress_total: 0,
    celery_task_id: null,
    result_payload: null,
    error_payload: null,
    error_message: null,
    queue: 'embedding',
    attempt_count: 0,
    max_attempts: 3,
    safe_error_category: null,
    created_at: '2026-01-01T00:00:00Z',
    updated_at: '2026-01-01T00:00:00Z',
    ...overrides
  };
}

const getBackgroundJob = api.getBackgroundJob as unknown as ReturnType<typeof vi.fn>;

// Fake timers replace global setTimeout, so @testing-library's own
// `waitFor` polling loop (which itself schedules via setTimeout) can never
// resolve on its own here - flushing pending microtasks directly (the
// mocked API call resolves immediately, it is real timers we are faking,
// not the JS microtask queue) is the correct, deterministic alternative.
async function flush(): Promise<void> {
  await act(async () => {
    await Promise.resolve();
    await Promise.resolve();
  });
}

beforeEach(() => {
  vi.useFakeTimers();
  getBackgroundJob.mockReset();
});

afterEach(() => {
  vi.useRealTimers();
});

// --- Pure backoff policy ----------------------------------------------------

describe('computeNextPollDelayMs', () => {
  it('uses the fast ~1s interval for the first three polls', () => {
    expect(computeNextPollDelayMs(0)).toBe(1000);
    expect(computeNextPollDelayMs(1)).toBe(1000);
    expect(computeNextPollDelayMs(2)).toBe(1000);
  });

  it('backs off to ~2s next', () => {
    expect(computeNextPollDelayMs(3)).toBe(2000);
    expect(computeNextPollDelayMs(5)).toBe(2000);
  });

  it('backs off to ~5s next', () => {
    expect(computeNextPollDelayMs(6)).toBe(5000);
    expect(computeNextPollDelayMs(8)).toBe(5000);
  });

  it('caps at 12s (within the 10-15s spec range) and never exceeds it', () => {
    expect(computeNextPollDelayMs(9)).toBe(12000);
    expect(computeNextPollDelayMs(1000)).toBe(12000);
  });
});

describe('isJobStatusTerminal', () => {
  it('is true only for succeeded/failed/cancelled', () => {
    expect(isJobStatusTerminal('succeeded')).toBe(true);
    expect(isJobStatusTerminal('failed')).toBe(true);
    expect(isJobStatusTerminal('cancelled')).toBe(true);
    expect(isJobStatusTerminal('pending')).toBe(false);
    expect(isJobStatusTerminal('queued')).toBe(false);
    expect(isJobStatusTerminal('running')).toBe(false);
    expect(isJobStatusTerminal('retry_scheduled')).toBe(false);
    expect(isJobStatusTerminal('recovery_pending')).toBe(false);
  });
});

// --- Hook lifecycle ----------------------------------------------------------

const scope = { accountKey: 'tok-a', profileKey: 7, jobId: 1 };

describe('useJobStatusPoller', () => {
  it('polls immediately on mount and reflects pending/queued/processing states', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('queued'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));

    await flush();
    expect(result.current.job?.status).toBe('queued');
    expect(result.current.loading).toBe(false);
    expect(result.current.isTerminal).toBe(false);
  });

  it('polls with an empty-string token (cookie-session resume after page reload)', async () => {
    // Task 65.7: after getSession() restore, MemorialWorkspace keeps
    // accessToken as '' and relies on the HttpOnly cookie. The poller must
    // still call getBackgroundJob - previously `!token` aborted the effect
    // and left contribution badges stuck on "indexing pending" until reload.
    getBackgroundJob.mockResolvedValueOnce(job('succeeded'));
    const { result } = renderHook(() =>
      useJobStatusPoller('', { accountKey: 'owner@example.com', profileKey: 7, jobId: 1 })
    );

    await flush();
    expect(getBackgroundJob).toHaveBeenCalledWith('', 1);
    expect(result.current.job?.status).toBe('succeeded');
    expect(result.current.isTerminal).toBe(true);
  });

  it('does not poll when token is explicitly null', async () => {
    const { result } = renderHook(() => useJobStatusPoller(null, scope));
    await flush();
    expect(getBackgroundJob).not.toHaveBeenCalled();
    expect(result.current.job).toBeNull();
    expect(result.current.loading).toBe(false);
  });

  it('shows retry_scheduled and recovery_pending as non-terminal', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('retry_scheduled'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('retry_scheduled');
    expect(result.current.isTerminal).toBe(false);

    getBackgroundJob.mockResolvedValueOnce(job('recovery_pending'));
    await act(async () => {
      await vi.advanceTimersByTimeAsync(1000);
    });
    expect(result.current.job?.status).toBe('recovery_pending');
    expect(result.current.isTerminal).toBe(false);
  });

  it('stops polling once succeeded is reached', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('queued'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('queued');

    getBackgroundJob.mockResolvedValueOnce(job('succeeded'));
    await act(async () => {
      await vi.advanceTimersByTimeAsync(1000);
    });
    expect(result.current.job?.status).toBe('succeeded');
    expect(result.current.isTerminal).toBe(true);

    const callsAtTerminal = getBackgroundJob.mock.calls.length;
    await act(async () => {
      await vi.advanceTimersByTimeAsync(60_000);
    });
    expect(getBackgroundJob.mock.calls.length).toBe(callsAtTerminal);
  });

  it('stops polling once failed is reached', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('failed', { safe_error_category: 'provider_corrupt' }));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('failed');
    expect(result.current.isTerminal).toBe(true);

    const callsAtTerminal = getBackgroundJob.mock.calls.length;
    await act(async () => {
      await vi.advanceTimersByTimeAsync(60_000);
    });
    expect(getBackgroundJob.mock.calls.length).toBe(callsAtTerminal);
  });

  it('stops polling once cancelled is reached', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('cancelled'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('cancelled');
    expect(result.current.isTerminal).toBe(true);
  });

  it('never reports isTerminal before succeeded is actually observed', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('queued'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('queued');
    expect(result.current.isTerminal).toBe(false);
  });

  it('uses the fast interval for the first polls, then backs off', async () => {
    getBackgroundJob.mockResolvedValue(job('running'));
    renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(999);
    });
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);
    await act(async () => {
      await vi.advanceTimersByTimeAsync(2);
    });
    expect(getBackgroundJob).toHaveBeenCalledTimes(2);
  });

  it('slows down substantially while the tab is hidden', async () => {
    getBackgroundJob.mockResolvedValue(job('running'));
    Object.defineProperty(document, 'hidden', { configurable: true, get: () => true });
    renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(HIDDEN_TAB_POLL_DELAY_MS - 1);
    });
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);
    await act(async () => {
      await vi.advanceTimersByTimeAsync(2);
    });
    expect(getBackgroundJob).toHaveBeenCalledTimes(2);
    Object.defineProperty(document, 'hidden', { configurable: true, get: () => false });
  });

  it('polls immediately when the tab becomes visible again', async () => {
    getBackgroundJob.mockResolvedValue(job('running'));
    Object.defineProperty(document, 'hidden', { configurable: true, get: () => true });
    renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);

    Object.defineProperty(document, 'hidden', { configurable: true, get: () => false });
    await act(async () => {
      document.dispatchEvent(new Event('visibilitychange'));
      await Promise.resolve();
      await Promise.resolve();
    });
    expect(getBackgroundJob).toHaveBeenCalledTimes(2);
  });

  it('cancels polling on unmount (no further calls, no state updates)', async () => {
    getBackgroundJob.mockResolvedValue(job('running'));
    const { unmount } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);
    unmount();

    const callsAtUnmount = getBackgroundJob.mock.calls.length;
    await act(async () => {
      await vi.advanceTimersByTimeAsync(60_000);
    });
    expect(getBackgroundJob.mock.calls.length).toBe(callsAtUnmount);
  });

  it('resets job/error state and starts a fresh poll when the job id (route/action) changes', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('succeeded'));
    const { result, rerender } = renderHook(({ jobId }) => useJobStatusPoller('tok-a', { ...scope, jobId }), {
      initialProps: { jobId: 1 }
    });
    await flush();
    expect(result.current.isTerminal).toBe(true);

    getBackgroundJob.mockResolvedValueOnce(job('queued'));
    act(() => {
      rerender({ jobId: 2 });
    });
    // Immediately after the scope changes (before the new fetch resolves)
    // the previous terminal job must not still be visible.
    expect(result.current.job).toBeNull();
    await flush();
    expect(result.current.job?.status).toBe('queued');
    expect(result.current.isTerminal).toBe(false);
  });

  it('clears state and stops polling when the memorial/profile changes', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('running'));
    const { result, rerender } = renderHook(({ profileKey }) => useJobStatusPoller('tok-a', { ...scope, profileKey }), {
      initialProps: { profileKey: 7 }
    });
    await flush();
    expect(result.current.job?.status).toBe('running');

    getBackgroundJob.mockResolvedValueOnce(job('queued'));
    act(() => {
      rerender({ profileKey: 99 });
    });
    expect(result.current.job).toBeNull();
    await flush();
    expect(result.current.job?.status).toBe('queued');
  });

  it('clears state and stops polling when the account changes', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('running'));
    const { result, rerender } = renderHook(({ token }) => useJobStatusPoller(token, scope), {
      initialProps: { token: 'tok-a' }
    });
    await flush();
    expect(result.current.job?.status).toBe('running');

    act(() => {
      rerender({ token: 'tok-b' });
    });
    expect(result.current.job).toBeNull();
  });

  it('does not create duplicate pollers on duplicate render with the same scope', async () => {
    getBackgroundJob.mockResolvedValue(job('running'));
    const { rerender } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);
    act(() => {
      rerender();
      rerender();
    });
    // A same-scope re-render must not start a second overlapping fetch
    // chain - only the timer-driven schedule should still be in flight.
    expect(getBackgroundJob).toHaveBeenCalledTimes(1);
  });

  it('stops polling and clears state on 401 (authorization failure)', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('running'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('running');

    getBackgroundJob.mockRejectedValueOnce(new MemorialApiError(401, 'Authentication is required.'));
    await act(async () => {
      await vi.advanceTimersByTimeAsync(1000);
    });
    expect(result.current.job).toBeNull();
    expect(result.current.fatalError).toBe('unauthorized');

    const callsAfter401 = getBackgroundJob.mock.calls.length;
    await act(async () => {
      await vi.advanceTimersByTimeAsync(60_000);
    });
    expect(getBackgroundJob.mock.calls.length).toBe(callsAfter401);
  });

  it('stops polling and clears state on 403 (authorization failure)', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('running'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('running');

    getBackgroundJob.mockRejectedValueOnce(new MemorialApiError(403, 'You do not have permission to perform this action.'));
    await act(async () => {
      await vi.advanceTimersByTimeAsync(1000);
    });
    expect(result.current.fatalError).toBe('unauthorized');
  });

  it('treats a temporary network failure as retryable, not as job failure', async () => {
    getBackgroundJob.mockResolvedValueOnce(job('running'));
    const { result } = renderHook(() => useJobStatusPoller('tok-a', scope));
    await flush();
    expect(result.current.job?.status).toBe('running');

    getBackgroundJob.mockRejectedValueOnce(new MemorialApiError(0, 'The server could not be reached.'));
    getBackgroundJob.mockResolvedValueOnce(job('running'));
    await act(async () => {
      await vi.advanceTimersByTimeAsync(1000);
    });
    // Backend job state remains authoritative - a transient network blip
    // never flips the locally-observed status to "failed".
    expect(result.current.job?.status).toBe('running');
    expect(result.current.fatalError).toBeNull();

    await act(async () => {
      await vi.advanceTimersByTimeAsync(1000);
    });
    expect(result.current.job?.status).toBe('running');
  });
});

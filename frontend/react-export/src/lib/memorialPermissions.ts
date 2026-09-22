import type { ContributionRead, MemorialRole } from '../types/memorial';

export function canInvite(role: MemorialRole): boolean {
  return role === 'owner';
}

/** Owner-only: soft-revoke non-owner members. Backend enforces independently. */
export function canManageMembers(role: MemorialRole): boolean {
  return role === 'owner';
}

/** Canonical owned-vs-shared rule for dashboard grouping. */
export function isOwnedMemorial(role: MemorialRole): boolean {
  return role === 'owner';
}

export function partitionMemorialsByOwnership<T extends { current_user_role: MemorialRole; id: number }>(
  memorials: T[]
): { owned: T[]; shared: T[] } {
  const owned: T[] = [];
  const shared: T[] = [];
  for (const memorial of memorials) {
    if (isOwnedMemorial(memorial.current_user_role)) {
      owned.push(memorial);
    } else {
      shared.push(memorial);
    }
  }
  return { owned, shared };
}

export function canReview(role: MemorialRole): boolean {
  return role === 'owner' || role === 'trusted_reviewer';
}

export function canSubmitContribution(role: MemorialRole): boolean {
  return role === 'owner' || role === 'trusted_reviewer' || role === 'contributor';
}

export function isActiveMemoryEligible(contribution: ContributionRead): boolean {
  return contribution.active_memory_eligible && contribution.status === 'approved' && contribution.is_current;
}

/** Task 65.5: editing memorial metadata, editing/clearing the biography,
 * and deleting the memorial are all owner-only - the backend enforces this
 * independently (DIRECT_MEMORY_WRITE capability for biography, direct
 * `user_id` ownership for memorial update/delete), this just keeps the
 * destructive/edit controls out of contributor/reviewer/viewer UI. */
export function canEditMemorial(role: MemorialRole): boolean {
  return role === 'owner';
}

export function canClearBiography(role: MemorialRole): boolean {
  return role === 'owner';
}

export function canDeleteMemorial(role: MemorialRole): boolean {
  return role === 'owner';
}

import type { ContributionRead, MemorialRole } from '../types/memorial';

export function canInvite(role: MemorialRole): boolean {
  return role === 'owner';
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

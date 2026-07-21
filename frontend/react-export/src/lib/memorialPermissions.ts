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

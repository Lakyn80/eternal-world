import { describe, expect, it } from 'vitest';
import {
  canEditOwnContribution,
  canInvite,
  canManageMembers,
  canReview,
  canSubmitContribution,
  isActiveMemoryEligible,
  isOwnedMemorial,
  partitionMemorialsByOwnership
} from './memorialPermissions';
import type { ContributionRead } from '../types/memorial';

describe('memorialPermissions', () => {
  it('only the owner can invite', () => {
    expect(canInvite('owner')).toBe(true);
    expect(canInvite('trusted_reviewer')).toBe(false);
    expect(canInvite('contributor')).toBe(false);
    expect(canInvite('viewer')).toBe(false);
  });

  it('only the owner can manage (soft-revoke) members', () => {
    expect(canManageMembers('owner')).toBe(true);
    expect(canManageMembers('trusted_reviewer')).toBe(false);
    expect(canManageMembers('contributor')).toBe(false);
    expect(canManageMembers('viewer')).toBe(false);
  });

  it('partitions memorials by current_user_role ownership without duplicates', () => {
    const memorials = [
      { id: 1, current_user_role: 'owner' as const },
      { id: 2, current_user_role: 'contributor' as const },
      { id: 3, current_user_role: 'trusted_reviewer' as const },
      { id: 4, current_user_role: 'viewer' as const },
    ];
    expect(isOwnedMemorial('owner')).toBe(true);
    expect(isOwnedMemorial('contributor')).toBe(false);
    const { owned, shared } = partitionMemorialsByOwnership(memorials);
    expect(owned.map((item) => item.id)).toEqual([1]);
    expect(shared.map((item) => item.id)).toEqual([2, 3, 4]);
    expect(owned.length + shared.length).toBe(memorials.length);
  });

  it('owner and trusted_reviewer can review; contributor and viewer cannot', () => {
    expect(canReview('owner')).toBe(true);
    expect(canReview('trusted_reviewer')).toBe(true);
    expect(canReview('contributor')).toBe(false);
    expect(canReview('viewer')).toBe(false);
  });

  it('viewer alone cannot submit a contribution', () => {
    expect(canSubmitContribution('owner')).toBe(true);
    expect(canSubmitContribution('trusted_reviewer')).toBe(true);
    expect(canSubmitContribution('contributor')).toBe(true);
    expect(canSubmitContribution('viewer')).toBe(false);
  });

  it('Phase 5C: edit own only for draft/needs_review matching current user email', () => {
    expect(
      canEditOwnContribution({ status: 'needs_review', author_email: 'me@example.com' }, 'me@example.com')
    ).toBe(true);
    expect(canEditOwnContribution({ status: 'draft', author_email: 'Me@Example.com' }, 'me@example.com')).toBe(true);
    expect(
      canEditOwnContribution({ status: 'approved', author_email: 'me@example.com' }, 'me@example.com')
    ).toBe(false);
    expect(
      canEditOwnContribution({ status: 'archived', author_email: 'me@example.com' }, 'me@example.com')
    ).toBe(false);
    expect(
      canEditOwnContribution({ status: 'needs_review', author_email: 'other@example.com' }, 'me@example.com')
    ).toBe(false);
    expect(canEditOwnContribution({ status: 'needs_review', author_email: 'me@example.com' }, null)).toBe(false);
  });

  it('active-memory eligibility requires approved, current, and eligible', () => {
    const base: ContributionRead = {
      id: 1,
      profile_id: 1,
      author_user_id: 1,
      author_email: 'a@example.com',
      title: 't',
      memory_text: 'm',
      source_language: 'cs',
      source_note: null,
      privacy_scope: 'all_family',
      status: 'approved',
      is_current: true,
      supersedes_contribution_id: null,
      reviewed_at: null,
      reviewed_by_user_id: null,
      review_note: null,
      rejection_reason: null,
      active_memory_eligible: true,
      indexing_status: { state: 'not_applicable', indexed_at: null, attempt_count: 0, failure_reason: null },
      created_at: '2026-01-01T00:00:00Z',
      updated_at: '2026-01-01T00:00:00Z'
    };
    expect(isActiveMemoryEligible(base)).toBe(true);
    expect(isActiveMemoryEligible({ ...base, is_current: false })).toBe(false);
    expect(isActiveMemoryEligible({ ...base, status: 'needs_review' })).toBe(false);
    expect(isActiveMemoryEligible({ ...base, active_memory_eligible: false })).toBe(false);
  });
});

/**
 * Task 65.7 (Part G.50): scans rendered output for forbidden raw backend
 * enum tokens - fails if the Czech (or Russian) UI ever shows a raw
 * English/Russian internal status/role/privacy-scope value instead of a
 * localized label.
 */
import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { CandidatesReviewSection, COPY, ContributionForm, ContributionList, MembersSection } from './MemorialWorkspace';
import type { ContributionRead, MembershipRead, MemoryCandidateEnrichmentRead } from '../types/memorial';
import * as api from '../lib/memorialApi';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    listMemoryCandidates: vi.fn(),
    ownerReviewCandidate: vi.fn(),
    indexCandidateMemory: vi.fn(),
    getCandidateHistory: vi.fn()
  };
});

// Every raw token the task spec explicitly calls out as forbidden in the
// Czech UI (Part G.50), plus a few more from the full enum inventory.
const FORBIDDEN_RAW_TOKENS = [
  'private_owner',
  'selected_family',
  'all_family',
  'public_legacy',
  'needs_review',
  'pending_index',
  'initial_claim',
  'clarification_answer',
  'trusted_reviewer',
  'contributor',
  'archived',
  'superseded',
  'draft'
];

function candidateFixture(overrides: Partial<MemoryCandidateEnrichmentRead> = {}): MemoryCandidateEnrichmentRead {
  return {
    candidate_id: 1,
    avatar_id: 'avatar-1',
    profile_id: 7,
    memory_type: 'general',
    enrichment_status: 'ready_for_owner_review',
    review_status: 'needs_review',
    dispute_status: 'none',
    privacy_scope: 'private_owner',
    unresolved_clarification_count: 0,
    finalized_memory_text: 'Text.',
    finalized_at: null,
    finalized_by: null,
    owner_reviewed_at: null,
    owner_reviewed_by: null,
    contribution_count: 1,
    next_clarification_question: null,
    promotion_id: null,
    promotion_status: null,
    searchable_as_fact: false,
    explicit_indexing_required: false,
    ...overrides
  };
}

function assertNoRawTokens(container: HTMLElement) {
  const text = container.textContent ?? '';
  for (const token of FORBIDDEN_RAW_TOKENS) {
    expect(text).not.toContain(token);
  }
}

describe('Czech UI raw-enum scan', () => {
  const t = COPY.cs;

  it('CandidatesReviewSection never shows a raw privacy_scope/review_status/dispute_status', async () => {
    vi.mocked(api.listMemoryCandidates).mockResolvedValue([
      candidateFixture({ finalized_memory_text: 'Text one.', privacy_scope: 'private_owner', review_status: 'needs_review' }),
      candidateFixture({ candidate_id: 2, finalized_memory_text: 'Text two.', privacy_scope: 'selected_family', dispute_status: 'disputed' }),
      candidateFixture({
        candidate_id: 3,
        finalized_memory_text: 'Text three.',
        privacy_scope: 'all_family',
        review_status: 'approved',
        promotion_id: 9,
        promotion_status: 'pending_index',
        explicit_indexing_required: true
      })
    ]);
    const { container } = render(<CandidatesReviewSection isOwner lang="cs" profileId={7} t={t} token="tok" />);
    await screen.findByText('Text three.');
    assertNoRawTokens(container);
  });

  it('ContributionForm privacy-scope select never shows raw option values', () => {
    const { container } = render(<ContributionForm onSubmitted={() => {}} profileId={7} t={t} token="tok" />);
    assertNoRawTokens(container);
  });

  it('ContributionList never shows raw status values', () => {
    const contributions: ContributionRead[] = [
      {
        id: 1,
        profile_id: 7,
        author_user_id: 1,
        author_email: 'a@example.com',
        title: 'Title',
        memory_text: 'Text',
        source_note: null,
        privacy_scope: 'private_owner',
        status: 'needs_review',
        is_current: true,
        supersedes_contribution_id: null,
        reviewed_at: null,
        reviewed_by_user_id: null,
        review_note: null,
        rejection_reason: null,
        active_memory_eligible: false,
        indexing_status: { state: 'not_applicable', indexed_at: null, attempt_count: 0, failure_reason: null },
        created_at: '2026-01-01T00:00:00Z',
        updated_at: '2026-01-01T00:00:00Z'
      }
    ];
    const { container } = render(<ContributionList contributions={contributions} lang="cs" t={t} />);
    assertNoRawTokens(container);
  });

  it('MembersSection never shows a raw role value', () => {
    const members: MembershipRead[] = [
      {
        id: 1,
        profile_id: 7,
        user_id: 1,
        email: 'owner@example.com',
        full_name: 'Owner',
        role: 'owner',
        status: 'active',
        created_at: '2026-01-01T00:00:00Z',
        updated_at: '2026-01-01T00:00:00Z'
      },
      {
        id: 2,
        profile_id: 7,
        user_id: 2,
        email: 'reviewer@example.com',
        full_name: 'Reviewer',
        role: 'trusted_reviewer',
        status: 'active',
        created_at: '2026-01-01T00:00:00Z',
        updated_at: '2026-01-01T00:00:00Z'
      },
      {
        id: 3,
        profile_id: 7,
        user_id: 3,
        email: 'carol@example.com',
        full_name: 'Carol',
        role: 'contributor',
        status: 'active',
        created_at: '2026-01-01T00:00:00Z',
        updated_at: '2026-01-01T00:00:00Z'
      }
    ];
    const { container } = render(<MembersSection members={members} t={t} />);
    assertNoRawTokens(container);
    // Confirms the fix directly - "owner" must render as the localized
    // "Vlastník", not the raw English word.
    expect(screen.getByText('Vlastník')).toBeInTheDocument();
    expect(screen.getByText('Důvěryhodný kontrolor')).toBeInTheDocument();
    expect(screen.getByText('Přispěvatel')).toBeInTheDocument();
  });
});

describe('locale dictionary completeness', () => {
  it('every Copy key present in English is also present (non-empty) in Czech and Russian', () => {
    const enKeys = Object.keys(COPY.en) as (keyof typeof COPY.en)[];
    for (const key of enKeys) {
      expect(COPY.cs[key], `missing/empty Czech key: ${String(key)}`).toBeTruthy();
      expect(COPY.ru[key], `missing/empty Russian key: ${String(key)}`).toBeTruthy();
    }
  });
});

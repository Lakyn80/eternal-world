import { FormEvent, type ReactNode, useEffect, useMemo, useRef, useState } from 'react';
import type { Lang } from '../i18n';
import {
  acceptInvitation,
  answerBiographerQuestion,
  answerCandidateClarification,
  clearBiography,
  createMemorial,
  deleteMemorial,
  fetchMemorial,
  getActiveChat,
  getBiographerEligibility,
  getBillingLimits,
  getBiographyStatus,
  getBiographerResume,
  getCandidateHistory,
  getNextBiographerQuestion,
  getSession,
  indexCandidateMemory,
  inviteParticipant,
  listBiographyMemoryEntries,
  listChatMessages,
  listContributions,
  listMembers,
  listMemorials,
  listMemoryCandidates,
  listReviewQueue,
  login,
  logoutSession,
  MemorialApiError,
  ownerReviewCandidate,
  register,
  resetChat,
  retryContributionIndexing,
  reviewContribution,
  sendChatMessage,
  setUnauthorizedHandler,
  postponeBiographerQuestion,
  skipBiographerQuestion,
  startBiographyIngestion,
  submitContribution,
  updateBiography,
  updateMemorialMetadata
} from '../lib/memorialApi';
import { canInvite, canReview, canSubmitContribution, isActiveMemoryEligible } from '../lib/memorialPermissions';
import { APP_ROOT_PATH, buildMemorialPath, navigate, parseAppRoute, usePathname } from '../lib/router';
import { useJobStatusPoller } from '../hooks/useJobStatusPoller';
import type {
  AuthSession,
  BackgroundJobRead,
  BackgroundJobStatusValue,
  BiographerBlockedReason,
  BiographerEligibilityRead,
  BiographerQuestionRead,
  BillingLimitsRead,
  BiographyMemoryEntryRead,
  BiographyStatusRead,
  CandidateHistoryRead,
  ChatMessageRead,
  ClarificationQuestionRead,
  ContributionRead,
  InvitationCreateResponse,
  InvitableMemorialRole,
  MembershipRead,
  MemoryCandidateEnrichmentRead,
  MemorialRead,
  MemorialRole,
  OwnerReviewCandidateAction,
  PrivacyScope,
  WorkspaceTab
} from '../types/memorial';

export type Copy = {
  kicker: string;
  title: string;
  subtitle: string;
  signInTitle: string;
  signInHelp: string;
  signIn: string;
  createAccount: string;
  fullName: string;
  email: string;
  password: string;
  signedInAs: string;
  signOut: string;
  sessionExpired: string;
  refresh: string;
  chat: string;
  chatEmpty: string;
  chatPlaceholder: string;
  chatSend: string;
  chatYou: string;
  chatAvatar: string;
  chatReset: string;
  chatResetConfirmTitle: string;
  chatResetConfirmYes: string;
  chatResetConfirmCancel: string;
  chatResetDone: string;
  biography: string;
  biographyIntro: string;
  biographyPlaceholder: string;
  biographySave: string;
  biographyStartIngestion: string;
  biographyConfirmNote: string;
  biographyStatusDraft: string;
  biographyStatusReady: string;
  biographyStatusIngesting: string;
  biographyStatusIndexed: string;
  biographyStatusFailed: string;
  biographyStatusStale: string;
  biographyRetry: string;
  biographyTextLabel: string;
  biographySavedNotIndexed: string;
  biographySavedNowStale: string;
  biographyLastIndexed: string;
  biographyFailureReason: string;
  biographyAttempts: string;
  biographyUpToDate: string;
  biographyConflict: string;
  biographyConfirmStartTitle: string;
  biographyConfirmStartBody: string;
  biographyConfirmStartYes: string;
  biographyConfirmCancel: string;
  confirmedMemoriesTitle: string;
  confirmedMemoriesIntro: string;
  confirmedMemoriesEmpty: string;
  confirmedMemoriesIndexedBadge: string;
  confirmedMemoriesPendingBadge: string;
  confirmedMemoriesFailedBadge: string;
  biographer: string;
  biographerIntro: string;
  biographerBlockedMissing: string;
  biographerBlockedNotIndexed: string;
  biographerBlockedIndexing: string;
  biographerBlockedStale: string;
  biographerBlockedActive: string;
  biographerBlockedWaitingReview: string;
  biographerBlockedPermission: string;
  biographerGoToBiography: string;
  biographerGenerationFailed: string;
  biographerDone: string;
  biographerAnswerPlaceholder: string;
  biographerSubmit: string;
  biographerSkip: string;
  biographerPostpone: string;
  biographerTopicLabel: string;
  biographerRelevanceTemplate: string;
  biographerMoreDetailsNeeded: string;
  biographerReadyForReview: string;
  biographerCandidatePendingIndex: string;
  biographerCandidateIndexed: string;
  biographerGoToReview: string;
  biographerTopicChildhood: string;
  biographerTopicFamily: string;
  biographerTopicEducation: string;
  biographerTopicWork: string;
  biographerTopicRelationships: string;
  biographerTopicPlaces: string;
  biographerTopicTraditions: string;
  biographerTopicValues: string;
  candidatesTitle: string;
  candidatesSubtitle: string;
  candidatesEmpty: string;
  candidateConfirm: string;
  candidateEditAndConfirm: string;
  candidateEditTextareaLabel: string;
  candidateApproveMultiplePerspectives: string;
  candidateReject: string;
  candidateRejectReasonLabel: string;
  candidateRequestDetails: string;
  candidateMarkDisputed: string;
  candidateIndexButton: string;
  candidateIndexedLabel: string;
  candidatePendingIndexLabel: string;
  candidatePendingIndexNotice: string;
  candidateAlreadyIndexed: string;
  candidateIndexingFailedLabel: string;
  candidateIndexRetryButton: string;
  candidateIndexConfirmTitle: string;
  candidateIndexConfirmBody: string;
  candidateIndexConfirmYes: string;
  candidatePrivacyScopeLabel: string;
  candidatePrivacyPrivateOwner: string;
  candidatePrivacySelectedFamily: string;
  candidatePrivacyAllFamily: string;
  candidatePrivacyPublicLegacy: string;
  candidateViewHistory: string;
  candidateHideHistory: string;
  candidateHistoryContributions: string;
  candidateHistoryClarifications: string;
  candidateHistoryEmpty: string;
  candidateClarificationPending: string;
  candidateClarificationPlaceholder: string;
  candidateClarificationSubmit: string;
  overviewBiographyLabel: string;
  overviewBiographyNotSaved: string;
  overviewBiographyIndexed: string;
  overviewBiographyNotIndexed: string;
  overviewBiographyStale: string;
  overviewBiographerLabel: string;
  overviewBiographerQuestionActive: string;
  overviewBiographerNoQuestion: string;
  overviewReviewLabel: string;
  overviewReviewClarifications: string;
  overviewReviewCandidates: string;
  overviewIndexingLabel: string;
  overviewIndexingPending: string;
  overviewIndexingDone: string;
  overviewNextAction: string;
  overviewNextActionAddBiography: string;
  overviewNextActionStartIndexing: string;
  overviewNextActionAnswerQuestion: string;
  overviewNextActionCompleteClarification: string;
  overviewNextActionReviewCandidate: string;
  overviewNextActionIndexApproved: string;
  overviewNextActionTestChat: string;
  overviewAllCaughtUp: string;
  goAction: string;
  cancelAction: string;
  createMemorial: string;
  name: string;
  description: string;
  yourMemorials: string;
  empty: string;
  openWorkspace: string;
  overview: string;
  contributions: string;
  review: string;
  members: string;
  invitations: string;
  role: string;
  roleOwner: string;
  roleTrustedReviewer: string;
  roleContributor: string;
  roleViewer: string;
  roleSystem: string;
  statusDraft: string;
  statusNeedsReview: string;
  statusApproved: string;
  statusRejected: string;
  statusArchived: string;
  statusSuperseded: string;
  statusPendingIndex: string;
  statusIndexed: string;
  statusPromotionFailed: string;
  statusPromotionCancelled: string;
  disputeStatusNone: string;
  disputeStatusDisputed: string;
  disputeStatusResolved: string;
  clarificationStatusPending: string;
  clarificationStatusAnswered: string;
  clarificationStatusSkipped: string;
  clarificationStatusCancelled: string;
  contributionTypeInitialClaim: string;
  contributionTypeClarificationAnswer: string;
  contributionTypeOwnerCorrection: string;
  contributionTypeOwnerConfirmation: string;
  contributionTypeReviewerNote: string;
  contributionTypeDisputeStatement: string;
  contributionTypeSystemNormalization: string;
  submitMemory: string;
  titleLabel: string;
  memoryText: string;
  sourceNote: string;
  privacyScope: string;
  submitForReview: string;
  viewerReadOnly: string;
  noContributions: string;
  notActiveMemory: string;
  activeMemory: string;
  noPending: string;
  approve: string;
  reject: string;
  archive: string;
  inviteParticipant: string;
  inviteHelp: string;
  invitationCreated: string;
  devToken: string;
  tokenNote: string;
  acceptTitle: string;
  acceptHelp: string;
  acceptInvitation: string;
  invitationAccepted: string;
  noToken: string;
  creating: string;
  submitting: string;
  working: string;
  indexingPending: string;
  indexingIndexed: string;
  indexingFailed: string;
  indexingRetired: string;
  retryIndexing: string;
  retryIndexingSuccess: string;
  // Task 65.9.1 (Part F/G): localized labels for every BackgroundJob
  // status the async job-status poller can observe, covering both
  // "Index memory" and contribution retry-indexing.
  jobStatusPending: string;
  jobStatusQueued: string;
  jobStatusProcessing: string;
  jobStatusRetryScheduled: string;
  jobStatusRecoveryPending: string;
  jobStatusSucceeded: string;
  jobStatusFailed: string;
  jobStatusCancelled: string;
  jobStatusUnauthorized: string;
  jobStatusNetworkRetrying: string;
  backToSite: string;
  planLimitReachedMessage: string;
  openExistingMemorial: string;
  biographyIndexingExplanation: string;
  editMemorial: string;
  saveChanges: string;
  clearBiography: string;
  clearBiographyConfirmTitle: string;
  clearBiographyConfirmBody: string;
  clearBiographyConfirmYes: string;
  deleteMemorial: string;
  deleteMemorialConfirmTitle: string;
  deleteMemorialConfirmBody: string;
  deleteMemorialConfirmLabel: string;
  deleteMemorialConfirmButton: string;
  deleteMemorialPartialFailure: string;
  backToMemorials: string;
};

export const COPY: Record<Lang, Copy> = {
  en: {
    kicker: 'Family access control',
    title: 'Private memorial workspace',
    subtitle: 'Create a memorial, invite family members, collect contributions and approve only memories that should become active avatar knowledge.',
    signInTitle: 'Sign in to continue',
    signInHelp: 'Use a real account from the backend. The frontend keeps the access token only in memory.',
    signIn: 'Sign in',
    createAccount: 'Create account',
    fullName: 'Full name',
    email: 'Email',
    password: 'Password',
    signedInAs: 'Signed in as',
    signOut: 'Sign out',
    sessionExpired: 'Your session has expired. Please sign in again.',
    refresh: 'Refresh',
    chat: 'Chat',
    chatEmpty: 'No messages yet. Say hello to start the conversation.',
    chatPlaceholder: 'Write a message...',
    chatSend: 'Send',
    chatYou: 'You',
    chatAvatar: 'Avatar',
    chatReset: 'Reset chat',
    chatResetConfirmTitle: 'Clear the current chat and start a new one?',
    chatResetConfirmYes: 'Yes, start new chat',
    chatResetConfirmCancel: 'Cancel',
    chatResetDone: 'New chat is ready.',
    biography: 'Biography',
    biographyIntro: 'Write the memorial\'s initial life story. Nothing becomes avatar memory until you explicitly start indexing.',
    biographyPlaceholder: 'Write the biography here...',
    biographySave: 'Save biography',
    biographyStartIngestion: 'Start indexing',
    biographyConfirmNote: 'After indexing, the avatar may use this biography in its answers.',
    biographyStatusDraft: 'Draft - not indexed yet',
    biographyStatusReady: 'Queued for indexing',
    biographyStatusIngesting: 'Indexing in progress...',
    biographyStatusIndexed: 'Indexed - part of avatar memory',
    biographyStatusFailed: 'Indexing failed',
    biographyStatusStale: 'Edited since last indexing - re-index to update avatar memory',
    biographyRetry: 'Retry indexing',
    biographyTextLabel: 'Biography text',
    biographySavedNotIndexed: 'Biography saved. It has not been indexed yet.',
    biographySavedNowStale: 'New version saved. Re-index it to update the avatar memory - the previously indexed version is still active until then.',
    biographyLastIndexed: 'Last indexed',
    biographyFailureReason: 'Reason',
    biographyAttempts: 'Attempts',
    biographyUpToDate: 'Indexed and up to date - no action needed.',
    biographyConflict: 'An indexing job for this biography is already running.',
    biographyConfirmStartTitle: 'Start indexing this biography?',
    biographyConfirmStartBody: 'After indexing, the avatar may use this biography in its answers.',
    biographyConfirmStartYes: 'Yes, start indexing',
    biographyConfirmCancel: 'Cancel',
    confirmedMemoriesTitle: 'Confirmed memories',
    confirmedMemoriesIntro: 'Memories the AI Biographer proposed and you approved. They complement the biography text above and are only shown here once approved.',
    confirmedMemoriesEmpty: 'No approved biographer memories yet.',
    confirmedMemoriesIndexedBadge: 'Searchable by the avatar',
    confirmedMemoriesPendingBadge: 'Approved, not yet searchable',
    confirmedMemoriesFailedBadge: 'Indexing failed',
    biographer: 'Biographer',
    biographerIntro: 'The AI Biographer works from the indexed biography and approved memories. It first figures out what is already known, then asks one question that adds to the story. Answers are never indexed automatically - they go through review first.',
    biographerBlockedMissing: 'Save the biography first.',
    biographerBlockedNotIndexed: 'Index the biography before starting the Biographer.',
    biographerBlockedIndexing: 'Biography indexing is in progress. The Biographer will be available once it finishes.',
    biographerBlockedStale: 'The biography changed since it was last indexed. Re-index it to let the Biographer use the current text.',
    biographerBlockedActive: 'Please finish answering the current clarification question below before continuing.',
    biographerBlockedWaitingReview: 'The current topic has a memory candidate waiting for owner review. Another topic will be offered once you continue.',
    biographerBlockedPermission: 'You do not have permission to use the Biographer for this memorial.',
    biographerGoToBiography: 'Start biography indexing',
    biographerGenerationFailed: 'The Biographer could not prepare a question right now. Please try again.',
    biographerDone: 'All Biographer topics for this memorial have been covered.',
    biographerAnswerPlaceholder: 'Write your answer...',
    biographerSubmit: 'Submit answer',
    biographerSkip: 'Skip this question',
    biographerPostpone: 'Ask me later',
    biographerTopicLabel: 'Topic',
    biographerRelevanceTemplate: 'This question adds to the topic {topic}.',
    biographerMoreDetailsNeeded: 'More details required',
    biographerReadyForReview: 'Ready for owner review.',
    biographerCandidatePendingIndex: 'Approved and waiting to be indexed.',
    biographerCandidateIndexed: 'This memory has been indexed.',
    biographerGoToReview: 'Go to Review',
    biographerTopicChildhood: 'Childhood',
    biographerTopicFamily: 'Family',
    biographerTopicEducation: 'Education',
    biographerTopicWork: 'Work',
    biographerTopicRelationships: 'Relationships',
    biographerTopicPlaces: 'Places',
    biographerTopicTraditions: 'Traditions',
    biographerTopicValues: 'Values',
    candidatesTitle: 'Biographer memories',
    candidatesSubtitle: 'Memory candidates awaiting or completing owner review - separate from membership/family contribution requests above.',
    candidatesEmpty: 'No Biographer-sourced memories yet.',
    candidateConfirm: 'Confirm',
    candidateEditAndConfirm: 'Edit and confirm',
    candidateEditTextareaLabel: 'Edit the finalized memory text',
    candidateApproveMultiplePerspectives: 'Approve as multiple perspectives',
    candidateReject: 'Reject',
    candidateRejectReasonLabel: 'Reason (optional)',
    candidateRequestDetails: 'Request more details',
    candidateMarkDisputed: 'Mark disputed',
    candidateIndexButton: 'Index memory',
    candidateIndexedLabel: 'Indexed and searchable',
    candidatePendingIndexLabel: 'Approved, not yet indexed',
    candidatePendingIndexNotice: 'Memory approved. Status: pending_index. The memory is approved but not yet searchable by the avatar.',
    candidateAlreadyIndexed: 'This memory is already indexed.',
    candidateIndexingFailedLabel: 'Indexing failed',
    candidateIndexRetryButton: 'Retry indexing',
    candidateIndexConfirmTitle: 'Index this memory?',
    candidateIndexConfirmBody: 'This creates an embedding and makes the approved memory available to avatar retrieval.',
    candidateIndexConfirmYes: 'Yes, index memory',
    candidatePrivacyScopeLabel: 'Privacy scope',
    candidatePrivacyPrivateOwner: 'Owner only',
    candidatePrivacySelectedFamily: 'Selected family members',
    candidatePrivacyAllFamily: 'All family members',
    candidatePrivacyPublicLegacy: 'Public legacy',
    candidateViewHistory: 'View history',
    candidateHideHistory: 'Hide history',
    candidateHistoryContributions: 'Contribution history',
    candidateHistoryClarifications: 'Clarification questions',
    candidateHistoryEmpty: 'No entries yet.',
    candidateClarificationPending: 'The Biographer needs one more detail before this can be reviewed:',
    candidateClarificationPlaceholder: 'Write your answer...',
    candidateClarificationSubmit: 'Submit',
    overviewBiographyLabel: 'Biography',
    overviewBiographyNotSaved: 'Not saved yet',
    overviewBiographyIndexed: 'Indexed',
    overviewBiographyNotIndexed: 'Not indexed',
    overviewBiographyStale: 'Edited - needs re-indexing',
    overviewBiographerLabel: 'Biographer',
    overviewBiographerQuestionActive: 'A question is waiting for your answer',
    overviewBiographerNoQuestion: 'No active question',
    overviewReviewLabel: 'Review',
    overviewReviewClarifications: 'clarifications required',
    overviewReviewCandidates: 'candidates waiting for review',
    overviewIndexingLabel: 'Indexing',
    overviewIndexingPending: 'approved memories waiting for indexing',
    overviewIndexingDone: 'indexed memories',
    overviewNextAction: 'Next step',
    overviewNextActionAddBiography: 'Add a biography',
    overviewNextActionStartIndexing: 'Start biography indexing',
    overviewNextActionAnswerQuestion: 'Answer the Biographer question',
    overviewNextActionCompleteClarification: 'Complete the pending clarification',
    overviewNextActionReviewCandidate: 'Review a memory candidate',
    overviewNextActionIndexApproved: 'Index an approved memory',
    overviewNextActionTestChat: 'Test the avatar in Chat',
    overviewAllCaughtUp: 'Everything is up to date.',
    goAction: 'Go',
    cancelAction: 'Cancel',
    createMemorial: 'Create memorial',
    name: 'Name',
    description: 'Description',
    yourMemorials: 'Your memorials',
    empty: 'No memorials are available for this account yet.',
    openWorkspace: 'Open workspace',
    overview: 'Overview',
    contributions: 'Contributions',
    review: 'Review',
    members: 'Members',
    invitations: 'Invitations',
    role: 'Role',
    roleOwner: 'Owner',
    roleTrustedReviewer: 'Trusted reviewer',
    roleContributor: 'Contributor',
    roleViewer: 'Viewer',
    roleSystem: 'System',
    statusDraft: 'Saved, not indexed',
    statusNeedsReview: 'Waiting for review',
    statusApproved: 'Approved',
    statusRejected: 'Rejected',
    statusArchived: 'Archived',
    statusSuperseded: 'Superseded',
    statusPendingIndex: 'Approved, waiting to be indexed',
    statusIndexed: 'Indexed',
    statusPromotionFailed: 'Indexing failed',
    statusPromotionCancelled: 'Indexing cancelled',
    disputeStatusNone: 'No dispute',
    disputeStatusDisputed: 'Disputed memory',
    disputeStatusResolved: 'Dispute resolved',
    clarificationStatusPending: 'Waiting for an answer',
    clarificationStatusAnswered: 'Answered',
    clarificationStatusSkipped: 'Skipped',
    clarificationStatusCancelled: 'Not required',
    contributionTypeInitialClaim: 'Original answer',
    contributionTypeClarificationAnswer: 'Clarification answer',
    contributionTypeOwnerCorrection: 'Owner correction',
    contributionTypeOwnerConfirmation: 'Owner confirmation',
    contributionTypeReviewerNote: 'Reviewer note',
    contributionTypeDisputeStatement: 'Dispute statement',
    contributionTypeSystemNormalization: 'System update',
    submitMemory: 'Submit a memory',
    titleLabel: 'Title',
    memoryText: 'Memory text',
    sourceNote: 'Source note',
    privacyScope: 'Privacy scope',
    submitForReview: 'Submit for review',
    viewerReadOnly: 'Viewers cannot submit memories.',
    noContributions: 'No contributions are visible for this role.',
    notActiveMemory: 'Not active memory',
    activeMemory: 'Active-memory eligible',
    noPending: 'No family contributions are waiting for review. (Biographer-sourced memories are listed separately below.)',
    approve: 'Approve',
    reject: 'Reject',
    archive: 'Archive',
    inviteParticipant: 'Invite participant',
    inviteHelp: 'Owners can invite trusted reviewers, contributors or viewers.',
    invitationCreated: 'Invitation created.',
    devToken: 'Development invite token',
    tokenNote: 'Shown because the backend returned it for dev/test flow. It is not stored in browser storage.',
    acceptTitle: 'Accept invitation',
    acceptHelp: 'Sign in with the invited account. The token is used once from the URL.',
    acceptInvitation: 'Accept invitation',
    invitationAccepted: 'Invitation accepted.',
    noToken: 'Invitation token is missing.',
    creating: 'Creating',
    submitting: 'Submitting',
    working: 'Working',
    indexingPending: 'Approved, indexing pending',
    indexingIndexed: 'Indexed and searchable',
    indexingFailed: 'Indexing failed',
    indexingRetired: 'No longer active evidence',
    retryIndexing: 'Retry indexing',
    retryIndexingSuccess: 'Indexing retried.',
    jobStatusPending: 'Waiting to start',
    jobStatusQueued: 'Queued for indexing',
    jobStatusProcessing: 'Indexing in progress',
    jobStatusRetryScheduled: 'Temporary issue - retrying automatically',
    jobStatusRecoveryPending: 'Recovering the indexing service - retrying automatically',
    jobStatusSucceeded: 'Indexed and searchable',
    jobStatusFailed: 'Indexing failed',
    jobStatusCancelled: 'Indexing cancelled',
    jobStatusUnauthorized: 'Sign in again to see the latest indexing status.',
    jobStatusNetworkRetrying: 'Reconnecting to check indexing status...',
    backToSite: 'Back to site',
    planLimitReachedMessage:
      'Your current plan already includes the maximum number of memorials.\nOpen your existing memorial to edit its biography.',
    openExistingMemorial: 'Open existing memorial',
    biographyIndexingExplanation:
      'The biography is saved, but the avatar cannot use it yet. Start indexing to create memory embeddings.',
    editMemorial: 'Edit memorial',
    saveChanges: 'Save changes',
    clearBiography: 'Clear biography',
    clearBiographyConfirmTitle: 'Clear this biography?',
    clearBiographyConfirmBody:
      'This removes the saved biography text and any memory created from it. Membership, invitations and other approved memories are not affected.',
    clearBiographyConfirmYes: 'Yes, clear biography',
    deleteMemorial: 'Delete memorial',
    deleteMemorialConfirmTitle: 'Delete this memorial?',
    deleteMemorialConfirmBody:
      'This permanently deletes the memorial, its biography, members, invitations, contributions and all indexed avatar memory. This cannot be undone.',
    deleteMemorialConfirmLabel: 'Type the memorial name to confirm',
    deleteMemorialConfirmButton: 'Permanently delete',
    deleteMemorialPartialFailure: 'Deletion could not be completed safely and was cancelled. Please try again.',
    backToMemorials: 'Back to memorials'
  },
  cs: {
    kicker: 'Kontrola rodinného přístupu',
    title: 'Soukromý memorial workspace',
    subtitle: 'Vytvořte memorial, pozvěte rodinu, sbírejte vzpomínky a schvalte jen to, co se má stát aktivní znalostí avatara.',
    signInTitle: 'Přihlaste se',
    signInHelp: 'Použijte skutečný účet z backendu. Frontend drží access token pouze v paměti.',
    signIn: 'Přihlásit',
    createAccount: 'Vytvořit účet',
    fullName: 'Celé jméno',
    email: 'E-mail',
    password: 'Heslo',
    signedInAs: 'Přihlášen jako',
    signOut: 'Odhlásit',
    sessionExpired: 'Vaše přihlášení vypršelo. Přihlaste se prosím znovu.',
    refresh: 'Obnovit',
    chat: 'Chat',
    chatEmpty: 'Zatím žádné zprávy. Napište pozdrav a začněte konverzaci.',
    chatPlaceholder: 'Napište zprávu...',
    chatSend: 'Odeslat',
    chatYou: 'Vy',
    chatAvatar: 'Avatar',
    chatReset: 'Obnovit chat',
    chatResetConfirmTitle: 'Vymazat současný chat a začít nový?',
    chatResetConfirmYes: 'Ano, začít nový chat',
    chatResetConfirmCancel: 'Zrušit',
    chatResetDone: 'Nový chat je připraven.',
    biography: 'Životopis',
    biographyIntro: 'Napište počáteční životní příběh memorialu. Nic se nestane pamětí avatara, dokud výslovně nespustíte indexaci.',
    biographyPlaceholder: 'Sem napište životopis...',
    biographySave: 'Uložit životopis',
    biographyStartIngestion: 'Spustit indexaci',
    biographyConfirmNote: 'Po zaindexování může avatar tento životopis použít ve svých odpovědích.',
    biographyStatusDraft: 'Koncept - zatím neindexováno',
    biographyStatusReady: 'Čeká na indexaci',
    biographyStatusIngesting: 'Probíhá indexace...',
    biographyStatusIndexed: 'Zaindexováno - součást paměti avatara',
    biographyStatusFailed: 'Indexace selhala',
    biographyStatusStale: 'Upraveno od poslední indexace - spusťte indexaci znovu, aby se paměť avatara aktualizovala',
    biographyRetry: 'Zkusit indexaci znovu',
    biographyTextLabel: 'Text životopisu',
    biographySavedNotIndexed: 'Životopis uložen. Zatím nebyl zaindexován.',
    biographySavedNowStale: 'Nová verze uložena. Spusťte znovu indexaci, aby se aktualizovala paměť avatara - do té doby zůstává aktivní předchozí zaindexovaná verze.',
    biographyLastIndexed: 'Naposledy zaindexováno',
    biographyFailureReason: 'Důvod',
    biographyAttempts: 'Počet pokusů',
    biographyUpToDate: 'Zaindexováno a aktuální - není potřeba žádná akce.',
    biographyConflict: 'Indexace tohoto životopisu už právě probíhá.',
    biographyConfirmStartTitle: 'Spustit indexaci tohoto životopisu?',
    biographyConfirmStartBody: 'Po zaindexování může avatar tento životopis použít ve svých odpovědích.',
    biographyConfirmStartYes: 'Ano, spustit indexaci',
    biographyConfirmCancel: 'Zrušit',
    confirmedMemoriesTitle: 'Potvrzené vzpomínky',
    confirmedMemoriesIntro: 'Vzpomínky, které navrhl AI biograf a vy jste je schválili. Doplňují text životopisu výše a zobrazují se zde až po schválení.',
    confirmedMemoriesEmpty: 'Zatím žádné schválené vzpomínky od biografa.',
    confirmedMemoriesIndexedBadge: 'Vyhledatelné avatarem',
    confirmedMemoriesPendingBadge: 'Schváleno, zatím nevyhledatelné',
    confirmedMemoriesFailedBadge: 'Indexace selhala',
    biographer: 'AI biograf',
    biographerIntro: 'AI biograf vychází ze zaindexovaného životopisu a schválených vzpomínek. Nejdřív zjistí, co už je známé, a potom položí jednu otázku, která příběh doplní. Odpověď se nikdy nezaindexuje automaticky - nejprve projde kontrolou.',
    biographerBlockedMissing: 'Nejprve uložte životopis.',
    biographerBlockedNotIndexed: 'Před spuštěním biografa nejprve zaindexujte životopis.',
    biographerBlockedIndexing: 'Indexace životopisu probíhá. AI biograf bude dostupný po dokončení.',
    biographerBlockedStale: 'Životopis byl po zaindexování upraven. Zaindexujte ho znovu, aby biograf pracoval s aktuálním textem.',
    biographerBlockedActive: 'Nejprve prosím odpovězte na aktuální upřesňující otázku níže.',
    biographerBlockedWaitingReview: 'Aktuální téma má vzpomínku čekající na kontrolu vlastníkem. Další téma se nabídne po jejím vyřízení.',
    biographerBlockedPermission: 'Nemáte oprávnění používat AI biografa u tohoto memorialu.',
    biographerGoToBiography: 'Spustit indexaci životopisu',
    biographerGenerationFailed: 'AI biografovi se teď nepodařilo připravit otázku. Zkuste to prosím znovu.',
    biographerDone: 'Všechna témata AI biografa pro tento memorial už byla probrána.',
    biographerAnswerPlaceholder: 'Napište svou odpověď...',
    biographerSubmit: 'Odeslat odpověď',
    biographerSkip: 'Přeskočit otázku',
    biographerPostpone: 'Zeptat se později',
    biographerTopicLabel: 'Téma',
    biographerRelevanceTemplate: 'Tato otázka doplňuje téma {topic}.',
    biographerTopicChildhood: 'Dětství',
    biographerTopicFamily: 'Rodina',
    biographerTopicEducation: 'Vzdělání',
    biographerTopicWork: 'Práce',
    biographerTopicRelationships: 'Vztahy',
    biographerTopicPlaces: 'Místa',
    biographerTopicTraditions: 'Tradice',
    biographerTopicValues: 'Hodnoty',
    biographerMoreDetailsNeeded: 'Je potřeba více podrobností',
    biographerReadyForReview: 'Připraveno ke kontrole vlastníkem.',
    biographerCandidatePendingIndex: 'Schváleno, čeká na zaindexování.',
    biographerCandidateIndexed: 'Tato vzpomínka byla zaindexována.',
    biographerGoToReview: 'Přejít na Kontrolu',
    candidatesTitle: 'Vzpomínky od biografa',
    candidatesSubtitle: 'Vzpomínkoví kandidáti čekající na kontrolu vlastníkem nebo již zkontrolovaní - odděleno od vzpomínek/příspěvků rodiny výše.',
    candidatesEmpty: 'Zatím žádné vzpomínky od AI biografa.',
    candidateConfirm: 'Potvrdit',
    candidateEditAndConfirm: 'Upravit a potvrdit',
    candidateEditTextareaLabel: 'Upravit finální text vzpomínky',
    candidateApproveMultiplePerspectives: 'Schválit jako více pohledů',
    candidateReject: 'Odmítnout',
    candidateRejectReasonLabel: 'Důvod (nepovinné)',
    candidateRequestDetails: 'Vyžádat více podrobností',
    candidateMarkDisputed: 'Označit jako sporné',
    candidateIndexButton: 'Zaindexovat vzpomínku',
    candidateIndexedLabel: 'Zaindexováno a vyhledatelné',
    candidatePendingIndexLabel: 'Schváleno, zatím nezaindexováno',
    candidatePendingIndexNotice: 'Vzpomínka schválena. Stav: čeká na indexaci. Vzpomínka je schválena, ale avatar ji zatím nemůže vyhledat.',
    candidateAlreadyIndexed: 'Tato vzpomínka je již zaindexována.',
    candidateIndexingFailedLabel: 'Indexace selhala',
    candidateIndexRetryButton: 'Zkusit indexaci znovu',
    candidateIndexConfirmTitle: 'Zaindexovat tuto vzpomínku?',
    candidateIndexConfirmBody: 'Tím se vytvoří embedding a schválená vzpomínka bude dostupná pro vyhledávání avatarem.',
    candidateIndexConfirmYes: 'Ano, zaindexovat vzpomínku',
    candidatePrivacyScopeLabel: 'Úroveň soukromí',
    candidatePrivacyPrivateOwner: 'Jen vlastník',
    candidatePrivacySelectedFamily: 'Vybraní členové rodiny',
    candidatePrivacyAllFamily: 'Všichni členové rodiny',
    candidatePrivacyPublicLegacy: 'Veřejný odkaz',
    candidateViewHistory: 'Zobrazit historii',
    candidateHideHistory: 'Skrýt historii',
    candidateHistoryContributions: 'Historie příspěvků',
    candidateHistoryClarifications: 'Upřesňující otázky',
    candidateHistoryEmpty: 'Zatím žádné záznamy.',
    candidateClarificationPending: 'AI biograf potřebuje ještě jeden detail, než se to dá zkontrolovat:',
    candidateClarificationPlaceholder: 'Napište svou odpověď...',
    candidateClarificationSubmit: 'Odeslat',
    overviewBiographyLabel: 'Životopis',
    overviewBiographyNotSaved: 'Zatím neuloženo',
    overviewBiographyIndexed: 'Zaindexováno',
    overviewBiographyNotIndexed: 'Nezaindexováno',
    overviewBiographyStale: 'Upraveno - je potřeba nová indexace',
    overviewBiographerLabel: 'AI biograf',
    overviewBiographerQuestionActive: 'Čeká otázka na vaši odpověď',
    overviewBiographerNoQuestion: 'Žádná aktivní otázka',
    overviewReviewLabel: 'Kontrola',
    overviewReviewClarifications: 'upřesnění je potřeba doplnit',
    overviewReviewCandidates: 'kandidátů čeká na kontrolu',
    overviewIndexingLabel: 'Indexace',
    overviewIndexingPending: 'schválených vzpomínek čeká na indexaci',
    overviewIndexingDone: 'zaindexovaných vzpomínek',
    overviewNextAction: 'Další krok',
    overviewNextActionAddBiography: 'Přidat životopis',
    overviewNextActionStartIndexing: 'Spustit indexaci životopisu',
    overviewNextActionAnswerQuestion: 'Odpovědět na otázku biografa',
    overviewNextActionCompleteClarification: 'Doplnit čekající upřesnění',
    overviewNextActionReviewCandidate: 'Zkontrolovat vzpomínkového kandidáta',
    overviewNextActionIndexApproved: 'Zaindexovat schválenou vzpomínku',
    overviewNextActionTestChat: 'Vyzkoušet avatara v Chatu',
    overviewAllCaughtUp: 'Vše je aktuální.',
    goAction: 'Přejít',
    cancelAction: 'Zrušit',
    createMemorial: 'Vytvořit memorial',
    name: 'Jméno',
    description: 'Popis',
    yourMemorials: 'Vaše memorialy',
    empty: 'Tento účet zatím nemá žádný memorial.',
    openWorkspace: 'Otevřít workspace',
    overview: 'Přehled',
    contributions: 'Vzpomínky',
    review: 'Kontrola',
    members: 'Členové',
    invitations: 'Pozvánky',
    role: 'Role',
    roleOwner: 'Vlastník',
    roleTrustedReviewer: 'Důvěryhodný kontrolor',
    roleContributor: 'Přispěvatel',
    roleViewer: 'Čtenář',
    roleSystem: 'Systém',
    statusDraft: 'Uloženo, nezaindexováno',
    statusNeedsReview: 'Čeká na kontrolu',
    statusApproved: 'Schváleno',
    statusRejected: 'Zamítnuto',
    statusArchived: 'Archivováno',
    statusSuperseded: 'Nahrazeno novější verzí',
    statusPendingIndex: 'Schváleno, čeká na indexaci',
    statusIndexed: 'Zaindexováno',
    statusPromotionFailed: 'Indexace se nezdařila',
    statusPromotionCancelled: 'Indexace zrušena',
    disputeStatusNone: 'Bez sporu',
    disputeStatusDisputed: 'Sporná vzpomínka',
    disputeStatusResolved: 'Spor vyřešen',
    clarificationStatusPending: 'Čeká na odpověď',
    clarificationStatusAnswered: 'Zodpovězeno',
    clarificationStatusSkipped: 'Přeskočeno',
    clarificationStatusCancelled: 'Není potřeba',
    contributionTypeInitialClaim: 'Původní odpověď',
    contributionTypeClarificationAnswer: 'Odpověď na doplňující otázku',
    contributionTypeOwnerCorrection: 'Oprava vlastníkem',
    contributionTypeOwnerConfirmation: 'Potvrzení vlastníkem',
    contributionTypeReviewerNote: 'Poznámka kontrolora',
    contributionTypeDisputeStatement: 'Vyjádření ke sporu',
    contributionTypeSystemNormalization: 'Systémová úprava',
    submitMemory: 'Přidat vzpomínku',
    titleLabel: 'Název',
    memoryText: 'Text vzpomínky',
    sourceNote: 'Poznámka ke zdroji',
    privacyScope: 'Soukromí',
    submitForReview: 'Odeslat ke kontrole',
    viewerReadOnly: 'Viewer nemůže přidávat vzpomínky.',
    noContributions: 'Pro tuto roli nejsou viditelné žádné vzpomínky.',
    notActiveMemory: 'Není aktivní paměť',
    activeMemory: 'Vhodné pro aktivní paměť',
    noPending: 'Žádné příspěvky od rodiny nečekají na kontrolu. (Vzpomínky od AI biografa jsou v samostatném seznamu níže.)',
    approve: 'Schválit',
    reject: 'Odmítnout',
    archive: 'Archivovat',
    inviteParticipant: 'Pozvat účastníka',
    inviteHelp: 'Vlastník může pozvat trusted reviewera, contributora nebo viewera.',
    invitationCreated: 'Pozvánka vytvořena.',
    devToken: 'Vývojový invite token',
    tokenNote: 'Zobrazeno, protože backend token vrací pro dev/test flow. Neukládá se do browser storage.',
    acceptTitle: 'Přijmout pozvánku',
    acceptHelp: 'Přihlaste se účtem pozvaného člověka. Token se použije jednou z URL.',
    acceptInvitation: 'Přijmout pozvánku',
    invitationAccepted: 'Pozvánka přijata.',
    noToken: 'Chybí token pozvánky.',
    creating: 'Vytvářím',
    submitting: 'Odesílám',
    working: 'Pracuji',
    indexingPending: 'Schváleno, čeká na indexaci',
    indexingIndexed: 'Indexováno a vyhledatelné',
    indexingFailed: 'Indexace selhala',
    indexingRetired: 'Již není aktivní znalost',
    retryIndexing: 'Zkusit indexaci znovu',
    retryIndexingSuccess: 'Indexace byla zopakována.',
    jobStatusPending: 'Čeká na zahájení',
    jobStatusQueued: 'Zařazeno do fronty na indexaci',
    jobStatusProcessing: 'Probíhá indexace',
    jobStatusRetryScheduled: 'Dočasný problém - automaticky se opakuje',
    jobStatusRecoveryPending: 'Obnovuji indexační službu - automaticky se opakuje',
    jobStatusSucceeded: 'Indexováno a vyhledatelné',
    jobStatusFailed: 'Indexace selhala',
    jobStatusCancelled: 'Indexace zrušena',
    jobStatusUnauthorized: 'Přihlaste se znovu pro zobrazení aktuálního stavu indexace.',
    jobStatusNetworkRetrying: 'Obnovuji připojení pro kontrolu stavu indexace...',
    backToSite: 'Zpět na web',
    planLimitReachedMessage:
      'V aktuálním plánu už máte maximální počet memorialů.\nOtevřete existující memorial a upravte jeho životopis.',
    openExistingMemorial: 'Otevřít existující memorial',
    biographyIndexingExplanation:
      'Životopis je uložený, ale avatar ho zatím nemůže používat.\nSpusťte indexaci, aby se vytvořila jeho paměť.',
    editMemorial: 'Upravit memorial',
    saveChanges: 'Uložit změny',
    clearBiography: 'Vymazat životopis',
    clearBiographyConfirmTitle: 'Vymazat tento životopis?',
    clearBiographyConfirmBody:
      'Odstraní se uložený text životopisu a veškerá paměť z něj vytvořená. Členství, pozvánky a další schválené vzpomínky zůstanou zachovány.',
    clearBiographyConfirmYes: 'Ano, vymazat životopis',
    deleteMemorial: 'Smazat memorial',
    deleteMemorialConfirmTitle: 'Smazat tento memorial?',
    deleteMemorialConfirmBody:
      'Trvale se smaže memorial, jeho životopis, členové, pozvánky, příspěvky a veškerá zaindexovaná paměť avatara. Tuto akci nelze vrátit zpět.',
    deleteMemorialConfirmLabel: 'Pro potvrzení napište název memorialu',
    deleteMemorialConfirmButton: 'Trvale smazat',
    deleteMemorialPartialFailure: 'Smazání se nepodařilo bezpečně dokončit a bylo zrušeno. Zkuste to prosím znovu.',
    backToMemorials: 'Zpět na memorialy'
  },
  ru: {
    kicker: 'Семейный контроль доступа',
    title: 'Приватное пространство мемориала',
    subtitle: 'Создайте мемориал, пригласите семью, собирайте воспоминания и одобряйте только то, что должно стать активной памятью аватара.',
    signInTitle: 'Войдите',
    signInHelp: 'Используйте реальный аккаунт backend. Frontend держит access token только в памяти.',
    signIn: 'Войти',
    createAccount: 'Создать аккаунт',
    fullName: 'Полное имя',
    email: 'E-mail',
    password: 'Пароль',
    signedInAs: 'Вошли как',
    signOut: 'Выйти',
    sessionExpired: 'Ваш сеанс истёк. Пожалуйста, войдите снова.',
    refresh: 'Обновить',
    chat: 'Чат',
    chatEmpty: 'Пока нет сообщений. Напишите привет, чтобы начать разговор.',
    chatPlaceholder: 'Напишите сообщение...',
    chatSend: 'Отправить',
    chatYou: 'Вы',
    chatAvatar: 'Аватар',
    chatReset: 'Обновить чат',
    chatResetConfirmTitle: 'Очистить текущий чат и начать новый?',
    chatResetConfirmYes: 'Да, начать новый чат',
    chatResetConfirmCancel: 'Отмена',
    chatResetDone: 'Новый чат готов.',
    biography: 'Биография',
    biographyIntro: 'Напишите начальную историю жизни мемориала. Ничто не станет памятью аватара, пока вы явно не запустите индексацию.',
    biographyPlaceholder: 'Напишите биографию здесь...',
    biographySave: 'Сохранить биографию',
    biographyStartIngestion: 'Запустить индексацию',
    biographyConfirmNote: 'После индексации аватар сможет использовать эту биографию в своих ответах.',
    biographyStatusDraft: 'Черновик - ещё не проиндексировано',
    biographyStatusReady: 'В очереди на индексацию',
    biographyStatusIngesting: 'Идёт индексация...',
    biographyStatusIndexed: 'Проиндексировано - часть памяти аватара',
    biographyStatusFailed: 'Индексация не удалась',
    biographyStatusStale: 'Изменено после последней индексации - запустите индексацию заново',
    biographyRetry: 'Повторить индексацию',
    biographyTextLabel: 'Текст биографии',
    biographySavedNotIndexed: 'Биография сохранена. Она ещё не проиндексирована.',
    biographySavedNowStale: 'Новая версия сохранена. Запустите индексацию заново, чтобы обновить память аватара - до этого момента остаётся активной предыдущая проиндексированная версия.',
    biographyLastIndexed: 'Последняя индексация',
    biographyFailureReason: 'Причина',
    biographyAttempts: 'Количество попыток',
    biographyUpToDate: 'Проиндексировано и актуально - действие не требуется.',
    biographyConflict: 'Индексация этой биографии уже выполняется.',
    biographyConfirmStartTitle: 'Запустить индексацию этой биографии?',
    biographyConfirmStartBody: 'После индексации аватар сможет использовать эту биографию в своих ответах.',
    biographyConfirmStartYes: 'Да, запустить индексацию',
    biographyConfirmCancel: 'Отмена',
    confirmedMemoriesTitle: 'Подтверждённые воспоминания',
    confirmedMemoriesIntro: 'Воспоминания, которые предложил ИИ-биограф и которые вы одобрили. Они дополняют текст биографии выше и отображаются здесь только после одобрения.',
    confirmedMemoriesEmpty: 'Пока нет одобренных воспоминаний от биографа.',
    confirmedMemoriesIndexedBadge: 'Доступно для поиска аватаром',
    confirmedMemoriesPendingBadge: 'Одобрено, ещё не доступно для поиска',
    confirmedMemoriesFailedBadge: 'Индексация не удалась',
    biographer: 'ИИ-биограф',
    biographerIntro: 'ИИ-биограф использует проиндексированную биографию и одобренные воспоминания. Сначала он определяет, что уже известно, а затем задаёт один вопрос, который дополняет историю. Ответ никогда не индексируется автоматически - сначала он проходит проверку.',
    biographerBlockedMissing: 'Сначала сохраните биографию.',
    biographerBlockedNotIndexed: 'Сначала проиндексируйте биографию, прежде чем запускать биографа.',
    biographerBlockedIndexing: 'Индексация биографии выполняется. ИИ-биограф станет доступен после её завершения.',
    biographerBlockedStale: 'Биография была изменена после индексации. Проиндексируйте её заново, чтобы биограф использовал актуальный текст.',
    biographerBlockedActive: 'Пожалуйста, сначала ответьте на текущий уточняющий вопрос ниже.',
    biographerBlockedWaitingReview: 'По текущей теме есть воспоминание, ожидающее проверки владельцем. Следующая тема будет предложена после её рассмотрения.',
    biographerBlockedPermission: 'У вас нет прав на использование ИИ-биографа для этого мемориала.',
    biographerGoToBiography: 'Запустить индексацию биографии',
    biographerGenerationFailed: 'ИИ-биографу не удалось подготовить вопрос. Попробуйте ещё раз.',
    biographerDone: 'Все темы ИИ-биографа для этого мемориала уже пройдены.',
    biographerAnswerPlaceholder: 'Напишите свой ответ...',
    biographerSubmit: 'Отправить ответ',
    biographerSkip: 'Пропустить вопрос',
    biographerPostpone: 'Спросить позже',
    biographerTopicLabel: 'Тема',
    biographerRelevanceTemplate: 'Этот вопрос дополняет тему {topic}.',
    biographerTopicChildhood: 'Детство',
    biographerTopicFamily: 'Семья',
    biographerTopicEducation: 'Образование',
    biographerTopicWork: 'Работа',
    biographerTopicRelationships: 'Отношения',
    biographerTopicPlaces: 'Места',
    biographerTopicTraditions: 'Традиции',
    biographerTopicValues: 'Ценности',
    biographerMoreDetailsNeeded: 'Нужно больше деталей',
    biographerReadyForReview: 'Готово к проверке владельцем.',
    biographerCandidatePendingIndex: 'Одобрено, ожидает индексации.',
    biographerCandidateIndexed: 'Это воспоминание проиндексировано.',
    biographerGoToReview: 'Перейти к проверке',
    candidatesTitle: 'Воспоминания от биографа',
    candidatesSubtitle: 'Кандидаты в воспоминания, ожидающие или прошедшие проверку владельцем - отдельно от вкладов/воспоминаний семьи выше.',
    candidatesEmpty: 'Пока нет воспоминаний от ИИ-биографа.',
    candidateConfirm: 'Подтвердить',
    candidateEditAndConfirm: 'Изменить и подтвердить',
    candidateEditTextareaLabel: 'Изменить итоговый текст воспоминания',
    candidateApproveMultiplePerspectives: 'Одобрить как несколько точек зрения',
    candidateReject: 'Отклонить',
    candidateRejectReasonLabel: 'Причина (необязательно)',
    candidateRequestDetails: 'Запросить больше деталей',
    candidateMarkDisputed: 'Отметить как спорное',
    candidateIndexButton: 'Проиндексировать воспоминание',
    candidateIndexedLabel: 'Проиндексировано и доступно для поиска',
    candidatePendingIndexLabel: 'Одобрено, ещё не проиндексировано',
    candidatePendingIndexNotice: 'Воспоминание одобрено. Статус: ожидает индексации. Воспоминание одобрено, но пока недоступно для поиска аватаром.',
    candidateAlreadyIndexed: 'Это воспоминание уже проиндексировано.',
    candidateIndexingFailedLabel: 'Индексация не удалась',
    candidateIndexRetryButton: 'Повторить индексацию',
    candidateIndexConfirmTitle: 'Проиндексировать это воспоминание?',
    candidateIndexConfirmBody: 'Это создаст embedding и сделает одобренное воспоминание доступным для поиска аватаром.',
    candidateIndexConfirmYes: 'Да, проиндексировать воспоминание',
    candidatePrivacyScopeLabel: 'Уровень приватности',
    candidatePrivacyPrivateOwner: 'Только владелец',
    candidatePrivacySelectedFamily: 'Выбранные члены семьи',
    candidatePrivacyAllFamily: 'Все члены семьи',
    candidatePrivacyPublicLegacy: 'Публичное наследие',
    candidateViewHistory: 'Показать историю',
    candidateHideHistory: 'Скрыть историю',
    candidateHistoryContributions: 'История вкладов',
    candidateHistoryClarifications: 'Уточняющие вопросы',
    candidateHistoryEmpty: 'Пока нет записей.',
    candidateClarificationPending: 'Биографу нужна ещё одна деталь, прежде чем это можно будет проверить:',
    candidateClarificationPlaceholder: 'Напишите свой ответ...',
    candidateClarificationSubmit: 'Отправить',
    overviewBiographyLabel: 'Биография',
    overviewBiographyNotSaved: 'Пока не сохранена',
    overviewBiographyIndexed: 'Проиндексирована',
    overviewBiographyNotIndexed: 'Не проиндексирована',
    overviewBiographyStale: 'Изменена - нужна повторная индексация',
    overviewBiographerLabel: 'ИИ-биограф',
    overviewBiographerQuestionActive: 'Вопрос ждёт вашего ответа',
    overviewBiographerNoQuestion: 'Нет активного вопроса',
    overviewReviewLabel: 'Проверка',
    overviewReviewClarifications: 'уточнений нужно заполнить',
    overviewReviewCandidates: 'кандидатов ждут проверки',
    overviewIndexingLabel: 'Индексация',
    overviewIndexingPending: 'одобренных воспоминаний ждут индексации',
    overviewIndexingDone: 'проиндексированных воспоминаний',
    overviewNextAction: 'Следующий шаг',
    overviewNextActionAddBiography: 'Добавить биографию',
    overviewNextActionStartIndexing: 'Запустить индексацию биографии',
    overviewNextActionAnswerQuestion: 'Ответить на вопрос биографа',
    overviewNextActionCompleteClarification: 'Заполнить ожидающее уточнение',
    overviewNextActionReviewCandidate: 'Проверить кандидата в воспоминания',
    overviewNextActionIndexApproved: 'Проиндексировать одобренное воспоминание',
    overviewNextActionTestChat: 'Проверить аватара в чате',
    overviewAllCaughtUp: 'Всё актуально.',
    goAction: 'Перейти',
    cancelAction: 'Отмена',
    createMemorial: 'Создать мемориал',
    name: 'Имя',
    description: 'Описание',
    yourMemorials: 'Ваши мемориалы',
    empty: 'Для этого аккаунта пока нет мемориалов.',
    openWorkspace: 'Открыть workspace',
    overview: 'Обзор',
    contributions: 'Воспоминания',
    review: 'Проверка',
    members: 'Участники',
    invitations: 'Приглашения',
    role: 'Роль',
    roleOwner: 'Владелец',
    roleTrustedReviewer: 'Доверенный рецензент',
    roleContributor: 'Соавтор',
    roleViewer: 'Читатель',
    roleSystem: 'Система',
    statusDraft: 'Сохранено, не проиндексировано',
    statusNeedsReview: 'Ожидает проверки',
    statusApproved: 'Одобрено',
    statusRejected: 'Отклонено',
    statusArchived: 'В архиве',
    statusSuperseded: 'Заменено новой версией',
    statusPendingIndex: 'Одобрено, ожидает индексации',
    statusIndexed: 'Проиндексировано',
    statusPromotionFailed: 'Индексация не удалась',
    statusPromotionCancelled: 'Индексация отменена',
    disputeStatusNone: 'Без спора',
    disputeStatusDisputed: 'Спорное воспоминание',
    disputeStatusResolved: 'Спор разрешён',
    clarificationStatusPending: 'Ожидает ответа',
    clarificationStatusAnswered: 'Отвечено',
    clarificationStatusSkipped: 'Пропущено',
    clarificationStatusCancelled: 'Не требуется',
    contributionTypeInitialClaim: 'Первоначальный ответ',
    contributionTypeClarificationAnswer: 'Ответ на уточняющий вопрос',
    contributionTypeOwnerCorrection: 'Исправление владельцем',
    contributionTypeOwnerConfirmation: 'Подтверждение владельцем',
    contributionTypeReviewerNote: 'Заметка рецензента',
    contributionTypeDisputeStatement: 'Заявление по спору',
    contributionTypeSystemNormalization: 'Системное обновление',
    submitMemory: 'Добавить воспоминание',
    titleLabel: 'Название',
    memoryText: 'Текст воспоминания',
    sourceNote: 'Источник',
    privacyScope: 'Приватность',
    submitForReview: 'Отправить на проверку',
    viewerReadOnly: 'Viewer не может добавлять воспоминания.',
    noContributions: 'Для этой роли нет видимых воспоминаний.',
    notActiveMemory: 'Не активная память',
    activeMemory: 'Подходит для активной памяти',
    noPending: 'Нет записей от семьи, ожидающих проверки. (Воспоминания от ИИ-биографа перечислены отдельно ниже.)',
    approve: 'Одобрить',
    reject: 'Отклонить',
    archive: 'Архивировать',
    inviteParticipant: 'Пригласить участника',
    inviteHelp: 'Владелец может пригласить trusted reviewer, contributor или viewer.',
    invitationCreated: 'Приглашение создано.',
    devToken: 'Dev invite token',
    tokenNote: 'Показан потому, что backend возвращает его для dev/test flow. Он не сохраняется в browser storage.',
    acceptTitle: 'Принять приглашение',
    acceptHelp: 'Войдите под приглашенным аккаунтом. Token используется один раз из URL.',
    acceptInvitation: 'Принять приглашение',
    invitationAccepted: 'Приглашение принято.',
    noToken: 'Token приглашения отсутствует.',
    creating: 'Создаю',
    submitting: 'Отправляю',
    working: 'Выполняю',
    indexingPending: 'Одобрено, ожидает индексации',
    indexingIndexed: 'Проиндексировано и доступно для поиска',
    indexingFailed: 'Индексация не удалась',
    indexingRetired: 'Больше не активное знание',
    retryIndexing: 'Повторить индексацию',
    retryIndexingSuccess: 'Индексация повторена.',
    jobStatusPending: 'Ожидает начала',
    jobStatusQueued: 'В очереди на индексацию',
    jobStatusProcessing: 'Идёт индексация',
    jobStatusRetryScheduled: 'Временная проблема - повтор выполняется автоматически',
    jobStatusRecoveryPending: 'Восстанавливаем службу индексации - повтор выполняется автоматически',
    jobStatusSucceeded: 'Проиндексировано и доступно для поиска',
    jobStatusFailed: 'Индексация не удалась',
    jobStatusCancelled: 'Индексация отменена',
    jobStatusUnauthorized: 'Войдите снова, чтобы увидеть актуальный статус индексации.',
    jobStatusNetworkRetrying: 'Восстанавливаем соединение для проверки статуса индексации...',
    backToSite: 'Вернуться на сайт',
    planLimitReachedMessage:
      'В текущем тарифе уже создано максимальное количество мемориалов.\nОткройте существующий мемориал и измените его биографию.',
    openExistingMemorial: 'Открыть существующий мемориал',
    biographyIndexingExplanation:
      'Биография сохранена, но аватар пока не может её использовать.\nЗапустите индексацию, чтобы создать его память.',
    editMemorial: 'Редактировать мемориал',
    saveChanges: 'Сохранить изменения',
    clearBiography: 'Очистить биографию',
    clearBiographyConfirmTitle: 'Очистить эту биографию?',
    clearBiographyConfirmBody:
      'Будет удалён сохранённый текст биографии и вся созданная из него память. Участники, приглашения и другие одобренные воспоминания не будут затронуты.',
    clearBiographyConfirmYes: 'Да, очистить биографию',
    deleteMemorial: 'Удалить мемориал',
    deleteMemorialConfirmTitle: 'Удалить этот мемориал?',
    deleteMemorialConfirmBody:
      'Мемориал, его биография, участники, приглашения, вклады и вся проиндексированная память аватара будут удалены безвозвратно. Это действие нельзя отменить.',
    deleteMemorialConfirmLabel: 'Введите название мемориала для подтверждения',
    deleteMemorialConfirmButton: 'Удалить навсегда',
    deleteMemorialPartialFailure: 'Удаление не удалось безопасно завершить и было отменено. Попробуйте ещё раз.',
    backToMemorials: 'Назад к мемориалам'
  }
};

const INVITE_ROLES: InvitableMemorialRole[] = ['trusted_reviewer', 'contributor', 'viewer'];
const PRIVACY_SCOPES: PrivacyScope[] = ['private_owner', 'selected_family', 'all_family', 'public_legacy'];

function normalizeEmail(value: string): string {
  return value.trim().toLowerCase();
}

function safeError(error: unknown): string {
  return error instanceof MemorialApiError ? error.detail : 'The action could not be completed.';
}

// Task 65.7 (Part G.49): the last-resort fallback for a genuinely unknown
// enum value - never the primary label for a known one. Every localizer
// below falls back to this (with a console warning) instead of ever
// silently rendering nothing.
function prettifyEnumFallback(value: string): string {
  return value.replace(/_/g, ' ');
}

function warnUnknownEnum(category: string, value: string): void {
  // eslint-disable-next-line no-console
  console.warn(`[localization] unknown ${category} value: "${value}"`);
}

function roleLabel(t: Copy, role: string): string {
  switch (role) {
    case 'owner':
      return t.roleOwner;
    case 'trusted_reviewer':
      return t.roleTrustedReviewer;
    case 'contributor':
      return t.roleContributor;
    case 'viewer':
      return t.roleViewer;
    case 'system':
      return t.roleSystem;
    default:
      warnUnknownEnum('role', role);
      return prettifyEnumFallback(role);
  }
}

// Shared by both `ConversationMemoryCandidate.status` ("review_status" in
// `CandidateEnrichmentRead`) and `FamilyMemoryContribution.status` - the
// same underlying concept (a review-lifecycle status) uses the same label
// regardless of which record carries it.
function candidateStatusLabel(t: Copy, status: string): string {
  switch (status) {
    case 'draft':
      return t.statusDraft;
    case 'needs_review':
      return t.statusNeedsReview;
    case 'approved':
      return t.statusApproved;
    case 'rejected':
      return t.statusRejected;
    case 'archived':
      return t.statusArchived;
    case 'superseded':
      return t.statusSuperseded;
    default:
      warnUnknownEnum('candidate/contribution status', status);
      return prettifyEnumFallback(status);
  }
}

function disputeStatusLabel(t: Copy, status: string): string {
  switch (status) {
    case 'none':
      return t.disputeStatusNone;
    case 'disputed':
      return t.disputeStatusDisputed;
    case 'resolved':
      return t.disputeStatusResolved;
    default:
      warnUnknownEnum('dispute status', status);
      return prettifyEnumFallback(status);
  }
}

function clarificationStatusLabel(t: Copy, status: string): string {
  switch (status) {
    case 'pending':
      return t.clarificationStatusPending;
    case 'answered':
      return t.clarificationStatusAnswered;
    case 'skipped':
      return t.clarificationStatusSkipped;
    case 'cancelled':
      return t.clarificationStatusCancelled;
    default:
      warnUnknownEnum('clarification status', status);
      return prettifyEnumFallback(status);
  }
}

function contributionTypeLabel(t: Copy, type: string): string {
  switch (type) {
    case 'initial_claim':
      return t.contributionTypeInitialClaim;
    case 'clarification_answer':
      return t.contributionTypeClarificationAnswer;
    case 'owner_correction':
      return t.contributionTypeOwnerCorrection;
    case 'owner_confirmation':
      return t.contributionTypeOwnerConfirmation;
    case 'reviewer_note':
      return t.contributionTypeReviewerNote;
    case 'dispute_statement':
      return t.contributionTypeDisputeStatement;
    case 'system_normalization':
      return t.contributionTypeSystemNormalization;
    default:
      warnUnknownEnum('contribution type', type);
      return prettifyEnumFallback(type);
  }
}

function promotionStatusLabel(t: Copy, status: string): string {
  switch (status) {
    case 'pending_index':
      return t.statusPendingIndex;
    case 'indexed':
      return t.statusIndexed;
    case 'failed':
      return t.statusPromotionFailed;
    case 'cancelled':
      return t.statusPromotionCancelled;
    default:
      warnUnknownEnum('promotion status', status);
      return prettifyEnumFallback(status);
  }
}

function formatDate(value: string | null, lang: Lang): string {
  if (!value) return '-';
  const locale = lang === 'cs' ? 'cs-CZ' : lang === 'ru' ? 'ru-RU' : 'en-US';
  return new Intl.DateTimeFormat(locale).format(new Date(value));
}

function getInvitationTokenFromUrl(): string | null {
  const params = new URLSearchParams(window.location.search);
  return params.get('token');
}

const SHORT_PREVIEW_MAX_LENGTH = 220;

/** A guaranteed, JS-level short preview - never depends on CSS line-clamp
 * support to keep a long biography from being rendered in full anywhere
 * outside its dedicated editor (Task 65.5 Part 21/22: memorial cards and
 * the Overview must show a short preview, never the complete text). */
export function shortTextPreview(value: string | null | undefined): string {
  const normalized = (value || '').trim();
  if (normalized.length <= SHORT_PREVIEW_MAX_LENGTH) return normalized;
  return `${normalized.slice(0, SHORT_PREVIEW_MAX_LENGTH).trimEnd()}…`;
}

export default function MemorialWorkspace({ lang }: { lang: Lang }) {
  const t = COPY[lang];
  const [session, setSession] = useState<AuthSession | null>(null);
  const [memorials, setMemorials] = useState<MemorialRead[]>([]);
  const [selected, setSelected] = useState<MemorialRead | null>(null);
  const [members, setMembers] = useState<MembershipRead[]>([]);
  const [contributions, setContributions] = useState<ContributionRead[]>([]);
  const [reviewQueue, setReviewQueue] = useState<ContributionRead[]>([]);
  const [biographyStatus, setBiographyStatus] = useState<BiographyStatusRead | null>(null);
  const [biographerEligible, setBiographerEligible] = useState(false);
  const [biographerQuestion, setBiographerQuestion] = useState<BiographerQuestionRead | null>(null);
  const [candidatesSummary, setCandidatesSummary] = useState<MemoryCandidateEnrichmentRead[]>([]);
  const [activeTab, setActiveTab] = useState<WorkspaceTab>('overview');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [invitationToken, setInvitationToken] = useState<string | null>(null);
  const [billingLimits, setBillingLimits] = useState<BillingLimitsRead | null>(null);
  // Task 65.7 (Part B.13): bounded startup rehydration - true only while
  // the one-shot `GET /api/auth/session` probe below is in flight, so the
  // login form is never briefly flashed for an already-logged-in user
  // returning from navigation/a page refresh.
  const [sessionHydrating, setSessionHydrating] = useState(true);

  const role = selected?.current_user_role;
  const mayInvite = role ? canInvite(role) : false;
  const mayReview = role ? canReview(role) : false;
  const maySubmit = role ? canSubmitContribution(role) : false;

  const pathname = usePathname();
  const route = parseAppRoute(pathname);

  useEffect(() => {
    const token = getInvitationTokenFromUrl();
    setInvitationToken(token);
    if (token) {
      const url = new URL(window.location.href);
      url.searchParams.delete('token');
      window.history.replaceState({}, document.title, `${url.pathname}${url.search}${url.hash}`);
    }
  }, []);

  const visibleTabs = useMemo(() => {
    const tabs: WorkspaceTab[] = ['overview', 'biography', 'biographer', 'chat', 'contributions', 'review', 'members', 'invitations'];
    return tabs.filter((tab) => {
      if (tab === 'review') return mayReview;
      if (tab === 'members') return mayReview;
      if (tab === 'invitations') return mayInvite;
      if (tab === 'biography') return role === 'owner';
      // Every Biographer endpoint requires SUBMIT_CONTRIBUTION server-side
      // (confirmed via backend audit) - a viewer's every request there would
      // 403, so the tab is hidden rather than shown broken.
      if (tab === 'biographer') return maySubmit;
      return true;
    });
  }, [mayInvite, mayReview, maySubmit, role]);

  async function loadMemorials(accessToken = session?.accessToken, options: { resolveBootstrap?: boolean } = {}) {
    // An empty string is a valid, intentional "authenticate via the
    // browser-session cookie only" value (Task 65.7) - only `undefined`
    // (no session resolved at all yet) skips loading.
    if (accessToken === undefined) return;
    setLoading(true);
    setError(null);
    try {
      const memorialList = await listMemorials(accessToken);
      setMemorials(memorialList);
      // Billing limits gate the create-memorial form (Task 65.5) - fetched
      // alongside the memorial list itself, and re-fetched after create or
      // delete since both change `current_usage.current_profiles`. A failure
      // here fails open (leaves `billingLimits` as-is / null), letting the
      // backend remain the authoritative enforcement point either way.
      void getBillingLimits(accessToken)
        .then(setBillingLimits)
        .catch(() => {});
      if (options.resolveBootstrap) {
        await resolveBootstrapSelection(memorialList, accessToken);
      }
    } catch (loadError) {
      setError(safeError(loadError));
      setMemorials([]);
      setSelected(null);
    } finally {
      setLoading(false);
    }
  }

  /**
   * Deterministic zero/one/many bootstrap (Task 65.1B): a route that already
   * names a memorial id wins (deep link / browser back-forward - still
   * re-validated against the authenticated user's memberships by
   * `loadWorkspace` itself, never trusted blindly). Otherwise, exactly one
   * accessible memorial auto-opens; zero memorials leaves the onboarding
   * create-form visible; more than one leaves the explicit selector visible
   * rather than silently picking one.
   */
  async function resolveBootstrapSelection(memorialList: MemorialRead[], accessToken: string) {
    if (route.name === 'app-memorial') {
      await loadWorkspace(route.profileId, accessToken);
      return;
    }
    if (memorialList.length === 1) {
      await loadWorkspace(memorialList[0].id, accessToken);
    }
  }

  function refreshOverviewSummary(
    accessToken: string,
    profileId: number,
    role: MemorialRole
  ) {
    // Overview/tab-badge summary data (Part 31-33): one controlled fetch
    // path, reused on initial workspace load and whenever the owner
    // returns to the Overview tab - not an independent poll per tab.
    void getBiographyStatus(accessToken, profileId)
      .then(setBiographyStatus)
      .catch(() => setBiographyStatus(null));
    if (canSubmitContribution(role)) {
      void getBiographerEligibility(accessToken, profileId)
        .then(async (eligibility) => {
          setBiographerEligible(eligibility.eligible);
          if (eligibility.eligible) {
            const nextQuestion = await getNextBiographerQuestion(accessToken, profileId, biographerLocale(lang));
            setBiographerQuestion(nextQuestion);
          } else {
            setBiographerQuestion(null);
          }
        })
        .catch(() => {
          setBiographerEligible(false);
          setBiographerQuestion(null);
        });
    }
    if (canReview(role)) {
      void listMemoryCandidates(accessToken, profileId)
        .then(setCandidatesSummary)
        .catch(() => setCandidatesSummary([]));
    }
  }

  async function loadWorkspace(profileId: number, accessToken = session?.accessToken) {
    if (accessToken === undefined) return;
    setLoading(true);
    setError(null);
    setMembers([]);
    setContributions([]);
    setReviewQueue([]);
    setBiographyStatus(null);
    setBiographerEligible(false);
    setBiographerQuestion(null);
    setCandidatesSummary([]);
    try {
      const memorial = await fetchMemorial(accessToken, profileId);
      setSelected(memorial);
      setActiveTab('overview');
      navigate(buildMemorialPath(profileId));
      const canReviewHere = canReview(memorial.current_user_role);
      const [contributionList, memberList, pendingList] = await Promise.all([
        listContributions(accessToken, profileId),
        canReviewHere ? listMembers(accessToken, profileId) : Promise.resolve([]),
        canReviewHere ? listReviewQueue(accessToken, profileId) : Promise.resolve([])
      ]);
      setContributions(contributionList);
      setMembers(memberList);
      setReviewQueue(pendingList);
      refreshOverviewSummary(accessToken, profileId, memorial.current_user_role);
    } catch (loadError) {
      // A stale or unauthorized route memorial id must never render cached
      // private data - clear the active memorial and send the URL back to
      // the selector/onboarding root rather than leaving a dead deep link.
      setSelected(null);
      setMembers([]);
      setContributions([]);
      setReviewQueue([]);
      setError(safeError(loadError));
      navigate(APP_ROOT_PATH);
    } finally {
      setLoading(false);
    }
  }

  // Task 65.9.1 (Part F) - reconciles the contribution list from the
  // backend once a polled retry-indexing job reaches a terminal state
  // (see `ContributionList`'s `JobStatusBadge` usage below) - lighter than
  // re-running the full `loadWorkspace` (members/review-queue/biography
  // all stay untouched), and always reads the current `selected`/`session`
  // via closure rather than being passed stale values as props.
  async function refreshContributions() {
    if (!selected || !session) return;
    try {
      setContributions(await listContributions(session.accessToken, selected.id));
    } catch {
      // Transient failure: keep the previous (still authoritative-enough)
      // list rather than clearing it - the next successful poll/tab
      // switch will reconcile it.
    }
  }

  useEffect(() => {
    if (activeTab === 'overview' && selected && session) {
      refreshOverviewSummary(session.accessToken, selected.id, selected.current_user_role);
    }
    // Deliberately excludes refreshOverviewSummary/selected/session from the
    // dependency array - this should only re-run when the user actually
    // navigates back to the Overview tab, not on every render of those
    // stable-shaped objects (avoids a refetch loop).
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [activeTab]);

  useEffect(() => {
    // The family-contribution review queue (unlike CandidatesReviewSection,
    // which fetches fresh on its own mount) is plain state handed down as a
    // prop, so it goes stale if a contribution reaches needs_review after
    // the initial workspace load. Re-fetch it every time the owner/reviewer
    // actually switches onto the Review tab so "nothing pending" is never a
    // stale read.
    if (activeTab === 'review' && selected && session && canReview(selected.current_user_role)) {
      void listReviewQueue(session.accessToken, selected.id)
        .then(setReviewQueue)
        .catch(() => {});
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [activeTab]);

  function onAuthenticated(nextSession: AuthSession) {
    setSession(nextSession);
    void loadMemorials(nextSession.accessToken, { resolveBootstrap: true });
  }

  function signOut(reason?: 'expired') {
    setSession(null);
    setMemorials([]);
    setSelected(null);
    setMembers([]);
    setContributions([]);
    setReviewQueue([]);
    setError(null);
    setNotice(reason === 'expired' ? t.sessionExpired : null);
    void logoutSession().catch(() => {});
    // Clear the active-memorial URL too, so a subsequently logged-in user
    // (same browser tab) never lands back on the previous user's deep link.
    navigate(APP_ROOT_PATH);
  }

  useEffect(() => {
    // Task 65.7 (Part B.13/B.15): the one-shot startup rehydration probe -
    // resolves the HttpOnly browser-session cookie set by a prior `login`
    // (Part B.11) into a restored session, so navigating from the
    // workspace to the main marketing page and back (which fully unmounts
    // and remounts this component, see `App.tsx`'s route-boundary comment)
    // - or a plain browser refresh - never forces another login. A 401
    // here (no/expired session) is expected and silent: it just leaves
    // `session` null so `AuthPanel` renders normally, never an "expired"
    // notice (the user may simply have never logged in yet).
    let cancelled = false;
    getSession()
      .then((user) => {
        if (cancelled) return;
        // No bearer token is available from a cookie-only resume - every
        // `memorialApi` call already falls back to the session cookie
        // (`credentials: 'include'`) whenever no token is supplied, so an
        // empty string here is intentional, not a placeholder bug.
        const restoredSession: AuthSession = { accessToken: '', email: user.email };
        setSession(restoredSession);
        void loadMemorials('', { resolveBootstrap: true });
      })
      .catch(() => {
        // No valid session - fall through to the login form.
      })
      .finally(() => {
        if (!cancelled) setSessionHydrating(false);
      });
    return () => {
      cancelled = true;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    // Part 38 (Task 65.4): any authenticated request coming back 401
    // (expired/invalid token) clears the session exactly once, through the
    // existing sign-out path - never an infinite retry loop. Known
    // limitation: unsaved draft text in whichever tab was open is not
    // preserved across a forced expiry (would need a separate durable
    // draft-persistence layer, out of scope here).
    setUnauthorizedHandler(() => signOut('expired'));
    return () => setUnauthorizedHandler(null);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <section id="memorial-workspace" className="relative overflow-hidden px-4 py-24 sm:px-6">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_70%_45%_at_50%_5%,rgba(127,216,247,.16),transparent_70%),radial-gradient(ellipse_45%_35%_at_100%_40%,rgba(139,124,246,.16),transparent_70%)]" />
      <div className="relative mx-auto max-w-7xl">
        <div className="mx-auto mb-10 max-w-3xl text-center">
          <div className="mb-4 text-xs uppercase tracking-[.34em] text-cyan/65">{t.kicker}</div>
          <h2 className="font-serif text-[clamp(34px,5vw,68px)] leading-[1.05] text-balance">{t.title}</h2>
          <p className="mx-auto mt-5 max-w-2xl text-sm leading-7 text-fg/62 sm:text-base">{t.subtitle}</p>
        </div>

        {invitationToken && (
          <InvitationAcceptPanel
            invitationToken={invitationToken}
            lang={lang}
            onAccepted={(membership) => {
              setNotice(t.invitationAccepted);
              setInvitationToken(null);
              if (session) void loadMemorials(session.accessToken);
              if (membership.profile_id && session) void loadWorkspace(membership.profile_id, session.accessToken);
            }}
            onAuthenticated={onAuthenticated}
            session={session}
            t={t}
          />
        )}

        {sessionHydrating ? (
          <p className="text-center text-sm text-fg/55">{t.working}</p>
        ) : !session ? (
          invitationToken ? null : (
          <AuthPanel onAuthenticated={onAuthenticated} t={t} />
          )
        ) : (
          <div className="space-y-5">
            <section className="rounded-[28px] border border-white/10 bg-white/[.045] p-4 shadow-[0_24px_80px_rgba(0,0,0,.28)] backdrop-blur sm:p-5">
              <div className="flex min-w-0 flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <div className="min-w-0">
                  <p className="text-xs uppercase tracking-[.22em] text-fg/40">{t.signedInAs}</p>
                  <strong className="block truncate text-sm text-fg sm:text-base">{session.email}</strong>
                </div>
                <div className="grid grid-cols-2 gap-2 sm:flex sm:justify-end">
                  <button className="rounded-full border border-white/15 px-4 py-2.5 text-sm text-fg/75 transition hover:bg-white/10" onClick={() => void loadMemorials()} type="button">
                    {t.refresh}
                  </button>
                  <button className="rounded-full border border-white/15 px-4 py-2.5 text-sm text-fg/75 transition hover:bg-white/10" onClick={() => signOut()} type="button">
                    {t.signOut}
                  </button>
                </div>
              </div>
            </section>

            {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
            {notice && <p className="rounded-2xl border border-cyan/30 bg-cyan/10 px-4 py-3 text-sm text-cyan">{notice}</p>}

            {/* Task 65.5 Part G: the create/list picker is only ever shown
                when no memorial is open - once one is selected, its own
                "Open workspace" button (in MemorialList) would otherwise
                render simultaneously with the workspace already being open,
                a duplicated affordance for the same action. */}
            {!selected && (
              <div className="grid min-w-0 gap-5 lg:grid-cols-[minmax(0,0.88fr)_minmax(0,1.12fr)]">
                <CreateMemorialForm
                  billingLimits={billingLimits}
                  existingMemorials={memorials}
                  onCreated={(memorial) => {
                    setMemorials((items) => [memorial, ...items.filter((item) => item.id !== memorial.id)]);
                    void loadWorkspace(memorial.id);
                  }}
                  onOpenExisting={(profileId) => void loadWorkspace(profileId)}
                  t={t}
                  token={session.accessToken}
                />
                <MemorialList
                  loading={loading && !selected}
                  memorials={memorials}
                  onOpen={(profileId) => void loadWorkspace(profileId)}
                  t={t}
                  lang={lang}
                />
              </div>
            )}

            {selected && (
              <section className="grid min-w-0 gap-5 rounded-[34px] border border-white/10 bg-black/20 p-3 sm:p-4 lg:grid-cols-[280px_minmax(0,1fr)]">
                <aside className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-5">
                  <button
                    className="mb-3 text-xs uppercase tracking-[.24em] text-cyan/60 transition hover:text-cyan"
                    onClick={() => {
                      setSelected(null);
                      navigate(APP_ROOT_PATH);
                    }}
                    type="button"
                  >
                    ← {t.backToMemorials}
                  </button>
                  <h3 className="break-words font-serif text-3xl leading-tight">{selected.name}</h3>
                  <p className="mt-2 text-sm text-fg/55">
                    {t.role}: {roleLabel(t, selected.current_user_role)}
                  </p>
                  <div className="mt-6 grid gap-2" role="tablist" aria-label="Workspace sections">
                    {visibleTabs.map((tab) => {
                      const badgeCount =
                        tab === 'biographer'
                          ? (biographerQuestion ? 1 : 0) +
                            candidatesSummary.filter((candidate) => candidate.next_clarification_question).length
                          : tab === 'review'
                            ? reviewQueue.length +
                              candidatesSummary.filter(
                                (candidate) => candidate.review_status === 'needs_review' && !candidate.next_clarification_question
                              ).length
                            : 0;
                      return (
                        <button
                          aria-selected={activeTab === tab}
                          className={`flex min-w-0 items-center justify-between gap-2 rounded-2xl px-4 py-3 text-left text-sm transition ${
                            activeTab === tab ? 'bg-cyan/18 text-cyan shadow-[0_0_24px_rgba(127,216,247,.14)]' : 'bg-white/[.045] text-fg/65 hover:bg-white/[.08]'
                          }`}
                          key={tab}
                          onClick={() => setActiveTab(tab)}
                          role="tab"
                          type="button"
                        >
                          <span className="truncate">{t[tab]}</span>
                          {badgeCount > 0 && (
                            <span className="shrink-0 rounded-full bg-cyan/25 px-2 py-0.5 text-xs text-cyan">{badgeCount}</span>
                          )}
                        </button>
                      );
                    })}
                  </div>
                </aside>

                <div className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-6">
                  {activeTab === 'overview' && (
                    <Overview
                      biographerEligible={biographerEligible}
                      biographerQuestion={biographerQuestion}
                      biographyStatus={biographyStatus}
                      candidates={candidatesSummary}
                      canReviewHere={mayReview}
                      canSubmitHere={maySubmit}
                      isOwner={role === 'owner'}
                      lang={lang}
                      memorial={selected}
                      onMemorialDeleted={() => {
                        const deletedId = selected.id;
                        setSelected(null);
                        setMemorials((items) => items.filter((item) => item.id !== deletedId));
                        void loadMemorials(session.accessToken);
                        navigate(APP_ROOT_PATH);
                      }}
                      onMemorialUpdated={(updated) => {
                        setSelected(updated);
                        setMemorials((items) => items.map((item) => (item.id === updated.id ? updated : item)));
                      }}
                      onNavigate={(tab) => setActiveTab(tab)}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                  {activeTab === 'biography' && role === 'owner' && (
                    <BiographyPanel
                      initialBiography={selected.biography}
                      lang={lang}
                      profileId={selected.id}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                  {activeTab === 'biographer' && maySubmit && (
                    <BiographerPanel
                      email={session.email}
                      lang={lang}
                      onNavigateToBiography={role === 'owner' ? () => setActiveTab('biography') : null}
                      onNavigateToReview={() => setActiveTab('review')}
                      profileId={selected.id}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                  {activeTab === 'chat' && (
                    <ChatPanel email={session.email} profileId={selected.id} t={t} token={session.accessToken} />
                  )}
                  {activeTab === 'contributions' && (
                    <ContributionsSection
                      contributions={contributions}
                      lang={lang}
                      mayReview={mayReview}
                      maySubmit={maySubmit}
                      onIndexingRetried={(updated) => {
                        setContributions((items) => items.map((item) => (item.id === updated.id ? updated : item)));
                      }}
                      onIndexingSettled={refreshContributions}
                      onSubmitted={(contribution) => {
                        setContributions((items) => [contribution, ...items]);
                        if (mayReview && contribution.status === 'needs_review') {
                          setReviewQueue((items) => [contribution, ...items]);
                        }
                        setNotice(t.submitting);
                      }}
                      profileId={selected.id}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                  {activeTab === 'review' && mayReview && (
                    <ReviewQueue
                      lang={lang}
                      onReviewed={(updated) => {
                        setReviewQueue((items) => items.filter((item) => item.id !== updated.id));
                        setContributions((items) =>
                          items.map((item) =>
                            item.id === updated.id
                              ? updated
                              : updated.supersedes_contribution_id === item.id
                                ? { ...item, status: 'superseded', is_current: false, active_memory_eligible: false }
                                : item
                          )
                        );
                        setNotice(`${t.review}: ${updated.status}.`);
                      }}
                      profileId={selected.id}
                      queue={reviewQueue}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                  {activeTab === 'review' && mayReview && (
                    <div className="mt-8 border-t border-white/10 pt-8">
                      <CandidatesReviewSection
                        isOwner={role === 'owner'}
                        lang={lang}
                        profileId={selected.id}
                        t={t}
                        token={session.accessToken}
                      />
                    </div>
                  )}
                  {activeTab === 'members' && mayReview && <MembersSection members={members} t={t} />}
                  {activeTab === 'invitations' && mayInvite && (
                    <InvitationSection
                      onInvited={() => setNotice(t.invitationCreated)}
                      profileId={selected.id}
                      t={t}
                      token={session.accessToken}
                    />
                  )}
                </div>
              </section>
            )}
          </div>
        )}
      </div>
    </section>
  );
}

function AuthPanel({ t, onAuthenticated }: { t: Copy; onAuthenticated: (session: AuthSession) => void }) {
  const [mode, setMode] = useState<'login' | 'register'>('login');
  const [email, setEmail] = useState('');
  const [fullName, setFullName] = useState('');
  const [password, setPassword] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const normalizedEmail = normalizeEmail(email);
    if (!normalizedEmail.includes('@')) {
      setError('Enter a valid email address.');
      return;
    }
    if (password.length < 8) {
      setError('Password must have at least 8 characters.');
      return;
    }

    setBusy(true);
    setError(null);
    try {
      if (mode === 'register') await register(normalizedEmail, password, fullName.trim() || null);
      const accessToken = await login(normalizedEmail, password);
      setPassword('');
      onAuthenticated({ accessToken, email: normalizedEmail });
    } catch (authError) {
      setError(safeError(authError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="mx-auto max-w-2xl rounded-[34px] border border-white/10 bg-white/[.045] p-5 shadow-[0_24px_80px_rgba(0,0,0,.32)] backdrop-blur sm:p-7">
      <p className="text-xs uppercase tracking-[.26em] text-cyan/60">{t.signInTitle}</p>
      <p className="mt-3 text-sm leading-6 text-fg/60">{t.signInHelp}</p>
      <div className="mt-6 grid grid-cols-2 gap-2 rounded-full border border-white/10 bg-black/20 p-1">
        <button className={`rounded-full px-4 py-2.5 text-sm ${mode === 'login' ? 'bg-cyan/20 text-cyan' : 'text-fg/55'}`} onClick={() => setMode('login')} type="button">
          {t.signIn}
        </button>
        <button className={`rounded-full px-4 py-2.5 text-sm ${mode === 'register' ? 'bg-cyan/20 text-cyan' : 'text-fg/55'}`} onClick={() => setMode('register')} type="button">
          {t.createAccount}
        </button>
      </div>
      <form className="mt-5 grid gap-4" onSubmit={submit}>
        <Field label={t.email} value={email} onChange={setEmail} type="email" required />
        {mode === 'register' && <Field label={t.fullName} value={fullName} onChange={setFullName} />}
        <Field label={t.password} value={password} onChange={setPassword} type="password" required />
        {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
          {busy ? t.working : mode === 'login' ? t.signIn : t.createAccount}
        </button>
      </form>
    </section>
  );
}

function InvitationAcceptPanel({
  invitationToken,
  lang,
  onAccepted,
  onAuthenticated,
  session,
  t
}: {
  invitationToken: string;
  lang: Lang;
  onAccepted: (membership: MembershipRead) => void;
  onAuthenticated: (session: AuthSession) => void;
  session: AuthSession | null;
  t: Copy;
}) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function accept() {
    if (!session) {
      setError(t.signInTitle);
      return;
    }
    setBusy(true);
    setError(null);
    try {
      onAccepted(await acceptInvitation(session.accessToken, invitationToken));
    } catch (acceptError) {
      setError(safeError(acceptError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="mb-5 grid gap-4 rounded-[30px] border border-cyan/20 bg-cyan/10 p-4 sm:p-6 lg:grid-cols-[minmax(0,1fr)_minmax(280px,420px)]">
      <div className="min-w-0">
        <p className="text-xs uppercase tracking-[.24em] text-cyan/70">{t.acceptTitle}</p>
        <p className="mt-3 text-sm leading-6 text-fg/65">{t.acceptHelp}</p>
        {error && <p className="mt-4 rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        {session && (
          <button className="mt-5 w-full rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55 sm:w-auto" disabled={busy} onClick={accept} type="button">
            {busy ? t.working : t.acceptInvitation}
          </button>
        )}
      </div>
      {!session && <AuthPanel onAuthenticated={onAuthenticated} t={t} />}
      {session && <p className="self-center rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/65">{formatDate(new Date().toISOString(), lang)}</p>}
    </section>
  );
}

/** Task 65.5: whether the backend would currently accept another memorial
 * for this account, based on `/api/billing/limits`. `max_profiles === null`
 * means unlimited. Fails open (allows the form) when the limits haven't
 * loaded yet or failed to load - the backend remains authoritative and
 * still rejects the request server-side if the plan really is at its
 * limit; this only controls whether the frontend shows the full create
 * form as the primary action versus the "open existing memorial" message. */
function hasReachedProfileLimit(billingLimits: BillingLimitsRead | null): boolean {
  if (!billingLimits) return false;
  const max = billingLimits.limits.max_profiles;
  if (max === null) return false;
  return billingLimits.current_usage.current_profiles >= max;
}

export function CreateMemorialForm({
  token,
  t,
  onCreated,
  billingLimits,
  existingMemorials,
  onOpenExisting
}: {
  token: string;
  t: Copy;
  onCreated: (memorial: MemorialRead) => void;
  billingLimits: BillingLimitsRead | null;
  existingMemorials: MemorialRead[];
  onOpenExisting: (profileId: number) => void;
}) {
  const [name, setName] = useState('');
  const [biography, setBiography] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [limitErrorOnSubmit, setLimitErrorOnSubmit] = useState(false);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (name.trim().length < 2) {
      setError('Memorial name is required.');
      return;
    }
    setBusy(true);
    setError(null);
    setLimitErrorOnSubmit(false);
    try {
      const memorial = await createMemorial(token, { name: name.trim(), biography: biography.trim() || null });
      setName('');
      setBiography('');
      onCreated(memorial);
    } catch (createError) {
      // The backend remains authoritative: even if the frontend's own
      // billing-limits check said the form should be offered, a concurrent
      // change (e.g. another tab already created the last allowed profile)
      // can still return this error on submit. Normalize it into the same
      // friendly, actionable message rather than surfacing raw backend
      // wording, and preserve the entered draft text instead of clearing it.
      if (createError instanceof MemorialApiError && createError.status === 403) {
        setLimitErrorOnSubmit(true);
      } else {
        setError(safeError(createError));
      }
    } finally {
      setBusy(false);
    }
  }

  if (hasReachedProfileLimit(billingLimits) || limitErrorOnSubmit) {
    return (
      <section className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-6">
        <h3 className="font-serif text-3xl">{t.createMemorial}</h3>
        <p className="mt-4 whitespace-pre-line text-sm leading-6 text-fg/70">{t.planLimitReachedMessage}</p>
        {existingMemorials[0] && (
          <button
            className="mt-5 rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink"
            onClick={() => onOpenExisting(existingMemorials[0].id)}
            type="button"
          >
            {t.openExistingMemorial}
          </button>
        )}
      </section>
    );
  }

  return (
    <section className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-6">
      <h3 className="font-serif text-3xl">{t.createMemorial}</h3>
      <form className="mt-5 grid gap-4" onSubmit={submit}>
        <Field label={t.name} value={name} onChange={setName} required />
        <Textarea label={t.description} value={biography} onChange={setBiography} />
        {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
          {busy ? t.creating : t.createMemorial}
        </button>
      </form>
    </section>
  );
}

export function MemorialList({
  loading,
  memorials,
  onOpen,
  t,
  lang
}: {
  loading: boolean;
  memorials: MemorialRead[];
  onOpen: (profileId: number) => void;
  t: Copy;
  lang: Lang;
}) {
  return (
    <section className="min-w-0 rounded-[28px] border border-white/10 bg-white/[.045] p-4 sm:p-6">
      <div className="flex items-center justify-between gap-3">
        <h3 className="font-serif text-3xl">{t.yourMemorials}</h3>
        {loading && <span className="rounded-full bg-white/10 px-3 py-1 text-xs text-fg/55">{t.working}</span>}
      </div>
      {!loading && memorials.length === 0 && <p className="mt-5 text-sm leading-6 text-fg/58">{t.empty}</p>}
      <div className="mt-5 grid gap-3">
        {memorials.map((memorial) => (
          <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={memorial.id}>
            <div className="flex min-w-0 flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
              <div className="min-w-0">
                <h4 className="break-words text-lg font-semibold">{memorial.name}</h4>
                <p className="mt-2 line-clamp-3 text-sm leading-6 text-fg/55">{shortTextPreview(memorial.biography) || t.description}</p>
                <p className="mt-2 text-xs text-fg/38">{formatDate(memorial.created_at, lang)}</p>
              </div>
              <span className="w-fit rounded-full bg-white/10 px-3 py-1 text-xs text-cyan">{roleLabel(t, memorial.current_user_role)}</span>
            </div>
            <button className="mt-4 w-full rounded-full border border-white/15 px-4 py-3 text-sm text-fg/75 transition hover:bg-white/10 sm:w-auto" onClick={() => onOpen(memorial.id)} type="button">
              {t.openWorkspace}
            </button>
          </article>
        ))}
      </div>
    </section>
  );
}

type NextAction = { label: string; tab: WorkspaceTab };

export function Overview({
  memorial,
  t,
  lang,
  isOwner,
  canSubmitHere,
  canReviewHere,
  biographyStatus,
  biographerEligible,
  biographerQuestion,
  candidates,
  onNavigate,
  token,
  onMemorialUpdated,
  onMemorialDeleted
}: {
  memorial: MemorialRead;
  t: Copy;
  lang: Lang;
  isOwner: boolean;
  canSubmitHere: boolean;
  canReviewHere: boolean;
  biographyStatus: BiographyStatusRead | null;
  biographerEligible: boolean;
  biographerQuestion: BiographerQuestionRead | null;
  candidates: MemoryCandidateEnrichmentRead[];
  onNavigate: (tab: WorkspaceTab) => void;
  token: string;
  onMemorialUpdated: (memorial: MemorialRead) => void;
  onMemorialDeleted: () => void;
}) {
  const [editingName, setEditingName] = useState(false);
  const [nameDraft, setNameDraft] = useState(memorial.name);
  const [nameBusy, setNameBusy] = useState(false);
  const [nameError, setNameError] = useState<string | null>(null);

  useEffect(() => {
    setNameDraft(memorial.name);
  }, [memorial.id, memorial.name]);

  async function saveName() {
    const trimmed = nameDraft.trim();
    if (trimmed.length < 2) {
      setNameError('Memorial name is required.');
      return;
    }
    setNameBusy(true);
    setNameError(null);
    try {
      const updated = await updateMemorialMetadata(token, memorial.id, { name: trimmed });
      onMemorialUpdated(updated);
      setEditingName(false);
    } catch (updateError) {
      // The entered draft name is deliberately left in `nameDraft` on
      // failure rather than reset - the owner should not have to retype it.
      setNameError(safeError(updateError));
    } finally {
      setNameBusy(false);
    }
  }

  const [confirmingDelete, setConfirmingDelete] = useState(false);
  const [deleteConfirmText, setDeleteConfirmText] = useState('');
  const [deleteBusy, setDeleteBusy] = useState(false);
  const [deleteError, setDeleteError] = useState<string | null>(null);

  async function performDelete() {
    setDeleteBusy(true);
    setDeleteError(null);
    try {
      await deleteMemorial(token, memorial.id);
      onMemorialDeleted();
    } catch (deleteErr) {
      // A 409 here means the backend's Qdrant-cleanup pass failed partway
      // through and deliberately left the memorial (and its DB rows) intact
      // rather than deleting the record while vectors remain retrievable -
      // never claim success in that case, just let the owner retry.
      if (deleteErr instanceof MemorialApiError && deleteErr.status === 409) {
        setDeleteError(t.deleteMemorialPartialFailure);
      } else {
        setDeleteError(safeError(deleteErr));
      }
    } finally {
      setDeleteBusy(false);
    }
  }
  const clarificationsRequired = candidates.filter((candidate) => candidate.next_clarification_question).length;
  const candidatesAwaitingReview = candidates.filter(
    (candidate) => candidate.review_status === 'needs_review' && !candidate.next_clarification_question
  ).length;
  const approvedAwaitingIndex = candidates.filter(
    (candidate) => candidate.explicit_indexing_required && !candidate.searchable_as_fact
  ).length;
  const indexedCount = candidates.filter((candidate) => candidate.searchable_as_fact).length;

  function biographyOverviewLabel(): string {
    if (!biographyStatus || !memorial.biography) return t.overviewBiographyNotSaved;
    if (biographyStatus.status === 'indexed') return t.overviewBiographyIndexed;
    if (biographyStatus.status === 'stale') return t.overviewBiographyStale;
    return t.overviewBiographyNotIndexed;
  }

  function nextAction(): NextAction | null {
    if (isOwner && !memorial.biography) {
      return { label: t.overviewNextActionAddBiography, tab: 'biography' };
    }
    if (
      isOwner &&
      biographyStatus &&
      // 'draft' is the real backend status right after a biography save
      // (confirmed via live diagnosis: update_biography sets 'draft', not
      // 'ready_for_ingestion' - that value is only set momentarily inside
      // start_biography_ingestion itself, immediately before enqueueing).
      // Omitting 'draft' here was a proven Task 65.4 regression: a saved-
      // but-never-indexed biography fell through every branch below and
      // Overview incorrectly claimed "everything is up to date".
      (biographyStatus.status === 'draft' ||
        biographyStatus.status === 'ready_for_ingestion' ||
        biographyStatus.status === 'failed' ||
        biographyStatus.status === 'stale')
    ) {
      return { label: t.overviewNextActionStartIndexing, tab: 'biography' };
    }
    if (canSubmitHere && biographerEligible && biographerQuestion) {
      return { label: t.overviewNextActionAnswerQuestion, tab: 'biographer' };
    }
    if (clarificationsRequired > 0) {
      return { label: t.overviewNextActionCompleteClarification, tab: 'biographer' };
    }
    if (canReviewHere && candidatesAwaitingReview > 0) {
      return { label: t.overviewNextActionReviewCandidate, tab: 'review' };
    }
    if (isOwner && approvedAwaitingIndex > 0) {
      return { label: t.overviewNextActionIndexApproved, tab: 'review' };
    }
    if (biographyStatus?.status === 'indexed' || indexedCount > 0) {
      return { label: t.overviewNextActionTestChat, tab: 'chat' };
    }
    return null;
  }

  const action = nextAction();

  return (
    <div className="min-w-0 space-y-5">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <h3 className="font-serif text-3xl">{t.overview}</h3>
        {isOwner && !editingName && (
          <button
            className="shrink-0 rounded-full border border-white/15 px-4 py-2 text-sm text-fg/75 transition hover:bg-white/10"
            onClick={() => setEditingName(true)}
            type="button"
          >
            {t.editMemorial}
          </button>
        )}
      </div>
      {editingName ? (
        <div className="grid gap-3 rounded-2xl border border-white/10 bg-black/20 p-4">
          <Field label={t.name} value={nameDraft} onChange={setNameDraft} required />
          {nameError && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{nameError}</p>}
          <div className="flex flex-wrap gap-3">
            <button
              className="rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-2.5 text-sm font-semibold text-ink disabled:opacity-55"
              disabled={nameBusy}
              onClick={() => void saveName()}
              type="button"
            >
              {nameBusy ? t.working : t.saveChanges}
            </button>
            <button
              className="rounded-full border border-white/15 px-5 py-2.5 text-sm text-fg/75 transition hover:bg-white/10"
              disabled={nameBusy}
              onClick={() => {
                setEditingName(false);
                setNameError(null);
                setNameDraft(memorial.name);
              }}
              type="button"
            >
              {t.cancelAction}
            </button>
          </div>
        </div>
      ) : (
        <p className="break-words text-sm leading-7 text-fg/65">{shortTextPreview(memorial.biography) || t.empty}</p>
      )}
      <div className="flex flex-wrap gap-2">
        <Badge>{t.role}: {roleLabel(t, memorial.current_user_role)}</Badge>
        <Badge>{formatDate(memorial.created_at, lang)}</Badge>
      </div>

      <div className="rounded-2xl border border-cyan/25 bg-cyan/10 p-4">
        <p className="text-xs uppercase tracking-[.2em] text-cyan/60">{t.overviewNextAction}</p>
        {action ? (
          <div className="mt-2 flex flex-wrap items-center justify-between gap-3">
            <p className="text-sm font-semibold text-fg">{action.label}</p>
            <button
              className="shrink-0 rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-2 text-sm font-semibold text-ink"
              onClick={() => onNavigate(action.tab)}
              type="button"
            >
              {t.goAction}
            </button>
          </div>
        ) : (
          <p className="mt-2 text-sm text-fg/65">{t.overviewAllCaughtUp}</p>
        )}
      </div>

      <div className="grid gap-3 sm:grid-cols-2">
        <div className="rounded-2xl border border-white/10 bg-black/20 p-4">
          <p className="text-xs uppercase tracking-[.2em] text-fg/40">{t.overviewBiographyLabel}</p>
          <p className="mt-2 text-sm text-fg/75">{biographyOverviewLabel()}</p>
        </div>
        {canSubmitHere && (
          <div className="rounded-2xl border border-white/10 bg-black/20 p-4">
            <p className="text-xs uppercase tracking-[.2em] text-fg/40">{t.overviewBiographerLabel}</p>
            <p className="mt-2 text-sm text-fg/75">
              {biographerEligible && biographerQuestion ? t.overviewBiographerQuestionActive : t.overviewBiographerNoQuestion}
            </p>
          </div>
        )}
        {canReviewHere && (
          <div className="rounded-2xl border border-white/10 bg-black/20 p-4">
            <p className="text-xs uppercase tracking-[.2em] text-fg/40">{t.overviewReviewLabel}</p>
            <p className="mt-2 text-sm text-fg/75">
              {clarificationsRequired} {t.overviewReviewClarifications}
            </p>
            <p className="mt-1 text-sm text-fg/75">
              {candidatesAwaitingReview} {t.overviewReviewCandidates}
            </p>
          </div>
        )}
        {canReviewHere && (
          <div className="rounded-2xl border border-white/10 bg-black/20 p-4">
            <p className="text-xs uppercase tracking-[.2em] text-fg/40">{t.overviewIndexingLabel}</p>
            <p className="mt-2 text-sm text-fg/75">
              {approvedAwaitingIndex} {t.overviewIndexingPending}
            </p>
            <p className="mt-1 text-sm text-fg/75">
              {indexedCount} {t.overviewIndexingDone}
            </p>
          </div>
        )}
      </div>

      {isOwner && (
        <div className="mt-8 rounded-2xl border border-red-400/25 bg-red-500/[.04] p-4">
          {!confirmingDelete ? (
            <button
              className="rounded-full border border-red-400/30 px-5 py-2.5 text-sm text-red-200 transition hover:bg-red-500/10"
              onClick={() => setConfirmingDelete(true)}
              type="button"
            >
              {t.deleteMemorial}
            </button>
          ) : (
            <div className="grid gap-3">
              <p className="text-sm font-semibold text-fg">{t.deleteMemorialConfirmTitle}</p>
              <p className="text-sm leading-6 text-fg/70">{t.deleteMemorialConfirmBody}</p>
              <Field label={t.deleteMemorialConfirmLabel} value={deleteConfirmText} onChange={setDeleteConfirmText} />
              {deleteError && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{deleteError}</p>}
              <div className="flex flex-wrap gap-3">
                <button
                  className="rounded-full bg-red-500/80 px-5 py-2.5 text-sm font-semibold text-white disabled:opacity-40"
                  disabled={deleteBusy || deleteConfirmText.trim() !== memorial.name.trim()}
                  onClick={() => void performDelete()}
                  type="button"
                >
                  {deleteBusy ? t.working : t.deleteMemorialConfirmButton}
                </button>
                <button
                  className="rounded-full border border-white/15 px-5 py-2.5 text-sm text-fg/75 transition hover:bg-white/10"
                  disabled={deleteBusy}
                  onClick={() => {
                    setConfirmingDelete(false);
                    setDeleteConfirmText('');
                    setDeleteError(null);
                  }}
                  type="button"
                >
                  {t.cancelAction}
                </button>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

const CHAT_DRAFT_STORAGE_PREFIX = 'eternal_world:chat_draft';

function chatDraftKey({ email, profileId }: { email: string; profileId: number }): string {
  return `${CHAT_DRAFT_STORAGE_PREFIX}:${email}:${profileId}`;
}

function ChatPanel({ token, profileId, email, t }: { token: string; profileId: number; email: string; t: Copy }) {
  const [messages, setMessages] = useState<ChatMessageRead[]>([]);
  const [text, setText] = useState(() => {
    try {
      return window.sessionStorage.getItem(chatDraftKey({ email, profileId })) ?? '';
    } catch {
      return '';
    }
  });
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [confirmingReset, setConfirmingReset] = useState(false);
  const [resetBusy, setResetBusy] = useState(false);
  const [resetNotice, setResetNotice] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    getActiveChat(token, profileId)
      .then((active) => {
        if (!cancelled) setMessages(active.messages);
      })
      .catch((loadError) => {
        if (!cancelled) setError(safeError(loadError));
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [token, profileId]);

  // Task 65.7 (Part 26/53): unsaved chat input survives navigation away and
  // back within the same browser session - never submitted data, which the
  // backend already restores via `getActiveChat` above.
  useEffect(() => {
    try {
      const key = chatDraftKey({ email, profileId });
      if (text.trim()) {
        window.sessionStorage.setItem(key, text);
      } else {
        window.sessionStorage.removeItem(key);
      }
    } catch {
      // sessionStorage may be unavailable (private browsing) - drafts are a
      // convenience, never required for correctness.
    }
  }, [text, email, profileId]);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const trimmed = text.trim();
    if (!trimmed) return;
    setBusy(true);
    setError(null);
    setResetNotice(false);
    const optimisticUserMessage: ChatMessageRead = {
      id: -Date.now(),
      profile_id: profileId,
      role: 'user',
      content: trimmed,
      created_at: new Date().toISOString()
    };
    setMessages((items) => [...items, optimisticUserMessage]);
    setText('');
    try {
      const response = await sendChatMessage(token, profileId, trimmed);
      setMessages((items) => [
        ...items.filter((item) => item.id !== optimisticUserMessage.id),
        { id: response.message_id - 1, profile_id: response.profile_id, role: 'user', content: response.user_message, created_at: response.created_at },
        { id: response.message_id, profile_id: response.profile_id, role: 'assistant', content: response.ai_response_text, created_at: response.created_at }
      ]);
    } catch (sendError) {
      setMessages((items) => items.filter((item) => item.id !== optimisticUserMessage.id));
      setText(trimmed);
      setError(safeError(sendError));
    } finally {
      setBusy(false);
    }
  }

  async function confirmReset() {
    setResetBusy(true);
    setError(null);
    try {
      const fresh = await resetChat(token, profileId);
      setMessages(fresh.messages);
      setConfirmingReset(false);
      setResetNotice(true);
    } catch (resetError) {
      setError(safeError(resetError));
    } finally {
      setResetBusy(false);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <h3 className="font-serif text-3xl">{t.chat}</h3>
        {!confirmingReset ? (
          <button
            className="shrink-0 rounded-full border border-white/15 px-4 py-2 text-sm text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
            disabled={loading || messages.length === 0}
            onClick={() => setConfirmingReset(true)}
            type="button"
          >
            {t.chatReset}
          </button>
        ) : (
          <div className="flex flex-wrap items-center gap-2 rounded-2xl border border-cyan/25 bg-cyan/10 px-3 py-2">
            <span className="text-sm text-fg/80">{t.chatResetConfirmTitle}</span>
            <button
              className="rounded-full bg-gradient-to-r from-cyan to-violet px-4 py-1.5 text-xs font-semibold text-ink disabled:opacity-55"
              disabled={resetBusy}
              onClick={() => void confirmReset()}
              type="button"
            >
              {resetBusy ? t.working : t.chatResetConfirmYes}
            </button>
            <button
              className="rounded-full border border-white/15 px-4 py-1.5 text-xs text-fg/75 transition hover:bg-white/10"
              disabled={resetBusy}
              onClick={() => setConfirmingReset(false)}
              type="button"
            >
              {t.chatResetConfirmCancel}
            </button>
          </div>
        )}
      </div>
      {resetNotice && <p className="rounded-2xl border border-cyan/30 bg-cyan/10 px-4 py-3 text-sm text-cyan">{t.chatResetDone}</p>}
      <div className="min-w-0 space-y-3 rounded-3xl border border-white/10 bg-black/20 p-4">
        {loading && <p className="text-sm text-fg/55">{t.working}</p>}
        {!loading && messages.length === 0 && <p className="text-sm text-fg/60">{t.chatEmpty}</p>}
        {messages.map((message) => (
          <div className={`min-w-0 ${message.role === 'assistant' ? '' : 'text-right'}`} key={message.id}>
            <p className="text-xs uppercase tracking-[.18em] text-fg/38">
              {message.role === 'assistant' ? t.chatAvatar : t.chatYou}
            </p>
            <p
              className={`mt-1 inline-block max-w-full whitespace-pre-wrap break-words rounded-2xl px-4 py-2.5 text-left text-sm leading-6 ${
                message.role === 'assistant' ? 'bg-white/[.06] text-fg/85' : 'bg-cyan/15 text-fg'
              }`}
            >
              {message.content}
            </p>
          </div>
        ))}
      </div>
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      <form className="flex min-w-0 flex-col gap-3 sm:flex-row" onSubmit={submit}>
        <input
          className="min-w-0 flex-1 rounded-2xl border border-white/10 bg-black/25 px-4 py-3 text-fg outline-none transition placeholder:text-fg/30 focus:border-cyan/70"
          maxLength={4000}
          onChange={(event) => setText(event.target.value)}
          placeholder={t.chatPlaceholder}
          value={text}
        />
        <button className="shrink-0 rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy || !text.trim()} type="submit">
          {busy ? t.working : t.chatSend}
        </button>
      </form>
    </div>
  );
}

const BIOGRAPHY_POLL_INTERVAL_MS = 3000;

export function biographyStatusLabel(t: Copy, status: BiographyStatusRead['status']): string {
  switch (status) {
    case 'draft':
      return t.biographyStatusDraft;
    case 'ready_for_ingestion':
      return t.biographyStatusReady;
    case 'ingesting':
      return t.biographyStatusIngesting;
    case 'indexed':
      return t.biographyStatusIndexed;
    case 'failed':
      return t.biographyStatusFailed;
    case 'stale':
      return t.biographyStatusStale;
    default:
      return status;
  }
}

export function isBiographyJobActive(status: BiographyStatusRead): boolean {
  // A job is genuinely in flight only while the backend reports `ingesting`
  // or a queued/running background job - `ready_for_ingestion` means the
  // owner saved but has not yet clicked "Start indexing", so there is
  // nothing to poll for yet (Part 13: do not poll forever).
  return (
    status.status === 'ingesting' ||
    status.background_job_status === 'queued' ||
    status.background_job_status === 'running'
  );
}

// Task 65.9.1 (Part F/G) - localized label for a polled BackgroundJob
// status, shared by both the candidate "Index memory" and contribution
// retry-indexing poll displays. Never returns a raw backend enum string to
// the user (Part 8 of the roadmap's core rules: no raw internal codes in
// client-facing text) - an unrecognized/future status falls back to the
// generic `jobStatusProcessing` label rather than leaking the raw value.
export function jobStatusLabel(t: Copy, status: BackgroundJobStatusValue | null | undefined): string {
  switch (status) {
    case 'pending':
      return t.jobStatusPending;
    case 'queued':
      return t.jobStatusQueued;
    case 'running':
      return t.jobStatusProcessing;
    case 'retry_scheduled':
      return t.jobStatusRetryScheduled;
    case 'recovery_pending':
      return t.jobStatusRecoveryPending;
    case 'succeeded':
      return t.jobStatusSucceeded;
    case 'failed':
      return t.jobStatusFailed;
    case 'cancelled':
      return t.jobStatusCancelled;
    default:
      return t.jobStatusProcessing;
  }
}

// Task 65.9.1 (Part F.13): "Retry indexing" must only ever be offered once
// the backend itself has reached a permanent failure - never while a
// bounded infrastructure retry/provider-recovery attempt is still legally
// in flight for the exact same job (that would risk a second, redundant
// job for work already converging safely).
export function isJobRetryEligible(job: BackgroundJobRead | null): boolean {
  return job !== null && job.status === 'failed';
}

export function BiographyPanel({
  token,
  profileId,
  t,
  lang,
  initialBiography
}: {
  token: string;
  profileId: number;
  t: Copy;
  lang: Lang;
  initialBiography: string | null;
}) {
  const [text, setText] = useState(initialBiography ?? '');
  const [status, setStatus] = useState<BiographyStatusRead | null>(null);
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [confirmingStart, setConfirmingStart] = useState(false);
  const [confirmingClear, setConfirmingClear] = useState(false);
  const [clearBusy, setClearBusy] = useState(false);
  const [memoryEntries, setMemoryEntries] = useState<BiographyMemoryEntryRead[]>([]);
  const [memoryEntriesLoading, setMemoryEntriesLoading] = useState(true);
  const [memoryEntriesError, setMemoryEntriesError] = useState<string | null>(null);

  useEffect(() => {
    setText(initialBiography ?? '');
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [profileId]);

  // Task 65.6.1 (Part E/K): approved candidate memories projected into the
  // Biography tab - a separate, read-only list from the free-text
  // `biography` field above. Re-fetched whenever the memorial switches so a
  // previously-loaded memorial's entries never linger after switching
  // (Part K: "memorial switching does not leak biography data").
  useEffect(() => {
    let cancelled = false;
    setMemoryEntriesLoading(true);
    setMemoryEntriesError(null);
    listBiographyMemoryEntries(token, profileId)
      .then((entries) => {
        if (!cancelled) setMemoryEntries(entries);
      })
      .catch((loadError) => {
        if (!cancelled) setMemoryEntriesError(safeError(loadError));
      })
      .finally(() => {
        if (!cancelled) setMemoryEntriesLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [token, profileId]);

  const pollCancelledRef = useRef(false);
  const pollTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Bug fix: this used to be a plain effect-local `poll()` that stopped
  // scheduling itself the moment a fetch found no active job (true at
  // mount, before the owner ever starts indexing) and never restarted -
  // `startIngestion` below then only ran one extra one-off status check 3s
  // later "because the loop above would keep going", but that loop had
  // already exited for good. Net effect: the panel froze showing
  // "ingesting" forever once a job actually started, even after the
  // backend finished successfully, because nothing was left polling.
  // Promoting this to a component-scoped, restartable loop (shared by the
  // mount effect and by every action that puts a job in flight) fixes
  // that - restarting it just resumes the same continuous poll instead of
  // firing a second, competing one-shot check.
  function pollWhileActive() {
    pollCancelledRef.current = false;
    if (pollTimerRef.current) {
      clearTimeout(pollTimerRef.current);
      pollTimerRef.current = null;
    }

    async function tick() {
      try {
        const next = await getBiographyStatus(token, profileId);
        if (pollCancelledRef.current) return;
        setStatus(next);
        setLoading(false);
        if (isBiographyJobActive(next)) {
          pollTimerRef.current = setTimeout(tick, BIOGRAPHY_POLL_INTERVAL_MS);
        }
      } catch (loadError) {
        if (!pollCancelledRef.current) {
          setError(safeError(loadError));
          setLoading(false);
        }
      }
    }

    void tick();
  }

  useEffect(() => {
    pollWhileActive();
    return () => {
      pollCancelledRef.current = true;
      if (pollTimerRef.current) clearTimeout(pollTimerRef.current);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token, profileId]);

  async function save() {
    setBusy(true);
    setError(null);
    setNotice(null);
    try {
      const next = await updateBiography(token, profileId, text);
      setStatus(next);
      // `update_biography` is idempotent: saving text identical to what is
      // already stored is a no-op and leaves status exactly as it was. If
      // the biography was already `indexed`, showing "saved, not indexed
      // yet" here would contradict the still-correct "Indexed / up to
      // date" state shown above - only claim "not indexed" when saving
      // actually left it in a not-yet-indexed state. A correction to an
      // already-indexed biography (`stale`) gets its own message - it *was*
      // indexed and the new text is now saved, just not the version the
      // avatar currently uses yet - distinct from "saved, never indexed".
      if (next.status === 'stale') {
        setNotice(t.biographySavedNowStale);
      } else if (next.status !== 'indexed') {
        setNotice(t.biographySavedNotIndexed);
      }
    } catch (saveError) {
      setError(safeError(saveError));
    } finally {
      setBusy(false);
    }
  }

  async function startIngestion() {
    setConfirmingStart(false);
    setBusy(true);
    setError(null);
    setNotice(null);
    try {
      await startBiographyIngestion(token, profileId);
      // The ingestion-start response is intentionally a smaller shape than
      // the full status (Task 65.4 contract audit) - re-fetch the complete
      // status immediately rather than merging a partial object into state.
      const refreshed = await getBiographyStatus(token, profileId);
      setStatus(refreshed);
      if (isBiographyJobActive(refreshed)) {
        // Restart the shared continuous poll loop rather than firing one
        // extra one-off check - see `pollWhileActive` above for why a
        // single bonus check silently let the UI freeze mid-job.
        pollWhileActive();
      }
    } catch (startError) {
      if (startError instanceof MemorialApiError && startError.status === 409) {
        setError(t.biographyConflict);
      } else {
        setError(safeError(startError));
      }
    } finally {
      setBusy(false);
    }
  }

  async function clear() {
    setClearBusy(true);
    setError(null);
    setNotice(null);
    try {
      const next = await clearBiography(token, profileId);
      setStatus(next);
      setText('');
      setConfirmingClear(false);
    } catch (clearError) {
      setError(safeError(clearError));
    } finally {
      setClearBusy(false);
    }
  }

  const hasEnoughText = text.trim().length >= 2;
  const jobActive = status !== null && isBiographyJobActive(status);
  const canOfferIndexing = status !== null && hasEnoughText && !jobActive && status.status !== 'indexed';
  const isRetry = status?.status === 'failed' || status?.status === 'stale';
  const hasBiographyContent = text.trim().length > 0 || Boolean(status?.content_hash);

  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.biography}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.biographyIntro}</p>
      </div>
      {loading && <p className="text-sm text-fg/55">{t.working}</p>}
      {status && (
        <div className="flex flex-wrap items-center gap-2">
          <Badge tone={status.status === 'indexed' ? 'cyan' : status.status === 'failed' ? 'danger' : 'muted'}>
            {biographyStatusLabel(t, status.status)}
          </Badge>
          {jobActive && status.background_job_status && <Badge>{status.background_job_status}</Badge>}
          {status.status === 'indexed' && status.indexed_at && (
            <Badge>
              {t.biographyLastIndexed}: {formatDate(status.indexed_at, lang)}
            </Badge>
          )}
          {status.attempt_count > 0 && <Badge>{t.biographyAttempts}: {status.attempt_count}</Badge>}
        </div>
      )}
      {status?.status === 'failed' && status.failure_reason && (
        <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">
          {t.biographyFailureReason}: {status.failure_reason}
        </p>
      )}
      {status?.status === 'indexed' && (
        <p className="text-xs text-fg/45">{t.biographyUpToDate}</p>
      )}
      <Textarea label={t.biographyTextLabel} value={text} onChange={setText} required maxLength={20000} />
      <p className="text-xs text-fg/45">{t.biographyConfirmNote}</p>
      {canOfferIndexing && (
        <p className="whitespace-pre-line rounded-2xl border border-cyan/25 bg-cyan/10 px-4 py-3 text-sm leading-6 text-fg/75">
          {t.biographyIndexingExplanation}
        </p>
      )}
      {notice && <p className="rounded-2xl border border-cyan/30 bg-cyan/10 px-4 py-3 text-sm text-cyan">{notice}</p>}
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      <div className="flex flex-wrap gap-3">
        <button
          className="rounded-full border border-white/15 px-5 py-3 text-sm text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
          disabled={busy || !hasEnoughText}
          onClick={() => void save()}
          type="button"
        >
          {busy ? t.working : t.biographySave}
        </button>
        {canOfferIndexing && !confirmingStart && (
          <button
            className="rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-3 text-sm font-semibold text-ink disabled:opacity-55"
            disabled={busy}
            onClick={() => setConfirmingStart(true)}
            type="button"
          >
            {isRetry ? t.biographyRetry : t.biographyStartIngestion}
          </button>
        )}
        {jobActive && <span className="rounded-full border border-white/15 px-5 py-3 text-sm text-fg/55">{t.working}</span>}
      </div>
      {confirmingStart && (
        <div className="grid gap-3 rounded-2xl border border-cyan/25 bg-cyan/10 p-4">
          <p className="text-sm font-semibold text-fg">{t.biographyConfirmStartTitle}</p>
          <p className="text-sm leading-6 text-fg/70">{t.biographyConfirmStartBody}</p>
          <div className="flex flex-wrap gap-3">
            <button
              className="rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-2.5 text-sm font-semibold text-ink disabled:opacity-55"
              disabled={busy}
              onClick={() => void startIngestion()}
              type="button"
            >
              {busy ? t.working : t.biographyConfirmStartYes}
            </button>
            <button
              className="rounded-full border border-white/15 px-5 py-2.5 text-sm text-fg/75 transition hover:bg-white/10"
              disabled={busy}
              onClick={() => setConfirmingStart(false)}
              type="button"
            >
              {t.biographyConfirmCancel}
            </button>
          </div>
        </div>
      )}
      <div className="mt-6 border-t border-white/10 pt-5">
        <h4 className="font-serif text-xl">{t.confirmedMemoriesTitle}</h4>
        <p className="mt-1 text-sm leading-6 text-fg/58">{t.confirmedMemoriesIntro}</p>
        {memoryEntriesLoading && <p className="mt-3 text-sm text-fg/55">{t.working}</p>}
        {memoryEntriesError && (
          <p className="mt-3 rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">
            {memoryEntriesError}
          </p>
        )}
        {!memoryEntriesLoading && !memoryEntriesError && memoryEntries.length === 0 && (
          <p className="mt-3 text-sm text-fg/50">{t.confirmedMemoriesEmpty}</p>
        )}
        <div className="mt-3 grid gap-3">
          {memoryEntries.map((entry) => (
            <article className="min-w-0 rounded-2xl border border-white/10 bg-black/20 p-4" key={entry.promotion_id}>
              <p className="break-words text-sm leading-6 text-fg/80">{entry.text}</p>
              <div className="mt-2 flex flex-wrap gap-2">
                <Badge>{privacyScopeLabel(t, entry.privacy_scope)}</Badge>
                {entry.searchable_as_fact && <Badge tone="cyan">{t.confirmedMemoriesIndexedBadge}</Badge>}
                {!entry.searchable_as_fact && entry.promotion_status !== 'failed' && (
                  <Badge tone="muted">{t.confirmedMemoriesPendingBadge}</Badge>
                )}
                {entry.promotion_status === 'failed' && <Badge tone="danger">{t.confirmedMemoriesFailedBadge}</Badge>}
              </div>
            </article>
          ))}
        </div>
      </div>
      {hasBiographyContent && (
        <div className="mt-6 border-t border-white/10 pt-5">
          {!confirmingClear ? (
            <button
              className="rounded-full border border-red-400/30 px-5 py-2.5 text-sm text-red-200 transition hover:bg-red-500/10"
              onClick={() => setConfirmingClear(true)}
              type="button"
            >
              {t.clearBiography}
            </button>
          ) : (
            <div className="grid gap-3 rounded-2xl border border-red-400/30 bg-red-500/10 p-4">
              <p className="text-sm font-semibold text-fg">{t.clearBiographyConfirmTitle}</p>
              <p className="text-sm leading-6 text-fg/70">{t.clearBiographyConfirmBody}</p>
              <div className="flex flex-wrap gap-3">
                <button
                  className="rounded-full bg-red-500/80 px-5 py-2.5 text-sm font-semibold text-white disabled:opacity-55"
                  disabled={clearBusy}
                  onClick={() => void clear()}
                  type="button"
                >
                  {clearBusy ? t.working : t.clearBiographyConfirmYes}
                </button>
                <button
                  className="rounded-full border border-white/15 px-5 py-2.5 text-sm text-fg/75 transition hover:bg-white/10"
                  disabled={clearBusy}
                  onClick={() => setConfirmingClear(false)}
                  type="button"
                >
                  {t.biographyConfirmCancel}
                </button>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export function biographerLocale(lang: Lang): 'cs' | 'ru' {
  // The Biographer backend only understands cs/ru (Task 65.2); the app's
  // 'en' marketing locale has no Biographer question bank, so it falls
  // back to Czech rather than silently mis-requesting an unsupported value.
  return lang === 'ru' ? 'ru' : 'cs';
}

export function biographerTopicLabel(t: Copy, topic: string): string {
  switch (topic) {
    case 'childhood':
      return t.biographerTopicChildhood;
    case 'family':
      return t.biographerTopicFamily;
    case 'education':
      return t.biographerTopicEducation;
    case 'work':
      return t.biographerTopicWork;
    case 'relationships':
      return t.biographerTopicRelationships;
    case 'places':
      return t.biographerTopicPlaces;
    case 'traditions':
      return t.biographerTopicTraditions;
    case 'values':
      return t.biographerTopicValues;
    default:
      // Unknown/future topic keys still render something readable rather
      // than the raw enum value as the primary label.
      warnUnknownEnum('biographer topic', topic);
      return prettifyEnumFallback(topic);
  }
}

//: Blocked reasons where re-polling makes sense (indexing is actively
//: running in the background) - every other reason requires the owner to
//: take an action first, so polling would spin forever for no reason.
const BIOGRAPHER_POLL_BLOCKED_REASONS: ReadonlySet<BiographerBlockedReason> = new Set(['indexing_in_progress']);

const BIOGRAPHER_DRAFT_STORAGE_PREFIX = 'eternal_world:biographer_draft';

function biographerDraftKey({
  email,
  profileId,
  questionId
}: {
  email: string;
  profileId: number;
  questionId: number;
}): string {
  return `${BIOGRAPHER_DRAFT_STORAGE_PREFIX}:${email}:${profileId}:${questionId}`;
}

export function BiographerPanel({
  token,
  profileId,
  email,
  t,
  lang,
  onNavigateToReview,
  onNavigateToBiography
}: {
  token: string;
  profileId: number;
  email: string;
  t: Copy;
  lang: Lang;
  onNavigateToReview: () => void;
  onNavigateToBiography: (() => void) | null;
}) {
  const [eligibility, setEligibility] = useState<BiographerEligibilityRead | null>(null);
  const [question, setQuestion] = useState<BiographerQuestionRead | null>(null);
  const [activeCandidateId, setActiveCandidateId] = useState<number | null>(null);
  // Task 65.10.1: the real clarification question behind an
  // `active_clarification_exists` block, restored from the resume
  // endpoint's `next_clarification_question` - without this, resuming a
  // session left mid-clarification (fresh mount/page reload) showed the
  // "please answer the current clarification question below" notice with
  // nothing rendered below it, since `activeCandidateId` used to only ever
  // get set transiently right after `submitAnswer`, never on resume.
  const [activeClarificationQuestion, setActiveClarificationQuestion] = useState<ClarificationQuestionRead | null>(null);
  const [answerText, setAnswerText] = useState('');
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState(false);
  const [readyForReview, setReadyForReview] = useState(false);
  const [pendingIndex, setPendingIndex] = useState(false);
  const [indexed, setIndexed] = useState(false);
  const [generationFailed, setGenerationFailed] = useState(false);

  const locale = biographerLocale(lang);

  // Task 65.7 (Part 26/28): restores an unsubmitted draft answer for the
  // SAME question after navigating away and back - never restored onto a
  // different question, and cleared automatically once that question is no
  // longer the active one (see the effect below).
  useEffect(() => {
    if (!question) return;
    try {
      const draft = window.sessionStorage.getItem(biographerDraftKey({ email, profileId, questionId: question.id }));
      if (draft) setAnswerText(draft);
    } catch {
      // sessionStorage may be unavailable - drafts are a convenience only.
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [question?.id]);

  useEffect(() => {
    if (!question) return;
    try {
      const key = biographerDraftKey({ email, profileId, questionId: question.id });
      if (answerText.trim()) {
        window.sessionStorage.setItem(key, answerText);
      } else {
        window.sessionStorage.removeItem(key);
      }
    } catch {
      // Ignored - see above.
    }
  }, [answerText, email, profileId, question]);

  function clearDraft(questionId: number) {
    try {
      window.sessionStorage.removeItem(biographerDraftKey({ email, profileId, questionId }));
    } catch {
      // Ignored - see above.
    }
  }

  async function load() {
    setLoading(true);
    setError(null);
    setDone(false);
    setGenerationFailed(false);
    try {
      // Task 65.7 (Part D.25/27): the resume endpoint is the primary state
      // source - it reflects exactly what the backend already knows
      // (a just-answered candidate ready for review, pending index, or
      // already indexed) without triggering a new question generation.
      // `next-question` is only ever called when resume itself says a new
      // question should be fetched/generated.
      const resume = await getBiographerResume(token, profileId, locale);
      setEligibility({ eligible: resume.eligible, blocked_reason: resume.blocked_reason });
      setReadyForReview(resume.next_action === 'candidate_ready_for_review');
      setPendingIndex(resume.next_action === 'candidate_pending_index');
      setIndexed(resume.next_action === 'candidate_indexed');
      // Task 65.10.1: restore the pending-candidate-clarification state
      // (the `activeCandidateId` form below) from the resume response on
      // every load - not just transiently after `submitAnswer` - so a
      // session resumed mid-clarification (fresh mount, page reload,
      // navigating back to the tab) renders the real question instead of
      // just the blocking notice with nothing answerable underneath it.
      if (resume.next_action === 'clarification_pending' && resume.candidate_id) {
        setActiveCandidateId(resume.candidate_id);
        setActiveClarificationQuestion(resume.next_clarification_question);
        setQuestion(null);
        return;
      }
      setActiveCandidateId(null);
      setActiveClarificationQuestion(null);
      if (!resume.eligible) {
        setQuestion(null);
        return;
      }
      if (resume.active_question) {
        setQuestion(resume.active_question);
        return;
      }
      if (resume.next_action === 'question_ready') {
        const nextQuestion = await getNextBiographerQuestion(token, profileId, locale);
        setQuestion(nextQuestion);
        setDone(nextQuestion === null);
      } else {
        setQuestion(null);
      }
    } catch (loadError) {
      if (loadError instanceof MemorialApiError && loadError.status === 503) {
        setGenerationFailed(true);
      } else {
        setError(safeError(loadError));
      }
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    void load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token, profileId, locale]);

  useEffect(() => {
    // Auto-refresh only while biography indexing is genuinely in progress
    // (Part 31/33 of the task spec) - every other blocked reason needs an
    // owner action first, so polling would never resolve on its own.
    if (!eligibility || eligibility.eligible) return;
    if (!BIOGRAPHER_POLL_BLOCKED_REASONS.has(eligibility.blocked_reason as BiographerBlockedReason)) return;
    const timer = setTimeout(() => void load(), BIOGRAPHY_POLL_INTERVAL_MS);
    return () => clearTimeout(timer);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [eligibility, token, profileId, locale]);

  async function submitAnswer(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!question || !answerText.trim()) return;
    setBusy(true);
    setError(null);
    setReadyForReview(false);
    try {
      await answerBiographerQuestion(token, profileId, question.id, locale, answerText.trim());
      clearDraft(question.id);
      setAnswerText('');
      // Task 65.10.1: always re-fetch through `load()` (the resume
      // endpoint) instead of deciding the post-answer state from this
      // response alone - `load()` already recomputes `readyForReview` from
      // fresh resume data, and it is the only path that also restores the
      // real clarification question text (`activeClarificationQuestion`)
      // when the answer created a candidate that still needs one, so a
      // subsequent remount/reload sees exactly the same state.
      await load();
    } catch (answerError) {
      setError(safeError(answerError));
    } finally {
      setBusy(false);
    }
  }

  async function submitClarification(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!activeCandidateId || !answerText.trim()) return;
    setBusy(true);
    setError(null);
    try {
      const enrichment = await answerCandidateClarification(token, profileId, activeCandidateId, answerText.trim());
      setAnswerText('');
      if (enrichment.unresolved_clarification_count === 0) {
        setActiveCandidateId(null);
        setActiveClarificationQuestion(null);
        if (enrichment.enrichment_status === 'ready_for_owner_review') {
          setReadyForReview(true);
        }
        await load();
      } else {
        // Task 65.10.1: childhood/bedtime-song topics can require more than
        // one clarification - advance to the actual next question the
        // backend already returned instead of leaving the just-answered one
        // displayed (or, worse, nothing at all).
        setActiveClarificationQuestion(enrichment.next_clarification_question);
      }
    } catch (clarificationError) {
      setError(safeError(clarificationError));
    } finally {
      setBusy(false);
    }
  }

  async function skip() {
    if (!question) return;
    setBusy(true);
    setError(null);
    setReadyForReview(false);
    try {
      await skipBiographerQuestion(token, profileId, question.id);
      clearDraft(question.id);
      setAnswerText('');
      await load();
    } catch (skipError) {
      setError(safeError(skipError));
    } finally {
      setBusy(false);
    }
  }

  async function postpone() {
    if (!question) return;
    setBusy(true);
    setError(null);
    setReadyForReview(false);
    try {
      await postponeBiographerQuestion(token, profileId, question.id);
      clearDraft(question.id);
      setAnswerText('');
      await load();
    } catch (postponeError) {
      setError(safeError(postponeError));
    } finally {
      setBusy(false);
    }
  }

  const showBiographyCta =
    onNavigateToBiography !== null &&
    (eligibility?.blocked_reason === 'biography_missing' ||
      eligibility?.blocked_reason === 'biography_not_indexed' ||
      eligibility?.blocked_reason === 'biography_stale');

  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.biographer}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.biographerIntro}</p>
      </div>
      {loading && <p className="text-sm text-fg/55">{t.working}</p>}
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      {generationFailed && (
        <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">
          {t.biographerGenerationFailed}
        </p>
      )}
      {!loading && eligibility && !eligibility.eligible && (
        <div className="grid gap-3 rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">
          <p>
            {eligibility.blocked_reason === 'biography_missing' && t.biographerBlockedMissing}
            {eligibility.blocked_reason === 'biography_not_indexed' && t.biographerBlockedNotIndexed}
            {eligibility.blocked_reason === 'indexing_in_progress' && t.biographerBlockedIndexing}
            {eligibility.blocked_reason === 'biography_stale' && t.biographerBlockedStale}
            {eligibility.blocked_reason === 'active_clarification_exists' &&
              activeClarificationQuestion &&
              t.biographerBlockedActive}
            {eligibility.blocked_reason === 'candidate_waiting_for_review' && t.biographerBlockedWaitingReview}
            {eligibility.blocked_reason === 'permission_denied' && t.biographerBlockedPermission}
          </p>
          {showBiographyCta && onNavigateToBiography && (
            <button
              className="shrink-0 self-start rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-2.5 text-sm font-semibold text-ink"
              onClick={onNavigateToBiography}
              type="button"
            >
              {t.biographerGoToBiography}
            </button>
          )}
        </div>
      )}
      {readyForReview && (
        <div className="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-cyan/25 bg-cyan/10 p-4">
          <p className="text-sm text-fg/80">{t.biographerReadyForReview}</p>
          <button
            className="shrink-0 rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-2.5 text-sm font-semibold text-ink"
            onClick={onNavigateToReview}
            type="button"
          >
            {t.biographerGoToReview}
          </button>
        </div>
      )}
      {pendingIndex && (
        <div className="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-cyan/25 bg-cyan/10 p-4">
          <p className="text-sm text-fg/80">{t.biographerCandidatePendingIndex}</p>
          <button
            className="shrink-0 rounded-full bg-gradient-to-r from-cyan to-violet px-5 py-2.5 text-sm font-semibold text-ink"
            onClick={onNavigateToReview}
            type="button"
          >
            {t.biographerGoToReview}
          </button>
        </div>
      )}
      {indexed && <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.biographerCandidateIndexed}</p>}
      {!loading && activeCandidateId && (
        <form className="grid gap-4 rounded-3xl border border-cyan/20 bg-cyan/10 p-4" onSubmit={(event) => void submitClarification(event)}>
          <p className="text-xs uppercase tracking-[.18em] text-cyan/60">{t.biographerMoreDetailsNeeded}</p>
          <p className="text-sm leading-6 text-fg/75">{t.candidateClarificationPending}</p>
          {/* Task 65.10.1: the actual clarification question text - this is
              the piece that was missing entirely (both on resume and via
              submitAnswer's immediate response), leaving only the generic
              lead-in sentence above with no real question rendered. */}
          {activeClarificationQuestion && (
            <p className="text-lg font-semibold text-fg">{activeClarificationQuestion.question_text}</p>
          )}
          <Textarea label={t.candidateClarificationPlaceholder} value={answerText} onChange={setAnswerText} required maxLength={1000} />
          <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy || !answerText.trim()} type="submit">
            {busy ? t.working : t.candidateClarificationSubmit}
          </button>
        </form>
      )}
      {!loading && !activeCandidateId && eligibility?.eligible && question && (
        <form className="grid gap-4 rounded-3xl border border-white/10 bg-black/20 p-4" onSubmit={(event) => void submitAnswer(event)}>
          <Badge>{t.biographerTopicLabel}: {biographerTopicLabel(t, question.topic)}</Badge>
          <p className="text-lg font-semibold text-fg">{question.question_text}</p>
          <p className="text-xs text-fg/45">
            {t.biographerRelevanceTemplate.replace('{topic}', biographerTopicLabel(t, question.topic))}
          </p>
          <Textarea label={t.biographerAnswerPlaceholder} value={answerText} onChange={setAnswerText} required maxLength={2000} />
          <div className="flex flex-wrap gap-3">
            <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy || !answerText.trim()} type="submit">
              {busy ? t.working : t.biographerSubmit}
            </button>
            <button
              className="rounded-full border border-white/15 px-6 py-3 text-sm text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
              disabled={busy}
              onClick={() => void skip()}
              type="button"
            >
              {t.biographerSkip}
            </button>
            <button
              className="rounded-full border border-white/15 px-6 py-3 text-sm text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
              disabled={busy}
              onClick={() => void postpone()}
              type="button"
            >
              {t.biographerPostpone}
            </button>
          </div>
        </form>
      )}
      {!loading && !activeCandidateId && eligibility?.eligible && done && (
        <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.biographerDone}</p>
      )}
    </div>
  );
}

export function privacyScopeLabel(t: Copy, scope: PrivacyScope): string {
  switch (scope) {
    case 'private_owner':
      return t.candidatePrivacyPrivateOwner;
    case 'selected_family':
      return t.candidatePrivacySelectedFamily;
    case 'all_family':
      return t.candidatePrivacyAllFamily;
    case 'public_legacy':
      return t.candidatePrivacyPublicLegacy;
    default:
      return scope;
  }
}

/** Task 65.9.1 (Part F) - polls exactly one background job's status and
 * reports its terminal outcome to the caller. A separate component (rather
 * than calling `useJobStatusPoller` conditionally inside a list-rendering
 * parent) so React's rules of hooks are respected even when zero, one, or
 * many candidates/contributions each have their own in-flight job at once
 * - mounting/unmounting this component per job id is what starts/stops
 * that job's poller (Part F.8: one poller per job, never more). */
function JobStatusBadge({
  token,
  accountKey,
  profileId,
  jobId,
  t,
  onTerminal
}: {
  token: string;
  accountKey: string;
  profileId: number;
  jobId: number;
  t: Copy;
  onTerminal: (job: BackgroundJobRead) => void;
}) {
  const { job, fatalError, isTerminal } = useJobStatusPoller(token, {
    accountKey,
    profileKey: profileId,
    jobId
  });
  const firedRef = useRef(false);

  useEffect(() => {
    firedRef.current = false;
  }, [jobId]);

  useEffect(() => {
    if (isTerminal && job && !firedRef.current) {
      firedRef.current = true;
      onTerminal(job);
    }
  }, [isTerminal, job, onTerminal]);

  if (fatalError === 'unauthorized') {
    return <Badge tone="danger">{t.jobStatusUnauthorized}</Badge>;
  }
  if (fatalError === 'not_found' || !job) {
    return null;
  }
  return <Badge tone={job.status === 'failed' ? 'danger' : 'muted'}>{jobStatusLabel(t, job.status)}</Badge>;
}

export function CandidatesReviewSection({
  token,
  profileId,
  t,
  lang,
  isOwner
}: {
  token: string;
  profileId: number;
  t: Copy;
  lang: Lang;
  isOwner: boolean;
}) {
  const [candidates, setCandidates] = useState<MemoryCandidateEnrichmentRead[]>([]);
  const [loading, setLoading] = useState(true);
  const [busyId, setBusyId] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [clarificationDrafts, setClarificationDrafts] = useState<Record<number, string>>({});
  const [privacyDrafts, setPrivacyDrafts] = useState<Record<number, PrivacyScope>>({});
  const [editingId, setEditingId] = useState<number | null>(null);
  const [editDrafts, setEditDrafts] = useState<Record<number, string>>({});
  const [rejectingId, setRejectingId] = useState<number | null>(null);
  const [rejectReasonDrafts, setRejectReasonDrafts] = useState<Record<number, string>>({});
  const [confirmingIndexId, setConfirmingIndexId] = useState<number | null>(null);
  const [resultNotices, setResultNotices] = useState<Record<number, string>>({});
  // Task 65.9.1 (Part F) - candidate id -> the background job id currently
  // being polled for it (only ever set for a freshly-queued index action;
  // cleared as soon as that job reaches a terminal state).
  const [activeJobIdByCandidate, setActiveJobIdByCandidate] = useState<Record<number, number>>({});
  const [historyOpenId, setHistoryOpenId] = useState<number | null>(null);
  const [historyById, setHistoryById] = useState<Record<number, CandidateHistoryRead>>({});
  const [historyLoadingId, setHistoryLoadingId] = useState<number | null>(null);

  async function load() {
    setLoading(true);
    setError(null);
    try {
      setCandidates(await listMemoryCandidates(token, profileId));
    } catch (loadError) {
      setError(safeError(loadError));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    // Task 65.9.1 (Part F.9/F.10): switching memorial/profile (or account,
    // via `token`) must never keep polling/showing a job status that
    // belonged to a different memorial's candidate.
    setActiveJobIdByCandidate({});
    void load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token, profileId]);

  function privacyFor(candidate: MemoryCandidateEnrichmentRead): PrivacyScope {
    return privacyDrafts[candidate.candidate_id] ?? candidate.privacy_scope;
  }

  async function review(
    candidateId: number,
    action: OwnerReviewCandidateAction,
    extra: { finalized_memory_text?: string; privacy_scope?: PrivacyScope; rejection_reason?: string } = {}
  ) {
    setBusyId(candidateId);
    setError(null);
    try {
      const updated = await ownerReviewCandidate(token, profileId, candidateId, action, extra);
      setCandidates((items) => items.map((item) => (item.candidate_id === candidateId ? updated : item)));
      setEditingId(null);
      setRejectingId(null);
      if (updated.explicit_indexing_required && !updated.searchable_as_fact) {
        setResultNotices((notices) => ({ ...notices, [candidateId]: t.candidatePendingIndexNotice }));
      }
    } catch (reviewError) {
      setError(safeError(reviewError));
    } finally {
      setBusyId(null);
    }
  }

  async function answerClarification(candidateId: number) {
    const draft = clarificationDrafts[candidateId]?.trim();
    if (!draft) return;
    setBusyId(candidateId);
    setError(null);
    try {
      const updated = await answerCandidateClarification(token, profileId, candidateId, draft);
      setCandidates((items) => items.map((item) => (item.candidate_id === candidateId ? updated : item)));
      setClarificationDrafts((drafts) => ({ ...drafts, [candidateId]: '' }));
    } catch (clarificationError) {
      setError(safeError(clarificationError));
    } finally {
      setBusyId(null);
    }
  }

  async function indexMemory(candidateId: number) {
    setConfirmingIndexId(null);
    setBusyId(candidateId);
    setError(null);
    try {
      const result = await indexCandidateMemory(token, profileId, candidateId);
      // Task 65.9 (Part V): indexing is now always asynchronous - the
      // endpoint returns 202/'queued' the moment the job is created, and
      // 'indexed'/'already_indexed' is only ever returned for the no-op
      // path where the backend has *already* confirmed success. Never
      // show "Indexed and searchable" for a merely-queued job.
      const noticeByResult: Record<typeof result.result, string> = {
        already_indexed: t.candidateAlreadyIndexed,
        indexed: t.candidateIndexedLabel,
        queued: t.candidatePendingIndexLabel
      };
      setResultNotices((notices) => ({
        ...notices,
        [candidateId]: noticeByResult[result.result]
      }));
      // Task 65.9.1 (Part F): a freshly-queued job gets tracked for live
      // polling instead of only relying on the single `load()` reload
      // below - `onJobTerminal` (rendered via `JobStatusBadge`) is what
      // eventually reconciles the canonical searchable/failed state.
      if (result.result === 'queued' && typeof result.job_id === 'number') {
        setActiveJobIdByCandidate((current) => ({ ...current, [candidateId]: result.job_id as number }));
      }
      await load();
    } catch (indexError) {
      setError(safeError(indexError));
    } finally {
      setBusyId(null);
    }
  }

  function onJobTerminal(candidateId: number) {
    setActiveJobIdByCandidate((current) => {
      const { [candidateId]: _removed, ...rest } = current;
      return rest;
    });
    // The job reached a terminal state (succeeded/failed/cancelled) -
    // reload from the backend so the candidate's own
    // searchable_as_fact/promotion_status reflects the confirmed outcome
    // rather than being inferred client-side (Part F.3).
    void load();
  }

  async function toggleHistory(candidateId: number) {
    if (historyOpenId === candidateId) {
      setHistoryOpenId(null);
      return;
    }
    setHistoryOpenId(candidateId);
    if (historyById[candidateId]) return;
    setHistoryLoadingId(candidateId);
    try {
      const history = await getCandidateHistory(token, profileId, candidateId);
      setHistoryById((items) => ({ ...items, [candidateId]: history }));
    } catch (historyError) {
      setError(safeError(historyError));
    } finally {
      setHistoryLoadingId(null);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.candidatesTitle}</h3>
        <p className="mt-1 text-sm leading-6 text-fg/58">{t.candidatesSubtitle}</p>
      </div>
      {loading && <p className="text-sm text-fg/55">{t.working}</p>}
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      {!loading && candidates.length === 0 && <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.candidatesEmpty}</p>}
      <div className="grid gap-3">
        {candidates.map((candidate) => {
          const isBusy = busyId === candidate.candidate_id;
          const isEditing = editingId === candidate.candidate_id;
          const isRejecting = rejectingId === candidate.candidate_id;
          const isConfirmingIndex = confirmingIndexId === candidate.candidate_id;
          const isHistoryOpen = historyOpenId === candidate.candidate_id;
          const history = historyById[candidate.candidate_id];
          const notice = resultNotices[candidate.candidate_id];
          const canAct = candidate.review_status === 'needs_review' && !candidate.next_clarification_question && isOwner;

          return (
            <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={candidate.candidate_id}>
              <p className="break-words text-sm leading-6 text-fg/80">{candidate.finalized_memory_text || '-'}</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <Badge>{candidateStatusLabel(t, candidate.review_status)}</Badge>
                <Badge>{privacyScopeLabel(t, candidate.privacy_scope)}</Badge>
                {candidate.dispute_status === 'disputed' && <Badge tone="danger">{disputeStatusLabel(t, candidate.dispute_status)}</Badge>}
                {candidate.searchable_as_fact && <Badge tone="cyan">{t.candidateIndexedLabel}</Badge>}
                {candidate.explicit_indexing_required && !candidate.searchable_as_fact && (
                  <Badge tone="muted">{t.candidatePendingIndexLabel}</Badge>
                )}
                {candidate.promotion_status === 'failed' && <Badge tone="danger">{t.candidateIndexingFailedLabel}</Badge>}
                {activeJobIdByCandidate[candidate.candidate_id] !== undefined && (
                  <JobStatusBadge
                    accountKey={token}
                    jobId={activeJobIdByCandidate[candidate.candidate_id]}
                    onTerminal={() => onJobTerminal(candidate.candidate_id)}
                    profileId={profileId}
                    t={t}
                    token={token}
                  />
                )}
              </div>

              {notice && <p className="mt-3 rounded-2xl border border-cyan/25 bg-cyan/10 px-3 py-2 text-xs text-cyan">{notice}</p>}

              <button
                className="mt-3 text-xs text-cyan/70 underline-offset-2 hover:underline"
                onClick={() => void toggleHistory(candidate.candidate_id)}
                type="button"
              >
                {isHistoryOpen ? t.candidateHideHistory : t.candidateViewHistory}
              </button>
              {isHistoryOpen && (
                <div className="mt-3 grid gap-3 rounded-2xl border border-white/10 bg-black/25 p-3">
                  {historyLoadingId === candidate.candidate_id && <p className="text-xs text-fg/55">{t.working}</p>}
                  {history && (
                    <>
                      <div>
                        <p className="text-xs uppercase tracking-[.18em] text-fg/40">{t.candidateHistoryContributions}</p>
                        {history.contributions.length === 0 && <p className="text-xs text-fg/50">{t.candidateHistoryEmpty}</p>}
                        <div className="mt-2 grid gap-2">
                          {history.contributions.map((contribution) => (
                            <div className="rounded-xl border border-white/10 bg-black/20 p-2.5" key={contribution.contribution_id}>
                              <p className="break-words text-xs leading-5 text-fg/75">{contribution.contribution_text}</p>
                              <p className="mt-1 text-[10px] uppercase tracking-[.14em] text-fg/35">
                                {contributionTypeLabel(t, contribution.contribution_type)} - {roleLabel(t, contribution.actor_role)} - {formatDate(contribution.created_at, lang)}
                              </p>
                            </div>
                          ))}
                        </div>
                      </div>
                      <div>
                        <p className="text-xs uppercase tracking-[.18em] text-fg/40">{t.candidateHistoryClarifications}</p>
                        {history.clarifications.length === 0 && <p className="text-xs text-fg/50">{t.candidateHistoryEmpty}</p>}
                        <div className="mt-2 grid gap-2">
                          {history.clarifications.map((clarification) => (
                            <div className="rounded-xl border border-white/10 bg-black/20 p-2.5" key={clarification.clarification_id}>
                              <p className="break-words text-xs leading-5 text-fg/75">{clarification.question_text}</p>
                              <p className="mt-1 text-[10px] uppercase tracking-[.14em] text-fg/35">{clarificationStatusLabel(t, clarification.status)}</p>
                            </div>
                          ))}
                        </div>
                      </div>
                    </>
                  )}
                </div>
              )}

              {candidate.next_clarification_question && (
                <div className="mt-4 grid gap-2 rounded-2xl border border-cyan/20 bg-cyan/10 p-3">
                  <p className="text-sm text-fg/75">{candidate.next_clarification_question.question_text}</p>
                  <input
                    className="min-w-0 rounded-2xl border border-white/10 bg-black/25 px-4 py-2.5 text-fg outline-none focus:border-cyan/70"
                    onChange={(event) =>
                      setClarificationDrafts((drafts) => ({ ...drafts, [candidate.candidate_id]: event.target.value }))
                    }
                    value={clarificationDrafts[candidate.candidate_id] || ''}
                  />
                  <button
                    className="w-fit rounded-full border border-white/15 px-4 py-2 text-xs text-fg/75 transition hover:bg-white/10 disabled:opacity-55"
                    disabled={isBusy}
                    onClick={() => void answerClarification(candidate.candidate_id)}
                    type="button"
                  >
                    {t.candidateClarificationSubmit}
                  </button>
                </div>
              )}

              {canAct && (
                <div className="mt-4 grid gap-3">
                  <label className="grid min-w-0 max-w-xs gap-1.5 text-xs text-fg/60">
                    <span>{t.candidatePrivacyScopeLabel}</span>
                    <select
                      className="rounded-xl border border-white/10 bg-black/25 px-3 py-2 text-sm text-fg outline-none focus:border-cyan/70"
                      onChange={(event) =>
                        setPrivacyDrafts((drafts) => ({
                          ...drafts,
                          [candidate.candidate_id]: event.target.value as PrivacyScope
                        }))
                      }
                      value={privacyFor(candidate)}
                    >
                      {PRIVACY_SCOPES.map((scope) => (
                        <option key={scope} value={scope}>
                          {privacyScopeLabel(t, scope)}
                        </option>
                      ))}
                    </select>
                  </label>

                  {isEditing ? (
                    <div className="grid gap-2">
                      <Textarea
                        label={t.candidateEditTextareaLabel}
                        maxLength={500}
                        onChange={(value) => setEditDrafts((drafts) => ({ ...drafts, [candidate.candidate_id]: value }))}
                        value={editDrafts[candidate.candidate_id] ?? candidate.finalized_memory_text ?? ''}
                      />
                      <div className="flex flex-wrap gap-2">
                        <ActionButton
                          disabled={isBusy || !(editDrafts[candidate.candidate_id] ?? candidate.finalized_memory_text ?? '').trim()}
                          label={t.candidateEditAndConfirm}
                          onClick={() =>
                            void review(candidate.candidate_id, 'edit_and_confirm', {
                              finalized_memory_text: (
                                editDrafts[candidate.candidate_id] ?? candidate.finalized_memory_text ?? ''
                              ).trim(),
                              privacy_scope: privacyFor(candidate)
                            })
                          }
                          tone="primary"
                        />
                        <ActionButton
                          disabled={isBusy}
                          label={t.cancelAction}
                          onClick={() => setEditingId(null)}
                          tone="secondary"
                        />
                      </div>
                    </div>
                  ) : isRejecting ? (
                    <div className="grid gap-2">
                      <Field
                        label={t.candidateRejectReasonLabel}
                        onChange={(value) => setRejectReasonDrafts((drafts) => ({ ...drafts, [candidate.candidate_id]: value }))}
                        value={rejectReasonDrafts[candidate.candidate_id] ?? ''}
                      />
                      <div className="flex flex-wrap gap-2">
                        <ActionButton
                          disabled={isBusy}
                          label={t.candidateReject}
                          onClick={() =>
                            void review(candidate.candidate_id, 'reject', {
                              rejection_reason: rejectReasonDrafts[candidate.candidate_id]?.trim() || undefined
                            })
                          }
                          tone="danger"
                        />
                        <ActionButton
                          disabled={isBusy}
                          label={t.cancelAction}
                          onClick={() => setRejectingId(null)}
                          tone="secondary"
                        />
                      </div>
                    </div>
                  ) : (
                    <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
                      <ActionButton
                        disabled={isBusy}
                        label={t.candidateConfirm}
                        onClick={() => void review(candidate.candidate_id, 'confirm', { privacy_scope: privacyFor(candidate) })}
                        tone="primary"
                      />
                      <ActionButton
                        disabled={isBusy}
                        label={t.candidateEditAndConfirm}
                        onClick={() => setEditingId(candidate.candidate_id)}
                        tone="secondary"
                      />
                      {candidate.dispute_status === 'disputed' && (
                        <ActionButton
                          disabled={isBusy}
                          label={t.candidateApproveMultiplePerspectives}
                          onClick={() =>
                            void review(candidate.candidate_id, 'approve_multiple_perspectives', {
                              privacy_scope: privacyFor(candidate)
                            })
                          }
                          tone="secondary"
                        />
                      )}
                      <ActionButton
                        disabled={isBusy}
                        label={t.candidateRequestDetails}
                        onClick={() => void review(candidate.candidate_id, 'request_more_details')}
                        tone="secondary"
                      />
                      <ActionButton
                        disabled={isBusy}
                        label={t.candidateMarkDisputed}
                        onClick={() => void review(candidate.candidate_id, 'mark_disputed')}
                        tone="secondary"
                      />
                      <ActionButton
                        disabled={isBusy}
                        label={t.candidateReject}
                        onClick={() => setRejectingId(candidate.candidate_id)}
                        tone="danger"
                      />
                    </div>
                  )}
                </div>
              )}

              {(candidate.explicit_indexing_required || candidate.promotion_status === 'failed') && isOwner && (
                <div className="mt-4">
                  {isConfirmingIndex ? (
                    <div className="grid gap-3 rounded-2xl border border-cyan/25 bg-cyan/10 p-4">
                      <p className="text-sm font-semibold text-fg">{t.candidateIndexConfirmTitle}</p>
                      <p className="text-sm leading-6 text-fg/70">{t.candidateIndexConfirmBody}</p>
                      <div className="flex flex-wrap gap-3">
                        <ActionButton
                          disabled={isBusy}
                          label={t.candidateIndexConfirmYes}
                          onClick={() => void indexMemory(candidate.candidate_id)}
                          tone="primary"
                        />
                        <ActionButton
                          disabled={isBusy}
                          label={t.cancelAction}
                          onClick={() => setConfirmingIndexId(null)}
                          tone="secondary"
                        />
                      </div>
                    </div>
                  ) : (
                    <ActionButton
                      disabled={isBusy}
                      label={candidate.promotion_status === 'failed' ? t.candidateIndexRetryButton : t.candidateIndexButton}
                      onClick={() => setConfirmingIndexId(candidate.candidate_id)}
                      tone={candidate.promotion_status === 'failed' ? 'danger' : 'primary'}
                    />
                  )}
                </div>
              )}
            </article>
          );
        })}
      </div>
    </div>
  );
}

function ContributionsSection({
  contributions,
  lang,
  mayReview,
  maySubmit,
  onIndexingRetried,
  onIndexingSettled,
  onSubmitted,
  profileId,
  t,
  token
}: {
  contributions: ContributionRead[];
  lang: Lang;
  mayReview: boolean;
  maySubmit: boolean;
  onIndexingRetried: (contribution: ContributionRead) => void;
  /** Task 65.9.1 (Part F) - called once a polled indexing job (retry or
   * approval-triggered) reaches a terminal state, so the list can be
   * reconciled with the backend's confirmed outcome. */
  onIndexingSettled?: () => void;
  onSubmitted: (contribution: ContributionRead) => void;
  profileId: number;
  t: Copy;
  token: string;
}) {
  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.contributions}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.submitMemory}</p>
      </div>
      {maySubmit ? <ContributionForm onSubmitted={onSubmitted} profileId={profileId} t={t} token={token} /> : <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.viewerReadOnly}</p>}
      <ContributionList
        contributions={contributions}
        lang={lang}
        canRetryIndexing={mayReview}
        onIndexingRetried={onIndexingRetried}
        onIndexingSettled={onIndexingSettled}
        profileId={profileId}
        t={t}
        token={token}
      />
    </div>
  );
}

export function ContributionForm({
  token,
  profileId,
  t,
  onSubmitted
}: {
  token: string;
  profileId: number;
  t: Copy;
  onSubmitted: (contribution: ContributionRead) => void;
}) {
  const [title, setTitle] = useState('');
  const [memoryText, setMemoryText] = useState('');
  const [sourceNote, setSourceNote] = useState('');
  const [privacyScope, setPrivacyScope] = useState<PrivacyScope>('private_owner');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!title.trim() || !memoryText.trim()) {
      setError('Title and memory text are required.');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const contribution = await submitContribution(token, profileId, {
        title: title.trim(),
        memory_text: memoryText.trim(),
        source_note: sourceNote.trim() || null,
        privacy_scope: privacyScope
      });
      setTitle('');
      setMemoryText('');
      setSourceNote('');
      onSubmitted(contribution);
    } catch (submitError) {
      setError(safeError(submitError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <form className="grid gap-4 rounded-3xl border border-white/10 bg-black/20 p-4" onSubmit={submit}>
      <Field label={t.titleLabel} value={title} onChange={setTitle} required maxLength={200} />
      <Textarea label={t.memoryText} value={memoryText} onChange={setMemoryText} required maxLength={5000} />
      <Field label={t.sourceNote} value={sourceNote} onChange={setSourceNote} maxLength={500} />
      <label className="grid gap-2 text-sm text-fg/62">
        <span>{t.privacyScope}</span>
        <select className="min-w-0 rounded-2xl border border-white/10 bg-ink px-4 py-3 text-fg outline-none focus:border-cyan/70" onChange={(event) => setPrivacyScope(event.target.value as PrivacyScope)} value={privacyScope}>
          {PRIVACY_SCOPES.map((scope) => (
            <option key={scope} value={scope}>
              {privacyScopeLabel(t, scope)}
            </option>
          ))}
        </select>
      </label>
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
        {busy ? t.submitting : t.submitForReview}
      </button>
    </form>
  );
}

export function ContributionList({
  contributions,
  lang,
  t,
  canRetryIndexing = false,
  onIndexingRetried,
  onIndexingSettled,
  profileId,
  token
}: {
  contributions: ContributionRead[];
  lang: Lang;
  t: Copy;
  /** Task 65.8 (Part I/J): backend-authorized reviewers only - mirrors the
   * `mayReview` capability already gating the review queue. The frontend
   * flag only controls whether the button is *offered*; the backend
   * re-checks authorization and eligibility on every request regardless. */
  canRetryIndexing?: boolean;
  onIndexingRetried?: (contribution: ContributionRead) => void;
  onIndexingSettled?: () => void;
  profileId?: number;
  token?: string;
}) {
  const [retryingId, setRetryingId] = useState<number | null>(null);
  const [retryErrorById, setRetryErrorById] = useState<Record<number, string>>({});
  // Task 65.9.1 (Part F) - contribution id -> the background job id
  // currently being polled for it. Seeded/kept in sync from
  // `contribution.indexing_status.job_id` (Part F.14: recovers an
  // in-flight job after a browser refresh, not only right after this
  // component itself triggered the retry).
  const [activeJobIdByContribution, setActiveJobIdByContribution] = useState<Record<number, number>>({});
  const canOfferRetry = canRetryIndexing && typeof profileId === 'number' && typeof token === 'string' && !!onIndexingRetried;

  useEffect(() => {
    setActiveJobIdByContribution((current) => {
      const next: Record<number, number> = {};
      for (const contribution of contributions) {
        const jobId = contribution.indexing_status.job_id;
        if (contribution.indexing_status.state === 'pending' && typeof jobId === 'number') {
          next[contribution.id] = jobId;
        }
      }
      // Avoid a needless state update (and re-render) when nothing
      // actually changed - a plain reference-equality shortcut is enough
      // since both objects are small closed-set maps built fresh here.
      const unchanged =
        Object.keys(current).length === Object.keys(next).length &&
        Object.entries(next).every(([id, jobId]) => current[Number(id)] === jobId);
      return unchanged ? current : next;
    });
  }, [contributions]);

  function onJobTerminal(contributionId: number) {
    setActiveJobIdByContribution((current) => {
      const { [contributionId]: _removed, ...rest } = current;
      return rest;
    });
    onIndexingSettled?.();
  }

  async function retryIndexing(contribution: ContributionRead) {
    if (!canOfferRetry || typeof profileId !== 'number' || typeof token !== 'string' || !onIndexingRetried) return;
    setRetryingId(contribution.id);
    setRetryErrorById((current) => {
      const { [contribution.id]: _removed, ...rest } = current;
      return rest;
    });
    try {
      const updated = await retryContributionIndexing(token, profileId, contribution.id);
      onIndexingRetried(updated);
      const jobId = updated.indexing_status.job_id;
      if (updated.indexing_status.state === 'pending' && typeof jobId === 'number') {
        setActiveJobIdByContribution((current) => ({ ...current, [contribution.id]: jobId }));
      }
    } catch (retryError) {
      setRetryErrorById((current) => ({ ...current, [contribution.id]: safeError(retryError) }));
    } finally {
      setRetryingId(null);
    }
  }

  if (contributions.length === 0) {
    return <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.noContributions}</p>;
  }
  return (
    <div className="grid min-w-0 gap-3">
      {contributions.map((contribution) => {
        const showRetry = canOfferRetry && contribution.indexing_status.state === 'failed';
        const retryError = retryErrorById[contribution.id];
        return (
          <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={contribution.id}>
            <div className="flex min-w-0 flex-col gap-3 lg:flex-row lg:items-start lg:justify-between">
              <div className="min-w-0">
                <h4 className="break-words text-lg font-semibold">{contribution.title}</h4>
                <p className="mt-2 break-words text-sm leading-6 text-fg/60">{contribution.memory_text}</p>
                <p className="mt-3 text-xs text-fg/38">
                  {contribution.author_email} · {formatDate(contribution.created_at, lang)}
                </p>
                {contribution.rejection_reason && <p className="mt-2 text-sm text-red-100">{contribution.rejection_reason}</p>}
              </div>
              <div className="flex shrink-0 flex-wrap gap-2 lg:justify-end">
                <Badge>{candidateStatusLabel(t, contribution.status)}</Badge>
                <Badge tone={isActiveMemoryEligible(contribution) ? 'cyan' : 'muted'}>
                  {isActiveMemoryEligible(contribution) ? t.activeMemory : t.notActiveMemory}
                </Badge>
                {indexingStatusLabel(t, contribution.indexing_status.state) && (
                  <Badge tone={indexingStatusTone(contribution.indexing_status.state)}>
                    {indexingStatusLabel(t, contribution.indexing_status.state)}
                  </Badge>
                )}
                {typeof token === 'string' &&
                  typeof profileId === 'number' &&
                  activeJobIdByContribution[contribution.id] !== undefined && (
                    <JobStatusBadge
                      accountKey={token}
                      jobId={activeJobIdByContribution[contribution.id]}
                      onTerminal={() => onJobTerminal(contribution.id)}
                      profileId={profileId}
                      t={t}
                      token={token}
                    />
                  )}
              </div>
            </div>
            {showRetry && (
              <div className="mt-3 flex flex-col items-start gap-2">
                <ActionButton
                  disabled={retryingId === contribution.id}
                  label={t.retryIndexing}
                  onClick={() => void retryIndexing(contribution)}
                  tone="secondary"
                />
                {retryError && <p className="text-sm text-red-100">{retryError}</p>}
              </div>
            )}
          </article>
        );
      })}
    </div>
  );
}

function ReviewQueue({
  token,
  profileId,
  queue,
  t,
  lang,
  onReviewed
}: {
  token: string;
  profileId: number;
  queue: ContributionRead[];
  t: Copy;
  lang: Lang;
  onReviewed: (contribution: ContributionRead) => void;
}) {
  const [busyId, setBusyId] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function submitAction(contribution: ContributionRead, action: 'approve' | 'reject' | 'archive') {
    if (!window.confirm(`${action}: ${contribution.title}?`)) return;
    setBusyId(contribution.id);
    setError(null);
    try {
      onReviewed(await reviewContribution(token, profileId, contribution.id, action));
    } catch (reviewError) {
      setError(safeError(reviewError));
    } finally {
      setBusyId(null);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <h3 className="font-serif text-3xl">{t.review}</h3>
      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      {queue.length === 0 && <p className="rounded-2xl border border-white/10 bg-black/20 p-4 text-sm text-fg/60">{t.noPending}</p>}
      {queue.map((contribution) => (
        <article className="min-w-0 rounded-3xl border border-white/10 bg-black/20 p-4" key={contribution.id}>
          <h4 className="break-words text-lg font-semibold">{contribution.title}</h4>
          <p className="mt-2 break-words text-sm leading-6 text-fg/60">{contribution.memory_text}</p>
          <p className="mt-3 text-xs text-fg/38">
            {contribution.author_email} · {formatDate(contribution.created_at, lang)}
          </p>
          <div className="mt-4 grid gap-2 sm:grid-cols-3">
            <ActionButton disabled={busyId === contribution.id} label={t.approve} onClick={() => void submitAction(contribution, 'approve')} tone="primary" />
            <ActionButton disabled={busyId === contribution.id} label={t.reject} onClick={() => void submitAction(contribution, 'reject')} tone="secondary" />
            <ActionButton disabled={busyId === contribution.id} label={t.archive} onClick={() => void submitAction(contribution, 'archive')} tone="danger" />
          </div>
        </article>
      ))}
    </div>
  );
}

export function MembersSection({ members, t }: { members: MembershipRead[]; t: Copy }) {
  return (
    <div className="min-w-0 space-y-5">
      <h3 className="font-serif text-3xl">{t.members}</h3>
      <div className="grid gap-3">
        {members.map((member) => (
          <article className="flex min-w-0 flex-col gap-2 rounded-3xl border border-white/10 bg-black/20 p-4 sm:flex-row sm:items-center sm:justify-between" key={member.id}>
            <div className="min-w-0">
              <h4 className="truncate text-base font-semibold">{member.email}</h4>
              <p className="text-sm text-fg/45">{member.full_name || '-'}</p>
            </div>
            <Badge>{roleLabel(t, member.role)}</Badge>
          </article>
        ))}
      </div>
    </div>
  );
}

export function InvitationSection({ token, profileId, t, onInvited }: { token: string; profileId: number; t: Copy; onInvited: (invitation: InvitationCreateResponse) => void }) {
  const [email, setEmail] = useState('');
  const [role, setRole] = useState<InvitableMemorialRole>('contributor');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lastInvitation, setLastInvitation] = useState<InvitationCreateResponse | null>(null);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const normalizedEmail = normalizeEmail(email);
    if (!normalizedEmail.includes('@')) {
      setError('Enter a valid email address.');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const invitation = await inviteParticipant(token, profileId, { email: normalizedEmail, role });
      setLastInvitation(invitation);
      setEmail('');
      onInvited(invitation);
    } catch (inviteError) {
      setError(safeError(inviteError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="min-w-0 space-y-5">
      <div>
        <h3 className="font-serif text-3xl">{t.invitations}</h3>
        <p className="mt-2 text-sm leading-6 text-fg/58">{t.inviteHelp}</p>
      </div>
      <form className="grid gap-4 rounded-3xl border border-white/10 bg-black/20 p-4" onSubmit={submit}>
        <Field label={t.email} value={email} onChange={setEmail} type="email" required />
        <label className="grid gap-2 text-sm text-fg/62">
          <span>{t.role}</span>
          <select className="min-w-0 rounded-2xl border border-white/10 bg-ink px-4 py-3 text-fg outline-none focus:border-cyan/70" onChange={(event) => setRole(event.target.value as InvitableMemorialRole)} value={role}>
            {INVITE_ROLES.map((item) => (
              <option key={item} value={item}>
                {roleLabel(t, item)}
              </option>
            ))}
          </select>
        </label>
        {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
        <button className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55" disabled={busy} type="submit">
          {busy ? t.working : t.inviteParticipant}
        </button>
      </form>
      {lastInvitation?.token && (
        <div className="min-w-0 rounded-3xl border border-cyan/20 bg-cyan/10 p-4">
          <strong className="text-cyan">{t.devToken}</strong>
          <p className="mt-2 text-sm leading-6 text-fg/60">{t.tokenNote}</p>
          <p className="mt-3 break-all rounded-2xl border border-white/10 bg-black/30 p-3 font-mono text-xs text-fg/80">{lastInvitation.token}</p>
        </div>
      )}
    </div>
  );
}

function Field({
  label,
  value,
  onChange,
  type = 'text',
  required = false,
  maxLength
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  type?: string;
  required?: boolean;
  maxLength?: number;
}) {
  return (
    <label className="grid min-w-0 gap-2 text-sm text-fg/62">
      <span>{label}</span>
      <input
        className="min-w-0 rounded-2xl border border-white/10 bg-black/25 px-4 py-3 text-fg outline-none transition placeholder:text-fg/30 focus:border-cyan/70"
        maxLength={maxLength}
        onChange={(event) => onChange(event.target.value)}
        required={required}
        type={type}
        value={value}
      />
    </label>
  );
}

function Textarea({
  label,
  value,
  onChange,
  required = false,
  maxLength
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  required?: boolean;
  maxLength?: number;
}) {
  return (
    <label className="grid min-w-0 gap-2 text-sm text-fg/62">
      <span>{label}</span>
      <textarea
        className="min-h-28 min-w-0 resize-y rounded-2xl border border-white/10 bg-black/25 px-4 py-3 text-fg outline-none transition placeholder:text-fg/30 focus:border-cyan/70"
        maxLength={maxLength}
        onChange={(event) => onChange(event.target.value)}
        required={required}
        value={value}
      />
    </label>
  );
}

function Badge({ children, tone = 'muted' }: { children: ReactNode; tone?: 'muted' | 'cyan' | 'danger' }) {
  const toneClassName =
    tone === 'cyan' ? 'bg-cyan/15 text-cyan' : tone === 'danger' ? 'bg-red-500/15 text-red-200' : 'bg-white/10 text-fg/62';
  return <span className={`w-fit rounded-full px-3 py-1 text-xs ${toneClassName}`}>{children}</span>;
}

function indexingStatusLabel(t: Copy, state: ContributionRead['indexing_status']['state']): string | null {
  if (state === 'pending') return t.indexingPending;
  if (state === 'indexed') return t.indexingIndexed;
  if (state === 'failed') return t.indexingFailed;
  if (state === 'retired') return t.indexingRetired;
  return null;
}

function indexingStatusTone(state: ContributionRead['indexing_status']['state']): 'cyan' | 'muted' | 'danger' {
  if (state === 'indexed') return 'cyan';
  if (state === 'failed') return 'danger';
  return 'muted';
}

function ActionButton({ disabled, label, onClick, tone }: { disabled: boolean; label: string; onClick: () => void; tone: 'primary' | 'secondary' | 'danger' }) {
  const className =
    tone === 'primary'
      ? 'bg-gradient-to-r from-cyan to-violet text-ink'
      : tone === 'danger'
        ? 'border border-red-300/30 bg-red-500/10 text-red-100'
        : 'border border-white/15 bg-white/[.04] text-fg/75';
  return (
    <button className={`min-w-0 rounded-full px-4 py-3 text-sm font-semibold disabled:opacity-55 ${className}`} disabled={disabled} onClick={onClick} type="button">
      {label}
    </button>
  );
}

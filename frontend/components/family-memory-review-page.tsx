"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";

import {
  ApiRequestError,
  fetchMemoryCandidateReviewDetail,
  fetchMemoryCandidateSummaries,
  retryMemoryCandidateTranslation,
  submitIndexMemoryPromotion,
  submitOwnerReview,
} from "../lib/api/family-memory-review";
import { getDictionary, type Dictionary } from "../lib/i18n/get-dictionary";
import { toIntlLocaleTag, type AppLocale } from "../lib/i18n/locales";
import { LanguageSwitcher } from "./language-switcher";
import type {
  ActorContext,
  ClarificationQuestionRead,
  ContributionType,
  FamilyMemoryContributionRead,
  MemoryCandidateReviewDetail,
  MemoryCandidateSummary,
  MemoryContentTranslation,
  OwnerReviewAction,
  PrivacyScope,
} from "../types/family-memory";
import styles from "./family-memory-review-page.module.css";

const FINALIZED_TEXT_MAX_LENGTH = 500;
const NOTE_MAX_LENGTH = 500;

function buildDemoActors(dictionary: Dictionary): { key: string; actor: ActorContext; label: string }[] {
  return [
    {
      key: "owner",
      actor: { actorId: "demo-owner-eva", actorRole: "owner" },
      label: dictionary.actorBar.ownerLabel,
    },
    {
      key: "contributor",
      actor: { actorId: "family-anna", actorRole: "contributor", relationshipToOwner: "внучка" },
      label: dictionary.actorBar.contributorLabel,
    },
  ];
}

type FilterValue =
  | "all"
  | "needs_review"
  | "collecting_details"
  | "ready_for_owner_review"
  | "approved"
  | "rejected"
  | "disputed"
  | "pending_index"
  | "indexed";

const FILTER_VALUES: FilterValue[] = [
  "all",
  "needs_review",
  "collecting_details",
  "ready_for_owner_review",
  "approved",
  "rejected",
  "disputed",
  "pending_index",
  "indexed",
];

function blockedReasonLabel(dictionary: Dictionary, reason: string): string {
  const known = (dictionary.blockedReasons as Record<string, string>)[reason];
  if (known) {
    return known;
  }
  return reason.startsWith("promotion_status_") ? "" : reason;
}

function formatDateTime(value: string | null, locale: AppLocale): string {
  if (!value) {
    return "—";
  }
  try {
    return new Date(value).toLocaleString(toIntlLocaleTag(locale), {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  } catch {
    return value;
  }
}

function truncate(value: string, limit: number): string {
  if (value.length <= limit) {
    return value;
  }
  return `${value.slice(0, limit - 1).trimEnd()}…`;
}

function candidateCardTitle(item: MemoryCandidateSummary): string {
  const text = item.finalized_memory_text || item.user_message_excerpt;
  return truncate(text, 110);
}

type PendingAction =
  | { type: OwnerReviewAction }
  | { type: "index" };

function translationStatusLabel(
  dictionary: Dictionary,
  status: MemoryContentTranslation["translation_status"] | "source"
): string {
  switch (status) {
    case "source":
      return dictionary.translationPanel.statusOriginal;
    case "translated":
      return dictionary.translationPanel.statusTranslated;
    case "pending":
      return dictionary.translationPanel.statusPending;
    case "failed":
      return dictionary.translationPanel.statusFailed;
    case "stale":
      return dictionary.translationPanel.statusStale;
    case "human_reviewed":
      return dictionary.translationPanel.statusHumanReviewed;
    default:
      return status;
  }
}

/** Finds the current translation row for the candidate's finalized memory
 * text targeting the given language, if one exists. */
function findFinalizedTranslation(
  translations: MemoryContentTranslation[] | undefined,
  targetLanguage: AppLocale
): MemoryContentTranslation | null {
  return (
    (translations ?? []).find(
      (row) =>
        row.entity_type === "memory_candidate" &&
        row.field_name === "finalized_memory_text" &&
        row.target_language === targetLanguage
    ) ?? null
  );
}

export function FamilyMemoryReviewPage({ locale }: { locale: AppLocale }) {
  const dictionary = getDictionary(locale);
  const demoActors = useMemo(() => buildDemoActors(dictionary), [dictionary]);

  const searchParams = useSearchParams();
  const deepLinkCandidateId = searchParams?.get("candidate");

  const [actorKey, setActorKey] = useState<string>("owner");
  const actor = useMemo(
    () => demoActors.find((item) => item.key === actorKey)?.actor ?? demoActors[0].actor,
    [actorKey, demoActors]
  );
  const isOwnerSelected = actor.actorRole === "owner";

  const [summaries, setSummaries] = useState<MemoryCandidateSummary[] | null>(null);
  const [summariesLoading, setSummariesLoading] = useState(true);
  const [summariesError, setSummariesError] = useState<string | null>(null);
  const [filterValue, setFilterValue] = useState<FilterValue>("all");
  const [debugEnabled, setDebugEnabled] = useState(false);

  const [selectedCandidateId, setSelectedCandidateId] = useState<number | null>(null);
  const [detail, setDetail] = useState<MemoryCandidateReviewDetail | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);
  const [detailError, setDetailError] = useState<string | null>(null);

  const [editableFinalizedText, setEditableFinalizedText] = useState("");
  const [privacyScope, setPrivacyScope] = useState<PrivacyScope>("private_owner");
  const [reviewNote, setReviewNote] = useState("");
  const [rejectionReason, setRejectionReason] = useState("");
  const [pendingAction, setPendingAction] = useState<PendingAction | null>(null);
  const [actionBusy, setActionBusy] = useState(false);
  const [actionError, setActionError] = useState<string | null>(null);
  const [lastResultMessage, setLastResultMessage] = useState<string | null>(null);
  const [translationRetryBusy, setTranslationRetryBusy] = useState(false);
  const actionBusyRef = useRef(false);

  const deepLinkAppliedRef = useRef(false);

  const loadSummaries = useCallback(async () => {
    setSummariesLoading(true);
    setSummariesError(null);
    try {
      const response = await fetchMemoryCandidateSummaries(null, actor, locale);
      setSummaries(response.items);
    } catch (error) {
      setSummaries(null);
      setSummariesError(error instanceof ApiRequestError ? error.detail : dictionary.inbox.loadError);
    } finally {
      setSummariesLoading(false);
    }
  }, [actor, locale, dictionary.inbox.loadError]);

  const loadDetail = useCallback(
    async (candidateId: number) => {
      setDetailLoading(true);
      setDetailError(null);
      try {
        const response = await fetchMemoryCandidateReviewDetail(candidateId, null, actor, locale);
        setDetail(response);
        setEditableFinalizedText(response.candidate.finalized_memory_text ?? "");
        setPrivacyScope(
          response.enrichment?.privacy_scope ?? response.candidate.privacy_scope ?? "private_owner"
        );
        setReviewNote("");
        setRejectionReason("");
      } catch (error) {
        setDetail(null);
        setDetailError(error instanceof ApiRequestError ? error.detail : dictionary.detail.loadError);
      } finally {
        setDetailLoading(false);
      }
    },
    [actor, locale, dictionary.detail.loadError]
  );

  useEffect(() => {
    void loadSummaries();
  }, [loadSummaries]);

  useEffect(() => {
    if (!deepLinkAppliedRef.current && deepLinkCandidateId) {
      deepLinkAppliedRef.current = true;
      const parsed = Number(deepLinkCandidateId);
      if (Number.isInteger(parsed) && parsed > 0) {
        setSelectedCandidateId(parsed);
      }
    }
  }, [deepLinkCandidateId]);

  useEffect(() => {
    if (selectedCandidateId !== null) {
      void loadDetail(selectedCandidateId);
      setActionError(null);
      setLastResultMessage(null);
    } else {
      setDetail(null);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedCandidateId, actor]);

  const filteredSummaries = useMemo(() => {
    if (!summaries) {
      return [];
    }
    switch (filterValue) {
      case "all":
        return summaries;
      case "needs_review":
        return summaries.filter((item) => item.status === "needs_review");
      case "collecting_details":
        return summaries.filter((item) => item.enrichment_status === "collecting_details");
      case "ready_for_owner_review":
        return summaries.filter(
          (item) => item.enrichment_status === "ready_for_owner_review" && item.status === "needs_review"
        );
      case "approved":
        return summaries.filter((item) => item.status === "approved");
      case "rejected":
        return summaries.filter((item) => item.status === "rejected");
      case "disputed":
        return summaries.filter((item) => item.dispute_status === "disputed");
      case "pending_index":
        return summaries.filter((item) => item.promotion_status === "pending_index");
      case "indexed":
        return summaries.filter((item) => item.promotion_status === "indexed");
      default:
        return summaries;
    }
  }, [summaries, filterValue]);

  const isTextEdited =
    detail !== null && editableFinalizedText.trim() !== (detail.candidate.finalized_memory_text ?? "").trim();

  async function refreshAfterAction() {
    await loadSummaries();
    if (selectedCandidateId !== null) {
      await loadDetail(selectedCandidateId);
    }
  }

  async function runOwnerReviewAction(action: OwnerReviewAction) {
    if (!detail) {
      return;
    }
    const payload = {
      actor_id: actor.actorId,
      actor_role: actor.actorRole,
      relationship_to_owner: actor.relationshipToOwner ?? null,
      action,
      privacy_scope: privacyScope,
      review_note: reviewNote.trim() ? reviewNote.trim() : null,
      rejection_reason: action === "reject" && rejectionReason.trim() ? rejectionReason.trim() : null,
      finalized_memory_text:
        action === "edit_and_confirm" || action === "approve_multiple_perspectives"
          ? editableFinalizedText.trim()
          : null,
    };
    setActionBusy(true);
    setActionError(null);
    try {
      const response = await submitOwnerReview(detail.candidate.candidate_id, payload, locale);
      setLastResultMessage(
        response.review_status === "approved"
          ? dictionary.resultMessages.approved
          : response.review_status === "rejected"
            ? dictionary.resultMessages.rejected
            : dictionary.resultMessages.statusUpdated
      );
      await refreshAfterAction();
    } catch (error) {
      if (error instanceof ApiRequestError && error.status === 409) {
        setActionError(dictionary.errors.statusChanged);
        await refreshAfterAction();
      } else {
        setActionError(error instanceof ApiRequestError ? error.detail : dictionary.errors.genericAction);
      }
    } finally {
      setActionBusy(false);
      setPendingAction(null);
    }
  }

  async function runIndexAction() {
    if (!detail?.promotion) {
      return;
    }
    if (actionBusyRef.current) {
      return;
    }
    actionBusyRef.current = true;
    setActionBusy(true);
    setActionError(null);
    try {
      const result = await submitIndexMemoryPromotion(detail.promotion.promotion_id, null, actor, locale);
      setLastResultMessage(
        result.result === "already_indexed"
          ? dictionary.resultMessages.alreadyIndexed
          : dictionary.resultMessages.indexed
      );
      await refreshAfterAction();
    } catch (error) {
      if (error instanceof ApiRequestError && error.status === 409) {
        setActionError(dictionary.errors.promotionStateChanged);
        await refreshAfterAction();
      } else if (error instanceof ApiRequestError && error.status === 503) {
        setActionError(dictionary.detail.promotionIndexFailed);
      } else {
        setActionError(error instanceof ApiRequestError ? error.detail : dictionary.errors.genericAction);
      }
    } finally {
      actionBusyRef.current = false;
      setActionBusy(false);
      setPendingAction(null);
    }
  }

  async function runTranslationRetry() {
    if (!detail || translationRetryBusy) {
      return;
    }
    setTranslationRetryBusy(true);
    setActionError(null);
    try {
      await retryMemoryCandidateTranslation(detail.candidate.candidate_id, "ru", null, actor, locale);
      await refreshAfterAction();
    } catch (error) {
      setActionError(error instanceof ApiRequestError ? error.detail : dictionary.errors.translationFailed);
    } finally {
      setTranslationRetryBusy(false);
    }
  }

  function confirmPendingAction() {
    if (!pendingAction) {
      return;
    }
    if (pendingAction.type === "index") {
      void runIndexAction();
    } else {
      void runOwnerReviewAction(pendingAction.type);
    }
  }

  const primaryConfirmAction: OwnerReviewAction = isTextEdited ? "edit_and_confirm" : "confirm";
  const primaryConfirmAllowed = detail
    ? (isTextEdited ? detail.can_edit_and_confirm : detail.can_confirm)
    : false;

  const isCzechOrigin = detail?.source_language === "cs";
  const russianTranslation = detail ? findFinalizedTranslation(detail.translations, "ru") : null;

  return (
    <main className={styles.page}>
      <header className={styles.pageHeader}>
        <div>
          <p className={styles.eyebrow}>{dictionary.eyebrow}</p>
          <h1 className={styles.title}>{dictionary.reviewTitle}</h1>
        </div>
        <div className={styles.headerTools}>
          <LanguageSwitcher currentLocale={locale} />
          <Link className={styles.backLink} href={`/${locale}/fa-chat`}>
            {dictionary.nav.backToChat}
          </Link>
        </div>
      </header>

      <div className={styles.demoWarning} role="note">
        {dictionary.demoWarning}
      </div>

      <div className={styles.actorBar}>
        <label className={styles.actorLabel} htmlFor="demo-actor-select">
          {dictionary.actorBar.label}
        </label>
        <select
          className={styles.actorSelect}
          id="demo-actor-select"
          onChange={(event) => setActorKey(event.target.value)}
          value={actorKey}
        >
          {demoActors.map((item) => (
            <option key={item.key} value={item.key}>
              {item.label}
            </option>
          ))}
        </select>
        <label className={styles.toggle}>
          <input
            checked={debugEnabled}
            onChange={(event) => setDebugEnabled(event.target.checked)}
            type="checkbox"
          />
          <span>{dictionary.actorBar.technicalDetails}</span>
        </label>
      </div>

      <div className={styles.layout}>
        <section aria-label={dictionary.inbox.ariaLabel} className={styles.inboxColumn}>
          <div className={styles.filterRow}>
            {FILTER_VALUES.map((value) => (
              <button
                aria-pressed={filterValue === value}
                className={`${styles.filterChip} ${filterValue === value ? styles.filterChipActive : ""}`}
                key={value}
                onClick={() => setFilterValue(value)}
                type="button"
              >
                {dictionary.inbox.filters[value]}
              </button>
            ))}
          </div>

          {summariesLoading ? (
            <div className={styles.skeletonList} data-testid="inbox-loading">
              <div className={styles.skeletonCard} />
              <div className={styles.skeletonCard} />
              <div className={styles.skeletonCard} />
            </div>
          ) : summariesError ? (
            <div className={styles.errorBanner} role="alert">
              <p>{summariesError}</p>
              <button className={styles.retryButton} onClick={() => void loadSummaries()} type="button">
                {dictionary.inbox.retry}
              </button>
            </div>
          ) : filteredSummaries.length === 0 ? (
            <div className={styles.emptyCard}>
              {summaries && summaries.length === 0 ? dictionary.inbox.emptyNoEpisodes : dictionary.inbox.emptyFiltered}
            </div>
          ) : (
            <ul className={styles.candidateList}>
              {filteredSummaries.map((item) => (
                <li key={item.candidate_id}>
                  <button
                    aria-current={selectedCandidateId === item.candidate_id}
                    className={`${styles.candidateCard} ${
                      selectedCandidateId === item.candidate_id ? styles.candidateCardSelected : ""
                    }`}
                    onClick={() => setSelectedCandidateId(item.candidate_id)}
                    type="button"
                  >
                    <div className={styles.candidateCardTitle}>{candidateCardTitle(item)}</div>
                    <div className={styles.candidateCardMeta}>
                      {item.contributor_actor_id ? (
                        <span>
                          {dictionary.inbox.contributorFrom} {item.contributor_actor_id}
                          {item.contributor_relationship_to_owner
                            ? ` (${item.contributor_relationship_to_owner})`
                            : ""}
                        </span>
                      ) : (
                        <span>{dictionary.inbox.contributorUnknown}</span>
                      )}
                      <span>{formatDateTime(item.updated_at, locale)}</span>
                    </div>
                    <div className={styles.badgeRow}>
                      <span className={styles.badge}>{dictionary.reviewStatus[item.status]}</span>
                      <span className={styles.badge}>{dictionary.enrichmentStatus[item.enrichment_status]}</span>
                      {item.dispute_status === "disputed" ? (
                        <span className={`${styles.badge} ${styles.badgeWarning}`}>
                          {dictionary.disputeStatus.disputed}
                        </span>
                      ) : null}
                      {item.promotion_status ? (
                        <span className={styles.badge}>{dictionary.promotionStatus[item.promotion_status]}</span>
                      ) : null}
                      {item.unresolved_clarification_count > 0 ? (
                        <span className={`${styles.badge} ${styles.badgeInfo}`}>
                          {dictionary.inbox.unresolvedQuestions}: {item.unresolved_clarification_count}
                        </span>
                      ) : null}
                    </div>
                    {debugEnabled ? (
                      <div className={styles.debugLine}>id: {item.candidate_id}</div>
                    ) : null}
                  </button>
                </li>
              ))}
            </ul>
          )}
        </section>

        <section aria-label={dictionary.detail.ariaLabel} className={styles.detailColumn}>
          {selectedCandidateId === null ? (
            <div className={styles.emptyCard}>{dictionary.detail.selectPrompt}</div>
          ) : detailLoading ? (
            <div className={styles.skeletonList} data-testid="detail-loading">
              <div className={styles.skeletonCard} />
              <div className={styles.skeletonCard} />
            </div>
          ) : detailError ? (
            <div className={styles.errorBanner} role="alert">
              <p>{detailError}</p>
              <button
                className={styles.retryButton}
                onClick={() => void loadDetail(selectedCandidateId)}
                type="button"
              >
                {dictionary.inbox.retry}
              </button>
            </div>
          ) : detail ? (
            <div className={styles.detailContent}>
              {lastResultMessage ? (
                <div className={styles.successBanner} role="status">
                  {lastResultMessage}
                </div>
              ) : null}
              {actionError ? (
                <div className={styles.errorBanner} role="alert">
                  {actionError}
                </div>
              ) : null}

              {!isOwnerSelected ? (
                <div className={styles.contributorNotice} role="note">
                  {dictionary.detail.contributorNotice}
                </div>
              ) : null}

              <section className={styles.overviewCard}>
                <div className={styles.badgeRow}>
                  <span className={styles.badge}>{dictionary.reviewStatus[detail.candidate.status]}</span>
                  <span className={styles.badge}>
                    {dictionary.enrichmentStatus[detail.candidate.enrichment_status]}
                  </span>
                  <span className={styles.badge}>{dictionary.disputeStatus[detail.candidate.dispute_status]}</span>
                  {detail.promotion ? (
                    <span className={styles.badge}>
                      {dictionary.promotionStatus[detail.promotion.promotion_status]}
                    </span>
                  ) : null}
                  <span className={detail.promotion?.searchable_as_fact ? styles.badgeSuccess : styles.badge}>
                    {detail.promotion?.searchable_as_fact
                      ? dictionary.detail.availableToAvatar
                      : dictionary.detail.notYetAvailableToAvatar}
                  </span>
                  {isCzechOrigin ? (
                    <span className={styles.badge}>{dictionary.translationPanel.sourceOfCzechOrigin}</span>
                  ) : null}
                </div>
                <p className={styles.overviewExcerpt}>{detail.candidate.user_message_excerpt}</p>
                {debugEnabled ? (
                  <details className={styles.debugDetails}>
                    <summary>{dictionary.detail.technicalData}</summary>
                    <ul>
                      <li>candidate_id: {detail.candidate.candidate_id}</li>
                      <li>promotion_id: {detail.promotion?.promotion_id ?? "—"}</li>
                      <li>target_collection_name: {detail.promotion?.target_collection_name ?? "—"}</li>
                      <li>qdrant_point_id: {detail.promotion?.qdrant_point_id ?? "—"}</li>
                      <li>source_language: {detail.source_language ?? "—"}</li>
                    </ul>
                  </details>
                ) : null}
              </section>

              {isCzechOrigin || russianTranslation ? (
                <section aria-label={dictionary.translationPanel.title} className={styles.translationCard}>
                  <h2 className={styles.sectionTitle}>{dictionary.translationPanel.title}</h2>
                  <div className={styles.translationGrid}>
                    <div className={styles.translationColumn}>
                      <h3 className={styles.translationColumnHeading}>
                        {dictionary.translationPanel.czechSourceHeading}
                      </h3>
                      <p className={styles.timelineText}>
                        {isCzechOrigin ? detail.candidate.finalized_memory_text : "—"}
                      </p>
                      <span className={styles.badge}>{dictionary.translationPanel.statusOriginal}</span>
                    </div>
                    <div className={styles.translationColumn}>
                      <h3 className={styles.translationColumnHeading}>
                        {dictionary.translationPanel.russianVersionHeading}
                      </h3>
                      <p className={styles.timelineText}>
                        {russianTranslation?.translated_text ?? dictionary.translationPanel.noTranslationYet}
                      </p>
                      <span
                        className={
                          russianTranslation?.translation_status === "translated" ||
                          russianTranslation?.translation_status === "human_reviewed"
                            ? styles.badgeSuccess
                            : russianTranslation?.translation_status === "failed"
                              ? `${styles.badge} ${styles.badgeWarning}`
                              : styles.badge
                        }
                      >
                        {russianTranslation
                          ? translationStatusLabel(dictionary, russianTranslation.translation_status)
                          : translationStatusLabel(dictionary, "pending")}
                      </span>
                      {russianTranslation?.translated_at ? (
                        <p className={styles.mutedText}>
                          {dictionary.translationPanel.lastTranslatedAt}{" "}
                          {formatDateTime(russianTranslation.translated_at, locale)}
                        </p>
                      ) : null}
                    </div>
                  </div>
                  {detail.translation_block_reason ? (
                    <p className={styles.errorBanner} role="alert">
                      {dictionary.translationPanel.cannotIndexNotice}
                    </p>
                  ) : null}
                  {isOwnerSelected ? (
                    <button
                      className={styles.secondaryButton}
                      disabled={translationRetryBusy}
                      onClick={() => void runTranslationRetry()}
                      type="button"
                    >
                      {dictionary.translationPanel.retryTranslation}
                    </button>
                  ) : null}
                </section>
              ) : null}

              <section aria-label={dictionary.detail.contributionHistoryTitle} className={styles.timelineCard}>
                <h2 className={styles.sectionTitle}>{dictionary.detail.contributionHistoryTitle}</h2>
                {detail.contributions.length === 0 ? (
                  <p className={styles.mutedText}>{dictionary.detail.contributionHistoryEmpty}</p>
                ) : (
                  <ol className={styles.timelineList}>
                    {detail.contributions.map((item: FamilyMemoryContributionRead) => (
                      <li className={styles.timelineItem} key={item.contribution_id}>
                        <div className={styles.timelineItemHeader}>
                          <span className={styles.timelineType}>
                            {dictionary.contributionType[item.contribution_type as ContributionType]}
                          </span>
                          <span className={styles.timelineDate}>{formatDateTime(item.created_at, locale)}</span>
                        </div>
                        <div className={styles.timelineActor}>
                          {item.actor_id}
                          {item.relationship_to_owner ? ` (${item.relationship_to_owner})` : ""}
                          {item.is_owner_correction ? ` · ${dictionary.detail.ownerCorrection}` : ""}
                          {item.is_disputed ? ` · ${dictionary.detail.disputedSuffix}` : ""}
                        </div>
                        <p className={styles.timelineText}>{item.contribution_text}</p>
                      </li>
                    ))}
                  </ol>
                )}
              </section>

              <section aria-label={dictionary.detail.clarificationsTitle} className={styles.timelineCard}>
                <h2 className={styles.sectionTitle}>{dictionary.detail.clarificationsTitle}</h2>
                {detail.clarifications.length === 0 ? (
                  <p className={styles.mutedText}>{dictionary.detail.clarificationsEmpty}</p>
                ) : (
                  <ul className={styles.timelineList}>
                    {detail.clarifications.map((item: ClarificationQuestionRead) => (
                      <li className={styles.timelineItem} key={item.clarification_id}>
                        <div className={styles.timelineItemHeader}>
                          <span
                            className={
                              item.status === "pending" && item.required
                                ? `${styles.timelineType} ${styles.timelineTypeWarning}`
                                : styles.timelineType
                            }
                          >
                            {dictionary.clarificationStatus[item.status]}
                            {" · "}
                            {item.required ? dictionary.detail.requiredSuffix : dictionary.detail.optionalSuffix}
                          </span>
                        </div>
                        <p className={styles.timelineText}>{item.question_text}</p>
                        {item.answered_at ? (
                          <p className={styles.mutedText}>
                            {dictionary.detail.answeredAt} {formatDateTime(item.answered_at, locale)}
                          </p>
                        ) : null}
                      </li>
                    ))}
                  </ul>
                )}
              </section>

              {detail.candidate.dispute_status === "disputed" ? (
                <section aria-label={dictionary.detail.disputeTitle} className={styles.disputeCard}>
                  <h2 className={styles.sectionTitle}>{dictionary.detail.disputeTitle}</h2>
                  <p className={styles.disputeWarning}>{dictionary.detail.disputeWarning}</p>
                  <ul className={styles.timelineList}>
                    {detail.contributions
                      .filter((item) => item.is_disputed || item.contribution_type === "owner_correction")
                      .map((item) => (
                        <li className={styles.timelineItem} key={`perspective-${item.contribution_id}`}>
                          <div className={styles.timelineActor}>
                            {item.actor_role === "owner"
                              ? dictionary.detail.ownerPerspective
                              : dictionary.detail.contributorPerspective}
                          </div>
                          <p className={styles.timelineText}>{item.contribution_text}</p>
                        </li>
                      ))}
                  </ul>
                </section>
              ) : null}

              <section aria-label={dictionary.detail.finalTextTitle} className={styles.editorCard}>
                <h2 className={styles.sectionTitle}>{dictionary.detail.finalTextTitle}</h2>
                <label className={styles.visuallyHidden} htmlFor="finalized-memory-text">
                  {dictionary.detail.finalTextTitle}
                </label>
                <textarea
                  className={styles.editorTextarea}
                  disabled={!isOwnerSelected}
                  id="finalized-memory-text"
                  maxLength={FINALIZED_TEXT_MAX_LENGTH}
                  onChange={(event) => setEditableFinalizedText(event.target.value)}
                  rows={4}
                  value={editableFinalizedText}
                />
                <div className={styles.editorFooter}>
                  <span className={styles.charCount}>
                    {editableFinalizedText.length}/{FINALIZED_TEXT_MAX_LENGTH}
                  </span>
                  {isTextEdited ? (
                    <button
                      className={styles.resetButton}
                      disabled={!isOwnerSelected}
                      onClick={() => setEditableFinalizedText(detail.candidate.finalized_memory_text ?? "")}
                      type="button"
                    >
                      {dictionary.detail.resetOriginalText}
                    </button>
                  ) : null}
                </div>
                {isTextEdited ? <p className={styles.mutedText}>{dictionary.detail.textEditedNotice}</p> : null}
              </section>

              <section aria-label={dictionary.detail.privacyTitle} className={styles.privacyCard}>
                <h2 className={styles.sectionTitle}>{dictionary.detail.privacyTitle}</h2>
                <div className={styles.privacyOptions} role="radiogroup" aria-label={dictionary.detail.privacyTitle}>
                  {(Object.keys(dictionary.privacyScope) as PrivacyScope[]).map((value) => (
                    <label className={styles.privacyOption} key={value}>
                      <input
                        checked={privacyScope === value}
                        disabled={!isOwnerSelected}
                        name="privacy-scope"
                        onChange={() => setPrivacyScope(value)}
                        type="radio"
                        value={value}
                      />
                      <span>
                        <strong>{dictionary.privacyScope[value].label}</strong>
                        <br />
                        <span className={styles.mutedText}>{dictionary.privacyScope[value].description}</span>
                      </span>
                    </label>
                  ))}
                </div>
              </section>

              <section aria-label={dictionary.detail.actionsTitle} className={styles.actionsCard}>
                <h2 className={styles.sectionTitle}>{dictionary.detail.actionsTitle}</h2>
                <label className={styles.visuallyHidden} htmlFor="review-note">
                  {dictionary.detail.reviewNotePlaceholder}
                </label>
                <textarea
                  className={styles.noteTextarea}
                  disabled={!isOwnerSelected}
                  id="review-note"
                  maxLength={NOTE_MAX_LENGTH}
                  onChange={(event) => setReviewNote(event.target.value)}
                  placeholder={dictionary.detail.reviewNotePlaceholder}
                  rows={2}
                  value={reviewNote}
                />

                {!detail.is_owner_actor && detail.blocked_reasons.includes("actor_is_not_owner") ? (
                  <p className={styles.mutedText}>{dictionary.detail.switchToOwnerNotice}</p>
                ) : null}

                {detail.blocked_reasons
                  .filter((reason) => reason !== "actor_is_not_owner" && blockedReasonLabel(dictionary, reason))
                  .map((reason) => (
                    <p className={styles.blockedReason} key={reason}>
                      {blockedReasonLabel(dictionary, reason)}
                    </p>
                  ))}

                <div className={styles.actionButtonRow}>
                  <button
                    className={styles.primaryButton}
                    disabled={!primaryConfirmAllowed || actionBusy}
                    onClick={() => setPendingAction({ type: primaryConfirmAction })}
                    type="button"
                  >
                    {dictionary.actions[primaryConfirmAction]}
                  </button>
                  <button
                    className={styles.secondaryButton}
                    disabled={!detail.can_reject || actionBusy}
                    onClick={() => setPendingAction({ type: "reject" })}
                    type="button"
                  >
                    {dictionary.actions.reject}
                  </button>
                  <button
                    className={styles.secondaryButton}
                    disabled={!detail.can_request_more_details || actionBusy}
                    onClick={() => setPendingAction({ type: "request_more_details" })}
                    type="button"
                  >
                    {dictionary.actions.request_more_details}
                  </button>
                  <button
                    className={styles.secondaryButton}
                    disabled={!detail.can_mark_disputed || actionBusy}
                    onClick={() => setPendingAction({ type: "mark_disputed" })}
                    type="button"
                  >
                    {dictionary.actions.mark_disputed}
                  </button>
                  {detail.candidate.dispute_status === "disputed" ? (
                    <button
                      className={styles.secondaryButton}
                      disabled={!detail.can_approve_multiple_perspectives || actionBusy}
                      onClick={() => setPendingAction({ type: "approve_multiple_perspectives" })}
                      type="button"
                    >
                      {dictionary.actions.approve_multiple_perspectives}
                    </button>
                  ) : null}
                </div>

                {pendingAction && pendingAction.type === "reject" ? (
                  <div className={styles.inlineField}>
                    <label htmlFor="rejection-reason">{dictionary.detail.rejectionReasonLabel}</label>
                    <input
                      id="rejection-reason"
                      maxLength={NOTE_MAX_LENGTH}
                      onChange={(event) => setRejectionReason(event.target.value)}
                      type="text"
                      value={rejectionReason}
                    />
                  </div>
                ) : null}
              </section>

              <section aria-label={dictionary.detail.promotionTitle} className={styles.promotionCard}>
                <h2 className={styles.sectionTitle}>{dictionary.detail.promotionTitle}</h2>
                {detail.promotion ? (
                  <>
                    <div className={styles.badgeRow}>
                      <span className={styles.badge}>
                        {dictionary.promotionStatus[detail.promotion.promotion_status]}
                      </span>
                      <span
                        className={detail.promotion.searchable_as_fact ? styles.badgeSuccess : styles.badge}
                      >
                        {detail.promotion.searchable_as_fact
                          ? dictionary.detail.availableToAvatar
                          : dictionary.detail.notYetAvailableToAvatar}
                      </span>
                    </div>
                    <p className={styles.mutedText}>
                      {dictionary.detail.promotionCreatedAt} {formatDateTime(detail.promotion.created_at, locale)}
                    </p>
                    {detail.promotion.promotion_status === "failed" ? (
                      <p className={styles.errorBanner} role="alert">
                        {dictionary.detail.promotionIndexFailed}
                      </p>
                    ) : null}
                    <button
                      className={styles.primaryButton}
                      disabled={!detail.can_index || actionBusy}
                      onClick={() => setPendingAction({ type: "index" })}
                      type="button"
                    >
                      {dictionary.actions.indexMemory}
                    </button>
                  </>
                ) : (
                  <p className={styles.mutedText}>{dictionary.detail.promotionNotYetCreated}</p>
                )}
              </section>
            </div>
          ) : null}
        </section>
      </div>

      {pendingAction ? (
        <ConfirmDialog
          candidateTitle={detail ? candidateCardTitle({
            candidate_id: detail.candidate.candidate_id,
            status: detail.candidate.status,
            workflow_version: detail.candidate.workflow_version,
            memory_type: detail.candidate.memory_type,
            enrichment_status: detail.candidate.enrichment_status,
            privacy_scope: detail.candidate.privacy_scope,
            dispute_status: detail.candidate.dispute_status,
            unresolved_clarification_count: detail.candidate.unresolved_clarification_count,
            finalized_memory_text: editableFinalizedText || detail.candidate.finalized_memory_text,
            user_message_excerpt: detail.candidate.user_message_excerpt,
            created_at: detail.candidate.created_at,
            updated_at: detail.candidate.updated_at,
            contributor_actor_id: null,
            contributor_actor_role: null,
            contributor_relationship_to_owner: null,
            promotion_id: detail.promotion?.promotion_id ?? null,
            promotion_status: detail.promotion?.promotion_status ?? null,
            searchable_as_fact: detail.promotion?.searchable_as_fact ?? false,
          }) : ""}
          dictionary={dictionary}
          onCancel={() => setPendingAction(null)}
          onConfirm={confirmPendingAction}
          pendingAction={pendingAction}
          privacyScope={privacyScope}
          promotionWillBeCreated={
            pendingAction.type !== "index" &&
            (pendingAction.type === "confirm" ||
              pendingAction.type === "edit_and_confirm" ||
              pendingAction.type === "approve_multiple_perspectives") &&
            (privacyScope === "all_family" || privacyScope === "public_legacy")
          }
        />
      ) : null}
    </main>
  );
}

function ConfirmDialog({
  pendingAction,
  candidateTitle,
  privacyScope,
  promotionWillBeCreated,
  dictionary,
  onConfirm,
  onCancel,
}: {
  pendingAction: PendingAction;
  candidateTitle: string;
  privacyScope: PrivacyScope;
  promotionWillBeCreated: boolean;
  dictionary: Dictionary;
  onConfirm: () => void;
  onCancel: () => void;
}) {
  const dialogRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    dialogRef.current?.focus();
    function onKeyDown(event: KeyboardEvent) {
      if (event.key === "Escape") {
        onCancel();
      }
    }
    document.addEventListener("keydown", onKeyDown);
    return () => document.removeEventListener("keydown", onKeyDown);
  }, [onCancel]);

  const actionLabel =
    pendingAction.type === "index" ? dictionary.actions.indexMemory : dictionary.actions[pendingAction.type];
  const privacyLabel = dictionary.privacyScope[privacyScope]?.label ?? privacyScope;

  return (
    <div className={styles.dialogOverlay}>
      <div
        aria-labelledby="confirm-dialog-title"
        aria-modal="true"
        className={styles.dialog}
        ref={dialogRef}
        role="dialog"
        tabIndex={-1}
      >
        <h2 className={styles.dialogTitle} id="confirm-dialog-title">
          {dictionary.confirmDialog.titlePrefix} {actionLabel}
        </h2>
        <p>
          {dictionary.confirmDialog.episodeLabel} {candidateTitle || dictionary.confirmDialog.untitled}
        </p>
        {pendingAction.type !== "index" ? (
          <p>
            {dictionary.confirmDialog.privacyLabel} {privacyLabel}
          </p>
        ) : null}
        {pendingAction.type !== "index" ? (
          <p>
            {promotionWillBeCreated
              ? dictionary.confirmDialog.promotionWillBeCreated
              : dictionary.confirmDialog.promotionWillNotBeCreated}
          </p>
        ) : (
          <p>{dictionary.confirmDialog.indexingExplanation}</p>
        )}
        <div className={styles.dialogActions}>
          <button className={styles.secondaryButton} onClick={onCancel} type="button">
            {dictionary.confirmDialog.cancel}
          </button>
          <button className={styles.primaryButton} onClick={onConfirm} type="button">
            {dictionary.confirmDialog.confirm}
          </button>
        </div>
      </div>
    </div>
  );
}

export default FamilyMemoryReviewPage;

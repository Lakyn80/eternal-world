"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";

import {
  ApiRequestError,
  fetchMemoryCandidateReviewDetail,
  fetchMemoryCandidateSummaries,
  submitIndexMemoryPromotion,
  submitOwnerReview,
} from "../lib/api/family-memory-review";
import type {
  ActorContext,
  ClarificationQuestionRead,
  ContributionType,
  FamilyMemoryContributionRead,
  MemoryCandidateReviewDetail,
  MemoryCandidateSummary,
  OwnerReviewAction,
  PrivacyScope,
} from "../types/family-memory";
import styles from "./family-memory-review-page.module.css";

const FINALIZED_TEXT_MAX_LENGTH = 500;
const NOTE_MAX_LENGTH = 500;

const DEMO_ACTORS: { key: string; actor: ActorContext; label: string }[] = [
  {
    key: "owner",
    actor: { actorId: "demo-owner-eva", actorRole: "owner" },
    label: "Владелец аватара (Ева)",
  },
  {
    key: "contributor",
    actor: { actorId: "family-anna", actorRole: "contributor", relationshipToOwner: "внучка" },
    label: "Внучка Анна (участник семьи)",
  },
];

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

const FILTER_OPTIONS: { value: FilterValue; label: string }[] = [
  { value: "all", label: "Все" },
  { value: "needs_review", label: "Требует проверки" },
  { value: "collecting_details", label: "Сбор деталей" },
  { value: "ready_for_owner_review", label: "Готово к проверке" },
  { value: "approved", label: "Подтверждено" },
  { value: "rejected", label: "Отклонено" },
  { value: "disputed", label: "Спорное" },
  { value: "pending_index", label: "Ожидает индексации" },
  { value: "indexed", label: "Проиндексировано" },
];

const REVIEW_STATUS_LABELS: Record<string, string> = {
  needs_review: "Требует проверки",
  approved: "Подтверждено",
  rejected: "Отклонено",
  archived: "В архиве",
};

const ENRICHMENT_STATUS_LABELS: Record<string, string> = {
  draft: "Черновик",
  collecting_details: "Сбор деталей",
  ready_for_owner_review: "Готово к проверке",
};

const DISPUTE_STATUS_LABELS: Record<string, string> = {
  none: "Без спора",
  disputed: "Спорное",
  resolved: "Спор разрешён",
};

const PROMOTION_STATUS_LABELS: Record<string, string> = {
  pending_index: "Ожидает индексации",
  indexed: "Проиндексировано",
  failed: "Ошибка индексации",
  cancelled: "Отменено",
};

const CONTRIBUTION_TYPE_LABELS: Record<ContributionType, string> = {
  initial_claim: "Первоначальный рассказ",
  clarification_answer: "Ответ на уточнение",
  owner_correction: "Правка владельца",
  owner_confirmation: "Подтверждение владельца",
  reviewer_note: "Заметка проверяющего",
  dispute_statement: "Заявление о споре",
  system_normalization: "Системная нормализация",
};

const CLARIFICATION_STATUS_LABELS: Record<string, string> = {
  pending: "Ожидает ответа",
  answered: "Отвечено",
  skipped: "Пропущено",
  cancelled: "Отменено",
};

const PRIVACY_SCOPE_OPTIONS: {
  value: PrivacyScope;
  label: string;
  indexable: boolean;
  description: string;
}[] = [
  {
    value: "private_owner",
    label: "Только владелец",
    indexable: false,
    description: "Можно подтвердить, но пока нельзя проиндексировать.",
  },
  {
    value: "selected_family",
    label: "Выбранные родственники",
    indexable: false,
    description:
      "Можно подтвердить, но индексация недоступна, пока не появится учёт прав доступа по кругу семьи.",
  },
  {
    value: "all_family",
    label: "Вся семья",
    indexable: true,
    description: "Может быть проиндексировано после подтверждения.",
  },
  {
    value: "public_legacy",
    label: "Публичное наследие",
    indexable: true,
    description: "Может быть проиндексировано после подтверждения.",
  },
];

const BLOCKED_REASON_LABELS: Record<string, string> = {
  legacy_workflow_not_supported_in_review_ui: "Это старый формат эпизода без семейной проверки.",
  actor_is_not_owner: "Только владелец аватара может выполнять это действие.",
  candidate_review_already_terminal: "Проверка этого эпизода уже завершена.",
  collecting_details: "Ожидаются ответы на уточняющие вопросы.",
  not_ready_for_review: "Эпизод ещё не готов к проверке владельцем.",
  disputed: "Есть неразрешённое расхождение во мнениях.",
  not_promoted_yet: "Эпизод ещё не подтверждён владельцем.",
  privacy_scope_not_indexable: "При текущей области приватности индексация недоступна.",
};

function blockedReasonLabel(reason: string): string {
  return BLOCKED_REASON_LABELS[reason] ?? (reason.startsWith("promotion_status_") ? "" : reason);
}

function formatDateTime(value: string | null): string {
  if (!value) {
    return "—";
  }
  try {
    return new Date(value).toLocaleString("ru-RU", {
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

const ACTION_LABELS: Record<OwnerReviewAction, string> = {
  confirm: "Подтвердить",
  edit_and_confirm: "Сохранить и подтвердить",
  reject: "Отклонить",
  request_more_details: "Запросить больше деталей",
  mark_disputed: "Отметить как спорное",
  approve_multiple_perspectives: "Подтвердить с разными точками зрения",
};

export function FamilyMemoryReviewPage() {
  const searchParams = useSearchParams();
  const deepLinkCandidateId = searchParams?.get("candidate");

  const [actorKey, setActorKey] = useState<string>("owner");
  const actor = useMemo(
    () => DEMO_ACTORS.find((item) => item.key === actorKey)?.actor ?? DEMO_ACTORS[0].actor,
    [actorKey]
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
  const actionBusyRef = useRef(false);

  const deepLinkAppliedRef = useRef(false);

  const loadSummaries = useCallback(async () => {
    setSummariesLoading(true);
    setSummariesError(null);
    try {
      const response = await fetchMemoryCandidateSummaries(null, actor);
      setSummaries(response.items);
    } catch (error) {
      setSummaries(null);
      setSummariesError(
        error instanceof ApiRequestError ? error.detail : "Не удалось загрузить список эпизодов."
      );
    } finally {
      setSummariesLoading(false);
    }
  }, [actor]);

  const loadDetail = useCallback(
    async (candidateId: number) => {
      setDetailLoading(true);
      setDetailError(null);
      try {
        const response = await fetchMemoryCandidateReviewDetail(candidateId, null, actor);
        setDetail(response);
        setEditableFinalizedText(response.candidate.finalized_memory_text ?? "");
        setPrivacyScope(
          response.enrichment?.privacy_scope ?? response.candidate.privacy_scope ?? "private_owner"
        );
        setReviewNote("");
        setRejectionReason("");
      } catch (error) {
        setDetail(null);
        setDetailError(
          error instanceof ApiRequestError ? error.detail : "Не удалось загрузить карточку эпизода."
        );
      } finally {
        setDetailLoading(false);
      }
    },
    [actor]
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
      const response = await submitOwnerReview(detail.candidate.candidate_id, payload);
      setLastResultMessage(
        response.review_status === "approved"
          ? "Эпизод подтверждён владельцем."
          : response.review_status === "rejected"
            ? "Эпизод отклонён."
            : "Статус эпизода обновлён."
      );
      await refreshAfterAction();
    } catch (error) {
      if (error instanceof ApiRequestError && error.status === 409) {
        setActionError("Состояние эпизода изменилось на сервере. Данные обновлены, проверьте текущий статус.");
        await refreshAfterAction();
      } else {
        setActionError(
          error instanceof ApiRequestError ? error.detail : "Не удалось выполнить действие. Попробуйте ещё раз."
        );
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
      const result = await submitIndexMemoryPromotion(detail.promotion.promotion_id, null, actor);
      setLastResultMessage(
        result.result === "already_indexed"
          ? "Это воспоминание уже было проиндексировано ранее."
          : "Аватар теперь может использовать это воспоминание."
      );
      await refreshAfterAction();
    } catch (error) {
      if (error instanceof ApiRequestError && error.status === 409) {
        setActionError("Состояние продвижения изменилось на сервере. Данные обновлены.");
        await refreshAfterAction();
      } else if (error instanceof ApiRequestError && error.status === 503) {
        setActionError(
          "Индексация подтверждённого воспоминания не выполнена. Повторная попытка сейчас недоступна в этом интерфейсе."
        );
      } else {
        setActionError(
          error instanceof ApiRequestError ? error.detail : "Не удалось выполнить индексацию. Попробуйте ещё раз."
        );
      }
    } finally {
      actionBusyRef.current = false;
      setActionBusy(false);
      setPendingAction(null);
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

  return (
    <main className={styles.page}>
      <header className={styles.pageHeader}>
        <div>
          <p className={styles.eyebrow}>Вечный мир</p>
          <h1 className={styles.title}>Проверка семейных воспоминаний</h1>
        </div>
        <Link className={styles.backLink} href="/fa-chat">
          Вернуться в чат
        </Link>
      </header>

      <div className={styles.demoWarning} role="note">
        Демо-режим: личность и семейная роль участника имитируются выбором ниже. Не используйте этот
        интерфейс с реальными приватными семейными данными.
      </div>

      <div className={styles.actorBar}>
        <label className={styles.actorLabel} htmlFor="demo-actor-select">
          Демо-роль участника
        </label>
        <select
          className={styles.actorSelect}
          id="demo-actor-select"
          onChange={(event) => setActorKey(event.target.value)}
          value={actorKey}
        >
          {DEMO_ACTORS.map((item) => (
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
          <span>технические детали</span>
        </label>
      </div>

      <div className={styles.layout}>
        <section aria-label="Список эпизодов на проверке" className={styles.inboxColumn}>
          <div className={styles.filterRow}>
            {FILTER_OPTIONS.map((option) => (
              <button
                aria-pressed={filterValue === option.value}
                className={`${styles.filterChip} ${filterValue === option.value ? styles.filterChipActive : ""}`}
                key={option.value}
                onClick={() => setFilterValue(option.value)}
                type="button"
              >
                {option.label}
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
                Повторить попытку
              </button>
            </div>
          ) : filteredSummaries.length === 0 ? (
            <div className={styles.emptyCard}>
              {summaries && summaries.length === 0
                ? "Пока нет эпизодов, предложенных членами семьи."
                : "Нет эпизодов с выбранным статусом."}
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
                          от {item.contributor_actor_id}
                          {item.contributor_relationship_to_owner
                            ? ` (${item.contributor_relationship_to_owner})`
                            : ""}
                        </span>
                      ) : (
                        <span>участник неизвестен</span>
                      )}
                      <span>{formatDateTime(item.updated_at)}</span>
                    </div>
                    <div className={styles.badgeRow}>
                      <span className={styles.badge}>{REVIEW_STATUS_LABELS[item.status]}</span>
                      <span className={styles.badge}>{ENRICHMENT_STATUS_LABELS[item.enrichment_status]}</span>
                      {item.dispute_status === "disputed" ? (
                        <span className={`${styles.badge} ${styles.badgeWarning}`}>Спорное</span>
                      ) : null}
                      {item.promotion_status ? (
                        <span className={styles.badge}>{PROMOTION_STATUS_LABELS[item.promotion_status]}</span>
                      ) : null}
                      {item.unresolved_clarification_count > 0 ? (
                        <span className={`${styles.badge} ${styles.badgeInfo}`}>
                          вопросов без ответа: {item.unresolved_clarification_count}
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

        <section aria-label="Карточка эпизода" className={styles.detailColumn}>
          {selectedCandidateId === null ? (
            <div className={styles.emptyCard}>Выберите эпизод слева, чтобы увидеть подробности.</div>
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
                Повторить попытку
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
                  Вы просматриваете эпизод как участник семьи. Подтверждение, отклонение и другие решения
                  доступны только владельцу аватара.
                </div>
              ) : null}

              <section className={styles.overviewCard}>
                <div className={styles.badgeRow}>
                  <span className={styles.badge}>{REVIEW_STATUS_LABELS[detail.candidate.status]}</span>
                  <span className={styles.badge}>
                    {ENRICHMENT_STATUS_LABELS[detail.candidate.enrichment_status]}
                  </span>
                  <span className={styles.badge}>{DISPUTE_STATUS_LABELS[detail.candidate.dispute_status]}</span>
                  {detail.promotion ? (
                    <span className={styles.badge}>
                      {PROMOTION_STATUS_LABELS[detail.promotion.promotion_status]}
                    </span>
                  ) : null}
                  <span className={detail.promotion?.searchable_as_fact ? styles.badgeSuccess : styles.badge}>
                    {detail.promotion?.searchable_as_fact ? "Доступно аватару" : "Пока не используется аватаром"}
                  </span>
                </div>
                <p className={styles.overviewExcerpt}>{detail.candidate.user_message_excerpt}</p>
                {debugEnabled ? (
                  <details className={styles.debugDetails}>
                    <summary>Технические данные</summary>
                    <ul>
                      <li>candidate_id: {detail.candidate.candidate_id}</li>
                      <li>promotion_id: {detail.promotion?.promotion_id ?? "—"}</li>
                      <li>target_collection_name: {detail.promotion?.target_collection_name ?? "—"}</li>
                      <li>qdrant_point_id: {detail.promotion?.qdrant_point_id ?? "—"}</li>
                    </ul>
                  </details>
                ) : null}
              </section>

              <section aria-label="История дополнений" className={styles.timelineCard}>
                <h2 className={styles.sectionTitle}>История дополнений (только для чтения)</h2>
                {detail.contributions.length === 0 ? (
                  <p className={styles.mutedText}>Пока нет записей истории.</p>
                ) : (
                  <ol className={styles.timelineList}>
                    {detail.contributions.map((item: FamilyMemoryContributionRead) => (
                      <li className={styles.timelineItem} key={item.contribution_id}>
                        <div className={styles.timelineItemHeader}>
                          <span className={styles.timelineType}>
                            {CONTRIBUTION_TYPE_LABELS[item.contribution_type]}
                          </span>
                          <span className={styles.timelineDate}>{formatDateTime(item.created_at)}</span>
                        </div>
                        <div className={styles.timelineActor}>
                          {item.actor_id}
                          {item.relationship_to_owner ? ` (${item.relationship_to_owner})` : ""}
                          {item.is_owner_correction ? " · правка владельца" : ""}
                          {item.is_disputed ? " · спорно" : ""}
                        </div>
                        <p className={styles.timelineText}>{item.contribution_text}</p>
                      </li>
                    ))}
                  </ol>
                )}
              </section>

              <section aria-label="Уточняющие вопросы" className={styles.timelineCard}>
                <h2 className={styles.sectionTitle}>Уточняющие вопросы</h2>
                {detail.clarifications.length === 0 ? (
                  <p className={styles.mutedText}>Дополнительных вопросов не задавалось.</p>
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
                            {CLARIFICATION_STATUS_LABELS[item.status]}
                            {item.required ? " · обязательный" : " · необязательный"}
                          </span>
                        </div>
                        <p className={styles.timelineText}>{item.question_text}</p>
                        {item.answered_at ? (
                          <p className={styles.mutedText}>Отвечено {formatDateTime(item.answered_at)}</p>
                        ) : null}
                      </li>
                    ))}
                  </ul>
                )}
              </section>

              {detail.candidate.dispute_status === "disputed" ? (
                <section aria-label="Разные точки зрения" className={styles.disputeCard}>
                  <h2 className={styles.sectionTitle}>Разные точки зрения</h2>
                  <p className={styles.disputeWarning}>
                    Это воспоминание содержит разные приписанные точки зрения. Подтверждение сохраняет
                    расхождение, а не выбирает одну версию как достоверную.
                  </p>
                  <ul className={styles.timelineList}>
                    {detail.contributions
                      .filter((item) => item.is_disputed || item.contribution_type === "owner_correction")
                      .map((item) => (
                        <li className={styles.timelineItem} key={`perspective-${item.contribution_id}`}>
                          <div className={styles.timelineActor}>
                            {item.actor_role === "owner" ? "Точка зрения владельца" : "Точка зрения участника семьи"}
                          </div>
                          <p className={styles.timelineText}>{item.contribution_text}</p>
                        </li>
                      ))}
                  </ul>
                </section>
              ) : null}

              <section aria-label="Итоговый текст воспоминания" className={styles.editorCard}>
                <h2 className={styles.sectionTitle}>Итоговый текст воспоминания</h2>
                <label className={styles.visuallyHidden} htmlFor="finalized-memory-text">
                  Итоговый текст воспоминания
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
                      Вернуть исходный текст
                    </button>
                  ) : null}
                </div>
                {isTextEdited ? (
                  <p className={styles.mutedText}>
                    Текст отличается от сохранённого на сервере варианта. Изменение будет сохранено как
                    отдельная правка владельца в истории.
                  </p>
                ) : null}
              </section>

              <section aria-label="Область приватности" className={styles.privacyCard}>
                <h2 className={styles.sectionTitle}>Область приватности</h2>
                <div className={styles.privacyOptions} role="radiogroup" aria-label="Область приватности">
                  {PRIVACY_SCOPE_OPTIONS.map((option) => (
                    <label className={styles.privacyOption} key={option.value}>
                      <input
                        checked={privacyScope === option.value}
                        disabled={!isOwnerSelected}
                        name="privacy-scope"
                        onChange={() => setPrivacyScope(option.value)}
                        type="radio"
                        value={option.value}
                      />
                      <span>
                        <strong>{option.label}</strong>
                        <br />
                        <span className={styles.mutedText}>{option.description}</span>
                      </span>
                    </label>
                  ))}
                </div>
              </section>

              <section aria-label="Действия владельца" className={styles.actionsCard}>
                <h2 className={styles.sectionTitle}>Действия владельца</h2>
                <label className={styles.visuallyHidden} htmlFor="review-note">
                  Заметка проверяющего
                </label>
                <textarea
                  className={styles.noteTextarea}
                  disabled={!isOwnerSelected}
                  id="review-note"
                  maxLength={NOTE_MAX_LENGTH}
                  onChange={(event) => setReviewNote(event.target.value)}
                  placeholder="Необязательная заметка к решению..."
                  rows={2}
                  value={reviewNote}
                />

                {!detail.is_owner_actor && detail.blocked_reasons.includes("actor_is_not_owner") ? (
                  <p className={styles.mutedText}>
                    Переключитесь на демо-роль владельца выше, чтобы выполнять действия проверки.
                  </p>
                ) : null}

                {detail.blocked_reasons
                  .filter((reason) => reason !== "actor_is_not_owner" && blockedReasonLabel(reason))
                  .map((reason) => (
                    <p className={styles.blockedReason} key={reason}>
                      {blockedReasonLabel(reason)}
                    </p>
                  ))}

                <div className={styles.actionButtonRow}>
                  <button
                    className={styles.primaryButton}
                    disabled={!primaryConfirmAllowed || actionBusy}
                    onClick={() => setPendingAction({ type: primaryConfirmAction })}
                    type="button"
                  >
                    {ACTION_LABELS[primaryConfirmAction]}
                  </button>
                  <button
                    className={styles.secondaryButton}
                    disabled={!detail.can_reject || actionBusy}
                    onClick={() => setPendingAction({ type: "reject" })}
                    type="button"
                  >
                    Отклонить
                  </button>
                  <button
                    className={styles.secondaryButton}
                    disabled={!detail.can_request_more_details || actionBusy}
                    onClick={() => setPendingAction({ type: "request_more_details" })}
                    type="button"
                  >
                    Запросить больше деталей
                  </button>
                  <button
                    className={styles.secondaryButton}
                    disabled={!detail.can_mark_disputed || actionBusy}
                    onClick={() => setPendingAction({ type: "mark_disputed" })}
                    type="button"
                  >
                    Отметить как спорное
                  </button>
                  {detail.candidate.dispute_status === "disputed" ? (
                    <button
                      className={styles.secondaryButton}
                      disabled={!detail.can_approve_multiple_perspectives || actionBusy}
                      onClick={() => setPendingAction({ type: "approve_multiple_perspectives" })}
                      type="button"
                    >
                      Подтвердить с разными точками зрения
                    </button>
                  ) : null}
                </div>

                {pendingAction && pendingAction.type === "reject" ? (
                  <div className={styles.inlineField}>
                    <label htmlFor="rejection-reason">Причина отклонения (необязательно)</label>
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

              <section aria-label="Продвижение и индексация" className={styles.promotionCard}>
                <h2 className={styles.sectionTitle}>Продвижение и индексация</h2>
                {detail.promotion ? (
                  <>
                    <div className={styles.badgeRow}>
                      <span className={styles.badge}>
                        {PROMOTION_STATUS_LABELS[detail.promotion.promotion_status]}
                      </span>
                      <span
                        className={detail.promotion.searchable_as_fact ? styles.badgeSuccess : styles.badge}
                      >
                        {detail.promotion.searchable_as_fact ? "Доступно аватару" : "Пока недоступно аватару"}
                      </span>
                    </div>
                    <p className={styles.mutedText}>Создано {formatDateTime(detail.promotion.created_at)}</p>
                    {detail.promotion.promotion_status === "failed" ? (
                      <p className={styles.errorBanner} role="alert">
                        Индексация подтверждённого воспоминания не выполнена. Повторная попытка сейчас
                        недоступна в этом интерфейсе.
                      </p>
                    ) : null}
                    <button
                      className={styles.primaryButton}
                      disabled={!detail.can_index || actionBusy}
                      onClick={() => setPendingAction({ type: "index" })}
                      type="button"
                    >
                      Индексировать воспоминание
                    </button>
                  </>
                ) : (
                  <p className={styles.mutedText}>
                    Продвижение появится после подтверждения владельцем с областью приватности, доступной
                    для индексации.
                  </p>
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
  onConfirm,
  onCancel,
}: {
  pendingAction: PendingAction;
  candidateTitle: string;
  privacyScope: PrivacyScope;
  promotionWillBeCreated: boolean;
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
    pendingAction.type === "index" ? "Индексировать воспоминание" : ACTION_LABELS[pendingAction.type];
  const privacyLabel = PRIVACY_SCOPE_OPTIONS.find((option) => option.value === privacyScope)?.label ?? privacyScope;

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
          Подтвердите действие: {actionLabel}
        </h2>
        <p>Эпизод: {candidateTitle || "без названия"}</p>
        {pendingAction.type !== "index" ? <p>Область приватности: {privacyLabel}</p> : null}
        {pendingAction.type !== "index" ? (
          <p>
            {promotionWillBeCreated
              ? "Будет создано продвижение воспоминания, ожидающее явной индексации."
              : "Продвижение не будет создано автоматически при текущей области приватности."}
          </p>
        ) : (
          <p>Индексация сделает воспоминание доступным аватару для использования в ответах.</p>
        )}
        <div className={styles.dialogActions}>
          <button className={styles.secondaryButton} onClick={onCancel} type="button">
            Отмена
          </button>
          <button className={styles.primaryButton} onClick={onConfirm} type="button">
            Подтвердить
          </button>
        </div>
      </div>
    </div>
  );
}

export default FamilyMemoryReviewPage;

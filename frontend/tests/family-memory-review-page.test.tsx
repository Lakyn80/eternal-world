import React, { act } from "react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { createRoot, Root } from "react-dom/client";

vi.mock("next/navigation", () => ({
  useSearchParams: () => new URLSearchParams(),
}));

import { FamilyMemoryReviewPage } from "../components/family-memory-review-page";
import type {
  MemoryCandidateReviewDetail,
  MemoryCandidateSummary,
  MemoryCandidateSummaryListResponse,
} from "../types/family-memory";

(globalThis as typeof globalThis & { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

type RenderHandle = {
  container: HTMLDivElement;
  root: Root;
  unmount: () => void;
};

function renderComponent(): RenderHandle {
  const container = document.createElement("div");
  document.body.appendChild(container);
  const root = createRoot(container);
  act(() => {
    root.render(<FamilyMemoryReviewPage />);
  });
  return {
    container,
    root,
    unmount: () => {
      act(() => {
        root.unmount();
      });
      container.remove();
    },
  };
}

function jsonResponse(body: unknown, status = 200): Response {
  return {
    ok: status >= 200 && status < 300,
    status,
    json: async () => body,
  } as Response;
}

function buildSummary(overrides: Partial<MemoryCandidateSummary> = {}): MemoryCandidateSummary {
  return {
    candidate_id: 1,
    status: "needs_review",
    workflow_version: 2,
    memory_type: "bedtime_song",
    enrichment_status: "collecting_details",
    privacy_scope: "private_owner",
    dispute_status: "none",
    unresolved_clarification_count: 1,
    finalized_memory_text: null,
    user_message_excerpt: "Бабушка пела мне колыбельную перед сном.",
    created_at: "2026-07-01T10:00:00Z",
    updated_at: "2026-07-01T10:00:00Z",
    contributor_actor_id: "family-anna",
    contributor_actor_role: "contributor",
    contributor_relationship_to_owner: "внучка",
    promotion_id: null,
    promotion_status: null,
    searchable_as_fact: false,
    ...overrides,
  };
}

function buildDetail(overrides: Partial<MemoryCandidateReviewDetail> = {}): MemoryCandidateReviewDetail {
  return {
    candidate: {
      candidate_id: 1,
      owner_user_id: 1,
      avatar_id: "eva_novakova_demo",
      profile_id: 1,
      conversation_id: null,
      trace_id: null,
      source: "conversation",
      status: "needs_review",
      confidence: "unverified",
      user_message_excerpt: "Бабушка пела мне колыбельную перед сном.",
      proposed_memory_text: "Бабушка пела колыбельную перед сном.",
      reason: "A family member introduced a possible personal memory.",
      language: "ru",
      created_at: "2026-07-01T10:00:00Z",
      updated_at: "2026-07-01T10:00:00Z",
      reviewed_at: null,
      reviewed_by: null,
      review_note: null,
      rejection_reason: null,
      memory_type: "bedtime_song",
      enrichment_status: "ready_for_owner_review",
      finalized_memory_text: "Бабушка пела «Спи, моя радость, усни» дома в детской комнате.",
      privacy_scope: "private_owner",
      dispute_status: "none",
      finalized_at: "2026-07-01T10:05:00Z",
      finalized_by: "system:deterministic-finalizer",
      owner_reviewed_at: null,
      owner_reviewed_by: null,
      owner_review_actor_role: null,
      unresolved_clarification_count: 0,
      version: 4,
      workflow_version: 2,
    },
    enrichment: {
      candidate_id: 1,
      avatar_id: "eva_novakova_demo",
      profile_id: 1,
      memory_type: "bedtime_song",
      enrichment_status: "ready_for_owner_review",
      review_status: "needs_review",
      dispute_status: "none",
      privacy_scope: "private_owner",
      unresolved_clarification_count: 0,
      finalized_memory_text: "Бабушка пела «Спи, моя радость, усни» дома в детской комнате.",
      finalized_at: "2026-07-01T10:05:00Z",
      finalized_by: "system:deterministic-finalizer",
      owner_reviewed_at: null,
      owner_reviewed_by: null,
      contribution_count: 4,
      next_clarification_question: null,
      promotion_id: null,
      promotion_status: null,
      searchable_as_fact: false,
      explicit_indexing_required: false,
    },
    contributions: [
      {
        contribution_id: 1,
        candidate_id: 1,
        avatar_id: "eva_novakova_demo",
        profile_id: 1,
        actor_id: "family-anna",
        actor_role: "contributor",
        relationship_to_owner: "внучка",
        contribution_type: "initial_claim",
        contribution_text: "Бабушка пела мне колыбельную перед сном.",
        structured_details: null,
        language: "ru",
        source_message_hash: null,
        trace_id: null,
        supersedes_contribution_id: null,
        is_owner_correction: false,
        is_disputed: false,
        privacy_scope_snapshot: "private_owner",
        created_at: "2026-07-01T10:00:00Z",
      },
    ],
    clarifications: [
      {
        clarification_id: 1,
        candidate_id: 1,
        question_key: "song_title",
        question_text: "Какую песню пела бабушка?",
        language: "ru",
        status: "answered",
        required: true,
        asked_at: "2026-07-01T10:00:00Z",
        answered_at: "2026-07-01T10:01:00Z",
        answered_by: "family-anna",
        answer_contribution_id: 2,
      },
    ],
    promotion: null,
    is_owner_actor: true,
    can_confirm: true,
    can_edit_and_confirm: true,
    can_reject: true,
    can_request_more_details: true,
    can_mark_disputed: true,
    can_approve_multiple_perspectives: false,
    can_index: false,
    blocked_reasons: ["not_promoted_yet", "privacy_scope_not_indexable"],
    ...overrides,
  };
}

function routeFetch(handlers: Array<{
  test: (url: string, init?: RequestInit) => boolean;
  respond: (url: string, init?: RequestInit) => Response | Promise<Response>;
}>) {
  return vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
    const url = typeof input === "string" ? input : input.toString();
    const handler = handlers.find((item) => item.test(url, init));
    if (!handler) {
      throw new Error(`Unhandled fetch in test: ${url}`);
    }
    return handler.respond(url, init);
  });
}

afterEach(() => {
  document.body.innerHTML = "";
  vi.restoreAllMocks();
});

describe("family memory review inbox", () => {
  it("shows a loading skeleton then renders candidate cards", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    vi.stubGlobal(
      "fetch",
      routeFetch([{ test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) }])
    );

    const view = renderComponent();
    expect(view.container.querySelector('[data-testid="inbox-loading"]')).not.toBeNull();

    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(view.container.textContent).toContain("Бабушка пела мне колыбельную перед сном.");
    expect(view.container.textContent).toContain("Демо-режим");
    view.unmount();
  });

  it("shows an empty inbox message when there are no candidates", async () => {
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse({ items: [], total: 0 }) },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(view.container.textContent).toContain("Пока нет эпизодов");
    view.unmount();
  });

  it("shows a safe retry banner when the inbox request fails, without raw payloads", async () => {
    vi.stubGlobal(
      "fetch",
      routeFetch([
        {
          test: (url) => url.includes("/review-summary"),
          respond: () => jsonResponse({ detail: "Тестовый профиль аватара сейчас недоступен." }, 404),
        },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(view.container.textContent).toContain("Тестовый профиль аватара сейчас недоступен.");
    expect(view.container.textContent).not.toContain("Traceback");
    expect(view.container.querySelector("button")?.textContent).toBeTruthy();
    view.unmount();
  });

  it("filters the candidate list by status", async () => {
    const summaries: MemoryCandidateSummaryListResponse = {
      items: [
        buildSummary({ candidate_id: 1, status: "needs_review", user_message_excerpt: "Первый эпизод" }),
        buildSummary({ candidate_id: 2, status: "rejected", user_message_excerpt: "Второй эпизод" }),
      ],
      total: 2,
    };
    vi.stubGlobal(
      "fetch",
      routeFetch([{ test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) }])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(view.container.textContent).toContain("Первый эпизод");
    expect(view.container.textContent).toContain("Второй эпизод");

    const rejectedChip = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Отклонено"
    );
    expect(rejectedChip).toBeTruthy();
    await act(async () => {
      rejectedChip?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    expect(view.container.textContent).not.toContain("Первый эпизод");
    expect(view.container.textContent).toContain("Второй эпизод");
    view.unmount();
  });
});

describe("family memory review candidate detail", () => {
  it("renders contribution history, clarifications, finalized text, privacy scope", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail();
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("button.candidateCard, [class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(view.container.textContent).toContain("Первоначальный рассказ");
    expect(view.container.textContent).toContain("Какую песню пела бабушка?");
    expect(view.container.textContent).toContain("Спи, моя радость, усни");
    expect(view.container.textContent).toContain("Только владелец");
    expect(view.container.textContent).toContain("Пока недоступно аватару".slice(0, 5));
    view.unmount();
  });

  it("shows the multiple-perspectives warning only for disputed candidates and keeps the action separate", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail({
      candidate: {
        ...buildDetail().candidate,
        dispute_status: "disputed",
      },
      can_confirm: false,
      can_approve_multiple_perspectives: true,
      blocked_reasons: ["disputed", "not_promoted_yet", "privacy_scope_not_indexable"],
    });
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(view.container.textContent).toContain("Разные точки зрения");
    expect(view.container.textContent).toContain("сохраняет");
    const confirmButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Подтвердить"
    );
    expect(confirmButton?.hasAttribute("disabled")).toBe(true);
    const perspectivesButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Подтвердить с разными точками зрения"
    );
    expect(perspectivesButton?.hasAttribute("disabled")).toBe(false);
    view.unmount();
  });
});

describe("family memory review authorization", () => {
  it("hides active owner actions for a contributor actor and shows the demo warning", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const ownerDetail = buildDetail();
    const contributorDetail = buildDetail({
      is_owner_actor: false,
      can_confirm: false,
      can_edit_and_confirm: false,
      can_reject: false,
      can_request_more_details: false,
      can_mark_disputed: false,
      can_approve_multiple_perspectives: false,
      can_index: false,
      blocked_reasons: ["actor_is_not_owner"],
    });
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        {
          test: (url) => url.includes("/review-detail") && url.includes("family-anna"),
          respond: () => jsonResponse(contributorDetail),
        },
        {
          test: (url) => url.includes("/review-detail"),
          respond: () => jsonResponse(ownerDetail),
        },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const actorSelect = view.container.querySelector("#demo-actor-select") as HTMLSelectElement;
    await act(async () => {
      actorSelect.value = "contributor";
      actorSelect.dispatchEvent(new Event("change", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const confirmButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Подтвердить"
    );
    expect(confirmButton?.hasAttribute("disabled")).toBe(true);
    expect(view.container.textContent).toContain("только владельцу аватара");
    expect(view.container.textContent).toContain("Демо-режим");
    view.unmount();
  });
});

describe("family memory review owner actions", () => {
  it("sends the correct edit_and_confirm payload after confirmation", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail();
    let postedBody: Record<string, unknown> | null = null;
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
        {
          test: (url, init) => url.includes("/owner-review") && init?.method === "POST",
          respond: (_url, init) => {
            postedBody = JSON.parse(String(init?.body));
            return jsonResponse({
              ...detail.enrichment,
              review_status: "approved",
              promotion_created: true,
              promotion_id: 9,
              promotion_status: "pending_index",
              searchable_as_fact: false,
            });
          },
        },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const textarea = view.container.querySelector("#finalized-memory-text") as HTMLTextAreaElement;
    const nativeTextareaValueSetter = Object.getOwnPropertyDescriptor(
      window.HTMLTextAreaElement.prototype,
      "value"
    )!.set!;
    await act(async () => {
      nativeTextareaValueSetter.call(textarea, "Бабушка пела «Спи, моя радость, усни» летом у реки.");
      textarea.dispatchEvent(new Event("input", { bubbles: true }));
    });

    const primaryButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Сохранить и подтвердить"
    );
    expect(primaryButton).toBeTruthy();
    await act(async () => {
      primaryButton?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    // A confirmation dialog must appear before the request is sent (Part G.16).
    expect(view.container.querySelector('[role="dialog"]')).not.toBeNull();
    expect(postedBody).toBeNull();

    const dialogConfirm = Array.from(
      view.container.querySelector('[role="dialog"]')!.querySelectorAll("button")
    ).find((button) => button.textContent === "Подтвердить");
    await act(async () => {
      dialogConfirm?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(postedBody).not.toBeNull();
    expect(postedBody!.action).toBe("edit_and_confirm");
    expect(postedBody!.finalized_memory_text).toBe("Бабушка пела «Спи, моя радость, усни» летом у реки.");
    expect(postedBody!.actor_id).toBe("demo-owner-eva");
    view.unmount();
  });

  it("requires confirmation before rejecting a candidate", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail();
    let rejectCalled = false;
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
        {
          test: (url, init) => url.includes("/owner-review") && init?.method === "POST",
          respond: () => {
            rejectCalled = true;
            return jsonResponse({ ...detail.enrichment, review_status: "rejected", promotion_created: false });
          },
        },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const rejectButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Отклонить"
    );
    await act(async () => {
      rejectButton?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    expect(rejectCalled).toBe(false);
    expect(view.container.querySelector('[role="dialog"]')).not.toBeNull();
    view.unmount();
  });

  it("refreshes candidate state instead of showing a raw error on a 409 conflict", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail();
    let reviewAttempts = 0;
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
        {
          test: (url, init) => url.includes("/owner-review") && init?.method === "POST",
          respond: () => {
            reviewAttempts += 1;
            return jsonResponse(
              { detail: "Family memory action is not allowed in the current state" },
              409
            );
          },
        },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const primaryButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Подтвердить"
    );
    await act(async () => {
      primaryButton?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });
    const dialogConfirm = Array.from(
      view.container.querySelector('[role="dialog"]')!.querySelectorAll("button")
    ).find((button) => button.textContent === "Подтвердить");
    await act(async () => {
      dialogConfirm?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(reviewAttempts).toBe(1);
    expect(view.container.textContent).toContain("изменилось на сервере");
    expect(view.container.textContent).not.toContain("Traceback");
    view.unmount();
  });
});

describe("family memory review indexing", () => {
  it("only shows the index button when eligible and treats already_indexed as success", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail({
      promotion: {
        promotion_id: 9,
        candidate_id: 1,
        owner_user_id: 1,
        avatar_id: "eva_novakova_demo",
        profile_id: 1,
        source_type: "conversation_candidate",
        promotion_status: "pending_index",
        approved_memory_text: "Бабушка пела «Спи, моя радость, усни» дома в детской комнате.",
        normalized_memory_text: "Бабушка пела «Спи, моя радость, усни» дома в детской комнате.",
        language: "ru",
        searchable_as_fact: false,
        created_at: "2026-07-01T11:00:00Z",
        updated_at: "2026-07-01T11:00:00Z",
        indexed_at: null,
        failed_at: null,
        cancelled_at: null,
        failure_reason: null,
        target_collection_name: "demo-memory",
        qdrant_point_id: null,
        indexing_attempt_count: 0,
        trace_id: null,
        source_candidate_status_snapshot: "approved",
        review_note_snapshot: null,
      },
      can_index: true,
      can_confirm: false,
      can_edit_and_confirm: false,
      blocked_reasons: [],
    });
    let indexCalls = 0;
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
        {
          test: (url, init) => url.includes("/index") && init?.method === "POST",
          respond: () => {
            indexCalls += 1;
            return jsonResponse({
              promotion_id: 9,
              promotion_status: "indexed",
              indexed_at: "2026-07-01T12:00:00Z",
              target_collection_name: "demo-memory",
              qdrant_point_id: "point-9",
              searchable_as_fact: true,
              result: indexCalls === 1 ? "indexed" : "already_indexed",
            });
          },
        },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const indexButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Индексировать воспоминание"
    );
    expect(indexButton).toBeTruthy();
    expect(indexButton?.hasAttribute("disabled")).toBe(false);

    await act(async () => {
      indexButton?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });
    const dialogConfirm = Array.from(
      view.container.querySelector('[role="dialog"]')!.querySelectorAll("button")
    ).find((button) => button.textContent === "Подтвердить");
    await act(async () => {
      dialogConfirm?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(indexCalls).toBe(1);
    expect(view.container.textContent).toContain("теперь может использовать");
    view.unmount();
  });

  it("hides the index button when the promotion is not yet eligible", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail();
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const indexButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Индексировать воспоминание"
    );
    expect(indexButton).toBeUndefined();
    expect(view.container.textContent).toContain("Продвижение появится после подтверждения");
    view.unmount();
  });
});

describe("family memory review privacy scope", () => {
  it("explains that private_owner and selected_family block indexing without changing backend rules", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail();
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    expect(view.container.textContent).toContain("нельзя проиндексировать");
    expect(view.container.textContent).toContain("индексация недоступна");
    expect(view.container.textContent).toContain("Может быть проиндексировано после подтверждения.");
    view.unmount();
  });
});

describe("family memory review accessibility", () => {
  it("renders the confirmation dialog with an accessible role and label", async () => {
    const summaries: MemoryCandidateSummaryListResponse = { items: [buildSummary()], total: 1 };
    const detail = buildDetail();
    vi.stubGlobal(
      "fetch",
      routeFetch([
        { test: (url) => url.includes("/review-summary"), respond: () => jsonResponse(summaries) },
        { test: (url) => url.includes("/review-detail"), respond: () => jsonResponse(detail) },
      ])
    );

    const view = renderComponent();
    await act(async () => {
      await Promise.resolve();
      await Promise.resolve();
    });
    const card = view.container.querySelector("[class*='candidateCard']") as HTMLElement;
    await act(async () => {
      card.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      await Promise.resolve();
      await Promise.resolve();
    });

    const primaryButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Подтвердить"
    );
    await act(async () => {
      primaryButton?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    const dialog = view.container.querySelector('[role="dialog"]');
    expect(dialog).not.toBeNull();
    expect(dialog?.getAttribute("aria-modal")).toBe("true");
    expect(dialog?.getAttribute("aria-labelledby")).toBe("confirm-dialog-title");
    expect(view.container.querySelector("#confirm-dialog-title")).not.toBeNull();

    const finalizedLabel = view.container.querySelector('label[for="finalized-memory-text"]');
    expect(finalizedLabel).not.toBeNull();
    view.unmount();
  });
});

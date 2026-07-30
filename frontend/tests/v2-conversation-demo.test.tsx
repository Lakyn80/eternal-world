import React, { act } from "react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { createRoot, Root } from "react-dom/client";

import V2ConversationDemo from "../components/v2-experience/v2-conversation-demo";
import { getV2ExperienceContent } from "../lib/v2-experience/content";
import type { AppLocale } from "../lib/i18n/locales";

type RenderHandle = {
  container: HTMLDivElement;
  root: Root;
  unmount: () => void;
};

(globalThis as typeof globalThis & { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

function renderComponent(locale: AppLocale): RenderHandle {
  const container = document.createElement("div");
  document.body.appendChild(container);
  const root = createRoot(container);

  act(() => {
    root.render(<V2ConversationDemo content={getV2ExperienceContent(locale).conversation} locale={locale} />);
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

afterEach(() => {
  document.body.innerHTML = "";
  vi.restoreAllMocks();
});

describe("v2 conversation demo", () => {
  it("renders the Czech shell and sends locale=cs to the backend", async () => {
    const fetchMock = vi.fn(async (_input: RequestInfo | URL, init?: RequestInit) => ({
      ok: true,
      json: async () => ({
        answer: "Vyrůstala jsem v Brně.",
        trace_id: "v2-cs-trace",
        lack_of_evidence: false,
        evidence: [
          {
            chunk_id: "chunk-1",
            source_id: 21,
            source_title: null,
            score: 0.92,
            text_preview: "Krátký důkazní úryvek.",
          },
        ],
        memory_candidate: null,
      }),
    })) as unknown as ReturnType<typeof vi.fn>;
    vi.stubGlobal("fetch", fetchMock);

    const view = renderComponent("cs");

    expect(view.container.textContent).toContain("Stejný backend, jiný frontend obal");
    expect(view.container.querySelector("input")?.getAttribute("placeholder")).toBe(
      "Napište Evě otázku nebo vřelou zprávu..."
    );
    expect(view.container.textContent).toContain("Odeslat");

    const suggestionButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Kde jsi žila v dětství?"
    );
    if (!suggestionButton) {
      throw new Error("Suggestion button not found");
    }

    await act(async () => {
      suggestionButton.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    expect(fetchMock).toHaveBeenCalledTimes(1);
    const requestBody = JSON.parse(String(fetchMock.mock.calls[0]?.[1]?.body));
    expect(requestBody.locale).toBe("cs");
    expect(requestBody.message).toBe("Kde jsi žila v dětství?");

    expect(view.container.textContent).toContain("Vyrůstala jsem v Brně.");
    expect(view.container.textContent).toContain("trace_id: v2-cs-trace");
    expect(view.container.textContent).toContain("Zdroj #21");

    view.unmount();
  });

  it("shows backend detail when the request fails", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async () => ({
        ok: false,
        json: async () => ({
          detail: "Демо временно недоступно: индекс памяти ещё не готов.",
        }),
      }))
    );

    const view = renderComponent("ru");
    const suggestionButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Где ты жила в детстве?"
    );
    if (!suggestionButton) {
      throw new Error("Suggestion button not found");
    }

    await act(async () => {
      suggestionButton.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    expect(view.container.textContent).toContain("Демо временно недоступно: индекс памяти ещё не готов.");

    view.unmount();
  });

  it("shows the localized invalid-response error when the payload is malformed", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async () => ({
        ok: true,
        json: async () => ({
          wrong: true,
        }),
      }))
    );

    const view = renderComponent("en");
    const suggestionButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Where did you live as a child?"
    );
    if (!suggestionButton) {
      throw new Error("Suggestion button not found");
    }

    await act(async () => {
      suggestionButton.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    expect(view.container.textContent).toContain(
      "The server returned an invalid response. Check the backend contract."
    );

    view.unmount();
  });
});

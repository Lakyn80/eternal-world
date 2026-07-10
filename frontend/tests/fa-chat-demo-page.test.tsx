import React, { act } from "react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { createRoot, Root } from "react-dom/client";

import { FaChatDemoPage } from "../components/fa-chat-demo-page";


type RenderHandle = {
  container: HTMLDivElement;
  root: Root;
  unmount: () => void;
};

(globalThis as typeof globalThis & { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;


function renderComponent(): RenderHandle {
  const container = document.createElement("div");
  document.body.appendChild(container);
  const root = createRoot(container);
  act(() => {
    root.render(<FaChatDemoPage />);
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


describe("fa chat demo page", () => {
  it("renders Russian title, input and send button", () => {
    const view = renderComponent();

    expect(view.container.textContent).toContain("Тестовый чат с цифровым аватаром");
    expect(view.container.querySelector("textarea")?.getAttribute("placeholder")).toBe(
      "Напишите Еве вопрос или тёплое сообщение..."
    );
    expect(view.container.textContent).toContain("Отправить");

    view.unmount();
  });

  it("calls backend, shows loading state and displays answer", async () => {
    let resolveFetch: ((value: Response) => void) | null = null;
    const fetchPromise = new Promise<Response>((resolve) => {
      resolveFetch = resolve;
    });
    const fetchMock = vi.fn(() => fetchPromise);
    vi.stubGlobal("fetch", fetchMock);

    const view = renderComponent();
    const form = view.container.querySelector("form");
    const exampleButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Где ты жила в детстве?"
    );
    if (!form || !exampleButton) {
      throw new Error("Required form controls are missing");
    }

    await act(async () => {
      exampleButton.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    await act(async () => {
      form.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
    });

    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(String(fetchMock.mock.calls[0]?.[0])).toContain("/api/demo/fa-chat/message");
    expect(view.container.textContent).toContain("Ева подбирает ответ...");

    await act(async () => {
      resolveFetch?.({
        ok: true,
        json: async () => ({
          answer: "В детстве я жила с родителями в домике у Попице. [rag:27618]",
          lack_of_evidence: false,
          retrieval_used: true,
          persona_applied: true,
          guard_applied: false,
          guard_reason: null,
          trace_id: "demo-trace-frontend",
          memory_candidate: null,
          emotion: {
            primary: "warm_nostalgic",
            intensity: 0.61,
          },
          face_directives: {
            expression: "gentle_smile",
            gaze: "soft",
            head_motion: "small_nod",
          },
          voice_directives: {
            tone: "warm",
            pace: "slow",
            volume: "normal",
          },
          evidence: [],
        }),
      } as Response);
      await fetchPromise;
    });

    expect(view.container.textContent).toContain("В детстве я жила с родителями в домике у Попице. [rag:27618]");
    expect(view.container.textContent).toContain("trace_id: demo-trace-frontend");
    expect(view.container.textContent).toContain("persona: on");

    view.unmount();
  });

  it("shows backend Russian detail when backend request fails", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async () => {
        return {
          ok: false,
          json: async () => ({
            detail: "Демо временно недоступно: модель эмбеддингов BGE-M3 не инициализирована.",
          }),
        } as Response;
      })
    );

    const view = renderComponent();
    const form = view.container.querySelector("form");
    const exampleButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Ты помнишь, как пела мне песню перед сном?"
    );
    if (!form || !exampleButton) {
      throw new Error("Required form controls are missing");
    }

    await act(async () => {
      exampleButton.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    await act(async () => {
      form.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
    });

    expect(view.container.textContent).toContain(
      "Демо временно недоступно: модель эмбеддингов BGE-M3 не инициализирована."
    );

    view.unmount();
  });
});

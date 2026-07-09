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
      "Напишите вопрос аватару..."
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
      (button) => button.textContent === "Где Павел жил в детстве?"
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
    expect(view.container.textContent).toContain("Аватар думает...");

    await act(async () => {
      resolveFetch?.({
        ok: true,
        json: async () => ({
          answer: "Павел в детстве жил у Попице. [rag:27618]",
          lack_of_evidence: false,
          retrieval_used: true,
          guard_applied: false,
          guard_reason: null,
          trace_id: "demo-trace-frontend",
          evidence: [],
        }),
      } as Response);
      await fetchPromise;
    });

    expect(view.container.textContent).toContain("Павел в детстве жил у Попице. [rag:27618]");
    expect(view.container.textContent).toContain("trace_id: demo-trace-frontend");

    view.unmount();
  });

  it("shows a Russian error message when backend request fails", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async () => {
        throw new Error("network");
      })
    );

    const view = renderComponent();
    const form = view.container.querySelector("form");
    const exampleButton = Array.from(view.container.querySelectorAll("button")).find(
      (button) => button.textContent === "Что известно о доме в Ржечковицах?"
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

    expect(view.container.textContent).toContain("Не удалось получить ответ. Попробуйте ещё раз.");

    view.unmount();
  });
});

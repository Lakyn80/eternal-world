"use client";

import { FormEvent, useMemo, useState } from "react";


type DemoEvidenceItem = {
  chunk_id: string;
  source_id: number | null;
  source_title: string | null;
  score: number | null;
  text_preview: string | null;
};

type DemoFaChatResponse = {
  answer: string;
  lack_of_evidence: boolean;
  retrieval_used: boolean;
  guard_applied: boolean;
  guard_reason: string | null;
  trace_id: string;
  evidence: DemoEvidenceItem[];
};

type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  text: string;
  traceId?: string;
  lackOfEvidence?: boolean;
  retrievalUsed?: boolean;
  guardApplied?: boolean;
  guardReason?: string | null;
  evidence: DemoEvidenceItem[];
};

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8033";
const EXAMPLE_QUESTIONS = [
  "Где Павел жил в детстве?",
  "Кто подписал строительный план дома?",
  "Что известно о доме в Ржечковицах?",
];

function buildApiUrl(path: string): string {
  return `${API_BASE_URL.replace(/\/$/, "")}${path}`;
}

export function FaChatDemoPage() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [debugEnabled, setDebugEnabled] = useState(false);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const emptyStateVisible = useMemo(() => messages.length === 0, [messages.length]);

  async function sendMessage(messageText: string) {
    const trimmedMessage = messageText.trim();
    if (!trimmedMessage || loading) {
      return;
    }

    setErrorMessage(null);
    setLoading(true);
    setMessages((currentMessages) => [
      ...currentMessages,
      {
        id: `user-${Date.now()}`,
        role: "user",
        text: trimmedMessage,
        evidence: [],
      },
    ]);
    setInputValue("");

    try {
      const response = await fetch(buildApiUrl("/api/demo/fa-chat/message"), {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: trimmedMessage,
          debug: debugEnabled,
        }),
      });
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const payload = (await response.json()) as DemoFaChatResponse;
      setMessages((currentMessages) => [
        ...currentMessages,
        {
          id: `assistant-${payload.trace_id}`,
          role: "assistant",
          text: payload.answer,
          traceId: payload.trace_id,
          lackOfEvidence: payload.lack_of_evidence,
          retrievalUsed: payload.retrieval_used,
          guardApplied: payload.guard_applied,
          guardReason: payload.guard_reason,
          evidence: payload.evidence,
        },
      ]);
    } catch (_error) {
      setErrorMessage("Не удалось получить ответ. Попробуйте ещё раз.");
    } finally {
      setLoading(false);
    }
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    void sendMessage(inputValue);
  }

  return (
    <main
      style={{
        minHeight: "100vh",
        background: "linear-gradient(180deg, #f7f3eb 0%, #efe6d3 100%)",
        color: "#2e241c",
        padding: "32px 16px 48px",
        fontFamily: "Georgia, 'Times New Roman', serif",
      }}
    >
      <div
        style={{
          margin: "0 auto",
          maxWidth: 880,
          display: "grid",
          gap: 20,
        }}
      >
        <section
          style={{
            background: "rgba(255, 252, 246, 0.92)",
            border: "1px solid #d9c8a8",
            borderRadius: 24,
            padding: 24,
            boxShadow: "0 18px 40px rgba(88, 63, 34, 0.08)",
          }}
        >
          <p style={{ margin: 0, fontSize: 13, letterSpacing: "0.08em", textTransform: "uppercase" }}>
            Family Avatar Demo
          </p>
          <h1 style={{ margin: "10px 0 12px", fontSize: "clamp(2rem, 5vw, 3.4rem)", lineHeight: 1.05 }}>
            Тестовый чат с цифровым аватаром
          </h1>
          <p style={{ margin: 0, fontSize: 18, lineHeight: 1.6, maxWidth: 720 }}>
            Это демонстрационная версия. Аватар отвечает только на основе подготовленных воспоминаний.
            Если информации нет, он честно скажет, что не знает.
          </p>
        </section>

        <section
          style={{
            background: "rgba(255, 252, 246, 0.94)",
            border: "1px solid #d9c8a8",
            borderRadius: 24,
            padding: 20,
            display: "grid",
            gap: 16,
          }}
        >
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              gap: 16,
              flexWrap: "wrap",
            }}
          >
            <label style={{ display: "inline-flex", alignItems: "center", gap: 10, fontSize: 15 }}>
              <input
                checked={debugEnabled}
                onChange={(event) => setDebugEnabled(event.target.checked)}
                type="checkbox"
              />
              Показать использованные воспоминания
            </label>
            <button
              onClick={() => {
                setMessages([]);
                setErrorMessage(null);
              }}
              style={{
                borderRadius: 999,
                border: "1px solid #9b7d53",
                background: "transparent",
                color: "#6c4e28",
                padding: "10px 16px",
                cursor: "pointer",
              }}
              type="button"
            >
              Очистить чат
            </button>
          </div>

          <div
            style={{
              minHeight: 320,
              display: "grid",
              gap: 12,
              alignContent: "start",
            }}
          >
            {emptyStateVisible ? (
              <section
                style={{
                  borderRadius: 20,
                  border: "1px dashed #cfbb96",
                  padding: 18,
                  background: "#fbf7ef",
                }}
              >
                <strong style={{ display: "block", marginBottom: 10 }}>Попробуйте спросить:</strong>
                <div style={{ display: "flex", flexWrap: "wrap", gap: 10 }}>
                  {EXAMPLE_QUESTIONS.map((exampleQuestion) => (
                    <button
                      key={exampleQuestion}
                      onClick={() => setInputValue(exampleQuestion)}
                      style={{
                        borderRadius: 999,
                        border: "1px solid #cfbb96",
                        background: "#fffdf8",
                        color: "#4d3922",
                        cursor: "pointer",
                        padding: "10px 14px",
                      }}
                      type="button"
                    >
                      {exampleQuestion}
                    </button>
                  ))}
                </div>
              </section>
            ) : null}

            {messages.map((message) => (
              <article
                key={message.id}
                style={{
                  justifySelf: message.role === "user" ? "end" : "start",
                  maxWidth: "80%",
                  borderRadius: 20,
                  padding: "14px 16px",
                  background: message.role === "user" ? "#7a5030" : "#fffaf1",
                  color: message.role === "user" ? "#fff8ef" : "#33271e",
                  border: message.role === "user" ? "none" : "1px solid #dcc9a7",
                }}
              >
                <div style={{ fontSize: 13, marginBottom: 8, opacity: 0.78 }}>
                  {message.role === "user" ? "Вы" : "Аватар"}
                </div>
                <div style={{ lineHeight: 1.6, whiteSpace: "pre-wrap" }}>{message.text}</div>
                {message.role === "assistant" && message.lackOfEvidence ? (
                  <div style={{ marginTop: 10, fontSize: 13, opacity: 0.72 }}>
                    Нет точного подтверждения в доступных воспоминаниях.
                  </div>
                ) : null}
                {message.role === "assistant" && message.traceId ? (
                  <div style={{ marginTop: 10, fontSize: 12, opacity: 0.6 }}>
                    trace_id: {message.traceId}
                  </div>
                ) : null}
                {message.role === "assistant" && debugEnabled && message.evidence.length > 0 ? (
                  <details style={{ marginTop: 12 }}>
                    <summary style={{ cursor: "pointer" }}>Использованные воспоминания</summary>
                    <div style={{ display: "grid", gap: 10, marginTop: 10 }}>
                      {message.evidence.map((evidenceItem) => (
                        <div
                          key={`${message.id}-${evidenceItem.chunk_id}`}
                          style={{
                            borderRadius: 14,
                            border: "1px solid #e3d4b8",
                            padding: 12,
                            background: "#fffdf8",
                          }}
                        >
                          <div style={{ fontSize: 13, marginBottom: 6 }}>
                            chunk_id: {evidenceItem.chunk_id}
                            {evidenceItem.score !== null ? ` • score: ${evidenceItem.score.toFixed(3)}` : ""}
                          </div>
                          {evidenceItem.source_title ? (
                            <div style={{ fontSize: 13, marginBottom: 6 }}>{evidenceItem.source_title}</div>
                          ) : null}
                          <div style={{ fontSize: 14, lineHeight: 1.5 }}>
                            {evidenceItem.text_preview ?? "Короткий фрагмент недоступен."}
                          </div>
                        </div>
                      ))}
                    </div>
                  </details>
                ) : null}
              </article>
            ))}

            {loading ? (
              <div style={{ fontSize: 16, color: "#5b4630" }}>Аватар думает...</div>
            ) : null}
            {errorMessage ? (
              <div
                role="alert"
                style={{
                  borderRadius: 16,
                  padding: "12px 14px",
                  background: "#fff0ec",
                  color: "#8a3524",
                  border: "1px solid #e0b1a7",
                }}
              >
                {errorMessage}
              </div>
            ) : null}
          </div>

          <form onSubmit={handleSubmit} style={{ display: "grid", gap: 12 }}>
            <textarea
              aria-label="Сообщение для аватара"
              onChange={(event) => setInputValue(event.target.value)}
              placeholder="Напишите вопрос аватару..."
              rows={4}
              style={{
                width: "100%",
                resize: "vertical",
                borderRadius: 18,
                border: "1px solid #cbb58d",
                padding: 14,
                font: "inherit",
                color: "#2e241c",
                background: "#fffdf8",
              }}
              value={inputValue}
            />
            <div style={{ display: "flex", justifyContent: "flex-end" }}>
              <button
                disabled={loading}
                style={{
                  borderRadius: 999,
                  border: "none",
                  background: loading ? "#a68d72" : "#5f3f23",
                  color: "#fff7ee",
                  cursor: loading ? "default" : "pointer",
                  padding: "12px 20px",
                  font: "inherit",
                }}
                type="submit"
              >
                Отправить
              </button>
            </div>
          </form>
        </section>
      </div>
    </main>
  );
}

export default FaChatDemoPage;

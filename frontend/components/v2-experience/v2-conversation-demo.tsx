import { type FormEvent, useEffect, useState } from "react";

import type { AppLocale } from "../../lib/i18n/locales";
import { sendExperienceDemoMessage, type ExperienceDemoResponse } from "../../lib/v2-experience/chat";
import type { V2ExperienceContent } from "../../lib/v2-experience/content";
import V2SectionHeading from "./v2-section-heading";

type ConversationMessage = {
  id: string;
  role: "assistant" | "user";
  text: string;
  traceId?: string;
  evidence?: ExperienceDemoResponse["evidence"];
  memoryCandidate?: ExperienceDemoResponse["memoryCandidate"];
  lackOfEvidence?: boolean;
};

type V2ConversationDemoProps = {
  locale: AppLocale;
  content: V2ExperienceContent["conversation"];
};

function seedGreeting(content: V2ExperienceContent["conversation"]): ConversationMessage {
  return {
    id: "assistant-greeting",
    role: "assistant",
    text: content.greeting,
  };
}

export default function V2ConversationDemo({ locale, content }: V2ConversationDemoProps) {
  const [messages, setMessages] = useState<ConversationMessage[]>(() => [seedGreeting(content)]);
  const [inputValue, setInputValue] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  useEffect(() => {
    setMessages([seedGreeting(content)]);
    setInputValue("");
    setLoading(false);
    setErrorMessage(null);
  }, [content]);

  async function submitQuestion(rawValue: string) {
    const message = rawValue.trim();
    if (!message || loading) {
      return;
    }

    setMessages((currentMessages) => [
      ...currentMessages,
      {
        id: `user-${Date.now()}`,
        role: "user",
        text: message,
      },
    ]);
    setInputValue("");
    setErrorMessage(null);
    setLoading(true);

    try {
      const response = await sendExperienceDemoMessage(locale, message);
      setMessages((currentMessages) => [
        ...currentMessages,
        {
          id: `assistant-${response.traceId}`,
          role: "assistant",
          text: response.answer,
          traceId: response.traceId,
          evidence: response.evidence,
          memoryCandidate: response.memoryCandidate,
          lackOfEvidence: response.lackOfEvidence,
        },
      ]);
    } catch (error) {
      if (error instanceof Error && error.message.trim().length > 0) {
        setErrorMessage(error.message);
      } else {
        setErrorMessage(content.genericError);
      }
    } finally {
      setLoading(false);
    }
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    void submitQuestion(inputValue);
  }

  return (
    <section className="scroll-mt-32 px-4 py-24 sm:px-6 lg:px-8" id="demo">
      <div className="mx-auto max-w-7xl">
        <V2SectionHeading
          accent="cyan"
          description={content.lead}
          eyebrow={content.kicker}
          title={content.title}
        />

        <div className="mt-14 overflow-hidden rounded-[1.5rem] border border-white/10 bg-white/[0.035] shadow-[0_24px_80px_rgba(10,14,30,0.34)] backdrop-blur-xl sm:rounded-[2rem] lg:grid lg:grid-cols-[18rem_minmax(0,1fr)]">
          <aside
            className="border-b border-white/8 p-5 sm:p-8 lg:border-b-0 lg:border-r"
            style={{
              background: "radial-gradient(circle at 50% 28%, rgba(70, 90, 200, 0.28), transparent 68%)",
            }}
          >
            <div className="flex items-center justify-between gap-3">
              <span className="rounded-full border border-cyan/25 bg-cyan/10 px-3 py-1 text-[11px] uppercase tracking-[0.22em] text-cyan">
                {content.connectedBadge}
              </span>
              <span className="text-xs uppercase tracking-[0.18em] text-fg/40">POST /api/demo/fa-chat/message</span>
            </div>

            <div className="mt-8 flex items-center justify-center">
              <div className="relative h-28 w-28 animate-breathe rounded-full">
                <div
                  className="absolute inset-[-1rem] animate-halo rounded-full"
                  style={{ background: "radial-gradient(circle, rgba(110, 160, 255, 0.28), transparent 70%)" }}
                />
                <div
                  className="absolute inset-0 rounded-full"
                  style={{
                    background:
                      "radial-gradient(circle at 36% 30%, rgba(210, 238, 255, 0.95), rgba(110, 170, 246, 0.85) 40%, rgba(88, 72, 214, 0.9) 75%, rgba(20, 18, 60, 0.95))",
                    boxShadow: "0 0 34px rgba(100, 160, 255, 0.5)",
                  }}
                />
              </div>
            </div>

            <div className="mt-6 text-center">
              <h3 className="text-xl font-semibold text-fg">{content.shellTitle}</h3>
              <p className="mt-1 text-sm text-fg/55">{content.shellSubtitle}</p>
            </div>

            <div className="mt-8 flex h-10 items-end justify-center gap-1" data-testid="v2-wavebars">
              {Array.from({ length: 14 }).map((_, index) => (
                <span
                  className="w-1 rounded-full bg-[linear-gradient(180deg,#7fd8f7,#8b7cf6)] animate-wavebar"
                  key={index}
                  style={{
                    animationDelay: `${(index * 71) % 900}ms`,
                    animationPlayState: loading ? "running" : "paused",
                    height: `${18 + ((index * 7) % 18)}px`,
                  }}
                />
              ))}
            </div>

            <p className="mt-4 text-center text-xs uppercase tracking-[0.24em] text-fg/42">
              {loading ? content.loading : content.connectedBadge}
            </p>
          </aside>

          <div className="flex min-h-[34rem] flex-col sm:min-h-[38rem]">
            <div aria-live="polite" className="flex-1 space-y-4 overflow-y-auto px-5 py-6 sm:px-7">
              {messages.map((message) => {
                const isUser = message.role === "user";
                return (
                  <div className={isUser ? "flex justify-end" : "flex justify-start"} key={message.id}>
                    <div
                      className={`max-w-full rounded-[1.35rem] border px-4 py-3.5 text-sm leading-7 sm:max-w-[78%] ${
                        isUser
                          ? "border-cyan/25 bg-[linear-gradient(135deg,rgba(143,214,245,0.22),rgba(139,124,246,0.22))] text-fg"
                          : "border-white/10 bg-white/[0.05] text-fg/92"
                      }`}
                    >
                      <div className="mb-2 text-[11px] uppercase tracking-[0.22em] text-fg/45">
                        {isUser ? content.youLabel : content.shellTitle}
                      </div>
                      <div>{message.text}</div>

                      {!isUser && message.lackOfEvidence ? (
                        <div className="mt-4 rounded-2xl border border-gold/25 bg-gold/10 px-3 py-2 text-xs leading-6 text-gold">
                          {content.lackOfEvidenceLabel}
                        </div>
                      ) : null}

                      {!isUser && message.memoryCandidate ? (
                        <div className="mt-4 rounded-2xl border border-cyan/20 bg-cyan/10 px-3 py-3 text-xs leading-6 text-fg/78">
                          <div className="text-[11px] uppercase tracking-[0.18em] text-cyan">
                            {content.reviewCandidateLabel}
                          </div>
                          <div className="mt-2">{message.memoryCandidate.proposedMemoryText}</div>
                        </div>
                      ) : null}

                      {!isUser && message.traceId ? (
                        <div className="mt-4 space-y-3">
                          <div className="text-[11px] uppercase tracking-[0.18em] text-fg/38">
                            {content.traceLabel}: {message.traceId}
                          </div>

                          <div className="rounded-2xl border border-white/10 bg-ink/30 p-3">
                            <div className="text-[11px] uppercase tracking-[0.18em] text-fg/42">
                              {content.evidenceTitle}
                            </div>

                            {message.evidence && message.evidence.length > 0 ? (
                              <div className="mt-3 space-y-3">
                                {message.evidence.slice(0, 3).map((item) => (
                                  <div className="rounded-2xl border border-white/8 bg-white/[0.03] p-3" key={item.chunkId}>
                                    <div className="text-xs font-medium text-fg">
                                      {item.sourceTitle ??
                                        (item.sourceId !== null
                                          ? `${content.sourceFallbackPrefix} #${item.sourceId}`
                                          : item.chunkId)}
                                    </div>
                                    {item.textPreview ? (
                                      <div className="mt-1 text-xs leading-6 text-fg/58">{item.textPreview}</div>
                                    ) : null}
                                  </div>
                                ))}
                              </div>
                            ) : (
                              <div className="mt-3 text-xs leading-6 text-fg/55">{content.noEvidence}</div>
                            )}
                          </div>
                        </div>
                      ) : null}
                    </div>
                  </div>
                );
              })}

              {messages.length === 1 ? (
                <div className="rounded-[1.5rem] border border-dashed border-white/12 bg-white/[0.03] p-5 text-sm text-fg/58">
                  <div className="text-[11px] uppercase tracking-[0.22em] text-fg/42">{content.emptyTitle}</div>
                  <p className="mt-2 leading-7">{content.emptyBody}</p>
                </div>
              ) : null}

              {loading ? (
                <div className="flex justify-start">
                  <div className="rounded-[1.35rem] border border-white/10 bg-white/[0.05] px-4 py-3.5 text-sm text-fg/60">
                    {content.loading}
                  </div>
                </div>
              ) : null}
            </div>

            <div className="border-t border-white/8 px-5 py-4 sm:px-7">
              <div className="mb-3 flex flex-wrap gap-2">
                {content.suggestions.map((suggestion) => (
                  <button
                    className="rounded-full border border-white/12 bg-white/5 px-3.5 py-1.5 text-xs text-fg/72 transition-colors hover:border-cyan/35 hover:bg-cyan/10 hover:text-fg"
                    key={suggestion}
                    onClick={() => void submitQuestion(suggestion)}
                    type="button"
                  >
                    {suggestion}
                  </button>
                ))}
              </div>

              {errorMessage ? (
                <div className="mb-3 rounded-2xl border border-rose-300/30 bg-rose-500/10 px-4 py-3 text-sm text-rose-100">
                  {errorMessage}
                </div>
              ) : null}

              <form className="flex flex-col gap-3 sm:flex-row" onSubmit={handleSubmit}>
                <input
                  className="min-w-0 flex-1 rounded-[1.2rem] border border-white/12 bg-white/5 px-4 py-3 text-sm text-fg outline-none transition-colors placeholder:text-fg/35 focus:border-cyan/45"
                  onChange={(event) => setInputValue(event.target.value)}
                  placeholder={content.placeholder}
                  type="text"
                  value={inputValue}
                />
                <button
                  className="inline-flex items-center justify-center rounded-[1.2rem] bg-[linear-gradient(135deg,#8fd6f5,#8b7cf6)] px-5 py-3 text-sm font-semibold text-ink disabled:cursor-not-allowed disabled:opacity-60"
                  disabled={loading}
                  type="submit"
                >
                  {content.send}
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

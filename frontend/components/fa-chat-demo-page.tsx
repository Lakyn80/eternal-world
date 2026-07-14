"use client";

import { FormEvent, useState } from "react";
import Link from "next/link";

import { buildApiUrl } from "../lib/api-config";
import { getDictionary } from "../lib/i18n/get-dictionary";
import type { AppLocale } from "../lib/i18n/locales";
import { LanguageSwitcher } from "./language-switcher";
import styles from "./fa-chat-demo-page.module.css";


type DemoEvidenceItem = {
  chunk_id: string;
  source_id: number | null;
  source_title: string | null;
  score: number | null;
  text_preview: string | null;
};

type DemoMemoryCandidate = {
  status: "needs_review";
  confidence: "unverified";
  source: "conversation";
  proposed_memory_text: string;
  user_message_excerpt: string;
  reason: string;
};

type DemoEmotion = {
  primary: string;
  intensity: number;
};

type DemoFaceDirectives = {
  expression: string;
  gaze: string;
  head_motion: string;
};

type DemoVoiceDirectives = {
  tone: string;
  pace: string;
  volume: string;
};

type DemoFaChatResponse = {
  answer: string;
  locale?: AppLocale;
  lack_of_evidence: boolean;
  retrieval_used: boolean;
  persona_applied: boolean;
  guard_applied: boolean;
  guard_reason: string | null;
  trace_id: string;
  memory_candidate: DemoMemoryCandidate | null;
  emotion: DemoEmotion | null;
  face_directives: DemoFaceDirectives | null;
  voice_directives: DemoVoiceDirectives | null;
  evidence: DemoEvidenceItem[];
};

type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  text: string;
  traceId?: string;
  lackOfEvidence?: boolean;
  retrievalUsed?: boolean;
  personaApplied?: boolean;
  guardApplied?: boolean;
  guardReason?: string | null;
  memoryCandidate?: DemoMemoryCandidate | null;
  emotion?: DemoEmotion | null;
  faceDirectives?: DemoFaceDirectives | null;
  voiceDirectives?: DemoVoiceDirectives | null;
  evidence: DemoEvidenceItem[];
};

export function FaChatDemoPage({ locale }: { locale: AppLocale }) {
  const dictionary = getDictionary(locale);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [debugEnabled, setDebugEnabled] = useState(false);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const emptyStateVisible = messages.length === 0;

  async function readErrorDetail(response: Response): Promise<string> {
    try {
      const payload = (await response.json()) as { detail?: string };
      if (payload.detail) {
        return payload.detail;
      }
    } catch {
      // Ignore JSON parsing errors and fall back to a generic message.
    }
    return dictionary.chat.genericError;
  }

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
          locale,
        }),
      });
      if (!response.ok) {
        throw new Error(await readErrorDetail(response));
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
          personaApplied: payload.persona_applied,
          guardApplied: payload.guard_applied,
          guardReason: payload.guard_reason,
          memoryCandidate: payload.memory_candidate,
          emotion: payload.emotion,
          faceDirectives: payload.face_directives,
          voiceDirectives: payload.voice_directives,
          evidence: payload.evidence,
        },
      ]);
    } catch (error) {
      if (error instanceof Error && error.message.trim()) {
        setErrorMessage(error.message);
      } else {
        setErrorMessage(dictionary.chat.genericError);
      }
    } finally {
      setLoading(false);
    }
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    void sendMessage(inputValue);
  }

  return (
    <main className={styles.page}>
      <div className={styles.pageGlow} />
      <div className={styles.shell}>
        <section className={styles.scene}>
          <div className={styles.heroColumn}>
            <div className={styles.heroVisual}>
              <div className={styles.heroMist} />
              <div className={styles.avatarHalo}>
                <div className={styles.avatarCore}>
                  <div className={styles.avatarMonogram}>{dictionary.chat.avatarMonogram}</div>
                  <div className={styles.avatarName}>{dictionary.chat.avatarName}</div>
                  <div className={styles.avatarRole}>{dictionary.chat.avatarRole}</div>
                </div>
              </div>
            </div>

            <div className={styles.heroCopy}>
              <p className={styles.eyebrow}>{dictionary.chat.eyebrow}</p>
              <h1 className={styles.title}>{dictionary.chat.title}</h1>
              <p className={styles.lead}>{dictionary.chat.lead}</p>
              <div className={styles.exampleCluster}>
                {dictionary.chat.examples.map((exampleQuestion) => (
                  <button
                    key={exampleQuestion}
                    className={styles.exampleChip}
                    onClick={() => setInputValue(exampleQuestion)}
                    type="button"
                  >
                    {exampleQuestion}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <section className={styles.chatPanel}>
            <header className={styles.chatHeader}>
              <div>
                <div className={styles.chatBrand}>{dictionary.chat.brand}</div>
                <div className={styles.chatSubhead}>{dictionary.chat.subhead}</div>
              </div>
              <div className={styles.chatTools}>
                <LanguageSwitcher currentLocale={locale} />
                <Link className={styles.reviewLink} href={`/${locale}/family-memory-review`}>
                  {dictionary.chat.reviewLink}
                </Link>
                <label className={styles.toggle}>
                  <input
                    checked={debugEnabled}
                    onChange={(event) => setDebugEnabled(event.target.checked)}
                    type="checkbox"
                  />
                  <span>{dictionary.chat.debugLabel}</span>
                </label>
                <button
                  className={styles.clearButton}
                  onClick={() => {
                    setMessages([]);
                    setErrorMessage(null);
                  }}
                  type="button"
                >
                  {dictionary.chat.clear}
                </button>
              </div>
            </header>

            <div className={styles.chatBody}>
              {emptyStateVisible ? (
                <section className={styles.emptyCard}>
                  <div className={styles.emptyTitle}>{dictionary.chat.emptyTitle}</div>
                  <p className={styles.emptyText}>{dictionary.chat.emptyText}</p>
                </section>
              ) : null}

              {messages.map((message) => (
                <article
                  key={message.id}
                  className={`${styles.messageRow} ${
                    message.role === "user" ? styles.messageRowUser : styles.messageRowAssistant
                  }`}
                >
                  <div
                    className={`${styles.messageBubble} ${
                      message.role === "user" ? styles.userBubble : styles.assistantBubble
                    }`}
                  >
                    <div className={styles.messageRole}>
                      {message.role === "user" ? dictionary.chat.you : dictionary.chat.avatarName.split(" ")[0]}
                    </div>
                    <div className={styles.messageText}>{message.text}</div>

                    {message.role === "assistant" && message.lackOfEvidence ? (
                      <div className={styles.messageHint}>{dictionary.chat.lackOfEvidenceHint}</div>
                    ) : null}

                    {message.role === "assistant" && message.memoryCandidate ? (
                      <section className={styles.candidateCard}>
                        <div className={styles.candidateTitle}>{dictionary.chat.newEpisodeCardTitle}</div>
                        <div className={styles.candidateText}>
                          {message.memoryCandidate.proposed_memory_text}
                        </div>
                        <div className={styles.candidateMeta}>
                          status: {message.memoryCandidate.status} • confidence:{" "}
                          {message.memoryCandidate.confidence}
                        </div>
                      </section>
                    ) : null}

                    {message.role === "assistant" && message.emotion ? (
                      <div className={styles.directiveStrip}>
                        <span>tone: {message.emotion.primary}</span>
                        <span>intensity: {message.emotion.intensity.toFixed(2)}</span>
                        {message.personaApplied ? <span>persona: on</span> : null}
                      </div>
                    ) : null}

                    {message.role === "assistant" && message.traceId ? (
                      <div className={styles.traceLine}>trace_id: {message.traceId}</div>
                    ) : null}

                    {message.role === "assistant" && debugEnabled && message.evidence.length > 0 ? (
                      <details className={styles.detailsBlock}>
                        <summary>{dictionary.chat.usedMemoriesSummary}</summary>
                        <div className={styles.evidenceList}>
                          {message.evidence.map((evidenceItem) => (
                            <div
                              key={`${message.id}-${evidenceItem.chunk_id}`}
                              className={styles.evidenceCard}
                            >
                              <div className={styles.evidenceMeta}>
                                chunk_id: {evidenceItem.chunk_id}
                                {evidenceItem.score !== null
                                  ? ` • score: ${evidenceItem.score.toFixed(3)}`
                                  : ""}
                              </div>
                              {evidenceItem.source_title ? (
                                <div className={styles.evidenceTitle}>{evidenceItem.source_title}</div>
                              ) : null}
                              <div className={styles.evidenceText}>
                                {evidenceItem.text_preview ?? dictionary.chat.noPreview}
                              </div>
                            </div>
                          ))}
                        </div>
                      </details>
                    ) : null}

                    {message.role === "assistant" && debugEnabled && message.faceDirectives && message.voiceDirectives ? (
                      <div className={styles.debugMeta}>
                        face: {message.faceDirectives.expression} / {message.faceDirectives.gaze} /{" "}
                        {message.faceDirectives.head_motion}
                        <br />
                        voice: {message.voiceDirectives.tone} / {message.voiceDirectives.pace} /{" "}
                        {message.voiceDirectives.volume}
                      </div>
                    ) : null}
                  </div>
                </article>
              ))}

              {loading ? <div className={styles.loadingState}>{dictionary.chat.loading}</div> : null}

              {errorMessage ? (
                <div className={styles.errorBanner} role="alert">
                  {errorMessage}
                </div>
              ) : null}
            </div>

            <form className={styles.composer} onSubmit={handleSubmit}>
              <textarea
                aria-label={dictionary.chat.composerAriaLabel}
                className={styles.textarea}
                onChange={(event) => setInputValue(event.target.value)}
                placeholder={dictionary.chat.composerPlaceholder}
                rows={3}
                value={inputValue}
              />
              <div className={styles.composerFooter}>
                <div className={styles.composerHint}>{dictionary.chat.composerHint}</div>
                <button className={styles.sendButton} disabled={loading} type="submit">
                  {dictionary.chat.send}
                </button>
              </div>
            </form>
          </section>
        </section>
      </div>
    </main>
  );
}

export default FaChatDemoPage;

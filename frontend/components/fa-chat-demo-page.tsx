"use client";

import { FormEvent, useMemo, useState } from "react";
import Link from "next/link";

import { buildApiUrl } from "../lib/api-config";
import { getDictionary } from "../lib/i18n/get-dictionary";
import type { AppLocale } from "../lib/i18n/locales";
import { useUiTheme } from "../lib/use-ui-theme";
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
  candidate_id?: number | null;
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

function getShellText(locale: AppLocale) {
  if (locale === "cs") {
    return {
      home: "Produktový web",
      modeLight: "Světlý režim",
      modeDark: "Tmavý režim",
      liveBadge: "Živý workspace",
      evidence: "Panel důkazů",
      evidenceHint: "Avatar odpovídá jen z ověřené paměti. Důkaz je vždy důležitější než plynulost projevu.",
      emotionalLayer: "Emoční vrstva",
      emotionalHint: "Mění tón, tempo a výraz. Nikdy nemění fakta.",
      trustTitle: "Pravdivostní guardrail",
      trustBody: "Když důkaz chybí, systém řekne, že neví. Neimprovizuje rodinnou historii.",
      reviewQueue: "Rodinná fronta",
      reviewHint: "Nové epizody se posílají do workflow ke schválení vlastníkem avatara.",
      emptyEvidence: "Zatím nejsou zobrazené žádné zdroje.",
    };
  }
  if (locale === "ru") {
    return {
      home: "Продуктовый сайт",
      modeLight: "Светлый режим",
      modeDark: "Тёмный режим",
      liveBadge: "Живой workspace",
      evidence: "Панель доказательств",
      evidenceHint: "Аватар отвечает только из подтверждённой памяти. Доказательство важнее гладкости ответа.",
      emotionalLayer: "Эмоциональный слой",
      emotionalHint: "Он меняет тон, темп и выражение. Никогда не меняет факты.",
      trustTitle: "Guardrail правдивости",
      trustBody: "Когда доказательства нет, система говорит, что не знает. Семейная история не дорисовывается.",
      reviewQueue: "Семейная очередь",
      reviewHint: "Новые эпизоды попадают в workflow на утверждение владельцем аватара.",
      emptyEvidence: "Пока нет отображаемых источников.",
    };
  }
  return {
    home: "Product site",
    modeLight: "Light mode",
    modeDark: "Dark mode",
    liveBadge: "Live workspace",
    evidence: "Evidence panel",
    evidenceHint: "The avatar answers only from verified memory. Supporting evidence matters more than conversational smoothness.",
    emotionalLayer: "Emotion layer",
    emotionalHint: "It changes tone, pace, and expression. It never changes facts.",
    trustTitle: "Truthfulness guardrail",
    trustBody: "When evidence is missing, the system says it does not know. It does not improvise family history.",
    reviewQueue: "Family review queue",
    reviewHint: "New episodes are routed into owner review before they can become trusted avatar memory.",
    emptyEvidence: "No evidence sources are visible yet.",
  };
}

export function FaChatDemoPage({ locale }: { locale: AppLocale }) {
  const dictionary = getDictionary(locale);
  const shellText = getShellText(locale);
  const [theme, toggleTheme] = useUiTheme();
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [debugEnabled, setDebugEnabled] = useState(false);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const latestAssistantMessage = useMemo(
    () => [...messages].reverse().find((message) => message.role === "assistant") ?? null,
    [messages]
  );

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
    <main className={styles.page} data-theme={theme}>
      <header className={styles.header}>
        <div className={styles.headerBrand}>
          <Link className={styles.brandLink} href={`/${locale}`}>
            Eternal World
          </Link>
          <span className={styles.liveBadge}>{shellText.liveBadge}</span>
        </div>
        <div className={styles.headerTools}>
          <LanguageSwitcher currentLocale={locale} variant={theme === "dark" ? "dark" : "light"} />
          <button className={styles.themeButton} onClick={toggleTheme} type="button">
            {theme === "light" ? shellText.modeDark : shellText.modeLight}
          </button>
          <Link className={styles.headerLink} href={`/${locale}/family-memory-review`}>
            {dictionary.chat.reviewLink}
          </Link>
          <Link className={styles.headerLink} href={`/${locale}`}>
            {shellText.home}
          </Link>
        </div>
      </header>

      <section className={styles.hero}>
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
          <div className={styles.trustStrip}>
            <span>{shellText.trustTitle}</span>
            <span>{shellText.evidence}</span>
            <span>{shellText.reviewQueue}</span>
          </div>
        </div>

        <aside className={styles.heroPanel}>
          <div className={styles.avatarStage}>
            <div className={styles.avatarHalo} />
            <div className={styles.avatarCore}>
              <span className={styles.avatarMonogram}>{dictionary.chat.avatarMonogram}</span>
              <strong>{dictionary.chat.avatarName}</strong>
              <span>{dictionary.chat.avatarRole}</span>
            </div>
            <div className={styles.voiceWave} aria-hidden="true">
              <span />
              <span />
              <span />
              <span />
              <span />
            </div>
          </div>
          <div className={styles.sideCard}>
            <p className={styles.sideCardLabel}>{shellText.trustTitle}</p>
            <p>{shellText.trustBody}</p>
          </div>
          <div className={styles.sideCard}>
            <p className={styles.sideCardLabel}>{shellText.emotionalLayer}</p>
            <p>{shellText.emotionalHint}</p>
          </div>
        </aside>
      </section>

      <section className={styles.workspace}>
        <section className={styles.chatPanel}>
          <header className={styles.chatHeader}>
            <div>
              <div className={styles.chatBrand}>{dictionary.chat.brand}</div>
              <div className={styles.chatSubhead}>{dictionary.chat.subhead}</div>
            </div>
            <div className={styles.chatTools}>
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
            {messages.length === 0 ? (
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
                      <div className={styles.candidateText}>{message.memoryCandidate.proposed_memory_text}</div>
                      <div className={styles.candidateMeta}>
                        status: {message.memoryCandidate.status} • confidence: {message.memoryCandidate.confidence}
                      </div>
                      {message.memoryCandidate.candidate_id ? (
                        <Link
                          className={styles.reviewCandidateLink}
                          href={`/${locale}/family-memory-review?candidate=${message.memoryCandidate.candidate_id}`}
                        >
                          {dictionary.chat.reviewLink}
                        </Link>
                      ) : null}
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

                  {message.role === "assistant" && message.evidence.length > 0 ? (
                    <details className={styles.detailsBlock} open>
                      <summary>{dictionary.chat.usedMemoriesSummary}</summary>
                      <div className={styles.evidenceList}>
                        {message.evidence.map((evidenceItem) => (
                          <div key={`${message.id}-${evidenceItem.chunk_id}`} className={styles.evidenceCard}>
                            {evidenceItem.source_title ? (
                              <div className={styles.evidenceTitle}>{evidenceItem.source_title}</div>
                            ) : null}
                            <div className={styles.evidenceText}>
                              {evidenceItem.text_preview ?? dictionary.chat.noPreview}
                            </div>
                            {debugEnabled ? (
                              <div className={styles.evidenceMeta}>
                                chunk_id: {evidenceItem.chunk_id}
                                {evidenceItem.score !== null ? ` • score: ${evidenceItem.score.toFixed(3)}` : ""}
                              </div>
                            ) : null}
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

        <aside className={styles.insightPanel}>
          <div className={styles.sideCard}>
            <p className={styles.sideCardLabel}>{shellText.evidence}</p>
            <p>{shellText.evidenceHint}</p>
            {latestAssistantMessage?.evidence && latestAssistantMessage.evidence.length > 0 ? (
              <ul className={styles.insightList}>
                {latestAssistantMessage.evidence.map((item) => (
                  <li key={item.chunk_id}>{item.source_title ?? item.text_preview ?? item.chunk_id}</li>
                ))}
              </ul>
            ) : (
              <p className={styles.sideMuted}>{shellText.emptyEvidence}</p>
            )}
          </div>

          <div className={styles.sideCard}>
            <p className={styles.sideCardLabel}>{shellText.emotionalLayer}</p>
            {latestAssistantMessage?.emotion ? (
              <div className={styles.directivePanel}>
                <div>
                  <span>emotion</span>
                  <strong>{latestAssistantMessage.emotion.primary}</strong>
                </div>
                <div>
                  <span>intensity</span>
                  <strong>{latestAssistantMessage.emotion.intensity.toFixed(2)}</strong>
                </div>
                <div>
                  <span>gaze</span>
                  <strong>{latestAssistantMessage.faceDirectives?.gaze ?? "—"}</strong>
                </div>
                <div>
                  <span>pace</span>
                  <strong>{latestAssistantMessage.voiceDirectives?.pace ?? "—"}</strong>
                </div>
              </div>
            ) : (
              <p className={styles.sideMuted}>{shellText.emotionalHint}</p>
            )}
          </div>

          <div className={styles.sideCard}>
            <p className={styles.sideCardLabel}>{shellText.reviewQueue}</p>
            <p>{shellText.reviewHint}</p>
            <Link className={styles.reviewLink} href={`/${locale}/family-memory-review`}>
              {dictionary.chat.reviewLink}
            </Link>
          </div>
        </aside>
      </section>
    </main>
  );
}

export default FaChatDemoPage;

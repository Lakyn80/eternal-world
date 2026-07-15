import { buildApiUrl } from "../api-config";
import type { AppLocale } from "../i18n/locales";
import { getV2ExperienceContent } from "./content";

export type ExperienceEvidenceItem = {
  chunkId: string;
  sourceId: number | null;
  sourceTitle: string | null;
  score: number | null;
  textPreview: string | null;
};

export type ExperienceMemoryCandidate = {
  candidateId: number | null;
  status: "needs_review";
  confidence: "unverified";
  source: "conversation";
  proposedMemoryText: string;
  userMessageExcerpt: string;
  reason: string;
};

export type ExperienceDemoResponse = {
  answer: string;
  traceId: string;
  lackOfEvidence: boolean;
  evidence: ExperienceEvidenceItem[];
  memoryCandidate: ExperienceMemoryCandidate | null;
};

type RawRecord = Record<string, unknown>;

function isRecord(value: unknown): value is RawRecord {
  return typeof value === "object" && value !== null;
}

function nullableString(value: unknown): string | null {
  return typeof value === "string" && value.trim().length > 0 ? value : null;
}

function nullableNumber(value: unknown): number | null {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

function parseEvidenceItem(value: unknown): ExperienceEvidenceItem | null {
  if (!isRecord(value) || typeof value.chunk_id !== "string") {
    return null;
  }

  return {
    chunkId: value.chunk_id,
    sourceId: nullableNumber(value.source_id),
    sourceTitle: nullableString(value.source_title),
    score: nullableNumber(value.score),
    textPreview: nullableString(value.text_preview),
  };
}

function parseMemoryCandidate(value: unknown): ExperienceMemoryCandidate | null {
  if (!isRecord(value)) {
    return null;
  }

  if (
    value.status !== "needs_review" ||
    value.confidence !== "unverified" ||
    value.source !== "conversation" ||
    typeof value.proposed_memory_text !== "string" ||
    typeof value.user_message_excerpt !== "string" ||
    typeof value.reason !== "string"
  ) {
    return null;
  }

  return {
    candidateId: nullableNumber(value.candidate_id),
    status: "needs_review",
    confidence: "unverified",
    source: "conversation",
    proposedMemoryText: value.proposed_memory_text,
    userMessageExcerpt: value.user_message_excerpt,
    reason: value.reason,
  };
}

async function readErrorDetail(response: Response, locale: AppLocale): Promise<string> {
  const content = getV2ExperienceContent(locale);

  try {
    const payload = (await response.json()) as { detail?: unknown };
    if (typeof payload.detail === "string" && payload.detail.trim().length > 0) {
      return payload.detail;
    }
  } catch {
    // Fall back to a user-safe localized message.
  }

  return content.conversation.genericError;
}

function normalizeDemoResponse(payload: unknown, locale: AppLocale): ExperienceDemoResponse {
  const content = getV2ExperienceContent(locale);

  if (!isRecord(payload) || typeof payload.answer !== "string" || typeof payload.trace_id !== "string") {
    throw new Error(content.conversation.responseError);
  }

  const evidence = Array.isArray(payload.evidence) ? payload.evidence.map(parseEvidenceItem).filter(Boolean) : [];

  return {
    answer: payload.answer,
    traceId: payload.trace_id,
    lackOfEvidence: Boolean(payload.lack_of_evidence),
    evidence: evidence as ExperienceEvidenceItem[],
    memoryCandidate: parseMemoryCandidate(payload.memory_candidate),
  };
}

export async function sendExperienceDemoMessage(locale: AppLocale, message: string): Promise<ExperienceDemoResponse> {
  const content = getV2ExperienceContent(locale);

  let response: Response;
  try {
    response = await fetch(buildApiUrl("/api/demo/fa-chat/message"), {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        locale,
        message,
        debug: false,
      }),
    });
  } catch {
    throw new Error(content.conversation.networkError);
  }

  if (!response.ok) {
    throw new Error(await readErrorDetail(response, locale));
  }

  const payload = await response.json();
  return normalizeDemoResponse(payload, locale);
}

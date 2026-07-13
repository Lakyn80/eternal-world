import { buildApiUrl } from "../api-config";
import type {
  ActorContext,
  AvatarMemoryIndexingRead,
  MemoryCandidateReviewDetail,
  MemoryCandidateSummaryListResponse,
  OwnerReviewRequestPayload,
  OwnerReviewResponse,
} from "../../types/family-memory";

export class ApiRequestError extends Error {
  readonly status: number;
  readonly detail: string;

  constructor(status: number, detail: string) {
    super(detail);
    this.name = "ApiRequestError";
    this.status = status;
    this.detail = detail;
  }
}

const FALLBACK_MESSAGES: Record<number, string> = {
  400: "Некорректный запрос. Проверьте введённые данные и попробуйте ещё раз.",
  401: "Это действие недоступно для текущего участника.",
  403: "Это действие недоступно для текущего участника.",
  404: "Запись не найдена. Возможно, она была удалена или ещё не создана.",
  409: "Состояние записи изменилось на сервере. Данные будут обновлены.",
  422: "Введённые данные не прошли проверку.",
  500: "Временная ошибка сервиса. Попробуйте ещё раз через момент.",
  503: "Сервис индексации временно недоступен. Попробуйте ещё раз позже.",
};
const DEFAULT_FALLBACK_MESSAGE = "Не удалось выполнить действие. Попробуйте ещё раз.";

async function parseErrorDetail(response: Response): Promise<string> {
  try {
    const payload = (await response.json()) as { detail?: unknown };
    if (payload && typeof payload.detail === "string" && payload.detail.trim()) {
      return payload.detail;
    }
  } catch {
    // Body was not JSON (e.g. network gateway page) - fall back to a safe generic message.
  }
  return FALLBACK_MESSAGES[response.status] ?? DEFAULT_FALLBACK_MESSAGE;
}

async function requestJson<T>(url: string, init?: RequestInit): Promise<T> {
  let response: Response;
  try {
    response = await fetch(url, init);
  } catch {
    throw new ApiRequestError(0, "Не удалось связаться с сервером. Проверьте подключение.");
  }
  if (!response.ok) {
    throw new ApiRequestError(response.status, await parseErrorDetail(response));
  }
  return (await response.json()) as T;
}

function actorSearchParams(actor: ActorContext | null): URLSearchParams {
  const params = new URLSearchParams();
  if (actor) {
    params.set("actor_id", actor.actorId);
    params.set("actor_role", actor.actorRole);
    if (actor.relationshipToOwner) {
      params.set("relationship_to_owner", actor.relationshipToOwner);
    }
  }
  return params;
}

export async function fetchMemoryCandidateSummaries(
  profileId: number | null,
  actor: ActorContext | null
): Promise<MemoryCandidateSummaryListResponse> {
  const params = actorSearchParams(actor);
  if (profileId !== null) {
    params.set("profile_id", String(profileId));
  }
  const query = params.toString();
  return requestJson<MemoryCandidateSummaryListResponse>(
    buildApiUrl(`/api/demo/fa-chat/memory-candidates/review-summary${query ? `?${query}` : ""}`)
  );
}

export async function fetchMemoryCandidateReviewDetail(
  candidateId: number,
  profileId: number | null,
  actor: ActorContext | null
): Promise<MemoryCandidateReviewDetail> {
  const params = actorSearchParams(actor);
  if (profileId !== null) {
    params.set("profile_id", String(profileId));
  }
  const query = params.toString();
  return requestJson<MemoryCandidateReviewDetail>(
    buildApiUrl(`/api/demo/fa-chat/memory-candidates/${candidateId}/review-detail${query ? `?${query}` : ""}`)
  );
}

export async function submitOwnerReview(
  candidateId: number,
  payload: OwnerReviewRequestPayload
): Promise<OwnerReviewResponse> {
  return requestJson<OwnerReviewResponse>(
    buildApiUrl(`/api/demo/fa-chat/memory-candidates/${candidateId}/owner-review`),
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    }
  );
}

export async function submitIndexMemoryPromotion(
  promotionId: number,
  profileId: number | null,
  actor: ActorContext
): Promise<AvatarMemoryIndexingRead> {
  const params = actorSearchParams(actor);
  if (profileId !== null) {
    params.set("profile_id", String(profileId));
  }
  const query = params.toString();
  return requestJson<AvatarMemoryIndexingRead>(
    buildApiUrl(`/api/demo/fa-chat/memory-promotions/${promotionId}/index${query ? `?${query}` : ""}`),
    { method: "POST" }
  );
}

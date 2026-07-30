import { buildApiUrl } from "../api-config";
import type { AppLocale } from "../i18n/locales";
import type {
  ActorContext,
  AvatarMemoryIndexingRead,
  MemoryCandidateReviewDetail,
  MemoryCandidateSummaryListResponse,
  MemoryContentTranslation,
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

const FALLBACK_MESSAGES: Record<AppLocale, Record<number, string>> = {
  ru: {
    400: "Некорректный запрос. Проверьте введённые данные и попробуйте ещё раз.",
    401: "Это действие недоступно для текущего участника.",
    403: "Это действие недоступно для текущего участника.",
    404: "Запись не найдена. Возможно, она была удалена или ещё не создана.",
    409: "Состояние записи изменилось на сервере. Данные будут обновлены.",
    422: "Введённые данные не прошли проверку.",
    500: "Временная ошибка сервиса. Попробуйте ещё раз через момент.",
    503: "Сервис индексации временно недоступен. Попробуйте ещё раз позже.",
  },
  cs: {
    400: "Neplatný požadavek. Zkontrolujte zadané údaje a zkuste to znovu.",
    401: "Tato akce není pro současného účastníka dostupná.",
    403: "Tato akce není pro současného účastníka dostupná.",
    404: "Záznam nebyl nalezen. Možná byl odstraněn nebo ještě nebyl vytvořen.",
    409: "Stav záznamu se na serveru změnil. Data budou aktualizována.",
    422: "Zadané údaje neprošly ověřením.",
    500: "Dočasná chyba služby. Zkuste to prosím za chvíli znovu.",
    503: "Služba indexace je momentálně nedostupná. Zkuste to prosím později.",
  },
  en: {
    400: "The request is invalid. Check the entered data and try again.",
    401: "This action is not available for the current participant.",
    403: "This action is not available for the current participant.",
    404: "The record was not found. It may have been removed or not created yet.",
    409: "The record state changed on the server. The data will be refreshed.",
    422: "The submitted data did not pass validation.",
    500: "Temporary service error. Try again in a moment.",
    503: "The indexing service is temporarily unavailable. Try again later.",
  },
};
const DEFAULT_FALLBACK_MESSAGE: Record<AppLocale, string> = {
  ru: "Не удалось выполнить действие. Попробуйте ещё раз.",
  cs: "Akci se nepodařilo provést. Zkuste to prosím znovu.",
  en: "The action could not be completed. Try again.",
};
const NETWORK_ERROR_MESSAGE: Record<AppLocale, string> = {
  ru: "Не удалось связаться с сервером. Проверьте подключение.",
  cs: "Nepodařilo se spojit se serverem. Zkontrolujte připojení.",
  en: "The server could not be reached. Check the connection.",
};

async function parseErrorDetail(response: Response, locale: AppLocale): Promise<string> {
  try {
    const payload = (await response.json()) as { detail?: unknown };
    if (payload && typeof payload.detail === "string" && payload.detail.trim()) {
      return payload.detail;
    }
  } catch {
    // Body was not JSON (e.g. network gateway page) - fall back to a safe generic message.
  }
  return FALLBACK_MESSAGES[locale][response.status] ?? DEFAULT_FALLBACK_MESSAGE[locale];
}

async function requestJson<T>(url: string, init?: RequestInit, locale: AppLocale = "ru"): Promise<T> {
  let response: Response;
  try {
    response = await fetch(url, init);
  } catch {
    throw new ApiRequestError(0, NETWORK_ERROR_MESSAGE[locale]);
  }
  if (!response.ok) {
    throw new ApiRequestError(response.status, await parseErrorDetail(response, locale));
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
  actor: ActorContext | null,
  locale: AppLocale = "ru"
): Promise<MemoryCandidateSummaryListResponse> {
  const params = actorSearchParams(actor);
  if (profileId !== null) {
    params.set("profile_id", String(profileId));
  }
  params.set("locale", locale);
  const query = params.toString();
  return requestJson<MemoryCandidateSummaryListResponse>(
    buildApiUrl(`/api/demo/fa-chat/memory-candidates/review-summary${query ? `?${query}` : ""}`),
    undefined,
    locale
  );
}

export async function fetchMemoryCandidateReviewDetail(
  candidateId: number,
  profileId: number | null,
  actor: ActorContext | null,
  locale: AppLocale = "ru"
): Promise<MemoryCandidateReviewDetail> {
  const params = actorSearchParams(actor);
  if (profileId !== null) {
    params.set("profile_id", String(profileId));
  }
  params.set("locale", locale);
  const query = params.toString();
  return requestJson<MemoryCandidateReviewDetail>(
    buildApiUrl(`/api/demo/fa-chat/memory-candidates/${candidateId}/review-detail${query ? `?${query}` : ""}`),
    undefined,
    locale
  );
}

export async function submitOwnerReview(
  candidateId: number,
  payload: OwnerReviewRequestPayload,
  locale: AppLocale = "ru"
): Promise<OwnerReviewResponse> {
  return requestJson<OwnerReviewResponse>(
    buildApiUrl(`/api/demo/fa-chat/memory-candidates/${candidateId}/owner-review`),
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    },
    locale
  );
}

export async function submitIndexMemoryPromotion(
  promotionId: number,
  profileId: number | null,
  actor: ActorContext,
  locale: AppLocale = "ru"
): Promise<AvatarMemoryIndexingRead> {
  const params = actorSearchParams(actor);
  if (profileId !== null) {
    params.set("profile_id", String(profileId));
  }
  params.set("locale", locale);
  const query = params.toString();
  return requestJson<AvatarMemoryIndexingRead>(
    buildApiUrl(`/api/demo/fa-chat/memory-promotions/${promotionId}/index${query ? `?${query}` : ""}`),
    { method: "POST" },
    locale
  );
}

/** Explicit, owner-only translation retry (Task 64.5.1, Part G.29). Never
 * approves or indexes the candidate; safe to call repeatedly. */
export async function retryMemoryCandidateTranslation(
  candidateId: number,
  targetLanguage: "cs" | "ru",
  profileId: number | null,
  actor: ActorContext,
  locale: AppLocale = "ru"
): Promise<MemoryContentTranslation> {
  const params = actorSearchParams(actor);
  if (profileId !== null) {
    params.set("profile_id", String(profileId));
  }
  params.set("locale", locale);
  const query = params.toString();
  return requestJson<MemoryContentTranslation>(
    buildApiUrl(
      `/api/demo/fa-chat/memory-candidates/${candidateId}/translations/${targetLanguage}/retry${
        query ? `?${query}` : ""
      }`
    ),
    { method: "POST" },
    locale
  );
}

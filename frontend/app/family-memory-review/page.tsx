import { redirect } from "next/navigation";

import { DEFAULT_LOCALE } from "../../lib/i18n/locales";

/**
 * Task 64.5.1: superseded by `app/[locale]/family-memory-review/page.tsx`.
 * `middleware.ts` already redirects `/family-memory-review` (preserving
 * query parameters such as `?candidate=14`) to
 * `/{DEFAULT_LOCALE}/family-memory-review` at the edge; this Server
 * Component redirect is a defense-in-depth fallback that also preserves
 * query parameters (kept, not deleted, to preserve this exact legacy route).
 */
export default function FamilyMemoryReviewRoute({
  searchParams,
}: {
  searchParams: Record<string, string | string[] | undefined>;
}) {
  const params = new URLSearchParams();
  for (const [key, value] of Object.entries(searchParams)) {
    if (typeof value === "string") {
      params.set(key, value);
    } else if (Array.isArray(value) && value[0] !== undefined) {
      params.set(key, value[0]);
    }
  }
  const query = params.toString();
  redirect(`/${DEFAULT_LOCALE}/family-memory-review${query ? `?${query}` : ""}`);
}

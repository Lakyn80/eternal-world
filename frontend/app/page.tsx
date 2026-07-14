import { redirect } from "next/navigation";

import { DEFAULT_LOCALE } from "../lib/i18n/locales";

/**
 * Task 64.5.1: the real home page now lives at `app/[locale]/page.tsx`.
 * `middleware.ts` already redirects bare `/` to `/{DEFAULT_LOCALE}` at the
 * edge; this Server Component redirect is a defense-in-depth fallback for
 * any request that reaches Next.js routing without going through
 * middleware (kept, not deleted, to preserve this exact legacy route).
 */
export default function HomePage() {
  redirect(`/${DEFAULT_LOCALE}`);
}

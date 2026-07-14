import { redirect } from "next/navigation";

import { DEFAULT_LOCALE } from "../../lib/i18n/locales";

/**
 * Task 64.5.1: superseded by `app/[locale]/fa-chat/page.tsx`.
 * `middleware.ts` already redirects `/fa-chat` to `/{DEFAULT_LOCALE}/fa-chat`
 * at the edge; this Server Component redirect is a defense-in-depth
 * fallback (kept, not deleted, to preserve this exact legacy route).
 */
export default function FamilyAvatarChatPage() {
  redirect(`/${DEFAULT_LOCALE}/fa-chat`);
}

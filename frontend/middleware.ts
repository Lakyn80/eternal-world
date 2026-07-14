import { NextResponse, type NextRequest } from "next/server";

import { DEFAULT_LOCALE, isAppLocale } from "./lib/i18n/locales";

/**
 * Task 64.5.1 locale routing. Keeps the two supported interface locales
 * (cs/ru) at the very top of every path (`/cs/...`, `/ru/...`) and:
 *  - redirects legacy bare paths (`/fa-chat`, `/family-memory-review`, `/`)
 *    to their Czech (default) equivalent, so existing bookmarks/links
 *    keep working;
 *  - returns a safe 404 for an unsupported locale-shaped segment (e.g.
 *    `/de/fa-chat`) instead of silently accepting or double-prefixing it.
 *
 * Only touches routing - never reads/writes any stored data.
 */
export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  if (
    pathname.startsWith("/_next") ||
    pathname.startsWith("/api") ||
    pathname === "/favicon.ico" ||
    pathname.includes(".")
  ) {
    return NextResponse.next();
  }

  const segments = pathname.split("/").filter(Boolean);
  const firstSegment = segments[0];

  if (isAppLocale(firstSegment)) {
    // Thread the matched locale to the root layout via a request header
    // (read with `next/headers` in `app/layout.tsx`) so the very first
    // server-rendered response already has the correct `<html lang>` -
    // Next.js does not give the single top-level root layout access to a
    // nested `[locale]` route param directly, since that layout is also
    // shared by the (redirect-only) legacy non-locale routes.
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-app-locale", firstSegment);
    return NextResponse.next({ request: { headers: requestHeaders } });
  }

  // A locale-shaped (two-letter lowercase) segment that isn't one of our
  // supported locales is rejected explicitly, rather than being silently
  // treated as a path segment under the default locale.
  if (firstSegment && /^[a-z]{2}$/.test(firstSegment)) {
    return new NextResponse(null, { status: 404 });
  }

  const url = request.nextUrl.clone();
  url.pathname = `/${DEFAULT_LOCALE}${pathname === "/" ? "" : pathname}`;
  return NextResponse.redirect(url);
}

export const config = {
  matcher: ["/((?!_next|api|.*\\..*).*)"],
};

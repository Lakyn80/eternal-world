import Link from "next/link";

import { getDictionary } from "../../lib/i18n/get-dictionary";
import { parseAppLocale } from "../../lib/i18n/locales";
import { notFound } from "next/navigation";

export default function HomePage({ params }: { params: { locale: string } }) {
  const locale = parseAppLocale(params.locale);
  if (locale === null) {
    notFound();
  }
  const dictionary = getDictionary(locale);

  return (
    <main
      style={{
        minHeight: "100vh",
        display: "grid",
        placeItems: "center",
        background: "linear-gradient(180deg, #f7f3eb 0%, #efe6d3 100%)",
        padding: 24,
        fontFamily: "Georgia, 'Times New Roman', serif",
        color: "#2e241c",
      }}
    >
      <div
        style={{
          maxWidth: 760,
          textAlign: "center",
          background: "rgba(255, 252, 246, 0.94)",
          border: "1px solid #d9c8a8",
          borderRadius: 24,
          padding: 28,
        }}
      >
        <h1 style={{ marginTop: 0 }}>{dictionary.homePage.eyebrow}</h1>
        <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap", marginTop: 12 }}>
          <Link
            href={`/${locale}/fa-chat`}
            style={{
              display: "inline-block",
              borderRadius: 999,
              background: "#5f3f23",
              color: "#fff7ee",
              padding: "12px 18px",
              textDecoration: "none",
            }}
          >
            {dictionary.nav.goToChat}
          </Link>
          <Link
            href={`/${locale}/family-memory-review`}
            style={{
              display: "inline-block",
              borderRadius: 999,
              border: "1px solid #5f3f23",
              color: "#5f3f23",
              padding: "12px 18px",
              textDecoration: "none",
            }}
          >
            {dictionary.nav.goToReview}
          </Link>
        </div>
      </div>
    </main>
  );
}

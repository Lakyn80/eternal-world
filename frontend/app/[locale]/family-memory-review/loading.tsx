"use client";

import { usePathname } from "next/navigation";

const LOADING_TEXT: Record<string, string> = {
  cs: "Načítáme epizody ke kontrole...",
  ru: "Загружаем эпизоды на проверке...",
};

export default function FamilyMemoryReviewLoading() {
  const pathname = usePathname() ?? "";
  const locale = pathname.startsWith("/cs") ? "cs" : "ru";

  return (
    <main
      style={{
        minHeight: "100vh",
        display: "grid",
        placeItems: "center",
        background: "linear-gradient(180deg, #f7f3eb 0%, #efe6d3 100%)",
        color: "#6b5738",
        fontFamily: "Georgia, 'Times New Roman', serif",
      }}
    >
      <p>{LOADING_TEXT[locale]}</p>
    </main>
  );
}

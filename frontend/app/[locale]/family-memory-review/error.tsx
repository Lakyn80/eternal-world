"use client";

import { usePathname } from "next/navigation";

const ERROR_TEXT: Record<string, { message: string; retry: string }> = {
  cs: {
    message: "Nepodařilo se otevřít stránku kontroly rodinných vzpomínek. Zkuste to prosím znovu.",
    retry: "Zkusit znovu",
  },
  ru: {
    message: "Не удалось открыть страницу проверки семейных воспоминаний. Попробуйте ещё раз.",
    retry: "Повторить попытку",
  },
};

export default function FamilyMemoryReviewError({ reset }: { error: Error; reset: () => void }) {
  const pathname = usePathname() ?? "";
  const locale = pathname.startsWith("/cs") ? "cs" : "ru";
  const text = ERROR_TEXT[locale];

  return (
    <main
      style={{
        minHeight: "100vh",
        display: "grid",
        placeItems: "center",
        background: "linear-gradient(180deg, #f7f3eb 0%, #efe6d3 100%)",
        color: "#2e241c",
        fontFamily: "Georgia, 'Times New Roman', serif",
        padding: 24,
      }}
    >
      <div
        style={{
          maxWidth: 480,
          textAlign: "center",
          background: "rgba(255, 252, 246, 0.94)",
          border: "1px solid #d9c8a8",
          borderRadius: 20,
          padding: 24,
        }}
        role="alert"
      >
        <p>{text.message}</p>
        <button
          onClick={() => reset()}
          style={{
            marginTop: 12,
            borderRadius: 999,
            border: "1px solid #5f3f23",
            background: "#5f3f23",
            color: "#fff7ee",
            padding: "10px 18px",
            cursor: "pointer",
            font: "inherit",
          }}
          type="button"
        >
          {text.retry}
        </button>
      </div>
    </main>
  );
}

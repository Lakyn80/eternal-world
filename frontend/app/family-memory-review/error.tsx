"use client";

export default function FamilyMemoryReviewError({ reset }: { error: Error; reset: () => void }) {
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
        <p>Не удалось открыть страницу проверки семейных воспоминаний. Попробуйте ещё раз.</p>
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
          Повторить попытку
        </button>
      </div>
    </main>
  );
}

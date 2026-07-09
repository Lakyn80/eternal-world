import Link from "next/link";


export default function HomePage() {
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
        <h1 style={{ marginTop: 0 }}>Демо Eternal World</h1>
        <p style={{ lineHeight: 1.6 }}>
          Откройте тестовый чат с цифровым аватаром и задайте вопрос на русском языке.
        </p>
        <Link
          href="/fa-chat"
          style={{
            display: "inline-block",
            marginTop: 12,
            borderRadius: 999,
            background: "#5f3f23",
            color: "#fff7ee",
            padding: "12px 18px",
            textDecoration: "none",
          }}
        >
          Перейти в чат
        </Link>
      </div>
    </main>
  );
}

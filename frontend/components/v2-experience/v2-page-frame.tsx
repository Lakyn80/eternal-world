import { IBM_Plex_Sans, IBM_Plex_Serif } from "next/font/google";

const v2Sans = IBM_Plex_Sans({
  subsets: ["latin", "latin-ext", "cyrillic"],
  weight: ["300", "400", "500", "600"],
  display: "swap",
  variable: "--font-v2-sans",
});

const v2Serif = IBM_Plex_Serif({
  subsets: ["latin", "latin-ext", "cyrillic"],
  weight: ["400", "500", "600"],
  display: "swap",
  variable: "--font-v2-serif",
});

export default function V2PageFrame({ children }: { children: React.ReactNode }) {
  return <div className={`${v2Sans.variable} ${v2Serif.variable}`}>{children}</div>;
}

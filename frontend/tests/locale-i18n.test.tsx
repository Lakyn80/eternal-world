import React, { act } from "react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { createRoot, Root } from "react-dom/client";

const mockPathname = { value: "/cs/family-memory-review" };
const mockSearchParams = { value: new URLSearchParams() };

vi.mock("next/navigation", () => ({
  usePathname: () => mockPathname.value,
  useSearchParams: () => mockSearchParams.value,
}));

import { LanguageSwitcher } from "../components/language-switcher";
import { getDictionary } from "../lib/i18n/get-dictionary";
import {
  DEFAULT_LOCALE,
  isAppLocale,
  parseAppLocale,
  SUPPORTED_LOCALES,
  toIntlLocaleTag,
} from "../lib/i18n/locales";

(globalThis as typeof globalThis & { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

afterEach(() => {
  document.body.innerHTML = "";
  vi.restoreAllMocks();
});

describe("locale support (Task 64.5.1)", () => {
  it("default locale is Czech and all supported locales are exposed", () => {
    expect(DEFAULT_LOCALE).toBe("cs");
    expect(SUPPORTED_LOCALES).toContain("cs");
    expect(SUPPORTED_LOCALES).toContain("ru");
    expect(SUPPORTED_LOCALES).toContain("en");
    expect(SUPPORTED_LOCALES.length).toBe(3);
  });

  it("rejects an unsupported locale instead of silently accepting it", () => {
    expect(isAppLocale("de")).toBe(false);
    expect(parseAppLocale("de")).toBeNull();
    expect(parseAppLocale("cs")).toBe("cs");
    expect(parseAppLocale("ru")).toBe("ru");
    expect(parseAppLocale("en")).toBe("en");
  });

  it("maps locales to the correct Intl/BCP-47 tag for date formatting", () => {
    expect(toIntlLocaleTag("cs")).toBe("cs-CZ");
    expect(toIntlLocaleTag("ru")).toBe("ru-RU");
    expect(toIntlLocaleTag("en")).toBe("en-US");
  });

  it("all dictionaries expose exactly the same set of top-level keys", () => {
    const cs = getDictionary("cs");
    const ru = getDictionary("ru");
    const en = getDictionary("en");
    expect(Object.keys(cs).sort()).toEqual(Object.keys(ru).sort());
    expect(Object.keys(cs).sort()).toEqual(Object.keys(en).sort());
    // A representative nested section must also match key-for-key, so a
    // missing Czech translation cannot silently fall back to Russian.
    expect(Object.keys(cs.actions).sort()).toEqual(Object.keys(ru.actions).sort());
    expect(Object.keys(cs.actions).sort()).toEqual(Object.keys(en.actions).sort());
    expect(Object.keys(cs.translationPanel).sort()).toEqual(Object.keys(ru.translationPanel).sort());
    expect(Object.keys(cs.translationPanel).sort()).toEqual(Object.keys(en.translationPanel).sort());
    expect(Object.keys(cs.privacyScope).sort()).toEqual(Object.keys(ru.privacyScope).sort());
    expect(Object.keys(cs.privacyScope).sort()).toEqual(Object.keys(en.privacyScope).sort());
  });

  it("Czech dictionary text is never identical to Russian for primary UI strings", () => {
    const cs = getDictionary("cs");
    const ru = getDictionary("ru");
    expect(cs.reviewTitle).not.toBe(ru.reviewTitle);
    expect(cs.demoWarning).not.toBe(ru.demoWarning);
    expect(cs.actions.confirm).not.toBe(ru.actions.confirm);
    expect(cs.chat.title).not.toBe(ru.chat.title);
  });
});

function renderSwitcher(locale: "cs" | "ru" | "en"): { container: HTMLDivElement; root: Root } {
  const container = document.createElement("div");
  document.body.appendChild(container);
  const root = createRoot(container);
  act(() => {
    root.render(<LanguageSwitcher currentLocale={locale} />);
  });
  return { container, root };
}

describe("language switcher", () => {
  it("preserves the candidate query parameter when switching locale", () => {
    mockPathname.value = "/cs/family-memory-review";
    mockSearchParams.value = new URLSearchParams("candidate=14");

    const { container, root } = renderSwitcher("cs");
    const russianLink = Array.from(container.querySelectorAll("a")).find(
      (anchor) => anchor.textContent === "Русский"
    );
    expect(russianLink).toBeDefined();
    expect(russianLink?.getAttribute("href")).toBe("/ru/family-memory-review?candidate=14");

    act(() => {
      root.unmount();
    });
    container.remove();
  });

  it("does not render a link for the currently active locale", () => {
    mockPathname.value = "/ru/fa-chat";
    mockSearchParams.value = new URLSearchParams();

    const { container, root } = renderSwitcher("ru");
    expect(container.querySelectorAll("a").length).toBe(2);
    expect(container.textContent).toContain("Русский");
    expect(container.textContent).toContain("Čeština");
    expect(container.textContent).toContain("English");

    act(() => {
      root.unmount();
    });
    container.remove();
  });
});

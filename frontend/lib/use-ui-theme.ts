"use client";

import { useEffect, useState } from "react";

export type UiTheme = "light" | "dark";

const STORAGE_KEY = "ew-ui-theme";

export function useUiTheme(): [UiTheme, () => void] {
  const [theme, setTheme] = useState<UiTheme>("light");

  useEffect(() => {
    const storedTheme = window.localStorage.getItem(STORAGE_KEY);
    if (storedTheme === "light" || storedTheme === "dark") {
      setTheme(storedTheme);
      return;
    }
    const prefersDark =
      typeof window.matchMedia === "function" &&
      window.matchMedia("(prefers-color-scheme: dark)").matches;
    const preferredTheme = prefersDark ? "dark" : "light";
    setTheme(preferredTheme);
  }, []);

  useEffect(() => {
    window.localStorage.setItem(STORAGE_KEY, theme);
  }, [theme]);

  function toggleTheme() {
    setTheme((currentTheme) => (currentTheme === "light" ? "dark" : "light"));
  }

  return [theme, toggleTheme];
}

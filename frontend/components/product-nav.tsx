"use client";

import { useEffect, useId, useState } from "react";
import Link from "next/link";

import type { AppLocale } from "../lib/i18n/locales";
import { LanguageSwitcher } from "./language-switcher";

export type ProductNavItem = {
  label: string;
  href?: string;
  onClick?: () => void;
};

export type ProductNavProps = {
  locale: AppLocale;
  title?: string;
  subtitle?: string;
  items: ProductNavItem[];
  theme: "light" | "dark";
  themeLabel?: string;
  onToggleTheme?: () => void;
  activeHref?: string;
  menuLabel?: string;
};

export default function ProductNav({
  locale,
  title = "Eternal World",
  subtitle,
  items,
  theme,
  themeLabel,
  onToggleTheme,
  activeHref,
  menuLabel,
}: ProductNavProps) {
  const [open, setOpen] = useState(false);
  const menuId = useId();
  const resolvedMenuLabel = menuLabel ?? (locale === "ru" ? "Меню" : "Menu");

  useEffect(() => {
    if (!open) {
      return;
    }

    function handleKeyDown(event: KeyboardEvent) {
      if (event.key === "Escape") {
        setOpen(false);
      }
    }

    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, [open]);

  function renderItem(item: ProductNavItem, mobile = false) {
    const className = "ew-nav-link";
    if (item.href) {
      return (
        <Link
          aria-current={activeHref === item.href ? "page" : undefined}
          className={className}
          href={item.href}
          key={`${mobile ? "mobile" : "desktop"}-${item.href}-${item.label}`}
          onClick={() => setOpen(false)}
        >
          {item.label}
        </Link>
      );
    }

    return (
      <button
        className="ew-nav-action"
        key={`${mobile ? "mobile" : "desktop"}-${item.label}`}
        onClick={() => {
          item.onClick?.();
          setOpen(false);
        }}
        type="button"
      >
        {item.label}
      </button>
    );
  }

  return (
    <nav className="ew-nav ew-container-wide" data-theme={theme}>
      <div className="ew-nav-inner">
        <Link className="ew-nav-brand" href={`/${locale}`} onClick={() => setOpen(false)}>
          <span aria-hidden="true" className="ew-nav-mark" />
          <span className="ew-nav-title">
            <span className="ew-nav-name">{title}</span>
            {subtitle ? <span className="ew-nav-subtitle">{subtitle}</span> : null}
          </span>
        </Link>

        <div className="ew-nav-desktop">
          {items.map((item) => renderItem(item))}
          <span className="ew-nav-locale">
            <LanguageSwitcher currentLocale={locale} variant={theme === "dark" ? "dark" : "light"} />
          </span>
          {themeLabel && onToggleTheme ? (
            <button className="ew-nav-action" onClick={onToggleTheme} type="button">
              {themeLabel}
            </button>
          ) : null}
        </div>

        <button
          aria-controls={menuId}
          aria-expanded={open}
          className="ew-nav-menu-button"
          onClick={() => setOpen((current) => !current)}
          type="button"
        >
          {resolvedMenuLabel}
        </button>
      </div>

      <div className="ew-nav-mobile" hidden={!open} id={menuId}>
        {items.map((item) => renderItem(item, true))}
        <span className="ew-nav-locale">
          <LanguageSwitcher currentLocale={locale} variant={theme === "dark" ? "dark" : "light"} />
        </span>
        {themeLabel && onToggleTheme ? (
          <button className="ew-nav-action" onClick={onToggleTheme} type="button">
            {themeLabel}
          </button>
        ) : null}
      </div>
    </nav>
  );
}

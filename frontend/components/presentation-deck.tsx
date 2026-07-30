"use client";

import type { KeyboardEvent, TouchEvent, WheelEvent } from "react";
import { useEffect, useRef, useState } from "react";

import type { ExperienceContent } from "../lib/experience-content";
import styles from "./presentation-deck.module.css";

type PresentationDeckProps = {
  content: ExperienceContent;
  locale: "cs" | "ru" | "en";
  fullScreen?: boolean;
};

function getDeckLabels(locale: "cs" | "ru" | "en") {
  if (locale === "cs") {
    return { previous: "Předchozí", next: "Další" };
  }
  if (locale === "ru") {
    return { previous: "Назад", next: "Дальше" };
  }
  return { previous: "Prev", next: "Next" };
}

export function PresentationDeck({ content, locale, fullScreen = false }: PresentationDeckProps) {
  const [activeSlide, setActiveSlide] = useState(0);
  const deckRef = useRef<HTMLDivElement | null>(null);
  const lastWheelAtRef = useRef(0);
  const touchStartRef = useRef<number | null>(null);
  const labels = getDeckLabels(locale);

  useEffect(() => {
    if (fullScreen) {
      deckRef.current?.focus();
    }
  }, [fullScreen]);

  function updateSlide(nextIndex: number) {
    const lastIndex = content.slides.length - 1;
    const bounded = Math.max(0, Math.min(lastIndex, nextIndex));
    setActiveSlide(bounded);
  }

  function advance(direction: 1 | -1) {
    updateSlide(activeSlide + direction);
  }

  function handleWheel(event: WheelEvent<HTMLDivElement>) {
    const now = Date.now();
    if (now - lastWheelAtRef.current < 550) {
      return;
    }
    if (Math.abs(event.deltaY) < 18) {
      return;
    }
    lastWheelAtRef.current = now;
    advance(event.deltaY > 0 ? 1 : -1);
  }

  function handleTouchStart(event: TouchEvent<HTMLDivElement>) {
    touchStartRef.current = event.touches[0]?.clientY ?? null;
  }

  function handleTouchEnd(event: TouchEvent<HTMLDivElement>) {
    const startY = touchStartRef.current;
    const endY = event.changedTouches[0]?.clientY ?? null;
    touchStartRef.current = null;
    if (startY === null || endY === null) {
      return;
    }
    const deltaY = startY - endY;
    if (Math.abs(deltaY) < 42) {
      return;
    }
    advance(deltaY > 0 ? 1 : -1);
  }

  function handleKeyDown(event: KeyboardEvent<HTMLDivElement>) {
    if (event.key === "ArrowRight" || event.key === "ArrowDown" || event.key === "PageDown") {
      event.preventDefault();
      advance(1);
    }
    if (event.key === "ArrowLeft" || event.key === "ArrowUp" || event.key === "PageUp") {
      event.preventDefault();
      advance(-1);
    }
    if (event.key === "Home") {
      event.preventDefault();
      updateSlide(0);
    }
    if (event.key === "End") {
      event.preventDefault();
      updateSlide(content.slides.length - 1);
    }
  }

  const slide = content.slides[activeSlide];
  const progress = ((activeSlide + 1) / content.slides.length) * 100;

  return (
    <section className={fullScreen ? `${styles.deck} ${styles.deckFullScreen}` : styles.deck}>
      <div className={styles.deckHeader}>
        <div>
          <p className={styles.deckEyebrow}>{content.presentation.title}</p>
          <p className={styles.deckBody}>{content.presentation.body}</p>
        </div>
        <div className={styles.slideCounter}>
          {String(activeSlide + 1).padStart(2, "0")} / {String(content.slides.length).padStart(2, "0")}
        </div>
      </div>

      <div
        aria-label={content.presentation.title}
        className={styles.deckViewport}
        onKeyDown={handleKeyDown}
        onTouchEnd={handleTouchEnd}
        onTouchStart={handleTouchStart}
        onWheel={handleWheel}
        ref={deckRef}
        role="region"
        tabIndex={0}
      >
        <div className={styles.deckBackdrop} />
        <div className={styles.deckGlow} />
        <div className={styles.slideFrame}>
          <div className={styles.slideMeta}>{slide.kicker}</div>
          <h2 className={styles.slideTitle}>{slide.title}</h2>
          <p className={styles.slideText}>{slide.body}</p>
          <div className={styles.slideAccent}>{slide.accent}</div>
        </div>

        <aside className={styles.slideRail}>
          {content.slides.map((item, index) => (
            <button
              aria-current={index === activeSlide}
              className={index === activeSlide ? `${styles.railDot} ${styles.railDotActive}` : styles.railDot}
              key={item.title}
              onClick={() => updateSlide(index)}
              type="button"
            >
              <span className={styles.visuallyHidden}>{item.title}</span>
            </button>
          ))}
        </aside>
      </div>

      <div className={styles.deckFooter}>
        <div className={styles.progressTrack} aria-hidden="true">
          <div className={styles.progressFill} style={{ width: `${progress}%` }} />
        </div>
        <div className={styles.controls}>
          <span className={styles.usageHint}>{content.presentation.usage}</span>
          <div className={styles.buttonRow}>
            <button className={styles.navButton} onClick={() => advance(-1)} type="button">
              {labels.previous}
            </button>
            <button className={styles.navButton} onClick={() => advance(1)} type="button">
              {labels.next}
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

export default PresentationDeck;

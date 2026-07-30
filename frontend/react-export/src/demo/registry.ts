import type { DemoLang, MarketingDemoPersona } from './types';
import { csMarketingDemo } from './personas/cs';
import { enMarketingDemo } from './personas/en';
import { ruMarketingDemo } from './personas/ru';

/**
 * Single registry for homepage marketing demos. Adding a language = add a
 * persona file + one line here. Callers must go through `getMarketingDemo`
 * so UI never hardcodes Czech (or any other) realia.
 */
export const MARKETING_DEMOS: Record<DemoLang, MarketingDemoPersona> = {
  cs: csMarketingDemo,
  en: enMarketingDemo,
  ru: ruMarketingDemo,
};

export function getMarketingDemo(lang: DemoLang): MarketingDemoPersona {
  return MARKETING_DEMOS[lang];
}

export function matchDemoReply(lang: DemoLang, question: string): string {
  const demo = getMarketingDemo(lang);
  const s = question.toLowerCase();
  const hit = (keys: string[]) => keys.some((k) => s.includes(k.toLowerCase()));

  if (hit(demo.matchers.childhood)) return demo.replies.childhood;
  if (hit(demo.matchers.milestone)) return demo.replies.milestone;
  if (hit(demo.matchers.advice)) return demo.replies.advice;
  if (hit(demo.matchers.spouse)) return demo.replies.spouse;
  return demo.replies.fallback;
}

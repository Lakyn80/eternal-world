/**
 * Locale-scoped marketing demo persona (homepage ConversationDemo / Timeline /
 * AvatarStudio / Moments). Each UI language gets its own culturally grounded
 * fictional memory — Czech realia stay on `cs` only; `en` and `ru` must not
 * reuse Brno / Josef / Velvet November as a translation of the Czech story.
 *
 * Add a new language by creating `personas/<lang>.ts` and registering it in
 * `registry.ts`. Components never hardcode a persona name or place.
 */

export type DemoLang = 'en' | 'cs' | 'ru';

export interface DemoEvent {
  year: number;
  title: string;
  desc: string;
  media: string[];
}

export interface DemoMoment {
  slot: string;
  ph: string;
  quote: string;
  caption: string;
}

export interface DemoReplies {
  childhood: string;
  milestone: string;
  advice: string;
  spouse: string;
  fallback: string;
}

export interface MarketingDemoPersona {
  /** Stable id for tests / analytics (not shown in UI). */
  id: string;
  /** Given name shown in chat shell and avatar studio. */
  displayName: string;
  /** Birth year shown next to the name (e.g. "Josef · 1948"). */
  birthYear: number;
  /** Short place label used in chrome copy (city / region). */
  homePlace: string;
  /** Spouse given name used by reply matching. */
  spouseName: string;
  /** UI strings that mention the persona by name. */
  copy: {
    demoSub: string;
    demoPersona: string;
    demoPlaceholder: string;
    greet: string;
  };
  events: DemoEvent[];
  moments: DemoMoment[];
  replies: DemoReplies;
  suggestions: string[];
  /** Preferred speech languages offered in Avatar Studio for this locale. */
  avatarLangs: string[];
  /**
   * Extra lowercase keywords (beyond shared language roots) that map a user
   * question onto a reply slot. Keep short; matching is substring-based.
   */
  matchers: {
    childhood: string[];
    milestone: string[];
    advice: string[];
    spouse: string[];
  };
}

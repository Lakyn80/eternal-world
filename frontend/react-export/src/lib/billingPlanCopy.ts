import type { Lang } from '../i18n';

export type BillingPlanLocaleCopy = {
  name: string;
  features: string[];
};

/** UI copy for catalog plans. Entitlements stay backend-authoritative; only display text is localized. */
const PLAN_COPY: Record<Lang, Record<string, BillingPlanLocaleCopy>> = {
  en: {
    free: {
      name: 'Free',
      features: [
        '1 memorial',
        'up to 10 memories',
        '30 minutes of audio',
        '3 videos per month up to 30 seconds',
        'watermark enabled'
      ]
    },
    basic: {
      name: 'Basic',
      features: [
        'up to 3 memorials',
        'unlimited memories',
        'up to 5 hours of audio',
        '10 videos per month up to 2 minutes',
        'no watermark'
      ]
    },
    premium: {
      name: 'Premium',
      features: [
        'unlimited memorials',
        'unlimited audio and video',
        '4K quality',
        'video up to 10 minutes',
        'unlimited chat',
        'priority support'
      ]
    },
    family: {
      name: 'Family',
      features: [
        'everything from Premium',
        'up to 6 family members',
        'shared memories',
        'family tree support',
        'priority support'
      ]
    }
  },
  cs: {
    free: {
      name: 'Zdarma',
      features: [
        '1 memoriál',
        'až 10 vzpomínek',
        '30 minut audia',
        '3 videa měsíčně do 30 sekund',
        's vodoznakem'
      ]
    },
    basic: {
      name: 'Basic',
      features: [
        'až 3 memoriály',
        'neomezené vzpomínky',
        'až 5 hodin audia',
        '10 videí měsíčně do 2 minut',
        'bez vodoznaku'
      ]
    },
    premium: {
      name: 'Premium',
      features: [
        'neomezené memoriály',
        'neomezené audio a video',
        'kvalita 4K',
        'video až 10 minut',
        'neomezený chat',
        'prioritní podpora'
      ]
    },
    family: {
      name: 'Family',
      features: [
        'vše z Premium',
        'až 6 členů rodiny',
        'sdílené vzpomínky',
        'podpora rodokmenu',
        'prioritní podpora'
      ]
    }
  },
  ru: {
    free: {
      name: 'Бесплатно',
      features: [
        '1 мемориал',
        'до 10 воспоминаний',
        '30 минут аудио',
        '3 видео в месяц до 30 секунд',
        'с водяным знаком'
      ]
    },
    basic: {
      name: 'Basic',
      features: [
        'до 3 мемориалов',
        'неограниченные воспоминания',
        'до 5 часов аудио',
        '10 видео в месяц до 2 минут',
        'без водяного знака'
      ]
    },
    premium: {
      name: 'Premium',
      features: [
        'неограниченные мемориалы',
        'неограниченные аудио и видео',
        'качество 4K',
        'видео до 10 минут',
        'неограниченный чат',
        'приоритетная поддержка'
      ]
    },
    family: {
      name: 'Family',
      features: [
        'всё из Premium',
        'до 6 членов семьи',
        'общие воспоминания',
        'поддержка семейного дерева',
        'приоритетная поддержка'
      ]
    }
  }
};

export function getBillingPlanLocaleCopy(
  lang: Lang,
  planCode: string,
  fallbackName: string,
  fallbackFeatures: string[]
): BillingPlanLocaleCopy {
  const localized = PLAN_COPY[lang]?.[planCode.trim().toLowerCase()];
  if (localized) return localized;
  return { name: fallbackName, features: fallbackFeatures };
}

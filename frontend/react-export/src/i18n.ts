import { getMarketingDemo, matchDemoReply } from './demo';

export type Lang = 'en' | 'cs' | 'ru';

export interface FeatureT { title: string; desc: string; points: string[]; }
export interface BrainT { name: string; sub: string; }
export interface EventT { year: number; title: string; desc: string; media: string[]; }
export interface MomentT { slot: string; ph: string; quote: string; caption: string; }
export interface Replies { childhood: string; y1995: string; advice: string; marie: string; fallback: string; }

export interface Copy {
  navCta: string; kicker: string; heroTitle: string; heroSub: string; btnCreate: string; btnDemo: string;
  demoKicker: string; demoTitle: string; demoSub: string; demoPersona: string; demoPlaceholder: string; demoSend: string;
  listening: string; speakingSt: string; greet: string;
  featKicker: string; featTitle: string;
  brainKicker: string; brainTitle: string;
  tlKicker: string; tlTitle: string; tlDrop: string;
  stKicker: string; stTitle: string; stSub: string; stVoice: string; stPers: string; stLang: string; stAge: string; stAgeHint: string;
  momKicker: string; momTitle: string;
  footTitle: string; footSub: string; footNote: string;
}

function demoCopy(lang: Lang): Pick<Copy, 'demoSub' | 'demoPersona' | 'demoPlaceholder' | 'greet'> {
  return getMarketingDemo(lang).copy;
}

export const T: Record<Lang, Copy> = {
  en: {
    navCta: 'Create your AI', kicker: 'Digital immortality',
    heroTitle: 'Some stories should never end.',
    heroSub: 'Create your digital memory. Preserve your voice, your face, your memories and your personality — so the people you love can still reach you, forever.',
    btnCreate: 'Create your AI', btnDemo: 'Watch the demo',
    demoKicker: 'Live conversation', demoTitle: 'A conversation that never has to stop',
    ...demoCopy('en'),
    demoSend: 'Ask',
    listening: 'Listening', speakingSt: 'Speaking',
    featKicker: 'What is preserved', featTitle: 'Everything a person is.',
    brainKicker: 'Architecture', brainTitle: 'How a memory becomes a voice',
    tlKicker: 'Life timeline', tlTitle: 'A life, laid out in light', tlDrop: 'Drop a photo from this year',
    stKicker: 'Avatar studio', stTitle: 'Shape how they return',
    stSub: 'Families choose the voice, the age, the language and the temperament their memory speaks with.',
    stVoice: 'Voice', stPers: 'Temperament', stLang: 'Speaks', stAge: 'Remembered age',
    stAgeHint: 'The age the avatar looks and sounds. Most families choose the age they remember best.',
    momKicker: 'Why it matters', momTitle: 'The moments this is for',
    footTitle: 'You are not creating a chatbot. You are preserving a human being.',
    footSub: 'Voice, face, memories, temperament — kept safe, kept private, kept alive for the people who come after you.',
    footNote: 'Private by design · Family-owned memories · 2026'
  },
  cs: {
    navCta: 'Vytvořit své AI', kicker: 'Digitální nesmrtelnost',
    heroTitle: 'Některé příběhy by nikdy neměly skončit.',
    heroSub: 'Vytvořte svou digitální vzpomínku. Uchovejte svůj hlas, tvář, vzpomínky i osobnost — aby vás vaši blízcí mohli slyšet navždy.',
    btnCreate: 'Vytvořit své AI', btnDemo: 'Přehrát ukázku',
    demoKicker: 'Živý rozhovor', demoTitle: 'Rozhovor, který nemusí nikdy skončit',
    ...demoCopy('cs'),
    demoSend: 'Zeptat se',
    listening: 'Naslouchá', speakingSt: 'Mluví',
    featKicker: 'Co uchováváme', featTitle: 'Všechno, čím člověk je.',
    brainKicker: 'Architektura', brainTitle: 'Jak se vzpomínka stane hlasem',
    tlKicker: 'Časová osa života', tlTitle: 'Život vykreslený světlem', tlDrop: 'Vložte fotografii z tohoto roku',
    stKicker: 'Studio avatara', stTitle: 'Určete, jak se vrátí',
    stSub: 'Rodina volí hlas, věk, jazyk i povahu, se kterou vzpomínka mluví.',
    stVoice: 'Hlas', stPers: 'Povaha', stLang: 'Mluví', stAge: 'Zapamatovaný věk',
    stAgeHint: 'Věk, ve kterém avatar vypadá a zní. Rodiny většinou volí věk, který si pamatují nejlépe.',
    momKicker: 'Proč na tom záleží', momTitle: 'Chvíle, pro které to je',
    footTitle: 'Nevytváříte chatbota. Uchováváte člověka.',
    footSub: 'Hlas, tvář, vzpomínky, povaha — v bezpečí, v soukromí, živé pro ty, kdo přijdou po vás.',
    footNote: 'Soukromí především · Vzpomínky patří rodině · 2026'
  },
  ru: {
    navCta: 'Создать своё AI', kicker: 'Цифровое бессмертие',
    heroTitle: 'Некоторые истории не должны заканчиваться.',
    heroSub: 'Создайте свою цифровую память. Сохраните голос, лицо, воспоминания и личность — чтобы близкие могли слышать вас всегда.',
    btnCreate: 'Создать своё AI', btnDemo: 'Смотреть демо',
    demoKicker: 'Живой разговор', demoTitle: 'Разговор, который не должен прерываться',
    ...demoCopy('ru'),
    demoSend: 'Спросить',
    listening: 'Слушает', speakingSt: 'Говорит',
    featKicker: 'Что сохраняется', featTitle: 'Всё, чем является человек.',
    brainKicker: 'Архитектура', brainTitle: 'Как память становится голосом',
    tlKicker: 'Линия жизни', tlTitle: 'Жизнь, выложенная светом', tlDrop: 'Перетащите фото этого года',
    stKicker: 'Студия аватара', stTitle: 'Выберите, каким он вернётся',
    stSub: 'Семья выбирает голос, возраст, язык и характер, с которыми говорит память.',
    stVoice: 'Голос', stPers: 'Характер', stLang: 'Говорит на', stAge: 'Возраст в памяти',
    stAgeHint: 'Возраст, в котором аватар выглядит и звучит. Семьи чаще выбирают возраст, который помнят лучше всего.',
    momKicker: 'Почему это важно', momTitle: 'Моменты, ради которых это создано',
    footTitle: 'Вы создаёте не чат-бота. Вы сохраняете человека.',
    footSub: 'Голос, лицо, воспоминания, характер — в безопасности, в тайне, живые для тех, кто придёт после вас.',
    footNote: 'Приватность прежде всего · Память принадлежит семье · 2026'
  }
};

export const FEATURES: Record<Lang, FeatureT[]> = {
  en: [
    { title: 'AI Memory', desc: 'Unlimited memories: stories, documents, photos, videos, voice recordings and personal knowledge.', points: ['Stories', 'Photos & video', 'Voice recordings'] },
    { title: 'AI Chat', desc: 'Natural conversations with long-term memory, context and emotional understanding.', points: ['Long-term memory', 'Emotional', 'Multi-language'] },
    { title: 'Voice Clone', desc: 'Their real voice with natural emotion — streaming conversation, calls and voice messages.', points: ['Real voice', 'Phone calls', 'Voice messages'] },
    { title: 'Face Avatar', desc: 'A photorealistic avatar with eye movement, expression and lip synchronization.', points: ['Expressions', 'Eye contact', 'Lip sync'] },
    { title: 'Family Archive', desc: 'Private family memories, shared albums, a family timeline and the events that mattered.', points: ['Private', 'Shared albums', 'Relationships'] },
    { title: 'Daily Diary', desc: 'Voice or text diary with automatic summaries and search through a lifetime of memory.', points: ['Voice diary', 'Summaries', 'Search'] },
    { title: 'AI Biography', desc: 'An automatically written biography — chapters, people, places and achievements.', points: ['Life chapters', 'People', 'Places'] },
    { title: 'Family Questions', desc: '"What was grandpa like?" "What happened in 1995?" The AI answers naturally.', points: ['For children', 'Natural answers', 'Advice'] },
    { title: 'Legacy', desc: 'Future generations can still speak with you. Your personality never disappears.', points: ['Generations', 'Forever', 'Yours'] }
  ],
  cs: [
    { title: 'AI paměť', desc: 'Neomezené vzpomínky: příběhy, dokumenty, fotografie, videa, nahrávky hlasu a osobní znalosti.', points: ['Příběhy', 'Fotky a videa', 'Nahrávky hlasu'] },
    { title: 'AI rozhovor', desc: 'Přirozené rozhovory s dlouhodobou pamětí, kontextem a citovým porozuměním.', points: ['Dlouhodobá paměť', 'Emoce', 'Více jazyků'] },
    { title: 'Klon hlasu', desc: 'Skutečný hlas s přirozenými emocemi — plynulý rozhovor, telefonáty i hlasové zprávy.', points: ['Skutečný hlas', 'Telefonáty', 'Hlasové zprávy'] },
    { title: 'Avatar tváře', desc: 'Fotorealistický avatar s pohybem očí, výrazem a synchronizací rtů.', points: ['Výrazy', 'Oční kontakt', 'Synchronizace rtů'] },
    { title: 'Rodinný archiv', desc: 'Soukromé rodinné vzpomínky, sdílená alba, rodinná časová osa a důležité události.', points: ['Soukromé', 'Sdílená alba', 'Vztahy'] },
    { title: 'Denní deník', desc: 'Hlasový nebo textový deník s automatickými souhrny a vyhledáváním v celém životě.', points: ['Hlasový deník', 'Souhrny', 'Vyhledávání'] },
    { title: 'AI biografie', desc: 'Automaticky psaná biografie — kapitoly, lidé, místa a úspěchy.', points: ['Kapitoly života', 'Lidé', 'Místa'] },
    { title: 'Otázky rodiny', desc: '„Jaký byl děda?" „Co se stalo v roce 1995?" AI odpovídá přirozeně.', points: ['Pro děti', 'Přirozené odpovědi', 'Rady'] },
    { title: 'Odkaz', desc: 'Budoucí generace s vámi stále mohou mluvit. Vaše osobnost nikdy nezmizí.', points: ['Generace', 'Navždy', 'Vaše'] }
  ],
  ru: [
    { title: 'AI-память', desc: 'Безграничные воспоминания: истории, документы, фотографии, видео, записи голоса и личные знания.', points: ['Истории', 'Фото и видео', 'Записи голоса'] },
    { title: 'AI-диалог', desc: 'Естественные разговоры с долгой памятью, контекстом и эмоциональным пониманием.', points: ['Долгая память', 'Эмоции', 'Много языков'] },
    { title: 'Клон голоса', desc: 'Настоящий голос с живыми эмоциями — разговор в реальном времени, звонки и голосовые сообщения.', points: ['Настоящий голос', 'Звонки', 'Голосовые'] },
    { title: 'Аватар лица', desc: 'Фотореалистичный аватар с движением глаз, мимикой и синхронизацией губ.', points: ['Мимика', 'Взгляд', 'Синхронизация губ'] },
    { title: 'Семейный архив', desc: 'Приватные семейные воспоминания, общие альбомы, семейная линия времени и важные события.', points: ['Приватно', 'Общие альбомы', 'Связи'] },
    { title: 'Ежедневный дневник', desc: 'Голосовой или текстовый дневник с автоматическими итогами и поиском по всей жизни.', points: ['Голосовой дневник', 'Итоги', 'Поиск'] },
    { title: 'AI-биография', desc: 'Автоматически написанная биография — главы, люди, места и достижения.', points: ['Главы жизни', 'Люди', 'Места'] },
    { title: 'Вопросы семьи', desc: '«Каким был дедушка?» «Что случилось в 1995-м?» AI отвечает естественно.', points: ['Для детей', 'Живые ответы', 'Советы'] },
    { title: 'Наследие', desc: 'Будущие поколения смогут говорить с вами. Ваша личность никогда не исчезнет.', points: ['Поколения', 'Навсегда', 'Ваше'] }
  ]
};

export const BRAIN: Record<Lang, BrainT[]> = {
  en: [
    { name: 'Memory', sub: 'everything recorded' }, { name: 'Knowledge', sub: 'a life, structured' }, { name: 'Reasoning', sub: 'how they thought' },
    { name: 'Voice', sub: 'how they sounded' }, { name: 'Avatar', sub: 'how they looked' }, { name: 'Conversation', sub: 'how they loved' }
  ],
  cs: [
    { name: 'Paměť', sub: 'vše zaznamenané' }, { name: 'Znalosti', sub: 'život v souvislostech' }, { name: 'Uvažování', sub: 'jak přemýšlel' },
    { name: 'Hlas', sub: 'jak zněl' }, { name: 'Avatar', sub: 'jak vypadal' }, { name: 'Rozhovor', sub: 'jak měl rád' }
  ],
  ru: [
    { name: 'Память', sub: 'всё записанное' }, { name: 'Знания', sub: 'жизнь в связях' }, { name: 'Мышление', sub: 'как он думал' },
    { name: 'Голос', sub: 'как он звучал' }, { name: 'Аватар', sub: 'как он выглядел' }, { name: 'Разговор', sub: 'как он любил' }
  ]
};

/** Locale-scoped life timeline — sourced from the marketing demo persona pack. */
export const EVENTS: Record<Lang, EventT[]> = {
  en: getMarketingDemo('en').events,
  cs: getMarketingDemo('cs').events,
  ru: getMarketingDemo('ru').events,
};

export const VOICES: Record<Lang, string[]> = {
  en: ['Original recording', 'Warm · older', 'Younger self'],
  cs: ['Původní nahrávka', 'Vřelý · starší', 'Mladší já'],
  ru: ['Оригинальная запись', 'Тёплый · старше', 'Молодой я']
};
export const PERSONALITIES: Record<Lang, string[]> = {
  en: ['Gentle', 'Witty', 'Thoughtful'],
  cs: ['Jemný', 'Vtipný', 'Přemýšlivý'],
  ru: ['Мягкий', 'С юмором', 'Задумчивый']
};
export const AVATAR_LANGS: Record<Lang, string[]> = {
  en: getMarketingDemo('en').avatarLangs,
  cs: getMarketingDemo('cs').avatarLangs,
  ru: getMarketingDemo('ru').avatarLangs,
};

export const MOMENTS: Record<Lang, MomentT[]> = {
  en: getMarketingDemo('en').moments,
  cs: getMarketingDemo('cs').moments,
  ru: getMarketingDemo('ru').moments,
};

/** @deprecated Prefer getMarketingDemo(lang).replies — kept for callers expecting the old shape. */
export const REPLIES: Record<Lang, Replies> = {
  en: {
    childhood: getMarketingDemo('en').replies.childhood,
    y1995: getMarketingDemo('en').replies.milestone,
    advice: getMarketingDemo('en').replies.advice,
    marie: getMarketingDemo('en').replies.spouse,
    fallback: getMarketingDemo('en').replies.fallback,
  },
  cs: {
    childhood: getMarketingDemo('cs').replies.childhood,
    y1995: getMarketingDemo('cs').replies.milestone,
    advice: getMarketingDemo('cs').replies.advice,
    marie: getMarketingDemo('cs').replies.spouse,
    fallback: getMarketingDemo('cs').replies.fallback,
  },
  ru: {
    childhood: getMarketingDemo('ru').replies.childhood,
    y1995: getMarketingDemo('ru').replies.milestone,
    advice: getMarketingDemo('ru').replies.advice,
    marie: getMarketingDemo('ru').replies.spouse,
    fallback: getMarketingDemo('ru').replies.fallback,
  },
};

export const SUGGESTIONS: Record<Lang, string[]> = {
  en: getMarketingDemo('en').suggestions,
  cs: getMarketingDemo('cs').suggestions,
  ru: getMarketingDemo('ru').suggestions,
};

export function matchReply(lang: Lang, question: string): string {
  return matchDemoReply(lang, question);
}

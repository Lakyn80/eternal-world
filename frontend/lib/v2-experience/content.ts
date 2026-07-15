import type { AppLocale } from "../i18n/locales";

export type V2SectionId = "story" | "demo" | "architecture" | "timeline" | "studio" | "moments";

export type V2NavigationLink = {
  id: V2SectionId;
  label: string;
};

export type V2WorkspaceLink = {
  href: "/fa-chat" | "/family-memory-review" | "/presentation";
  label: string;
  description: string;
};

export type V2Feature = {
  title: string;
  description: string;
  points: string[];
};

export type V2ArchitectureNode = {
  name: string;
  detail: string;
};

export type V2TimelineEvent = {
  year: number;
  title: string;
  description: string;
  media: string[];
  slotTitle: string;
  slotBody: string;
};

export type V2Moment = {
  id: string;
  slotTitle: string;
  slotBody: string;
  quote: string;
  caption: string;
};

export type V2AvatarStudioPreset = {
  voices: string[];
  temperaments: string[];
  languages: string[];
  defaultAge: number;
  previewName: string;
  previewTagline: string;
};

export type V2ExperienceContent = {
  brand: {
    name: string;
    accent: string;
  };
  localeNames: Record<AppLocale, string>;
  navigation: {
    links: V2NavigationLink[];
    openWorkspace: string;
    switchLanguage: string;
  };
  hero: {
    kicker: string;
    title: string;
    lead: string;
    primaryCta: string;
    secondaryCta: string;
    trustLine: string;
    routeLabel: string;
    workspaceLinks: V2WorkspaceLink[];
  };
  conversation: {
    kicker: string;
    title: string;
    lead: string;
    connectedBadge: string;
    shellTitle: string;
    shellSubtitle: string;
    placeholder: string;
    send: string;
    loading: string;
    genericError: string;
    responseError: string;
    networkError: string;
    emptyTitle: string;
    emptyBody: string;
    evidenceTitle: string;
    noEvidence: string;
    traceLabel: string;
    reviewCandidateLabel: string;
    lackOfEvidenceLabel: string;
    youLabel: string;
    sourceFallbackPrefix: string;
    suggestions: string[];
    greeting: string;
  };
  features: {
    kicker: string;
    title: string;
    items: V2Feature[];
  };
  architecture: {
    kicker: string;
    title: string;
    items: V2ArchitectureNode[];
  };
  timeline: {
    kicker: string;
    title: string;
    actionLabel: string;
    badgeLabel: string;
    items: V2TimelineEvent[];
  };
  studio: {
    kicker: string;
    title: string;
    lead: string;
    voiceLabel: string;
    temperamentLabel: string;
    languageLabel: string;
    ageLabel: string;
    ageHint: string;
    previewNote: string;
    launchLabel: string;
    presets: V2AvatarStudioPreset;
  };
  moments: {
    kicker: string;
    title: string;
    actionLabel: string;
    badgeLabel: string;
    items: V2Moment[];
  };
  footer: {
    title: string;
    body: string;
    primaryCta: string;
    secondaryCta: string;
    note: string;
  };
};

const CONTENT: Record<AppLocale, V2ExperienceContent> = {
  cs: {
    brand: {
      name: "Eternal World",
      accent: "Věčný svět",
    },
    localeNames: {
      cs: "Čeština",
      ru: "Русский",
      en: "English",
    },
    navigation: {
      links: [
        { id: "story", label: "Příběh" },
        { id: "demo", label: "Živé demo" },
        { id: "architecture", label: "Architektura" },
        { id: "timeline", label: "Časová osa" },
        { id: "studio", label: "Studio" },
        { id: "moments", label: "Chvíle" },
      ],
      openWorkspace: "Otevřít chat",
      switchLanguage: "Přepnout jazyk",
    },
    hero: {
      kicker: "Digitální rodinná paměť",
      title: "Některé hlasy mají zůstat přesné, důvěryhodné a dostupné i za roky.",
      lead:
        "Nový frontend staví produktovou zkušenost kolem důvěry: avatar odpovídá z uložené paměti, nové epizody posílá do rodinné kontroly a teprve potom se stávají součástí živé paměti.",
      primaryCta: "Otevřít chat s avatarem",
      secondaryCta: "Zobrazit živé demo",
      trustLine: "Napojeno na existující chat, workflow kontroly i prezentaci. Produktové cesty zůstávají beze změny.",
      routeLabel: "Napojená část",
      workspaceLinks: [
        {
          href: "/fa-chat",
          label: "Chat s avatarem",
          description: "Reálný backend endpoint pro odpovědi, trace id a důkazní vrstvu.",
        },
        {
          href: "/family-memory-review",
          label: "Rodinná kontrola",
          description: "Kontrola vlastníkem, jazykové verze, indexace a stavy workflow.",
        },
        {
          href: "/presentation",
          label: "Produktová prezentace",
          description: "Prezentační pohled na produkt bez zásahu do pracovního toku.",
        },
      ],
    },
    conversation: {
      kicker: "Napojené demo",
      title: "Stejný backend, jiný frontend obal",
      lead:
        "Tato část už nehraje lokální simulovaný chat. Posílá dotazy na stávající demo API a zobrazuje odpověď, trace i případnou evidenci nebo návrh nové epizody ke kontrole.",
      connectedBadge: "Napojené API",
      shellTitle: "Eva Nováková",
      shellSubtitle: "Teplý rodinný avatar · ověřená paměť",
      placeholder: "Napište Evě otázku nebo vřelou zprávu...",
      send: "Odeslat",
      loading: "Eva připravuje odpověď...",
      genericError: "Nepodařilo se získat odpověď. Zkuste to prosím znovu.",
      responseError: "Server vrátil neplatnou odpověď. Zkontrolujte backend kontrakt.",
      networkError: "Nepodařilo se spojit se serverem. Zkontrolujte připojení.",
      emptyTitle: "Začněte ověřitelnou otázkou",
      emptyBody:
        "Ptejte se na dětství, rodinné vztahy nebo konkrétní vzpomínku. Pokud podklad chybí, systém to má přiznat a založit kandidáta do fronty kontroly.",
      evidenceTitle: "Použité zdroje",
      noEvidence: "Backend pro tuto odpověď nevrátil žádné viditelné zdroje.",
      traceLabel: "trace_id",
      reviewCandidateLabel: "Nová epizoda ke kontrole",
      lackOfEvidenceLabel: "Bez potvrzené opory v dostupné paměti",
      youLabel: "Vy",
      sourceFallbackPrefix: "Zdroj",
      suggestions: [
        "Kde jsi žila v dětství?",
        "Babičko, dnes je mi těžko.",
        "Pamatuješ si, jak jsi mi zpívala před spaním?",
      ],
      greeting:
        "Jsem Eva. Ptej se na to, co je opravdu uložené v mé paměti. Když si nebudu jistá, řeknu to.",
    },
    features: {
      kicker: "Co se uchovává",
      title: "Paměť není jen textové pole. Je to systém vztahů, důkazů a hlasu.",
      items: [
        {
          title: "Rodinné epizody",
          description: "Každá nová vzpomínka vzniká jako kandidát, ne jako automatická pravda.",
          points: ["fronta kontroly", "schválení vlastníkem", "auditní stopa"],
        },
        {
          title: "Ověřený chat",
          description: "Avatar odpovídá jen z toho, co backend dovolí použít jako potvrzenou paměť.",
          points: ["retrieval", "guardrails", "trace id"],
        },
        {
          title: "Vícejazyčné vrstvy",
          description: "Čeština, ruština a angličtina mají vlastní UI i vlastní textové verze obsahu.",
          points: ["lokalizované UI", "oddělené texty", "stavy překladu"],
        },
        {
          title: "Hlas a persona",
          description: "Rodina určuje, jak má avatar znít, v jakém věku a s jakou mírou jemnosti.",
          points: ["předvolba hlasu", "povaha", "zapamatovaný věk"],
        },
        {
          title: "Indexace až po schválení",
          description: "Do živé paměti se nic nedostane bez výslovné kontroly a indexačního kroku.",
          points: ["promotion", "index gating", "privacy scope"],
        },
        {
          title: "Dlouhodobá udržitelnost",
          description: "Architektura odděluje obsah, vrstvu zobrazení a API, aby šla bezpečně dál rozšiřovat.",
          points: ["typovaný obsah", "bezpečné chyby", "paralelní trasa v2"],
        },
      ],
    },
    architecture: {
      kicker: "Jak to proudí",
      title: "Paměť prochází přesně definovaným řetězcem, ne volnou improvizací modelu.",
      items: [
        { name: "Vzpomínky", detail: "fotky, text, hlas, rodinné epizody" },
        { name: "Kontrola", detail: "kontrola vlastníkem a více perspektiv" },
        { name: "Index", detail: "jen schválené a povolené položky" },
        { name: "Retrieval", detail: "zdroje pro konkrétní odpověď" },
        { name: "Guardrails", detail: "řekni nevím, když chybí důkaz" },
        { name: "Avatar", detail: "hlas, výraz a odpověď pro rodinu" },
      ],
    },
    timeline: {
      kicker: "Život v čase",
      title: "Časová osa je čitelná i na mobilu a připravená na napojení archivních médií.",
      actionLabel: "Otevřít rodinnou kontrolu",
      badgeLabel: "Archivní vrstva",
      items: [
        {
          year: 1948,
          title: "Začátek příběhu",
          description: "Původ rodinné vzpomínky: místa, hlas a první vazby, které se později skládají do avatara.",
          media: ["fotografie", "původ místa"],
          slotTitle: "Rodinné zdroje",
          slotBody: "Tato vrstva je připravená na skutečná média a metadata z archivu.",
        },
        {
          year: 1972,
          title: "Svatba a nová rodina",
          description: "Události, které se často vracejí v rodinných otázkách, potřebují jasnou verzi a více zdrojů.",
          media: ["dopis", "vyprávění", "fotografie"],
          slotTitle: "Více perspektiv",
          slotBody: "Když se rodinné verze rozcházejí, workflow je drží odděleně a přiznaně.",
        },
        {
          year: 1989,
          title: "Historické momenty",
          description: "Veřejná historie dává kontext, ale avatar ji nesmí zaměnit za osobní rodinný fakt.",
          media: ["kontext", "časová stopa"],
          slotTitle: "Důkaz před stylem",
          slotBody: "Design zvýrazňuje rok a souvislost, ale backend rozhoduje, co je podloženo.",
        },
        {
          year: 1995,
          title: "Silná rodinná epizoda",
          description: "Konkrétní rodinné vzpomínky bývají nejcennější a zároveň nejcitlivější na hallucination.",
          media: ["cesta", "oslava", "hlas"],
          slotTitle: "Kontrolovaná epizoda",
          slotBody: "Nové verze stejné epizody jdou zpět do kontroly místo přepisování historie.",
        },
        {
          year: 2018,
          title: "Zralá rodinná paměť",
          description: "Pozdní vzpomínky často kombinují cit, humor a retrospektivu. UI je musí nést bez sentimentálního kýče.",
          media: ["video", "projev"],
          slotTitle: "Připraveno pro média",
          slotBody: "Karty jsou navržené pro pozdější připojení fotek, videa i přepisů.",
        },
        {
          year: 2026,
          title: "Živý avatar",
          description: "Teprve po schválení, překladu a indexaci se paměť může bezpečně vrátit do odpovědí avatara.",
          media: ["chat", "kontrola", "indexace"],
          slotTitle: "Napojené workflow",
          slotBody: "Z této stránky lze přejít do reálné kontroly a zkontrolovat celý tok end to end.",
        },
      ],
    },
    studio: {
      kicker: "Studio avatara",
      title: "Prezentační vrstva je oddělená od reálné aplikace, ale připravená na budoucí napojení.",
      lead:
        "Studio zatím slouží jako produktový konfigurátor. Nenastírá zapisování do backendu, ale drží datový model čistý a připravený pro budoucí API.",
      voiceLabel: "Hlas",
      temperamentLabel: "Povaha",
      languageLabel: "Jazyk",
      ageLabel: "Zapamatovaný věk",
      ageHint: "Věk, ve kterém má avatar působit. Hodnota se mění jen lokálně v tomto náhledu.",
      previewNote: "Toto je pouze frontendový konfigurační náhled. Reálné workflow zůstává ve stávajících cestách.",
      launchLabel: "Pokračovat do živého chatu",
      presets: {
        voices: ["Původní nahrávka", "Vřelý tón", "Mladší verze"],
        temperaments: ["Jemná", "Humorná", "Přemýšlivá"],
        languages: ["Čeština", "Русский", "English"],
        defaultAge: 62,
        previewName: "Eva",
        previewTagline: "Rodina určuje způsob návratu, ne model sám.",
      },
    },
    moments: {
      kicker: "Pro jaké chvíle to je",
      title: "Produkt má smysl tehdy, když je užitečný v konkrétním rodinném momentu.",
      actionLabel: "Otevřít chat",
      badgeLabel: "Archivní vrstva",
      items: [
        {
          id: "daughter-advice",
          slotTitle: "Rada bez fabulace",
          slotBody: "Když si avatar není jistý, má to říct. To je důležitější než plynulost.",
          quote: "„Babičko, co bys mi poradila dnes?“",
          caption: "Užitečný avatar musí umět být blízko a zároveň fakticky disciplinovaný.",
        },
        {
          id: "shared-history",
          slotTitle: "Rodinná historie",
          slotBody: "Více generací potřebuje přístup ke stejnému příběhu bez přepisování detailů.",
          quote: "„Pověz mi znovu, jak to tehdy bylo.“",
          caption: "Workflow kontroly drží sporné nebo nové verze mimo potvrzenou paměť, dokud nejsou schválené.",
        },
        {
          id: "voice-return",
          slotTitle: "Návrat hlasu",
          slotBody: "Důležitá není jen odpověď, ale i důvěra, že zní jako někdo skutečný.",
          quote: "„Chtěla jsem znovu slyšet její hlas.“",
          caption: "Design drží klidný, světelný tón bez levných sci-fi efektů a bez přetížení na mobilu.",
        },
      ],
    },
    footer: {
      title: "Nový frontend je připravený běžet paralelně, bez přepisu současného produktu.",
      body:
        "Můžete ho nasadit jako testovací cestu, porovnat s aktuální zkušeností a teprve potom rozhodnout o přepnutí domovské stránky.",
      primaryCta: "Otevřít v2 chat",
      secondaryCta: "Otevřít rodinnou kontrolu",
      note: "Tailwind + TypeScript + Next App Router · mobile-first · bezpečné napojení na stávající backend",
    },
  },
  ru: {
    brand: {
      name: "Eternal World",
      accent: "Вечный мир",
    },
    localeNames: {
      cs: "Čeština",
      ru: "Русский",
      en: "English",
    },
    navigation: {
      links: [
        { id: "story", label: "История" },
        { id: "demo", label: "Живое демо" },
        { id: "architecture", label: "Архитектура" },
        { id: "timeline", label: "Линия времени" },
        { id: "studio", label: "Студия" },
        { id: "moments", label: "Моменты" },
      ],
      openWorkspace: "Открыть чат",
      switchLanguage: "Сменить язык",
    },
    hero: {
      kicker: "Цифровая семейная память",
      title: "Некоторые голоса должны оставаться точными, доверенными и доступными даже спустя годы.",
      lead:
        "Новый frontend строит продукт вокруг доверия: аватар отвечает из сохранённой памяти, отправляет новые эпизоды в семейную проверку и только потом допускает их в живую память.",
      primaryCta: "Открыть чат с аватаром",
      secondaryCta: "Показать живое демо",
      trustLine: "Подключено к текущему чату, workflow проверки и презентации. Существующие продуктовые маршруты не меняются.",
      routeLabel: "Подключённый модуль",
      workspaceLinks: [
        {
          href: "/fa-chat",
          label: "Чат с аватаром",
          description: "Реальный backend endpoint для ответов, trace id и доказательной панели.",
        },
        {
          href: "/family-memory-review",
          label: "Семейная проверка",
          description: "Проверка владельцем, языковые версии, индексация и состояния workflow.",
        },
        {
          href: "/presentation",
          label: "Продуктовая презентация",
          description: "Презентационный режим без вмешательства в рабочий поток.",
        },
      ],
    },
    conversation: {
      kicker: "Подключённое demo",
      title: "Тот же backend, новая frontend-оболочка",
      lead:
        "Этот блок больше не играет локальный симулированный чат. Он отправляет вопросы в существующий demo API и показывает ответ, trace, доказательства и возможный новый эпизод для проверки.",
      connectedBadge: "Подключённое API",
      shellTitle: "Ева Новакова",
      shellSubtitle: "Тёплый семейный аватар · подтверждённая память",
      placeholder: "Напишите Еве вопрос или тёплое сообщение...",
      send: "Отправить",
      loading: "Ева готовит ответ...",
      genericError: "Не удалось получить ответ. Попробуйте ещё раз.",
      responseError: "Сервер вернул некорректный ответ. Проверьте контракт backend.",
      networkError: "Не удалось связаться с сервером. Проверьте подключение.",
      emptyTitle: "Начните с проверяемого вопроса",
      emptyBody:
        "Спрашивайте о детстве, семейных связях или конкретном воспоминании. Если опоры нет, система должна признать это и создать кандидата в очередь проверки.",
      evidenceTitle: "Использованные источники",
      noEvidence: "Backend не вернул видимые источники для этого ответа.",
      traceLabel: "trace_id",
      reviewCandidateLabel: "Новый эпизод на проверку",
      lackOfEvidenceLabel: "Нет подтверждённой опоры в доступной памяти",
      youLabel: "Вы",
      sourceFallbackPrefix: "Источник",
      suggestions: [
        "Где ты жила в детстве?",
        "Бабушка, мне сегодня тяжело.",
        "Ты помнишь, как пела мне перед сном?",
      ],
      greeting:
        "Я Ева. Спрашивай о том, что действительно хранится в моей памяти. Если я не уверена, я скажу это прямо.",
    },
    features: {
      kicker: "Что сохраняется",
      title: "Память не равна одному текстовому полю. Это система связей, доказательств и голоса.",
      items: [
        {
          title: "Семейные эпизоды",
          description: "Каждое новое воспоминание сначала становится кандидатом, а не автоматической истиной.",
          points: ["очередь проверки", "подтверждение владельца", "аудитный след"],
        },
        {
          title: "Проверяемый чат",
          description: "Аватар отвечает только из того, что backend разрешил использовать как подтверждённую память.",
          points: ["retrieval", "guardrails", "trace id"],
        },
        {
          title: "Многоязычные слои",
          description: "Чешский, русский и английский имеют собственный UI и отдельные текстовые версии контента.",
          points: ["локализованный UI", "раздельные тексты", "состояния перевода"],
        },
        {
          title: "Голос и персона",
          description: "Семья определяет, как должен звучать аватар, в каком возрасте и с какой мягкостью.",
          points: ["настройка голоса", "характер", "возраст в памяти"],
        },
        {
          title: "Индексация только после подтверждения",
          description: "В живую память ничего не попадает без явной проверки и шага индексации.",
          points: ["promotion", "index gating", "privacy scope"],
        },
        {
          title: "Долгосрочная поддерживаемость",
          description: "Архитектура разделяет контент, слой отображения и API, чтобы продукт можно было спокойно расширять.",
          points: ["типизированный контент", "безопасные ошибки", "параллельный маршрут v2"],
        },
      ],
    },
    architecture: {
      kicker: "Как это течёт",
      title: "Память проходит по явной цепочке, а не через свободную импровизацию модели.",
      items: [
        { name: "Воспоминания", detail: "фото, текст, голос, семейные эпизоды" },
        { name: "Проверка", detail: "проверка владельцем и разные перспективы" },
        { name: "Индекс", detail: "только подтверждённые и разрешённые записи" },
        { name: "Retrieval", detail: "источники для конкретного ответа" },
        { name: "Guardrails", detail: "скажи 'не знаю', если нет доказательств" },
        { name: "Аватар", detail: "голос, выражение и ответ для семьи" },
      ],
    },
    timeline: {
      kicker: "Жизнь во времени",
      title: "Линия времени читается и на мобильном, и готова к подключению архивных медиа.",
      actionLabel: "Открыть семейную проверку",
      badgeLabel: "Архивный слой",
      items: [
        {
          year: 1948,
          title: "Начало истории",
          description: "Источник семейной памяти: места, голос и первые связи, из которых позже собирается аватар.",
          media: ["фотографии", "место"],
          slotTitle: "Семейные источники",
          slotBody: "Этот слой готов к реальным медиа и метаданным из архива.",
        },
        {
          year: 1972,
          title: "Свадьба и новая семья",
          description: "События, к которым семья возвращается чаще всего, требуют ясной версии и нескольких источников.",
          media: ["письмо", "рассказ", "фотографии"],
          slotTitle: "Несколько перспектив",
          slotBody: "Когда семейные версии расходятся, workflow хранит их раздельно и честно.",
        },
        {
          year: 1989,
          title: "Исторический контекст",
          description: "Общая история добавляет фон, но аватар не должен путать её с личным семейным фактом.",
          media: ["контекст", "временная метка"],
          slotTitle: "Доказательство выше стиля",
          slotBody: "Дизайн подчёркивает год и связь, но backend решает, что действительно подтверждено.",
        },
        {
          year: 1995,
          title: "Сильный семейный эпизод",
          description: "Конкретные семейные воспоминания особенно ценны и особенно чувствительны к hallucination.",
          media: ["поездка", "праздник", "голос"],
          slotTitle: "Контролируемый эпизод",
          slotBody: "Новые версии одного и того же эпизода возвращаются на проверку вместо переписывания истории.",
        },
        {
          year: 2018,
          title: "Зрелая семейная память",
          description: "Поздние воспоминания часто сочетают чувство, юмор и ретроспективу. UI должен нести это без дешёвой сентиментальности.",
          media: ["видео", "тост"],
          slotTitle: "Готово для медиа",
          slotBody: "Карточки спроектированы под будущие фотографии, видео и расшифровки.",
        },
        {
          year: 2026,
          title: "Живой аватар",
          description: "Только после подтверждения, перевода и индексации память может безопасно вернуться в ответы аватара.",
          media: ["чат", "проверка", "индексация"],
          slotTitle: "Подключённый workflow",
          slotBody: "С этой страницы можно перейти в реальную проверку и проверить поток end to end.",
        },
      ],
    },
    studio: {
      kicker: "Студия аватара",
      title: "Презентационный слой отделён от реального приложения, но готов к будущему API-подключению.",
      lead:
        "Пока studio работает как product configurator. Она не делает вид, что пишет в backend, но держит модель данных чистой и готовой к расширению.",
      voiceLabel: "Голос",
      temperamentLabel: "Характер",
      languageLabel: "Язык",
      ageLabel: "Возраст в памяти",
      ageHint: "Возраст, в котором аватар должен восприниматься. Значение меняется только локально в этом preview-режиме.",
      previewNote: "Это только frontend preview-конфигуратор. Реальный workflow остаётся в текущих маршрутах.",
      launchLabel: "Перейти в живой чат",
      presets: {
        voices: ["Оригинальная запись", "Тёплый тон", "Более молодая версия"],
        temperaments: ["Мягкая", "С юмором", "Задумчивая"],
        languages: ["Русский", "Čeština", "English"],
        defaultAge: 62,
        previewName: "Ева",
        previewTagline: "Семья определяет форму возвращения, а не модель сама по себе.",
      },
    },
    moments: {
      kicker: "Ради каких моментов это нужно",
      title: "Продукт важен тогда, когда он помогает в конкретном семейном моменте.",
      actionLabel: "Открыть чат",
      badgeLabel: "Архивный слой",
      items: [
        {
          id: "daughter-advice",
          slotTitle: "Совет без выдумки",
          slotBody: "Если аватар не уверен, он должен сказать это. Это важнее гладкости.",
          quote: "«Бабушка, что бы ты посоветовала мне сегодня?»",
          caption: "Полезный аватар должен быть рядом и при этом сохранять фактическую дисциплину.",
        },
        {
          id: "shared-history",
          slotTitle: "Общая история семьи",
          slotBody: "Нескольким поколениям нужен доступ к одной истории без переписывания деталей.",
          quote: "«Расскажи ещё раз, как это было тогда.»",
          caption: "Workflow проверки держит спорные или новые версии вне подтверждённой памяти, пока они не одобрены.",
        },
        {
          id: "voice-return",
          slotTitle: "Возвращение голоса",
          slotBody: "Важно не только содержание ответа, но и доверие к тому, что это звучит как живой человек.",
          quote: "«Я просто хотела снова услышать её голос.»",
          caption: "Дизайн держит спокойный световой тон без дешёвого sci-fi и без перегруза на мобильном.",
        },
      ],
    },
    footer: {
      title: "Новый frontend готов идти параллельно, не переписывая текущий продукт.",
      body:
        "Можно выкатить его как тестовый маршрут, сравнить с текущим опытом и только потом решать, переключать ли homepage.",
      primaryCta: "Открыть v2 чат",
      secondaryCta: "Открыть семейную проверку",
      note: "Tailwind + TypeScript + Next App Router · mobile-first · безопасное подключение к существующему backend",
    },
  },
  en: {
    brand: {
      name: "Eternal World",
      accent: "Eternal memory",
    },
    localeNames: {
      cs: "Čeština",
      ru: "Русский",
      en: "English",
    },
    navigation: {
      links: [
        { id: "story", label: "Story" },
        { id: "demo", label: "Live demo" },
        { id: "architecture", label: "Architecture" },
        { id: "timeline", label: "Timeline" },
        { id: "studio", label: "Studio" },
        { id: "moments", label: "Moments" },
      ],
      openWorkspace: "Open chat",
      switchLanguage: "Switch language",
    },
    hero: {
      kicker: "Digital family memory",
      title: "Some voices should remain precise, trusted, and reachable for years.",
      lead:
        "This new frontend centers the product around trust: the avatar answers from preserved memory, routes new episodes into family review, and only then lets them become part of live memory.",
      primaryCta: "Open avatar chat",
      secondaryCta: "Show live demo",
      trustLine: "Connected to the current chat, review workflow, and presentation. Existing product routes remain unchanged.",
      routeLabel: "Connected route",
      workspaceLinks: [
        {
          href: "/fa-chat",
          label: "Avatar chat",
          description: "Real backend endpoint for answers, trace ids, and evidence signals.",
        },
        {
          href: "/family-memory-review",
          label: "Family review",
          description: "Owner review, language variants, indexing, and workflow states.",
        },
        {
          href: "/presentation",
          label: "Product presentation",
          description: "Pitch view without disturbing the current working flow.",
        },
      ],
    },
    conversation: {
      kicker: "Connected demo",
      title: "The same backend, a new frontend shell",
      lead:
        "This section no longer plays a local fake chat. It sends questions to the existing demo API and renders the reply, trace, evidence, and any review candidate the backend returns.",
      connectedBadge: "Live API",
      shellTitle: "Eva Novakova",
      shellSubtitle: "Warm family avatar · verified memory",
      placeholder: "Write Eva a question or a warm message...",
      send: "Send",
      loading: "Eva is preparing an answer...",
      genericError: "The answer could not be retrieved. Try again.",
      responseError: "The server returned an invalid response. Check the backend contract.",
      networkError: "The server could not be reached. Check the connection.",
      emptyTitle: "Start with a verifiable question",
      emptyBody:
        "Ask about childhood, family ties, or a concrete memory. If supporting evidence is missing, the system should say so and create a review candidate instead of improvising.",
      evidenceTitle: "Evidence used",
      noEvidence: "The backend did not return visible evidence for this answer.",
      traceLabel: "trace_id",
      reviewCandidateLabel: "New episode for review",
      lackOfEvidenceLabel: "No confirmed support in the available memory set",
      youLabel: "You",
      sourceFallbackPrefix: "Source",
      suggestions: [
        "Where did you live as a child?",
        "Grandma, today feels heavy.",
        "Do you remember singing to me before bed?",
      ],
      greeting:
        "I am Eva. Ask about what is truly stored in my memory. If I am not sure, I should say that clearly.",
    },
    features: {
      kicker: "What gets preserved",
      title: "Memory is not a single text field. It is a system of relationships, evidence, and voice.",
      items: [
        {
          title: "Family episodes",
          description: "Every new memory begins as a candidate, not as automatic truth.",
          points: ["review queue", "owner approval", "audit trail"],
        },
        {
          title: "Verified chat",
          description: "The avatar answers only from what the backend allows as confirmed memory.",
          points: ["retrieval", "guardrails", "trace id"],
        },
        {
          title: "Multilingual layers",
          description: "Czech, Russian, and English each run with their own interface and content version.",
          points: ["localized UI", "separate copy", "translation states"],
        },
        {
          title: "Voice and persona",
          description: "Families choose how the avatar should sound, at what remembered age, and with what temperament.",
          points: ["voice preset", "temperament", "remembered age"],
        },
        {
          title: "Approval before indexing",
          description: "Nothing enters live memory without explicit review and an indexing step.",
          points: ["promotion", "index gating", "privacy scope"],
        },
        {
          title: "Long-term maintainability",
          description: "The architecture keeps content, view logic, and the API layer separate for future growth.",
          points: ["typed content", "safe failures", "parallel v2 route"],
        },
      ],
    },
    architecture: {
      kicker: "How it flows",
      title: "Memory moves through an explicit chain, not through model improvisation.",
      items: [
        { name: "Memories", detail: "photos, text, voice, family episodes" },
        { name: "Review", detail: "owner approval and multiple perspectives" },
        { name: "Index", detail: "only approved and allowed entries" },
        { name: "Retrieval", detail: "sources for a specific answer" },
        { name: "Guardrails", detail: "say 'I do not know' when evidence is missing" },
        { name: "Avatar", detail: "voice, expression, and reply for the family" },
      ],
    },
    timeline: {
      kicker: "A life in time",
      title: "The timeline reads cleanly on mobile and is ready for real archive media.",
      actionLabel: "Open family review",
      badgeLabel: "Archive layer",
      items: [
        {
          year: 1948,
          title: "The story begins",
          description: "The origin of family memory: places, voice, and the first ties that later shape the avatar.",
          media: ["photos", "place"],
          slotTitle: "Family sources",
          slotBody: "This layer is ready for real media and archive metadata.",
        },
        {
          year: 1972,
          title: "Marriage and new family",
          description: "Events that families revisit most often need a clear version and multiple sources.",
          media: ["letter", "story", "photos"],
          slotTitle: "Multiple perspectives",
          slotBody: "When family versions diverge, the workflow keeps them separate and explicit.",
        },
        {
          year: 1989,
          title: "Historical context",
          description: "Public history adds context, but the avatar must not confuse it with personal family fact.",
          media: ["context", "time marker"],
          slotTitle: "Evidence over style",
          slotBody: "The design highlights year and connection, but the backend decides what is supported.",
        },
        {
          year: 1995,
          title: "A strong family episode",
          description: "Concrete family memories are both the most valuable and the most sensitive to hallucination.",
          media: ["trip", "celebration", "voice"],
          slotTitle: "Controlled episode",
          slotBody: "New versions of the same episode go back to review instead of rewriting history.",
        },
        {
          year: 2018,
          title: "Mature family memory",
          description: "Late memories often mix warmth, humor, and retrospect. The interface should carry that without sentimentality.",
          media: ["video", "toast"],
          slotTitle: "Ready for media",
          slotBody: "The cards are prepared for real photos, video, and transcript material later.",
        },
        {
          year: 2026,
          title: "Live avatar",
          description: "Only after approval, translation, and indexing can memory safely return to avatar answers.",
          media: ["chat", "review", "indexing"],
          slotTitle: "Connected workflow",
          slotBody: "From this page you can jump into the live review flow and inspect the full path end to end.",
        },
      ],
    },
    studio: {
      kicker: "Avatar studio",
      title: "The presentation layer is separate from the live workflow, but ready for future API wiring.",
      lead:
        "For now the studio acts as a product configurator. It does not pretend to write into the backend, but it keeps the data model clean and ready for extension.",
      voiceLabel: "Voice",
      temperamentLabel: "Temperament",
      languageLabel: "Language",
      ageLabel: "Remembered age",
      ageHint: "The age the avatar should project. This value changes only inside this preview.",
      previewNote: "This is a frontend preview configurator only. The live workflow remains in the current routes.",
      launchLabel: "Continue to live chat",
      presets: {
        voices: ["Original recording", "Warm tone", "Younger version"],
        temperaments: ["Gentle", "Witty", "Thoughtful"],
        languages: ["English", "Čeština", "Русский"],
        defaultAge: 62,
        previewName: "Eva",
        previewTagline: "The family should define the return, not the model on its own.",
      },
    },
    moments: {
      kicker: "What this is for",
      title: "The product matters only when it helps in a real family moment.",
      actionLabel: "Open chat",
      badgeLabel: "Archive layer",
      items: [
        {
          id: "daughter-advice",
          slotTitle: "Advice without invention",
          slotBody: "If the avatar is unsure, it should say so. That matters more than smoothness.",
          quote: '"Grandma, what would you tell me today?"',
          caption: "A useful avatar needs to feel close while remaining factually disciplined.",
        },
        {
          id: "shared-history",
          slotTitle: "Shared family history",
          slotBody: "Multiple generations need access to the same story without silent rewrites.",
          quote: '"Tell me again how it really happened."',
          caption: "The review workflow keeps disputed or newly proposed versions out of confirmed memory until they are approved.",
        },
        {
          id: "voice-return",
          slotTitle: "The return of a voice",
          slotBody: "What matters is not just the answer, but trust that it sounds like someone real.",
          quote: '"I just wanted to hear her voice again."',
          caption: "The design keeps a calm luminous tone without cheap sci-fi effects or mobile overload.",
        },
      ],
    },
    footer: {
      title: "The new frontend is ready to run in parallel without rewriting the current product.",
      body:
        "You can ship it as a test route, compare it against the current experience, and only then decide whether to switch the homepage.",
      primaryCta: "Open the v2 chat shell",
      secondaryCta: "Open family review",
      note: "Tailwind + TypeScript + Next App Router · mobile-first · safe connection to the existing backend",
    },
  },
};

export function getV2ExperienceContent(locale: AppLocale): V2ExperienceContent {
  return CONTENT[locale];
}

export function getV2Route(locale: AppLocale): string {
  return `/${locale}/v2`;
}

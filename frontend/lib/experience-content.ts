import type { AppLocale } from "./i18n/locales";

export type PresentationSlide = {
  kicker: string;
  title: string;
  body: string;
  accent: string;
};

export type ExperienceContent = {
  brand: string;
  header: {
    story: string;
    process: string;
    trust: string;
    presentation: string;
    chat: string;
    review: string;
  };
  hero: {
    eyebrow: string;
    title: string;
    lead: string;
    primaryCta: string;
    secondaryCta: string;
    trustLine: string;
    evidenceTitle: string;
    evidenceSources: string[];
    noEvidenceTitle: string;
    noEvidenceBody: string;
  };
  problem: {
    title: string;
    intro: string;
    losses: string[];
  };
  steps: {
    title: string;
    items: Array<{
      step: string;
      title: string;
      body: string;
      bullets: string[];
    }>;
  };
  showcase: {
    title: string;
    intro: string;
    chat: {
      title: string;
      questionLabel: string;
      question: string;
      answerLabel: string;
      answer: string;
      evidenceLabel: string;
      evidence: string[];
      unknownQuestion: string;
      unknownAnswer: string;
    };
    review: {
      title: string;
      columns: string[];
      rows: Array<[string, string, string, string]>;
      footer: string;
    };
    directives: {
      title: string;
      values: Array<{ label: string; value: string }>;
      note: string;
    };
  };
  trust: {
    title: string;
    cards: Array<{ title: string; body: string }>;
  };
  multilingual: {
    title: string;
    body: string;
    cards: Array<{ language: string; line: string }>;
    note: string;
  };
  mission: {
    title: string;
    body: string;
    waitlist: string;
    contact: string;
    trustLine: string;
  };
  presentation: {
    title: string;
    body: string;
    openFullScreen: string;
    usage: string;
    backHome: string;
  };
  slides: PresentationSlide[];
};

const content: Record<AppLocale, ExperienceContent> = {
  cs: {
    brand: "Eternal World",
    header: {
      story: "Příběh",
      process: "Jak funguje",
      trust: "Důvěra",
      presentation: "Prezentace",
      chat: "Live chat",
      review: "Rodinná kontrola",
    },
    hero: {
      eyebrow: "Důstojné uchování rodinné paměti",
      title: "Mluvte s avatarem, který odpovídá jen z ověřených rodinných vzpomínek.",
      lead:
        "Eternal World uchovává hlas, moudrost a příběhy blízkého člověka pro další generace. Každá odpověď stojí na rodinou schválených dokumentech, fotografiích, nahrávkách a vzpomínkách. Když důkaz chybí, avatar to poctivě přizná.",
      primaryCta: "Vyzkoušet avatar chat",
      secondaryCta: "Otevřít pitch prezentaci",
      trustLine:
        "Jádro produktu: žádné smyšlené vzpomínky, jasné citace zdrojů, soukromé rodinné prostory, JWT autentizace a hashovaná hesla.",
      evidenceTitle: "Ukázka důkazu za odpovědí",
      evidenceSources: [
        "Rozhovor s Evou Novákovou, 14. března 2018",
        "Rodinný příběh schválený Annou a Petrem",
        "Fotografie: brněnská knihovna, 1967",
      ],
      noEvidenceTitle: "Ochrana proti fabulaci",
      noEvidenceBody:
        "„Nemám potvrzenou vzpomínku ani rodinou schválený zdroj, který by to dokazoval.“",
    },
    problem: {
      title: "Co rodiny časem ztrácejí",
      intro:
        "Nejde jen o data. Mizí tón hlasu, výraz tváře, kontext starých fotografií i věty, které nikdy nikdo nestačil zapsat.",
      losses: [
        "hlasy a rytmus řeči",
        "rodinné příběhy a detaily",
        "výrazy, gesta a drobné zvyky",
        "moudrost předávaná mezi generacemi",
        "kontext starých dopisů a fotografií",
        "vzpomínky, které nikdy nevznikly jako formální archiv",
      ],
    },
    steps: {
      title: "Jak systém pracuje s pravdou",
      items: [
        {
          step: "Krok 1",
          title: "Sbírejte rodinné materiály",
          body: "Dokumenty, fotografie, hlasové nahrávky, videa, dopisy, zprávy, vyprávění i rozhovory se ukládají do jednoho rodinného archivu.",
          bullets: ["fotografie a alba", "dopisy a zprávy", "audio a video", "rozhovory a rodinné historky"],
        },
        {
          step: "Krok 2",
          title: "Rodina doplní a schválí detaily",
          body: "Každý příspěvek prochází workflow od čekající kontroly přes doplnění detailů až po schválení, odmítnutí nebo spor.",
          bullets: ["čeká na kontrolu", "doplňují se detaily", "připraveno ke kontrole", "schváleno / odmítnuto / sporné / indexováno"],
        },
        {
          step: "Krok 3",
          title: "AI používá jen ověřenou pravdu",
          body: "RAG vrací pouze schválené materiály. Neschválené nebo sporné vzpomínky nejsou vydávány za fakta.",
          bullets: ["ověřené důkazy", "transparentní citace", "žádné domýšlení"],
        },
        {
          step: "Krok 4",
          title: "Avatar odpovídá s citací",
          body: "Odpověď působí přirozeně, ale je svázaná s důkazem. Pokud důkaz není, systém to přizná místo vytváření fikce.",
          bullets: ["evidence preview", "lack_of_evidence guard", "emoční vrstva bez změny faktů"],
        },
      ],
    },
    showcase: {
      title: "Dvě propojené produktové zkušenosti",
      intro:
        "Marketingový web vysvětluje filozofii produktu. Živá aplikace ukazuje, jak chat, rodinná kontrola a evidence fungují nad stejným backendem.",
      chat: {
        title: "Chat s avatarem",
        questionLabel: "Otázka",
        question: "Babičko, co si pamatuješ na svou první práci?",
        answerLabel: "Odpověď",
        answer:
          "Pracovala jsem v malé knihovně v Brně, když mi bylo jednadvacet. První den jsem byla nervózní, protože jsem ještě neuměla pracovat s katalogizačním systémem.",
        evidenceLabel: "Důkaz",
        evidence: [
          "Interview recording, 14 March 2018",
          "Family story approved by Anna and Petr",
          "Photograph: Brno library, 1967",
        ],
        unknownQuestion: "Navštívila jsi někdy Japonsko?",
        unknownAnswer: "Nemám potvrzenou vzpomínku ani rodinou schválený zdroj, že jsem Japonsko navštívila.",
      },
      review: {
        title: "Rodinná fronta ke kontrole",
        columns: ["Stav", "Přispěvatel", "Typ důkazu", "Datum"],
        rows: [
          ["Waiting for review", "Anna", "Voice note", "12 Jul"],
          ["Adding details", "Petr", "Photo + note", "13 Jul"],
          ["Ready for review", "Klára", "Interview transcript", "14 Jul"],
          ["Indexed", "Owner", "Approved memory", "15 Jul"],
        ],
        footer: "Konečné rozhodnutí má vlastník avatara nebo pověřený člen rodiny.",
      },
      directives: {
        title: "Emoční a hlasová vrstva",
        values: [
          { label: "emoce", value: "warm nostalgic" },
          { label: "výraz", value: "gentle smile" },
          { label: "pohled", value: "soft focus" },
          { label: "hlava", value: "small nod" },
          { label: "tempo", value: "measured" },
          { label: "hlas", value: "warm, low" },
        ],
        note: "Tyto direktivy mění projev, nikdy ne faktický obsah odpovědi.",
      },
    },
    trust: {
      title: "Důvěra, soukromí a rodinná kontrola",
      cards: [
        {
          title: "Souhlas a vlastnictví",
          body: "Rodina rozhoduje, co se stane součástí paměti avatara, a může kdykoli materiály odstranit nebo celý avatar smazat.",
        },
        {
          title: "Bez vymyšlených vzpomínek",
          body: "Lack-of-evidence guard je produktová zásada. Pokud neexistuje opora ve zdrojích, avatar odpoví, že to neví.",
        },
        {
          title: "Transparentní evidence",
          body: "Každá odpověď může otevřít konkrétní zdroj: dokument, fotografii, rozhovor nebo rodinné schválení.",
        },
        {
          title: "Bezpečné oddělení dat",
          body: "Soukromé rodinné prostory, oddělení demo a produkčních dat, JWT autentizace a hashovaná hesla chrání citlivý obsah.",
        },
      ],
    },
    multilingual: {
      title: "Jedna rodinná paměť, více jazyků",
      body:
        "Platforma podporuje češtinu, ruštinu a angličtinu. Každý člen rodiny může mluvit vlastním jazykem a stále pracovat nad stejnými ověřenými vzpomínkami.",
      cards: [
        { language: "Čeština", line: "Babičko, proč jsi měla tolik ráda knihovnu v Brně?" },
        { language: "Русский", line: "Бабушка, что ты больше всего любила в той библиотеке?" },
        { language: "English", line: "Grandma, what felt special about that library?" },
      ],
      note: "Architektura je připravená i pro další jazyky, ale význam i důkaz zůstávají konzistentní.",
    },
    mission: {
      title: "Uchovejte příběhy, které by rodina neměla ztratit.",
      body:
        "Eternal World není sci-fi o vzkříšení. Je to citlivý rodinný archiv, který uchovává lásku, hlas a moudrost tak, aby s nimi šlo mluvit pravdivě a důstojně.",
      waitlist: "Přidat se na waitlist",
      contact: "Kontaktovat tým",
      trustLine: "Soukromí, kontrola rodiny a pravdivost odpovědí jsou součást produktu od první vrstvy až po API.",
    },
    presentation: {
      title: "Pitch deck / scrollytelling",
      body:
        "Kratší, dramatičtější zkušenost pro klientské demo nebo investorskou prezentaci. Ovládejte ji klávesnicí, scrollováním nebo dotykem.",
      openFullScreen: "Otevřít celou prezentaci",
      usage: "Použijte šipky, scroll nebo swipe. Progress bar ukazuje příběhový oblouk.",
      backHome: "Zpět na produktový web",
    },
    slides: [
      {
        kicker: "Slide 1",
        title: "Co zmizí, když čas běží dál?",
        body: "Hlasy, nedořečené věty, kontext za starými fotografiemi i drobná rodinná moudrost, která nikdy nebyla zapsaná.",
        accent: "fading photographs / unfinished stories",
      },
      {
        kicker: "Slide 2",
        title: "Eternal World uchovává skutečné příběhy, ne iluzi vzkříšení.",
        body: "Je to živý rodinný archiv s konverzačním rozhraním, který chrání pravdivost i souhlas rodiny.",
        accent: "not resurrection / dignified preservation",
      },
      {
        kicker: "Slide 3",
        title: "Nejdřív sběr, potom ověření, až pak hlas avatara.",
        body: "Rodina nahraje materiály, doplní detaily a schválí, co je pravda. Teprve potom může avatar použít danou vzpomínku v odpovědi.",
        accent: "collect -> review -> answer",
      },
      {
        kicker: "Slide 4",
        title: "Rozdíl je v důkazu.",
        body: "Evidence-backed odpovědi, poctivé přiznání neznalosti, emoční vrstva bez změny faktů a rodinná kontrola každého kroku.",
        accent: "no fabrication",
      },
      {
        kicker: "Slide 5",
        title: "Jedna ověřená paměť může promlouvat ke třem generacím i třem jazykům.",
        body: "Čeština, ruština a angličtina sdílí stejný rodinný archiv i stejný důkaz za odpovědí.",
        accent: "multigenerational / multilingual",
      },
      {
        kicker: "Slide 6",
        title: "Uchovejte příběhy, které by vaše rodina neměla ztratit.",
        body: "Eternal World spojuje citlivý produktový design, rodinnou správu pravdy a backend připravený na skutečné použití.",
        accent: "privacy / control / truthfulness",
      },
    ],
  },
  ru: {
    brand: "Eternal World",
    header: {
      story: "История",
      process: "Как это работает",
      trust: "Доверие",
      presentation: "Презентация",
      chat: "Живой чат",
      review: "Семейная проверка",
    },
    hero: {
      eyebrow: "Бережное сохранение семейной памяти",
      title: "Общайтесь с аватаром, который отвечает только из подтверждённых семейных воспоминаний.",
      lead:
        "Eternal World сохраняет голос, мудрость и истории близкого человека для будущих поколений. Каждый ответ опирается на подтверждённые семьёй документы, фотографии, записи и рассказы. Когда доказательства нет, аватар честно это признаёт.",
      primaryCta: "Открыть чат с аватаром",
      secondaryCta: "Открыть pitch-презентацию",
      trustLine:
        "Основа продукта: никаких вымышленных воспоминаний, прозрачные ссылки на источники, приватные семейные пространства, JWT-аутентификация и хешированные пароли.",
      evidenceTitle: "Пример доказательства за ответом",
      evidenceSources: [
        "Запись интервью с Евой Новаковой, 14 марта 2018",
        "Семейная история, подтверждённая Анной и Петром",
        "Фотография: библиотека в Брно, 1967",
      ],
      noEvidenceTitle: "Защита от выдумок",
      noEvidenceBody:
        "«У меня нет подтверждённого воспоминания или семейно одобренного источника, который это доказывает.»",
    },
    problem: {
      title: "Что семьи теряют со временем",
      intro:
        "Исчезают не только данные. Уходят интонация голоса, выражение лица, контекст старых фотографий и фразы, которые никто не успел записать.",
      losses: [
        "голоса и темп речи",
        "семейные истории и детали",
        "мимика, жесты и маленькие привычки",
        "мудрость, передававшаяся между поколениями",
        "контекст старых писем и фотографий",
        "воспоминания, которые так и не стали формальным архивом",
      ],
    },
    steps: {
      title: "Как система работает с правдой",
      items: [
        {
          step: "Шаг 1",
          title: "Соберите семейные материалы",
          body: "Документы, фотографии, голосовые записи, видео, письма, сообщения, рассказы и интервью собираются в единый семейный архив.",
          bullets: ["фотографии и альбомы", "письма и сообщения", "аудио и видео", "интервью и семейные истории"],
        },
        {
          step: "Шаг 2",
          title: "Семья дополняет и подтверждает детали",
          body: "Каждый вклад проходит путь от ожидания проверки через добавление деталей к утверждению, отклонению или спорному статусу.",
          bullets: ["ожидает проверки", "добавляются детали", "готово к проверке", "подтверждено / отклонено / спорно / проиндексировано"],
        },
        {
          step: "Шаг 3",
          title: "AI использует только подтверждённую правду",
          body: "RAG возвращает только утверждённые материалы. Неподтверждённые и спорные воспоминания не выдаются за факты.",
          bullets: ["подтверждённые доказательства", "прозрачные цитаты", "никаких догадок"],
        },
        {
          step: "Шаг 4",
          title: "Аватар отвечает с опорой на источник",
          body: "Ответ звучит естественно, но остаётся связанным с доказательством. Если доказательства нет, система говорит об этом вместо создания вымысла.",
          bullets: ["evidence preview", "lack_of_evidence guard", "эмоциональный слой без изменения фактов"],
        },
      ],
    },
    showcase: {
      title: "Два связанных продуктовых опыта",
      intro:
        "Маркетинговый сайт объясняет философию продукта. Живое приложение показывает, как чат, семейная проверка и доказательства работают над тем же backend.",
      chat: {
        title: "Чат с аватаром",
        questionLabel: "Вопрос",
        question: "Бабушка, что ты помнишь о своей первой работе?",
        answerLabel: "Ответ",
        answer:
          "Я работала в маленькой библиотеке в Брно, когда мне был двадцать один год. В первый день я очень волновалась, потому что ещё не умела пользоваться системой каталогов.",
        evidenceLabel: "Доказательство",
        evidence: [
          "Interview recording, 14 March 2018",
          "Family story approved by Anna and Petr",
          "Photograph: Brno library, 1967",
        ],
        unknownQuestion: "Ты когда-нибудь была в Японии?",
        unknownAnswer: "У меня нет подтверждённого воспоминания или семейно утверждённого источника, что я была в Японии.",
      },
      review: {
        title: "Семейная очередь на проверку",
        columns: ["Статус", "Участник", "Тип доказательства", "Дата"],
        rows: [
          ["Waiting for review", "Anna", "Voice note", "12 Jul"],
          ["Adding details", "Petr", "Photo + note", "13 Jul"],
          ["Ready for review", "Klára", "Interview transcript", "14 Jul"],
          ["Indexed", "Owner", "Approved memory", "15 Jul"],
        ],
        footer: "Финальное решение всегда остаётся за владельцем аватара или уполномоченным членом семьи.",
      },
      directives: {
        title: "Эмоциональный и голосовой слой",
        values: [
          { label: "эмоция", value: "warm nostalgic" },
          { label: "выражение", value: "gentle smile" },
          { label: "взгляд", value: "soft focus" },
          { label: "голова", value: "small nod" },
          { label: "темп", value: "measured" },
          { label: "голос", value: "warm, low" },
        ],
        note: "Эти директивы меняют подачу, но никогда не меняют фактическое содержание ответа.",
      },
    },
    trust: {
      title: "Доверие, приватность и контроль семьи",
      cards: [
        {
          title: "Согласие и владение",
          body: "Семья решает, что станет частью памяти аватара, и в любой момент может удалить материалы или сам аватар.",
        },
        {
          title: "Без придуманных воспоминаний",
          body: "Lack-of-evidence guard является принципом продукта. Если источников нет, аватар честно говорит, что не знает.",
        },
        {
          title: "Прозрачная evidence",
          body: "За каждым ответом можно открыть конкретный источник: документ, фотографию, интервью или семейное подтверждение.",
        },
        {
          title: "Безопасное разделение данных",
          body: "Приватные семейные пространства, разделение demo и production данных, JWT-аутентификация и хешированные пароли защищают чувствительный контент.",
        },
      ],
    },
    multilingual: {
      title: "Одна семейная память, несколько языков",
      body:
        "Платформа поддерживает чешский, русский и английский. Каждый член семьи может говорить на своём языке и всё равно опираться на тот же подтверждённый архив.",
      cards: [
        { language: "Čeština", line: "Babičko, proč jsi měla tolik ráda knihovnu v Brně?" },
        { language: "Русский", line: "Бабушка, что тебе больше всего нравилось в той библиотеке?" },
        { language: "English", line: "Grandma, what felt special about that library?" },
      ],
      note: "Архитектура готова и для других языков, но смысл и доказательная база остаются едиными.",
    },
    mission: {
      title: "Сохраните истории, которые семья не должна потерять.",
      body:
        "Eternal World не про фантастику и воскрешение. Это бережный семейный архив, который сохраняет любовь, голос и мудрость так, чтобы с ними можно было говорить честно и достойно.",
      waitlist: "Присоединиться к waitlist",
      contact: "Связаться с командой",
      trustLine: "Приватность, семейный контроль и правдивость ответов встроены в продукт от интерфейса до API.",
    },
    presentation: {
      title: "Pitch deck / scrollytelling",
      body:
        "Более короткий и эмоциональный опыт для клиентского демо или инвесторской презентации. Управление клавиатурой, скроллом и жестами.",
      openFullScreen: "Открыть полную презентацию",
      usage: "Используйте стрелки, скролл или свайп. Индикатор прогресса показывает развитие истории.",
      backHome: "Вернуться на продуктовый сайт",
    },
    slides: [
      {
        kicker: "Slide 1",
        title: "Что исчезает, когда время идёт дальше?",
        body: "Голоса, недосказанные фразы, контекст старых фотографий и маленькая семейная мудрость, которую никто не успел записать.",
        accent: "fading photographs / unfinished stories",
      },
      {
        kicker: "Slide 2",
        title: "Eternal World сохраняет реальные истории, а не иллюзию воскрешения.",
        body: "Это живой семейный архив с разговорным интерфейсом, который защищает правду и согласие семьи.",
        accent: "not resurrection / dignified preservation",
      },
      {
        kicker: "Slide 3",
        title: "Сначала сбор, потом проверка, и только затем голос аватара.",
        body: "Семья загружает материалы, дополняет детали и подтверждает правду. Только после этого аватар может использовать воспоминание в ответе.",
        accent: "collect -> review -> answer",
      },
      {
        kicker: "Slide 4",
        title: "Разница в доказательстве.",
        body: "Evidence-backed ответы, честное признание незнания, эмоциональный слой без изменения фактов и семейный контроль каждого шага.",
        accent: "no fabrication",
      },
      {
        kicker: "Slide 5",
        title: "Одно подтверждённое воспоминание может говорить с тремя поколениями и на трёх языках.",
        body: "Чешский, русский и английский разделяют один семейный архив и один и тот же источник правды.",
        accent: "multigenerational / multilingual",
      },
      {
        kicker: "Slide 6",
        title: "Сохраните истории, которые ваша семья не должна потерять.",
        body: "Eternal World соединяет деликатный продуктовый дизайн, семейное управление правдой и backend, уже готовый к реальному использованию.",
        accent: "privacy / control / truthfulness",
      },
    ],
  },
  en: {
    brand: "Eternal World",
    header: {
      story: "Story",
      process: "How It Works",
      trust: "Trust",
      presentation: "Presentation",
      chat: "Live Chat",
      review: "Family Review",
    },
    hero: {
      eyebrow: "A dignified way to preserve family memory",
      title: "Speak with an avatar that answers only from verified family memories.",
      lead:
        "Eternal World preserves the voice, wisdom, and stories of a loved one for future generations. Every answer is grounded in family-approved documents, photographs, recordings, and memories. When evidence is missing, the avatar says so honestly.",
      primaryCta: "Open avatar chat",
      secondaryCta: "Open pitch presentation",
      trustLine:
        "Core product rule: no fabricated memories, clear evidence citations, private family spaces, JWT authentication, and hashed passwords.",
      evidenceTitle: "Example of evidence behind an answer",
      evidenceSources: [
        "Interview recording with Eva Novakova, March 14, 2018",
        "Family story approved by Anna and Petr",
        "Photograph: Brno library, 1967",
      ],
      noEvidenceTitle: "Hallucination guard",
      noEvidenceBody:
        "\"I do not have a confirmed memory or a family-approved source showing that.\"",
    },
    problem: {
      title: "What families gradually lose",
      intro:
        "The loss is not only archival. Families lose voices, expressions, context behind old photographs, and wisdom that was never formally written down.",
      losses: [
        "voices and speaking rhythm",
        "stories and fine-grained details",
        "expressions, gestures, and quiet habits",
        "wisdom passed between generations",
        "context behind letters and photographs",
        "memories that never became a formal archive",
      ],
    },
    steps: {
      title: "How the system treats truth",
      items: [
        {
          step: "Step 1",
          title: "Collect family materials",
          body: "Documents, photos, voice recordings, videos, letters, messages, stories, and interviews flow into one family archive.",
          bullets: ["photographs and albums", "letters and messages", "audio and video", "interviews and family stories"],
        },
        {
          step: "Step 2",
          title: "Family members review and add detail",
          body: "Every contribution moves through a workflow from waiting for review to adding details to approval, rejection, dispute, and indexing.",
          bullets: ["waiting for review", "adding details", "ready for review", "approved / rejected / disputed / indexed"],
        },
        {
          step: "Step 3",
          title: "AI uses verified truth only",
          body: "RAG retrieves only approved materials. Unapproved or disputed memories are never presented as verified fact.",
          bullets: ["verified evidence", "transparent citations", "no guessing"],
        },
        {
          step: "Step 4",
          title: "The avatar answers with evidence",
          body: "The answer feels natural, but it stays tied to supporting evidence. When evidence does not exist, the system says so instead of inventing a story.",
          bullets: ["evidence preview", "lack_of_evidence guard", "emotional layer without factual drift"],
        },
      ],
    },
    showcase: {
      title: "Two connected product experiences",
      intro:
        "The marketing site explains the philosophy. The live product workspace shows how chat, family review, and evidence run on the same backend contract.",
      chat: {
        title: "Avatar conversation",
        questionLabel: "Question",
        question: "Grandma, what do you remember about your first job?",
        answerLabel: "Answer",
        answer:
          "I worked in a small library in Brno when I was twenty-one. I remember feeling nervous on my first day because I had never used the cataloguing system before.",
        evidenceLabel: "Evidence",
        evidence: [
          "Interview recording, 14 March 2018",
          "Family story approved by Anna and Petr",
          "Photograph: Brno library, 1967",
        ],
        unknownQuestion: "Did you ever visit Japan?",
        unknownAnswer: "I do not have any confirmed memory or family-approved source showing that I visited Japan.",
      },
      review: {
        title: "Family memory review queue",
        columns: ["Status", "Contributor", "Evidence type", "Date"],
        rows: [
          ["Waiting for review", "Anna", "Voice note", "12 Jul"],
          ["Adding details", "Petr", "Photo + note", "13 Jul"],
          ["Ready for review", "Klára", "Interview transcript", "14 Jul"],
          ["Indexed", "Owner", "Approved memory", "15 Jul"],
        ],
        footer: "The final decision stays with the avatar owner or an authorized family member.",
      },
      directives: {
        title: "Emotion and voice layer",
        values: [
          { label: "emotion", value: "warm nostalgic" },
          { label: "expression", value: "gentle smile" },
          { label: "gaze", value: "soft focus" },
          { label: "head", value: "small nod" },
          { label: "pace", value: "measured" },
          { label: "voice", value: "warm, low" },
        ],
        note: "These directives shape delivery, never the factual content.",
      },
    },
    trust: {
      title: "Trust, privacy, and family control",
      cards: [
        {
          title: "Consent and ownership",
          body: "The family decides what becomes part of the avatar's memory and can remove materials or delete the avatar entirely.",
        },
        {
          title: "No invented memories",
          body: "The lack_of_evidence guard is a product rule. If supporting evidence does not exist, the avatar says it does not know.",
        },
        {
          title: "Transparent evidence",
          body: "Every answer can open the specific source behind it: a document, a photograph, an interview, or a family approval trail.",
        },
        {
          title: "Secure data separation",
          body: "Private family spaces, demo/production separation, JWT authentication, and hashed passwords protect sensitive content.",
        },
      ],
    },
    multilingual: {
      title: "One verified archive, many languages",
      body:
        "The platform supports Czech, Russian, and English. Each family member can speak in a preferred language while relying on the same verified memory archive.",
      cards: [
        { language: "Čeština", line: "Babičko, proč jsi měla tolik ráda knihovnu v Brně?" },
        { language: "Русский", line: "Бабушка, что тебе больше всего нравилось в той библиотеке?" },
        { language: "English", line: "Grandma, what felt special about that library?" },
      ],
      note: "The architecture is ready for additional languages while keeping meaning and evidence consistent.",
    },
    mission: {
      title: "Preserve the stories your family should never lose.",
      body:
        "Eternal World is not a resurrection fantasy. It is a sensitive family archive that preserves love, voice, and wisdom so future generations can speak with them truthfully and with dignity.",
      waitlist: "Join the waitlist",
      contact: "Contact the team",
      trustLine: "Privacy, family control, and truthfulness are built into the product from the interface down to the API.",
    },
    presentation: {
      title: "Pitch deck / scrollytelling",
      body:
        "A shorter, more dramatic narrative for client demos or investor conversations. Use the keyboard, scroll wheel, or touch gestures to move through it.",
      openFullScreen: "Open full presentation",
      usage: "Use arrow keys, scroll, or swipe. The progress bar shows the narrative arc.",
      backHome: "Back to the product site",
    },
    slides: [
      {
        kicker: "Slide 1",
        title: "What disappears when time passes?",
        body: "Voices, unfinished stories, the context behind old photographs, and quiet family wisdom that was never written down.",
        accent: "fading photographs / unfinished stories",
      },
      {
        kicker: "Slide 2",
        title: "Eternal World preserves real stories, not the illusion of resurrection.",
        body: "It is a living family archive with a conversational interface that protects truth and family consent.",
        accent: "not resurrection / dignified preservation",
      },
      {
        kicker: "Slide 3",
        title: "First collection, then verification, then the avatar's voice.",
        body: "Families upload materials, add detail, and confirm what is true. Only then can the avatar use that memory in conversation.",
        accent: "collect -> review -> answer",
      },
      {
        kicker: "Slide 4",
        title: "The difference is evidence.",
        body: "Evidence-backed answers, an honest lack-of-evidence guard, an emotionally expressive avatar, and family-controlled approval.",
        accent: "no fabrication",
      },
      {
        kicker: "Slide 5",
        title: "One verified memory can travel across generations and languages.",
        body: "Czech, Russian, and English all rely on the same family archive and the same proof behind the answer.",
        accent: "multigenerational / multilingual",
      },
      {
        kicker: "Slide 6",
        title: "Preserve the stories your family should never lose.",
        body: "Eternal World brings together sensitive product design, family truth workflows, and a backend already wired for real use.",
        accent: "privacy / control / truthfulness",
      },
    ],
  },
};

export function getExperienceContent(locale: AppLocale): ExperienceContent {
  return content[locale];
}

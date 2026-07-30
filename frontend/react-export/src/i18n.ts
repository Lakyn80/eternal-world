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

export const T: Record<Lang, Copy> = {
  en: {
    navCta: 'Create your AI', kicker: 'Digital immortality',
    heroTitle: 'Some stories should never end.',
    heroSub: 'Create your digital memory. Preserve your voice, your face, your memories and your personality — so the people you love can still reach you, forever.',
    btnCreate: 'Create your AI', btnDemo: 'Watch the demo',
    demoKicker: 'Live conversation', demoTitle: 'A conversation that never has to stop',
    demoSub: 'This is Josef — a preserved memory. Ask him anything his family would. Try typing, or tap a question.',
    demoPersona: 'Preserved memory · Brno', demoPlaceholder: 'Ask Josef something…', demoSend: 'Ask',
    listening: 'Listening', speakingSt: 'Speaking',
    greet: "Hello. I'm Josef — or the memory of him. Ask me anything you would have asked him.",
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
    demoSub: 'Tohle je Josef — uchovaná vzpomínka. Zeptejte se ho na cokoli, na co by se ptala jeho rodina.',
    demoPersona: 'Uchovaná vzpomínka · Brno', demoPlaceholder: 'Zeptejte se Josefa…', demoSend: 'Zeptat se',
    listening: 'Naslouchá', speakingSt: 'Mluví',
    greet: 'Dobrý den. Jsem Josef — tedy vzpomínka na něj. Zeptejte se mě na cokoli, na co byste se ptali jeho.',
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
    demoSub: 'Это Йозеф — сохранённая память. Спросите его о чём угодно, как спросила бы его семья.',
    demoPersona: 'Сохранённая память · Брно', demoPlaceholder: 'Спросите Йозефа…', demoSend: 'Спросить',
    listening: 'Слушает', speakingSt: 'Говорит',
    greet: 'Здравствуйте. Я Йозеф — точнее, память о нём. Спросите меня о чём угодно, о чём спросили бы его.',
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

export const EVENTS: Record<Lang, EventT[]> = {
  en: [
    { year: 1948, title: 'Born in Brno', desc: 'In a flat above the bakery on Pekařská street. The whole house smelled of bread until noon.', media: ['3 photos', 'Voice story'] },
    { year: 1966, title: 'First job — typesetter', desc: 'Letters in lead, ink under the fingernails. He set headlines for the morning paper for eleven years.', media: ['2 photos', 'Documents'] },
    { year: 1972, title: 'Married Marie', desc: 'A small wedding, borrowed suit, rain at exactly the right moment. They danced anyway.', media: ['8 photos', 'Voice story', 'Letter'] },
    { year: 1975, title: 'Hana is born', desc: 'His daughter. He said becoming a father was the only day his hands ever shook.', media: ['5 photos'] },
    { year: 1989, title: 'The Velvet November', desc: 'He stood on the square with keys in the cold air, and cried without being ashamed of it.', media: ['1 photo', 'Voice story'] },
    { year: 1995, title: 'The coast in the old Škoda', desc: 'Drove to the sea to celebrate Hana finishing university. Broke down twice. Laughed the whole way.', media: ['12 photos', 'Video'] },
    { year: 2003, title: 'First grandchild', desc: 'He learned to be patient all over again, and claimed he had invented every bedtime story himself.', media: ['9 photos', 'Voice recordings'] },
    { year: 2018, title: 'Golden wedding', desc: 'Fifty years with Marie. His toast was one sentence: "I would do all of it again, including the rain."', media: ['14 photos', 'Video', 'Speech'] },
    { year: 2024, title: 'Memory recorded', desc: 'Three months of conversations, 40 hours of voice, a lifetime of photographs. Josef, preserved.', media: ['Archive', '40h voice'] }
  ],
  cs: [
    { year: 1948, title: 'Narozen v Brně', desc: 'V bytě nad pekárnou na Pekařské. Celý dům do poledne voněl chlebem.', media: ['3 fotky', 'Hlasový příběh'] },
    { year: 1966, title: 'První práce — sazeč', desc: 'Písmena z olova, inkoust za nehty. Jedenáct let sázel titulky ranních novin.', media: ['2 fotky', 'Dokumenty'] },
    { year: 1972, title: 'Svatba s Marií', desc: 'Malá svatba, půjčený oblek, déšť přesně ve správnou chvíli. Stejně tančili.', media: ['8 fotek', 'Hlasový příběh', 'Dopis'] },
    { year: 1975, title: 'Narodila se Hana', desc: 'Jeho dcera. Říkal, že den, kdy se stal otcem, byl jediný, kdy se mu třásly ruce.', media: ['5 fotek'] },
    { year: 1989, title: 'Sametový listopad', desc: 'Stál na náměstí s klíči ve studeném vzduchu a plakal, aniž by se za to styděl.', media: ['1 fotka', 'Hlasový příběh'] },
    { year: 1995, title: 'K moři starou škodovkou', desc: 'Jeli k moři oslavit Haninu promoci. Auto se dvakrát rozbilo. Celou cestu se smáli.', media: ['12 fotek', 'Video'] },
    { year: 2003, title: 'První vnouče', desc: 'Znovu se učil trpělivosti a tvrdil, že všechny pohádky na dobrou noc vymyslel sám.', media: ['9 fotek', 'Nahrávky hlasu'] },
    { year: 2018, title: 'Zlatá svatba', desc: 'Padesát let s Marií. Jeho přípitek měl jednu větu: „Udělal bych to všechno znovu, i s tím deštěm."', media: ['14 fotek', 'Video', 'Projev'] },
    { year: 2024, title: 'Vzpomínka zaznamenána', desc: 'Tři měsíce rozhovorů, 40 hodin hlasu, celý život ve fotografiích. Josef, uchován.', media: ['Archiv', '40 h hlasu'] }
  ],
  ru: [
    { year: 1948, title: 'Родился в Брно', desc: 'В квартире над пекарней на Пекаржской. До полудня весь дом пах хлебом.', media: ['3 фото', 'Голосовая история'] },
    { year: 1966, title: 'Первая работа — наборщик', desc: 'Свинцовые буквы, чернила под ногтями. Одиннадцать лет он набирал заголовки утренних газет.', media: ['2 фото', 'Документы'] },
    { year: 1972, title: 'Свадьба с Марией', desc: 'Маленькая свадьба, одолженный костюм, дождь ровно в нужный момент. Они всё равно танцевали.', media: ['8 фото', 'Голосовая история', 'Письмо'] },
    { year: 1975, title: 'Родилась Гана', desc: 'Его дочь. Он говорил, что день, когда он стал отцом, — единственный, когда у него дрожали руки.', media: ['5 фото'] },
    { year: 1989, title: 'Бархатный ноябрь', desc: 'Он стоял на площади с ключами в холодном воздухе и плакал, не стыдясь этого.', media: ['1 фото', 'Голосовая история'] },
    { year: 1995, title: 'К морю на старой «Шкоде»', desc: 'Поехали к морю отметить диплом Ганы. Машина ломалась дважды. Всю дорогу смеялись.', media: ['12 фото', 'Видео'] },
    { year: 2003, title: 'Первый внук', desc: 'Он заново учился терпению и уверял, что все сказки на ночь придумал сам.', media: ['9 фото', 'Записи голоса'] },
    { year: 2018, title: 'Золотая свадьба', desc: 'Пятьдесят лет с Марией. Его тост был одной фразой: «Я бы повторил всё это снова, включая дождь».', media: ['14 фото', 'Видео', 'Речь'] },
    { year: 2024, title: 'Память записана', desc: 'Три месяца разговоров, 40 часов голоса, целая жизнь в фотографиях. Йозеф — сохранён.', media: ['Архив', '40 ч голоса'] }
  ]
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
  en: ['Čeština', 'English', 'Deutsch'],
  cs: ['Čeština', 'English', 'Deutsch'],
  ru: ['Русский', 'Čeština', 'English']
};

export const MOMENTS: Record<Lang, MomentT[]> = {
  en: [
    { slot: 'moment-1', ph: 'Granddaughter + tablet photo', quote: '"Grandpa, should I take the job in Prague?"', caption: 'A granddaughter asking her AI grandfather for advice — and getting the answer he would truly have given.' },
    { slot: 'moment-2', ph: 'Mother listening photo', quote: '"I just wanted to hear his voice again."', caption: "A mother listening to her father tell the story of 1972, in his own voice, one more time." },
    { slot: 'moment-3', ph: 'Family history photo', quote: '"Tell me about our family, from the beginning."', caption: 'A son tracing the family history through a conversation instead of a document.' }
  ],
  cs: [
    { slot: 'moment-1', ph: 'Fotka: vnučka s tabletem', quote: '„Dědo, mám vzít tu práci v Praze?"', caption: 'Vnučka se ptá svého AI dědečka na radu — a dostává odpověď, kterou by jí opravdu dal.' },
    { slot: 'moment-2', ph: 'Fotka: maminka naslouchá', quote: '„Chtěla jsem jen znovu slyšet jeho hlas."', caption: 'Maminka poslouchá, jak její otec ještě jednou vypráví příběh roku 1972 — svým vlastním hlasem.' },
    { slot: 'moment-3', ph: 'Fotka: rodinná historie', quote: '„Vyprávěj mi o naší rodině. Od začátku."', caption: 'Syn poznává rodinnou historii rozhovorem, ne dokumentem.' }
  ],
  ru: [
    { slot: 'moment-1', ph: 'Фото: внучка с планшетом', quote: '«Дедушка, соглашаться мне на работу в Праге?»', caption: 'Внучка просит совета у своего AI-дедушки — и получает ответ, который он действительно бы дал.' },
    { slot: 'moment-2', ph: 'Фото: мама слушает', quote: '«Я просто хотела ещё раз услышать его голос».', caption: 'Мама слушает, как её отец ещё раз рассказывает историю 1972 года — своим собственным голосом.' },
    { slot: 'moment-3', ph: 'Фото: история семьи', quote: '«Расскажи мне о нашей семье. С самого начала».', caption: 'Сын узнаёт историю семьи из разговора, а не из документа.' }
  ]
};

export const REPLIES: Record<Lang, Replies> = {
  en: {
    childhood: 'I grew up in Brno, in a flat above the bakery on Pekařská street. Summers belonged to the river — I could still tell you how it smelled after rain.',
    y1995: '1995 — the year Hana finished university. We drove to the coast in the old Škoda to celebrate. It broke down twice. We laughed the whole way.',
    advice: "Don't save the good plates for guests. Use them. Almost nothing you're worried about today will matter in ten years — the people will.",
    marie: 'Marie. Fifty years, and the rain at our wedding. I would do all of it again, including the rain.',
    fallback: 'Every question keeps me here a little longer. Ask me about a year, a place, or a person we both love.'
  },
  cs: {
    childhood: 'Vyrostl jsem v Brně, v bytě nad pekárnou na Pekařské. Léta patřila řece — dodnes bych vám popsal, jak voněla po dešti.',
    y1995: 'Rok 1995 — Hana dokončila vysokou školu. Jeli jsme to oslavit k moři starou škodovkou. Dvakrát se rozbila. Celou cestu jsme se smáli.',
    advice: 'Nešetřete sváteční talíře na návštěvy. Používejte je. Skoro nic, čeho se dnes bojíte, nebude za deset let důležité — lidé ano.',
    marie: 'Marie. Padesát let, a ten déšť na naší svatbě. Udělal bych to všechno znovu, i s tím deštěm.',
    fallback: 'Každá otázka mě tu udrží o chvíli déle. Zeptejte se mě na rok, na místo, nebo na člověka, kterého máme oba rádi.'
  },
  ru: {
    childhood: 'Я вырос в Брно, в квартире над пекарней на Пекаржской. Лето принадлежало реке — я и сейчас мог бы рассказать, как она пахла после дождя.',
    y1995: '1995-й — год, когда Гана окончила университет. Мы поехали к морю на старой «Шкоде» это отметить. Она ломалась дважды. Всю дорогу мы смеялись.',
    advice: 'Не берегите праздничные тарелки для гостей. Пользуйтесь ими. Почти ничего из того, о чём вы тревожитесь сегодня, через десять лет не будет важно — а люди будут.',
    marie: 'Мария. Пятьдесят лет, и тот дождь на нашей свадьбе. Я бы повторил всё это снова, включая дождь.',
    fallback: 'Каждый вопрос удерживает меня здесь чуть дольше. Спросите меня о годе, о месте или о человеке, которого мы оба любим.'
  }
};

export const SUGGESTIONS: Record<Lang, string[]> = {
  en: ['Tell me about your childhood.', 'What happened in 1995?', 'What advice would you give me?'],
  cs: ['Vyprávěj mi o svém dětství.', 'Co se stalo v roce 1995?', 'Jakou radu bys mi dal?'],
  ru: ['Расскажи о своём детстве.', 'Что случилось в 1995 году?', 'Какой совет ты бы мне дал?']
};

export function matchReply(lang: Lang, question: string): string {
  const R = REPLIES[lang];
  const s = question.toLowerCase();
  if (/(childhood|dětst|child|grew|vyrost|детств|вырос)/.test(s)) return R.childhood;
  if (/1995/.test(s)) return R.y1995;
  if (/(advice|rad[uy]|advise|совет)/.test(s)) return R.advice;
  if (/(marie|wife|žen|svatb|wedding|manžel|мари|жен|свадьб)/.test(s)) return R.marie;
  return R.fallback;
}

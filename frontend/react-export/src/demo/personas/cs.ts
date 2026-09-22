import type { MarketingDemoPersona } from '../types';

/**
 * Czech homepage demo — universal Western family story (Martin).
 * Non-political milestones; photos under /imgs/fe-imgs/martin-*.png.
 */
export const csMarketingDemo: MarketingDemoPersona = {
  id: 'martin-family-cs',
  displayName: 'Martin',
  birthYear: 1948,
  homePlace: 'město u řeky',
  spouseName: 'Marie',
  copy: {
    demoSub:
      'Tohle je Martin — uchovaná vzpomínka. Zeptejte se ho na cokoli, na co by se ptala jeho rodina.',
    demoPersona: 'Uchovaná vzpomínka · rodinný archiv',
    demoPlaceholder: 'Zeptejte se Martina…',
    greet:
      'Ahoj. Jsem Martin — tak, jak si ho jeho rodina pamatuje. Ptej se mě na cokoli.',
  },
  events: [
    {
      year: 1948,
      title: 'Narození',
      desc: 'První fotka v rodinném albu: malý Martin v náručí rodičů, světlo z okna a tichý úsměv.',
      media: ['3 fotky', 'Hlasový příběh'],
      image: {
        src: '/imgs/fe-imgs/martin-family-hospital.png',
        alt: 'Martin jako novorozenec s rodiči v nemocnici',
      },
    },
    {
      year: 1966,
      title: 'První práce v tiskárně',
      desc: 'Olovo, inkoust za nehty a ranní noviny. Jedenáct let sázel titulky — a byl na tu práci pyšný.',
      media: ['2 fotky', 'Dokumenty'],
      image: {
        src: '/imgs/fe-imgs/martin-print-shop.png',
        alt: 'Martin jako mladý sazeč v tiskárně',
      },
    },
    {
      year: 1972,
      title: 'Svatba s Marií',
      desc: 'Malá svatba, půjčený oblek, déšť přesně ve správnou chvíli. Stejně tančili.',
      media: ['8 fotek', 'Hlasový příběh', 'Dopis'],
      image: {
        src: '/imgs/fe-imgs/martin-wedding.png',
        alt: 'Martin a Marie v den svatby',
      },
    },
    {
      year: 1975,
      title: 'Narodila se Hana',
      desc: 'Jeho dcera. Říkal, že den, kdy se stal otcem, byl jediný, kdy se mu třásly ruce.',
      media: ['5 fotek'],
      image: {
        src: '/imgs/fe-imgs/martin-newborn.png',
        alt: 'Martin a Marie s novorozenou Hanou',
      },
    },
    {
      year: 1989,
      title: 'Rodinné setkání',
      desc: 'Dlouhý stůl, smích přes několik generací a fotografie, které se ještě ten večer založily do alba.',
      media: ['6 fotek', 'Hlasový příběh'],
      image: {
        src: '/imgs/fe-imgs/martin_family.png',
        alt: 'Rodinné setkání u Martina — společný stůl a album',
      },
    },
    {
      year: 1995,
      title: 'Dovolená starým autem',
      desc: 'Jeli k moři oslavit Haninu promoci. Auto se dvakrát rozbilo, ale právě ty neplánované zastávky udělaly z cesty nezapomenutelný výlet.',
      media: ['12 fotek', 'Video'],
      image: {
        src: '/imgs/fe-imgs/martin-road-trip.png',
        alt: 'Martin a Marie na dovolené u moře se starým autem',
      },
    },
    {
      year: 2003,
      title: 'První vnouče',
      desc: 'Znovu se učil trpělivosti a tvrdil, že všechny pohádky na dobrou noc vymyslel sám.',
      media: ['9 fotek', 'Nahrávky hlasu'],
      image: {
        src: '/imgs/fe-imgs/martin-grandchild.png',
        alt: 'Martin s dcerou a prvním vnoučetem',
      },
    },
    {
      year: 2018,
      title: 'Zlatá svatba',
      desc: 'Padesát let s Marií. Jeho přípitek měl jednu větu: „Udělal bych to všechno znovu, i s tím deštěm."',
      media: ['14 fotek', 'Video', 'Projev'],
      image: {
        src: '/imgs/fe-imgs/martin-golden-wedding.png',
        alt: 'Martin a Marie na oslavě zlaté svatby',
      },
    },
    {
      year: 2024,
      title: 'Vzpomínka zaznamenána',
      desc: 'Tři měsíce rozhovorů, 40 hodin hlasu, celý život ve fotografiích. Martin, uchován.',
      media: ['Archiv', '40 h hlasu'],
      image: {
        src: '/imgs/fe-imgs/martin-recording.png',
        alt: 'Martin vypráví rodinné vzpomínky při nahrávání',
      },
    },
  ],
  moments: [
    {
      slot: 'moment-1',
      ph: 'Fotka: vnučka s tabletem',
      quote: '„Dědo, mám vzít tu práci v Praze?"',
      caption:
        'Vnučka se ptá svého AI dědečka na radu — a dostává odpověď, kterou by jí opravdu dal.',
      image: {
        src: '/imgs/vnucka_deda.png',
        alt: 'Vnučka rozmlouvá s digitální vzpomínkou svého dědečka',
      },
    },
    {
      slot: 'moment-2',
      ph: 'Fotka: maminka naslouchá',
      quote: '„Chtěla jsem jen znovu slyšet jeho hlas."',
      caption:
        'Maminka poslouchá, jak její otec ještě jednou vypráví příběh roku 1972 — svým vlastním hlasem.',
      image: {
        src: '/imgs/vnucka.png',
        alt: 'Dcera poslouchá nahrávku hlasu svého otce',
      },
    },
    {
      slot: 'moment-3',
      ph: 'Fotka: rodinná historie',
      quote: '„Vyprávěj mi o naší rodině. Od začátku."',
      caption: 'Syn poznává rodinnou historii rozhovorem, ne dokumentem.',
      image: {
        src: '/imgs/deda.png',
        alt: 'Syn prochází rodinné fotografie s digitální vzpomínkou svého otce',
      },
    },
  ],
  replies: {
    childhood:
      'Vyrůstal jsem ve městě u řeky. V létě jsme byli skoro pořád venku. Po dešti měla tráva úplně zvláštní vůni. Tu si pamatuju dodnes.',
    milestone:
      'Hana promovala. Chtěli jsme to pořádně oslavit, tak jsme sedli do starého auta a vyrazili k moři. Auto se cestou dvakrát porouchalo, ale zpětně jsou právě ty neplánované zastávky jedna z mých nejoblíbenějších vzpomínek.',
    advice:
      'Neodkládej hezké věci na potom. Ani sváteční talíře, ani návštěvu, ani telefonát někomu, koho máš rád. Čas běží rychleji, než si myslíš.',
    spouse:
      'Marie. Padesát let, a ten déšť na naší svatbě. Udělal bych to všechno znovu, i s tím deštěm.',
    fallback:
      'Každá otázka mě tu udrží o chvíli déle. Zeptejte se mě na rok, na místo, nebo na člověka, kterého máme oba rádi.',
  },
  suggestions: [
    'Vyprávěj mi o svém dětství.',
    'Co se stalo v roce 1995?',
    'Jakou radu bys mi dal?',
  ],
  avatarLangs: ['Čeština', 'English', 'Deutsch'],
  matchers: {
    childhood: ['dětst', 'vyrost', 'řek', 'tráv'],
    milestone: ['1995', 'hana', 'auto', 'moře', 'promoc', 'dovolen'],
    advice: ['rad', 'porad'],
    spouse: ['marie', 'marii', 'žen', 'svatb', 'manžel'],
  },
};

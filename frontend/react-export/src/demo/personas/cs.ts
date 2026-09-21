import type { MarketingDemoPersona } from '../types';

/** Czech homepage demo — Czech names, places, and history only. */
export const csMarketingDemo: MarketingDemoPersona = {
  id: 'josef-brno-cs',
  displayName: 'Josef',
  birthYear: 1948,
  homePlace: 'Brno',
  spouseName: 'Marie',
  copy: {
    demoSub:
      'Tohle je Josef — uchovaná vzpomínka. Zeptejte se ho na cokoli, na co by se ptala jeho rodina.',
    demoPersona: 'Uchovaná vzpomínka · Brno',
    demoPlaceholder: 'Zeptejte se Josefa…',
    greet:
      'Ahoj. Jsem Josef — tak, jak si ho jeho rodina pamatuje. Ptej se mě na cokoli.',
  },
  events: [
    {
      year: 1948,
      title: 'Narozen v Brně',
      desc: 'V bytě nad pekárnou na Pekařské. Celý dům do poledne voněl chlebem.',
      media: ['3 fotky', 'Hlasový příběh'],
    },
    {
      year: 1966,
      title: 'První práce — sazeč',
      desc: 'Písmena z olova, inkoust za nehty. Jedenáct let sázel titulky ranních novin.',
      media: ['2 fotky', 'Dokumenty'],
    },
    {
      year: 1972,
      title: 'Svatba s Marií',
      desc: 'Malá svatba, půjčený oblek, déšť přesně ve správnou chvíli. Stejně tančili.',
      media: ['8 fotek', 'Hlasový příběh', 'Dopis'],
    },
    {
      year: 1975,
      title: 'Narodila se Hana',
      desc: 'Jeho dcera. Říkal, že den, kdy se stal otcem, byl jediný, kdy se mu třásly ruce.',
      media: ['5 fotek'],
    },
    {
      year: 1989,
      title: 'Sametový listopad',
      desc: 'Stál na náměstí s klíči ve studeném vzduchu a plakal, aniž by se za to styděl.',
      media: ['1 fotka', 'Hlasový příběh'],
    },
    {
      year: 1995,
      title: 'K moři starou škodovkou',
      desc: 'Jeli k moři oslavit Haninu promoci. Auto se dvakrát rozbilo, ale právě ty neplánované zastávky udělaly z cesty nezapomenutelný výlet.',
      media: ['12 fotek', 'Video'],
      image: {
        src: '/imgs/skodovka.png',
        alt: 'Rodinný výlet k moři se starou škodovkou',
      },
    },
    {
      year: 2003,
      title: 'První vnouče',
      desc: 'Znovu se učil trpělivosti a tvrdil, že všechny pohádky na dobrou noc vymyslel sám.',
      media: ['9 fotek', 'Nahrávky hlasu'],
    },
    {
      year: 2018,
      title: 'Zlatá svatba',
      desc: 'Padesát let s Marií. Jeho přípitek měl jednu větu: „Udělal bych to všechno znovu, i s tím deštěm."',
      media: ['14 fotek', 'Video', 'Projev'],
    },
    {
      year: 2024,
      title: 'Vzpomínka zaznamenána',
      desc: 'Tři měsíce rozhovorů, 40 hodin hlasu, celý život ve fotografiích. Josef, uchován.',
      media: ['Archiv', '40 h hlasu'],
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
      'Vyrůstal jsem v Brně na Pekařské, přímo nad pekárnou. V létě jsme byli skoro pořád u řeky. Po dešti měla úplně zvláštní vůni. Tu si pamatuju dodnes.',
    milestone:
      'Hana promovala. Chtěli jsme to pořádně oslavit, tak jsme sedli do staré škodovky a vyrazili k moři. Auto se cestou dvakrát porouchalo, ale zpětně jsou právě ty neplánované zastávky jedna z mých nejoblíbenějších vzpomínek.',
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
    childhood: ['dětst', 'vyrost', 'brno', 'pekař'],
    milestone: ['1995', 'hana', 'škod', 'skod', 'moře', 'promoc'],
    advice: ['rad', 'porad'],
    spouse: ['marie', 'marii', 'žen', 'svatb', 'manžel'],
  },
};

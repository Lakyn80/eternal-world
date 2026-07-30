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
      'Dobrý den. Jsem Josef — tedy vzpomínka na něj. Zeptejte se mě na cokoli, na co byste se ptali jeho.',
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
      desc: 'Jeli k moři oslavit Haninu promoci. Auto se dvakrát rozbilo. Celou cestu se smáli.',
      media: ['12 fotek', 'Video'],
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
    },
    {
      slot: 'moment-2',
      ph: 'Fotka: maminka naslouchá',
      quote: '„Chtěla jsem jen znovu slyšet jeho hlas."',
      caption:
        'Maminka poslouchá, jak její otec ještě jednou vypráví příběh roku 1972 — svým vlastním hlasem.',
    },
    {
      slot: 'moment-3',
      ph: 'Fotka: rodinná historie',
      quote: '„Vyprávěj mi o naší rodině. Od začátku."',
      caption: 'Syn poznává rodinnou historii rozhovorem, ne dokumentem.',
    },
  ],
  replies: {
    childhood:
      'Vyrostl jsem v Brně, v bytě nad pekárnou na Pekařské. Léta patřila řece — dodnes bych vám popsal, jak voněla po dešti.',
    milestone:
      'Rok 1995 — Hana dokončila vysokou školu. Jeli jsme to oslavit k moři starou škodovkou. Dvakrát se rozbila. Celou cestu jsme se smáli.',
    advice:
      'Nešetřete sváteční talíře na návštěvy. Používejte je. Skoro nic, čeho se dnes bojíte, nebude za deset let důležité — lidé ano.',
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

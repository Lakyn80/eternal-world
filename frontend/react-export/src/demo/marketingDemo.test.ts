import { describe, expect, it } from 'vitest';

import { getMarketingDemo, matchDemoReply, MARKETING_DEMOS } from './index';
import { EVENTS, MOMENTS, SUGGESTIONS, T, matchReply } from '../i18n';

describe('locale-scoped marketing demos', () => {
  it('registers exactly one persona pack per UI language', () => {
    expect(Object.keys(MARKETING_DEMOS).sort()).toEqual(['cs', 'en', 'ru']);
  });

  it('keeps Martin as the Czech demo persona with universal family realia', () => {
    const cs = getMarketingDemo('cs');
    expect(cs.displayName).toBe('Martin');
    expect(cs.homePlace).toMatch(/řek/i);
    const blob = JSON.stringify(cs);
    expect(blob).not.toMatch(/Josef|Pepa|Brno|Pekař|Škod|Sametov/i);
    expect(blob).toMatch(/Martin/);
    expect(cs.events.some((event) => /tiskárn/i.test(event.title))).toBe(true);
    expect(cs.events.some((event) => /Zlatá svatba/i.test(event.title))).toBe(true);
  });

  it('wires Martin family photos into timeline and moments', () => {
    const cs = getMarketingDemo('cs');
    const trip = cs.events.find((event) => event.year === 1995);

    expect(trip?.desc).toBe(
      'Jeli k moři oslavit Haninu promoci. Auto se dvakrát rozbilo, ale právě ty neplánované zastávky udělaly z cesty nezapomenutelný výlet.'
    );
    expect(trip?.image?.src).toBe('/imgs/fe-imgs/martin-road-trip.png');
    expect(cs.replies.milestone).not.toMatch(/Celou cestu jsme se smáli/);
    expect(cs.moments.map((moment) => moment.image?.src)).toEqual([
      '/imgs/vnucka_deda.png',
      '/imgs/vnucka.png',
      '/imgs/deda.png',
    ]);
    expect(cs.copy.greet).toBe(
      'Ahoj. Jsem Martin — tak, jak si ho jeho rodina pamatuje. Ptej se mě na cokoli.'
    );
    expect(cs.replies.childhood).toMatch(/městě u řeky/);
    expect(cs.replies.milestone).toMatch(/Hana promovala/);
    expect(cs.replies.advice).toMatch(/Neodkládej hezké věci na potom/);
    expect(cs.suggestions).toEqual([
      'Vyprávěj mi o svém dětství.',
      'Co se stalo v roce 1995?',
      'Jakou radu bys mi dal?',
    ]);
  });

  it('uses English realia for English — not Martin Czech story', () => {
    const en = getMarketingDemo('en');
    expect(en.displayName).toBe('James');
    expect(en.homePlace).toBe('Manchester');
    const blob = JSON.stringify(en);
    expect(blob).not.toMatch(/Josef|Pepa|Brno|Pekař|Škod|Sametov|Praze|Berlin Wall/i);
    expect(blob).toMatch(/Manchester|Cornwall|Margaret|London/);
  });

  it('uses Russian realia for Russian — not Martin Czech story', () => {
    const ru = getMarketingDemo('ru');
    expect(ru.displayName).toBe('Иван');
    expect(ru.homePlace).toBe('Ленинград');
    const blob = JSON.stringify(ru);
    expect(blob).not.toMatch(/Josef|Pepa|Йозеф|Brno|Брно|Pekař|Škod|Праге|Август девяносто/i);
    expect(blob).toMatch(/Ленинград|Фонтанк|Анна|Москве|Лад/);
  });

  it('switches chrome copy and timeline when the language changes', () => {
    expect(T.cs.greet).toContain('Martin');
    expect(T.en.greet).toContain('James');
    expect(T.ru.greet).toContain('Иван');

    expect(EVENTS.cs[0].title).toMatch(/Narození/i);
    expect(EVENTS.en[0].title).toMatch(/Manchester/i);
    expect(EVENTS.ru[0].title).toMatch(/Ленинград/i);

    expect(MOMENTS.cs[0].quote).toMatch(/Praze/);
    expect(MOMENTS.en[0].quote).toMatch(/London/);
    expect(MOMENTS.ru[0].quote).toMatch(/Москве/);

    expect(SUGGESTIONS.cs[0]).not.toBe(SUGGESTIONS.en[0]);
    expect(SUGGESTIONS.ru[0]).not.toBe(SUGGESTIONS.en[0]);
  });

  it('matches demo replies with locale-specific keywords', () => {
    expect(matchDemoReply('cs', 'Vyprávěj mi o svém dětství.')).toMatch(/řeky/);
    expect(matchReply('en', 'Tell me about your childhood.')).toMatch(/Manchester/);
    expect(matchReply('ru', 'Расскажи о своём детстве.')).toMatch(/Ленинград/);

    expect(matchReply('cs', 'Co říkáš o Marii?')).toMatch(/Marie/);
    expect(matchReply('en', 'Tell me about Margaret')).toMatch(/Margaret/);
    expect(matchReply('ru', 'Расскажи об Анне')).toMatch(/Анна/);
  });
});

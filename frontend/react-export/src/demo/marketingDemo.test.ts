import { describe, expect, it } from 'vitest';

import { getMarketingDemo, matchDemoReply, MARKETING_DEMOS } from './index';
import { EVENTS, MOMENTS, SUGGESTIONS, T, matchReply } from '../i18n';

describe('locale-scoped marketing demos', () => {
  it('registers exactly one persona pack per UI language', () => {
    expect(Object.keys(MARKETING_DEMOS).sort()).toEqual(['cs', 'en', 'ru']);
  });

  it('keeps Czech realia on the Czech pack only', () => {
    const cs = getMarketingDemo('cs');
    expect(cs.displayName).toBe('Josef');
    expect(cs.homePlace).toBe('Brno');
    expect(cs.events[0].title).toMatch(/Brně/i);
    expect(JSON.stringify(cs)).toMatch(/Pekařsk/);
    expect(JSON.stringify(cs)).toMatch(/Sametový/);
  });

  it('shows the supplied Czech family photos with the revised 1995 memory', () => {
    const cs = getMarketingDemo('cs');
    const trip = cs.events.find((event) => event.year === 1995);

    expect(trip?.desc).toBe(
      'Jeli k moři oslavit Haninu promoci. Auto se dvakrát rozbilo, ale právě ty neplánované zastávky udělaly z cesty nezapomenutelný výlet.'
    );
    expect(trip?.image?.src).toBe('/imgs/skodovka.png');
    expect(cs.replies.milestone).not.toMatch(/Celou cestu jsme se smáli/);
    expect(cs.moments.map((moment) => moment.image?.src)).toEqual([
      '/imgs/vnucka_deda.png',
      '/imgs/vnucka.png',
      '/imgs/deda.png',
    ]);
    expect(cs.copy.greet).toBe(
      'Ahoj. Jsem Josef — tak, jak si ho jeho rodina pamatuje. Ptej se mě na cokoli.'
    );
    expect(cs.replies.childhood).toMatch(/Vyrůstal jsem v Brně na Pekařské/);
    expect(cs.replies.milestone).toMatch(/Hana promovala/);
    expect(cs.replies.advice).toMatch(/Neodkládej hezké věci na potom/);
    expect(cs.suggestions).toEqual([
      'Vyprávěj mi o svém dětství.',
      'Co se stalo v roce 1995?',
      'Jakou radu bys mi dal?',
    ]);
  });

  it('uses English realia for English — not Brno/Josef', () => {
    const en = getMarketingDemo('en');
    expect(en.displayName).toBe('James');
    expect(en.homePlace).toBe('Manchester');
    const blob = JSON.stringify(en);
    expect(blob).not.toMatch(/Josef|Brno|Pekař|Škod|Sametov|Praze/i);
    expect(blob).toMatch(/Manchester|Cornwall|Margaret|London/);
  });

  it('uses Russian realia for Russian — not Brno/Josef', () => {
    const ru = getMarketingDemo('ru');
    expect(ru.displayName).toBe('Иван');
    expect(ru.homePlace).toBe('Ленинград');
    const blob = JSON.stringify(ru);
    expect(blob).not.toMatch(/Josef|Йозеф|Brno|Брно|Pekař|Škod|Праге/i);
    expect(blob).toMatch(/Ленинград|Фонтанк|Анна|Москве|Лад/);
  });

  it('switches chrome copy and timeline when the language changes', () => {
    expect(T.cs.greet).toContain('Josef');
    expect(T.en.greet).toContain('James');
    expect(T.ru.greet).toContain('Иван');

    expect(EVENTS.cs[0].title).toMatch(/Brně/i);
    expect(EVENTS.en[0].title).toMatch(/Manchester/i);
    expect(EVENTS.ru[0].title).toMatch(/Ленинград/i);

    expect(MOMENTS.cs[0].quote).toMatch(/Praze/);
    expect(MOMENTS.en[0].quote).toMatch(/London/);
    expect(MOMENTS.ru[0].quote).toMatch(/Москве/);

    expect(SUGGESTIONS.cs[0]).not.toBe(SUGGESTIONS.en[0]);
    expect(SUGGESTIONS.ru[0]).not.toBe(SUGGESTIONS.en[0]);
  });

  it('matches demo replies with locale-specific keywords', () => {
    expect(matchDemoReply('cs', 'Vyprávěj mi o svém dětství.')).toMatch(/Brně/);
    expect(matchReply('en', 'Tell me about your childhood.')).toMatch(/Manchester/);
    expect(matchReply('ru', 'Расскажи о своём детстве.')).toMatch(/Ленинград/);

    expect(matchReply('cs', 'Co říkáš o Marii?')).toMatch(/Marie/);
    expect(matchReply('en', 'Tell me about Margaret')).toMatch(/Margaret/);
    expect(matchReply('ru', 'Расскажи об Анне')).toMatch(/Анна/);
  });
});

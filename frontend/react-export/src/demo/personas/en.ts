import type { MarketingDemoPersona } from '../types';

/** English homepage demo — English-speaking realia only (not a translation of Josef). */
export const enMarketingDemo: MarketingDemoPersona = {
  id: 'james-manchester-en',
  displayName: 'James',
  birthYear: 1948,
  homePlace: 'Manchester',
  spouseName: 'Margaret',
  copy: {
    demoSub:
      'This is James — a preserved memory. Ask him anything his family would. Try typing, or tap a question.',
    demoPersona: 'Preserved memory · Manchester',
    demoPlaceholder: 'Ask James something…',
    greet:
      "Hello. I'm James — or the memory of him. Ask me anything you would have asked him.",
  },
  events: [
    {
      year: 1948,
      title: 'Born in Manchester',
      desc: 'In a terraced house near the canal. The kettle whistled before dawn and the street still smelled of coal smoke.',
      media: ['3 photos', 'Voice story'],
    },
    {
      year: 1966,
      title: 'First job — print compositor',
      desc: 'Lead type, ink under the fingernails. He set headlines for the morning paper for eleven years.',
      media: ['2 photos', 'Documents'],
    },
    {
      year: 1972,
      title: 'Married Margaret',
      desc: 'A small registry wedding, borrowed suit, rain at exactly the right moment. They danced anyway.',
      media: ['8 photos', 'Voice story', 'Letter'],
    },
    {
      year: 1975,
      title: 'Helen is born',
      desc: 'His daughter. He said becoming a father was the only day his hands ever shook.',
      media: ['5 photos'],
    },
    {
      year: 1989,
      title: 'The Berlin Wall falls',
      desc: 'He watched it on the evening news with Helen on his knee, and said the world had just gotten a little wider.',
      media: ['1 photo', 'Voice story'],
    },
    {
      year: 1995,
      title: 'Cornwall in the old Ford',
      desc: 'Drove to the coast to celebrate Helen finishing university. Broke down twice. Laughed the whole way.',
      media: ['12 photos', 'Video'],
    },
    {
      year: 2003,
      title: 'First grandchild',
      desc: 'He learned to be patient all over again, and claimed he had invented every bedtime story himself.',
      media: ['9 photos', 'Voice recordings'],
    },
    {
      year: 2018,
      title: 'Golden wedding',
      desc: 'Fifty years with Margaret. His toast was one sentence: "I would do all of it again, including the rain."',
      media: ['14 photos', 'Video', 'Speech'],
    },
    {
      year: 2024,
      title: 'Memory recorded',
      desc: 'Three months of conversations, 40 hours of voice, a lifetime of photographs. James, preserved.',
      media: ['Archive', '40h voice'],
    },
  ],
  moments: [
    {
      slot: 'moment-1',
      ph: 'Granddaughter + tablet photo',
      quote: '"Grandpa, should I take the job in London?"',
      caption:
        'A granddaughter asking her AI grandfather for advice — and getting the answer he would truly have given.',
    },
    {
      slot: 'moment-2',
      ph: 'Mother listening photo',
      quote: '"I just wanted to hear his voice again."',
      caption:
        'A mother listening to her father tell the story of 1972, in his own voice, one more time.',
    },
    {
      slot: 'moment-3',
      ph: 'Family history photo',
      quote: '"Tell me about our family, from the beginning."',
      caption: 'A son tracing the family history through a conversation instead of a document.',
    },
  ],
  replies: {
    childhood:
      'I grew up in Manchester, in a terraced house near the canal. Summers belonged to the park — I could still tell you how the grass smelled after rain.',
    milestone:
      '1995 — the year Helen finished university. We drove to Cornwall in the old Ford to celebrate. It broke down twice. We laughed the whole way.',
    advice:
      "Don't save the good plates for guests. Use them. Almost nothing you're worried about today will matter in ten years — the people will.",
    spouse:
      'Margaret. Fifty years, and the rain at our wedding. I would do all of it again, including the rain.',
    fallback:
      'Every question keeps me here a little longer. Ask me about a year, a place, or a person we both love.',
  },
  suggestions: [
    'Tell me about your childhood.',
    'What happened in 1995?',
    'What advice would you give me?',
  ],
  avatarLangs: ['English', 'Čeština', 'Deutsch'],
  matchers: {
    childhood: ['childhood', 'grew', 'manchester', 'canal'],
    milestone: ['1995', 'helen', 'cornwall', 'ford', 'university'],
    advice: ['advice', 'advise'],
    spouse: ['margaret', 'wife', 'wedding', 'married'],
  },
};

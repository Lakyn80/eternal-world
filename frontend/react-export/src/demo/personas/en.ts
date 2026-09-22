import type { MarketingDemoPersona } from '../types';

/** English homepage demo — English-speaking realia only (not a translation of Martin). */
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
      image: {
        src: '/imgs/english_verison/james-manchester-1948.png',
        alt: 'James as a newborn with his parents at Manchester Royal Infirmary',
      },
    },
    {
      year: 1966,
      title: 'First job — print compositor',
      desc: 'Lead type, ink under the fingernails. He set headlines for the morning paper for eleven years.',
      media: ['2 photos', 'Documents'],
      image: {
        src: '/imgs/english_verison/james-print-shop-1966.png',
        alt: 'James as a young print compositor at the composing table',
      },
    },
    {
      year: 1972,
      title: 'Married Margaret',
      desc: 'A small registry wedding, borrowed suit, rain at exactly the right moment. They danced anyway.',
      media: ['8 photos', 'Voice story', 'Letter'],
      image: {
        src: '/imgs/english_verison/james-wedding-1972.png',
        alt: 'James and Margaret leaving the church after their wedding',
      },
    },
    {
      year: 1975,
      title: 'Helen is born',
      desc: 'His daughter. He said becoming a father was the only day his hands ever shook.',
      media: ['5 photos'],
      image: {
        src: '/imgs/english_verison/james-helen-1975.png',
        alt: 'James and Margaret with newborn Helen in hospital',
      },
    },
    {
      year: 1989,
      title: 'A long family dinner',
      desc: 'Three generations around one table, leftover cake, and stories that somehow got funnier every year.',
      media: ['6 photos', 'Voice story'],
      image: {
        src: '/imgs/english_verison/james-family-dinner-1989.png',
        alt: 'James and his family around the dinner table in 1989',
      },
    },
    {
      year: 1995,
      title: 'Cornwall in the old Ford',
      desc: 'Drove to the coast to celebrate Helen finishing university. Broke down twice. Laughed the whole way.',
      media: ['12 photos', 'Video'],
      image: {
        src: '/imgs/english_verison/james-cornwall-1995.png',
        alt: 'James, Margaret and Helen by the old Ford on the Cornwall coast',
      },
    },
    {
      year: 2003,
      title: 'First grandchild',
      desc: 'He learned to be patient all over again, and claimed he had invented every bedtime story himself.',
      media: ['9 photos', 'Voice recordings'],
      image: {
        src: '/imgs/english_verison/james-grandchild-2003.png',
        alt: 'James holding his first grandchild with the family around him',
      },
    },
    {
      year: 2018,
      title: 'Golden wedding',
      desc: 'Fifty years with Margaret. His toast was one sentence: "I would do all of it again, including the rain."',
      media: ['14 photos', 'Video', 'Speech'],
      image: {
        src: '/imgs/english_verison/james-golden-wedding-2018.png',
        alt: 'James and Margaret celebrating their golden wedding with family',
      },
    },
    {
      year: 2024,
      title: 'Memory recorded',
      desc: 'Three months of conversations, 40 hours of voice, a lifetime of photographs. James, preserved.',
      media: ['Archive', '40h voice'],
      image: {
        src: '/imgs/english_verison/james-recording-2024.png',
        alt: 'James and Margaret recording family memories at home',
      },
    },
  ],
  moments: [
    {
      slot: 'moment-1',
      ph: 'Granddaughter + tablet photo',
      quote: '"Grandpa, should I take the job in London?"',
      caption:
        'A granddaughter asking her AI grandfather for advice — and getting the answer he would truly have given.',
      image: {
        src: '/imgs/english_verison/english_3pics/james-moment-granddaughter.png',
        alt: 'Granddaughter on a video call with her grandfather about a job offer in London',
      },
    },
    {
      slot: 'moment-2',
      ph: 'Mother listening photo',
      quote: '"I just wanted to hear his voice again."',
      caption:
        'A mother listening to her father tell the story of 1972, in his own voice, one more time.',
      image: {
        src: '/imgs/english_verison/english_3pics/james-moment-mother.png',
        alt: 'Daughter listening to her father’s recorded voice beside an old family photo',
      },
    },
    {
      slot: 'moment-3',
      ph: 'Family history photo',
      quote: '"Tell me about our family, from the beginning."',
      caption: 'A son tracing the family history through a conversation instead of a document.',
      image: {
        src: '/imgs/english_verison/english_3pics/james-moment-son.png',
        alt: 'Son exploring family photographs and a digital memory of his father',
      },
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

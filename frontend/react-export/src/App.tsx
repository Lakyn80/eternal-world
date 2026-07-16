import { useState } from 'react';
import type { Lang } from './i18n';
import Nav from './components/Nav';
import Hero from './components/Hero';
import ConversationDemo from './components/ConversationDemo';
import Features from './components/Features';
import Brain from './components/Brain';
import Timeline from './components/Timeline';
import AvatarStudio from './components/AvatarStudio';
import Moments from './components/Moments';
import Footer from './components/Footer';

const scrollTo = (id: string) => {
  const el = document.getElementById(id);
  if (el) window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 60, behavior: 'smooth' });
};

export default function App() {
  const [lang, setLang] = useState<Lang>('en');

  return (
    <div className="min-h-screen bg-ink text-fg font-sans">
      <Nav lang={lang} setLang={setLang} onGoHero={() => scrollTo('hero')} onGoStudio={() => scrollTo('studio')} />
      <Hero lang={lang} onGoStudio={() => scrollTo('studio')} onGoDemo={() => scrollTo('demo')} particles />
      <ConversationDemo lang={lang} autoplay />
      <Features lang={lang} />
      <Brain lang={lang} />
      <Timeline lang={lang} />
      <AvatarStudio lang={lang} />
      <Moments lang={lang} />
      <Footer lang={lang} onGoStudio={() => scrollTo('studio')} />
    </div>
  );
}

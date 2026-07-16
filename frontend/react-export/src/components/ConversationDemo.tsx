import { useEffect, useRef, useState } from 'react';
import type { Lang } from '../i18n';
import { T, SUGGESTIONS, matchReply } from '../i18n';

interface Message { role: 'ai' | 'user'; text: string; }

interface Props {
  lang: Lang;
  autoplay: boolean;
}

export default function ConversationDemo({ lang, autoplay }: Props) {
  const t = T[lang];
  const [messages, setMessages] = useState<Message[]>([{ role: 'ai', text: t.greet }]);
  const [input, setInput] = useState('');
  const [typing, setTyping] = useState(false);
  const [speaking, setSpeaking] = useState(false);
  const started = useRef(false);

  useEffect(() => {
    setMessages([{ role: 'ai', text: t.greet }]);
  }, [lang]);

  const ask = (q: string) => {
    if (!q.trim()) return;
    setMessages((m) => [...m, { role: 'user', text: q }]);
    setInput('');
    setTyping(true);
    setTimeout(() => {
      setMessages((m) => [...m, { role: 'ai', text: matchReply(lang, q) }]);
      setTyping(false);
      setSpeaking(true);
      setTimeout(() => setSpeaking(false), 3200);
    }, 1100);
  };

  useEffect(() => {
    if (!autoplay || started.current) return;
    started.current = true;
    const timer = setTimeout(() => ask(SUGGESTIONS[lang][0]), 1800);
    return () => clearTimeout(timer);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <section id="demo" className="relative py-28 px-6 flex flex-col items-center">
      <div className="text-xs tracking-[.3em] uppercase text-cyan mb-3.5">{t.demoKicker}</div>
      <h2 className="font-serif font-normal text-[clamp(30px,3.6vw,48px)] text-center max-w-[22ch] mb-2.5">
        {t.demoTitle}
      </h2>
      <p className="text-fg/60 font-light max-w-[52ch] text-center leading-relaxed mb-11">{t.demoSub}</p>

      <div className="flex w-full max-w-[940px] bg-white/[0.035] border border-white/[0.09] rounded-3xl overflow-hidden backdrop-blur-xl shadow-2xl">
        <div
          className="flex-none w-[280px] flex flex-col items-center justify-center gap-5 p-9 border-r border-white/[0.07]"
          style={{ background: 'radial-gradient(circle at 50% 34%, rgba(70,90,200,.25), transparent 70%)' }}
        >
          <div className="relative w-[120px] h-[120px] animate-breathe">
            <div
              className="absolute -inset-[18px] rounded-full animate-halo"
              style={{ background: 'radial-gradient(circle, rgba(110,160,255,.3), transparent 70%)' }}
            />
            <div
              className="absolute inset-0 rounded-full"
              style={{
                background:
                  'radial-gradient(circle at 36% 30%, rgba(210,238,255,.95), rgba(110,170,246,.85) 40%, rgba(88,72,214,.9) 75%, rgba(20,18,60,.95))',
                boxShadow: '0 0 34px rgba(100,160,255,.5)'
              }}
            />
          </div>
          <div className="text-center">
            <div className="font-medium text-[15px]">Josef · 1948</div>
            <div className="text-[12.5px] text-fg/50 mt-0.5">{t.demoPersona}</div>
          </div>
          <div className="flex items-center gap-[3px] h-10">
            {Array.from({ length: 18 }).map((_, i) => (
              <div
                key={i}
                className="w-[3px] h-[34px] rounded origin-center animate-wavebar"
                style={{
                  background: 'linear-gradient(180deg,#7fd8f7,#8b7cf6)',
                  animationDelay: `${(i * 73) % 900}ms`,
                  animationPlayState: speaking ? 'running' : 'paused'
                }}
              />
            ))}
          </div>
          <div className="text-[11.5px] tracking-wider uppercase" style={{ color: speaking ? '#7fd8f7' : 'rgba(233,236,245,.4)' }}>
            {speaking ? t.speakingSt : t.listening}
          </div>
        </div>

        <div className="flex-1 flex flex-col min-h-[460px]">
          <div className="flex-1 flex flex-col gap-3 p-7 overflow-y-auto max-h-[420px]">
            {messages.map((m, i) => (
              <div
                key={i}
                className={`max-w-[78%] px-4.5 py-3 text-[14.5px] leading-relaxed animate-fadein ${
                  m.role === 'user'
                    ? 'self-end rounded-[16px_16px_4px_16px] border border-[rgba(143,214,245,.25)]'
                    : 'self-start rounded-[16px_16px_16px_4px] bg-white/[0.06] border border-white/[0.08] font-light'
                }`}
                style={
                  m.role === 'user'
                    ? { background: 'linear-gradient(135deg,rgba(143,214,245,.22),rgba(139,124,246,.22))' }
                    : undefined
                }
              >
                {m.text}
              </div>
            ))}
            {typing && (
              <div className="self-start px-4.5 py-3 rounded-[16px_16px_16px_4px] bg-white/[0.06] text-fg/50 text-sm animate-fadein">
                ···
              </div>
            )}
          </div>
          <div className="flex gap-2 flex-wrap px-7 pb-3.5">
            {SUGGESTIONS[lang].map((q) => (
              <button
                key={q}
                onClick={() => ask(q)}
                className="font-sans text-xs text-fg/75 bg-white/5 border border-white/[0.13] rounded-full px-3.5 py-1.5 hover:bg-cyan/10 hover:border-cyan/40 transition-colors"
              >
                {q}
              </button>
            ))}
          </div>
          <div className="flex gap-2.5 px-7 py-5 border-t border-white/[0.07]">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && ask(input)}
              placeholder={t.demoPlaceholder}
              className="flex-1 font-sans text-sm text-fg bg-white/5 border border-white/[0.12] rounded-2xl px-4.5 py-3 outline-none focus:border-cyan/50"
            />
            <button
              onClick={() => ask(input)}
              className="font-sans text-sm font-medium text-ink rounded-2xl px-5.5 py-3"
              style={{ background: 'linear-gradient(135deg,#8fd6f5,#8b7cf6)' }}
            >
              {t.demoSend}
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

import { useEffect, useRef } from 'react';

interface Particle { x: number; y: number; r: number; s: number; tw: number; hue: string; }

export function useParticles(enabled: boolean) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const rafRef = useRef<number>();

  useEffect(() => {
    if (!enabled) return;
    const cv = canvasRef.current;
    if (!cv) return;
    const ctx = cv.getContext('2d');
    if (!ctx) return;
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    const size = () => { cv.width = cv.offsetWidth * dpr; cv.height = cv.offsetHeight * dpr; };
    size();
    window.addEventListener('resize', size);

    const particles: Particle[] = Array.from({ length: 110 }, () => ({
      x: Math.random(), y: Math.random(), r: 0.6 + Math.random() * 1.6,
      s: 0.00012 + Math.random() * 0.0004, tw: Math.random() * Math.PI * 2,
      hue: Math.random() < 0.8 ? '150,190,255' : '230,195,120'
    }));

    const loop = (ts: number) => {
      ctx.clearRect(0, 0, cv.width, cv.height);
      for (const p of particles) {
        p.y -= p.s;
        if (p.y < -0.02) { p.y = 1.02; p.x = Math.random(); }
        const a = 0.18 + 0.3 * (0.5 + 0.5 * Math.sin(ts / 900 + p.tw));
        ctx.beginPath();
        ctx.arc(p.x * cv.width, p.y * cv.height, p.r * dpr, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${p.hue},${a})`;
        ctx.fill();
      }
      rafRef.current = requestAnimationFrame(loop);
    };
    rafRef.current = requestAnimationFrame(loop);

    return () => {
      window.removeEventListener('resize', size);
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
    };
  }, [enabled]);

  return canvasRef;
}

import { useEffect, useRef } from "react";

type Particle = {
  x: number;
  y: number;
  radius: number;
  speed: number;
  twinkleOffset: number;
  hue: string;
};

export function useV2Particles(enabled: boolean) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frameRef = useRef<number | null>(null);

  useEffect(() => {
    if (!enabled) {
      return;
    }

    const canvas = canvasRef.current;
    if (!canvas) {
      return;
    }

    const context = canvas.getContext("2d");
    if (!context) {
      return;
    }

    const resize = () => {
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = canvas.clientWidth * ratio;
      canvas.height = canvas.clientHeight * ratio;
    };

    resize();
    const observer = new ResizeObserver(resize);
    observer.observe(canvas);

    const particles: Particle[] = Array.from({ length: 96 }, () => ({
      x: Math.random(),
      y: Math.random(),
      radius: 0.6 + Math.random() * 1.8,
      speed: 0.00008 + Math.random() * 0.00028,
      twinkleOffset: Math.random() * Math.PI * 2,
      hue: Math.random() < 0.82 ? "143, 214, 245" : "232, 195, 122",
    }));

    const render = (timestamp: number) => {
      context.clearRect(0, 0, canvas.width, canvas.height);

      for (const particle of particles) {
        particle.y -= particle.speed;
        if (particle.y < -0.02) {
          particle.y = 1.02;
          particle.x = Math.random();
        }

        const alpha = 0.12 + 0.28 * (0.5 + 0.5 * Math.sin(timestamp / 900 + particle.twinkleOffset));
        context.beginPath();
        context.arc(
          particle.x * canvas.width,
          particle.y * canvas.height,
          particle.radius * Math.min(window.devicePixelRatio || 1, 2),
          0,
          Math.PI * 2
        );
        context.fillStyle = `rgba(${particle.hue}, ${alpha})`;
        context.fill();
      }

      frameRef.current = window.requestAnimationFrame(render);
    };

    frameRef.current = window.requestAnimationFrame(render);

    return () => {
      observer.disconnect();
      if (frameRef.current !== null) {
        window.cancelAnimationFrame(frameRef.current);
      }
    };
  }, [enabled]);

  return canvasRef;
}

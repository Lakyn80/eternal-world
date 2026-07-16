/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        serif: ['"Instrument Serif"', 'serif'],
        sans: ['"Space Grotesk"', 'system-ui', 'sans-serif']
      },
      colors: {
        ink: '#04050b',
        fg: '#e9ecf5',
        cyan: '#7fd8f7',
        violet: '#8b7cf6',
        gold: '#e8c37a'
      },
      keyframes: {
        breathe: { '0%,100%': { transform: 'scale(1)' }, '50%': { transform: 'scale(1.045)' } },
        halo: { '0%,100%': { opacity: '0.55', transform: 'scale(1)' }, '50%': { opacity: '0.9', transform: 'scale(1.08)' } },
        wavebar: { '0%,100%': { transform: 'scaleY(.25)' }, '50%': { transform: 'scaleY(1)' } },
        flowlight: { '0%': { backgroundPosition: '200% 0' }, '100%': { backgroundPosition: '-200% 0' } },
        floaty: { '0%,100%': { transform: 'translateY(0)' }, '50%': { transform: 'translateY(-7px)' } },
        fadein: { from: { opacity: '0', transform: 'translateY(10px)' }, to: { opacity: '1', transform: 'translateY(0)' } }
      },
      animation: {
        breathe: 'breathe 6.5s ease-in-out infinite',
        halo: 'halo 6.5s ease-in-out infinite',
        wavebar: 'wavebar 1.05s ease-in-out infinite',
        flowlight: 'flowlight 2.4s linear infinite',
        floaty: 'floaty 5s ease-in-out infinite',
        fadein: 'fadein .3s ease'
      }
    }
  },
  plugins: []
};

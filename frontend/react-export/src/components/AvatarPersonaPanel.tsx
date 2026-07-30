import { FormEvent, useEffect, useState } from 'react';
import type { Lang } from '../i18n';
import { getAvatarPersonaSettings, MemorialApiError, updateAvatarPersonaSettings } from '../lib/memorialApi';
import type {
  AvatarPersonaLanguage,
  AvatarPersonaSettingsRead,
  AvatarPersonalityTrait,
  AvatarVoiceMode
} from '../types/memorial';

const MAX_COMMUNICATION = 4000;
const TRAITS: AvatarPersonalityTrait[] = ['gentle', 'funny', 'thoughtful'];
const LANGS: AvatarPersonaLanguage[] = ['cs', 'en', 'de'];
const VOICE_MODES: AvatarVoiceMode[] = ['original_recording', 'warm_older', 'younger_self'];

type PersonaCopy = {
  personaTitle: string;
  personaVoice: string;
  personaPersonality: string;
  personaLanguages: string;
  personaAge: string;
  personaAgeHint: string;
  personaCommunicationTitle: string;
  personaCommunicationLabel: string;
  personaCommunicationHelp: string;
  personaCommunicationPlaceholder: string;
  personaSave: string;
  personaSaved: string;
  personaWorking: string;
  traitGentle: string;
  traitFunny: string;
  traitThoughtful: string;
  voiceOriginal: string;
  voiceWarmOlder: string;
  voiceYounger: string;
  langCs: string;
  langEn: string;
  langDe: string;
  primaryLanguage: string;
};

function safeError(error: unknown): string {
  if (error instanceof MemorialApiError) return error.detail || 'Request failed.';
  if (error instanceof Error) return error.message;
  return 'Request failed.';
}

export default function AvatarPersonaPanel({
  token,
  profileId,
  lang,
  t
}: {
  token: string;
  profileId: number;
  lang: Lang;
  t: PersonaCopy;
}) {
  const [settings, setSettings] = useState<AvatarPersonaSettingsRead | null>(null);
  const [traits, setTraits] = useState<AvatarPersonalityTrait[]>([]);
  const [languages, setLanguages] = useState<AvatarPersonaLanguage[]>(['cs']);
  const [primary, setPrimary] = useState<AvatarPersonaLanguage>('cs');
  const [voiceMode, setVoiceMode] = useState<AvatarVoiceMode>('warm_older');
  const [age, setAge] = useState('');
  const [communication, setCommunication] = useState('');
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    getAvatarPersonaSettings(token, profileId)
      .then((data) => {
        if (cancelled) return;
        setSettings(data);
        setTraits(data.personality_traits);
        setLanguages(data.supported_languages);
        setPrimary(data.primary_language);
        setVoiceMode(data.voice_mode);
        setAge(data.remembered_age == null ? '' : String(data.remembered_age));
        setCommunication(data.communication_profile);
      })
      .catch((loadError) => {
        if (!cancelled) setError(safeError(loadError));
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [token, profileId]);

  function toggleTrait(trait: AvatarPersonalityTrait) {
    setTraits((current) => (current.includes(trait) ? current.filter((item) => item !== trait) : [...current, trait]));
  }

  function toggleLanguage(code: AvatarPersonaLanguage) {
    setLanguages((current) => {
      if (current.includes(code)) {
        if (code === primary) return current;
        const next = current.filter((item) => item !== code);
        return next.length === 0 ? current : next;
      }
      return [...current, code];
    });
  }

  async function onSave(event: FormEvent) {
    event.preventDefault();
    if (busy) return;
    const parsedAge = age.trim() === '' ? null : Number(age);
    if (parsedAge !== null && (!Number.isInteger(parsedAge) || parsedAge < 1 || parsedAge > 120)) {
      setError(lang === 'cs' ? 'Zapamatovaný věk musí být 1–120 nebo prázdný.' : 'Remembered age must be 1–120 or empty.');
      return;
    }
    if (communication.length > MAX_COMMUNICATION) {
      setError(lang === 'cs' ? 'Text je příliš dlouhý.' : 'Text is too long.');
      return;
    }
    if (!languages.includes(primary)) {
      setError(lang === 'cs' ? 'Hlavní jazyk musí být mezi podporovanými.' : 'Primary language must stay selected.');
      return;
    }

    setBusy(true);
    setError(null);
    setNotice(null);
    try {
      const saved = await updateAvatarPersonaSettings(token, profileId, {
        voice_mode: voiceMode,
        personality_traits: traits,
        primary_language: primary,
        supported_languages: languages,
        remembered_age: parsedAge,
        communication_profile: communication
      });
      setSettings(saved);
      setTraits(saved.personality_traits);
      setLanguages(saved.supported_languages);
      setPrimary(saved.primary_language);
      setVoiceMode(saved.voice_mode);
      setAge(saved.remembered_age == null ? '' : String(saved.remembered_age));
      setCommunication(saved.communication_profile);
      setNotice(t.personaSaved);
    } catch (saveError) {
      setError(safeError(saveError));
    } finally {
      setBusy(false);
    }
  }

  if (loading) {
    return <p className="text-sm text-fg/55">{t.personaWorking}</p>;
  }

  const traitLabel = (trait: AvatarPersonalityTrait) =>
    trait === 'gentle' ? t.traitGentle : trait === 'funny' ? t.traitFunny : t.traitThoughtful;
  const voiceLabel = (mode: AvatarVoiceMode) =>
    mode === 'original_recording' ? t.voiceOriginal : mode === 'younger_self' ? t.voiceYounger : t.voiceWarmOlder;
  const langLabel = (code: AvatarPersonaLanguage) =>
    code === 'cs' ? t.langCs : code === 'en' ? t.langEn : t.langDe;

  return (
    <form className="mt-8 grid min-w-0 gap-5 rounded-[28px] border border-white/10 bg-black/20 p-4 sm:p-5" onSubmit={onSave}>
      <div>
        <h3 className="font-serif text-2xl">{t.personaTitle}</h3>
        {settings?.original_recording_available === false && (
          <p className="mt-2 text-xs text-fg/45">{t.voiceOriginal}: —</p>
        )}
      </div>

      <div className="grid gap-2">
        <span className="text-xs uppercase tracking-[.18em] text-fg/40">{t.personaVoice}</span>
        <div className="flex flex-wrap gap-2">
          {VOICE_MODES.map((mode) => (
            <button
              className={`rounded-full border px-4 py-2 text-sm ${
                voiceMode === mode ? 'border-cyan/50 bg-cyan/15 text-cyan' : 'border-white/10 text-fg/70'
              } ${mode === 'original_recording' && !settings?.original_recording_available ? 'opacity-40' : ''}`}
              disabled={mode === 'original_recording' && !settings?.original_recording_available}
              key={mode}
              onClick={() => setVoiceMode(mode)}
              type="button"
            >
              {voiceLabel(mode)}
            </button>
          ))}
        </div>
      </div>

      <div className="grid gap-2">
        <span className="text-xs uppercase tracking-[.18em] text-fg/40">{t.personaPersonality}</span>
        <div className="flex flex-wrap gap-2">
          {TRAITS.map((trait) => (
            <button
              className={`rounded-full border px-4 py-2 text-sm ${
                traits.includes(trait) ? 'border-cyan/50 bg-cyan/15 text-cyan' : 'border-white/10 text-fg/70'
              }`}
              key={trait}
              onClick={() => toggleTrait(trait)}
              type="button"
            >
              {traitLabel(trait)}
            </button>
          ))}
        </div>
      </div>

      <div className="grid gap-2">
        <span className="text-xs uppercase tracking-[.18em] text-fg/40">{t.personaLanguages}</span>
        <div className="flex flex-wrap gap-2">
          {LANGS.map((code) => (
            <button
              className={`rounded-full border px-4 py-2 text-sm ${
                languages.includes(code) ? 'border-cyan/50 bg-cyan/15 text-cyan' : 'border-white/10 text-fg/70'
              }`}
              key={code}
              onClick={() => toggleLanguage(code)}
              type="button"
            >
              {langLabel(code)}
            </button>
          ))}
        </div>
        <label className="mt-2 grid gap-1 text-sm text-fg/60">
          <span>{t.primaryLanguage}</span>
          <select
            className="rounded-2xl border border-white/10 bg-ink px-4 py-2.5 text-fg outline-none"
            onChange={(event) => setPrimary(event.target.value as AvatarPersonaLanguage)}
            value={primary}
          >
            {languages.map((code) => (
              <option key={code} value={code}>
                {langLabel(code)}
              </option>
            ))}
          </select>
        </label>
      </div>

      <label className="grid gap-2 text-sm text-fg/62">
        <span>{t.personaAge}</span>
        <input
          className="rounded-2xl border border-white/10 bg-ink px-4 py-3 text-fg outline-none focus:border-cyan/70"
          inputMode="numeric"
          onChange={(event) => setAge(event.target.value)}
          placeholder="62"
          value={age}
        />
        <span className="text-xs text-fg/45">{t.personaAgeHint}</span>
      </label>

      <label className="grid gap-2 text-sm text-fg/62">
        <span className="font-serif text-lg text-fg">{t.personaCommunicationTitle}</span>
        <span>{t.personaCommunicationLabel}</span>
        <textarea
          className="min-h-[140px] rounded-2xl border border-white/10 bg-ink px-4 py-3 text-fg outline-none focus:border-cyan/70"
          maxLength={MAX_COMMUNICATION}
          onChange={(event) => setCommunication(event.target.value)}
          placeholder={t.personaCommunicationPlaceholder}
          value={communication}
        />
        <span className="text-xs text-fg/45">{t.personaCommunicationHelp}</span>
        <span className="text-xs text-fg/40">
          {communication.length}/{MAX_COMMUNICATION}
        </span>
      </label>

      {error && <p className="rounded-2xl border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-100">{error}</p>}
      {notice && <p className="rounded-2xl border border-cyan/25 bg-cyan/10 px-4 py-3 text-sm text-cyan">{notice}</p>}

      <button
        className="rounded-full bg-gradient-to-r from-cyan to-violet px-6 py-3.5 text-sm font-semibold text-ink disabled:opacity-55"
        disabled={busy}
        type="submit"
      >
        {busy ? t.personaWorking : t.personaSave}
      </button>
    </form>
  );
}

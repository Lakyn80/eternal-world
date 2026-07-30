import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import AvatarPersonaPanel from './AvatarPersonaPanel';
import * as api from '../lib/memorialApi';
import type { AvatarPersonaSettingsRead } from '../types/memorial';
import { COPY } from './MemorialWorkspace';

vi.mock('../lib/memorialApi', async () => {
  const actual = await vi.importActual<typeof import('../lib/memorialApi')>('../lib/memorialApi');
  return {
    ...actual,
    getAvatarPersonaSettings: vi.fn(),
    updateAvatarPersonaSettings: vi.fn()
  };
});

const defaults: AvatarPersonaSettingsRead = {
  profile_id: 7,
  voice_mode: 'warm_older',
  voice_style: 'warm',
  personality_traits: [],
  primary_language: 'cs',
  supported_languages: ['cs'],
  remembered_age: null,
  communication_profile: '',
  created_at: null,
  updated_at: null,
  original_recording_available: false,
  voice_provider_supports_style: false,
  voice_provider_supports_age: false
};

describe('AvatarPersonaPanel', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    vi.mocked(api.getAvatarPersonaSettings).mockResolvedValue({ ...defaults });
    vi.mocked(api.updateAvatarPersonaSettings).mockResolvedValue({
      ...defaults,
      personality_traits: ['gentle', 'funny'],
      supported_languages: ['cs', 'en'],
      primary_language: 'cs',
      remembered_age: 62,
      communication_profile: 'Mluvím klidně.'
    });
  });

  it('loads defaults and saves typed persona payload', async () => {
    const user = userEvent.setup();
    render(<AvatarPersonaPanel lang="cs" profileId={7} t={COPY.cs} token="tok" />);

    await waitFor(() => expect(screen.getByText('Hlas')).toBeInTheDocument());
    expect(screen.getByText('Osobnost a způsob komunikace')).toBeInTheDocument();
    expect(screen.getByText('Jak mluvím a reaguji')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Původní nahrávka' })).toBeDisabled();

    await user.click(screen.getByRole('button', { name: 'Jemný' }));
    await user.click(screen.getByRole('button', { name: 'Vtipný' }));
    await user.click(screen.getByRole('button', { name: 'English' }));

    const age = screen.getByPlaceholderText('62');
    await user.clear(age);
    await user.type(age, '62');

    const textarea = screen.getByPlaceholderText(/Mluvím klidně a používám kratší věty/);
    await user.clear(textarea);
    await user.type(textarea, 'Mluvím klidně.');

    await user.click(screen.getByRole('button', { name: 'Uložit personu' }));

    await waitFor(() => expect(api.updateAvatarPersonaSettings).toHaveBeenCalledTimes(1));
    expect(api.updateAvatarPersonaSettings).toHaveBeenCalledWith('tok', 7, {
      voice_mode: 'warm_older',
      personality_traits: ['gentle', 'funny'],
      primary_language: 'cs',
      supported_languages: ['cs', 'en'],
      remembered_age: 62,
      communication_profile: 'Mluvím klidně.'
    });
    expect(await screen.findByText('Nastavení persony uloženo.')).toBeInTheDocument();
  });

  it('rejects out-of-range remembered age without calling the API', async () => {
    const user = userEvent.setup();
    render(<AvatarPersonaPanel lang="cs" profileId={7} t={COPY.cs} token="tok" />);
    await waitFor(() => expect(screen.getByText('Hlas')).toBeInTheDocument());

    const age = screen.getByPlaceholderText('62');
    await user.type(age, '999');
    await user.click(screen.getByRole('button', { name: 'Uložit personu' }));

    expect(api.updateAvatarPersonaSettings).not.toHaveBeenCalled();
    expect(screen.getByText(/Zapamatovaný věk musí být 1–120/)).toBeInTheDocument();
  });

  it('shows character count for communication profile', async () => {
    render(<AvatarPersonaPanel lang="cs" profileId={7} t={COPY.cs} token="tok" />);
    await waitFor(() => expect(screen.getByText('0/4000')).toBeInTheDocument());

    const textarea = screen.getByPlaceholderText(/Mluvím klidně a používám kratší věty/);
    fireEvent.change(textarea, { target: { value: 'abc' } });
    expect(screen.getByText('3/4000')).toBeInTheDocument();
  });

  it('preserves entered text when save fails', async () => {
    vi.mocked(api.updateAvatarPersonaSettings).mockRejectedValueOnce(new Error('Save failed'));
    const user = userEvent.setup();
    render(<AvatarPersonaPanel lang="cs" profileId={7} t={COPY.cs} token="tok" />);
    await waitFor(() => expect(screen.getByText('Hlas')).toBeInTheDocument());

    const textarea = screen.getByPlaceholderText(/Mluvím klidně a používám kratší věty/);
    await user.type(textarea, 'Draft text stays');
    await user.click(screen.getByRole('button', { name: 'Uložit personu' }));

    expect(await screen.findByText('Save failed')).toBeInTheDocument();
    expect(textarea).toHaveValue('Draft text stays');
  });
});

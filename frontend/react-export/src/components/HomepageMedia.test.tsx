import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';

import Moments from './Moments';
import Timeline from './Timeline';

describe('Czech homepage media', () => {
  it('renders the 1995 road-trip photo with the revised memory', () => {
    render(<Timeline lang="cs" />);

    expect(
      screen.getByText(
        'Jeli k moři oslavit Haninu promoci. Auto se dvakrát rozbilo, ale právě ty neplánované zastávky udělaly z cesty nezapomenutelný výlet.'
      )
    ).toBeInTheDocument();
    expect(
      screen.getByRole('img', { name: 'Martin a Marie na dovolené u moře se starým autem' })
    ).toHaveAttribute('src', '/imgs/fe-imgs/martin-road-trip.png');
  });

  it('keeps the original Moments product photos', () => {
    render(<Moments lang="cs" />);

    expect(
      screen.getByRole('img', { name: 'Vnučka rozmlouvá s digitální vzpomínkou svého dědečka' })
    ).toHaveAttribute('src', '/imgs/vnucka_deda.png');
    expect(
      screen.getByRole('img', { name: 'Dcera poslouchá nahrávku hlasu svého otce' })
    ).toHaveAttribute('src', '/imgs/vnucka.png');
    expect(
      screen.getByRole('img', {
        name: 'Syn prochází rodinné fotografie s digitální vzpomínkou svého otce',
      })
    ).toHaveAttribute('src', '/imgs/deda.png');
  });
});

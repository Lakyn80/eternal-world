import { describe, expect, it } from 'vitest';
import { COPY, invitationAcceptErrorMessage } from './MemorialWorkspace';
import { MemorialApiError } from '../lib/memorialApi';

describe('invitationAcceptErrorMessage', () => {
  it('maps the backend email-mismatch detail to localized copy', () => {
    const error = new MemorialApiError(400, 'Invitation email does not match current user');
    expect(invitationAcceptErrorMessage(error, COPY.en)).toBe(COPY.en.invitationEmailMismatch);
    expect(invitationAcceptErrorMessage(error, COPY.cs)).toBe(COPY.cs.invitationEmailMismatch);
    expect(invitationAcceptErrorMessage(error, COPY.ru)).toBe(COPY.ru.invitationEmailMismatch);
  });

  it('falls back to the API detail for other accept failures', () => {
    const error = new MemorialApiError(400, 'Invitation has expired');
    expect(invitationAcceptErrorMessage(error, COPY.en)).toBe('Invitation has expired');
  });
});

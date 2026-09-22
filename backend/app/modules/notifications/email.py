from __future__ import annotations

import smtplib
from email.message import EmailMessage

from app.core.config import settings
from app.core.logging import get_logger


logger = get_logger("notifications.email")


class InvitationEmailDeliveryError(Exception):
    """SMTP (or mail configuration) failed. Safe to show as a generic API error."""


def build_invitation_accept_url(*, token: str) -> str:
    path = f"/invitations/accept?token={token}"
    origin = settings.public_app_origin.strip().rstrip("/")
    if not origin:
        return path
    return f"{origin}{path}"


def send_memorial_invitation_email(
    *,
    to_email: str,
    memorial_name: str,
    role: str,
    accept_url: str,
) -> None:
    """Send one invitation. Caller must only invoke this when email is enabled."""
    host = settings.email_smtp_host
    sender = settings.email_from
    if not host or not sender:
        raise InvitationEmailDeliveryError("Email is enabled but SMTP host or EMAIL_FROM is missing")

    message = EmailMessage()
    message["Subject"] = f"Invitation to {memorial_name}"
    message["From"] = sender
    message["To"] = to_email
    message.set_content(
        "\n".join(
            [
                f"You have been invited to the memorial \"{memorial_name}\" as {role.replace('_', ' ')}.",
                "",
                "Open this link while signed in with this email address to accept:",
                accept_url,
                "",
                "The link expires and can be used only once.",
            ]
        )
    )

    password = settings.email_smtp_password.get_secret_value() if settings.email_smtp_password else ""
    try:
        if settings.email_smtp_use_ssl:
            with smtplib.SMTP_SSL(host, settings.email_smtp_port, timeout=20) as client:
                if settings.email_smtp_user:
                    client.login(settings.email_smtp_user, password)
                client.send_message(message)
        else:
            with smtplib.SMTP(host, settings.email_smtp_port, timeout=20) as client:
                if settings.email_smtp_use_tls:
                    client.starttls()
                if settings.email_smtp_user:
                    client.login(settings.email_smtp_user, password)
                client.send_message(message)
    except (OSError, smtplib.SMTPException) as exc:
        logger.warning("invitation email delivery failed")
        raise InvitationEmailDeliveryError("Invitation email could not be sent") from exc

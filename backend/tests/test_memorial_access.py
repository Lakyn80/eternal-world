from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from app.db.models import MemorialInvitation, MemorialMembership
from app.main import app
from app.modules.memorial_access.service import list_active_memory_contributions
from app.modules.memorial_access import repository as membership_repository


PASSWORD = "StrongPass123"


def _register_and_login(client, email: str) -> str:
    client.post(
        "/api/auth/register",
        json={"email": email, "password": PASSWORD, "full_name": email.split("@")[0]},
    )
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _create_memorial(client, token: str, name: str = "Babička Marie") -> int:
    response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={"name": name, "biography": "Rodinný memorial", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    assert response.status_code == 201
    return response.json()["id"]


def _invite(client, owner_token: str, profile_id: int, email: str, role: str = "contributor") -> str:
    response = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": email, "role": role},
    )
    assert response.status_code == 201
    return response.json()["token"]


def _accept(client, token: str, invitation_token: str):
    return client.post(
        "/api/invitations/accept",
        headers=_auth_headers(token),
        json={"token": invitation_token},
    )


def _submit_contribution(client, token: str, profile_id: int, title: str = "Ukolébavka"):
    return client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(token),
        json={
            "title": title,
            "memory_text": "Babička zpívala ukolébavku o měsíci.",
            "source_note": "Rodinné vyprávění",
            "privacy_scope": "all_family",
        },
    )


def test_owner_can_create_memorial_and_becomes_owner_member(client):
    token = _register_and_login(client, "owner65@example.com")

    response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Babička Marie",
            "personality": "Laskavá",
            "canonical_language": "cs",
            "confirm_canonical_language": True,
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Babička Marie"
    assert body["current_user_role"] == "owner"

    members = client.get(f"/api/memorials/{body['id']}/members", headers=_auth_headers(token))
    assert members.status_code == 200
    assert members.json()[0]["role"] == "owner"
    assert members.json()[0]["email"] == "owner65@example.com"


def test_owner_can_invite_contributor_and_contributor_can_accept(client):
    owner_token = _register_and_login(client, "invite-owner65@example.com")
    contributor_token = _register_and_login(client, "daughter65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "daughter65@example.com")

    response = _accept(client, contributor_token, invitation_token)

    assert response.status_code == 200
    assert response.json()["role"] == "contributor"

    visible = client.get(f"/api/memorials/{profile_id}", headers=_auth_headers(contributor_token))
    assert visible.status_code == 200
    assert visible.json()["current_user_role"] == "contributor"


def test_invitation_token_is_single_use_and_invalid_token_is_safe(client):
    owner_token = _register_and_login(client, "single-owner65@example.com")
    contributor_token = _register_and_login(client, "single-contributor65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "single-contributor65@example.com")

    first = _accept(client, contributor_token, invitation_token)
    second = _accept(client, contributor_token, invitation_token)
    invalid = _accept(client, contributor_token, "not-a-real-invitation-token")

    assert first.status_code == 200
    assert second.status_code == 404
    assert second.json()["detail"] == "Invitation is invalid"
    assert invalid.status_code == 404


def test_expired_invitation_cannot_be_accepted(client):
    owner_token = _register_and_login(client, "expired-owner65@example.com")
    contributor_token = _register_and_login(client, "expired-contributor65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "expired-contributor65@example.com")

    db = app.state.testing_session_local()
    try:
        invitation = db.query(MemorialInvitation).one()
        invitation.expires_at = datetime.now(timezone.utc) - timedelta(minutes=1)
        db.commit()
    finally:
        db.close()

    response = _accept(client, contributor_token, invitation_token)

    assert response.status_code == 400
    assert response.json()["detail"] == "Invitation has expired"


def test_invitation_email_must_match_logged_in_user(client):
    owner_token = _register_and_login(client, "email-owner65@example.com")
    wrong_user_token = _register_and_login(client, "wrong-user65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "right-user65@example.com")

    response = _accept(client, wrong_user_token, invitation_token)

    assert response.status_code == 400
    assert response.json()["detail"] == "Invitation email does not match current user"


def test_invitation_email_match_uses_canonical_normalization(client):
    """Accept must succeed when stored invitation email differs only by case/whitespace."""
    owner_token = _register_and_login(client, "norm-owner65@example.com")
    invitee_token = _register_and_login(client, "norm-invitee65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "norm-invitee65@example.com")

    db = app.state.testing_session_local()
    try:
        invitation = db.query(MemorialInvitation).one()
        invitation.email = "  Norm-Invitee65@Example.COM "
        db.commit()
    finally:
        db.close()

    response = _accept(client, invitee_token, invitation_token)

    assert response.status_code == 200
    assert response.json()["role"] == "contributor"


def test_contributor_can_submit_but_cannot_approve_own_contribution(client):
    owner_token = _register_and_login(client, "review-owner65@example.com")
    contributor_token = _register_and_login(client, "review-contributor65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "review-contributor65@example.com")
    assert _accept(client, contributor_token, invitation_token).status_code == 200

    submitted = _submit_contribution(client, contributor_token, profile_id)
    approve_attempt = client.post(
        f"/api/memorials/{profile_id}/contributions/{submitted.json()['id']}/approve",
        headers=_auth_headers(contributor_token),
        json={"review_note": "self approval attempt"},
    )

    assert submitted.status_code == 201
    assert submitted.json()["status"] == "needs_review"
    assert submitted.json()["active_memory_eligible"] is False
    assert approve_attempt.status_code == 403


def test_owner_can_approve_and_rejected_contribution_is_never_active_memory(client):
    owner_token = _register_and_login(client, "approve-owner65@example.com")
    contributor_token = _register_and_login(client, "approve-contributor65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "approve-contributor65@example.com")
    assert _accept(client, contributor_token, invitation_token).status_code == 200

    approved_candidate = _submit_contribution(client, contributor_token, profile_id, "Approved")
    rejected_candidate = _submit_contribution(client, contributor_token, profile_id, "Rejected")
    approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{approved_candidate.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "family confirmed"},
    )
    rejected = client.post(
        f"/api/memorials/{profile_id}/contributions/{rejected_candidate.json()['id']}/reject",
        headers=_auth_headers(owner_token),
        json={"reason": "not confirmed"},
    )

    assert approved.status_code == 200
    assert approved.json()["status"] == "approved"
    assert approved.json()["is_current"] is True
    assert approved.json()["active_memory_eligible"] is True
    assert rejected.status_code == 200
    assert rejected.json()["status"] == "rejected"
    assert rejected.json()["active_memory_eligible"] is False

    db = app.state.testing_session_local()
    try:
        active = list_active_memory_contributions(db, profile_id=profile_id)
        assert [item.id for item in active] == [approved.json()["id"]]
    finally:
        db.close()


def test_trusted_reviewer_can_approve_but_viewer_cannot_submit(client):
    owner_token = _register_and_login(client, "roles-owner65@example.com")
    reviewer_token = _register_and_login(client, "reviewer65@example.com")
    viewer_token = _register_and_login(client, "viewer65@example.com")
    profile_id = _create_memorial(client, owner_token)
    reviewer_invite = _invite(client, owner_token, profile_id, "reviewer65@example.com", "trusted_reviewer")
    viewer_invite = _invite(client, owner_token, profile_id, "viewer65@example.com", "viewer")
    assert _accept(client, reviewer_token, reviewer_invite).status_code == 200
    assert _accept(client, viewer_token, viewer_invite).status_code == 200

    viewer_submit = _submit_contribution(client, viewer_token, profile_id)
    owner_submission = _submit_contribution(client, owner_token, profile_id)
    reviewer_approval = client.post(
        f"/api/memorials/{profile_id}/contributions/{owner_submission.json()['id']}/approve",
        headers=_auth_headers(reviewer_token),
        json={"review_note": "trusted reviewer confirmed"},
    )

    assert viewer_submit.status_code == 403
    assert reviewer_approval.status_code == 200
    assert reviewer_approval.json()["status"] == "approved"


def test_unrelated_user_and_cross_profile_access_are_blocked(client):
    first_owner_token = _register_and_login(client, "first-owner65@example.com")
    second_owner_token = _register_and_login(client, "second-owner65@example.com")
    unrelated_token = _register_and_login(client, "unrelated65@example.com")
    first_profile_id = _create_memorial(client, first_owner_token, "First Memorial")
    second_profile_id = _create_memorial(client, second_owner_token, "Second Memorial")
    contribution = _submit_contribution(client, first_owner_token, first_profile_id)

    unrelated_get = client.get(f"/api/memorials/{first_profile_id}", headers=_auth_headers(unrelated_token))
    unrelated_queue = client.get(
        f"/api/memorials/{first_profile_id}/review-queue",
        headers=_auth_headers(unrelated_token),
    )
    cross_profile_approve = client.post(
        f"/api/memorials/{second_profile_id}/contributions/{contribution.json()['id']}/approve",
        headers=_auth_headers(second_owner_token),
        json={"review_note": "wrong profile"},
    )

    assert unrelated_get.status_code == 404
    assert unrelated_queue.status_code == 404
    assert cross_profile_approve.status_code == 404


def test_review_queue_only_shows_pending_and_non_reviewers_cannot_list_it(client):
    owner_token = _register_and_login(client, "queue-owner65@example.com")
    contributor_token = _register_and_login(client, "queue-contributor65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "queue-contributor65@example.com")
    assert _accept(client, contributor_token, invitation_token).status_code == 200
    pending = _submit_contribution(client, contributor_token, profile_id, "Pending")
    approved_candidate = _submit_contribution(client, contributor_token, profile_id, "Approved")
    assert client.post(
        f"/api/memorials/{profile_id}/contributions/{approved_candidate.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "ok"},
    ).status_code == 200

    owner_queue = client.get(f"/api/memorials/{profile_id}/review-queue", headers=_auth_headers(owner_token))
    contributor_queue = client.get(
        f"/api/memorials/{profile_id}/review-queue",
        headers=_auth_headers(contributor_token),
    )

    assert owner_queue.status_code == 200
    assert [item["id"] for item in owner_queue.json()] == [pending.json()["id"]]
    assert contributor_queue.status_code == 403


def test_superseded_memory_is_not_active_and_current_approved_memory_wins(client):
    owner_token = _register_and_login(client, "supersede-owner65@example.com")
    profile_id = _create_memorial(client, owner_token)
    old_submission = _submit_contribution(client, owner_token, profile_id, "Old")
    old_approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{old_submission.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "old version"},
    )
    new_submission = _submit_contribution(client, owner_token, profile_id, "New")
    new_approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{new_submission.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={
            "review_note": "corrected version",
            "supersedes_contribution_id": old_approved.json()["id"],
        },
    )

    assert old_approved.status_code == 200
    assert new_approved.status_code == 200
    assert new_approved.json()["status"] == "approved"
    assert new_approved.json()["supersedes_contribution_id"] == old_approved.json()["id"]

    contributions = client.get(f"/api/memorials/{profile_id}/contributions", headers=_auth_headers(owner_token)).json()
    old_after = next(item for item in contributions if item["id"] == old_approved.json()["id"])
    assert old_after["status"] == "superseded"
    assert old_after["active_memory_eligible"] is False

    db = app.state.testing_session_local()
    try:
        active = list_active_memory_contributions(db, profile_id=profile_id)
        assert [item.id for item in active] == [new_approved.json()["id"]]
    finally:
        db.close()


def test_role_escalation_via_invitation_payload_is_blocked(client):
    owner_token = _register_and_login(client, "escalate-owner65@example.com")
    profile_id = _create_memorial(client, owner_token)

    response = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "new-owner65@example.com", "role": "owner"},
    )

    assert response.status_code == 422


def test_existing_member_cannot_be_invited_again(client):
    owner_token = _register_and_login(client, "member-owner65@example.com")
    profile_id = _create_memorial(client, owner_token)

    response = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "member-owner65@example.com", "role": "viewer"},
    )

    assert response.status_code == 409
    assert "membership" in response.json()["detail"].lower()


def test_active_pending_invitation_cannot_be_duplicated(client):
    owner_token = _register_and_login(client, "pending-owner65@example.com")
    profile_id = _create_memorial(client, owner_token)
    payload = {"email": "pending-guest65@example.com", "role": "viewer"}

    first = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json=payload,
    )
    second = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json=payload,
    )

    assert first.status_code == 201
    assert first.json()["token"]
    assert second.status_code == 409
    assert "invitation" in second.json()["detail"].lower()


def test_email_enabled_omits_raw_token(client, monkeypatch):
    from app.core.config import settings

    owner_token = _register_and_login(client, "mail-owner65@example.com")
    profile_id = _create_memorial(client, owner_token)
    sent: dict[str, str] = {}

    def _fake_send(**kwargs):
        sent["accept_url"] = kwargs["accept_url"]
        sent["to_email"] = kwargs["to_email"]

    monkeypatch.setattr(settings, "email_enabled", True)
    monkeypatch.setattr(settings, "public_app_origin", "https://example.test")
    monkeypatch.setattr(
        "app.modules.memorial_access.service.send_memorial_invitation_email",
        _fake_send,
    )

    response = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "mail-guest65@example.com", "role": "contributor"},
    )

    assert response.status_code == 201
    body = response.json()
    assert body["email_sent"] is True
    assert body["token"] is None
    assert body["accept_url"] is None
    assert sent["to_email"] == "mail-guest65@example.com"
    assert sent["accept_url"].startswith("https://example.test/invitations/accept?token=")


def test_email_delivery_failure_revokes_invitation(client, monkeypatch):
    from app.core.config import settings
    from app.modules.notifications.email import InvitationEmailDeliveryError

    owner_token = _register_and_login(client, "failmail-owner65@example.com")
    guest_token = _register_and_login(client, "failmail-guest65@example.com")
    profile_id = _create_memorial(client, owner_token)
    captured: dict[str, str] = {}

    def _fake_send(**kwargs):
        captured["accept_url"] = kwargs["accept_url"]
        raise InvitationEmailDeliveryError("smtp down")

    monkeypatch.setattr(settings, "email_enabled", True)
    monkeypatch.setattr(settings, "public_app_origin", "https://example.test")
    monkeypatch.setattr(
        "app.modules.memorial_access.service.send_memorial_invitation_email",
        _fake_send,
    )

    response = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "failmail-guest65@example.com", "role": "viewer"},
    )

    assert response.status_code == 503
    raw_token = captured["accept_url"].split("token=", 1)[1]
    accepted = _accept(client, guest_token, raw_token)
    assert accepted.status_code == 404


def _user_id(client, token: str) -> int:
    response = client.get("/api/auth/me", headers=_auth_headers(token))
    assert response.status_code == 200
    return response.json()["id"]


def test_owner_soft_revokes_contributor_and_access_is_lost(client):
    owner_token = _register_and_login(client, "revoke-owner65@example.com")
    contributor_token = _register_and_login(client, "revoke-contributor65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invitation_token = _invite(client, owner_token, profile_id, "revoke-contributor65@example.com")
    accepted = _accept(client, contributor_token, invitation_token)
    assert accepted.status_code == 200
    contributor_user_id = accepted.json()["user_id"]
    owner_user_id = _user_id(client, owner_token)

    revoke = client.delete(
        f"/api/memorials/{profile_id}/members/{contributor_user_id}",
        headers=_auth_headers(owner_token),
    )
    assert revoke.status_code == 200
    body = revoke.json()
    assert body["status"] == "revoked"
    assert body["user_id"] == contributor_user_id
    assert body["role"] == "contributor"

    db = app.state.testing_session_local()
    try:
        membership = (
            db.query(MemorialMembership)
            .filter(
                MemorialMembership.profile_id == profile_id,
                MemorialMembership.user_id == contributor_user_id,
            )
            .one()
        )
        assert membership.status == membership_repository.MEMBERSHIP_STATUS_REVOKED
        assert membership.revoked_at is not None
        assert membership.revoked_by_user_id == owner_user_id
    finally:
        db.close()

    members = client.get(f"/api/memorials/{profile_id}/members", headers=_auth_headers(owner_token))
    assert members.status_code == 200
    assert all(item["user_id"] != contributor_user_id for item in members.json())
    assert any(item["role"] == "owner" for item in members.json())

    denied = client.get(f"/api/memorials/{profile_id}", headers=_auth_headers(contributor_token))
    assert denied.status_code == 404


def test_non_owners_cannot_revoke_members(client):
    owner_token = _register_and_login(client, "revoke-authz-owner65@example.com")
    contributor_token = _register_and_login(client, "revoke-authz-contrib65@example.com")
    reviewer_token = _register_and_login(client, "revoke-authz-reviewer65@example.com")
    viewer_token = _register_and_login(client, "revoke-authz-viewer65@example.com")
    outsider_token = _register_and_login(client, "revoke-authz-outsider65@example.com")
    profile_id = _create_memorial(client, owner_token)

    contrib_invite = _invite(client, owner_token, profile_id, "revoke-authz-contrib65@example.com", "contributor")
    reviewer_invite = _invite(client, owner_token, profile_id, "revoke-authz-reviewer65@example.com", "trusted_reviewer")
    viewer_invite = _invite(client, owner_token, profile_id, "revoke-authz-viewer65@example.com", "viewer")
    assert _accept(client, contributor_token, contrib_invite).status_code == 200
    assert _accept(client, reviewer_token, reviewer_invite).status_code == 200
    assert _accept(client, viewer_token, viewer_invite).status_code == 200

    contributor_user_id = _user_id(client, contributor_token)
    reviewer_user_id = _user_id(client, reviewer_token)

    assert (
        client.delete(
            f"/api/memorials/{profile_id}/members/{reviewer_user_id}",
            headers=_auth_headers(contributor_token),
        ).status_code
        == 403
    )
    assert (
        client.delete(
            f"/api/memorials/{profile_id}/members/{contributor_user_id}",
            headers=_auth_headers(reviewer_token),
        ).status_code
        == 403
    )
    assert (
        client.delete(
            f"/api/memorials/{profile_id}/members/{contributor_user_id}",
            headers=_auth_headers(viewer_token),
        ).status_code
        == 403
    )
    assert (
        client.delete(
            f"/api/memorials/{profile_id}/members/{contributor_user_id}",
            headers=_auth_headers(outsider_token),
        ).status_code
        == 404
    )

def test_owner_cannot_revoke_owner_membership(client):
    owner_token = _register_and_login(client, "revoke-self-owner65@example.com")
    profile_id = _create_memorial(client, owner_token)
    owner_user_id = _user_id(client, owner_token)

    response = client.delete(
        f"/api/memorials/{profile_id}/members/{owner_user_id}",
        headers=_auth_headers(owner_token),
    )
    assert response.status_code == 403
    assert "owner" in response.json()["detail"].lower()


def test_unknown_membership_revoke_is_not_found(client):
    owner_token = _register_and_login(client, "revoke-missing-owner65@example.com")
    profile_id = _create_memorial(client, owner_token)

    response = client.delete(
        f"/api/memorials/{profile_id}/members/999999",
        headers=_auth_headers(owner_token),
    )
    assert response.status_code == 404


def test_revoked_member_can_be_reactivated_by_new_invitation(client):
    owner_token = _register_and_login(client, "reactivate-owner65@example.com")
    member_token = _register_and_login(client, "reactivate-member65@example.com")
    profile_id = _create_memorial(client, owner_token)
    first_invite = _invite(client, owner_token, profile_id, "reactivate-member65@example.com", "contributor")
    first_accept = _accept(client, member_token, first_invite)
    assert first_accept.status_code == 200
    member_user_id = first_accept.json()["user_id"]
    membership_id = first_accept.json()["id"]

    revoke = client.delete(
        f"/api/memorials/{profile_id}/members/{member_user_id}",
        headers=_auth_headers(owner_token),
    )
    assert revoke.status_code == 200

    second_invite = _invite(client, owner_token, profile_id, "reactivate-member65@example.com", "trusted_reviewer")
    second_accept = _accept(client, member_token, second_invite)
    assert second_accept.status_code == 200
    body = second_accept.json()
    assert body["id"] == membership_id
    assert body["role"] == "trusted_reviewer"
    assert body["status"] == "active"

    db = app.state.testing_session_local()
    try:
        membership = db.get(MemorialMembership, membership_id)
        assert membership is not None
        assert membership.status == membership_repository.MEMBERSHIP_STATUS_ACTIVE
        assert membership.role == "trusted_reviewer"
        assert membership.revoked_at is None
        assert membership.revoked_by_user_id is None
        assert db.query(MemorialMembership).filter(MemorialMembership.profile_id == profile_id).count() == 2
    finally:
        db.close()

    visible = client.get(f"/api/memorials/{profile_id}", headers=_auth_headers(member_token))
    assert visible.status_code == 200
    assert visible.json()["current_user_role"] == "trusted_reviewer"


def test_double_revoke_is_not_found(client):
    owner_token = _register_and_login(client, "double-revoke-owner65@example.com")
    member_token = _register_and_login(client, "double-revoke-member65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = _invite(client, owner_token, profile_id, "double-revoke-member65@example.com")
    accepted = _accept(client, member_token, invite)
    member_user_id = accepted.json()["user_id"]

    first = client.delete(
        f"/api/memorials/{profile_id}/members/{member_user_id}",
        headers=_auth_headers(owner_token),
    )
    second = client.delete(
        f"/api/memorials/{profile_id}/members/{member_user_id}",
        headers=_auth_headers(owner_token),
    )
    assert first.status_code == 200
    assert second.status_code == 404


def test_owner_sees_contributor_submission_in_review_queue(client):
    owner_token = _register_and_login(client, "queue-foreign-owner65@example.com")
    contributor_token = _register_and_login(client, "queue-foreign-contrib65@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = _invite(client, owner_token, profile_id, "queue-foreign-contrib65@example.com")
    assert _accept(client, contributor_token, invite).status_code == 200

    submitted = _submit_contribution(client, contributor_token, profile_id, "Foreign pending")
    assert submitted.status_code == 201

    owner_queue = client.get(f"/api/memorials/{profile_id}/review-queue", headers=_auth_headers(owner_token))
    assert owner_queue.status_code == 200
    assert [item["id"] for item in owner_queue.json()] == [submitted.json()["id"]]
    assert owner_queue.json()[0]["author_email"] == "queue-foreign-contrib65@example.com"


def test_archive_restore_returns_to_needs_review_without_indexing(client):
    from app.db.models import MemorialContributionPromotion

    owner_token = _register_and_login(client, "restore-owner65@example.com")
    contributor_token = _register_and_login(client, "restore-contrib65@example.com")
    viewer_token = _register_and_login(client, "restore-viewer65@example.com")
    profile_id = _create_memorial(client, owner_token)
    assert _accept(
        client,
        contributor_token,
        _invite(client, owner_token, profile_id, "restore-contrib65@example.com"),
    ).status_code == 200
    assert _accept(
        client,
        viewer_token,
        _invite(client, owner_token, profile_id, "restore-viewer65@example.com", "viewer"),
    ).status_code == 200

    submitted = _submit_contribution(client, contributor_token, profile_id, "Poslední den ve škole")
    contribution_id = submitted.json()["id"]

    archived = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/archive",
        headers=_auth_headers(owner_token),
        json={},
    )
    assert archived.status_code == 200
    assert archived.json()["status"] == "archived"
    assert archived.json()["active_memory_eligible"] is False

    queue_after_archive = client.get(
        f"/api/memorials/{profile_id}/review-queue",
        headers=_auth_headers(owner_token),
    )
    assert contribution_id not in [item["id"] for item in queue_after_archive.json()]

    forbidden_contrib = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/restore",
        headers=_auth_headers(contributor_token),
    )
    forbidden_viewer = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/restore",
        headers=_auth_headers(viewer_token),
    )
    assert forbidden_contrib.status_code == 403
    assert forbidden_viewer.status_code == 403

    restored = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/restore",
        headers=_auth_headers(owner_token),
    )
    assert restored.status_code == 200
    body = restored.json()
    assert body["status"] == "needs_review"
    assert body["is_current"] is False
    assert body["active_memory_eligible"] is False
    assert body["indexing_status"]["state"] == "not_applicable"

    db = app.state.testing_session_local()
    try:
        promotions = (
            db.query(MemorialContributionPromotion)
            .filter(MemorialContributionPromotion.contribution_id == contribution_id)
            .all()
        )
        assert promotions == [] or all(row.promotion_status == "retired" for row in promotions)
    finally:
        db.close()

    queue_after_restore = client.get(
        f"/api/memorials/{profile_id}/review-queue",
        headers=_auth_headers(owner_token),
    )
    assert [item["id"] for item in queue_after_restore.json()] == [contribution_id]

    bad_restore = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/restore",
        headers=_auth_headers(owner_token),
    )
    assert bad_restore.status_code == 400

    approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "ok after restore"},
    )
    assert approved.status_code == 200
    assert approved.json()["status"] == "approved"
    assert approved.json()["indexing_status"]["state"] == "pending"


def test_new_memorial_has_exactly_one_active_owner_matching_profile_user(client):
    from app.db.models import MemorialMembership, MemoryProfile
    from app.modules.memorial_access import repository as membership_repository

    token = _register_and_login(client, "owner-invariant-create65@example.com")
    profile_id = _create_memorial(client, token)

    me = client.get("/api/auth/me", headers=_auth_headers(token))
    assert me.status_code == 200
    owner_user_id = me.json()["id"]

    db = app.state.testing_session_local()
    try:
        profile = db.get(MemoryProfile, profile_id)
        assert profile is not None
        assert profile.user_id == owner_user_id
        owners = (
            db.query(MemorialMembership)
            .filter(
                MemorialMembership.profile_id == profile_id,
                MemorialMembership.role == "owner",
                MemorialMembership.status == membership_repository.MEMBERSHIP_STATUS_ACTIVE,
            )
            .all()
        )
        assert len(owners) == 1
        assert owners[0].user_id == profile.user_id
    finally:
        db.close()


def test_partial_unique_rejects_second_active_owner_even_when_service_bypassed(client):
    from sqlalchemy.exc import IntegrityError

    from app.db.models import MemorialMembership
    from app.modules.memorial_access import repository as membership_repository

    owner_token = _register_and_login(client, "owner-invariant-a65@example.com")
    other_token = _register_and_login(client, "owner-invariant-b65@example.com")
    profile_id = _create_memorial(client, owner_token)
    other_id = client.get("/api/auth/me", headers=_auth_headers(other_token)).json()["id"]

    db = app.state.testing_session_local()
    try:
        membership_repository.create_membership(
            db,
            profile_id=profile_id,
            user_id=other_id,
            role="owner",
            created_by_user_id=other_id,
        )
        with pytest.raises(IntegrityError):
            db.commit()
        db.rollback()
        active_owners = (
            db.query(MemorialMembership)
            .filter(
                MemorialMembership.profile_id == profile_id,
                MemorialMembership.role == "owner",
                MemorialMembership.status == membership_repository.MEMBERSHIP_STATUS_ACTIVE,
            )
            .count()
        )
        assert active_owners == 1
    finally:
        db.close()


def test_invite_cannot_assign_owner_role(client):
    owner_token = _register_and_login(client, "owner-invite-block65@example.com")
    profile_id = _create_memorial(client, owner_token)
    response = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "someone65@example.com", "role": "owner"},
    )
    assert response.status_code == 422


def test_reinvite_revoked_contributor_does_not_change_owner(client):
    from app.db.models import MemorialMembership, MemoryProfile
    from app.modules.memorial_access import repository as membership_repository

    owner_token = _register_and_login(client, "owner-reinvite-o65@example.com")
    contributor_token = _register_and_login(client, "owner-reinvite-c65@example.com")
    profile_id = _create_memorial(client, owner_token)
    owner_user_id = client.get("/api/auth/me", headers=_auth_headers(owner_token)).json()["id"]
    contributor_user_id = client.get("/api/auth/me", headers=_auth_headers(contributor_token)).json()["id"]

    invite = _invite(client, owner_token, profile_id, "owner-reinvite-c65@example.com")
    assert _accept(client, contributor_token, invite).status_code == 200
    assert (
        client.delete(
            f"/api/memorials/{profile_id}/members/{contributor_user_id}",
            headers=_auth_headers(owner_token),
        ).status_code
        == 200
    )

    reinvite = _invite(client, owner_token, profile_id, "owner-reinvite-c65@example.com", "trusted_reviewer")
    assert _accept(client, contributor_token, reinvite).status_code == 200

    db = app.state.testing_session_local()
    try:
        profile = db.get(MemoryProfile, profile_id)
        assert profile is not None
        assert profile.user_id == owner_user_id
        owners = (
            db.query(MemorialMembership)
            .filter(
                MemorialMembership.profile_id == profile_id,
                MemorialMembership.role == "owner",
                MemorialMembership.status == membership_repository.MEMBERSHIP_STATUS_ACTIVE,
            )
            .all()
        )
        assert len(owners) == 1
        assert owners[0].user_id == owner_user_id
        contributor = (
            db.query(MemorialMembership)
            .filter(
                MemorialMembership.profile_id == profile_id,
                MemorialMembership.user_id == contributor_user_id,
            )
            .one()
        )
        assert contributor.status == membership_repository.MEMBERSHIP_STATUS_ACTIVE
        assert contributor.role == "trusted_reviewer"
    finally:
        db.close()


def test_owner_revoke_remains_forbidden_under_single_owner_invariant(client):
    owner_token = _register_and_login(client, "owner-self-revoke65@example.com")
    profile_id = _create_memorial(client, owner_token)
    owner_user_id = client.get("/api/auth/me", headers=_auth_headers(owner_token)).json()["id"]
    response = client.delete(
        f"/api/memorials/{profile_id}/members/{owner_user_id}",
        headers=_auth_headers(owner_token),
    )
    assert response.status_code == 403


def test_legacy_memory_profile_zero_owner_self_heals_via_capability_path(client):
    """Legacy /api/memory-profiles create leaves zero owners until self-heal.

    Phase 5A documents this as intentional compatibility — not auto-repaired
    by migration. Capability resolution creates exactly one matching owner.
    """
    from app.db.models import MemorialMembership
    from app.modules.memorial_access import repository as membership_repository
    from app.modules.memorial_access.owner_integrity import check_memorial_owner_integrity

    token = _register_and_login(client, "legacy-zero-owner65@example.com")
    created = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": "Legacy Zero Owner", "canonical_language": "cs", "confirm_canonical_language": True},
    )
    assert created.status_code == 201
    profile_id = created.json()["id"]
    owner_user_id = client.get("/api/auth/me", headers=_auth_headers(token)).json()["id"]

    db = app.state.testing_session_local()
    try:
        assert (
            db.query(MemorialMembership)
            .filter(MemorialMembership.profile_id == profile_id)
            .count()
            == 0
        )
        report = check_memorial_owner_integrity(db)
        assert any(
            item.code == "zero_active_owners" and item.profile_id == profile_id for item in report.findings
        )
    finally:
        db.close()

    # Memorial list/get do not self-heal; capability path does.
    listed = client.get("/api/memorials", headers=_auth_headers(token))
    assert listed.status_code == 200
    assert all(item["id"] != profile_id for item in listed.json())

    persona = client.get(f"/api/memorials/{profile_id}/avatar-persona", headers=_auth_headers(token))
    assert persona.status_code == 200

    db = app.state.testing_session_local()
    try:
        owners = (
            db.query(MemorialMembership)
            .filter(
                MemorialMembership.profile_id == profile_id,
                MemorialMembership.role == "owner",
                MemorialMembership.status == membership_repository.MEMBERSHIP_STATUS_ACTIVE,
            )
            .all()
        )
        assert len(owners) == 1
        assert owners[0].user_id == owner_user_id
        report_after = check_memorial_owner_integrity(db)
        assert not any(
            item.code == "zero_active_owners" and item.profile_id == profile_id
            for item in report_after.findings
        )
    finally:
        db.close()


def test_owner_integrity_preflight_detects_zero_multi_and_mismatch(client):
    from app.db.models import MemoryProfile
    from app.modules.memorial_access.owner_integrity import check_memorial_owner_integrity

    token = _register_and_login(client, "integrity-scan-owner65@example.com")
    other = _register_and_login(client, "integrity-scan-other65@example.com")
    profile_id = _create_memorial(client, token)
    other_id = client.get("/api/auth/me", headers=_auth_headers(other)).json()["id"]

    # Clean memorial should not appear in findings for this profile.
    db = app.state.testing_session_local()
    try:
        clean = check_memorial_owner_integrity(db)
        assert not any(item.profile_id == profile_id for item in clean.findings)

        # Force mismatch by pointing profile.user_id at another user while
        # keeping the existing active owner membership (read-only scan only).
        profile = db.get(MemoryProfile, profile_id)
        assert profile is not None
        original_owner = profile.user_id
        profile.user_id = other_id
        db.commit()

        mismatch_report = check_memorial_owner_integrity(db)
        assert any(
            item.code == "owner_profile_mismatch" and item.profile_id == profile_id
            for item in mismatch_report.findings
        )

        # Restore profile owner for isolation (do not leave dirty fixture).
        profile = db.get(MemoryProfile, profile_id)
        assert profile is not None
        profile.user_id = original_owner
        db.commit()
    finally:
        db.close()


def test_owner_lists_and_revokes_pending_invitation(client):
    owner_token = _register_and_login(client, "invite-list-owner65@example.com")
    contributor_token = _register_and_login(client, "invite-list-contrib65@example.com")
    reviewer_token = _register_and_login(client, "invite-list-reviewer65@example.com")
    profile_id = _create_memorial(client, owner_token)
    assert (
        _accept(
            client,
            reviewer_token,
            _invite(client, owner_token, profile_id, "invite-list-reviewer65@example.com", "trusted_reviewer"),
        ).status_code
        == 200
    )

    invite_token = _invite(client, owner_token, profile_id, "invite-list-pending65@example.com")
    listed = client.get(f"/api/memorials/{profile_id}/invitations", headers=_auth_headers(owner_token))
    assert listed.status_code == 200
    body = listed.json()
    assert len(body) == 1
    assert body[0]["email"] == "invite-list-pending65@example.com"
    assert body[0]["role"] == "contributor"
    assert body[0]["status"] == "pending"
    assert body[0]["accepted_at"] is None
    assert body[0]["revoked_at"] is None
    invitation_id = body[0]["id"]

    forbidden_contrib = client.get(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(contributor_token),
    )
    # Contributor is not a member → memorial not revealed as 404.
    assert forbidden_contrib.status_code == 404
    forbidden_reviewer = client.get(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(reviewer_token),
    )
    assert forbidden_reviewer.status_code == 403

    forbidden_revoke = client.delete(
        f"/api/memorials/{profile_id}/invitations/{invitation_id}",
        headers=_auth_headers(reviewer_token),
    )
    assert forbidden_revoke.status_code == 403

    revoked = client.delete(
        f"/api/memorials/{profile_id}/invitations/{invitation_id}",
        headers=_auth_headers(owner_token),
    )
    assert revoked.status_code == 200
    assert revoked.json()["status"] == "revoked"
    assert revoked.json()["revoked_at"] is not None

    listed_after = client.get(f"/api/memorials/{profile_id}/invitations", headers=_auth_headers(owner_token))
    assert listed_after.json() == []

    accept_revoked = _accept(client, contributor_token, invite_token)
    assert accept_revoked.status_code == 404

    double = client.delete(
        f"/api/memorials/{profile_id}/invitations/{invitation_id}",
        headers=_auth_headers(owner_token),
    )
    assert double.status_code == 404


def test_reinvite_after_invitation_revoke_creates_new_pending(client):
    owner_token = _register_and_login(client, "reinvite-after-revoke-o65@example.com")
    invitee_token = _register_and_login(client, "reinvite-after-revoke-i65@example.com")
    profile_id = _create_memorial(client, owner_token)
    email = "reinvite-after-revoke-i65@example.com"

    first_token = _invite(client, owner_token, profile_id, email)
    listed = client.get(f"/api/memorials/{profile_id}/invitations", headers=_auth_headers(owner_token))
    invitation_id = listed.json()[0]["id"]
    assert (
        client.delete(
            f"/api/memorials/{profile_id}/invitations/{invitation_id}",
            headers=_auth_headers(owner_token),
        ).status_code
        == 200
    )

    second_token = _invite(client, owner_token, profile_id, email)
    assert second_token != first_token
    listed2 = client.get(f"/api/memorials/{profile_id}/invitations", headers=_auth_headers(owner_token))
    assert len(listed2.json()) == 1
    assert listed2.json()[0]["email"] == email
    assert listed2.json()[0]["status"] == "pending"

    accepted = _accept(client, invitee_token, second_token)
    assert accepted.status_code == 200
    assert accepted.json()["role"] == "contributor"

    members = client.get(f"/api/memorials/{profile_id}/members", headers=_auth_headers(owner_token))
    assert members.status_code == 200
    assert any(m["email"] == email and m["status"] == "active" for m in members.json())


def test_accepted_invitation_is_not_listed_and_cannot_be_revoked(client):
    owner_token = _register_and_login(client, "accepted-invite-o65@example.com")
    invitee_token = _register_and_login(client, "accepted-invite-i65@example.com")
    profile_id = _create_memorial(client, owner_token)
    token = _invite(client, owner_token, profile_id, "accepted-invite-i65@example.com")
    listed_before = client.get(f"/api/memorials/{profile_id}/invitations", headers=_auth_headers(owner_token))
    invitation_id = listed_before.json()[0]["id"]
    assert _accept(client, invitee_token, token).status_code == 200

    listed = client.get(f"/api/memorials/{profile_id}/invitations", headers=_auth_headers(owner_token))
    assert listed.json() == []

    revoke_accepted = client.delete(
        f"/api/memorials/{profile_id}/invitations/{invitation_id}",
        headers=_auth_headers(owner_token),
    )
    assert revoke_accepted.status_code == 409

    members = client.get(f"/api/memorials/{profile_id}/members", headers=_auth_headers(owner_token))
    assert any(m["email"] == "accepted-invite-i65@example.com" and m["status"] == "active" for m in members.json())


def test_expired_invitation_is_listed_as_expired_and_does_not_block_reinvite(client):
    owner_token = _register_and_login(client, "expired-list-o65@example.com")
    profile_id = _create_memorial(client, owner_token)
    _invite(client, owner_token, profile_id, "expired-list65@example.com")

    db = app.state.testing_session_local()
    try:
        invitation = db.query(MemorialInvitation).filter(MemorialInvitation.profile_id == profile_id).one()
        invitation.expires_at = datetime.now(timezone.utc) - timedelta(minutes=1)
        invitation_id = invitation.id
        db.commit()
    finally:
        db.close()

    listed = client.get(f"/api/memorials/{profile_id}/invitations", headers=_auth_headers(owner_token))
    assert listed.status_code == 200
    assert len(listed.json()) == 1
    assert listed.json()[0]["status"] == "expired"
    assert listed.json()[0]["id"] == invitation_id

    # Expired is not an active pending invite — re-invite must succeed.
    second = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "expired-list65@example.com", "role": "viewer"},
    )
    assert second.status_code == 201


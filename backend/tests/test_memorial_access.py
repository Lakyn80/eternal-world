from __future__ import annotations

from datetime import datetime, timedelta, timezone

from app.db.models import MemorialInvitation
from app.main import app
from app.modules.memorial_access.service import list_active_memory_contributions


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
        json={"name": name, "biography": "Rodinný memorial"},
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
        json={"name": "Babička Marie", "personality": "Laskavá"},
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


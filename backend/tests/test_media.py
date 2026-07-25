import re

import pytest
from sqlalchemy import LargeBinary

from app.core.config import settings
from app.db.models import MediaAsset
from app.modules.media.storage.local import LocalStorageProvider


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "Media User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return login_response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _create_profile(client, token: str, name: str) -> int:
    response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": name},
    )
    return response.json()["id"]


@pytest.fixture(autouse=True)
def media_settings(tmp_path, monkeypatch):
    media_root = tmp_path / "media"
    monkeypatch.setattr(settings, "media_storage_provider", "local")
    monkeypatch.setattr(settings, "media_root", media_root)
    monkeypatch.setattr(settings, "media_public_base_url", "/media")
    monkeypatch.setattr(settings, "media_max_file_size_bytes", 32)
    return media_root


def test_authenticated_user_can_upload_allowed_file(client, media_settings):
    token = _register_and_login(client, "upload-ok@example.com")

    response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("portrait.png", b"image-bytes", "image/png")},
    )

    assert response.status_code == 201
    body = response.json()
    assert body["owner_id"] > 0
    assert body["media_type"] == "image"
    assert body["storage_provider"] == "local"
    assert body["mime_type"] == "image/png"
    assert body["size_bytes"] == len(b"image-bytes")
    assert body["original_filename"] == "portrait.png"
    assert body["public_url"] == f"/media/{body['storage_key']}"
    assert str(media_settings.resolve()) not in body["public_url"]
    stored_files = [path for path in media_settings.rglob("*") if path.is_file()]
    assert len(stored_files) == 1


def test_local_media_route_serves_uploaded_local_file_safely(client):
    token = _register_and_login(client, "media-serve@example.com")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("portrait.png", b"image-bytes", "image/png")},
    )
    public_url = upload_response.json()["public_url"]

    response = client.get(public_url)

    assert response.status_code == 200
    assert response.content == b"image-bytes"
    assert response.headers["content-type"] == "image/png"


def test_local_media_route_rejects_path_traversal(client):
    response = client.get("/media/%2e%2e/%2e%2e/secret.png")

    assert response.status_code == 404
    assert response.json()["detail"] == "Media file not found"


def test_local_media_route_returns_404_for_missing_file(client):
    response = client.get("/media/image/2026/06/17/missing-file.png")

    assert response.status_code == 404
    assert response.json()["detail"] == "Media file not found"


def test_unauthenticated_upload_is_rejected(client):
    response = client.post(
        "/api/media/upload",
        files={"file": ("portrait.png", b"image-bytes", "image/png")},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_unsupported_mime_type_is_rejected(client):
    token = _register_and_login(client, "upload-bad-mime@example.com")

    response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("archive.zip", b"zip-bytes", "application/zip")},
    )

    assert response.status_code == 415
    assert response.json()["detail"] == "Unsupported media type"


def test_too_large_file_is_rejected(client):
    token = _register_and_login(client, "upload-too-large@example.com")

    response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("large.mp4", b"x" * 33, "video/mp4")},
    )

    assert response.status_code == 413
    assert response.json()["detail"] == "File is too large"


def test_path_traversal_filename_is_sanitized_and_stays_inside_media_root(client, media_settings):
    token = _register_and_login(client, "upload-traversal@example.com")

    response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("../../secret.png", b"safe-bytes", "image/png")},
    )

    assert response.status_code == 201
    body = response.json()
    assert body["original_filename"] == "secret.png"
    assert ".." not in body["storage_key"]
    assert str(media_settings.resolve()) not in body["storage_key"]
    stored_files = [path for path in media_settings.rglob("*") if path.is_file()]
    assert len(stored_files) == 1
    stored_files[0].resolve().relative_to(media_settings.resolve())


def test_user_can_list_only_own_media(client):
    first_token = _register_and_login(client, "media-first@example.com")
    second_token = _register_and_login(client, "media-second@example.com")

    client.post(
        "/api/media/upload",
        headers=_auth_headers(first_token),
        files={"file": ("first.png", b"first-bytes", "image/png")},
    )
    client.post(
        "/api/media/upload",
        headers=_auth_headers(second_token),
        files={"file": ("second.png", b"second-bytes", "image/png")},
    )

    response = client.get("/api/media", headers=_auth_headers(first_token))

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["original_filename"] == "first.png"


def test_user_can_get_own_media_metadata(client):
    token = _register_and_login(client, "media-get@example.com")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("voice.wav", b"wav-bytes", "audio/wav")},
    )
    media_id = upload_response.json()["id"]

    response = client.get(f"/api/media/{media_id}", headers=_auth_headers(token))

    assert response.status_code == 200
    assert response.json()["mime_type"] == "audio/wav"


def test_user_cannot_get_another_users_media(client):
    owner_token = _register_and_login(client, "media-owner@example.com")
    other_token = _register_and_login(client, "media-other@example.com")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(owner_token),
        files={"file": ("owner.png", b"owner-bytes", "image/png")},
    )
    media_id = upload_response.json()["id"]

    response = client.get(f"/api/media/{media_id}", headers=_auth_headers(other_token))

    assert response.status_code == 404
    assert response.json()["detail"] == "Media not found"


def test_user_can_delete_own_media_metadata_and_local_file(client, media_settings):
    token = _register_and_login(client, "media-delete@example.com")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("delete.webp", b"webp-bytes", "image/webp")},
    )
    media_id = upload_response.json()["id"]
    stored_files = [path for path in media_settings.rglob("*") if path.is_file()]
    assert len(stored_files) == 1

    delete_response = client.delete(f"/api/media/{media_id}", headers=_auth_headers(token))
    get_response = client.get(f"/api/media/{media_id}", headers=_auth_headers(token))

    assert delete_response.status_code == 204
    assert get_response.status_code == 404
    assert not any(path.is_file() for path in media_settings.rglob("*"))


def test_user_cannot_delete_another_users_media(client):
    owner_token = _register_and_login(client, "media-delete-owner@example.com")
    other_token = _register_and_login(client, "media-delete-other@example.com")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(owner_token),
        files={"file": ("owner.mp3", b"mp3-bytes", "audio/mpeg")},
    )
    media_id = upload_response.json()["id"]

    response = client.delete(f"/api/media/{media_id}", headers=_auth_headers(other_token))

    assert response.status_code == 404
    assert response.json()["detail"] == "Media not found"


def test_upload_with_another_users_profile_id_returns_404(client):
    owner_token = _register_and_login(client, "profile-owner-media@example.com")
    other_token = _register_and_login(client, "profile-other-media@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Profile")

    response = client.post(
        "/api/media/upload",
        headers=_auth_headers(other_token),
        data={"profile_id": str(profile_id)},
        files={"file": ("other.png", b"other-bytes", "image/png")},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_authenticated_user_can_assign_own_uploaded_image_to_own_memory_profile(client, media_settings):
    token = _register_and_login(client, "profile-photo-bind@example.com")
    profile_id = _create_profile(client, token, "Photo Profile")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("profile.png", b"profile-bytes", "image/png")},
    )
    media_body = upload_response.json()

    response = client.post(
        f"/api/memory-profiles/{profile_id}/photo",
        headers=_auth_headers(token),
        json={"media_id": media_body["id"]},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["photo_media_id"] == media_body["id"]
    assert body["photo_url"] == media_body["public_url"]
    assert str(media_settings.resolve()) not in body["photo_url"]


def test_authenticated_user_can_unset_profile_photo(client):
    token = _register_and_login(client, "profile-photo-unset@example.com")
    profile_id = _create_profile(client, token, "Unset Photo Profile")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("profile.webp", b"profile-webp", "image/webp")},
    )
    media_id = upload_response.json()["id"]
    client.post(
        f"/api/memory-profiles/{profile_id}/photo",
        headers=_auth_headers(token),
        json={"media_id": media_id},
    )

    response = client.delete(
        f"/api/memory-profiles/{profile_id}/photo",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["photo_media_id"] is None
    assert body["photo_url"] is None


def test_user_cannot_assign_another_users_media_as_profile_photo(client):
    owner_token = _register_and_login(client, "profile-photo-owner@example.com")
    other_token = _register_and_login(client, "profile-photo-other@example.com")
    profile_id = _create_profile(client, other_token, "Other User Profile")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(owner_token),
        files={"file": ("owner-photo.png", b"owner-photo", "image/png")},
    )
    media_id = upload_response.json()["id"]

    response = client.post(
        f"/api/memory-profiles/{profile_id}/photo",
        headers=_auth_headers(other_token),
        json={"media_id": media_id},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Media not found"


def test_user_cannot_assign_photo_to_another_users_profile(client):
    owner_token = _register_and_login(client, "profile-photo-owner-profile@example.com")
    other_token = _register_and_login(client, "profile-photo-owner-media@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Profile")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(other_token),
        files={"file": ("other-photo.png", b"other-photo", "image/png")},
    )
    media_id = upload_response.json()["id"]

    response = client.post(
        f"/api/memory-profiles/{profile_id}/photo",
        headers=_auth_headers(other_token),
        json={"media_id": media_id},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"


def test_non_image_media_cannot_be_assigned_as_profile_photo(client):
    token = _register_and_login(client, "profile-photo-audio@example.com")
    profile_id = _create_profile(client, token, "Audio Photo Profile")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("voice.wav", b"voice-bytes", "audio/wav")},
    )
    media_id = upload_response.json()["id"]

    response = client.post(
        f"/api/memory-profiles/{profile_id}/photo",
        headers=_auth_headers(token),
        json={"media_id": media_id},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Profile photo must be an image"


def test_unauthenticated_profile_photo_binding_is_rejected(client):
    token = _register_and_login(client, "profile-photo-auth-owner@example.com")
    profile_id = _create_profile(client, token, "Auth Profile")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("photo.png", b"auth-photo", "image/png")},
    )
    media_id = upload_response.json()["id"]

    client.cookies.clear()
    response = client.post(
        f"/api/memory-profiles/{profile_id}/photo",
        json={"media_id": media_id},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_profile_response_includes_usable_photo_reference(client, media_settings):
    token = _register_and_login(client, "profile-photo-response@example.com")
    profile_id = _create_profile(client, token, "Photo Response Profile")
    upload_response = client.post(
        "/api/media/upload",
        headers=_auth_headers(token),
        files={"file": ("photo-response.png", b"response-photo", "image/png")},
    )
    media_body = upload_response.json()
    client.post(
        f"/api/memory-profiles/{profile_id}/photo",
        headers=_auth_headers(token),
        json={"media_id": media_body["id"]},
    )

    response = client.get(
        f"/api/memory-profiles/{profile_id}",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["photo_media_id"] == media_body["id"]
    assert body["photo_url"] == media_body["public_url"]
    assert str(media_settings.resolve()) not in body["photo_url"]


def test_local_storage_provider_generates_safe_storage_keys(media_settings):
    provider = LocalStorageProvider(media_root=media_settings, public_base_url="/media")

    storage_key = provider.save_bytes(
        content=b"provider-bytes",
        media_type="image",
        extension=".png",
    )
    public_url = provider.build_public_url(storage_key=storage_key)

    assert re.fullmatch(r"image/\d{4}/\d{2}/\d{2}/[0-9a-f]{32}\.png", storage_key)
    assert ".." not in storage_key
    assert not storage_key.startswith("/")
    assert public_url == f"/media/{storage_key}"
    assert str(media_settings.resolve()) not in public_url


def test_media_metadata_model_stores_no_raw_file_bytes():
    assert "storage_key" in MediaAsset.__table__.columns.keys()
    assert "size_bytes" in MediaAsset.__table__.columns.keys()
    assert "content" not in MediaAsset.__table__.columns.keys()
    assert "file_bytes" not in MediaAsset.__table__.columns.keys()
    assert not any(isinstance(column.type, LargeBinary) for column in MediaAsset.__table__.columns)

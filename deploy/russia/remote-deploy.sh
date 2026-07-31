#!/usr/bin/env bash
# Remote deploy steps for the existing Russian production install.
# Invoked over SSH from GitHub Actions. Expects:
#   APP_DIR, APP_DOMAIN, BACKEND_HOST_PORT, FRONTEND_HOST_PORT,
#   IMAGE_TAG (full git SHA), GHCR_LOGIN_USER, GHCR_LOGIN_TOKEN,
#   LETSENCRYPT_EMAIL (optional)
#
# Preserves volumes. Never runs `docker compose down -v`.

set -euo pipefail

: "${APP_DIR:?}"
: "${APP_DOMAIN:?}"
: "${BACKEND_HOST_PORT:?}"
: "${FRONTEND_HOST_PORT:?}"
: "${IMAGE_TAG:?}"

if [ -n "${GHCR_LOGIN_USER:-}" ] && [ -n "${GHCR_LOGIN_TOKEN:-}" ]; then
  printf '%s\n' "${GHCR_LOGIN_TOKEN}" | docker login ghcr.io -u "${GHCR_LOGIN_USER}" --password-stdin
fi

docker volume create shared_huggingface_cache >/dev/null

mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled
rm -f /etc/nginx/sites-enabled/sites-available

if [ ! -f "/etc/letsencrypt/live/${APP_DOMAIN}/fullchain.pem" ]; then
  cp "${APP_DIR}/infra/nginx/eternalworld.lukiora.ru.bootstrap.conf" "/etc/nginx/sites-available/${APP_DOMAIN}"
  ln -sfn "/etc/nginx/sites-available/${APP_DOMAIN}" "/etc/nginx/sites-enabled/${APP_DOMAIN}"
  nginx -t
  systemctl reload nginx
  if [ -n "${LETSENCRYPT_EMAIL:-}" ]; then
    certbot --nginx --non-interactive --agree-tos -m "${LETSENCRYPT_EMAIL}" -d "${APP_DOMAIN}"
  else
    certbot --nginx --non-interactive --agree-tos --register-unsafely-without-email -d "${APP_DOMAIN}"
  fi
fi

cp "${APP_DIR}/infra/nginx/eternalworld.lukiora.ru.conf" "/etc/nginx/sites-available/${APP_DOMAIN}"
ln -sfn "/etc/nginx/sites-available/${APP_DOMAIN}" "/etc/nginx/sites-enabled/${APP_DOMAIN}"
nginx -t
systemctl reload nginx

cd "${APP_DIR}"

# Keep existing .env.prod secrets; only refresh image tags / ports / domain CORS.
tmp_env="$(mktemp)"
grep -vE '^(BACKEND_IMAGE|FRONTEND_IMAGE|BACKEND_HOST_PORT|FRONTEND_HOST_PORT|BACKEND_CORS_ORIGINS|VITE_API_URL)=' .env.prod > "${tmp_env}" || true
{
  printf '%s\n' "BACKEND_IMAGE=ghcr.io/lakyn80/eternal-world-backend:${IMAGE_TAG}"
  printf '%s\n' "FRONTEND_IMAGE=ghcr.io/lakyn80/eternal-world-frontend:${IMAGE_TAG}"
  printf '%s\n' "BACKEND_HOST_PORT=${BACKEND_HOST_PORT}"
  printf '%s\n' "FRONTEND_HOST_PORT=${FRONTEND_HOST_PORT}"
  printf '%s\n' "BACKEND_CORS_ORIGINS=https://${APP_DOMAIN}"
  printf '%s\n' "VITE_API_URL="
} >> "${tmp_env}"
mv "${tmp_env}" .env.prod

docker compose --env-file .env.prod -f docker-compose.prod.yml pull
docker compose --env-file .env.prod -f docker-compose.prod.yml up -d db redis qdrant
docker compose --env-file .env.prod -f docker-compose.prod.yml run --rm backend alembic upgrade head
docker compose --env-file .env.prod -f docker-compose.prod.yml run --rm backend python scripts/prefetch_embedding_model.py --provider bge_m3_dense_sparse
docker compose --env-file .env.prod -f docker-compose.prod.yml run --rm backend python scripts/ensure_active_retrieval_collection.py
docker compose --env-file .env.prod -f docker-compose.prod.yml run --rm backend python scripts/ensure_persona_chat_languages.py
# Preserve historical Russia behavior: seed demo profile when present.
docker compose --env-file .env.prod -f docker-compose.prod.yml run --rm backend python scripts/bootstrap_family_avatar_ru_e2e.py || true
# Match the established Russia process set (do not force new workers here).
docker compose --env-file .env.prod -f docker-compose.prod.yml up -d --remove-orphans backend celery_worker frontend

for attempt in $(seq 1 30); do
  if curl -fsS "http://127.0.0.1:${BACKEND_HOST_PORT}/health/runtime" >/dev/null; then
    break
  fi
  if [ "${attempt}" -eq 30 ]; then
    echo 'backend healthcheck failed' >&2
    exit 1
  fi
  sleep 5
done

for attempt in $(seq 1 30); do
  if curl -fsS -o /dev/null -w '%{http_code}' "http://127.0.0.1:${FRONTEND_HOST_PORT}/" | grep -q '^200$'; then
    break
  fi
  if [ "${attempt}" -eq 30 ]; then
    echo 'frontend local healthcheck failed' >&2
    docker compose --env-file .env.prod -f docker-compose.prod.yml ps >&2
    exit 1
  fi
  sleep 2
done

for attempt in $(seq 1 30); do
  if curl -fsS -o /dev/null -w '%{http_code}' "https://${APP_DOMAIN}/" | grep -q '^200$'; then
    break
  fi
  if [ "${attempt}" -eq 30 ]; then
    echo 'frontend public healthcheck failed' >&2
    exit 1
  fi
  sleep 2
done

echo "Russia deploy OK: ${IMAGE_TAG}"

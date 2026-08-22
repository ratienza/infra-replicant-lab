#!/usr/bin/env bash
set -euo pipefail

INFRA_REPO="${INFRA_REPO:-/opt/apps/infra-replicant-lab}"
ERASMUS_REPO="${ERASMUS_REPO:-/opt/apps/ErasmusHomes}"
COMPOSE_PROJECT="${COMPOSE_PROJECT:-infra-replicant-lab}"
PYTHON_BIN="${PYTHON_BIN:-$(command -v python3 || command -v python || true)}"

test -n "$PYTHON_BIN" || { echo "Python 3 is required." >&2; exit 1; }

for repo in "$INFRA_REPO" "$ERASMUS_REPO"; do
  test -d "$repo/.git"
  test -z "$(git -C "$repo" status --porcelain)" || { echo "Dirty checkout: $repo" >&2; exit 1; }
done

git -C "$ERASMUS_REPO" switch main
git -C "$ERASMUS_REPO" pull --ff-only origin main
git -C "$INFRA_REPO" switch main
git -C "$INFRA_REPO" pull --ff-only origin main

stage="$(mktemp -d)"
trap 'rm -rf "$stage"' EXIT
mkdir -p "$stage/infra"
cp -a "$INFRA_REPO/." "$stage/infra/"
"$PYTHON_BIN" "$stage/infra/scripts/erasmushomes_panel.py" generate --repo "$ERASMUS_REPO"
"$PYTHON_BIN" "$stage/infra/scripts/erasmushomes_panel.py" check

current_image="$(docker inspect --format '{{.Image}}' infra-replicant-docs 2>/dev/null || true)"
if test -n "$current_image"; then
  docker image tag "$current_image" infra-replicant-docs:last-good
fi

if ! docker compose -p "$COMPOSE_PROJECT" --project-directory "$stage/infra" -f "$stage/infra/compose.yml" up -d --build docs; then
  echo "Documentation build failed; restoring last-good image." >&2
  if docker image inspect infra-replicant-docs:last-good >/dev/null 2>&1; then
    docker image tag infra-replicant-docs:last-good infra-replicant-docs:local
    docker compose -p "$COMPOSE_PROJECT" --project-directory "$INFRA_REPO" -f "$INFRA_REPO/compose.yml" up -d --no-build --force-recreate docs
  fi
  exit 1
fi
expected_sha="$(git -C "$ERASMUS_REPO" rev-parse HEAD)"
published=0
for _attempt in $(seq 1 20); do
  if curl --fail --silent http://192.168.18.220:8082/aplicaciones/erasmushomes-control/ | grep --quiet "$expected_sha"; then
    published=1
    break
  fi
  sleep 1
done
if test "$published" -ne 1; then
  echo "New panel failed HTTP/SHA validation; restoring last-good image." >&2
  if docker image inspect infra-replicant-docs:last-good >/dev/null 2>&1; then
    docker image tag infra-replicant-docs:last-good infra-replicant-docs:local
    docker compose -p "$COMPOSE_PROJECT" --project-directory "$INFRA_REPO" -f "$INFRA_REPO/compose.yml" up -d --no-build --force-recreate docs
  fi
  exit 1
fi

echo "Published ErasmusHomes panel for $expected_sha through the existing Replicant Lab service."

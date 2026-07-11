#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  printf 'Verwendung: %s PFAD_ZUM_BACKUP\n' "$0" >&2
  exit 2
fi

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
backup_file=$1
checksum_file="$backup_file.sha256"

if [ ! -f "$backup_file" ] || [ ! -s "$backup_file" ]; then
  printf 'Fehler: Backup fehlt oder ist leer: %s\n' "$backup_file" >&2
  exit 1
fi

if [ ! -f "$checksum_file" ]; then
  printf 'Fehler: Prüfsummendatei fehlt: %s\n' "$checksum_file" >&2
  exit 1
fi

(
  cd "$(dirname -- "$backup_file")"
  sha256sum --check --strict "$(basename -- "$checksum_file")"
)

docker compose --project-directory "$repo_root" exec -T db \
  pg_restore --list < "$backup_file" >/dev/null

printf 'Backup ist lesbar und die Prüfsumme stimmt: %s\n' "$backup_file"

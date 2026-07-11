#!/bin/sh
set -eu

umask 077

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
backup_dir=${BACKUP_DIR:-$repo_root/backups/postgres}
retention_days=${BACKUP_RETENTION_DAYS:-30}

case "$backup_dir" in
  /*) ;;
  *) backup_dir="$repo_root/$backup_dir" ;;
esac

case "$retention_days" in
  ''|*[!0-9]*)
    printf 'Fehler: BACKUP_RETENTION_DAYS muss eine nichtnegative ganze Zahl sein.\n' >&2
    exit 2
    ;;
esac

mkdir -p "$backup_dir"
chmod 700 "$backup_dir"

lock_dir="$backup_dir/.backup.lock"
if ! mkdir "$lock_dir" 2>/dev/null; then
  printf 'Fehler: In %s läuft bereits ein Backup.\n' "$backup_dir" >&2
  exit 1
fi

tmp_file=
cleanup() {
  if [ -n "$tmp_file" ] && [ -f "$tmp_file" ]; then
    rm -f "$tmp_file"
  fi
  rmdir "$lock_dir" 2>/dev/null || true
}
trap cleanup EXIT HUP INT TERM

timestamp=$(date -u +%Y%m%dT%H%M%SZ)
filename="schule-postgres-$timestamp.dump"
backup_file="$backup_dir/$filename"
tmp_file="$backup_dir/.$filename.tmp"

printf 'PostgreSQL-Backup wird erstellt ...\n'
docker compose --project-directory "$repo_root" exec -T db \
  sh -c 'exec pg_dump --format=custom --no-owner --no-acl -U "$POSTGRES_USER" "$POSTGRES_DB"' \
  > "$tmp_file"

if [ ! -s "$tmp_file" ]; then
  printf 'Fehler: Das erzeugte Backup ist leer.\n' >&2
  exit 1
fi

chmod 600 "$tmp_file"
mv "$tmp_file" "$backup_file"
tmp_file=

(
  cd "$backup_dir"
  sha256sum "$filename" > "$filename.sha256"
  chmod 600 "$filename.sha256"
)

find "$backup_dir" -maxdepth 1 -type f \
  \( -name 'schule-postgres-*.dump' -o -name 'schule-postgres-*.dump.sha256' \) \
  -mtime "+$retention_days" -delete

printf 'Backup erstellt: %s\n' "$backup_file"
printf 'Prüfsumme: %s.sha256\n' "$backup_file"

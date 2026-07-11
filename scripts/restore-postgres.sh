#!/bin/sh
set -eu

if [ "$#" -ne 2 ] || [ "$2" != "--confirm-production-restore" ]; then
  printf 'Verwendung: %s PFAD_ZUM_BACKUP --confirm-production-restore\n' "$0" >&2
  printf 'Achtung: Dieser Vorgang ersetzt den Inhalt der konfigurierten Datenbank.\n' >&2
  exit 2
fi

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
backup_file=$1
web_stopped=false

"$repo_root/scripts/verify-postgres-backup.sh" "$backup_file"

printf 'Vor dem Restore wird ein Sicherheitsbackup erstellt.\n'
"$repo_root/scripts/backup-postgres.sh"

restart_web() {
  if [ "$web_stopped" = true ]; then
    docker compose --project-directory "$repo_root" up -d web >/dev/null || true
  fi
}
trap restart_web EXIT HUP INT TERM

docker compose --project-directory "$repo_root" stop web
web_stopped=true

docker compose --project-directory "$repo_root" exec -T db \
  sh -c 'exec pg_restore --clean --if-exists --exit-on-error --no-owner --no-acl -U "$POSTGRES_USER" -d "$POSTGRES_DB"' \
  < "$backup_file"

docker compose --project-directory "$repo_root" up -d web
web_stopped=false
trap - EXIT HUP INT TERM

printf 'Restore abgeschlossen. Containerstatus und Anwendung jetzt manuell prüfen.\n'

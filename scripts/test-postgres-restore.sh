#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  printf 'Verwendung: %s PFAD_ZUM_BACKUP\n' "$0" >&2
  exit 2
fi

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
backup_file=$1
container="schule-restore-test-$$"
image=${POSTGRES_RESTORE_IMAGE:-postgres:17.10-bookworm}

"$repo_root/scripts/verify-postgres-backup.sh" "$backup_file"

cleanup() {
  docker rm -f "$container" >/dev/null 2>&1 || true
}
trap cleanup EXIT HUP INT TERM

printf 'Isolierte PostgreSQL-Instanz wird gestartet ...\n'
docker run -d --name "$container" \
  --tmpfs /var/lib/postgresql/data:rw,noexec,nosuid,size=512m \
  -e POSTGRES_DB=restore_test \
  -e POSTGRES_USER=restore_test \
  -e POSTGRES_PASSWORD=rein-kuenstliches-testpasswort \
  "$image" >/dev/null

attempt=0
until docker exec "$container" pg_isready -U restore_test -d restore_test >/dev/null 2>&1; do
  attempt=$((attempt + 1))
  if [ "$attempt" -ge 30 ]; then
    printf 'Fehler: Die isolierte PostgreSQL-Instanz wurde nicht rechtzeitig bereit.\n' >&2
    docker logs "$container" >&2
    exit 1
  fi
  sleep 1
done

docker exec -i "$container" pg_restore \
  --exit-on-error --no-owner --no-acl \
  -U restore_test -d restore_test < "$backup_file"

table_count=$(docker exec "$container" psql -U restore_test -d restore_test \
  -Atqc "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';")
migration_table=$(docker exec "$container" psql -U restore_test -d restore_test \
  -Atqc "SELECT to_regclass('public.django_migrations') IS NOT NULL;")

if [ "$table_count" -lt 1 ] || [ "$migration_table" != "t" ]; then
  printf 'Fehler: Die Wiederherstellung enthält nicht die erwartete Django-Struktur.\n' >&2
  exit 1
fi

printf 'Restore-Test erfolgreich: %s Tabellen in einer isolierten Instanz geprüft.\n' "$table_count"

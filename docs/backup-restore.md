# Backup und Wiederherstellung von PostgreSQL

## Schutzbedarf

Ein Datenbankbackup kann personenbezogene Daten, Passwort-Hashes und vollständige Zeugnisstände enthalten. Es darf deshalb weder in Git eingecheckt noch unverschlüsselt an öffentliche oder fremde Dienste übertragen werden. Das Backupskript setzt Verzeichnisrechte auf `0700` und Dateirechte auf `0600`.

Das persistente Docker-Volume ist kein Backup: Es schützt nicht vor versehentlichem Löschen, defekten Migrationen oder einem Ausfall des Servers.

## Backup erstellen

Voraussetzungen sind ein gesunder Compose-Datenbankdienst sowie Schreibzugriff auf das Zielverzeichnis:

```bash
./scripts/backup-postgres.sh
```

Standardmäßig entstehen im ignorierten Verzeichnis `backups/postgres/`:

```text
schule-postgres-YYYYMMDDTHHMMSSZ.dump
schule-postgres-YYYYMMDDTHHMMSSZ.dump.sha256
```

Das Skript erzeugt ein PostgreSQL-Custom-Format mit `pg_dump`, schreibt zunächst in eine temporäre Datei und verschiebt diese erst nach erfolgreichem Abschluss an den endgültigen Pfad. Eine Sperre verhindert parallele Läufe. Backups, die älter als 30 Tage sind, werden standardmäßig entfernt.

Ziel und Aufbewahrung können für einen einzelnen Lauf gesetzt werden:

```bash
BACKUP_DIR=/sicherer/pfad BACKUP_RETENTION_DAYS=60 ./scripts/backup-postgres.sh
```

Ein externes Backupziel muss verschlüsselt, zugriffsbeschränkt und datenschutzrechtlich freigegeben sein. Die lokale Aufbewahrung auf demselben Server allein schützt nicht vor einem Serverausfall.

## Backup prüfen

Die Prüfung vergleicht SHA-256 und lässt PostgreSQL das Archivverzeichnis lesen. Sie verändert keine Datenbank:

```bash
./scripts/verify-postgres-backup.sh backups/postgres/schule-postgres-YYYYMMDDTHHMMSSZ.dump
```

Eine Prüfsumme belegt Integrität, ersetzt aber keinen Wiederherstellungstest.

## Isolierten Restore-Test ausführen

Der Test startet einen kurzlebigen PostgreSQL-Container ohne veröffentlichten Port und mit einem `tmpfs`. Anschließend wird das Backup eingespielt und die erwartete Django-Datenbankstruktur geprüft. Personenbezogene Inhalte werden nicht ausgegeben. Der Container wird danach entfernt.

```bash
./scripts/test-postgres-restore.sh backups/postgres/schule-postgres-YYYYMMDDTHHMMSSZ.dump
```

Das verwendete Image entspricht standardmäßig der in `compose.yaml` festgelegten PostgreSQL-Version. Der Test muss regelmäßig und nach Änderungen an PostgreSQL, Backupskripten oder Datenbankschema erfolgreich laufen.

## Produktive Wiederherstellung

Die produktive Wiederherstellung ist destruktiv und darf nur in einem angekündigten Wartungsfenster mit ausdrücklicher Freigabe erfolgen. Vorher sind Backup, Prüfsumme, freier Speicher, verwendete PostgreSQL-Version und Rückfallweg zu prüfen.

Empfohlener Ablauf:

1. Anwendung in Wartung nehmen und betroffene Personen informieren.
2. Gewähltes Backup mit dem Prüfskript und in einer isolierten Instanz testen.
3. Ein zusätzliches aktuelles Sicherheitsbackup anlegen.
4. Erst dann den ausdrücklich bestätigten Restore starten.
5. Containerstatus, Migrationen, Anmeldung und fachliche Stichproben prüfen.
6. Zeitpunkt, ausführende Person und Ergebnis im Betriebsprotokoll dokumentieren.

Das Skript erzwingt einen eindeutigen Bestätigungsparameter, erstellt selbst ein Sicherheitsbackup und stoppt während des Imports den Webdienst:

```bash
./scripts/restore-postgres.sh \
  backups/postgres/schule-postgres-YYYYMMDDTHHMMSSZ.dump \
  --confirm-production-restore
```

Ein fehlgeschlagener Restore kann die Zieldatenbank teilweise verändert hinterlassen. In diesem Fall den Webdienst nicht für Benutzer freigeben, Logs sichern und anhand des unmittelbar zuvor erstellten Sicherheitsbackups kontrolliert zurückfallen.

## Tägliche Ausführung mit systemd

Die Dateien unter `deploy/systemd/` sind Vorlagen und verändern den Server nicht automatisch. Vor der Installation müssen folgende Platzhalter ersetzt werden:

- `__SERVICE_USER__` und `__SERVICE_GROUP__`: eingeschränktes Betriebskonto mit genau den erforderlichen Docker-Rechten
- `__PROJECT_DIR__`: absoluter Repository-Pfad
- `__BACKUP_DIR__`: absolutes, geschütztes Backupziel

Die Mitgliedschaft in der Docker-Gruppe gewährt weitreichende Rechte auf dem Server und ist entsprechend restriktiv zu vergeben.

Nach manueller Prüfung können Administratoren die beiden Dateien nach `/etc/systemd/system/` kopieren und anschließend ausführen:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now schule-postgres-backup.timer
sudo systemctl list-timers schule-postgres-backup.timer
sudo systemctl start schule-postgres-backup.service
sudo journalctl -u schule-postgres-backup.service
```

Erst ein erfolgreicher manueller Lauf und Restore-Test bestätigen die Einrichtung. Fehlermeldungen des Timers müssen überwacht werden; die Vorlage allein stellt noch kein Monitoring bereit.

## Regelmäßige Betriebskontrollen

- täglich: erfolgreicher Backup-Lauf, Dateigröße und freier Speicher
- mindestens monatlich: isolierter Restore-Test
- nach Schema- oder PostgreSQL-Änderungen: zusätzlicher Restore-Test
- regelmäßig: verschlüsselte externe Kopie und deren Wiederherstellbarkeit
- nach Ablauf der fachlich und rechtlich festgelegten Frist: kontrollierte Löschung

Die konkrete Aufbewahrungsfrist und das freigegebene externe Sicherungsziel sind noch fachlich beziehungsweise datenschutzrechtlich festzulegen.

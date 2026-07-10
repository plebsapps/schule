# Schulische Zeugnisverwaltung

Dieses Repository enthält die Planung und schrittweise Umsetzung einer webbasierten Zeugnisverwaltung für Schulen. Die Anwendung soll eine bestehende Excel- und Seriendrucklösung ablösen und sensible Schülerdaten innerhalb einer kontrollierten Serverumgebung verarbeiten.

Der aktuelle Stand ist das technische Grundgerüst: Django-Anmeldung, PostgreSQL, Docker Compose, Healthcheck und Basistests sind vorhanden. Fachmodule und ein Produktiv-Deployment folgen in späteren Phasen.

## Zielbild

Vorgesehen sind Django, PostgreSQL, Docker Compose, Nginx, pytest sowie eine serverseitige HTML-zu-PDF-Erzeugung. Zentrale Anforderungen sind rollenbasierte serverseitige Berechtigungen, unveränderliche freigegebene Zeugnisse, Versionierung, Audit-Protokollierung und Schutz vor Bearbeitungskonflikten.

Die fachlichen Anforderungen und Umsetzungsphasen stehen in [PLAN.md](PLAN.md). Die verbindlichen Arbeits-, Datenschutz- und Sicherheitsregeln stehen in [AGENTS.md](AGENTS.md).

## Voraussetzungen

- Git
- Docker Engine mit Docker Compose v2
- alternativ Python 3.13 für eine lokale Entwicklung ohne Docker

## Lokale Installation

```bash
git clone https://github.com/plebsapps/schule.git
cd schule
```

Kopiere anschließend die Beispielkonfiguration:

```bash
cp .env.example .env
```

Ersetze in `.env` zwingend `POSTGRES_PASSWORD` und `DJANGO_SECRET_KEY` durch lange, zufällige Werte. `.env` wird von Git ignoriert.

## Konfiguration

Die Laufzeitkonfiguration erfolgt über Umgebungsvariablen. `.env.example` dokumentiert alle derzeit benötigten Werte. Für den späteren HTTPS-Betrieb müssen insbesondere folgende Werte gesetzt sein:

```dotenv
DJANGO_DEBUG=false
DJANGO_ALLOWED_HOSTS=schule.plebsapps.de
DJANGO_CSRF_TRUSTED_ORIGINS=https://schule.plebsapps.de
DJANGO_SECURE_COOKIES=true
DJANGO_SECURE_SSL_REDIRECT=true
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=true
DJANGO_SECURE_HSTS_PRELOAD=false
```

Secrets und echte Schülerdaten dürfen nicht in das Repository gelangen.

## Start

Der projektbezogene Stack wird gebaut und gestartet mit:

```bash
docker compose up --build -d
docker compose ps
```

Die Anwendung ist anschließend ausschließlich lokal am Server unter `http://127.0.0.1:8005` erreichbar. Der öffentliche Zugriff über `https://schule.plebsapps.de` wird erst im separaten Nginx-/HTTPS-Schritt eingerichtet.

Ein Administratorkonto wird bewusst nicht automatisch mit einem Standardpasswort erstellt:

```bash
docker compose exec web python manage.py createsuperuser
```

Stoppen ohne Datenverlust:

```bash
docker compose down
```

`docker compose down -v` löscht die projektbezogene Datenbank und darf nur nach ausdrücklicher Prüfung verwendet werden.

## Tests

Tests und statische Prüfungen laufen in einer lokalen Python-Umgebung:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements/dev.txt
pytest
ruff check .
ruff format --check .
python manage.py check
python manage.py makemigrations --check --dry-run
```

Alle Testdaten sind künstlich.

## Migrationen

Die initiale Migration für das projektspezifische Benutzer-Modell liegt unter `apps/accounts/migrations/`. Der Webcontainer führt ausstehende Migrationen beim Start aus. Neue Datenbankänderungen dürfen ausschließlich über versionierte Django-Migrationen erfolgen.

## Deployment

Das vorgesehene Ziel ist `https://schule.plebsapps.de`. Docker veröffentlicht Django nur an `127.0.0.1:8005`. Die geprüften Nginx-Vorlagen und manuellen HTTPS-Schritte stehen in [docs/deployment.md](docs/deployment.md). Änderungen an Nginx oder Zertifikaten benötigen Administratorrechte und einen erfolgreichen `nginx -t` vor jedem Reload.

## Backup und Wiederherstellung

Backup- und Restore-Verfahren werden vor der Verarbeitung produktiver Daten implementiert und durch Wiederherstellungstests geprüft. Das Volume `schule-postgres-data` ist persistent, gilt allein jedoch nicht als Backup.

## Praxislehrbuch

Das Verzeichnis [buch/](buch/) dokumentiert die Zusammenarbeit mit Codex als Praxislehrbuch. Relevante Prompts werden dort sprachlich und typografisch überarbeitet wiedergegeben, ohne ihre fachliche Absicht zu verändern. Echte Schülerdaten, Secrets und sensible lokale Systemdetails sind ausgeschlossen.

## Git-Workflow

Die Entwicklung erfolgt auf thematisch benannten Feature-Branches. Änderungen gelangen über geprüfte Pull Requests in den Standard-Branch. Direkte Entwicklung auf `main` ist grundsätzlich nicht vorgesehen.

## Bekannte Einschränkungen

- Es existieren noch keine fachlichen Apps für Schüler, Klassen, Noten oder Zeugnisse.
- Rollen und fachliche Berechtigungen sind noch nicht implementiert.
- Nginx, HTTPS, Backup und Restore sind noch nicht eingerichtet.
- Konkrete Zeugnisvorlagen und anonymisierte Quelldaten müssen noch fachlich analysiert werden.
- Offene Fachfragen sind in `PLAN.md` aufgeführt.

## Datenschutz und Sicherheit

Dieses öffentliche Repository darf ausschließlich Quellcode, künstliche Testdaten und nicht sensible Dokumentation enthalten. Echte Schülerdaten, Zeugnisse, Zugangsdaten, Tokens, produktive Konfigurationen und Backups dürfen niemals veröffentlicht werden.

## Lizenz

Dieses Projekt ist unter der GNU General Public License Version 3 lizenziert. Einzelheiten stehen in [LICENSE](LICENSE).

# Quellenverzeichnis

## Geltungsbereich

Dieses Quellenverzeichnis bündelt die externen Primärquellen, auf denen zeitabhängige Produktinformationen und zentrale technische Aussagen des Buchs beruhen. Alle Links wurden am **12. Juli 2026** auf öffentliche Erreichbarkeit geprüft.

Produktfunktionen, Modellzugänge, Preise, Kommandos und Softwaredokumentation können sich nach diesem Datum ändern. Kapitelnahe Quellenhinweise bleiben deshalb zusätzlich erhalten: Das zentrale Verzeichnis erleichtert die Gesamtprüfung, ersetzt aber nicht den direkten Bezug zwischen Aussage und Quelle.

## OpenAI und Codex

### GPT-5.6 – allgemeine Verfügbarkeit

- Herausgeber: OpenAI
- Titel: *GPT-5.6: Frontier intelligence that scales with your ambition*
- Veröffentlichung: 9. Juli 2026
- Abruf: 12. Juli 2026
- Verwendung im Buch: Modellgeneration, Sol/Terra/Luna, Funktionen, Benchmarks, Verfügbarkeit, API-Preise und Sicherheit
- URL: [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/)

### GPT-5.6 – Vorschauankündigung

- Herausgeber: OpenAI
- Titel: *Previewing GPT-5.6 Sol: a next-generation model*
- Veröffentlichung: 26. Juni 2026
- Abruf: 12. Juli 2026
- Verwendung im Buch: zeitliche Einordnung der Vorschau, ursprüngliche Modellpositionierung und Sicherheitsansatz
- URL: [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/)

### GPT-5.6 in ChatGPT und Codex

- Herausgeber: OpenAI Help Center
- Titel: *GPT-5.6 in ChatGPT*
- Seitenstand bei der Prüfung: 10. Juli 2026
- Abruf: 12. Juli 2026
- Verwendung im Buch: Produkt- und Tarifverfügbarkeit, Codex-Mindestversionen, Reasoning-Stufen und Einschränkungen
- URL: [https://help.openai.com/en/articles/20001354](https://help.openai.com/en/articles/20001354)

### Codex-Kommandos

- Herausgeber: OpenAI
- Titel: *Developer commands*
- Abruf: 12. Juli 2026
- Verwendung im Buch: Codex-CLI-Kommandos, Diagnose, Sitzung, Kontext, Erweiterungen und Arbeitsweisen
- URL: [https://learn.chatgpt.com/docs/developer-commands?surface=cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

### Slash-Kommandos

- Herausgeber: OpenAI
- Titel: *Slash commands*
- Abruf: 12. Juli 2026
- Verwendung im Buch: Slash-Kommandos der ChatGPT-Desktop-App und Abgrenzung zu CLI-Befehlen
- URL: [https://learn.chatgpt.com/docs/reference/slash-commands](https://learn.chatgpt.com/docs/reference/slash-commands)

## Technische Primärquellen

### Django 5.2 LTS

- Herausgeber: Django Software Foundation
- Titel: *Django 5.2 release notes*
- Abruf: 12. Juli 2026
- Verwendung im Buch: Einordnung der verwendeten Django-LTS-Reihe
- URL: [https://docs.djangoproject.com/en/5.2/releases/5.2/](https://docs.djangoproject.com/en/5.2/releases/5.2/)

### Docker Compose

- Herausgeber: Docker, Inc.
- Titel: *Docker Compose documentation*
- Abruf: 12. Juli 2026
- Verwendung im Buch: deklarativer Mehrcontainerbetrieb, Build und Start der Projektumgebung
- URL: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

### PostgreSQL `pg_dump`

- Herausgeber: PostgreSQL Global Development Group
- Titel: *pg_dump — extract a PostgreSQL database into a script file or other archive file*
- Abruf: 12. Juli 2026
- Verwendung im Buch: logische Datenbanksicherung und Wiederherstellungsworkflow
- URL: [https://www.postgresql.org/docs/current/app-pgdump.html](https://www.postgresql.org/docs/current/app-pgdump.html)

### Python 3.13

- Herausgeber: Python Software Foundation
- Titel: *Python 3.13 Documentation*
- Abruf: 12. Juli 2026
- Verwendung im Buch: technische Grundlage der Django-Anwendung
- URL: [https://docs.python.org/3.13/](https://docs.python.org/3.13/)

### Pandoc

- Herausgeber: Pandoc-Projekt
- Titel: *Pandoc User’s Guide*
- Abruf: 12. Juli 2026
- Verwendung im Buch: reproduzierbare Erzeugung des EPUB3-Zwischenstands
- URL: [https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html)

### GNU General Public License Version 3

- Herausgeber: Free Software Foundation
- Titel: *GNU General Public License, version 3*
- Abruf: 12. Juli 2026
- Verwendung im Buch: Lizenz des freien Projekts
- URL: [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

## Interne Projektquellen

Die praktische Fallstudie beruht außerdem auf versionierten Dateien des Repositorys. Diese Quellen sind Teil des Projekts und benötigen keine externe Produktbehauptung:

- `AGENTS.md`: verbindliche Arbeits-, Sicherheits-, Datenschutz- und Git-Regeln
- `PLAN.md`: Ziel, Architektur und ursprünglicher Projektumfang
- `README.md`: Installation, Betrieb, Tests und bekannte Grenzen
- `compose.yaml` und `Dockerfile`: reproduzierbare Laufzeitumgebung
- `requirements/base.txt` und `requirements/dev.txt`: kontrollierte Python-Abhängigkeiten
- `tests/`: ausführbare Prüfungen mit künstlichen Daten
- `docs/`: Deployment-, Backup- und Wiederherstellungsdokumentation
- `buch/projektchronik.md`: redaktionelle Entstehungs- und Vollständigkeitskontrolle

## Redaktionelle Quellenregel

Für spätere Auflagen gelten vier Regeln:

1. Zeitabhängige Produktinformationen werden vor der Veröffentlichung erneut gegen offizielle Primärquellen geprüft.
2. Jede neue Quelle erhält Herausgeber, Titel, URL und Abrufdatum.
3. Herstellerangaben und projektspezifische Erfahrungen werden sprachlich voneinander getrennt.
4. Nicht mehr öffentlich erreichbare oder fachlich überholte Quellen werden ersetzt oder ausdrücklich als historische Quelle gekennzeichnet.

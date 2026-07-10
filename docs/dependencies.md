# Abhängigkeiten des technischen Grundgerüsts

Alle Versionen sind kontrolliert festgelegt. Aktualisierungen erfolgen über eigene, getestete Pull Requests.

| Abhängigkeit | Zweck | Lizenz | Sicherheitsrelevanz und Wartung | Alternative ohne Abhängigkeit |
|---|---|---|---|---|
| Django 5.2.16 LTS | Webframework, Authentifizierung, CSRF-Schutz, ORM und Migrationen | BSD-3-Clause | Sicherheitskritische Kernkomponente; LTS-Sicherheitsunterstützung bis April 2028 | Eigenentwicklung wäre sicherheitskritisch und fachlich nicht vertretbar |
| django-axes 8.3.1 | Sperre nach wiederholten Anmeldefehlern | MIT | Verhindert ungebremste Brute-Force-Versuche; aktives Jazzband-Projekt | Eigene Middleware wäre möglich, aber fehleranfälliger |
| psycopg 3.3.4 mit Binary-Extra | PostgreSQL-Treiber | LGPL-3.0-only | Datenbankzugriff; stabile, aktiv gepflegte Psycopg-3-Reihe | Systemweit kompiliertes `psycopg[c]` reduziert gebündelte Binärdateien, erhöht aber Build-Komplexität |
| Gunicorn 26.0.0 | Produktionsgeeigneter WSGI-Prozess | MIT | Begrenzt und verwaltet Webprozesse; aktiv gepflegt | Djangos Entwicklungsserver ist nicht produktionsgeeignet |
| WhiteNoise 6.12.0 | Auslieferung versionierter und komprimierter statischer Dateien aus dem isolierten Webcontainer | MIT | Produktionsstabile WSGI-Middleware; verhindert eine zusätzliche schreibbare Host-Freigabe zwischen Nginx und Container | Nginx könnte ein gemeinsames Host-Verzeichnis ausliefern, würde aber zusätzliche Volume- und Rechteverwaltung erfordern |
| pytest 9.1.1 | Testausführung | MIT | Nur Entwicklung und CI; aktiv gepflegt | Djangos integrierter Testrunner |
| pytest-django 4.12.0 | Django-Integration für pytest | BSD-3-Clause | Nur Entwicklung und CI; aktiv gepflegt | Djangos integrierter Testrunner |
| Ruff 0.15.20 | Linting und Formatprüfung | MIT | Nur Entwicklung und CI; aktiv gepflegt | Separate Werkzeuge wie Flake8, isort und Black |
| Python 3.13.14 Slim Bookworm | Laufzeitbasis des Webcontainers | PSF-2.0; Debian-Pakete mit eigenen Lizenzen | Offizielles Image mit festem Patchstand; regelmäßig aktualisieren | Selbst gepflegtes Basisimage erhöht Wartungsaufwand |
| PostgreSQL 17.10 Bookworm | Relationale Datenbank | PostgreSQL License | Offizielles Image mit festem Patchstand; Datenbank nicht nach außen veröffentlicht | Bestehende externe PostgreSQL-Instanz, jedoch mit höherem Betriebs- und Isolationsaufwand |

Die Binary-Variante von Psycopg ist für das reproduzierbare Grundgerüst pragmatisch. Vor einem gehärteten Produktivbetrieb wird geprüft, ob ein Build gegen systemeigene `libpq`-Pakete bevorzugt werden soll.

## Dokumentationswerkzeug

| Abhängigkeit | Zweck | Lizenz | Sicherheitsrelevanz und Wartung | Alternative ohne Abhängigkeit |
|---|---|---|---|---|
| Pandoc 3.10.0.0 im offiziellen Container `pandoc/core` | Wiederholbarer EPUB3-Export des Praxislehrbuchs | GPL-2.0-or-later; enthaltene Komponenten können eigene kompatible Lizenzen besitzen | Nur für lokale Dokumenterzeugung; kein Teil des Anwendungscontainers; versionsfestes offizielles Image | Manuelle EPUB-Erstellung wäre fehleranfällig; eine globale Pandoc-Installation würde den Server verändern |

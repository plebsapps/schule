# Projektchronik und Vollständigkeitskontrolle

Diese Chronik verhindert, dass wichtige Schritte der Zusammenarbeit im späteren Buch verloren gehen. Sie enthält keine Secrets, echten Schülerdaten oder unnötigen lokalen Systemdetails.

## Erfassungsstatus

| Abschnitt | Wesentliche Ereignisse | Dokumentiert in | Status |
|---|---|---|---|
| Projektstart | `PLAN.md`, `AGENTS.md`, Git-Repository, erster Commit | Kapitel 1 | erfasst |
| GitHub-Grundlage | zunächst privates Repository, später öffentlich, GPLv3 | Kapitel 1 | erfasst |
| Buchregeln | Prompts redaktionell überarbeiten, keine sensiblen Inhalte | Kapitel 1 und `buch/README.md` | erfasst |
| Git-Workflow | Feature-Branches, Draft-PRs, Prüfungen, Mergefreigaben | Kapitel 1 und Kommandoreferenz | erfasst |
| Serveranalyse | DNS, belegte Ports, vorhandene Container und Nginx geprüft | Kapitel 2 | erfasst |
| Django-Grundgerüst | Django 5.2 LTS, eigenes Usermodell, PostgreSQL, Gunicorn | Kapitel 2 | erfasst |
| Sicherheit | CSRF, sichere Cookies, HTTPS-Redirect, HSTS, Login-Sperre | Kapitel 2 | erfasst |
| Docker | Nicht-Root-Webcontainer, Healthchecks, Port 8005 | Kapitel 2 | erfasst |
| erster Laufzeitfehler | `collectstatic` scheiterte an Verzeichnisrechten | Kapitel 2 | erfasst |
| HTTPS | Nginx, Let's Encrypt, HTTP-Weiterleitung, Zertifikatsprüfung | Kapitel 2 | erfasst |
| Healthcheck-Korrektur | Produktivhost und Proxyprotokoll ergänzt | Kapitel 2 | erfasst |
| UI-Grundsystem | Login, Navigation, Dashboard, responsives CSS | Kapitel 3 | erfasst |
| Beispieldaten | flüchtig, künstlich, sichtbar als Demo gekennzeichnet | Kapitel 3 | erfasst |
| Staticfiles | `STATICFILES_DIRS`, WhiteNoise und Live-CSS-Prüfung | Kapitel 3 | erfasst |
| Codex-Grundlage | GPT-5.6 Sol, Oberflächen und Befehlsarten | Kapitel 4 | erfasst |
| Codex-Kommandos | App-, CLI-, Git-, Docker- und Django-Referenz | Kommandoreferenz | erfasst |
| Fachmodelle | Unterlagenanalyse, Stammdaten und Berechtigungen | zukünftige Kapitel | offen |
| Noten und Zeugnisse | Validierung, Locking, Freigabe, PDF, Versionen | zukünftige Kapitel | offen |
| Betrieb | Backup, Restore-Test, Monitoring, Aufbewahrung | zukünftige Kapitel | offen |

## Bisherige Pull Requests

| PR | Inhalt | Ergebnis |
|---|---|---|
| #1 | öffentliche Projektregeln, README und GPLv3 | gemergt |
| #2 | Django-Grundgerüst, PostgreSQL, Docker und Tests | gemergt |
| #3 | Nginx- und HTTPS-Vorbereitung | gemergt |
| #4 | erfolgreicher HTTPS-Betrieb dokumentiert | gemergt |
| #5 | UI-Grundsystem und künstliches Demo-Dashboard | gemergt |

## Wiederkehrender Abschlusscheck

Nach jeder größeren Aufgabe beantworten:

1. Ist der redaktionell verbesserte Benutzerprompt dokumentiert?
2. Sind Ausgangslage und Ziel verständlich?
3. Sind Analyse, Risiken und Entscheidung festgehalten?
4. Sind wichtige Codex-, Git-, Docker- und Testbefehle erfasst?
5. Sind Fehler und deren tatsächliche Ursachen dokumentiert?
6. Sind Datenschutz- und Sicherheitsauswirkungen beschrieben?
7. Sind Tests und Prüfergebnisse genannt?
8. Sind Commit, Branch und Pull Request nachvollziehbar?
9. Sind offene Punkte und manuelle Schritte sichtbar?
10. Enthält der Text keine echten Schülerdaten, Secrets oder sensiblen Systemdetails?

## Noch nachzuarbeiten

- vorhandene Kapitel bei der späteren Buchredaktion in ein einheitliches Drucklayout überführen
- Screenshots ausschließlich mit künstlichen Daten erstellen
- genaue Codex-, Docker-, Django- und Betriebsversionen pro Buchauflage erfassen
- Quellenverzeichnis für zeitabhängige Produktinformationen anlegen
- Glossar für Prompt, Kontext, Skill, Plugin, MCP, Sandbox, Migration und Pull Request erstellen

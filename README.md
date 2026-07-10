# Schulische Zeugnisverwaltung

Dieses Repository enthält die Planung und schrittweise Umsetzung einer webbasierten Zeugnisverwaltung für Schulen. Die Anwendung soll eine bestehende Excel- und Seriendrucklösung ablösen und sensible Schülerdaten innerhalb einer kontrollierten Serverumgebung verarbeiten.

Der aktuelle Stand ist die Planungsphase. Anwendungscode und produktive Konfigurationen sind noch nicht vorhanden.

## Zielbild

Vorgesehen sind Django, PostgreSQL, Docker Compose, Nginx, pytest sowie eine serverseitige HTML-zu-PDF-Erzeugung. Zentrale Anforderungen sind rollenbasierte serverseitige Berechtigungen, unveränderliche freigegebene Zeugnisse, Versionierung, Audit-Protokollierung und Schutz vor Bearbeitungskonflikten.

Die fachlichen Anforderungen und Umsetzungsphasen stehen in [PLAN.md](PLAN.md). Die verbindlichen Arbeits-, Datenschutz- und Sicherheitsregeln stehen in [AGENTS.md](AGENTS.md).

## Voraussetzungen

Für den aktuellen Planungsstand werden nur Git und ein Markdown-Editor benötigt. Die Voraussetzungen für die spätere Anwendung werden mit dem technischen Grundgerüst konkretisiert und versioniert dokumentiert.

## Lokale Installation

```bash
git clone https://github.com/plebsapps/schule.git
cd schule
```

Eine installierbare Anwendung existiert derzeit noch nicht.

## Konfiguration

Es gibt noch keine Laufzeitkonfiguration. Mit dem Django-Grundgerüst wird eine `.env.example` ohne echte Geheimnisse bereitgestellt. Secrets und echte Schülerdaten dürfen nicht in das Repository gelangen.

## Start

Die Anwendung kann im aktuellen Planungsstand noch nicht gestartet werden. Der spätere lokale Start über Docker Compose wird hier dokumentiert.

## Tests

Es existieren noch keine automatisierten Tests, da noch kein Anwendungscode vorhanden ist. Testbefehle und Qualitätsprüfungen werden mit dem technischen Grundgerüst ergänzt.

## Migrationen

Es existieren noch keine Datenbankmigrationen. Datenbankänderungen werden später ausschließlich über versionierte Django-Migrationen durchgeführt.

## Deployment

Ein Deployment ist noch nicht vorgesehen. Produktive Änderungen an Nginx, Docker-Ressourcen, Datenbanken oder Serverkonfigurationen erfolgen nicht automatisch und werden als manuelle, geprüfte Schritte dokumentiert.

## Backup und Wiederherstellung

Backup- und Restore-Verfahren werden vor der Verarbeitung produktiver Daten implementiert und durch Wiederherstellungstests geprüft. Aktuell gibt es noch keine Anwendungsdaten oder erzeugten Zeugnisse zu sichern.

## Praxislehrbuch

Das Verzeichnis [buch/](buch/) dokumentiert die Zusammenarbeit mit Codex als Praxislehrbuch. Relevante Prompts werden dort sprachlich und typografisch überarbeitet wiedergegeben, ohne ihre fachliche Absicht zu verändern. Echte Schülerdaten, Secrets und sensible lokale Systemdetails sind ausgeschlossen.

## Git-Workflow

Die Entwicklung erfolgt auf thematisch benannten Feature-Branches. Änderungen gelangen über geprüfte Pull Requests in den Standard-Branch. Direkte Entwicklung auf `main` ist grundsätzlich nicht vorgesehen.

## Bekannte Einschränkungen

- Das Projekt befindet sich in der Planungsphase.
- Es gibt noch keinen Django-Anwendungscode.
- Konkrete Zeugnisvorlagen und anonymisierte Quelldaten müssen noch fachlich analysiert werden.
- Offene Fachfragen sind in `PLAN.md` aufgeführt.

## Datenschutz und Sicherheit

Dieses öffentliche Repository darf ausschließlich Quellcode, künstliche Testdaten und nicht sensible Dokumentation enthalten. Echte Schülerdaten, Zeugnisse, Zugangsdaten, Tokens, produktive Konfigurationen und Backups dürfen niemals veröffentlicht werden.

## Lizenz

Dieses Projekt ist unter der GNU General Public License Version 3 lizenziert. Einzelheiten stehen in [LICENSE](LICENSE).

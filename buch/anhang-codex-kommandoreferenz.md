# Anhang: Codex-Kommandoreferenz

## Geltungsbereich und Stand

Stand: 10. Juli 2026. Befehle können abhängig von Oberfläche, Version, Betriebssystem, Modell, Berechtigungen und freigeschalteten Funktionen fehlen. In der aktiven Oberfläche zeigt `/` die tatsächlich verfügbaren Slash-Kommandos.

ChatGPT-Web besitzt ein eigenes Kommandomenü. Die folgenden Desktop- und CLI-Kommandos dürfen nicht ungeprüft auf ChatGPT-Web übertragen werden.

## Slash-Kommandos der ChatGPT-Desktop-App

| Kommando | Kurzbeschreibung |
|---|---|
| `/approve` | Genehmigt einmalig die Wiederholung einer kürzlich automatisch abgelehnten Aktion. |
| `/cloud` | Führt eine Aufgabe in der Cloud aus, sofern verfügbar. |
| `/cloud-environment` | Wählt die Cloud-Umgebung. |
| `/compact` | Verdichtet den Aufgabenkontext. |
| `/fast` | Schaltet eine verfügbare schnelle Servicestufe ein oder aus. |
| `/feedback` | Öffnet den Feedbackdialog und kann Protokolle beifügen. |
| `/fork` | Kopiert eine lokale Aufgabe in eine neue Aufgabe oder einen Worktree. |
| `/goal` | Setzt oder verwaltet ein dauerhaftes Arbeitsziel. |
| `/ide-context` | Schaltet gemeinsam genutzten IDE-Kontext ein oder aus. |
| `/init` | Erzeugt ein `AGENTS.md`-Grundgerüst. |
| `/local` | Führt die Aufgabe im ausgewählten lokalen Projekt aus. |
| `/mcp` | Zeigt den Status verbundener MCP-Server. |
| `/memories` | Konfiguriert die Verwendung oder Erzeugung von Memories. |
| `/model` | Wählt das Modell für die aktuelle Aufgabe. |
| `/pet` | Zeigt oder verbirgt das Desktop-Pet. |
| `/personality` | Wählt einen unterstützten Antwortstil. |
| `/plan` | Schaltet den Planungsmodus ein oder aus. |
| `/project` | Wählt ein Projekt für neue Aufgaben. |
| `/reasoning` | Wählt den Reasoning-Aufwand. |
| `/review` | Startet eine Codeprüfung. |
| `/side` | Öffnet eine vorübergehende Nebenunterhaltung. |
| `/status` | Zeigt Task-ID, Kontextverbrauch und Nutzungslimits. |
| `/task` | Startet eine Aufgabe ohne Projekt. |
| `/worktree` | Startet die Aufgabe in einem neuen Git-Worktree. |

## Slash-Kommandos der Codex CLI

### Sicherheit, Kontext und Erweiterungen

| Kommando | Kurzbeschreibung |
|---|---|
| `/permissions` | Ändert Freigabe- und Sandboxprofil der Sitzung. |
| `/approve` | Wiederholt einmalig eine automatisch abgelehnte Aktion. |
| `/ide` | Fügt verfügbaren IDE-Kontext zum nächsten Prompt hinzu. |
| `/sandbox-add-read-dir` | Gewährt unter Windows Lesezugriff auf ein zusätzliches Verzeichnis. |
| `/setup-default-sandbox` | Richtet unter Windows die erweiterte Standardsandbox ein. |
| `/apps` | Zeigt Apps beziehungsweise Konnektoren. |
| `/plugins` | Zeigt und verwaltet Plugins. |
| `/hooks` | Zeigt und verwaltet Lifecycle-Hooks. |
| `/mcp` | Listet konfigurierte MCP-Werkzeuge; `verbose` zeigt Details. |
| `/skills` | Wählt einen verfügbaren Skill. |
| `/memories` | Konfiguriert Memory-Verwendung und -Erzeugung. |
| `/import` | Importiert unterstützte Claude-Code-Konfigurationen und Sitzungen. |
| `/mention` | Hängt eine Datei oder einen Ordner an die Unterhaltung. |

### Modell und Arbeitsweise

| Kommando | Kurzbeschreibung |
|---|---|
| `/model` | Wählt Modell und gegebenenfalls Reasoning-Aufwand. |
| `/fast` | Schaltet eine verfügbare Fast-Stufe ein oder aus. |
| `/plan` | Wechselt in den Planungsmodus und akzeptiert optional einen Prompt. |
| `/goal` | Setzt, zeigt, bearbeitet, pausiert oder löscht ein dauerhaftes Ziel. |
| `/personality` | Wählt den Kommunikationsstil, sofern unterstützt. |
| `/review` | Prüft den aktuellen Arbeitsbaum. |
| `/side` oder `/btw` | Startet eine kurzlebige Nebenunterhaltung. |
| `/agent` oder `/subagents` | Wechselt zwischen Haupt- und Subagenten-Threads. |

### Sitzung und Verlauf

| Kommando | Kurzbeschreibung |
|---|---|
| `/clear` | Leert die Ansicht und beginnt eine neue Aufgabe. |
| `/new` | Startet eine neue Aufgabe in derselben CLI-Sitzung. |
| `/rename` | Benennt die aktuelle Aufgabe um. |
| `/resume` | Setzt eine gespeicherte Unterhaltung fort. |
| `/fork` | Verzweigt die aktuelle Aufgabe. |
| `/archive` | Archiviert die Sitzung und beendet Codex. |
| `/delete` | Löscht Sitzung und Nachfolger dauerhaft. |
| `/compact` | Fasst den Verlauf zusammen und gibt Kontext frei. |
| `/copy` | Kopiert die letzte abgeschlossene Codex-Antwort. |
| `/exit` oder `/quit` | Beendet die CLI. |
| `/app` | Setzt die Sitzung in der Desktop-App fort. |

### Prüfung, Diagnose und Anzeige

| Kommando | Kurzbeschreibung |
|---|---|
| `/diff` | Zeigt Git-Änderungen einschließlich unversionierter Dateien. |
| `/status` | Zeigt Modell, Freigaben, schreibbare Pfade und Kontextverbrauch. |
| `/usage` | Zeigt Tokenaktivität oder verfügbare Rate-Limit-Optionen. |
| `/debug-config` | Zeigt Konfigurationsschichten und Richtlinienquellen. |
| `/ps` | Zeigt Hintergrundterminals und aktuelle Ausgaben. |
| `/stop` | Stoppt Hintergrundterminals; `/clean` kann als Alias verfügbar sein. |
| `/statusline` | Konfiguriert die Statuszeile der Terminaloberfläche. |
| `/title` | Konfiguriert den Terminaltitel. |
| `/theme` | Wählt das Syntaxfarbschema. |
| `/raw` | Schaltet Roh-Scrollback für einfacheres Markieren um. |
| `/keymap` | Konfiguriert Tastenkürzel. |
| `/vim` | Schaltet Vim-Bedienung im Composer um. |
| `/pets` oder `/pet` | Wählt oder verbirgt ein Terminal-Pet. |
| `/feedback` | Sendet Feedback und Diagnoseinformationen. |
| `/experimental` | Schaltet experimentelle Funktionen; Neustart kann nötig sein. |
| `/init` | Erzeugt ein `AGENTS.md`-Grundgerüst. |
| `/logout` | Entfernt lokale Codex-Anmeldedaten. |

## Wichtige Codex-Terminalbefehle

| Befehl | Kurzbeschreibung |
|---|---|
| `codex` | Startet die interaktive Terminaloberfläche. |
| `codex app` | Öffnet die Desktop-App, sofern unterstützt. |
| `codex login` | Meldet Codex über einen unterstützten Authentifizierungsweg an. |
| `codex login status` | Prüft den Anmeldestatus. |
| `codex logout` | Entfernt gespeicherte Anmeldedaten. |
| `codex doctor` | Erstellt einen Diagnosebericht zu Installation, Konfiguration und Laufzeit. |
| `codex resume` | Setzt eine gespeicherte Sitzung fort. |
| `codex fork` | Verzweigt eine frühere Sitzung. |
| `codex review` | Führt eine nicht interaktive Codeprüfung aus. |
| `codex exec` | Führt Codex nicht interaktiv aus; Alias `codex e`. |
| `codex mcp` | Verwaltet MCP-Server. |
| `codex mcp-server` | Startet Codex selbst als MCP-Server. |
| `codex plugin` | Installiert, listet oder entfernt Plugins. |
| `codex plugin marketplace` | Verwaltet Plugin-Marktplätze. |
| `codex features` | Zeigt und verwaltet Feature-Flags. |
| `codex sandbox` | Führt Befehle in einer Codex-Sandbox aus. |
| `codex apply` | Übernimmt den neuesten Diff einer Cloud-Aufgabe. |
| `codex archive` | Archiviert eine gespeicherte Sitzung. |
| `codex unarchive` | Stellt eine archivierte Sitzung wieder her. |
| `codex delete` | Löscht eine gespeicherte Sitzung dauerhaft. |
| `codex update` | Prüft und installiert bei unterstützten Builds ein CLI-Update. |

Experimentelle Entwicklerbefehle werden im Buch nur dann ausführlich behandelt, wenn sie im Projekt tatsächlich eingesetzt werden. Ihre Einstufung kann sich kurzfristig ändern.

## Häufig im Projekt verwendete Git-Befehle

| Befehl | Zweck |
|---|---|
| `git status --short --branch` | Zeigt Branch und Arbeitsbaum kompakt. |
| `git switch -c <branch>` | Erstellt und aktiviert einen Feature-Branch. |
| `git diff --check` | Findet Whitespace-Fehler. |
| `git add <dateien>` | Staged nur ausdrücklich ausgewählte Dateien. |
| `git commit -m "..."` | Erstellt einen thematisch klaren Commit. |
| `git push -u origin <branch>` | Veröffentlicht den Feature-Branch. |
| `git pull --ff-only origin main` | Synchronisiert `main` ohne unbeabsichtigten Merge-Commit. |
| `gh pr create --draft ...` | Erstellt einen Draft-Pull-Request. |
| `gh pr view ...` | Prüft PR-, Review- und Merge-Status. |
| `gh pr merge ... --merge` | Mergt einen ausdrücklich freigegebenen Pull Request. |

## Häufig im Projekt verwendete Docker- und Django-Befehle

| Befehl | Zweck |
|---|---|
| `docker compose config --quiet` | Prüft die aufgelöste Compose-Konfiguration. |
| `docker compose up --build -d` | Baut und startet den Projektstack. |
| `docker compose up --build -d web` | Baut und ersetzt gezielt den Webdienst. |
| `docker compose ps` | Zeigt Container- und Healthstatus. |
| `docker compose logs --tail 100 web` | Zeigt aktuelle Webprotokolle. |
| `docker compose exec web python manage.py createsuperuser` | Legt interaktiv einen Administrator an. |
| `python manage.py check` | Führt Djangos Systemprüfung aus. |
| `python manage.py check --deploy` | Prüft produktionsbezogene Sicherheitseinstellungen. |
| `python manage.py makemigrations --check --dry-run` | Prüft auf fehlende Migrationen. |
| `pytest` | Führt automatische Tests aus. |
| `ruff check .` | Prüft Python-Code statisch. |
| `ruff format --check .` | Prüft die Formatierung. |

## Gefährliche oder besonders prüfpflichtige Befehle

Nicht als normale Abkürzung verwenden:

- Optionen zum vollständigen Umgehen von Sandbox und Freigaben
- `docker compose down -v` ohne Prüfung, da Volumes gelöscht werden
- `git reset --hard` oder erzwungene Pushes ohne ausdrückliche Freigabe
- ungeprüfte Änderungen unter `/etc`
- Befehle mit Passwörtern, Tokens oder Schülerdaten in Argumenten

## Quellenpflege

Vor jeder Druckfassung:

1. aktuelle Codex-Version notieren
2. in App und CLI `/` öffnen
3. Tabellen mit der offiziellen Referenz vergleichen
4. neue, entfernte oder umbenannte Befehle kennzeichnen
5. Beispiele erneut auf Sicherheits- und Datenschutzwirkung prüfen

Offizielle Referenzen für diesen Stand:

- [Codex Developer Commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- [Slash-Kommandos der ChatGPT-Desktop-App](https://learn.chatgpt.com/docs/reference/slash-commands)

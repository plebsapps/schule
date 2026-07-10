# Kapitel 4: GPT-5.6 Sol und die Codex-Oberflächen

## Ausgangslage

Das Praxislehrbuch soll nicht nur die entstehende Zeugnisverwaltung zeigen, sondern auch erklären, wie Codex bedient und sicher in einem echten Projekt eingesetzt wird. Dazu müssen Modell, Oberfläche und Befehlsart sauber getrennt werden.

## Redaktionell überarbeiteter Prompt

> Strukturiere das Praxislehrbuch zunächst übersichtlich und lege eine Codex-Befehlsreferenz an. Danach soll die Entwicklung der Webseite wieder Priorität erhalten. Das Buch muss alle wichtigen Ereignisse der Zusammenarbeit vollständig erfassen und GPT-5.6 Sol als Arbeitsgrundlage dokumentieren.

## Modellgrundlage

Dieses Buch verwendet GPT-5.6 Sol mit der Modell-ID `gpt-5.6-sol` als benannte Arbeitsgrundlage. Die Modellfamilie wurde von OpenAI im Juni 2026 zunächst als Vorschau vorgestellt. Aussagen über Verfügbarkeit, Preise oder konkrete Fähigkeiten sind zeitabhängig und müssen vor einer späteren Drucklegung erneut anhand offizieller Quellen geprüft werden.

Das Modell ist nur ein Teil der Arbeitsumgebung. Das tatsächliche Verhalten wird zusätzlich beeinflusst durch:

- Codex-Oberfläche und Version
- Projektregeln in `AGENTS.md`
- aktive Skills und Plugins
- Sandbox- und Freigaberichtlinien
- verfügbare Werkzeuge und Konnektoren
- aktuellen Gesprächskontext
- Benutzerprompt

## Vier Befehlsarten

### 1. Natürliche Prompts

Prompts beschreiben Ziel, Kontext, Grenzen und gewünschtes Ergebnis in normaler Sprache. Sie sind die wichtigste Steuerungsebene für fachliche Aufgaben.

Beispiel:

```text
Analysiere zuerst PLAN.md und die vorhandenen Tests. Erstelle danach nur einen Umsetzungsplan und verändere noch keine Dateien.
```

### 2. Slash-Kommandos

Slash-Kommandos steuern die aktuelle Codex-Oberfläche. Sie beginnen mit `/`, beispielsweise `/status`, `/plan` oder `/review`. Welche Befehle verfügbar sind, hängt von Oberfläche, Version, Zugriff und Umgebung ab. Die Eingabe `/` zeigt die aktuelle Liste.

### 3. Codex-CLI-Befehle

Terminalbefehle wie `codex doctor`, `codex resume` oder `codex review` starten oder verwalten Codex außerhalb des Gesprächskomponisten.

### 4. Projekt- und Systembefehle

Git-, Docker-, Django-, Nginx- oder Testbefehle werden von Codex oder vom Benutzer im Terminal ausgeführt. Beispiele sind `git status`, `docker compose ps`, `pytest` und `python manage.py check`.

## Codex-Oberflächen

### ChatGPT-Desktop-App

Die Desktop-App verbindet Aufgaben, lokale Projekte, Cloud-Ausführung, Plugins und weitere Werkzeuge. Ihre Slash-Kommandos sind auf Aufgabensteuerung ausgerichtet, beispielsweise `/goal`, `/project`, `/local`, `/cloud` und `/status`.

### Codex CLI

Die CLI ist eine terminalorientierte Oberfläche für lokale Repository-Arbeit. Sie besitzt zusätzliche Befehle für Berechtigungen, Git-Diffs, Modelle, Hintergrundterminals, Sessions und Diagnose.

### IDE-Erweiterung

Die IDE-Erweiterung kann offene Dateien und markierten Code als Kontext bereitstellen. Je nach Oberfläche wird dies über IDE-Kontextfunktionen oder `/ide` gesteuert.

### Cloud-Ausführung

Cloud-Aufgaben laufen in einer bereitgestellten Umgebung. Lokale Dateien, Zugriffsrechte und installierte Werkzeuge können sich von einer lokalen Sitzung unterscheiden.

## Warum `/mode` nicht pauschal dokumentiert wird

Der Begriff „Mode“ wird in Codex für verschiedene Arbeits- oder Ausführungsarten verwendet. Die aktuell geprüfte öffentliche Referenz führt jedoch keinen universellen Slash-Befehl `/mode` auf.

Je nach beabsichtigtem Wechsel werden stattdessen beispielsweise verwendet:

- `/plan` für Planungsmodus
- `/local` für lokale Ausführung in der Desktop-App
- `/cloud` für Cloud-Ausführung
- `/permissions` für Freigabe- und Sandboxverhalten in der CLI

Wenn `/mode` in einer bestimmten Installation sichtbar ist, muss das Buch Oberfläche und Version ausdrücklich nennen. Die Eingabe `/` in der jeweiligen Sitzung bleibt die zuverlässigste Bestandsaufnahme.

## Sicherheitsregel für Befehle

Ein Befehl ist nicht allein deshalb sicher, weil Codex ihn anbietet. Vor Ausführung sind mindestens zu prüfen:

- betroffene Dateien und Systeme
- Lese- oder Schreibwirkung
- mögliche Datenübertragung
- benötigte Freigaben
- Rücknahmeweg
- Umgang mit Secrets und personenbezogenen Daten

Besonders gefährliche Optionen, die Sandbox oder Freigaben vollständig umgehen, gehören nicht in normale Projektabläufe.

## Quellenstand

Die Referenz wurde am 10. Juli 2026 gegen die offiziellen OpenAI-Seiten zu Codex-Kommandos, Slash-Kommandos und GPT-5.6 Sol abgeglichen. Vor einer Druckauflage ist dieser Abgleich zu wiederholen.

Offizielle Ausgangsquellen:

- [GPT-5.6 Sol – OpenAI-Ankündigung](https://openai.com/index/previewing-gpt-5-6-sol/)
- [GPT-5.6 Sol, Terra und Luna – OpenAI-Hilfe](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-5-6-sol-terra-and-luna)
- [Codex Developer Commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)
- [Slash-Kommandos der ChatGPT-Desktop-App](https://learn.chatgpt.com/docs/reference/slash-commands)

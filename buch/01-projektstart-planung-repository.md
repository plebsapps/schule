# Kapitel 1: Projektstart, Planung und Repository-Anlage

## Ausgangslage

Das Projekt startet als schulische Zeugnisverwaltung. Weil später sensible personenbezogene Daten verarbeitet werden, mussten Datenschutz, Berechtigungsschutz, Nachvollziehbarkeit und Datenintegrität von Anfang an als verbindliche Leitplanken festgelegt werden.

Der erste praktische Schritt bestand nicht aus Anwendungscode, sondern aus Projektplanung und Arbeitsregeln:

- `PLAN.md` beschreibt Ziel, Architektur, fachliche Anforderungen, Risiken und Umsetzungsphasen.
- `AGENTS.md` beschreibt verbindliche Arbeitsregeln für Codex.
- Das GitHub-Repository `plebsapps/schule` wurde angelegt.
- Die beiden Dateien wurden als Initialstand committed und auf den Branch `main` gepusht.

## Erkenntnis 1: Gute Codex-Arbeit beginnt vor dem Code

Codex sollte bei einem sensiblen Fachprojekt nicht sofort mit Implementierung beginnen.

Wichtige vorbereitende Fragen sind:

- Welche Daten werden verarbeitet?
- Welche Risiken bestehen?
- Welche Architektur ist vorgesehen?
- Welche Regeln gelten für Sicherheit, Datenschutz und Tests?
- Welche Änderungen darf Codex selbst durchführen?
- Welche Änderungen brauchen ausdrückliche Freigabe?

Diese Regeln wurden in `AGENTS.md` festgehalten. Dadurch erhält Codex bei späteren Aufgaben eine klare Arbeitsgrundlage.

## Erkenntnis 2: `PLAN.md` und `AGENTS.md` haben unterschiedliche Aufgaben

`PLAN.md` beschreibt das Produkt und den Weg dorthin.

`AGENTS.md` beschreibt, wie Codex im Repository arbeiten soll.

Diese Trennung ist wichtig:

- Der Plan erklärt das fachliche und technische Ziel.
- Die Agentenregeln begrenzen und steuern die konkrete Arbeit.

Für ein Lehrbuch ist diese Trennung ein gutes Muster, weil sie zeigt, wie Projektwissen und Arbeitsregeln getrennt gepflegt werden können.

## Erkenntnis 3: Repository-Anlage ist ein eigener Arbeitsschritt

Die Repository-Anlage bestand aus mehreren nachvollziehbaren Schritten:

1. Bestehende Dateien prüfen.
2. Git-Repository lokal initialisieren.
3. Nur die gewünschten Dateien hinzufügen.
4. Einen klaren Initialcommit erstellen.
5. GitHub-Authentifizierung prüfen.
6. Remote-Repository anlegen.
7. Branch `main` pushen.
8. Remote-Stand verifizieren.

Der Initialcommit lautete:

```text
docs: add project planning documents
```

## Praktische Befehle

Die folgenden Befehle waren für diesen Schritt relevant:

```powershell
git init
git add AGENTS.md PLAN.md
git commit -m "docs: add project planning documents"
git branch -M main
git remote add origin https://github.com/plebsapps/schule.git
gh auth login -h github.com
gh repo create plebsapps/schule --private --description "Schulische Zeugnisverwaltung"
git push -u origin main
```

## Aufgetretene Blocker

### Ungültige GitHub-Anmeldung

Die GitHub CLI war installiert, aber der vorhandene Token war ungültig. Die Lösung war eine erneute Anmeldung:

```powershell
gh auth login -h github.com
```

### Netzwerkzugriff war eingeschränkt

Der erste Login-Versuch scheiterte wegen eingeschränktem Netzwerkzugriff in der Arbeitsumgebung. Der Login musste mit freigegebenem Netzwerkzugriff erneut ausgeführt werden.

### Git blockierte den Push wegen Repository-Eigentümer

Git meldete `dubious ownership`, weil das Repository in einer Sandbox initialisiert worden war und der spätere Push unter einem anderen Windows-Benutzer lief.

Die Lösung war ein gezielter `safe.directory`-Eintrag für dieses Projekt:

```powershell
git config --global --add safe.directory C:/dev/schule
```

## Sicherheitsentscheidung

Das GitHub-Repository wurde privat angelegt.

Begründung:

- Das Projekt betrifft perspektivisch sensible Schuldaten.
- Bereits Planungsdokumente enthalten Sicherheits- und Architekturüberlegungen.
- Ein privates Repository reduziert unnötige Offenlegung in der frühen Projektphase.

## Ergebnis

Nach dem ersten Schritt lagen vor:

- ein lokales Git-Repository
- ein privates GitHub-Repository
- `AGENTS.md`
- `PLAN.md`
- ein sauberer Initialcommit
- ein dokumentierter Arbeitsprozess für das spätere Lehrbuch

## Übertragbare Regel

Bei Projekten mit sensiblen Daten sollte Codex zuerst Regeln, Plan und Repository-Struktur stabilisieren. Erst danach sollte Anwendungscode entstehen.

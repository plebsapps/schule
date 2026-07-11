# Kapitel 1: Projektstart, Planung und Repository-Anlage

## Ausgangslage

Das Projekt startet als schulische Zeugnisverwaltung. Weil später sensible personenbezogene Daten verarbeitet werden, mussten Datenschutz, Berechtigungsschutz, Nachvollziehbarkeit und Datenintegrität von Anfang an als verbindliche Leitplanken festgelegt werden.

Der erste praktische Schritt bestand nicht aus Anwendungscode, sondern aus Projektplanung und Arbeitsregeln:

- `PLAN.md` beschreibt Ziel, Architektur, fachliche Anforderungen, Risiken und Umsetzungsphasen.
- `AGENTS.md` beschreibt verbindliche Arbeitsregeln für Codex.
- Das GitHub-Repository `plebsapps/schule` wurde zunächst privat angelegt und später für die offene Weiterentwicklung vorbereitet.
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

[Bild001]

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

[Bild002]

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

## Weiterentwickelte Sicherheitsentscheidung

Das GitHub-Repository wurde in der ersten Projektphase privat angelegt. Später fiel die Entscheidung, Quellcode und allgemeine Projektdokumentation unter der GPLv3 öffentlich weiterzuentwickeln.

Für ein öffentliches Repository gelten deshalb verbindliche Grenzen:

- keine echten Schülerdaten oder Zeugnisse
- keine Secrets, Zugangstokens oder produktiven Konfigurationen
- keine Backups oder sensiblen lokalen Systemdetails
- ausschließlich künstliche und anonymisierte Testdaten

Die Veröffentlichung des Quellcodes bedeutet ausdrücklich nicht, dass die später verarbeiteten Schuldaten öffentlich sein dürfen.

[Bild003]

## Ergebnis

Nach dem ersten Schritt lagen vor:

- ein lokales Git-Repository
- ein zunächst privates GitHub-Repository mit dokumentiertem Weg zur öffentlichen GPLv3-Veröffentlichung
- `AGENTS.md`
- `PLAN.md`
- ein sauberer Initialcommit
- ein dokumentierter Arbeitsprozess für das spätere Lehrbuch

## Übertragbare Regel

Bei Projekten mit sensiblen Daten sollte Codex zuerst Regeln, Plan und Repository-Struktur stabilisieren. Erst danach sollte Anwendungscode entstehen.

## Redaktionell überarbeitete Prompts

Die folgenden Arbeitsaufträge wurden für die Druckfassung sprachlich überarbeitet. Inhalt und Absicht wurden nicht verändert.

### Arbeitsauftrag: Projektregeln und Plan lesen

> Lies zunächst die Dateien `AGENTS.md` und `PLAN.md` vollständig. Nimm noch keine Änderungen vor, da weitere Ergänzungen folgen.

### Arbeitsauftrag: Buch, Git-Workflow, README und Lizenz

> Ergänze die Projektregeln und Dokumentation um folgende Punkte:
>
> 1. Die relevanten Prompts sollen im Praxislehrbuch gespeichert werden. Für die Druckfassung sind Rechtschreibung, Grammatik und Form zu verbessern, ohne die fachliche Absicht zu verändern.
> 2. Halte in `AGENTS.md` fest, dass nicht direkt auf dem Standard-Branch gearbeitet wird. Für jedes Feature ist ein eigener Branch anzulegen; die Integration in den Standard-Branch erfolgt professionell über Git und GitHub.
> 3. Erstelle eine `README.md` im Wurzelverzeichnis des Repositorys.
> 4. Stelle das GitHub-Repository auf öffentlich um und lizenziere das Projekt unter der GPLv3.

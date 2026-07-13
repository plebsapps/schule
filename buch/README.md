# Arbeiten mit OpenAI Codex

**Praxisbeispiel am Beispiel einer schulischen Zeugnisverwaltung**

Dieses Verzeichnis sammelt die Erkenntnisse aus der praktischen Arbeit mit Codex an diesem Projekt.

Ziel dieses Praxisbeispiels ist es, nicht nur fertige Ergebnisse zu zeigen, sondern den Arbeitsprozess nachvollziehbar zu machen:

- Wie wird ein Projekt mit Codex gestartet?
- Welche Informationen braucht Codex vor der Umsetzung?
- Wie werden Regeln in `AGENTS.md` formuliert?
- Wie wird ein Plan in `PLAN.md` gepflegt?
- Wie werden GitHub, Git und lokale Dateien sauber zusammengeführt?
- Welche Fehler treten in der Praxis auf und wie werden sie gelöst?

Alle Inhalte müssen ohne echte Schülerdaten, ohne Secrets und ohne produktive Zugangsdaten auskommen. Davon getrennt ist das ausdrücklich öffentliche Read-only-Demokonto, dessen Kennwort nur für künstliche Show-case-Daten gilt und nicht als Secret behandelt wird.

## Projekt ansehen und sicher anmelden

Die Demonstration ist unter [https://schule.plebsapps.de](https://schule.plebsapps.de) öffentlich über das Internet erreichbar und enthält ausschließlich künstliche Daten. Ein echtes Produktivsystem mit Schuldaten würde dagegen nur im Schulnetz beziehungsweise von zu Hause über eine bereitgestellte VPN-Verbindung betrieben.

Für Leserinnen und Leser gibt es das Konto `Buch`. Es darf die künstlichen Show-case-Daten ansehen, aber keine Datensätze anlegen, ändern oder löschen. Auch eine eigenständige Passwortänderung ist für dieses verwaltete Lesekonto gesperrt.

URL, Benutzername und das bewusst öffentliche Demo-Kennwort stehen im Zugangskasten am Anfang von Kapitel 10. Dieses Kennwort darf niemals für ein anderes Konto oder ein System mit echten Daten wiederverwendet werden.

## Öffentliches GitHub-Repository

Der nachvollziehbare Projektstand liegt unter [https://github.com/plebsapps/schule](https://github.com/plebsapps/schule). Das öffentliche Repository enthält Quellcode, Buchmanuskript, künstliche Testdaten und technische Dokumentation. Echte Schülerdaten, produktive Zugangsdaten, Secrets, Datenbankbackups und echte Zeugnisse gehören niemals hinein. Ausgenommen ist nur das ausdrücklich freigegebene Kennwort des öffentlichen Read-only-Demokontos.

Das Projekt steht unter der GNU General Public License Version 3 (GPLv3). Issues dienen der nachvollziehbaren Beschreibung von Fehlern und Vorschlägen. Änderungen können über eigene Branches und Pull Requests geprüft werden. GitHub-Releases bewahren veröffentlichte Zwischenstände und zugehörige Downloadartefakte auf.

Repository und E-Book erfüllen unterschiedliche Aufgaben: Das Repository zeigt Quellen und Entwicklungsgeschichte. Veröffentlichte Buchfassungen werden außerhalb des Buchtexts bereitgestellt und einem dokumentierten Projektstand zugeordnet.

## Modell- und Dokumentationsgrundlage

Dieses Praxisbeispiel entsteht auf Grundlage der Projektarbeit mit GPT-5.6 Sol (`gpt-5.6-sol`). Die Befehls- und Funktionsbeschreibungen beziehen sich auf den dokumentierten Stand vom 12. Juli 2026.

Modellzugang, Codex-Oberflächen und Kommandos können sich ändern. Deshalb nennt jede Referenz die zugehörige Oberfläche und unterscheidet zwischen dauerhaftem Arbeitsprinzip und versionsabhängiger Bedienung.

## Buchstruktur

- [Vorwort: Grundlagen, Voraussetzungen und bewusste Abgrenzung](Vorwort.md)

### Teil I: Projekt und Ausgangslage

1. Projektstart, Planung und Repository-Anlage
2. Vom Plan zum technischen Django-Grundgerüst
3. Professionelles UI-Grundsystem und sichere Beispieldaten

### Teil II: Codex verstehen und bedienen

4. GPT-5.6 Sol, Codex-Oberflächen und Befehlsarten
5. Was ist neu in GPT-5.6?
6. GPT-5.6 Sol, Terra und Luna im Vergleich

### Teil III: Praktische Weiterentwicklung

7. Backups entwerfen und Wiederherstellungen beweisen
8. Mit unbekannten Fachdetails sicher beginnen
9. Eine kleine Demo fachlich vollständig machen

### Teil IV: Show-case-Abschluss

10. Show-case-Abschluss, Systemstart und Lesekonto

### Anhang

- [Über den Autor](Author.md)
- [Codex-Kommandoreferenz](anhang-codex-kommandoreferenz.md)
- [Glossar](glossar.md)
- [Quellenverzeichnis](quellenverzeichnis.md)
- [Projektchronik und Vollständigkeitskontrolle](projektchronik.md)
- [Bildverzeichnis und Generierungsbriefings](bildkonzept.md)
- Git-, Docker- und Betriebsbefehle
- Checklisten

## Vorhandene Kapitel

- [Kapitel 1: Projektstart, Planung und Repository-Anlage](01-projektstart-planung-repository.md)
- [Kapitel 2: Vom Plan zum technischen Grundgerüst](02-django-grundgeruest.md)
- [Kapitel 3: Ein professionelles UI mit sicheren Beispieldaten](03-ui-grundsystem-beispieldaten.md)
- [Kapitel 4: GPT-5.6 Sol und die Codex-Oberflächen](04-gpt-5-6-sol-codex-oberflaechen.md)
- [Kapitel 5: Was ist neu in GPT-5.6?](05-was-ist-neu-in-gpt-5-6.md)
- [Kapitel 6: GPT-5.6 Sol, Terra und Luna im Vergleich](06-sol-terra-luna-vergleich.md)
- [Kapitel 7: Backups entwerfen und Wiederherstellungen beweisen](07-backup-und-wiederherstellung.md)
- [Kapitel 8: Mit unbekannten Fachdetails sicher beginnen](08-stammdaten-ohne-vorlagen.md)
- [Kapitel 9: Eine kleine Demo fachlich vollständig machen](09-demo-noten-und-zeugnis.md)
- [Kapitel 10: Show-case-Abschluss, Systemstart und Lesekonto](10-showcase-abschluss-lesekonto-systemd.md)

## Redaktion der Prompts

Projektbezogene Prompts werden als Bestandteil der jeweiligen Kapitel dokumentiert. Der einmalige redaktionelle Hinweis zu ihrer Darstellung steht im Vorwort; die Kapitel verwenden danach nur noch die kurzen Überschriften „Prompt“ oder „Arbeitsauftrag“.

Vor der Aufnahme werden echte personenbezogene Daten, Secrets, Zugangstokens und sensible lokale Systemdetails entfernt oder durch künstliche Platzhalter ersetzt.

## Vollständigkeitsprinzip

Nach jeder größeren Aufgabe werden Kapitel, Kommandoreferenz und Projektchronik geprüft. Die Chronik dient als Inhaltsregister: Ein Ereignis gilt für das Buch erst dann als erfasst, wenn Ausgangslage, Prompt, Entscheidung, wichtige Befehle, Prüfungen, Blocker, Sicherheitsaspekte und Ergebnis dokumentiert oder eindeutig einem geplanten Kapitel zugeordnet sind.

Zum dokumentierten Show-case-Abschluss gehören auch der systemd-Autostart des Compose-Stacks und das nur lesende Buchkonto `Buch`. Dessen Kennwort wird für die öffentliche Demo bewusst abgedruckt; produktive Kennwörter bleiben weiterhin ausgeschlossen.

## Bildkonzept

Die Buchgrafiken sind im Manuskript fortlaufend als `[Bild001]`, `[Bild002]` und so weiter nummeriert. Das [Bildverzeichnis](bildkonzept.md) beschreibt für jede Nummer Platzierung, Lernziel, Format, Pflichtinhalte, Datenschutzgrenzen und den verwendbaren Generierungsprompt. Die fertigen Dateien liegen im Ordner `Bilder/` und werden aus dem Manuskript direkt referenziert.

## Transparenz und Entstehung

![Bild022: Buchtransparenz und Autor](../Bilder/bild022-buchtransparenz-autor.png)

Diese zusätzliche Grafik macht die Entstehung des Praxisbeispiels, die verwendeten Arbeitsartefakte und die Dokumentationsidee sichtbar.

## EPUB-Zwischenstand erzeugen

Der EPUB-Export verwendet ein fest versioniertes offizielles Pandoc-Containerimage und benötigt keine globale Pandoc-Installation:

```bash
./scripts/build-book-epub.sh
```

Die Ausgabe entsteht unter:

```text
buch/build/arbeiten-mit-codex-zwischenstand.epub
```

`buch/build/` enthält generierte Ausgaben und wird nicht versioniert. Maßgebliche Quellen bleiben die Markdown-Dateien, `metadata.yaml` und `epub.css`.

## Veröffentlichte Zwischenstände

Geprüfte EPUB-Zwischenstände werden als GitHub-Prereleases veröffentlicht. Dadurch bleiben Binärdateien aus der Git-Historie heraus, sind aber direkt über das öffentliche Repository abrufbar.

- [Praxisbeispiel – Zwischenstand 2026-07-10](https://github.com/plebsapps/schule/releases/tag/book-preview-2026-07-10)
- [EPUB direkt herunterladen](https://github.com/plebsapps/schule/releases/download/book-preview-2026-07-10/arbeiten-mit-codex-zwischenstand.epub)

Die Release-Notizen nennen Quell-Commit, Buildwerkzeug und SHA-256-Prüfsumme. Ein veröffentlichter Download wird nach dem Upload erneut heruntergeladen und gegen die lokale Prüfsumme verglichen.

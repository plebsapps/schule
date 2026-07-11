# Praxislehrbuch Arbeiten mit Codex

Dieses Verzeichnis sammelt die Erkenntnisse aus der praktischen Arbeit mit Codex an diesem Projekt.

Ziel ist ein späteres Lehrbuch, das nicht nur fertige Ergebnisse zeigt, sondern den Arbeitsprozess nachvollziehbar macht:

- Wie wird ein Projekt mit Codex gestartet?
- Welche Informationen braucht Codex vor der Umsetzung?
- Wie werden Regeln in `AGENTS.md` formuliert?
- Wie wird ein Plan in `PLAN.md` gepflegt?
- Wie werden GitHub, Git und lokale Dateien sauber zusammengeführt?
- Welche Fehler treten in der Praxis auf und wie werden sie gelöst?

Alle Inhalte müssen ohne echte Schülerdaten, ohne Secrets und ohne produktive Zugangsdaten auskommen.

## Modell- und Dokumentationsgrundlage

Dieses Praxislehrbuch entsteht auf Grundlage der Projektarbeit mit GPT-5.6 Sol (`gpt-5.6-sol`). Die Befehls- und Funktionsbeschreibungen beziehen sich auf den dokumentierten Stand vom 10. Juli 2026.

Modellzugang, Codex-Oberflächen und Kommandos können sich ändern. Deshalb nennt jede Referenz die zugehörige Oberfläche und unterscheidet zwischen dauerhaftem Arbeitsprinzip und versionsabhängiger Bedienung.

## Buchstruktur

### Teil I: Projekt und Ausgangslage

1. Projektstart, Planung und Repository-Anlage
2. Vom Plan zum technischen Django-Grundgerüst
3. Professionelles UI-Grundsystem und sichere Beispieldaten

### Teil II: Codex verstehen und bedienen

4. GPT-5.6 Sol, Codex-Oberflächen und Befehlsarten
5. Backups entwerfen und Wiederherstellungen beweisen
6. Mit unbekannten Fachdetails sicher beginnen

### Teil III: Praktische Weiterentwicklung

7. Eine kleine Demo fachlich vollständig machen

### Geplante Vertiefung

8. Gute Prompts und dauerhafte Projektregeln
9. Berechtigungen, Sandbox und sichere Ausführung
10. Fachmodelle und Migrationen
11. Rollen und serverseitige Berechtigungen
12. Noteneingabe, Konfliktschutz und Freigabe
13. Zeugnisversionen und PDF-Erzeugung
14. Import und Audit

### Anhang

- [Codex-Kommandoreferenz](anhang-codex-kommandoreferenz.md)
- [Projektchronik und Vollständigkeitskontrolle](projektchronik.md)
- [Bildverzeichnis und Generierungsbriefings](bildkonzept.md)
- Git-, Docker- und Betriebsbefehle
- Glossar und Checklisten

## Vorhandene Kapitel

- [Transparenz: Wie dieses Buch entstanden ist](00-transparenz.md)
- [Über den Autor – redaktionelle Vorlage](00-ueber-den-autor.md)
- [Redaktionelles Inhaltsverzeichnis](00-inhaltsverzeichnis.md)
- [Kapitel 1: Projektstart, Planung und Repository-Anlage](01-projektstart-planung-repository.md)
- [Kapitel 2: Vom Plan zum technischen Grundgerüst](02-django-grundgeruest.md)
- [Kapitel 3: Ein professionelles UI mit sicheren Beispieldaten](03-ui-grundsystem-beispieldaten.md)
- [Kapitel 4: GPT-5.6 Sol und die Codex-Oberflächen](04-gpt-5-6-sol-codex-oberflaechen.md)
- [Kapitel 5: Backups entwerfen und Wiederherstellungen beweisen](05-backup-und-wiederherstellung.md)
- [Kapitel 6: Mit unbekannten Fachdetails sicher beginnen](06-stammdaten-ohne-vorlagen.md)
- [Kapitel 7: Eine kleine Demo fachlich vollständig machen](07-demo-noten-und-zeugnis.md)

## Redaktion der Prompts

Projektbezogene Prompts werden als Bestandteil der jeweiligen Kapitel dokumentiert. Für eine lesbare Druckfassung werden Rechtschreibung, Grammatik, Zeichensetzung und Struktur verbessert. Die fachliche Absicht bleibt dabei unverändert; die Buchfassung wird als redaktionell überarbeiteter Prompt gekennzeichnet und nicht als wörtliches Transkript ausgegeben.

Vor der Aufnahme werden echte personenbezogene Daten, Secrets, Zugangstokens und sensible lokale Systemdetails entfernt oder durch künstliche Platzhalter ersetzt.

## Vollständigkeitsprinzip

Nach jeder größeren Aufgabe werden Kapitel, Kommandoreferenz und Projektchronik geprüft. Die Chronik dient als Inhaltsregister: Ein Ereignis gilt für das Buch erst dann als erfasst, wenn Ausgangslage, Prompt, Entscheidung, wichtige Befehle, Prüfungen, Blocker, Sicherheitsaspekte und Ergebnis dokumentiert oder eindeutig einem geplanten Kapitel zugeordnet sind.

## Bildkonzept

Geplante Grafiken werden im Manuskript fortlaufend als `[Bild001]`, `[Bild002]` und so weiter markiert. Das [Bildverzeichnis](bildkonzept.md) beschreibt für jede Nummer Platzierung, Lernziel, Format, Pflichtinhalte, Datenschutzgrenzen und einen direkt nutzbaren DALL·E-Prompt. Die eigentliche Bilderzeugung erfolgt getrennt; bis dahin bleiben die Platzhalter im EPUB sichtbar. Aktuell sind 22 Motive geplant.

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

- [Praxislehrbuch – Zwischenstand 2026-07-10](https://github.com/plebsapps/schule/releases/tag/book-preview-2026-07-10)
- [EPUB direkt herunterladen](https://github.com/plebsapps/schule/releases/download/book-preview-2026-07-10/arbeiten-mit-codex-zwischenstand.epub)

Die Release-Notizen nennen Quell-Commit, Buildwerkzeug und SHA-256-Prüfsumme. Ein veröffentlichter Download wird nach dem Upload erneut heruntergeladen und gegen die lokale Prüfsumme verglichen.

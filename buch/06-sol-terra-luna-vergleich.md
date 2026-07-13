# Kapitel 6: GPT-5.6 Sol, Terra und Luna im Vergleich

## Arbeitsauftrag

> Erkläre die Unterschiede zwischen GPT-5.6 Sol, Terra und Luna. Stelle Einsatzzweck, Stärken, Grenzen, Geschwindigkeit, Kosten und Verfügbarkeit anhand offizieller Quellen gegenüber. Ergänze eine drucktaugliche Vergleichstabelle und eine Entscheidungshilfe mit datenschutzkonformen Praxisbeispielen aus dem Projekt.

Die Bezeichnungen wurden vor der Ausarbeitung anhand offizieller OpenAI-Quellen geprüft. Die korrekte Schreibweise lautet **Sol**, **Terra** und **Luna**. Es handelt sich nicht um drei Reasoning-Stufen desselben Modells, sondern um Leistungsstufen innerhalb der Modellgeneration GPT-5.6.

## Drei Stufen statt eines Modells für jede Aufgabe

OpenAI beschreibt Sol als Flaggschiff und leistungsfähigste Stufe, Terra als ausgewogene Variante für die tägliche Arbeit und Luna als schnellste und kostengünstigste Variante. Die Zahl 5.6 bezeichnet die Generation; die Namen kennzeichnen dauerhafte Leistungsstufen, die sich nach Angaben des Herstellers in einem eigenen Rhythmus weiterentwickeln können.

Diese Einteilung löst ein praktisches Problem: Nicht jeder Arbeitsauftrag benötigt dieselbe maximale Modellleistung. Eine Architekturentscheidung mit Sicherheitsfolgen stellt andere Anforderungen als die Suche nach einer Datei oder eine kurze sprachliche Korrektur. Wer immer automatisch die größte Variante wählt, kann unnötig Zeit und Kosten verursachen. Wer ausschließlich die schnellste Variante nutzt, riskiert dagegen bei schwierigen Aufgaben eine oberflächliche Analyse.

## Vergleich auf einen Blick

Stand der folgenden Angaben: **12. Juli 2026**.

| Merkmal | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna |
|---|---|---|---|
| offizielle Rolle | Flaggschiff und leistungsfähigste Stufe | ausgewogene Stufe für tägliche Arbeit | schnellste und kostengünstigste Stufe |
| Modell-ID | `gpt-5.6-sol` | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Schwerpunkt | höchste Qualität für komplexe Aufgaben | gutes Verhältnis aus Qualität, Tempo und Kosten | kurze Laufzeit und niedrige Kosten |
| typische Wahl | schwierige Architektur, lange Analysen, anspruchsvolle Agentenarbeit | regelmäßige Entwicklung, Tests, Dokumentation und Reviews | schnelle Recherche, Klassifikation und klar begrenzte Routineaufgaben |
| API-Eingabe je 1 Mio. Token | 5,00 US-Dollar | 2,50 US-Dollar | 1,00 US-Dollar |
| API-Ausgabe je 1 Mio. Token | 30,00 US-Dollar | 15,00 US-Dollar | 6,00 US-Dollar |
| wichtige Grenze | höherer Zeit- und Kostenbedarf kann für einfache Aufgaben unnötig sein | bei besonders schwierigen Aufgaben kann Sol mehr Leistungsreserve bieten | Geschwindigkeit ersetzt keine tiefe fachliche oder sicherheitskritische Prüfung |

Die Preisangaben beziehen sich ausschließlich auf den veröffentlichten API-Stand. ChatGPT- und Codex-Zugänge werden zusätzlich durch Produkt, Tarif, Workspace-Regeln und Nutzungslimits bestimmt. Preise und Verfügbarkeit müssen vor jeder neuen Buchauflage erneut geprüft werden.

## GPT-5.6 Sol: maximale Leistungsreserve

Sol ist für die schwierigsten Aufgaben der Familie vorgesehen. OpenAI ordnet dieser Stufe die höchste Leistungsfähigkeit bei Softwareentwicklung, professioneller Wissensarbeit, Forschung, Computerbenutzung und Cybersicherheit zu. In den veröffentlichten Evaluationen erreicht Sol häufig die stärksten Werte der drei Stufen. Kapitel 5 zeigt dazu eine ausgewählte, differenzierte Benchmarktabelle.

Im Projekt ist Sol besonders sinnvoll, wenn viele voneinander abhängige Entscheidungen gleichzeitig berücksichtigt werden müssen. Beispiele sind:

- ein Datenmodell entwerfen, das historische Zeugnisdaten nicht verfälscht,
- Berechtigungen über Schule, Klasse, Fach und Zeugnisstatus hinweg prüfen,
- einen schwer reproduzierbaren Fehler über Anwendung, Container und Reverse Proxy verfolgen,
- eine größere Änderung einschließlich Tests, Dokumentation und Sicherheitsfolgen planen,
- mehrere unabhängige Teilanalysen mit Unteragenten koordinieren.

Sol ist dennoch keine Freigabeinstanz. Auch die stärkste Modellstufe kann eine Anforderung missverstehen, einen Benchmarkvorteil nicht auf den konkreten Fall übertragen oder eine fachlich falsche Annahme überzeugend formulieren. Gerade bei umfangreichen Ergebnissen müssen Diff, Tests, Quellen und fachliche Entscheidung sorgfältig geprüft werden.

## GPT-5.6 Terra: ausgewogen für den Arbeitsalltag

Terra ist die mittlere Leistungsstufe. OpenAI beschreibt sie als ausgewogene Variante für die tägliche Arbeit und als kostengünstigere Option mit einer Leistung, die insgesamt mit GPT-5.5 konkurriert. In mehreren veröffentlichten Coding- und Agenten-Evaluationen liegt Terra vor GPT-5.5; einzelne Tests zeigen jedoch geringere oder nur ähnliche Werte. Terra sollte deshalb nicht als „Sol zum halben Preis“ missverstanden werden.

Für viele normale Codex-Aufgaben ist Terra eine naheliegende Ausgangswahl:

- vorhandene Django-Modelle und Tests analysieren,
- eine klar abgegrenzte Formularänderung implementieren,
- Tests ergänzen und verständliche Fehlermeldungen formulieren,
- Dokumentation und Prompts pflegen,
- einen Pull Request zusammenfassen oder auf Konsistenz prüfen,
- bekannte Betriebsabläufe anhand vorhandener Anleitungen kontrollieren.

Terra bietet einen Mittelweg: mehr Reserve als eine rein auf Geschwindigkeit optimierte Variante, aber geringere API-Kosten als Sol. Wenn die Aufgabe während der Analyse deutlich komplexer wird, sollte nicht blind weitergearbeitet werden. Dann ist es sinnvoll, Umfang und Risiken neu zu bewerten und gegebenenfalls Sol einzusetzen.

## GPT-5.6 Luna: schnell für klar begrenzte Arbeit

Luna ist die schnellste und günstigste Stufe der Familie. Sie eignet sich besonders für Aufgaben mit engem Umfang, eindeutiger Fragestellung und leicht überprüfbarem Ergebnis. Beispiele sind:

- bestimmte Dateinamen oder Verweise in einem Repository suchen,
- eine kurze Liste aus vorhandenem Text strukturieren,
- einfache Formulierungen sprachlich vereinheitlichen,
- bekannte Prüfergebnisse zusammenfassen,
- Daten in ungefährliche Kategorien einordnen,
- kleine mechanische Änderungen vorbereiten, deren Diff sofort kontrolliert wird.

Luna ist nicht automatisch die richtige Wahl für sicherheitskritische Entscheidungen, nur weil sie schneller antwortet. Bei Berechtigungsmodellen, Datenmigrationen, Wiederherstellungen oder komplexen Ursachenanalysen kann die niedrigere Leistungsreserve entscheidend sein. Außerdem zeigen die offiziellen Benchmarks, dass Luna in einigen Aufgaben nahe an GPT-5.5 liegt oder darüber hinausgeht, in anderen aber darunter bleibt.

## Entscheidungshilfe für die Praxis

Die Auswahl sollte nicht allein nach dem Namen erfolgen. Vier Fragen helfen bei der Entscheidung:

1. Wie groß und verzweigt ist die Aufgabe?
2. Welche Folgen hätte ein übersehener Fehler?
3. Wie leicht lässt sich das Ergebnis prüfen?
4. Sind Geschwindigkeit oder Kosten für diesen Schritt tatsächlich entscheidend?

| Situation | Empfohlener Start | Begründung | Wechselkriterium |
|---|---|---|---|
| kurze Suche oder klarer Textumbau | Luna | enger Umfang und leicht prüfbares Ergebnis | zu Terra wechseln, sobald mehrere Dateien oder fachliche Abhängigkeiten betroffen sind |
| normale Feature-Arbeit mit Tests | Terra | ausgewogen für regelmäßige Entwicklung und Dokumentation | zu Sol wechseln, wenn Architektur, Sicherheit oder viele Teilbereiche zusammenkommen |
| komplexe Architektur- oder Sicherheitsanalyse | Sol | höchste Leistungsreserve für lange, mehrstufige Überlegungen | Aufgabe trotzdem verkleinern, wenn Ergebnis nicht mehr überschaubar prüfbar ist |
| parallele unabhängige Teilanalysen | Sol mit geeigneter Agentenarbeit | komplexe Koordination und Synthese | keine parallelen Schreibzugriffe auf dieselben Dateien zulassen |
| wiederholbare Routineprüfung | Luna oder Terra | Tempo und Kosten können wichtiger sein als maximale Tiefe | bei widersprüchlichen Ergebnissen mit Sol oder menschlicher Fachexpertise nachprüfen |

Die Empfehlung ist keine technische Zugriffsgarantie. Welche Stufen auswählbar sind, hängt von Oberfläche, Plan und Workspace-Einstellungen ab.

## Praxisbeispiele aus der Zeugnisverwaltung

### Beispiel 1: CSS-Regel im EPUB prüfen

Eine vorhandene CSS-Regel soll so ergänzt werden, dass Bilder zentriert bleiben. Die Änderung ist klein, der betroffene Dateibereich bekannt und das Ergebnis lässt sich im erzeugten EPUB prüfen. Luna kann für die erste Analyse genügen. Sobald unterschiedliche EPUB-Reader, Cover-SVG und Regressionstests gemeinsam betrachtet werden, bietet Terra mehr Reserve.

### Beispiel 2: Stammdatenformular ergänzen

Ein vorhandenes, serverseitig geschütztes Django-Formular erhält ein zusätzliches optionales Feld. Modelle, Migration, Formular, Berechtigungen und Tests sind betroffen, aber die Architektur ist bekannt. Terra ist dafür eine sinnvolle Ausgangswahl. Wird aus dem Feld später eine historische, versionierte Fachinformation, sollte die Aufgabe neu bewertet werden.

### Beispiel 3: Freigegebene Zeugnisse korrigieren

Eine Korrekturfunktion muss alte Versionen erhalten, eine neue PDF-Datei erzeugen, eine Prüfsumme speichern und die Freigabe protokollieren. Ein Fehler könnte historische Dokumente verfälschen. Hier ist Sol wegen Umfang, Risiko und zahlreicher Invarianten die angemessene Wahl. Trotzdem bleibt eine fachliche Freigabe zwingend.

### Beispiel 4: Projektchronik redaktionell ordnen

Vorhandene, bereits geprüfte Ereignisse sollen sprachlich vereinheitlicht und chronologisch sortiert werden. Terra kann Textverständnis und Konsistenz gut verbinden. Für eine rein mechanische Rechtschreibprüfung einzelner Absätze kann Luna ausreichen. Sol wäre erst dann sinnvoll, wenn aus vielen Quellen eine vollständige, widerspruchsfreie Entstehungsgeschichte rekonstruiert werden muss.

## Geschwindigkeit, Kosten und Qualität richtig verstehen

Die drei Ziele stehen nicht in einem einfachen linearen Verhältnis. Ein schnelleres Modell kann eine kleine Aufgabe früher abschließen, während ein stärkeres Modell bei einer schwierigen Aufgabe möglicherweise weniger Korrekturschleifen benötigt. Niedrigere Tokenpreise bedeuten ebenfalls nicht automatisch geringere Gesamtkosten: Wiederholte fehlgeschlagene Versuche können einen Preisvorteil aufzehren.

Eine praktische Kostenbetrachtung umfasst daher mehr als die API-Tabelle:

- Anzahl und Länge der benötigten Anfragen,
- Umfang von Eingabe und Ausgabe,
- Zahl der Werkzeugaufrufe und Korrekturschleifen,
- Zeit für menschliche Prüfung,
- mögliche Folgen eines übersehenen Fehlers.

Für dieses Buch werden keine Modellstufen automatisch nach Kosten gewechselt. Die Wahl richtet sich zuerst nach Aufgabe und Risiko. Kosten- und Geschwindigkeitsvorteile werden nur genutzt, wenn die notwendige Qualität und Prüfbarkeit erhalten bleiben.

## Verfügbarkeit nach Oberfläche

Zum Redaktionsstand waren Sol, Terra und Luna über die OpenAI API verfügbar. In Codex konnten Free- und Go-Zugänge Terra verwenden; Plus-, Pro-, Business- und Enterprise-Zugänge konnten nach der offiziellen Beschreibung zwischen Sol, Terra und Luna wählen. In normalen ChatGPT-Unterhaltungen waren Terra und Luna nicht direkt auswählbar, während sie in ChatGPT Work abhängig vom Plan zur Verfügung standen.

Diese Zuordnung kann sich kurzfristig ändern. Das Buch beschreibt deshalb nicht nur den Modellnamen, sondern immer auch Oberfläche, Version und Redaktionsdatum. Wenn eine Stufe im Modellwähler fehlt, beweist dies nicht, dass sie allgemein abgeschafft wurde; Plan, Workspace-Verwaltung, Rollout und regionale Verfügbarkeit müssen ebenfalls geprüft werden.

## Datenschutz und Modellwahl

Keine der drei Varianten ändert die Datenschutzgrenze dieses Projekts. Echte Schülerdaten, Zeugnisse, Passwörter und Zugangstokens dürfen nicht für externe Modellanfragen verwendet werden. Auch die günstigste oder schnellste Variante erhält dadurch keine weitergehende Erlaubnis.

Für Praxisbeispiele werden ausschließlich künstliche Daten verwendet. Produktive Probleme werden über anonymisierte Strukturen, Fehlermuster und lokal geprüfte Protokolle untersucht. Die Modellwahl bestimmt Leistungsprofil und Aufwand, nicht die zulässige Datenmenge.

## Merksatz

> Sol ist die Wahl für maximale Leistungsreserve, Terra für ausgewogene tägliche Arbeit und Luna für schnelle, klar begrenzte Aufgaben. Entscheidend ist jedoch nicht der Modellname allein, sondern ob Aufgabe, Risiko und Prüfbarkeit zur gewählten Stufe passen.

## Quellen

Abrufdatum aller Quellen: **12. Juli 2026**.

- OpenAI: [GPT-5.6: Frontier intelligence that scales with your ambition](https://openai.com/index/gpt-5-6/), veröffentlicht am 9. Juli 2026.
- OpenAI Help Center: [GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354), Stand laut Seite: 10. Juli 2026.
- OpenAI: [Previewing GPT-5.6 Sol: a next-generation model](https://openai.com/index/previewing-gpt-5-6-sol/), veröffentlicht am 26. Juni 2026.

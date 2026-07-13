# Kapitel 5: Was ist neu in GPT-5.6?

## Redaktionell überarbeiteter Arbeitsauftrag

> Ergänze das Praxisbeispiel um ein Kapitel mit dem Titel „Was ist neu in GPT-5.6?“. Erkläre die wichtigsten Veränderungen gegenüber den direkten Vorgängern anhand offizieller Quellen. Das Kapitel soll Vergleichstabellen und konkrete Praxisbeispiele enthalten. Aktualisiere außerdem Inhaltsverzeichnis, Kapitelnummerierung, Build-Reihenfolge und alle weiteren betroffenen Buchstellen.

Die Buchfassung verbessert Rechtschreibung und Satzbau des ursprünglichen Arbeitsauftrags, ohne dessen fachliche Absicht zu erweitern.

## Redaktionsstand und Einordnung

Dieses Kapitel beschreibt den öffentlich dokumentierten Stand vom **12. Juli 2026**. OpenAI veröffentlichte GPT-5.6 zunächst am 26. Juni 2026 als begrenzte Vorschau und kündigte am 9. Juli 2026 die allgemeine Verfügbarkeit der Modellfamilie an. Solche Produktangaben können sich nach der Drucklegung ändern. Deshalb sind Verfügbarkeit, Preise, Modellnamen und Oberflächen keine zeitlosen Eigenschaften, sondern Aussagen mit einem festen Redaktionsdatum.

GPT-5.6 ist eine Modellgeneration. **Sol**, **Terra** und **Luna** sind nach der offiziellen Beschreibung dauerhafte Leistungsstufen innerhalb dieser Generation. Sol ist die leistungsfähigste Stufe, Terra ist auf ein ausgewogenes Verhältnis von Leistung und Kosten ausgelegt, und Luna priorisiert Geschwindigkeit und niedrige Kosten. Der ausführliche Vergleich dieser drei Stufen folgt in einem eigenen Kapitel. Hier geht es zunächst um die Veränderungen der Generation GPT-5.6 gegenüber GPT-5.5.

## Der Schritt von GPT-5.5 zu GPT-5.6

Eine neue Modellnummer bedeutet nicht automatisch, dass jede Antwort in jeder Situation besser ausfällt. OpenAI beschreibt GPT-5.6 vor allem als Fortschritt bei länger laufender professioneller Wissensarbeit, Softwareentwicklung, Werkzeug- und Computerbenutzung, Wissenschaft sowie Cybersicherheit. Die veröffentlichten Evaluationen unterstützen diese Einordnung in vielen Bereichen, zeigen aber auch, dass nicht jede Modellstufe in jedem einzelnen Test vor GPT-5.5 liegt.

Für die Praxis ist deshalb eine differenzierte Aussage sinnvoller als ein pauschales „neuer ist immer besser“:

| Bereich | GPT-5.5 | Neuer Schwerpunkt bei GPT-5.6 | Bedeutung für die Praxis |
|---|---|---|---|
| Softwareentwicklung | leistungsfähige Grundlage für Coding-Aufgaben | stärkere agentische Terminal- und Werkzeugabläufe | komplexe Änderungen können über mehr Arbeitsschritte geplant, umgesetzt und geprüft werden |
| Wissensarbeit | gute Text- und Analyseleistung | stärkere lange Analysen, Recherche und strukturierte Arbeitsergebnisse | umfangreiche Anforderungen lassen sich besser mit Dokumentation und Prüfschritten verbinden |
| Computerbenutzung | vorhandene Browser- und Bedienfähigkeiten | verbesserte agentische Browser- und Computeraufgaben | Oberflächen können zuverlässiger in einen mehrstufigen Ablauf einbezogen werden |
| Dokumente und Tabellen | Erzeugung und Bearbeitung möglich | bessere Beachtung von Vorlagen, Layoutsystemen und komplexen Formaten | wiederholbare Berichte und strukturierte Arbeitsunterlagen profitieren besonders |
| Effizienz | abhängig von Aufgabe und Modellwahl | mehr Leistung pro eingesetztem Token und verschiedene Leistungsstufen | nicht jede Aufgabe benötigt automatisch die größte Modellstufe |
| Sicherheit | bestehende Schutzmechanismen | verstärkte, mehrschichtige Schutzmaßnahmen für leistungsfähigere Modelle | legitime Sicherheitsarbeit bleibt möglich, risikoreiche Anfragen können stärker geprüft oder abgelehnt werden |

Diese Tabelle beschreibt Schwerpunkte, keine Garantie für ein einzelnes Projekt. Ein Modell kann bei einer konkreten Aufgabe trotz besserer Durchschnittswerte Fehler machen, Anforderungen missverstehen oder eine technisch plausible, aber fachlich falsche Lösung vorschlagen.

## Ausgewählte offizielle Vergleichswerte

Benchmarks helfen bei der Einordnung, bilden aber niemals den gesamten Arbeitsalltag ab. Die folgende Auswahl stammt aus der offiziellen GPT-5.6-Veröffentlichung. Sie wurde bewusst klein gehalten und enthält sowohl deutliche Fortschritte als auch Werte, bei denen die Unterschiede gering oder uneinheitlich sind.

| Evaluation | GPT-5.5 | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna | Einordnung |
|---|---:|---:|---:|---:|---|
| Terminal-Bench 2.1 | 85,6 % | 88,8 % | 87,4 % | 84,7 % | Sol und Terra liegen vorn; Luna liegt in diesem Test knapp hinter GPT-5.5 |
| SWE-Bench Pro | 59,4 % | 64,6 % | 63,4 % | 62,7 % | alle drei GPT-5.6-Stufen erreichen höhere Werte |
| BrowseComp | 84,4 % | 90,4 % | 87,5 % | 83,3 % | Sol und Terra verbessern sich; Luna liegt leicht darunter |
| OSWorld 2.0 | 47,5 % | 62,6 % | 50,2 % | 45,6 % | besonders deutlicher Fortschritt bei Sol |
| AutomationBench | 12,9 % | 18,1 % | 15,2 % | 14,9 % | alle drei Stufen erreichen höhere Werte |
| MMMU Pro ohne Werkzeuge | 81,2 % | 83,0 % | 80,7 % | 78,4 % | nur Sol liegt in dieser Messung über GPT-5.5 |

Die Werte dürfen nicht miteinander vermischt oder auf beliebige Aufgaben übertragen werden. Sie wurden mit bestimmten Testaufbauten, Werkzeugen und Einstellungen ermittelt. Selbst ein hoher Benchmarkwert beweist nicht, dass eine konkrete Änderung im Schulprojekt korrekt, sicher oder datenschutzkonform ist.

## Neue Stufen für gründlicheres Arbeiten

Mit GPT-5.6 führte OpenAI die Reasoning-Stufe `max` ein. Sie gibt dem Modell mehr Raum für besonders anspruchsvolle Überlegungen. Zusätzlich nutzt `ultra` Unteragenten, um komplexe Aufgaben aufzuteilen und Teilergebnisse zusammenzuführen. In Codex ist `ultra` laut Veröffentlichung für Plus- und höherwertige Pläne vorgesehen; konkrete Verfügbarkeit kann vom Produkt, Tarif und Einführungsstand abhängen.

Mehr Rechenaufwand ist nicht automatisch für jede Aufgabe sinnvoll. Eine kleine Textkorrektur benötigt keine mehrstufige Agentenarbeit. Dagegen kann eine Aufgabe wie „Analysiere Berechtigungen, Migrationen, Tests und Dokumentation einer fachlichen Änderung“ von einer systematischen Aufteilung profitieren.

| Arbeitsweise | Geeignet für | Weniger geeignet für | Erforderliche Kontrolle |
|---|---|---|---|
| normale Reasoning-Stufe | klar begrenzte Änderungen und kurze Analysen | stark verzweigte Aufgaben mit vielen Abhängigkeiten | Diff, Tests und fachliche Plausibilität prüfen |
| `max` | schwierige Architektur-, Analyse- und Fehlersuchaufgaben | triviale Änderungen mit eindeutigem Lösungsweg | zusätzlichen Aufwand gegen tatsächlichen Nutzen abwägen |
| `ultra` mit Unteragenten | unabhängige Teilanalysen, große Repositorys und parallele Prüfungen | Aufgaben, deren Teilschritte dieselben Dateien gleichzeitig verändern | Zuständigkeiten trennen und Gesamtergebnis konsistent zusammenführen |

## Programmatic Tool Calling und Multi-Agent-Arbeit

Für die Responses API beschreibt OpenAI **Programmatic Tool Calling**: Das Modell kann Programme im Speicher schreiben und ausführen, die Werkzeuge koordinieren und Zwischenergebnisse verarbeiten. Daneben wurde Multi-Agent-Unterstützung zunächst als Beta eingeführt. Dabei arbeiten mehrere Unteragenten parallel an abgegrenzten Teilaufgaben; das Modell führt ihre Ergebnisse anschließend zusammen.

Für Codex lässt sich daraus ein allgemeines Arbeitsprinzip ableiten: Nicht jede große Aufgabe muss als ein einziger unübersichtlicher Schritt bearbeitet werden. Gute Teilaufgaben haben einen klaren Umfang, möglichst wenig Überschneidung und ein prüfbares Ergebnis. Parallelisierung ist besonders sinnvoll, wenn beispielsweise ein Agent die Tests analysiert, ein zweiter die Dokumentation prüft und ein dritter eine unabhängige Sicherheitsbetrachtung erstellt. Mehrere Agenten sollten dagegen nicht unkoordiniert dieselbe Datei bearbeiten.

Die Funktion nimmt dem Menschen die Freigabe nicht ab. Ein zusammengeführtes Ergebnis muss weiterhin gegen Anforderungen, Repository-Regeln und Tests geprüft werden.

## Vorhersehbareres Prompt-Caching

GPT-5.6 führte laut OpenAI explizite Cache-Grenzen und eine Mindestlebensdauer von 30 Minuten für Prompt-Caches ein. Prompt-Caching kann wiederkehrende große Kontexte effizienter machen, etwa stabile Systemregeln oder umfangreiche Referenztexte. Für normale Codex-Nutzung ist jedoch entscheidend, dass Caching keine inhaltliche Aktualität garantiert. Eine zwischengespeicherte Anweisung bleibt nur so gut wie ihr Inhalt.

Im Schulprojekt dürfen sensible Schülerdaten auch dann nicht unnötig an externe Dienste übertragen werden, wenn eine Caching-Funktion technisch verfügbar ist. Datenschutzregeln stehen über möglichen Geschwindigkeits- oder Kostenvorteilen.

## Praxisbeispiele aus diesem Projekt

### Beispiel 1: Eine fachliche Änderung vorbereiten

Auftrag: Eine neue Funktion zur Noteneingabe soll geplant werden.

GPT-5.6 kann die Analyse in Datenmodell, Berechtigungen, Validierung, Konfliktschutz, Tests und Dokumentation gliedern. Der Nutzen liegt nicht darin, möglichst viel Code auf einmal zu erzeugen. Entscheidend ist, Abhängigkeiten früh zu erkennen und die Änderung in kontrollierbare Schritte zu teilen.

Die menschliche Kontrolle bleibt notwendig: Stimmen Notenskala und Rollenmodell? Werden freigegebene Daten geschützt? Enthalten Tests ausschließlich künstliche Daten?

### Beispiel 2: Einen Fehler über mehrere Ebenen verfolgen

Auftrag: Die Anwendung antwortet nach einem Deployment mit einem Gateway-Fehler.

Eine mehrstufige Untersuchung kann Containerstatus, Healthcheck, Gunicorn, Host-Konfiguration und Reverse Proxy getrennt prüfen. GPT-5.6 kann Werkzeugergebnisse zusammenführen und wahrscheinliche Ursachen gegeneinander abgrenzen. Trotzdem darf es nicht ohne Freigabe globale Nginx-, Firewall- oder systemd-Konfigurationen verändern.

### Beispiel 3: Buch und Anwendung gemeinsam pflegen

Auftrag: Eine neue Funktion soll implementiert, getestet und anschließend für das Praxisbeispiel dokumentiert werden.

Hier müssen Quellcode, Tests, Betriebsdokumentation, Projektchronik, redaktionell überarbeiteter Prompt und EPUB-Build zusammenpassen. Ein leistungsfähigeres Modell kann diese Querverbindungen leichter verfolgen. Die verbindliche Vollständigkeitskontrolle bleibt dennoch notwendig, weil kein Modell allein garantieren kann, dass wirklich jede betroffene Stelle erkannt wurde.

### Beispiel 4: Datenschutz als unveränderliche Grenze

Auftrag: Ein Problem mit einem Zeugnisdatensatz soll analysiert werden.

Auch GPT-5.6 darf keine echten Schülerdaten an externe Dienste erhalten. Für Analyse, Tests und Dokumentation werden künstliche Datensätze oder vollständig anonymisierte Strukturen verwendet. Höhere Modellleistung erweitert die technischen Möglichkeiten, nicht die datenschutzrechtliche Erlaubnis.

| Praxisaufgabe | Möglicher Vorteil von GPT-5.6 | Unverzichtbare Absicherung |
|---|---|---|
| Repository analysieren | mehr Abhängigkeiten und längere Abläufe zusammenhängend betrachten | zuerst `PLAN.md`, Regeln, Status und Tests prüfen |
| Implementierung planen | Teilaufgaben und Risiken genauer strukturieren | Annahmen kennzeichnen und keine irreversible Entscheidung vorwegnehmen |
| Code ändern | Werkzeuge und Prüfungen über mehrere Schritte koordinieren | Feature-Branch, kleine Diffs, Review und Tests |
| Fehler suchen | Log-, Konfigurations- und Laufzeithinweise gemeinsam bewerten | keine Secrets ausgeben und keine Produktionsdaten verändern |
| Dokumentation erstellen | technische Arbeit in nachvollziehbare Lernschritte übersetzen | Fakten, Versionen und Quellen redaktionell prüfen |

## Was GPT-5.6 nicht verändert

Ein neues Modell ersetzt keine professionelle Arbeitsweise. Für dieses Projekt gelten weiterhin dieselben Grundsätze:

- `AGENTS.md` und `PLAN.md` müssen vor Änderungen berücksichtigt werden.
- Lese- und Schreibberechtigungen werden serverseitig geprüft.
- Änderungen entstehen auf einem eigenen Branch und werden nachvollziehbar geprüft.
- Tests bleiben erforderlich, auch wenn der erzeugte Code überzeugend aussieht.
- Fehlgeschlagene Prüfungen dürfen nicht ausgeblendet werden.
- Echte Schülerdaten, Passwörter und Zugangstokens gehören weder in Prompts noch in das Buch.
- Externe Serveränderungen benötigen eine ausdrückliche Freigabe.
- Fachliche Entscheidungen bleiben bei den verantwortlichen Menschen.

Gerade ein leistungsfähigeres Modell kann umfangreichere Änderungen erzeugen. Dadurch steigt nicht nur der mögliche Nutzen, sondern auch die Menge dessen, was vor einer Freigabe verstanden und kontrolliert werden muss.

## Verfügbarkeit ist Teil der Versionsangabe

Zum Redaktionsstand war GPT-5.6 in ChatGPT, Codex und der OpenAI API verfügbar, jedoch abhängig von Produkt, Tarif, Workspace-Einstellungen und laufendem Rollout. Die OpenAI-Hilfe nannte für Codex mindestens die Desktop-App-Version 26.707.30751 beziehungsweise die Codex-CLI-Version 0.144.0. Solche Mindestversionen altern schnell und gehören deshalb nicht als zeitlose Bedienregel in das Buch.

Auch die Modellwahl unterscheidet sich nach Oberfläche. In normalen ChatGPT-Unterhaltungen sind Terra und Luna nicht direkt auswählbar; in Codex und der API stehen sie je nach Zugang zur Verfügung. Leserinnen und Leser sollten daher stets zuerst prüfen, welche Oberfläche, Version und Berechtigung tatsächlich vorliegt.

## Grenzen der veröffentlichten Aussagen

Die verwendeten Quellen stammen von OpenAI und beschreiben das eigene Produkt. Sie sind die maßgebliche Quelle für Funktionen, Modellnamen und Verfügbarkeit, aber zugleich Herstellerangaben. Benchmarkresultate können reale Projektbedingungen nur teilweise abbilden. Latenz, Kosten, Antwortqualität und Werkzeugnutzung hängen unter anderem von Aufgabe, Prompt, Kontext, Reasoning-Stufe, Oberfläche und Systemauslastung ab.

Eine belastbare Bewertung kombiniert deshalb drei Ebenen:

1. offizielle Dokumentation für Produktfunktionen und Verfügbarkeit,
2. kontrollierte Tests für den eigenen Anwendungsfall,
3. menschliche Prüfung für Fachlichkeit, Datenschutz und Freigabe.

## Merksatz

> GPT-5.6 erweitert die Möglichkeiten von Codex, hebt aber die Regeln professioneller Softwareentwicklung nicht auf. Je leistungsfähiger das Modell wird, desto wichtiger bleiben ein klarer Auftrag, kontrollierte Berechtigungen, nachvollziehbare Änderungen und überprüfbare Tests.

## Quellen

Abrufdatum aller Quellen: **12. Juli 2026**.

- OpenAI: [GPT-5.6: Frontier intelligence that scales with your ambition](https://openai.com/index/gpt-5-6/), veröffentlicht am 9. Juli 2026.
- OpenAI: [Previewing GPT-5.6 Sol: a next-generation model](https://openai.com/index/previewing-gpt-5-6-sol/), veröffentlicht am 26. Juni 2026.
- OpenAI Help Center: [GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354), Stand laut Seite: 10. Juli 2026.

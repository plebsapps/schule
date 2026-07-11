# Transparenz: Wie dieses Buch entstanden ist

Dieses Praxislehrbuch ist aus einer realen, fortlaufenden Zusammenarbeit zwischen einem menschlichen Projektverantwortlichen und Codex entstanden. Gegenstand der Zusammenarbeit war der Aufbau einer kleinen webbasierten Zeugnisverwaltung. Planung, Quellcode, Tests, Deployment, Fehleranalyse und Buchmanuskript entwickelten sich schrittweise im selben öffentlichen Git-Repository.

Das Kapitel legt offen, welche Aufgaben der Mensch übernahm, wie Codex beteiligt war, wie Inhalte geprüft wurden und welche Grenzen für die Verwendung dieses Buches gelten.

## Menschliche Verantwortung

Der menschliche Autor beziehungsweise Projektverantwortliche bestimmte insbesondere:

- Ziel und fachliche Richtung des Projekts
- Prioritäten und Reihenfolge der Arbeit
- Anforderungen an Datenschutz, Sicherheit und Git-Workflow
- Freigaben für Merge, Deployment und Servereingriffe
- Auswahl der Inhalte für das Praxislehrbuch
- Entscheidung, welche Vorschläge übernommen, verändert oder verworfen werden

Die Verantwortung für Veröffentlichung, fachliche Richtigkeit und späteren Einsatz des Buches bleibt beim Menschen. Ein KI-System kann Vorschläge formulieren, Dateien bearbeiten und Prüfungen ausführen, übernimmt aber keine rechtliche, pädagogische oder betriebliche Verantwortung.

## Beitrag von Codex

Codex wurde als kollaboratives Entwicklungswerkzeug eingesetzt. Zu seinen Aufgaben gehörten unter anderem:

- Analyse von Projektregeln, Plan, Architektur und Tests
- Vorschläge für technische und redaktionelle Vorgehensweisen
- Erstellung und Änderung von Quellcode, Tests und Dokumentation
- Ausführung kontrollierter Git-, Docker-, Django- und Prüfabläufe
- Diagnose von Fehlern und Beschreibung ihrer Ursachen
- redaktionelle Überarbeitung projektbezogener Benutzerprompts
- Strukturierung und Fortschreibung des Buchmanuskripts
- Vorbereitung von Bildplatzhaltern und Generierungsbriefings

Codex arbeitete dabei nicht autonom ohne Grenzen. Repository-Regeln, Sandbox, Freigabeanforderungen, Benutzerentscheidungen und vorhandene Tests bestimmten, welche Handlungen zulässig waren.

## Modell- und Werkzeugstand

Als benannte Grundlage der dokumentierten Zusammenarbeit dient GPT-5.6 Sol mit der Modell-ID `gpt-5.6-sol`. Die konkrete Arbeitsumgebung umfasste zusätzlich Codex-Oberflächen, lokale Werkzeuge, GitHub-Anbindung, Docker und projektspezifische Regeln in `AGENTS.md`.

Modellnamen, Funktionen, Slash-Kommandos, Verfügbarkeit und Benutzeroberflächen können sich ändern. Zeitabhängige Aussagen müssen deshalb vor einer späteren Auflage erneut anhand offizieller Quellen geprüft werden. Dauerhafte Arbeitsprinzipien werden im Buch von versionsabhängigen Bedienhinweisen unterschieden.

## Vom Gespräch zum Manuskript

Die Kapitel sind kein unverändertes Chatprotokoll. Relevante Benutzerprompts wurden für eine lesbare Druckfassung redaktionell bearbeitet:

- Rechtschreibung, Grammatik und Zeichensetzung wurden korrigiert.
- Unübersichtliche Formulierungen wurden klar strukturiert.
- Die fachliche Absicht wurde nicht erweitert oder verkürzt.
- Wesentliche redaktionelle Annahmen werden kenntlich gemacht.
- Secrets, Zugangsdaten und sensible lokale Details werden nicht übernommen.

Die im Buch als redaktionell überarbeitete Prompts gekennzeichneten Texte sind daher nachvollziehbare Arbeitsaufträge, aber keine wörtlichen Transkripte.

## Technische Nachvollziehbarkeit

Das Buch beruht nicht ausschließlich auf erzählter Erinnerung. Wesentliche Schritte sind durch Artefakte im Repository nachvollziehbar:

- versionierte Markdown-Quellen des Buches
- Git-Commits, Feature-Branches und Pull Requests
- Django-Migrationen und automatisierte Tests
- Betriebs- und Sicherheitsdokumentation
- reproduzierbarer EPUB-Build mit einem fest versionierten Pandoc-Container
- Projektchronik als Vollständigkeitskontrolle

Testergebnisse und Betriebsprüfungen beziehen sich auf den jeweils dokumentierten Zwischenstand. Sie beweisen nicht automatisch, dass jede zukünftige Umgebung oder spätere Softwareversion identisch funktioniert.

## Umgang mit Fehlern und Unsicherheit

Fehler und Blocker wurden nicht aus der Darstellung entfernt. Das Buch beschreibt beispielsweise fehlgeschlagene Containerstarts, falsch übernommene Produktionswerte in Testläufen, kurzzeitige Erreichbarkeitsfehler während Neustarts und Probleme bei der GitHub-Authentifizierung.

Diese Ereignisse sind didaktisch wichtig: Gute Arbeit mit Codex besteht nicht darin, dass jeder erste Vorschlag richtig ist. Entscheidend sind überprüfbare Annahmen, kleine Änderungen, verständliche Fehlermeldungen, passende Tests und die Bereitschaft, eine vermeintliche Lösung zu korrigieren.

## Datenschutz und künstliche Daten

Das Projekt betrifft potenziell besonders schützenswerte Schuldaten. Für Repository, Tests, Dokumentation und Buch gelten deshalb strenge Grenzen:

- keine echten Schülerdaten
- keine echten Zeugnisse
- keine Passwörter, Tokens oder Secrets
- keine produktiven Backups
- keine unnötigen lokalen Systemdetails
- keine Übertragung von Schülerdaten an externe KI-Dienste

Alle im Buch genannten Schüler-, Klassen-, Noten- und Kontaktdaten sind künstlich. Beispiele werden sichtbar als `DEMO`, `Beispiel`, `Muster` oder `Test` gekennzeichnet.

## Bilder und KI-generierte Grafiken

Zum aktuellen Manuskript gehört ein Bildkonzept mit fortlaufenden Platzhaltern und detaillierten Generierungsbriefings. Die Grafiken selbst werden in einem getrennten Arbeitsschritt erzeugt. Wenn generative Bildwerkzeuge eingesetzt werden, wird dies in der späteren Bild- und Quellenübersicht offengelegt.

Vor der Veröffentlichung wird jede Grafik auf fachliche Aussage, Schreibfehler, Datenschutz, irreführende UI-Elemente und Druckqualität geprüft. Ein KI-generiertes Bild gilt nicht allein deshalb als korrekt, weil es den Prompt optisch überzeugend umsetzt.

## Grenzen dieses Buches

Dieses Buch ist ein Praxisbericht und eine technische Lernhilfe. Es ersetzt keine individuelle Rechtsberatung, Datenschutz-Folgenabschätzung, IT-Sicherheitsprüfung, pädagogische Fachberatung oder formale Abnahme einer Schulsoftware.

Die demonstrierte Zeugnisverwaltung ist bewusst klein. Eine überzeugende Demo-Oberfläche darf nicht mit einem vollständig geprüften Produktionssystem verwechselt werden. Vor einem realen Schuleinsatz wären zusätzliche fachliche Klärungen, Berechtigungsprüfungen, Aufbewahrungsregeln, Betriebsprozesse und unabhängige Sicherheitsprüfungen erforderlich.

## Redaktionell überarbeiteter Arbeitsauftrag

> Ergänze zunächst ein Transparenzkapitel, das nachvollziehbar erklärt, wie dieses Buch entstanden ist. Lege danach einen Abschnitt über den Autor an; die persönlichen Angaben liefere ich separat. Ergänze außerdem ein Inhaltsverzeichnis.

[Bild022]

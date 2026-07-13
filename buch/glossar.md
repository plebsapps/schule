# Glossar

Dieses Glossar erklärt zentrale Begriffe des Buchs in der Bedeutung, in der sie bei der gemeinsamen Arbeit mit Codex und an der schulischen Zeugnisverwaltung verwendet werden. Die Erläuterungen sind bewusst kurz und setzen kein tieferes Vorwissen voraus.

## A

**`AGENTS.md`**<br>
Eine Datei mit dauerhaften Arbeitsregeln für Codex innerhalb eines Repositorys. Sie kann beispielsweise Sicherheitsgrenzen, Testanforderungen, den Git-Workflow und Dokumentationspflichten festlegen. Regeln in einer näher am bearbeiteten Verzeichnis liegenden `AGENTS.md` können für diesen Teil des Projekts genauer gelten.

**Agent**<br>
Ein KI-gestützter Bearbeiter, der ein Ziel verfolgt, Kontext auswertet und dafür Werkzeuge verwenden kann. Codex ist ein Agent für Softwareentwicklung. Ein Agent ersetzt keine menschliche Freigabe und arbeitet nur innerhalb seiner Berechtigungen.

**App beziehungsweise Konnektor**<br>
Eine autorisierte Verbindung zu einem externen Dienst oder Datenbestand, etwa GitHub. Ein Konnektor stellt gezielte Werkzeuge bereit. Seine Verwendung kann Daten übertragen und muss deshalb zu Aufgabe, Berechtigung und Datenschutz passen.

**Audit-Protokoll**<br>
Eine gegen normale Bearbeitung geschützte Aufzeichnung wichtiger Ereignisse. In der Zeugnisverwaltung gehören dazu beispielsweise Anmeldung, Notenänderung, Freigabe und Rollenänderung. Das Protokoll macht nachvollziehbar, wer wann welche sicherheits- oder fachrelevante Aktion ausgeführt hat.

## B

**Backup**<br>
Eine getrennt aufbewahrte Sicherung, aus der Daten nach Verlust oder Beschädigung wiederhergestellt werden können. Ein persistentes Docker-Volume allein ist noch kein Backup. Erst eine geprüfte Wiederherstellung belegt, dass die Sicherung praktisch nutzbar ist.

**Branch**<br>
Ein benannter Entwicklungszweig in Git. Fachlich zusammenhängende Änderungen entstehen in diesem Projekt auf einem eigenen Feature-Branch und werden erst nach Prüfung in `main` integriert.

## C

**Codex**<br>
Der Softwareentwicklungsagent von OpenAI. Codex kann Quellcode und Dokumentation analysieren, Dateien bearbeiten, Befehle ausführen und Prüfungen unterstützen. Sein tatsächliches Verhalten hängt unter anderem von Modell, Oberfläche, Projektregeln, Kontext, Werkzeugen und Berechtigungen ab.

**Commit**<br>
Ein gespeicherter, benannter Stand von Änderungen in Git. Ein guter Commit ist klein, thematisch geschlossen und enthält keine Secrets oder echten personenbezogenen Daten.

**Container**<br>
Eine isolierte Laufzeitinstanz eines Docker-Images. Die Webanwendung und PostgreSQL laufen in getrennten Containern. Persistente Daten gehören in dafür vorgesehene Volumes und nicht in die kurzlebige Containerdateischicht.

**CSRF-Schutz**<br>
Eine serverseitige Schutzmaßnahme gegen ungewollte, von fremden Webseiten ausgelöste Formularaktionen. Django prüft dafür ein zur Sitzung gehörendes Token. Der Schutz darf für normale Schreibvorgänge nicht umgangen werden.

## D

**Datenmigration**<br>
Siehe **Migration**.

**Diff**<br>
Die Darstellung der Unterschiede zwischen zwei Dateiständen. Vor Commit und Merge zeigt ein Diff, was tatsächlich ergänzt, geändert oder entfernt wurde. Es ist eine zentrale Grundlage für Selbstkontrolle und Review.

**Docker Compose**<br>
Ein Werkzeug, das mehrere zusammengehörige Container, Netzwerke, Volumes und ihre Konfiguration deklarativ beschreibt und gemeinsam startet. In diesem Projekt koordiniert Compose Webanwendung und Datenbank.

## E

**EPUB**<br>
Ein offenes E-Book-Format, das HTML, CSS, Bilder, Metadaten und Inhaltsverzeichnis in einem Archiv bündelt. Die Darstellung passt sich an Lesegerät, Schriftgröße und Zoomstufe an. Deshalb ist eine EPUB-Seite keine unveränderliche Druckseite.

## F

**Feature-Branch**<br>
Ein Branch für eine fachlich zusammenhängende Aufgabe. Der Name beschreibt üblicherweise Art und Inhalt, beispielsweise `docs/buch-glossar`. Ein Feature-Branch hält unfertige Arbeit vom Standard-Branch fern.

**Fixture**<br>
Ein fest definierter Satz von Test- oder Beispieldaten, der reproduzierbar geladen werden kann. Fixtures dürfen in diesem Projekt ausschließlich künstliche Daten enthalten.

## G

**Git**<br>
Ein verteiltes Versionsverwaltungssystem. Git speichert Änderungen als Commits, ermöglicht Branches und unterstützt das nachvollziehbare Zusammenführen geprüfter Arbeit.

**GitHub**<br>
Eine Plattform zum Speichern von Git-Repositorys sowie zur Zusammenarbeit über Issues, Pull Requests, Reviews und Releases. Das öffentliche Repository enthält Quellcode und Dokumentation, aber keine echten Schuldaten oder Secrets.

## H

**Healthcheck**<br>
Eine automatische Prüfung, ob ein Dienst erreichbar und grundsätzlich funktionsfähig ist. Ein erfolgreicher Healthcheck beweist nicht die vollständige fachliche Korrektheit, verhindert aber, dass ein offensichtlich nicht gestarteter Dienst als betriebsbereit gilt.

## I

**Idempotent**<br>
Eine Operation ist idempotent, wenn ihre wiederholte Ausführung denselben gewünschten Endzustand erzeugt, ohne unkontrollierte Duplikate anzulegen. Der Management-Befehl für künstliche Beispieldaten ist dafür ein Projektbeispiel.

**Image**<br>
Im Docker-Kontext eine unveränderliche Vorlage, aus der Container gestartet werden. Das Image enthält Anwendungscode und kontrollierte Abhängigkeiten. Es ist nicht mit einer Buchgrafik zu verwechseln.

## K

**Kontext**<br>
Die Informationen, die dem Modell für eine Aufgabe zur Verfügung stehen. Dazu können Gesprächsverlauf, Benutzerprompt, geöffnete Dateien, Projektregeln, Werkzeugergebnisse und Systemanweisungen gehören. Nicht jede Datei eines Repositorys befindet sich automatisch im Kontext.

**Kontextfenster**<br>
Die begrenzte Menge an Informationen, die ein Modell gleichzeitig berücksichtigen kann. Lange Sitzungen können verdichtet werden. Wichtige dauerhafte Regeln gehören deshalb in Projektdateien und nicht ausschließlich in ältere Chatnachrichten.

## M

**Management-Befehl**<br>
Ein projektspezifischer Django-Kommandozeilenbefehl. Er eignet sich für wiederholbare Verwaltungsaufgaben, beispielsweise das kontrollierte Anlegen künstlicher Beispieldaten oder eines Lesekontos.

**MCP**<br>
Abkürzung für *Model Context Protocol*. MCP ist ein Protokoll, über das ein KI-System strukturierte Werkzeuge und Kontextquellen ansprechen kann. Ein eingebundener MCP-Server erhält nicht automatisch unbegrenzten Zugriff; Berechtigungen und angebotene Werkzeuge bleiben entscheidend.

**Merge**<br>
Das Zusammenführen der Änderungen eines Branches in einen anderen Branch. Im professionellen Workflow erfolgt der Merge erst nach Prüfung von Diff, Tests, Freigaben und möglichen Konflikten.

**Migration**<br>
Eine versionierte, reproduzierbare Änderung des Datenbankschemas. Django-Migrationen erstellen oder verändern beispielsweise Tabellen und Spalten. Produktionsdatenbanken werden nicht manuell an der versionierten Migrationshistorie vorbei geändert.

**Modell**<br>
Das KI-Modell, das eine Aufgabe verarbeitet. Im Buch ist GPT-5.6 Sol die benannte Grundlage. Modellwahl und Reasoning-Aufwand beeinflussen Leistungsprofil, Geschwindigkeit und Kosten, ersetzen aber keine Projektregeln oder Tests.

## O

**Optimistisches Locking**<br>
Ein Verfahren gegen unbemerktes Überschreiben paralleler Änderungen. Beim Speichern wird geprüft, ob die geladene Versionsnummer noch aktuell ist. Hat eine andere Person inzwischen gespeichert, erscheint ein Konflikt statt eines stillen Datenverlusts.

## P

**Pandoc**<br>
Ein Werkzeug zur Umwandlung zwischen Dokumentformaten. Das Buch wird mit einer festgelegten Pandoc-Containerfassung aus Markdown, CSS, Bildern und Metadaten als EPUB3 erzeugt.

**Plugin**<br>
Ein installierbares Erweiterungspaket für Codex. Ein Plugin kann Skills, Kommandos, Werkzeuge, MCP-Konfigurationen oder Apps bündeln. Es ist umfangreicher als ein einzelner Skill.

**PostgreSQL**<br>
Das relationale Datenbanksystem der Zeugnisverwaltung. Es speichert Anwendungsdaten transaktional und liegt in einem persistenten Docker-Volume. Sicherungen werden mit dafür vorgesehenen Datenbankwerkzeugen erzeugt.

**`PLAN.md`**<br>
Die Datei, die Ziel, Umfang, Architektur und wichtige Projektentscheidungen beschreibt. Sie beantwortet, was gebaut werden soll. `AGENTS.md` beschreibt dagegen, nach welchen Regeln Codex daran arbeitet.

**Prompt**<br>
Ein in natürlicher Sprache formulierter Arbeitsauftrag an ein KI-System. Ein guter Prompt nennt Ziel, relevanten Kontext, Grenzen und gewünschtes Ergebnis. Im Buch werden solche Anfragen als „Prompt“ oder „Arbeitsauftrag“ gekennzeichnet.

**Pull Request**<br>
Ein nachvollziehbarer Vorschlag, Änderungen aus einem Branch in den Standard-Branch zu übernehmen. Ein Pull Request bündelt Diff, Beschreibung, Prüfstatus, Diskussion und Review. Er wird erst gemergt, wenn die notwendigen Prüfungen und Freigaben vorliegen.

## R

**Reasoning-Aufwand**<br>
Eine Einstellung dafür, wie viel Rechen- und Bearbeitungsaufwand ein Modell für eine Aufgabe einsetzen darf. Mehr Reasoning kann bei schwierigen Aufgaben helfen, ist aber für kleine Änderungen nicht automatisch wirtschaftlich oder besser.

**Repository**<br>
Ein von Git verwaltetes Projektverzeichnis einschließlich Versionshistorie. Das Repository enthält Code, Tests und Dokumentation, jedoch keine produktiven Secrets oder echten Schülerdaten.

**Restore**<br>
Die Wiederherstellung von Daten aus einem Backup. Ein Restore-Test findet in einer isolierten Umgebung statt und prüft, ob Sicherung, Struktur und Wiederherstellungsweg tatsächlich funktionieren.

**Reverse Proxy**<br>
Ein vorgeschalteter Server, der Anfragen entgegennimmt und an die interne Webanwendung weiterleitet. In diesem Projekt übernimmt Nginx unter anderem HTTPS und leitet an den nur lokal erreichbaren Django-Port weiter.

## S

**Sandbox**<br>
Eine kontrollierte Ausführungsumgebung, die Datei-, Netzwerk- oder Systemzugriffe begrenzt. Sie reduziert die Folgen unbeabsichtigter oder riskanter Aktionen. Eine Freigabe erweitert nur den ausdrücklich erlaubten Zugriff und hebt Projektregeln nicht auf.

**Secret**<br>
Ein vertraulicher Wert wie ein produktives Passwort, API-Schlüssel oder Token. Secrets werden über geschützte Umgebungsvariablen oder vergleichbare Mechanismen bereitgestellt und niemals im Repository, Buch oder Testdatenbestand veröffentlicht. Ein ausdrücklich öffentlich freigegebenes Demo-Kennwort für ausschließlich künstliche Daten ist kein Secret, darf aber niemals für andere Konten oder produktive Systeme wiederverwendet werden.

**Skill**<br>
Eine wiederverwendbare Arbeitsanleitung für Codex. Ein Skill beschreibt einen spezialisierten Ablauf und kann Referenzen oder Hilfsskripte enthalten. Er wird verwendet, wenn eine Aufgabe zu seinem festgelegten Geltungsbereich passt.

**Subagent**<br>
Ein zusätzlicher Agent, der eine klar abgegrenzte Teilaufgabe parallel oder unabhängig bearbeitet. Subagenten sind besonders nützlich für voneinander trennbare Analysen. Unkoordinierte gleichzeitige Änderungen derselben Dateien werden vermieden.

## T

**Token**<br>
Eine Verarbeitungseinheit für Texteingaben und Modellausgaben. Tokenmenge beeinflusst Kontextverbrauch und bei API-Nutzung häufig die Kosten. Ein Token entspricht nicht zuverlässig einem vollständigen Wort.

**Transaktion**<br>
Eine Gruppe von Datenbankänderungen, die vollständig oder gar nicht ausgeführt wird. Transaktionen verhindern inkonsistente Zwischenstände, wenn ein zusammengehöriger Vorgang fehlschlägt.

## V

**Versionierung**<br>
Das nachvollziehbare Bewahren unterschiedlicher Stände. Git versioniert Quellcode; Migrationen versionieren das Datenbankschema; freigegebene Zeugnisse benötigen eine eigene unveränderliche fachliche Versionierung.

**Volume**<br>
Ein von Docker verwalteter persistenter Speicherbereich. Ein Volume überlebt den Austausch eines Containers, schützt aber nicht automatisch vor versehentlichem Löschen oder Beschädigung und ersetzt daher kein Backup.

## Z

**Zero Data Retention (ZDR)**<br>
Eine vertraglich und technisch definierte API-Datenverarbeitungsoption, bei der unterstützte Inhalte nicht über die für die Verarbeitung nötige Dauer gespeichert werden sollen. ZDR ersetzt keine Datenschutzprüfung und erlaubt nicht automatisch die Übertragung schulischer personenbezogener Daten.

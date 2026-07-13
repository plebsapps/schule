# AGENTS.md

# Verbindliche Arbeitsregeln für Codex

## 1. Grundauftrag

Dieses Repository enthält eine schulische Zeugnisverwaltung.

Die Anwendung verarbeitet sensible personenbezogene Daten von Schülerinnen und Schülern.

Qualität, Datenschutz, Nachvollziehbarkeit, Berechtigungsschutz und Datenintegrität haben Vorrang vor Entwicklungsgeschwindigkeit.

Codex muss vor Änderungen immer zuerst:

1. `PLAN.md` lesen
2. bestehende Architektur und Dateien analysieren
3. vorhandene Tests prüfen
4. Auswirkungen der geplanten Änderung benennen
5. nur danach Änderungen durchführen

## 2. Arbeitsweise

Bei jeder grösseren Aufgabe gilt:

1. Anforderungen analysieren
2. betroffene Komponenten identifizieren
3. Risiken benennen
4. Umsetzungsplan erstellen
5. kleine, nachvollziehbare Änderungen durchführen
6. passende Tests ergänzen
7. Tests ausführen
8. Dokumentation aktualisieren
9. Ergebnis zusammenfassen

Keine grossen unkontrollierten Änderungen durchführen.

Keine Dateien vollständig ersetzen, wenn eine gezielte Änderung ausreicht.

Keine bestehende Funktion entfernen, ohne die Auswirkungen zu prüfen und ausdrücklich zu dokumentieren.

## 3. Geltungsbereich

Codex darf standardmässig nur innerhalb des aktuellen Repository-Verzeichnisses arbeiten.

Nicht ohne ausdrückliche Freigabe ändern:

- `/etc/nginx`
- `/etc/ssl`
- `/etc/systemd`
- bestehende Docker-Container
- bestehende Docker-Netzwerke
- fremde Projektverzeichnisse
- globale Python-Installation
- globale Node.js-Installation
- Firewall-Regeln
- Benutzerkonten des Servers
- SSH-Konfiguration
- bestehende Datenbanken

Externe Serveränderungen müssen als manuelle Schritte dokumentiert werden.

## 4. Technologie

Bevorzugter Stack:

- Python
- Django
- PostgreSQL
- Docker Compose
- Nginx
- pytest
- HTML und CSS
- möglichst wenig JavaScript
- serverseitige Formulare
- HTML-zu-PDF-Erzeugung

Zusätzliche Bibliotheken nur verwenden, wenn sie fachlich oder technisch notwendig sind.

Für jede neue Abhängigkeit dokumentieren:

- Zweck
- Lizenz
- Sicherheitsrelevanz
- Wartungsstatus
- Alternative ohne diese Abhängigkeit

## 5. Architekturprinzipien

Die Anwendung muss modular aufgebaut werden.

Fachliche Bereiche in getrennten Django-Apps organisieren.

Beispiel:

- accounts
- schools
- students
- classes
- subjects
- grades
- reports
- imports
- audit

Geschäftslogik nicht unnötig in Views, Templates oder Signalen verstecken.

Komplexe Geschäftslogik in klar benannten Services oder Domänenfunktionen kapseln.

Modelle sollen fachliche Invarianten schützen.

Berechtigungsprüfungen müssen serverseitig erfolgen.

Clientseitige Einschränkungen sind niemals ausreichender Zugriffsschutz.

## 6. Datenmodell und Migrationen

Datenbankänderungen nur über versionierte Migrationen.

Keine manuelle Änderung der Produktionsdatenbank.

Migrationen müssen:

- reproduzierbar sein
- möglichst rückwärtsverträglich sein
- bestehende Daten berücksichtigen
- bei kritischen Änderungen einen Migrationsplan enthalten
- getestet werden

Keine Tabellen oder Spalten löschen, ohne:

- Datennutzung zu prüfen
- Backup- und Migrationsweg zu dokumentieren
- ausdrückliche Freigabe

Historische Zeugnisdaten dürfen nicht durch spätere Änderungen verfälscht werden.

## 7. Datenschutz

Es dürfen keine echten Schülerdaten in:

- Tests
- Fixtures
- Screenshots
- Dokumentation
- Beispielkonfigurationen
- Git-Commits
- Logausgaben

verwendet werden.

Testdaten müssen vollständig künstlich und anonym sein.

Keine Daten an externe Dienste übertragen.

Keine externen KI-APIs für Schülerdaten verwenden.

Keine Analyse-, Tracking- oder Werbedienste integrieren.

Logs dürfen keine vollständigen Zeugnisse, Passwörter oder unnötige personenbezogene Daten enthalten.

## 8. Sicherheit

Mindestens beachten:

- sichere Passwort-Hashes
- CSRF-Schutz
- sichere Session-Cookies
- HTTPS im Produktivbetrieb
- sichere Header
- Schutz vor SQL-Injection
- Schutz vor XSS
- Schutz vor unsicheren Datei-Uploads
- Rate-Limiting oder Login-Sperre
- minimale Datenbankrechte
- Secrets nur über Umgebungsvariablen oder Secrets
- keine Secrets im Repository
- keine Standardpasswörter
- keine Debug-Ausgaben in Produktion

Eng begrenzte Ausnahme für den öffentlichen Show-case: Ein ausdrücklich durch
den Benutzer freigegebenes Demo-Kennwort darf dokumentiert werden, wenn das
Konto ausschließlich künstliche Daten lesen kann, keine Schreibrechte besitzt,
sein Passwort nicht selbst ändern kann und das Kennwort in keinem anderen
System verwendet wird. Diese Ausnahme gilt niemals für produktive Konten,
Administratoren, echte Schuldaten oder andere Secrets.

`DEBUG` muss im Produktivbetrieb deaktiviert sein.

`ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` und Cookie-Einstellungen müssen korrekt konfigurierbar sein.

## 9. Berechtigungen

Jede schreibende und lesende Funktion benötigt eine serverseitige Berechtigungsprüfung.

Insbesondere prüfen:

- Benutzerrolle
- Schule
- Schuljahr
- Klasse
- Fach
- Zeugnisperiode
- Status des Datensatzes
- Freigabestatus

Fachlehrpersonen dürfen nur zugewiesene Fächer und Klassen bearbeiten.

Klassenlehrpersonen dürfen nur ihre Klassen bearbeiten.

Freigegebene Zeugnisse dürfen nicht normal bearbeitet werden.

Administratoren dürfen Berechtigungen verwalten, aber fachliche Sperren nicht unbemerkt umgehen.

## 10. Noten und Datenintegrität

Notenwerte müssen serverseitig validiert werden.

Validierung umfasst:

- zulässige Skala
- zulässige Schrittweite
- Sonderwerte
- Zeugnisperiode
- Berechtigung
- Sperrstatus
- Vollständigkeit

Unbemerkbares Überschreiben verhindern.

Für konfliktanfällige Datensätze optimistisches Locking oder eine gleichwertige Strategie verwenden.

Konflikte müssen dem Benutzer verständlich angezeigt werden.

## 11. Zeugnisse und Versionierung

Freigegebene Zeugnisse sind unveränderlich.

Korrekturen erzeugen eine neue Version.

Alte Versionen bleiben erhalten.

Für jede Version speichern:

- Datenstand
- Versionsnummer
- Erstellungszeitpunkt
- erstellende Person
- Freigabezeitpunkt
- freigebende Person
- Grund einer Korrektur
- erzeugte PDF-Datei
- Prüfsumme

PDFs müssen reproduzierbar sein.

## 12. Audit-Protokoll

Sicherheitsrelevante und fachlich relevante Änderungen protokollieren.

Mindestens:

- Anmeldung
- fehlgeschlagene Anmeldung
- Notenänderung
- Änderung von Fehlzeiten
- Änderung von Bemerkungen
- Freigabe
- Aufhebung einer Sperre
- Korrektur
- Import
- Benutzer- und Rollenänderung

Audit-Daten dürfen durch normale Benutzer nicht verändert werden.

## 13. Imports

Dateiimporte gelten als nicht vertrauenswürdig.

Jeder Import benötigt:

- Dateitypprüfung
- Grössenbegrenzung
- Validierung
- Vorschau
- Fehlerbericht
- ausdrückliche Bestätigung
- Transaktion
- Importprotokoll

Bei kritischen Fehlern keine Teilimporte durchführen.

Dateinamen nicht als sichere Pfade übernehmen.

## 14. PDF-Erzeugung

PDF-Layouts müssen stabil und druckbar sein.

Vorlagen versionieren.

Keine direkte freie HTML-Eingabe durch normale Benutzer zulassen.

Vorlagen müssen mit künstlichen Testdaten getestet werden.

Zu testen sind:

- lange Namen
- viele Fächer
- fehlende Werte
- Sonderzeichen
- Seitenumbrüche
- unterschiedliche Klassenstufen
- unterschiedliche Vorlagen

## 15. Fehlerbehandlung

Fehler niemals stillschweigend ignorieren.

Benutzer erhalten verständliche Meldungen.

Technische Details gehören in Logs, nicht in die Benutzeroberfläche.

Keine Stacktraces in Produktion anzeigen.

Datenbankoperationen mit zusammengehörigen Änderungen müssen transaktional erfolgen.

## 16. Tests

Jede fachliche Änderung benötigt passende Tests.

Mindestens verwenden:

- Unit-Tests
- Modelltests
- Service-Tests
- Berechtigungstests
- Integrationstests
- PDF-Tests, soweit technisch sinnvoll

Besonders kritisch testen:

- Rollen und Zugriffe
- Notenvalidierung
- Konflikterkennung
- Freigabe
- Sperrung
- Korrekturen
- Versionierung
- Import
- Audit-Protokoll
- Mandantentrennung, falls später mehrere Schulen unterstützt werden

Keine Änderung als abgeschlossen melden, wenn relevante Tests fehlschlagen.

## 17. Codequalität

Code muss:

- verständlich
- typisiert, soweit sinnvoll
- klein und modular
- testbar
- dokumentiert
- konsistent formatiert

sein.

Keine unnötigen Abstraktionen.

Keine übergrossen Dateien oder Funktionen.

Keine duplizierte Geschäftslogik.

Klare Namen verwenden.

Fachbegriffe im Code konsistent halten.

## 18. Konfiguration

Konfiguration über Umgebungsvariablen.

Eine `.env.example` bereitstellen.

Die `.env.example` darf keine echten Geheimnisse enthalten.

Mindestens konfigurierbar:

- Datenbankverbindung
- Django Secret Key
- Debug-Modus
- erlaubte Hosts
- CSRF-Ursprünge
- Session-Einstellungen
- E-Mail-Einstellungen, falls später benötigt
- Speicherorte
- Backup-Verzeichnis
- PDF-Konfiguration

## 19. Docker

Container sollen:

- nicht als Root laufen, soweit praktikabel
- Healthchecks besitzen
- reproduzierbar gebaut werden
- feste oder kontrollierte Abhängigkeitsversionen verwenden
- keine unnötigen Pakete enthalten
- persistente Daten nur in Volumes speichern

Keine bestehenden Docker-Ressourcen überschreiben.

Projektbezogene Container, Netzwerke und Volumes eindeutig benennen.

## 20. Git

Vor Änderungen zuerst den aktuellen Status prüfen.

Keine fremden uncommitted Änderungen überschreiben.

Keine Secrets committen.

Keine generierten Backups committen.

Keine echten PDF-Zeugnisse committen.

Commits sollen klein und thematisch klar sein.

Empfohlene Commit-Präfixe:

```text
feat:
fix:
refactor:
test:
docs:
chore:
security:
```

## 21. Dokumentation

Bei jeder relevanten Änderung prüfen, ob folgende Dateien angepasst werden müssen:

- `README.md`
- `PLAN.md`
- `AGENTS.md`
- `.env.example`
- Betriebsdokumentation
- Backup-Dokumentation
- Migrationshinweise

README muss mindestens enthalten:

- Voraussetzungen
- lokale Installation
- Konfiguration
- Start
- Tests
- Migrationen
- Deployment
- Backup
- Wiederherstellung
- bekannte Einschränkungen

## 22. Verbotene Abkürzungen

Nicht zulässig:

- Berechtigungen nur im Frontend prüfen
- Passwörter im Klartext speichern
- Secrets fest im Code hinterlegen
- echte Schülerdaten als Testdaten verwenden
- Produktionsdatenbank manuell verändern
- freigegebene Zeugnisse überschreiben
- Fehler durch pauschale Ausnahmebehandlung verstecken
- Tests deaktivieren, nur damit Builds erfolgreich sind
- bestehende Sicherheitsprüfungen entfernen
- SSL-Prüfungen abschalten
- unkontrollierte Shell-Befehle aus Benutzereingaben bilden
- Dateien ausserhalb des Projekts ohne Freigabe ändern
- automatisches Deployment in Produktion ohne ausdrückliche Freigabe

## 23. Vorgehen bei Unklarheiten

Bei fachlichen Unklarheiten:

1. Annahmen klar benennen
2. keine irreversible Entscheidung treffen
3. Datenmodell erweiterbar halten
4. offene Punkte in `docs/open-questions.md` dokumentieren
5. mit künstlichen Beispielen arbeiten

Bei technischen Unklarheiten:

1. bestehende Umgebung analysieren
2. risikoärmste Lösung wählen
3. Alternativen dokumentieren
4. keine bestehende Infrastruktur gefährden

## 24. Definition of Done

Eine Aufgabe ist erst abgeschlossen, wenn:

- Anforderungen umgesetzt sind
- Berechtigungen geprüft sind
- Tests vorhanden sind
- Tests erfolgreich laufen
- Migrationen vorhanden und geprüft sind
- keine Secrets enthalten sind
- Dokumentation aktualisiert ist
- Sicherheitsauswirkungen bewertet sind
- bestehende Funktionen nicht unbeabsichtigt beeinträchtigt wurden
- offene Punkte benannt sind
- manuelle Deployment-Schritte dokumentiert sind

## 25. Abschlussbericht durch Codex

Nach jeder grösseren Aufgabe soll Codex berichten:

1. was geändert wurde
2. welche Dateien betroffen sind
3. welche Architekturentscheidung getroffen wurde
4. welche Tests ausgeführt wurden
5. ob alle Tests erfolgreich waren
6. welche Migrationen entstanden sind
7. welche manuellen Schritte notwendig sind
8. welche Risiken oder offenen Punkte verbleiben

## 26. Praxisbeispiel Arbeiten mit Codex

Dieses Projekt dient zusätzlich als Praxisbeispiel zum Arbeiten mit Codex.

Alle übertragbaren Erkenntnisse aus der Zusammenarbeit mit Codex müssen im Verzeichnis `buch/` dokumentiert werden.

Dazu gehören insbesondere:

- Ausgangslage und Ziel der Aufgabe
- verwendete Codex-Arbeitsweise
- wichtige Entscheidungen
- konkrete Befehle und Git-Schritte
- Fehler, Blocker und deren Lösung
- Sicherheits- und Datenschutzüberlegungen
- Erkenntnisse für zukünftige Codex-Nutzung

Die Buchdokumentation darf keine echten Schülerdaten, keine Secrets, keine Zugangstokens und keine sensiblen lokalen Systemdetails enthalten.

Das ausdrücklich freigegebene Kennwort des öffentlichen Read-only-Demokontos
gilt nicht als Secret. Es darf nur dokumentiert werden, solange das Konto
ausschließlich künstliche Daten lesen kann und alle Bedingungen aus Abschnitt 8
erfüllt bleiben.

Wenn eine Aufgabe für das Praxisbeispiel relevant ist, muss Codex prüfen, ob eine Datei in `buch/` ergänzt oder neu angelegt werden muss.

## 27. Prompts als Bestandteil des Praxisbeispiels

Die für das Projekt relevanten Benutzer-Prompts müssen als nachvollziehbare Arbeitsaufträge im Verzeichnis `buch/` dokumentiert werden.

Für die Druckfassung werden die Prompts redaktionell überarbeitet:

- Rechtschreibung, Grammatik und Zeichensetzung korrigieren
- Formulierungen verständlich und eindeutig strukturieren
- fachliche Absicht und Umfang des ursprünglichen Prompts unverändert erhalten
- keine Anforderungen ergänzen oder entfernen
- bei wesentlichen Unklarheiten die redaktionelle Annahme kenntlich machen
- Prompts typografisch einheitlich und druckbar darstellen

Die Buchfassung ist eine sprachlich verbesserte Fassung und darf nicht fälschlich als wörtliches Transkript bezeichnet werden.

Prompts dürfen nicht in das Buch übernommen werden, wenn sie echte Schülerdaten, Secrets, Zugangstokens oder sensible lokale Systemdetails enthalten. Solche Inhalte müssen vor der Dokumentation entfernt oder durch eindeutig künstliche Platzhalter ersetzt werden.

## 28. Professioneller Git-Workflow

Änderungen dürfen grundsätzlich nicht direkt auf dem Standard-Branch `main` oder `master` entwickelt werden.

Für jede fachlich zusammenhängende Aufgabe ist vor der ersten Änderung ein eigener Branch vom aktuellen Standard-Branch zu erstellen.

Empfohlene Branch-Präfixe:

```text
feat/
fix/
docs/
test/
refactor/
chore/
security/
```

Der Ablauf ist:

1. aktuellen Git-Status prüfen
2. Standard-Branch aktualisieren, sofern dies ohne Überschreiben fremder Änderungen möglich ist
3. aussagekräftigen Feature-Branch erstellen
4. kleine, thematisch klare Commits erstellen
5. Branch zu GitHub pushen
6. Pull Request gegen den Standard-Branch erstellen
7. Tests und Prüfungen erfolgreich abschliessen
8. Änderungen prüfen und nachvollziehbar mergen
9. Feature-Branch nach erfolgreichem Merge löschen, sofern er nicht mehr benötigt wird

Direkte Commits und direkte Pushes auf `main` oder `master` sind nur mit ausdrücklicher Freigabe zulässig. Codex darf einen Pull Request nicht automatisch mergen, wenn Prüfungen fehlschlagen, Freigaben fehlen oder Konflikte bestehen.

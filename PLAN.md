# PLAN.md

# Zeugnisverwaltung für Schulen

## 1. Ziel des Projekts

Ziel ist die Ablösung einer bestehenden Excel- und Seriendrucklösung durch eine zentrale Webanwendung.

Lehrpersonen sollen sich anmelden, ihre zugewiesenen Klassen und Fächer sehen und die Noten der Schülerinnen und Schüler erfassen können. Nach Abschluss der Noteneingabe sollen Zeugnisse als PDF für einzelne Schülerinnen und Schüler, klassenweise oder für alle Klassen erzeugt und ausgedruckt werden können.

Die Anwendung soll den gleichzeitigen Zugriff mehrerer Benutzer ermöglichen, Eingabekonflikte verhindern, Änderungen nachvollziehbar protokollieren und sensible Schülerdaten innerhalb einer kontrollierten Serverumgebung verarbeiten.

## 2. Ausgangssituation

Die Schule arbeitet derzeit mit einer Excel-Datei.

Typische Probleme der bestehenden Lösung:

- gleichzeitige Bearbeitung ist nur eingeschränkt möglich
- Dateien können gesperrt sein
- Versionen können auseinanderlaufen
- versehentliche Änderungen sind schwer nachvollziehbar
- Berechtigungen lassen sich nur unzureichend abbilden
- Seriendruck und Vorlagenpflege sind fehleranfällig
- historische Zeugnisse und Korrekturen sind schwer sauber zu verwalten
- Backups und Wiederherstellung sind nicht zentral geregelt
- sensible Schülerdaten liegen in leicht kopierbaren Dateien

## 3. Zielarchitektur

Die Anwendung soll auf einem Ubuntu-Server in Docker betrieben werden.

Vorgesehene Komponenten:

- Python-Webanwendung
- Django als bevorzugtes Webframework
- PostgreSQL als Datenbank
- Docker Compose für Betrieb und Deployment
- Nginx als vorhandener Reverse Proxy
- HTTPS
- serverseitig erzeugte PDF-Zeugnisse
- Git für Versionsverwaltung
- automatische Tests mit pytest
- Datenbankmigrationen
- Backup- und Wiederherstellungsskripte

Vereinfachte Architektur:

```text
Browser
   |
HTTPS
   |
Nginx
   |
Django-Anwendung
   |
PostgreSQL
   |
PDF-Generator
```

## 4. Projektumfang der ersten Version

Die erste Version soll bewusst klein bleiben.

Zum MVP gehören:

1. Anmeldung und Benutzerverwaltung
2. Rollen und Berechtigungen
3. Verwaltung von Schuljahren und Zeugnisperioden
4. Verwaltung von Klassen
5. Verwaltung von Schülerinnen und Schülern
6. Verwaltung von Fächern
7. Zuordnung von Lehrpersonen zu Klassen und Fächern
8. Noteneingabe
9. Anzeige fehlender oder unvollständiger Eingaben
10. Zeugnisbemerkungen und Fehlzeiten
11. Freigabeprozess
12. Sperrung freigegebener Zeugnisse
13. PDF-Ausgabe
14. Änderungshistorie
15. Excel- oder CSV-Import
16. Backup und Wiederherstellung
17. technische Dokumentation

Nicht Bestandteil der ersten Version:

- Elternportal
- Schülerportal
- mobile App
- Stundenplan
- vollständig frei gestaltbarer Vorlageneditor
- Schnittstellen zu externen Schulverwaltungssystemen
- automatische komplexe Notenberechnungen
- digitale Signaturen
- Versand der Zeugnisse per E-Mail

## 5. Benutzerrollen

Mindestens folgende Rollen sind vorzusehen.

### Administrator

Darf:

- Benutzer verwalten
- Rollen zuweisen
- Schuljahre und Zeugnisperioden verwalten
- Klassen, Fächer und Schüler verwalten
- Vorlagen verwalten
- Daten importieren
- Systemeinstellungen ändern
- Backups ausführen
- Audit-Protokolle einsehen

### Schulleitung

Darf:

- alle Klassen und Zeugnisse einsehen
- Zeugnisse prüfen
- Zeugnisse freigeben
- freigegebene Zeugnisse für Korrekturen öffnen
- Berichte und Vollständigkeitsübersichten einsehen

### Klassenlehrperson

Darf:

- die eigene Klasse einsehen
- Zeugnisbemerkungen bearbeiten
- Fehlzeiten bearbeiten
- Vollständigkeit prüfen
- Zeugnisse zur Freigabe einreichen
- freigegebene Zeugnisse ausgeben

### Fachlehrperson

Darf:

- nur zugewiesene Klassen und Fächer einsehen
- Noten erfassen und ändern
- eigene Eingaben als abgeschlossen markieren
- fehlende Eingaben für die eigenen Fächer sehen

## 6. Fachliches Datenmodell

Mindestens folgende fachliche Objekte werden benötigt.

### Benutzer

Felder:

- Benutzername
- Vorname
- Nachname
- E-Mail
- aktiv oder gesperrt
- Rolle
- letzter Login
- Passwortänderung erforderlich

### Schule

Felder:

- Name
- Anschrift
- Logo
- Kontaktdaten
- Schulleitung
- Einstellungen

Die erste Version kann zunächst nur eine Schule unterstützen. Das Datenmodell sollte Mehrschulfähigkeit jedoch nicht unnötig verhindern.

### Schuljahr

Beispiel:

```text
2026/2027
```

Felder:

- Bezeichnung
- Startdatum
- Enddatum
- Status
- aktiv

### Zeugnisperiode

Beispiele:

- erstes Halbjahr
- zweites Halbjahr
- Jahreszeugnis
- Zwischenzeugnis
- Abschlusszeugnis

Status:

- Vorbereitung
- Eingabe geöffnet
- Prüfung
- freigegeben
- abgeschlossen
- archiviert

### Klasse

Felder:

- Bezeichnung
- Klassenstufe
- Schuljahr
- Klassenlehrperson
- Zeugnisvorlage
- aktiv

### Schüler

Felder:

- interne Schülernummer
- Vorname
- Nachname
- Geburtsdatum
- Geschlecht, sofern fachlich erforderlich
- Eintrittsdatum
- Austrittsdatum
- aktiv
- weitere zeugnisrelevante Stammdaten

### Klassenzuordnung

Die Klassenzuordnung darf nicht direkt dauerhaft am Schüler gespeichert werden.

Eine eigene Zuordnung wird benötigt:

- Schüler
- Klasse
- Schuljahr
- Eintrittsdatum
- Austrittsdatum

Dadurch bleiben Klassenwechsel und historische Zuordnungen nachvollziehbar.

### Fach

Felder:

- Bezeichnung
- Kurzbezeichnung
- Reihenfolge auf dem Zeugnis
- Pflichtfach oder Wahlfach
- sichtbar auf Zeugnis
- Notenskala
- zulässige Schrittweite

### Unterrichtszuordnung

Verknüpft:

- Lehrperson
- Klasse
- Fach
- Schuljahr
- Zeugnisperiode

### Note

Felder:

- Schüler
- Fach
- Klasse
- Zeugnisperiode
- Wert
- Sonderwert
- Bemerkung
- Bearbeitungsstatus
- Version
- geändert von
- geändert am

Sonderwerte können sein:

- nicht bewertet
- befreit
- teilgenommen
- nicht teilgenommen

### Fehlzeiten

Felder:

- entschuldigte Fehltage
- unentschuldigte Fehltage
- entschuldigte Fehlstunden
- unentschuldigte Fehlstunden
- Verspätungen

Die tatsächlich benötigten Felder müssen mit der Schule abgestimmt werden.

### Zeugnisbemerkung

Felder:

- Schüler
- Zeugnisperiode
- Bemerkung
- Verhalten
- Mitarbeit
- Versetzungsentscheidung
- weitere konfigurierbare Angaben

### Zeugnis

Felder:

- Schüler
- Zeugnisperiode
- Vorlage
- Status
- Versionsnummer
- freigegeben von
- freigegeben am
- erzeugte PDF-Datei
- Prüfsumme der PDF-Datei

### Zeugnisversion

Jede freigegebene Version bleibt erhalten.

Felder:

- Zeugnis
- Versionsnummer
- Datenstand
- PDF-Datei
- erstellt von
- erstellt am
- Grund einer Korrektur

### Audit-Protokoll

Mindestens zu protokollieren:

- Benutzer
- Zeitpunkt
- Aktion
- betroffenes Objekt
- alte Werte
- neue Werte
- IP-Adresse, soweit datenschutzrechtlich zulässig

## 7. Noteneingabe

Die Noteneingabe soll möglichst tabellarisch und effizient sein.

Anforderungen:

- Eingabe für eine vollständige Klasse
- Eingabe pro Fach
- Eingabe pro Schüler
- Tastaturnavigation
- Zwischenspeicherung
- sofortige Validierung
- Kennzeichnung ungültiger Werte
- Kennzeichnung fehlender Noten
- Anzeige des Bearbeitungsstatus
- Abschluss der Eingabe pro Fach
- erneutes Öffnen nur mit Berechtigung

Zulässige Notenwerte müssen konfigurierbar sein.

Beispiele:

- 1 bis 6
- Schrittweite 0,5
- Schrittweite 0,25
- ganze Noten
- Textbewertungen

## 8. Schutz vor Bearbeitungskonflikten

Gleichzeitige Bearbeitung muss möglich sein.

Unbemerkbares Überschreiben ist zu verhindern.

Vorgesehen ist optimistisches Locking.

Jeder relevante Datensatz erhält:

- Versionsnummer oder Änderungszeitpunkt
- letzte bearbeitende Person
- letzten Änderungszeitpunkt

Wurde ein Datensatz zwischenzeitlich geändert, darf die Anwendung den älteren Stand nicht einfach speichern.

Stattdessen erscheint ein Konflikthinweis mit:

- aktuellem Wert
- eigenem eingegebenem Wert
- Benutzer der letzten Änderung
- Zeitpunkt der letzten Änderung

## 9. Zeugnisvorlagen

Unterschiedliche Klassen können unterschiedliche Zeugnisvorlagen benötigen.

Eine Vorlage wird mindestens zugeordnet nach:

- Schuljahr
- Zeugnisart
- Klassenstufe
- Klasse
- Schule

Für die erste Version sollen Vorlagen nicht vollständig im Browser gestaltet werden.

Empfohlen wird:

- HTML- und CSS-basierte Vorlagen
- versionierte Vorlagendateien im Repository
- feste definierte Platzhalter
- PDF-Erzeugung aus HTML und CSS

Mögliche Platzhalter:

```text
{{ student.first_name }}
{{ student.last_name }}
{{ student.birth_date }}
{{ class.name }}
{{ school_year.name }}
{{ report_period.name }}
{{ grades }}
{{ absences }}
{{ remarks }}
{{ issue_date }}
```

Die konkrete Template-Syntax richtet sich nach der gewählten technischen Umsetzung.

## 10. PDF-Erzeugung

Die Zeugnisse müssen reproduzierbar und druckstabil sein.

Funktionen:

- Vorschau eines Zeugnisses
- PDF für einen Schüler
- gemeinsames PDF für eine Klasse
- gemeinsames PDF für alle freigegebenen Zeugnisse
- ZIP-Datei mit einzelnen PDFs
- erneute Ausgabe einer bestehenden freigegebenen Version

Die PDF-Dateien sollen nach einem einheitlichen Schema benannt werden.

Beispiel:

```text
2026-2027_1-Halbjahr_Klasse-7A_Mustermann_Max_v1.pdf
```

Die endgültige PDF wird erst nach Freigabe als unveränderliche Zeugnisversion gespeichert.

## 11. Freigabeprozess

Vorgesehener Ablauf:

1. Administrator öffnet die Zeugnisperiode.
2. Fachlehrpersonen tragen Noten ein.
3. Fachlehrpersonen markieren ihre Eingabe als abgeschlossen.
4. Die Anwendung prüft die Vollständigkeit.
5. Die Klassenlehrperson ergänzt Bemerkungen und Fehlzeiten.
6. Die Klassenlehrperson reicht die Zeugnisse zur Prüfung ein.
7. Die Schulleitung oder eine berechtigte Person prüft die Zeugnisse.
8. Die Zeugnisse werden freigegeben.
9. Die endgültigen PDFs werden erzeugt.
10. Freigegebene Daten werden gesperrt.

## 12. Korrekturen

Freigegebene Zeugnisse dürfen nicht direkt überschrieben werden.

Korrekturprozess:

1. Berechtigte Person beantragt oder startet eine Korrektur.
2. Der Grund wird dokumentiert.
3. Eine neue Arbeitsversion wird erzeugt.
4. Änderungen werden vorgenommen.
5. Erneute Prüfung und Freigabe erfolgen.
6. Eine neue Zeugnisversion wird erzeugt.
7. Die vorherige Version bleibt unverändert archiviert.

## 13. Import bestehender Daten

Die vorhandenen Excel-Daten sollen übernommen werden können.

Vorgesehener Import:

- Schüler
- Klassen
- Fächer
- Lehrpersonen
- Zuordnungen
- optional bestehende Noten

Der Import erfolgt mehrstufig:

1. Datei hochladen
2. Spalten zuordnen
3. Daten validieren
4. Fehlerbericht anzeigen
5. Vorschau anzeigen
6. Import ausdrücklich bestätigen
7. Ergebnis protokollieren

Fehlerhafte Datensätze dürfen nicht unbemerkt übernommen werden.

## 14. Dashboard

### Fachlehrperson

Anzeige:

- eigene Klassen
- eigene Fächer
- offene Zeugnisperioden
- fehlende Noten
- abgeschlossene Eingaben
- Fristen

### Klassenlehrperson

Zusätzlich:

- Vollständigkeit pro Fach
- fehlende Bemerkungen
- fehlende Fehlzeiten
- Status pro Schüler
- zur Freigabe bereite Zeugnisse

### Schulleitung

Zusätzlich:

- Status aller Klassen
- offene Eingaben
- Zeugnisse in Prüfung
- freigegebene Zeugnisse
- Korrekturen

## 15. Datenschutz und Sicherheit

Schülerdaten und Noten sind besonders schützenswerte personenbezogene Daten.

Mindestens umzusetzen:

- ausschliesslicher Betrieb über HTTPS
- sichere Passwort-Hashes
- keine Passwörter im Repository
- Geheimnisse nur über Umgebungsvariablen oder Docker Secrets
- rollenbasierte Zugriffskontrolle
- automatische Sitzungsbeendigung nach Inaktivität
- Schutz vor CSRF
- Schutz vor SQL-Injection
- sichere Cookies
- Login-Sperre nach wiederholten Fehlversuchen
- Protokollierung sicherheitsrelevanter Vorgänge
- minimale Rechte für Datenbankbenutzer
- getrennte Entwicklungs- und Produktionsumgebung
- keine echten Schülerdaten in Tests
- verschlüsselte Backups, sofern extern gespeichert
- dokumentiertes Lösch- und Aufbewahrungskonzept
- keine externen Analyse- oder Trackingdienste
- keine Übertragung von Schülerdaten an externe KI-Dienste

Vor Produktivbetrieb ist eine datenschutzrechtliche Prüfung durch die Schule erforderlich.

## 16. Backup und Wiederherstellung

Mindestens vorzusehen:

- automatisches tägliches PostgreSQL-Backup
- Aufbewahrung mehrerer Generationen
- Backup der erzeugten Zeugnis-PDFs
- Backup der Konfiguration
- dokumentierte Wiederherstellung
- regelmässiger Restore-Test
- keine Sicherung von Secrets im Git-Repository

Ein Backup gilt erst als zuverlässig, wenn die Wiederherstellung getestet wurde.

## 17. Qualitätssicherung

Automatische Tests:

- Modelltests
- Berechtigungstests
- Validierung von Noten
- Freigabeprozess
- Sperrung freigegebener Zeugnisse
- Korrekturprozess
- Importvalidierung
- PDF-Erzeugung
- Konflikterkennung
- Sicherheitsrelevante Zugriffstests

Zusätzlich:

- statische Codeanalyse
- Formatierung
- Linting
- Migrationsprüfung
- Docker-Healthchecks
- manuelle Abnahmetests mit anonymisierten Beispieldaten

## 18. Technische Projektstruktur

Vorgeschlagene Struktur:

```text
zeugnisverwaltung/
├── AGENTS.md
├── PLAN.md
├── README.md
├── .env.example
├── .gitignore
├── compose.yaml
├── Dockerfile
├── pyproject.toml
├── manage.py
├── config/
├── apps/
│   ├── accounts/
│   ├── schools/
│   ├── students/
│   ├── classes/
│   ├── subjects/
│   ├── grades/
│   ├── reports/
│   ├── imports/
│   └── audit/
├── templates/
├── static/
├── tests/
├── scripts/
├── buch/
├── docs/
├── backups/
└── nginx/
    └── zeugnisverwaltung.conf.example
```

## 19. Deployment

Das Deployment darf bestehende Dienste auf dem Server nicht beeinträchtigen.

Vor der Umsetzung prüfen:

- vorhandene Docker-Netzwerke
- belegte Ports
- laufende Container
- vorhandene Nginx-Konfigurationen
- vorhandene Domains und Subdomains
- vorhandene PostgreSQL-Instanzen
- Backup-Verzeichnisse
- Speicherplatz
- Benutzer- und Dateirechte

Die Anwendung soll intern nur auf einem nicht öffentlich erreichbaren Port lauschen.

Der externe Zugriff erfolgt ausschliesslich über Nginx und HTTPS.

## 20. Umsetzungsschritte

### Phase 1: Analyse

- bestehende Excel-Datei analysieren
- vorhandene Zeugnisvorlagen erfassen
- Rollen und Abläufe mit der Schule klären
- Notenskalen und Sonderwerte erfassen
- Datenschutzanforderungen klären
- technische Serverumgebung prüfen
- Codex-Arbeitsweise und Projekterkenntnisse für das Praxislehrbuch in `buch/` dokumentieren

### Phase 2: Technisches Grundgerüst

- Repository initialisieren
- Django-Projekt anlegen
- PostgreSQL integrieren
- Docker Compose erstellen
- Entwicklungsumgebung einrichten
- Benutzeranmeldung einrichten
- Healthcheck erstellen
- Basistests erstellen

### Phase 3: Stammdaten

- Schuljahre
- Zeugnisperioden
- Klassen
- Schüler
- Fächer
- Lehrpersonen
- Unterrichtszuordnungen

### Phase 4: Noteneingabe

- Notenmodell
- Validierung
- tabellarische Eingabe
- Berechtigungen
- Vollständigkeitsprüfung
- Konflikterkennung
- Abschluss pro Fach

### Phase 5: Zeugnisse

- Zeugnisdatenmodell
- Bemerkungen
- Fehlzeiten
- Vorlagen
- PDF-Vorschau
- PDF-Erzeugung
- Klassendruck

### Phase 6: Freigabe und Historie

- Prüfstatus
- Freigabe
- Sperrung
- Versionierung
- Korrekturprozess
- Audit-Protokoll

### Phase 7: Import

- Excel- und CSV-Upload
- Spaltenzuordnung
- Validierung
- Vorschau
- Fehlerbericht
- Importprotokoll

### Phase 8: Betrieb

- Produktionskonfiguration
- Nginx-Beispielkonfiguration
- HTTPS
- Backup
- Restore-Anleitung
- Monitoring
- Deployment-Dokumentation

### Phase 9: Abnahme

- anonymisierte Echtdaten
- mehrere Klassen
- verschiedene Zeugnisvorlagen
- parallele Bearbeitung
- Freigabeprozess
- Ausdruck
- Korrekturfall
- Restore-Test

## 21. Abnahmekriterien

Die erste Version gilt als abnahmefähig, wenn:

- mehrere Lehrpersonen gleichzeitig arbeiten können
- Lehrpersonen nur berechtigte Klassen und Fächer sehen
- Noten zuverlässig validiert werden
- fehlende Eingaben sichtbar sind
- Bearbeitungskonflikte nicht unbemerkt Daten überschreiben
- Zeugnisse für einzelne Schüler erzeugt werden können
- Zeugnisse klassenweise erzeugt werden können
- unterschiedliche Vorlagen unterstützt werden
- freigegebene Zeugnisse gesperrt sind
- Korrekturen versioniert erfolgen
- alle relevanten Änderungen protokolliert werden
- Backups erstellt und wiederhergestellt werden können
- die Anwendung über HTTPS erreichbar ist
- keine Geheimnisse im Repository enthalten sind
- die wichtigsten Abläufe automatisiert getestet sind

## 22. Offene fachliche Fragen

Vor der endgültigen Implementierung sind mindestens folgende Fragen zu klären:

1. Welche Klassen und Klassenstufen gibt es?
2. Welche Zeugnisarten gibt es?
3. Welche Zeugnisvorlagen werden verwendet?
4. Welche Unterschiede bestehen zwischen den Vorlagen?
5. Welche Notenskalen gelten?
6. Gibt es Textbewertungen?
7. Welche Sonderwerte sind zulässig?
8. Welche Fehlzeiten werden ausgewiesen?
9. Welche Bemerkungsfelder werden benötigt?
10. Wer darf Noten ändern?
11. Wer darf Zeugnisse freigeben?
12. Gibt es eine zusätzliche Freigabe durch die Schulleitung?
13. Wie werden Korrekturen aktuell behandelt?
14. Welche Daten stehen in der bestehenden Excel-Datei?
15. Wie lange müssen Zeugnisse und Änderungsprotokolle aufbewahrt werden?
16. Dürfen Zeugnisse dauerhaft digital gespeichert werden?
17. Ist der Zugriff nur im Schulnetz oder auch extern vorgesehen?
18. Wird VPN benötigt?
19. Welche Drucker und Papierformate werden verwendet?
20. Müssen Logos, Unterschriften oder Stempel eingebunden werden?

## 23. Wichtige Grundsatzentscheidung

Vor Beginn der eigentlichen Implementierung müssen folgende Unterlagen anonymisiert vorliegen:

- aktuelle Excel-Datei
- mindestens eine Vorlage jeder Zeugnisart
- Liste der Klassen und Fächer
- Beschreibung des aktuellen Arbeitsablaufs
- Beschreibung der Benutzerrollen
- Beispiele für Sonderfälle
- Vorgaben zu Datenschutz und Aufbewahrung

Das Datenmodell darf erst nach Analyse dieser Unterlagen als verbindlich angesehen werden.

## 24. Aktueller Umsetzungsstand

### Technisches Grundgerüst

Für Phase 2 ist umgesetzt:

- Django 5.2 LTS mit modularer App-Struktur
- projektspezifisches Benutzer-Modell vor den ersten fachlichen Migrationen
- serverseitige Anmeldung und geschützte Startseite
- Sperre nach wiederholten fehlgeschlagenen Anmeldeversuchen
- PostgreSQL in einem projektbezogenen Docker-Compose-Stack
- Webcontainer ohne Rootrechte
- ausschließlich lokale Bindung an `127.0.0.1:8005`
- Healthchecks für PostgreSQL und Django
- Basistests und statische Qualitätskonfiguration

Vorgesehene öffentliche Domain:

```text
https://schule.plebsapps.de
```

Nginx und HTTPS wurden nach erfolgreicher Prüfung des Anwendungsstacks in einem getrennten, ausdrücklich freigegebenen Server-Schritt eingerichtet.

Die Anwendung ist unter `https://schule.plebsapps.de` erreichbar. HTTP wird auf HTTPS umgeleitet, Django bleibt ausschließlich an `127.0.0.1:8005` gebunden, und das Let's-Encrypt-Zertifikat wird durch den aktivierten Certbot-Timer erneuert. Versionierte Bootstrap- und TLS-Vorlagen sowie die Betriebsanleitung liegen unter `nginx/` und `docs/deployment.md` vor.

### UI-Grundsystem

Für die weitere Fachentwicklung ist ein responsives, serverseitig gerendertes Designsystem umgesetzt. Login, Navigation, Dashboard-Karten, Tabellen, Fortschrittsanzeigen, Status und Formulare besitzen ein einheitliches Grundlayout. Externe Fonts, Trackingdienste und unnötiges JavaScript werden nicht verwendet.

Bis zur fachlichen Klärung des Datenmodells zeigt das Dashboard ausschließlich klar gekennzeichnete, flüchtige und vollständig künstliche Beispieldaten. Diese werden nicht in der Datenbank gespeichert und dürfen nicht als reale Schüler-, Klassen- oder Notendaten interpretiert werden.

### Praxislehrbuch

Die Buchstruktur unterscheidet Projektchronik, Fachkapitel und versionsbezogene Referenzen. GPT-5.6 Sol (`gpt-5.6-sol`) ist als Arbeitsgrundlage benannt. Eine eigene Kommandoreferenz erfasst die aktuell dokumentierten Slash-Kommandos der Desktop-App und der Codex CLI sowie die im Projekt verwendeten Codex-, Git-, Docker- und Django-Befehle.

Die Projektchronik wird nach jeder größeren Aufgabe fortgeschrieben. Dadurch bleiben Prompts, Entscheidungen, Befehle, Tests, Blocker, Sicherheitsüberlegungen und Ergebnisse bis zur späteren Druckfassung nachvollziehbar.

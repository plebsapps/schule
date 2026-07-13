# Bildverzeichnis und Generierungsbriefings

Dieses Verzeichnis beschreibt alle geplanten Abbildungen des Praxisbeispiels. Die Platzhalter `[Bild001]` bis `[Bild022]` stehen bereits an der vorgesehenen Stelle im jeweiligen Kapitel oder in der ergänzenden Buchdokumentation. Die Bilder werden in einem getrennten Arbeitsschritt erzeugt.

## Redaktionell überarbeiteter Arbeitsauftrag

> Aktualisiere jetzt das Buch und plane passende Abbildungen. Identifiziere alle Stellen, an denen eine Grafik das Verständnis verbessert, und füge dort fortlaufende Platzhalter im Format `[Bild001]` ein. Erstelle zusätzlich eine vollständige Liste aller Bilder. Beschreibe für jedes Bild so exakt, was dargestellt werden muss, dass es anschließend in einem getrennten Arbeitsschritt mit DALL·E erzeugt werden kann.

Die Buchfassung präzisiert Rechtschreibung und Satzbau. Die fachliche Absicht – Bildstellen markieren und die eigentliche Generierung getrennt vorbereiten – bleibt unverändert.

## Einheitlicher Stil für alle Bilder

- moderne, reduzierte Fachbuchgrafik statt dekorativer Werbeillustration
- heller Hintergrund, dunkelblaue Konturen, Akzente in Blau, Grün und warmem Gelb
- klare visuelle Hierarchie, viel Weißraum, barrierearme Kontraste
- flache Vektorillustration oder präzises isometrisches Diagramm, keine Fotografie
- deutsche Beschriftungen exakt wie angegeben, keine zusätzlichen Fantasietexte
- keine Markenlogos, keine echten Benutzeroberflächen, keine echten Personen
- ausschließlich künstliche Namen und Daten; niemals Tokens, Passwörter, IP-Adressen oder echte Schülerdaten
- drucktauglich, scharfe Kanten, keine Wasserzeichen und keine Signatur

Bei Diagrammen sollte nach der Generierung kontrolliert werden, ob alle Texte korrekt geschrieben sind. Falls das Bildmodell Text fehlerhaft wiedergibt, wird zunächst eine textarme Variante erzeugt und die Beschriftung später im Layout ergänzt.

## Bild001 – Zwei Dokumente, zwei Aufgaben

- Platzierung: Kapitel 1, nach der Abgrenzung von `PLAN.md` und `AGENTS.md`
- Lernziel: Produktwissen und Arbeitsregeln auf einen Blick unterscheiden
- Format: Querformat 3:2
- Muss zeigen: zwei Dokumentkarten; links Produktziel, rechts Arbeitsweise; beide führen gemeinsam zu sicherer Umsetzung
- Exakte Beschriftungen: `PLAN.md`, `Was soll entstehen?`, `AGENTS.md`, `Wie arbeitet Codex?`, `Sichere Umsetzung`
- DALL·E-Prompt:

> Erzeuge eine drucktaugliche deutsche Fachbuchgrafik im reduzierten Vektorstil, Querformat 3:2, heller Hintergrund, dunkelblaue Linien, blaue und grüne Akzente. Links eine Dokumentkarte mit der exakten Überschrift „PLAN.md“ und darunter „Was soll entstehen?“. Rechts eine Dokumentkarte mit der exakten Überschrift „AGENTS.md“ und darunter „Wie arbeitet Codex?“. Von beiden Karten führen gleichwertige Pfeile zu einem zentralen Schild mit der Beschriftung „Sichere Umsetzung“. Klare Typografie, viel Weißraum, keine Logos, keine Personen, keine weiteren Texte, keine Wasserzeichen.

## Bild002 – Professioneller Git-Workflow

- Platzierung: Kapitel 1, nach den acht Schritten der Repository-Anlage
- Lernziel: Entwicklung außerhalb von `main` und kontrollierten Merge visualisieren
- Format: sehr breites Querformat 16:9
- Muss zeigen: `main` → Feature-Branch → Commits → Push → Draft-PR → Prüfungen → Merge → Branch löschen
- DALL·E-Prompt:

> Erzeuge ein präzises horizontales Git-Ablaufdiagramm für ein deutsches Fachbuch, Format 16:9. Zeige von links nach rechts acht klar getrennte Stationen mit Pfeilen: „main“, „Feature-Branch“, „kleine Commits“, „Push“, „Draft-PR“, „Tests und Prüfung“, „Merge nach main“, „Branch löschen“. Der Feature-Branch soll sichtbar von main abzweigen und beim Merge zurücklaufen. Reduzierter Vektorstil, heller Hintergrund, dunkelblaue Linien, grüne Häkchen nur bei Tests und Merge, keine Terminal-Screenshots, keine Logos, keine zusätzlichen Texte.

## Bild003 – Öffentliches Repository, geschützte Schuldaten

- Platzierung: Kapitel 1, nach den Grenzen des öffentlichen Repositorys
- Lernziel: Open Source und Datenschutz klar trennen
- Format: Querformat 3:2
- Muss zeigen: öffentliche Zone mit Code/Dokumentation; geschützte Zone mit Schülerdaten/Backups/Secrets; feste Barriere
- DALL·E-Prompt:

> Erzeuge eine klare Sicherheitsinfografik im Querformat 3:2. Links eine offene, helle Zone „Öffentliches Repository“ mit drei Symbolkarten „Quellcode“, „Dokumentation“, „künstliche Testdaten“. Rechts eine abgeschirmte Zone „Geschützte Serverumgebung“ mit „Schülerdaten“, „Backups“, „Secrets“. Dazwischen eine starke Schutzbarriere mit Schloss und der Beschriftung „Nicht veröffentlichen“. Moderner deutscher Fachbuch-Vektorstil, keine echten Namen, keine Zahlen, keine Logos, keine zusätzlichen Texte.

## Bild004 – Serverarchitektur der Anwendung

- Platzierung: Kapitel 2, nach der Wahl von Port 8005
- Lernziel: Request-Weg und interne Grenzen verstehen
- Format: Hochformat 4:5
- Muss zeigen: Browser → HTTPS/Nginx → Loopback 127.0.0.1:8005 → Django → internes PostgreSQL
- DALL·E-Prompt:

> Erzeuge ein vertikales Architekturdiagramm im Hochformat 4:5 für ein deutsches IT-Fachbuch. Von oben nach unten: „Browser“, Pfeil „HTTPS“, „Nginx Reverse Proxy“, Pfeil „nur intern“, „Django · 127.0.0.1:8005“, Pfeil innerhalb eines Docker-Rahmens, „PostgreSQL · kein öffentlicher Port“. Zeige eine äußere Servergrenze und eine innere Docker-Netzwerkgrenze. Klare dunkelblaue Konturen, blaue und grüne Akzente, weißer Hintergrund, keine Logos, keine zusätzlichen Beschriftungen.

## Bild005 – Getrennter Weg zu HTTPS

- Platzierung: Kapitel 2, nach der Entscheidung für einen separaten Nginx-Schritt
- Lernziel: erst Anwendung prüfen, dann Infrastruktur freigeben
- Format: Querformat 16:9
- Muss zeigen: zwei Phasen mit Prüfgatter
- DALL·E-Prompt:

> Erzeuge ein zweiphasiges Prozessdiagramm, Format 16:9. Phase 1 links heißt „Anwendung intern prüfen“ und enthält „Django“, „PostgreSQL“, „Migrationen“, „Healthchecks“. In der Mitte ein deutliches Prüfgatter „alles gesund?“. Phase 2 rechts heißt „HTTPS freigeben“ und enthält „Nginx“, „Zertifikat“, „öffentlicher Test“. Nur ein grüner Pfeil durch das erfolgreiche Prüfgatter verbindet die Phasen. Reduzierter Fachbuch-Vektorstil, heller Hintergrund, keine Markenlogos, keine Personen.

## Bild006 – Containerrechte richtig korrigieren

- Platzierung: Kapitel 2, nach dem `collectstatic`-Rechtefehler
- Lernziel: Nicht-Root-Prinzip trotz Dateirechtefehler beibehalten
- Format: Querformat 3:2
- Muss zeigen: falscher Weg Root rot markiert; richtiger Weg gezielte Verzeichnisrechte grün
- DALL·E-Prompt:

> Erzeuge eine Vergleichsgrafik im Querformat 3:2. Links rot markiert: Container als „Root“ mit Warnsymbol und Text „zu viele Rechte“. Rechts grün markiert: „Nicht-Root-Benutzer“ erhält gezielt Zugriff auf zwei Ordner „staticfiles“ und „media“. Darüber die gemeinsame Ausgangsmeldung „Schreibzugriff fehlt“. Der rechte Weg endet in „Healthcheck erfolgreich“. Klare deutsche Fachbuchgrafik, flacher Vektorstil, keine zusätzlichen Texte.

## Bild007 – UI-Grundsystem der Zeugnisverwaltung

- Platzierung: Kapitel 3, nach der Gestaltungsentscheidung
- Lernziel: visuelle Komponenten und konsistente Hierarchie zeigen
- Format: Querformat 16:10
- Muss zeigen: abstrahiertes Dashboard mit Sidebar, Kopfzeile, vier Kennzahlen, Tabelle; nur DEMO-Daten
- DALL·E-Prompt:

> Erzeuge ein hochwertiges, aber bewusst abstrahiertes Web-Dashboard-Mockup im Querformat 16:10. Deutsche Schulverwaltung, dunkelblaue Sidebar, helle Kopfzeile, vier Kennzahlenkarten, eine Klassentabelle und ein sichtbares gelbes Kennzeichen „DEMO“. Verwende ausschließlich künstliche Einträge „DEMO-7A“, „3 Schüler“, „3 Fächer“, „1 offene Periode“. Keine echten Namen, keine Logos, keine Browser-Chrome, keine fotorealistischen Elemente, klare druckbare Vektorgrafik.

## Bild008 – Entwicklung von flüchtigen zu reproduzierbaren Beispieldaten

- Platzierung: Kapitel 3, nach der vorläufigen Beispieldatenentscheidung
- Lernziel: Reifegrade von Demo-Daten unterscheiden
- Format: Querformat 16:9
- Muss zeigen: statische Anzeige → Fachmodelle geklärt → Management-Befehl → Datenbank
- DALL·E-Prompt:

> Erzeuge ein vierstufiges Reifegrad-Diagramm im Querformat 16:9. Stationen von links nach rechts: „flüchtige UI-Daten“, „Fachmodell geklärt“, „idempotenter Management-Befehl“, „künstliche Datenbankobjekte“. Jede Station wird stabiler und strukturierter dargestellt. Zwischen den Stationen Pfeile, über allem der Titel „Beispieldaten wachsen mit dem Modell“. Reduzierter deutscher Fachbuchstil, keine Personen, keine zusätzlichen Texte.

## Bild009 – Was Codex-Verhalten beeinflusst

- Platzierung: Kapitel 4, nach der Liste der Einflussfaktoren
- Lernziel: Modell nicht mit gesamter Arbeitsumgebung verwechseln
- Format: quadratisch 1:1
- Muss zeigen: GPT-5.6 Sol im Zentrum; sieben Einflussfaktoren ringförmig
- DALL·E-Prompt:

> Erzeuge eine quadratische Systemgrafik 1:1. Im Zentrum ein neutraler Kreis „GPT-5.6 Sol“. Darum sieben gleichwertige Segmente: „Oberfläche“, „AGENTS.md“, „Skills und Plugins“, „Sandbox“, „Werkzeuge“, „Gesprächskontext“, „Benutzerprompt“. Pfeile zeigen von allen Segmenten zum Zentrum und von dort zum Ergebnis „Codex-Antwort und Aktion“. Keine Roboterfigur, keine OpenAI-Logos, sachlicher Vektorstil, deutsche Beschriftungen exakt, heller Hintergrund.

## Bild010 – Vier Befehlsarten

- Platzierung: Kapitel 4, nach den vier Befehlsarten
- Lernziel: Prompt, Slash-Kommando, Codex CLI und Projektbefehl unterscheiden
- Format: Querformat 2:1
- Muss zeigen: vier Spalten mit je einem typischen Beispiel
- DALL·E-Prompt:

> Erzeuge eine klare Vier-Spalten-Infografik im breiten Querformat 2:1. Spalte 1: „Natürlicher Prompt“ mit Beispiel „Analysiere PLAN.md“. Spalte 2: „Slash-Kommando“ mit Beispiel „/status“. Spalte 3: „Codex CLI“ mit Beispiel „codex review“. Spalte 4: „Projektbefehl“ mit Beispiel „pytest“. Unter jeder Spalte eine kurze Ebene: „Aufgabe“, „Oberfläche“, „Codex starten“, „Projekt ausführen“. Präziser deutscher Fachbuch-Vektorstil, monospace für Befehle, keine weiteren Texte.

## Bild011 – Codex-Oberflächen im Vergleich

- Platzierung: Kapitel 4, nach der Cloud-Ausführung
- Lernziel: lokale und entfernte Kontexte unterscheiden
- Format: Querformat 16:9
- Muss zeigen: Desktop-App, CLI, IDE, Cloud; jeweils Kontext und Ausführungsort
- DALL·E-Prompt:

> Erzeuge eine Vergleichsgrafik im Querformat 16:9 mit vier gleich großen Karten: „Desktop-App“, „Codex CLI“, „IDE-Erweiterung“, „Cloud-Ausführung“. Zeige je Karte symbolisch Oberfläche, Kontextquelle und Ausführungsort. Desktop: Projekt und Aufgaben; CLI: Terminal und lokales Repository; IDE: offene Dateien und markierter Code; Cloud: bereitgestellte entfernte Umgebung. Verbinde alle Karten mit „gleiche Projektregeln, unterschiedlicher Kontext“. Keine Markenlogos, keine echten Screenshots, sachlicher Vektorstil.

## Bild012 – Lebenszyklus eines zuverlässigen Backups

- Platzierung: Kapitel 7, nach der Zerlegung in vier Werkzeuge
- Lernziel: Backup ist erst mit Restore-Test vollständig
- Format: Querformat 16:9
- Muss zeigen: Dump → atomare Ablage → Prüfsumme → Aufbewahrung → isolierter Restore → Ergebnis
- DALL·E-Prompt:

> Erzeuge ein zyklisches Backup-Diagramm im Querformat 16:9. Stationen: „pg_dump“, „temporäre Datei“, „atomar fertigstellen“, „SHA-256 prüfen“, „geschützt aufbewahren“, „isoliert wiederherstellen“, „Struktur prüfen“. Ein grüner Rückpfeil führt vom erfolgreichen Strukturtest zum nächsten geplanten Backup. Zeige bei der Ablage klein „0700“ am Ordner und „0600“ an der Datei. Keine realen Pfade, keine Dateninhalte, präziser deutscher Fachbuchstil.

## Bild013 – Drei Schutzebenen für Backups

- Platzierung: Kapitel 7, nach Sicherheits- und Datenschutzentscheidungen
- Lernziel: Rechte, Verschlüsselung und externes Ziel nicht verwechseln
- Format: Querformat 3:2
- Muss zeigen: konzentrische Schutzschichten
- DALL·E-Prompt:

> Erzeuge eine Sicherheitsgrafik mit drei konzentrischen Schutzschichten, Querformat 3:2. Innerer Kern „Datenbankbackup“. Erste Schicht „Dateirechte 0600“. Zweite Schicht „verschlüsseltes Backupziel“. Dritte Schicht „getrennter Speicherort und Zugriffskontrolle“. Daneben ein Hinweisfeld „Prüfsumme erkennt Veränderung, verschlüsselt aber nicht“. Heller Hintergrund, dunkelblaue Konturen, grüne Schutzakzente, keine weiteren Texte.

## Bild014 – Test- und Produktionskonfiguration auseinanderhalten

- Platzierung: Kapitel 7, nach dem konfigurationsbedingten Testfehler
- Lernziel: gleiche Anwendung, unterschiedliche Konfigurationsprofile
- Format: Querformat 16:9
- Muss zeigen: Testprofil und Produktionsprofil, falsche Kreuzung verursacht 301/Manifestfehler
- DALL·E-Prompt:

> Erzeuge eine zweigeteilte technische Infografik im Querformat 16:9. Links „Testprofil“ mit „DEBUG=true“, „HTTPS-Redirect=false“, „Testdatenbank“. Rechts „Produktionsprofil“ mit „DEBUG=false“, „HTTPS-Redirect=true“, „Staticfiles-Manifest“. In der Mitte ein rotes Kreuz bei „Produktionswerte im Test“ mit zwei kleinen Fehlerkarten „301 statt Testantwort“ und „Manifest fehlt“. Unten grüner Satz „Konfigurationsklasse ausdrücklich setzen“. Präzise deutsche Typografie, keine Logos.

## Bild015 – Fachliches Stammdatenmodell

- Platzierung: Kapitel 8, nach der Erklärung historischer Zuordnungen
- Lernziel: wichtigste Entitäten und Beziehungen verstehen
- Format: sehr breites Querformat 2:1
- Muss zeigen: Schule, Schuljahr, Periode, Klasse, Schüler, Klassenzuordnung, Fach, Lehrkraft, Unterrichtszuordnung, Vorlage
- DALL·E-Prompt:

> Erzeuge ein sauberes Entity-Relationship-Diagramm im breiten Querformat 2:1. Entitäten als Karten: „Schule“, „Schuljahr“, „Zeugnisperiode“, „Klasse“, „Schüler“, „Klassenzuordnung“, „Fach“, „Lehrkraft“, „Unterrichtszuordnung“, „Zeugnisvorlage“. Beziehungen: Schule zu Schuljahr, Fach, Schüler und Vorlage; Schuljahr zu Periode und Klasse; Klassenzuordnung verbindet Schüler und Klasse; Unterrichtszuordnung verbindet Lehrkraft, Klasse, Fach und Zeugnisperiode. Hebe Klassenzuordnung und Unterrichtszuordnung als historische Verbindungstabellen hervor. Keine Felddetails, keine Crow’s-Foot-Sonderzeichen, klare Pfeile, deutscher Fachbuchstil.

## Bild016 – Staff-Status ist keine Fachberechtigung

- Platzierung: Kapitel 8, nach dem fehlgeschlagenen Berechtigungstest
- Lernziel: Zugang zum Adminbereich und Modellrechte trennen
- Format: Querformat 3:2
- Muss zeigen: Anmeldung → is_staff-Gatter → Modellberechtigungs-Gatter → Daten; HTTP 403 bei fehlendem Recht
- DALL·E-Prompt:

> Erzeuge ein Berechtigungspfad-Diagramm im Querformat 3:2. Start „angemeldeter Benutzer“. Erstes Gatter „is_staff?“ führt bei Nein zu „kein Adminzugang“. Bei Ja folgt zwingend ein zweites Gatter „Modellberechtigung vorhanden?“. Bei Nein endet der Pfad rot mit „HTTP 403“. Nur bei Ja führt ein grüner Pfad zu „Schuldaten anzeigen oder ändern“. Betone sichtbar: „Staff allein reicht nicht“. Sachlicher deutscher Vektorstil, keine Personenbilder.

## Bild017 – Idempotenter Beispieldaten-Befehl

- Platzierung: Kapitel 8, nach der Beschreibung des Management-Befehls
- Lernziel: wiederholte Ausführung ohne Duplikate erklären
- Format: Querformat 16:9
- Muss zeigen: erster Lauf erstellt DEMO-Objekte, zweiter Lauf erkennt sie, gleicher Endbestand
- DALL·E-Prompt:

> Erzeuge ein Vorher-Nachher-Ablaufdiagramm im Querformat 16:9. Erster Lauf: Befehl „create_demo_master_data“ erzeugt „1 DEMO-Schule“, „1 DEMO-Klasse“, „3 DEMO-Schüler“, „3 DEMO-Fächer“. Zweiter Lauf desselben Befehls zeigt Lupensymbole „bereits vorhanden“ und endet beim exakt gleichen Bestand, deutlich „keine Duplikate“. Seitlich ein geschütztes Administratorkonto mit Text „unverändert“. Keine echten Namen oder Passwörter, klarer Fachbuch-Vektorstil.

## Bild018 – Rollenbezogene Dashboard-Abfrage

- Platzierung: Kapitel 8, nach der Umstellung auf echte Dashboard-Daten
- Lernziel: Daten bereits in der Abfrage filtern
- Format: Querformat 16:9
- Muss zeigen: Datenbank in Mitte; Admin/Schulleitung bekommt Gesamtübersicht; Lehrkraft nur zugewiesene Klasse; fremde Klasse blockiert
- DALL·E-Prompt:

> Erzeuge ein rollenbezogenes Datenflussdiagramm im Querformat 16:9. In der Mitte „Datenbank“. Links Rollen „Administration / Schulleitung“ mit grünem Pfeil zu „Gesamtübersicht“. Rechts „Fach- oder Klassenlehrkraft“ mit grünem Pfeil nur zu „zugewiesene Klasse DEMO-7A“. Eine zweite Klasse „fremde Klasse“ ist durch eine rote serverseitige Sperre blockiert und gelangt nicht ins HTML. Titel „Filtern in der Datenbankabfrage“. Keine echten Namen, keine Logos.

## Bild019 – Vertikaler Demo-Zeugnisablauf

- Platzierung: Kapitel 9, nach der Beschreibung des zusammenhängenden Ablaufs
- Lernziel: drei Demo-Punkte als eine Nutzungsreise zeigen
- Format: breites Querformat 2:1
- Muss zeigen: Zuordnung → Schülerliste → Noten → speichern → abschließen → gesperrt → Vorschau → Druck
- DALL·E-Prompt:

> Erzeuge ein horizontales End-to-End-Prozessdiagramm im breiten Format 2:1. Stationen: „Unterrichtszuordnung“, „Schülerliste“, „Noten eingeben“, „Zwischenspeichern“, „vollständig abschließen“, „gesperrt“, „Zeugnisvorschau“, „Browserdruck“. Zeige bei Speichern ein kleines Audit-Symbol und bei Abschluss ein Schloss. Verwende künstliche Bezeichnung „DEMO-7A“, keine echten Schülernamen, klare deutsche Fachbuchgrafik.

## Bild020 – Optimistisches Locking bei Noten

- Platzierung: Kapitel 9, nach der Beschreibung der Versionsnummer
- Lernziel: paralleles Überschreiben verständlich machen
- Format: Querformat 16:9
- Muss zeigen: Lehrkraft A und B laden v1; A speichert v2; B sendet v1; Konflikt statt Überschreiben
- DALL·E-Prompt:

> Erzeuge ein Sequenzdiagramm im Querformat 16:9 mit drei Spalten „Lehrkraft A“, „Server“, „Lehrkraft B“. Beide laden zuerst „Note 2,0 · Version 1“. Lehrkraft A speichert „Note 2,5“, Server bestätigt „Version 2“. Lehrkraft B sendet danach auf Basis „Version 1“ die Note „3,0“. Der Server blockiert rot mit „Konflikt – Seite neu laden“; die gespeicherte Version 2 bleibt unverändert. Präzise deutsche Beschriftung, keine Personenfotos, technischer Vektorstil.

## Bild021 – Druckbare Zeugnisvorschau mit klarer Grenze

- Platzierung: Kapitel 9, nach der bewussten Abgrenzung der Druckansicht
- Lernziel: überzeugende Demo zeigen, ohne Freigabe vorzutäuschen
- Format: Hochformat A4-ähnlich 4:5
- Muss zeigen: stilisierte Vorschauseite mit künstlichen Daten und deutlichem Hinweis
- DALL·E-Prompt:

> Erzeuge ein drucktaugliches, stilisiertes Zeugnis-Mockup im Hochformat 4:5, weißes Papier auf sehr hellem Hintergrund. Oben „DEMO – Beispielschule am Stadtpark“, darunter „1. Halbjahr · Klasse DEMO-7A“. Schülername ausschließlich „Alex Muster“. Kleine Tabelle mit „Deutsch 2,0“, „Mathematik 2,5“, „Englisch 3,0“. Sehr deutlich oberhalb und im Fußbereich: „NICHT FREIGEGEBENE DEMO-VORSCHAU“. Seriöses Schulverwaltungsdesign, keine Unterschriften, keine Siegel, keine Logos, kein Wappen, keine echten Daten, keine weiteren Texte.

## Bild022 – Buchtransparenz und Entstehung

- Platzierung: `buch/projektchronik.md`, im Abschnitt zur Entstehung und Transparenz des Buchs
- Lernziel: verdeutlichen, dass das Praxisbeispiel aus dokumentierten Arbeitsartefakten, Entscheidungen und Prüfungen entstanden ist
- Format: Querformat 3:2
- Muss zeigen: Buchstapel in der Mitte; daneben Karten für Prompts, Entscheidungen, Tests und Versionen; unten Zeitachse mit den Schritten Entstehung, Arbeitsweise, Transparenz; kleine Autorenkarte
- DALL·E-Prompt:

> Erzeuge eine drucktaugliche deutsche Fachbuchgrafik im reduzierten Vektorstil, Querformat 3:2, heller Hintergrund, dunkelblaue Linien, blaue, grüne und warme Gelb-Akzente. In der Mitte ein Buchstapel mit einer Buchkarte. Daneben vier Dokumentkarten mit den Überschriften „PROMPTS“, „ENTSCHEIDUNGEN“, „TESTS“ und „VERSIONEN“. Unten eine Zeitachse mit den Beschriftungen „Entstehung“, „Arbeitsweise“ und „Transparenz“. Ergänze eine kleine Autorenkarte mit der Beschriftung „Autor“. Klare Typografie, viel Weißraum, keine Logos, keine Personen, keine weiteren Texte, keine Wasserzeichen.

## Produktions- und Ablagehinweise

Nach der Generierung soll jede Datei unter `Bilder/` nach folgendem Muster abgelegt werden:

```text
bild001-plan-und-agents.png
bild002-git-workflow.png
...
bild021-zeugnisvorschau.png
bild022-buchtransparenz-autor.png
```

Vor der Einbindung sind zu prüfen:

1. Nummer und Motiv stimmen mit dem Platzhalter überein.
2. Alle sichtbaren Texte sind korrekt geschrieben.
3. Es sind keine echten Personen, Schülerdaten, Secrets oder Markenlogos enthalten.
4. Die Grafik bleibt in Graustufen verständlich und besitzt ausreichenden Kontrast.
5. Die Auflösung reicht für mindestens 300 dpi in der vorgesehenen Druckgröße.
6. Die Quelldatei und die verwendete Promptfassung werden nachvollziehbar archiviert.

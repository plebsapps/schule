# Kapitel 6: Mit unbekannten Fachdetails sicher beginnen

Ein Softwareprojekt kann nicht immer auf vollständige Vorlagen, Tabellen und Prozessbeschreibungen warten. Gleichzeitig wäre es gefährlich, aus wenigen Annahmen sofort ein starres Datenmodell oder eine scheinbar fertige Noteneingabe zu bauen. Dieses Kapitel zeigt den gewählten Mittelweg: ein kleiner, erweiterbarer Fachkern mit klar markierten Grenzen.

## Redaktionell überarbeiteter Prompt

> Leider liegen uns noch keine Vorlagen vor, und das Datenmodell muss später möglicherweise angepasst werden. Trotzdem sollen Fächer, Schülerinnen und Schüler, Dokumentvorlagen für Zeugnisse, Noten, Lehrkräfte und alle weiteren schulischen Stammdaten eingegeben werden können. Merge zuerst Pull Request 9 und setze die Entwicklung anschließend fort.

Die Buchfassung korrigiert Sprache und Struktur, ohne die Anforderung zu erweitern. Der Wunsch nach Noteneingabe wird bewusst nicht als Freigabe für eine ungeschützte Schnelllösung verstanden.

## Entscheidung: zuerst sichere Stammdaten

Pull Request 9 wurde zunächst konfliktfrei nach `main` gemergt. Für die neue Aufgabe entstand danach ein eigener Feature-Branch. Die bestehende Architektur besaß bereits Anmeldung, PostgreSQL, ein eigenes Benutzermodell und eine geschützte Django-Administration. Deshalb wurde diese Administration als erster Eingabekanal wiederverwendet.

Der Fachkern trennt:

- Schule, Schuljahr und Zeugnisperiode
- Lehrkräfte als Benutzerkonten mit schulischer Rolle
- Fächer mit konfigurierbarem Notenbereich
- Klassen und Klassenleitungen
- Schülerstammdaten und historische Klassenzuordnungen
- Unterrichtszuordnungen pro Klasse, Fach, Lehrkraft und Periode
- versionierte Metadaten für spätere Zeugnisvorlagen

Historische Zuordnungen stehen in eigenen Tabellen. Dadurch muss ein Klassenwechsel nicht durch Überschreiben alter Schülerdaten abgebildet werden.

## Ein hilfreicher fehlgeschlagener Test

Der erste Berechtigungstest erwartete, dass jeder Benutzer mit `is_staff=True` Schuldaten öffnen könne. Django antwortete korrekt mit HTTP 403: Staff-Zugang allein verleiht noch keine Modellberechtigung. Die Anwendung wurde nicht aufgeweicht. Stattdessen wurden Test und Navigation so korrigiert, dass jede Datenart ihre ausdrücklichen Anzeige-, Anlage-, Änderungs- und Löschrechte behält.

## Warum Noten noch gesperrt bleiben

Eine einfache Notentabelle wäre schnell erstellt. Sie wäre aber fachlich und sicherheitstechnisch unvollständig. Vor einer Freischaltung müssen mindestens die zugewiesene Schule, Klasse, das Fach, die Zeugnisperiode, deren Status, die Notenskala und die letzte Datensatzversion serverseitig geprüft werden. Außerdem sind Audit-Protokoll und Konfliktmeldung erforderlich.

Die wichtige Codex-Erkenntnis lautet: Ein Auftrag darf in sichere, nutzbare Ausbaustufen zerlegt werden, wenn eine sofortige Gesamtumsetzung zentrale Schutzregeln verletzen würde. Die noch nicht erfüllte Anforderung muss dabei sichtbar bleiben und als nächster Schritt geplant werden.

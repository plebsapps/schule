# Schulstammdaten verwalten

## Aktueller Funktionsumfang

Der erste fachliche Datenstand wird über die serverseitige Django-Administration gepflegt. Berechtigte Benutzer erreichen sie über die Verwaltungslinks auf der Startseite oder unter `/admin/`.

Erfasst werden können:

- Schulen
- Schuljahre und Zeugnisperioden
- Lehrkräfte als Benutzerkonten mit schulischer Rolle
- Fächer einschließlich Notenbereich und Schrittweite
- Klassen und Klassenleitungen
- Schülerinnen und Schüler
- historische Klassenzuordnungen
- Unterrichtszuordnungen aus Lehrkraft, Klasse, Fach und Zeugnisperiode
- Metadaten versionierter Zeugnisvorlagen

Die Eingabe erfolgt in dieser Reihenfolge, weil spätere Datensätze auf frühere verweisen:

1. Schule
2. Schuljahr
3. Zeugnisperiode
4. Lehrkräfte
5. Fächer
6. Klassen
7. Schüler und Klassenzuordnungen
8. Unterrichtszuordnungen
9. Zeugnisvorlagen-Metadaten

## Berechtigungen

`is_staff` gewährt nur grundsätzlich Zugang zur Administration. Jede Modellart benötigt zusätzlich ihre eigenen Django-Berechtigungen zum Anzeigen, Hinzufügen, Ändern oder Löschen. Superuser besitzen alle Berechtigungen.

Normale Lehrkräfte dürfen die Stammdatenverwaltung nicht öffnen. Rollen allein ersetzen keine Berechtigungsprüfung. Objektbezogene Beschränkungen nach Schule, Klasse und Fach werden vor der Noteneingabe ergänzt.

## Datenintegrität

- Abhängige Schulen, Schuljahre, Klassen, Fächer, Benutzer und Schüler werden durch `PROTECT` vor unbemerktem Löschen geschützt.
- Zeiträume werden auf eine sinnvolle Reihenfolge geprüft.
- Zeugnisperioden müssen innerhalb ihres Schuljahres liegen.
- Klassenzuordnungen dürfen keine Schule wechseln.
- Unterrichtszuordnungen müssen zu derselben Schule und demselben Schuljahr gehören.
- Eindeutigkeitsbedingungen verhindern doppelte interne Schülernummern, Klassenbezeichnungen und Zuordnungen.

## Bewusste Grenzen

Die Dashboard-Kennzahlen bleiben vorerst künstliche Beispieldaten. Noten können in diesem Stand noch nicht eingegeben werden. Eine Noteneingabe wird erst freigeschaltet, wenn serverseitige Objektberechtigungen, Notenvalidierung, Audit-Protokollierung und Schutz vor parallelem Überschreiben implementiert und getestet sind.

Die Zeugnisvorlagenverwaltung speichert nur Bezeichnung, Art, Klassenstufe, Vorlagenschlüssel und Version. Freie HTML-Eingaben oder Datei-Uploads sind aus Sicherheits- und Reproduzierbarkeitsgründen noch nicht möglich.

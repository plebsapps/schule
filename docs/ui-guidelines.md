# UI-Grundregeln

## Ziel

Die Oberfläche soll ruhig, professionell und auch bei langen Arbeitssitzungen verständlich bleiben. Datenschutz, Berechtigungen und fachliche Zustände müssen sichtbar und eindeutig vermittelt werden.

## Gestaltungsprinzipien

- serverseitig gerenderte HTML-Seiten als Standard
- möglichst wenig JavaScript
- klare Seitenüberschriften und konsistente Navigation
- ausreichende Kontraste und sichtbare Tastaturfokusse
- semantische Überschriften, Tabellen, Formulare und Statusangaben
- responsive Darstellung ohne Verlust wichtiger Informationen
- keine externen Fonts, Tracker, Analyse- oder Werbedienste
- Icons niemals als einzige Information verwenden
- Fehler verständlich im Kontext anzeigen
- sensible technische Details nicht in Fehlermeldungen ausgeben

## Beispieldaten

Beispieldaten müssen:

- vollständig künstlich sein
- sichtbar als Demo gekennzeichnet sein
- aus einer klar abgegrenzten Quelle stammen
- keine echten Namen oder Schülerdaten nachahmen
- keine fachlichen Datenbankmigrationen vorwegnehmen
- nicht automatisch produktive Benutzerkonten mit Standardpasswörtern anlegen

Das aktuelle Dashboard verwendet ausschließlich flüchtige Werte aus `apps/core/demo_data.py`. Diese Daten dienen der UI-Entwicklung und sind kein verbindliches Fachmodell.

## Farben und Status

Farben unterstützen den Status, ersetzen aber niemals Text. Grün steht für vollständig oder verfügbar, Gelb für Aufmerksamkeit, Rot für Fehler und Blau für neutrale Arbeitszustände. Status müssen zusätzlich ausgeschrieben werden.

## Formulare

- jedes Eingabefeld besitzt eine sichtbare Beschriftung
- Pflichtfelder und Validierungsfehler werden serverseitig geprüft
- Aktionen verwenden eindeutige Verben
- destructive Aktionen benötigen zusätzliche Bestätigung
- Login- und Sicherheitsformulare verwenden CSRF-Schutz

## Weiterentwicklung

Neue Fachmodule sollen dieses Grundlayout wiederverwenden. Vor größeren Änderungen sind Desktop-, Tablet- und Mobilansicht sowie Tastaturbedienung zu prüfen.

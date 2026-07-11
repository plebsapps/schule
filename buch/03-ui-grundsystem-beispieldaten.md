# Kapitel 3: Ein professionelles UI mit sicheren Beispieldaten

## Ausgangslage

Nach dem technischen Deployment funktionierten Anmeldung, Datenbank und HTTPS, die Oberfläche bestand jedoch nur aus ungestalteten Standardformularen. Für die weitere Entwicklung musste ein visuelles Grundsystem geschaffen werden, bevor zahlreiche Fachseiten voneinander abweichende Einzellösungen erzeugen.

## Redaktionell überarbeiteter Prompt

> Die Anwendung benötigt ein professionelles und konsistentes Design. Ergänze außerdem geeignete Beispieldaten.

## Analyse vor der Umsetzung

Zu diesem Zeitpunkt existierten noch keine verbindlich geklärten Fachmodelle für Klassen, Schüler, Fächer oder Noten. Dauerhafte Beispieldatensätze hätten deshalb fachliche Entscheidungen vorweggenommen und möglicherweise spätere Migrationen erschwert.

Codex trennte daher zwei Aufgaben:

1. Das wiederverwendbare UI-Grundsystem wurde als echte Produktkomponente umgesetzt.
2. Die Dashboard-Werte wurden als klar abgegrenzte, flüchtige Demonstrationsdaten ergänzt.

## Gestaltungsentscheidung

Die Anwendung verwendet ein ruhiges, kontrastreiches Verwaltungsdesign mit:

- einer klaren Seiten- und Navigationshierarchie
- einem zweigeteilten Anmeldebildschirm
- wiederverwendbaren Karten, Tabellen und Statusanzeigen
- sichtbaren Tastaturfokussen
- responsiven Layouts für kleinere Bildschirme
- möglichst wenig JavaScript
- ausschließlich lokal ausgeliefertem CSS

Externe Schriften, Trackingdienste und Bilddienste wurden bewusst vermieden. Dadurch entstehen weder unnötige Datenübertragungen noch zusätzliche Verfügbarkeits- und Datenschutzabhängigkeiten.

[Bild007]

## Umgang mit Beispieldaten

Die Demonstrationswerte sind sichtbar mit `DEMO` und dem Hinweis „Ausschließlich künstliche Beispieldaten“ gekennzeichnet. Namen verwenden Begriffe wie „Beispiel“, „Muster“ und „Demo“. Die Werte liegen in einer eigenen Quellcodedatei und erzeugen keine Datenbankobjekte.

Diese Lösung ist absichtlich vorläufig. Sobald die anonymisierten fachlichen Unterlagen analysiert und die Modelle freigegeben sind, werden versionierte Fixtures oder Management-Kommandos für realistische künstliche Datensätze ergänzt.

[Bild008]

## Tests

Automatisierte Tests prüfen:

- Anmeldung bleibt Voraussetzung für das Dashboard
- Demo-Hinweis wird angezeigt
- künstliche Beispielbezeichnungen erscheinen
- Dashboard-Aufruf erzeugt keine unerwarteten Datenbankobjekte
- Login-Felder besitzen sichtbare Beschriftungen
- CSS wird lokal gefunden
- keine externen Font-Dienste werden eingebunden

Der erste Testlauf fand einen Konfigurationsfehler: Das neue Root-Verzeichnis `static/` war noch nicht in Djangos `STATICFILES_DIRS` eingetragen. Dadurch hätte `collectstatic` das Design nicht übernommen. Der Asset-Test machte den Fehler vor dem Deployment sichtbar; die statische Suchkonfiguration wurde anschließend gezielt ergänzt.

Der anschließende reale HTTPS-Test fand einen zweiten Fehler: `collectstatic` kopierte das CSS zwar in den Container, aber Djangos Produktionsserver liefert statische Dateien standardmäßig nicht aus. Der externe Nginx konnte auf das containerinterne Verzeichnis ebenfalls nicht zugreifen. Statt ein zusätzliches schreibbares Host-Volume mit eigener Rechteverwaltung einzuführen, wurde die produktionsstabile WSGI-Middleware WhiteNoise ergänzt. Sie liefert versionierte und komprimierte statische Dateien direkt aus dem isolierten Webcontainer aus.

Beim letzten Container-Neustart traf die sofort ausgeführte externe Prüfung kurzzeitig auf `502 Bad Gateway`, weil Nginx bereits weiterleitete, während Gunicorn noch startete. Nach dem erfolgreichen Container-Healthcheck antworteten CSS und Anwendung regulär. Die Erkenntnis: Externe Abnahmeprüfungen müssen auf den Healthstatus warten; ein einzelner Aufruf unmittelbar nach `docker compose up` ist kein zuverlässiger Betriebsnachweis.

## Übertragbare Erkenntnis

„Beispieldaten hinzufügen“ bedeutet nicht automatisch, frühzeitig Tabellen mit erfundenen Fachannahmen zu füllen. Codex sollte zuerst entscheiden, ob Daten nur eine Oberfläche demonstrieren oder bereits ein freigegebenes Domänenmodell testen sollen. Diese Trennung verhindert unnötige Migrationen und macht den vorläufigen Charakter für Benutzer sichtbar.

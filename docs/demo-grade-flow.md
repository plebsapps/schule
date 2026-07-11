# Demo-Ablauf für Noten und Zeugnisvorschau

## Ablauf

1. Eine berechtigte Lehrkraft öffnet **Noteneingabe** und wählt eine zugewiesene Klasse, ein Fach und eine offene Zeugnisperiode.
2. Sie trägt für alle Schüler Noten innerhalb der am Fach konfigurierten Skala und Schrittweite ein.
3. **Zwischenspeichern** lässt die Eingabe weiter bearbeitbar.
4. **Vollständig abschließen** ist erst möglich, wenn alle Schüler eine Note besitzen. Danach ist die Eingabe gesperrt.
5. Ein Administrator kann eine abgeschlossene Eingabe in der Django-Administration über die Aktion **Ausgewählte Noteneingaben wieder öffnen** entsperren.
6. Die Zeugnisvorschau zeigt die aktuell gespeicherten Noten eines Schülers und kann über die Browser-Druckfunktion ausgegeben werden.

## Sicherheit und Integrität

- Unterrichtszuordnung, Rolle und Klassenbezug werden serverseitig geprüft.
- Nur offene Zeugnisperioden erlauben Änderungen.
- Notenbereich und Schrittweite werden serverseitig validiert.
- Versionsnummern verhindern unbemerktes Überschreiben bei paralleler Bearbeitung.
- Speichern, Abschluss und Wiederöffnung werden im unveränderbaren Audit-Modell protokolliert.
- Abgeschlossene Eingaben sind für Lehrkräfte gesperrt.
- Direkte Notenänderungen in der Django-Administration sind deaktiviert.

## Bewusste Demo-Grenzen

Die HTML-Ansicht ist eine nicht freigegebene Vorschau, kein rechtlich oder fachlich finales Zeugnis. Noch nicht enthalten sind PDF-Archivierung, Zeugnisversionen, Fehlzeiten, Bemerkungen, Korrekturversionen und ein mehrstufiger Freigabeprozess.

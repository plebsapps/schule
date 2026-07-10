"""Rein künstliche Anzeigedaten für das UI-Grundgerüst.

Die Daten werden nicht gespeichert und bilden kein verbindliches Fachmodell ab.
"""

DEMO_DASHBOARD = {
    "school_year": "2026/2027",
    "period": "1. Halbjahr",
    "summary": (
        {"label": "Klassen", "value": "3", "detail": "künstliche Beispielklassen", "tone": "blue"},
        {"label": "Lernende", "value": "72", "detail": "nur Demonstrationswert", "tone": "violet"},
        {"label": "Offene Eingaben", "value": "14", "detail": "in 4 Fachzuordnungen", "tone": "amber"},
        {"label": "Vollständig", "value": "81 %", "detail": "Beispiel-Fortschritt", "tone": "green"},
    ),
    "classes": (
        {"name": "7A", "lead": "Lehrkraft Beispiel", "complete": 92, "missing": 5, "status": "Fast vollständig"},
        {"name": "8B", "lead": "Lehrkraft Muster", "complete": 78, "missing": 16, "status": "In Bearbeitung"},
        {"name": "9C", "lead": "Lehrkraft Demo", "complete": 64, "missing": 24, "status": "Eingabe offen"},
    ),
    "tasks": (
        {"title": "Noten in Mathematik ergänzen", "context": "Klasse 8B · 6 Einträge fehlen", "priority": "Heute"},
        {"title": "Vollständigkeit prüfen", "context": "Klasse 7A · 2 Fächer offen", "priority": "Diese Woche"},
        {"title": "Bemerkungen vorbereiten", "context": "Klasse 9C · künstlicher Arbeitsauftrag", "priority": "Später"},
    ),
}

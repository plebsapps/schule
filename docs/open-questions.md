# Offene Fragen und bewusste Entscheidungen

## HSTS-Preload

Die Produktionskonfiguration bereitet HSTS mit einem Jahr Laufzeit und `includeSubDomains` vor. `SECURE_HSTS_PRELOAD` bleibt zunächst deaktiviert.

Begründung: Die Aufnahme in Browser-Preload-Listen ist eine langfristige Entscheidung und kann nicht kurzfristig rückgängig gemacht werden. Vor einer Aktivierung müssen HTTPS-Betrieb, Zertifikatserneuerung und alle betroffenen Subdomains dauerhaft abgesichert sein.

Auswirkung: `python manage.py check --deploy` meldet bis zu dieser Entscheidung die Warnung `security.W021`. Die Warnung wird nicht unterdrückt.

## Öffentlicher Zugriff

Vor der Nginx-/HTTPS-Freigabe ist fachlich zu entscheiden, ob `schule.plebsapps.de` aus dem gesamten Internet oder nur über Schulnetz beziehungsweise VPN erreichbar sein soll. Unabhängig davon bleiben Authentifizierung und serverseitige Berechtigungen erforderlich.

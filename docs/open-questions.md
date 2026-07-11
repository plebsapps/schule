# Offene Fragen und bewusste Entscheidungen

## HSTS-Preload

Die Produktionskonfiguration aktiviert HSTS mit einem Jahr Laufzeit, `includeSubDomains` und `preload`.

Begründung: Der HTTPS-Betrieb ist bereits produktiv, die Zertifikatskette wird regelmäßig erneuert und die betroffene Domain ist klar abgegrenzt. Für dieses Projekt ist die Preload-Variante daher die saubere Endkonfiguration.

Auswirkung: `python manage.py check --deploy` meldet die Warnung `security.W021` nicht mehr.

## Öffentlicher Zugriff

Vor der Nginx-/HTTPS-Freigabe ist fachlich zu entscheiden, ob `schule.plebsapps.de` aus dem gesamten Internet oder nur über Schulnetz beziehungsweise VPN erreichbar sein soll. Unabhängig davon bleiben Authentifizierung und serverseitige Berechtigungen erforderlich.

# Offene Fragen und bewusste Entscheidungen

## HSTS-Preload

Die Produktionskonfiguration aktiviert HSTS mit einem Jahr Laufzeit, `includeSubDomains` und `preload`.

Begründung: Der HTTPS-Betrieb ist bereits produktiv, die Zertifikatskette wird regelmäßig erneuert und die betroffene Domain ist klar abgegrenzt. Für dieses Projekt ist die Preload-Variante daher die saubere Endkonfiguration.

Auswirkung: `python manage.py check --deploy` meldet die Warnung `security.W021` nicht mehr.

## Zugriffsbeschränkung

`schule.plebsapps.de` wird nur im Schulnetz betrieben. Externe Zugriffe erfolgen ausschließlich über VPN.

Begründung: Die Anwendung verarbeitet sensible personenbezogene Schuldaten. Eine Begrenzung auf Schulnetz und VPN reduziert das Risiko unnötiger Exposition und passt zur Datenschutzanforderung dieses Projekts.

Unabhängig davon bleiben Authentifizierung und serverseitige Berechtigungen erforderlich.

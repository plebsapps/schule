# Offene Fragen und bewusste Entscheidungen

## HSTS-Preload

Die Produktionskonfiguration aktiviert HSTS mit einem Jahr Laufzeit, `includeSubDomains` und `preload`.

Begründung: Der HTTPS-Betrieb ist bereits produktiv, die Zertifikatskette wird regelmäßig erneuert und die betroffene Domain ist klar abgegrenzt. Für dieses Projekt ist die Preload-Variante daher die saubere Endkonfiguration.

Auswirkung: `python manage.py check --deploy` meldet die Warnung `security.W021` nicht mehr.

## Zugriffsbeschränkung

Der aktuelle Show-case unter `schule.plebsapps.de` ist öffentlich über das Internet erreichbar und verarbeitet ausschließlich künstliche Daten. Ein späteres Produktivsystem mit echten Schuldaten wird nur im Schulnetz betrieben; externe Zugriffe erfolgen ausschließlich über VPN.

Begründung: Der öffentliche Show-case soll ohne getrennten Netzzugang nachvollziehbar sein, enthält aber keine echten Schuldaten und erlaubt dem veröffentlichten Demokonto keine Änderungen. Für sensible personenbezogene Schuldaten reduziert die Begrenzung auf Schulnetz und VPN weiterhin das Risiko unnötiger Exposition.

Unabhängig davon bleiben Authentifizierung und serverseitige Berechtigungen erforderlich.

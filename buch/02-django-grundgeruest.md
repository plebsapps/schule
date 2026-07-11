# Kapitel 2: Vom Plan zum technischen Grundgerüst

## Ausgangslage und Ziel

Nach der Planungsphase sollte die Anwendung auf demselben Server wie mehrere bestehende Dienste vorbereitet werden. Die Domain `schule.plebsapps.de` war bereits im DNS eingetragen. Vor Änderungen wurden deshalb DNS-Ziel, belegte Ports, bestehende Container und die grundsätzliche Nginx-Situation ausschließlich lesend geprüft.

Die Prüfung zeigte: Die vorgesehenen internen Ports `8000` bis `8004` waren bereits belegt. Für die Zeugnisverwaltung wurde deshalb `127.0.0.1:8005` gewählt. Die Bindung an die Loopback-Adresse verhindert, dass Django den Reverse Proxy umgeht und direkt öffentlich erreichbar wird.

[Bild004]

## Redaktionell überarbeiteter Prompt

> Das Projekt soll auf diesem Server unter `schule.plebsapps.de` betrieben werden. Der DNS-Eintrag wurde bereits in der Domainverwaltung gesetzt.
>
> Setze die nächsten Schritte in der vorgeschlagenen Reihenfolge um. Der interne Port `8005` ist dafür geeignet.

## Verwendete Codex-Arbeitsweise

1. Projektregeln und Plan berücksichtigen.
2. Git-Status prüfen und einen Feature-Branch erstellen.
3. Bestehende Serverressourcen nur lesend untersuchen.
4. Risiken und Auswirkungen vor der Umsetzung benennen.
5. Abhängigkeiten und Supportzeiträume aus Primärquellen prüfen.
6. Grundgerüst in kleinen, nachvollziehbaren Dateien erstellen.
7. Migrationen, Tests, Linting und Containerstart prüfen.
8. Dokumentation und Lehrbuch parallel aktualisieren.

## Wichtige Entscheidungen

### Django 5.2 LTS

Die LTS-Reihe wurde einer kurzlebigeren Funktionsversion vorgezogen. Für eine Anwendung mit sensiblen Schuldaten ist ein längerer Zeitraum für Sicherheitsupdates wichtiger als die neuesten Framework-Funktionen.

### Eigenes Benutzer-Modell von Anfang an

Ein Wechsel des Django-Benutzer-Modells nach den ersten Migrationen ist aufwendig und riskant. Daher wurde bereits im Grundgerüst ein schlankes projektspezifisches Modell angelegt, obwohl fachliche Rollen erst später folgen.

### Keine Standardpasswörter

Der Stack erstellt weder Datenbank- noch Administrationspasswörter automatisch. Lokale Secrets müssen außerhalb von Git in `.env` gesetzt werden. Ein Administratorkonto wird ausdrücklich und interaktiv angelegt.

### Getrennter Nginx-Schritt

Das Grundgerüst verändert keine vorhandene Nginx- oder Zertifikatskonfiguration. Erst wenn Django, PostgreSQL, Migrationen und Healthchecks funktionieren, wird der öffentliche HTTPS-Zugriff separat vorbereitet und geprüft.

[Bild005]

## Sicherheits- und Datenschutzüberlegungen

- PostgreSQL besitzt keine veröffentlichte Host-Portfreigabe.
- Django bindet nur an `127.0.0.1:8005`.
- Der Webcontainer läuft als nicht privilegierter Benutzer.
- Sichere Cookie-, HTTPS- und Header-Einstellungen sind konfigurierbar.
- Wiederholte fehlgeschlagene Anmeldungen führen zu einer zeitweiligen Sperre.
- Tests enthalten ausschließlich künstliche Benutzerdaten.
- Logs sollen keine Passwörter oder unnötigen personenbezogenen Daten enthalten.

## Erkenntnis für zukünftige Codex-Nutzung

Ein DNS-Eintrag allein macht noch kein Deployment. Codex sollte zuerst prüfen, ob überhaupt eine startbare Anwendung vorhanden ist, welche lokalen Ports bereits belegt sind und wo die Grenze zwischen Repository-Arbeit und freizugebender Serveränderung liegt.

## Blocker beim ersten Containerstart

Der erste reale Start deckte einen Dateirechtefehler auf: Der Webcontainer lief wie vorgesehen ohne Rootrechte, aber das Arbeitsverzeichnis war noch Eigentum von Root. Deshalb konnte Django das Verzeichnis `staticfiles` bei `collectstatic` nicht anlegen und der Container startete wiederholt neu.

Die Korrektur bestand nicht darin, den Container wieder als Root auszuführen. Stattdessen werden ausschließlich die benötigten Anwendungsverzeichnisse beim Image-Build angelegt und dem nicht privilegierten Benutzer zugeordnet. Dieser Fehler zeigt, warum ein erfolgreicher Image-Build den tatsächlichen Containerstart mit Healthcheck nicht ersetzt.

[Bild006]

## Bewusste offene Sicherheitsentscheidung

Djangos Deployment-Prüfung meldete HSTS-Preload als nicht aktiviert. Diese Warnung wurde bewusst nicht durch unüberlegtes Aktivieren oder Ausblenden beseitigt. Die Aufnahme in Browser-Preload-Listen ist langfristig und setzt einen dauerhaft zuverlässigen HTTPS-Betrieb voraus. Der offene Punkt wurde deshalb für die spätere Nginx-/HTTPS-Phase dokumentiert.

## Vorbereitung von Nginx und HTTPS

Das bereits vorhandene Let's-Encrypt-Zertifikat für `plebsapps.de` wurde über den öffentlich ausgelieferten Zertifikatsinhalt geprüft. Es enthielt `pdb.plebsapps.de`, `plebsapps.de` und `www.plebsapps.de`, aber nicht `schule.plebsapps.de`. Für die neue Anwendung ist deshalb ein eigenes Zertifikat erforderlich.

Da Administratorrechte auf dem Server ein interaktives sudo-Passwort verlangen, wurden keine Zugangsdaten im Chat oder in Befehlsausgaben übertragen. Stattdessen entstanden zwei versionierte Nginx-Vorlagen:

1. eine reine HTTP-Bootstrap-Site für die Certbot-Prüfung
2. eine endgültige HTTPS-Site mit Weiterleitung und sicheren Proxy-Headern

Die privilegierten Installationsschritte wurden als manuelle Betriebsanleitung dokumentiert. Dieses Vorgehen hält den Quellcode nachvollziehbar und vermeidet das riskante Umgehen der Serverberechtigungen.

Beim Umschalten von Django auf den Produktionsmodus zeigte der Container-Healthcheck zunächst einen Fehler: `ALLOWED_HOSTS` erlaubte korrekt nur die Produktivdomain, der interne Check sendete aber `127.0.0.1` als Host. Statt die Sicherheitsregel durch eine zusätzliche Hostfreigabe abzuschwächen, wurde der Healthcheck so angepasst, dass er den echten Produktivhost und das erwartete HTTPS-Proxyprotokoll mitsendet.

## Erfolgreiche HTTPS-Inbetriebnahme

Nach dem Merge der geprüften Vorlagen führte der Serveradministrator die privilegierten Schritte direkt im Serverterminal aus. Danach wurden unabhängig geprüft:

- dauerhafte Weiterleitung von HTTP auf HTTPS
- gültiges Let's-Encrypt-Zertifikat ausschließlich für `schule.plebsapps.de`
- Weiterleitung nicht angemeldeter Benutzer zur Anmeldeseite
- HSTS, Frame-Schutz, MIME-Sniffing-Schutz und Referrer-Policy
- erfolgreicher öffentlicher Healthcheck
- gesunder Zustand beider Projektcontainer
- aktivierter Certbot-Timer

Es wurde kein Standardbenutzer mit veröffentlichtem Passwort angelegt. Der erste Administrator wird interaktiv im Container erstellt, damit das Passwort weder im Repository noch in Chat- oder Befehlsprotokollen erscheint.

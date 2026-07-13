# Deployment auf `schule.plebsapps.de`

## Aktueller Betriebsstand

Das erste Deployment wurde am 10. Juli 2026 erfolgreich abgeschlossen:

- HTTP leitet auf HTTPS um.
- Let's Encrypt liefert ein Zertifikat für `schule.plebsapps.de` aus.
- Django läuft mit deaktiviertem Debug-Modus und sicheren Cookies.
- HSTS ist für ein Jahr mit `includeSubDomains` aktiv.
- Nginx leitet ausschließlich an `127.0.0.1:8005` weiter.
- PostgreSQL besitzt keinen veröffentlichten Host-Port.
- `schule-web` und `schule-db` sind gesund.
- der Certbot-Timer ist aktiviert.

Ein separater `certbot renew --dry-run` benötigt Administratorrechte und bleibt als regelmäßige Betriebsprüfung erforderlich.

## Voraussetzungen

- DNS-A-Record zeigt auf den vorgesehenen Server.
- `schule-web` und `schule-db` sind gesund.
- Django ist ausschließlich unter `127.0.0.1:8005` erreichbar.
- Nginx und Certbot sind installiert.
- Port 80 und 443 werden durch Nginx bedient.
- Es liegt ein aktuelles Backup der vorhandenen Nginx-Konfiguration vor.

Die folgenden Serverbefehle benötigen Administratorrechte und müssen manuell auf dem Server ausgeführt werden. Vorhandene Site-Dateien dürfen nicht ersetzt werden.

## 0. Docker-Compose-Autostart aktivieren

Damit die Anwendung nach einem Serverneustart wieder hochkommt, wird ein systemd-Dienst für den Compose-Stack installiert. Die Container selbst besitzen zusätzlich `restart: unless-stopped`, damit sie nach einem Docker-Neustart ebenfalls wieder starten.

Die Datei `deploy/systemd/schule-compose.service.example` ist eine Vorlage und verändert den Server nicht automatisch. Vor der Installation muss `__PROJECT_DIR__` durch den absoluten Repository-Pfad ersetzt werden.

Dann auf dem Zielserver:

```bash
sudo install -o root -g root -m 0644 \
  deploy/systemd/schule-compose.service.example \
  /etc/systemd/system/schule-compose.service

sudo systemctl daemon-reload
sudo systemctl enable --now schule-compose.service
sudo systemctl status schule-compose.service
```

Falls Docker selbst noch nicht beim Booten aktiviert ist, muss das parallel ergänzt werden. Der Dienst benötigt keine manuelle Reaktivierung nach jedem Neustart, solange der Host die systemd-Einheit lädt.

## 1. Bootstrap-Site installieren

```bash
sudo install -o root -g root -m 0644 \
  nginx/schule.plebsapps.de.bootstrap.conf \
  /etc/nginx/sites-available/schule.plebsapps.de

sudo ln -s \
  /etc/nginx/sites-available/schule.plebsapps.de \
  /etc/nginx/sites-enabled/schule.plebsapps.de

sudo nginx -t
sudo systemctl reload nginx
```

Falls der Link bereits existiert, nicht blind überschreiben. Zuerst Ziel und Inhalt prüfen.

HTTP-Prüfung:

```bash
curl -I http://schule.plebsapps.de/anmelden/
```

## 2. Zertifikat ausstellen

```bash
sudo certbot --nginx -d schule.plebsapps.de --redirect
```

Certbot darf nur fortgesetzt werden, wenn es ausschließlich die neue Site `schule.plebsapps.de` ändern will.

## 3. Endgültige Site-Konfiguration angleichen

Die von Certbot erzeugte Konfiguration mit `nginx/schule.plebsapps.de.conf.example` vergleichen. Zertifikatspfade müssen auf `/etc/letsencrypt/live/schule.plebsapps.de/` zeigen. Danach:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

## 4. Django auf Produktionsmodus umstellen

In der lokalen, nicht versionierten `.env`:

```dotenv
DJANGO_DEBUG=false
DJANGO_ALLOWED_HOSTS=schule.plebsapps.de
DJANGO_CSRF_TRUSTED_ORIGINS=https://schule.plebsapps.de
DJANGO_SECURE_COOKIES=true
DJANGO_SECURE_SSL_REDIRECT=true
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=true
DJANGO_SECURE_HSTS_PRELOAD=false
```

Anschließend nur den Webdienst neu erstellen:

```bash
docker compose up -d --no-deps --force-recreate web
docker compose ps
```

## 5. Abnahme

```bash
curl -I http://schule.plebsapps.de/
curl -I https://schule.plebsapps.de/
curl --fail https://schule.plebsapps.de/health/
sudo certbot renew --dry-run
```

Erwartet werden:

- HTTP leitet dauerhaft auf HTTPS um.
- HTTPS verwendet ein gültiges Zertifikat für `schule.plebsapps.de`.
- `/` leitet nicht angemeldete Benutzer auf `/anmelden/` um.
- `/health/` liefert `{"status": "ok"}`.
- sichere Cookies und Sicherheitsheader sind aktiv.
- beide Docker-Container bleiben gesund.

## Rücknahme

Wenn der neue Host Nginx beeinträchtigt:

```bash
sudo rm /etc/nginx/sites-enabled/schule.plebsapps.de
sudo nginx -t
sudo systemctl reload nginx
```

Die Datei unter `sites-available` und Zertifikate nicht ungeprüft löschen. Ein fehlgeschlagenes `nginx -t` darf niemals durch einen Reload übergangen werden.

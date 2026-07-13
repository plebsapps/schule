# Kapitel 10: Show-case-Abschluss, Systemstart und Lesekonto

::: {.demo-access}
**Öffentlicher Demo-Zugang – ausschließlich künstliche Daten**

- **URL:** [https://schule.plebsapps.de](https://schule.plebsapps.de)
- **Benutzer:** `Buch`
- **Passwort:** `BuchPW$1`

Das Konto besitzt ausschließlich Leserechte. Es kann keine Daten anlegen,
ändern oder löschen und das eigene Passwort nicht ändern.
:::

## Prompt

> Schließe den Show-case sauber ab. Der Docker-Compose-Stack soll nach einem Serverneustart automatisch wieder starten, und das Praxisbeispiel benötigt zusätzlich ein separates Lesekonto mit reinen Lese-Rechten. Alle dafür relevanten Arbeitsschritte sollen nachvollziehbar dokumentiert werden. Sensible Zugangsdaten werden nicht im Buch als Klartext gespeichert.

## Ein Betriebsdetail, das im Show-case den Unterschied macht

Für eine kleine Demo ist es leicht, den laufenden Zustand mit dem eigentlichen Projektstand zu verwechseln. Deshalb wurde die Anwendung so ergänzt, dass der Docker-Compose-Stack nach einem Neustart des Servers automatisch wieder startet. Die Container selbst sind zusätzlich auf ein robustes Restart-Verhalten ausgelegt.

Das ist kein Ausbau zu einer Dauerbaustelle, sondern eine klare Betriebsgrenze. Der Show-case bleibt klein, aber er ist nach einem Neustart nicht einfach „weg“, nur weil der Server neu gebootet wurde.

## Ein Lesekonto ohne Schreibrecht

Zum Buch gehört ein separates Konto mit dem Namen `Buch`. Dieses Konto ist für die Einsicht in die dokumentierten Verwaltungsdaten gedacht, nicht für die Bearbeitung.

Die Berechtigung ist bewusst eng gefasst:

- lesen erlaubt
- schreiben nicht erlaubt
- ändern nicht erlaubt
- administrative Funktionen nicht erlaubt

Damit kann das Buch im Alltag nachvollzogen werden, ohne dass das Lesekonto selbst zu einem weiteren Bearbeitungspfad wird.

Das veröffentlichte Passwort ist ausschließlich für diesen öffentlichen
Show-case vorgesehen und wird bewusst nicht als Secret behandelt. Es darf
niemals für ein anderes Konto oder ein System mit echten Daten wiederverwendet
werden.

Das Lesekonto darf sein Passwort außerdem nicht selbst über die
Django-Administration ändern. Die Passwortänderung ist serverseitig gesperrt
und der entsprechende Link wird für das Konto ausgeblendet. Eine notwendige
Rotation führt ausschließlich eine administrierende Person über den dafür
vorgesehenen Management-Befehl durch. So kann das gemeinsam genutzte
Demonstrationskonto nicht unbemerkt durch eine lesende Person übernommen werden.

## Zugang, Netzwerkgrenze und Passwortübermittlung

Die Demonstration ist öffentlich über das Internet erreichbar und enthält
ausschließlich künstliche Show-case-Daten. URL, Benutzername und Passwort sind
deshalb direkt im Zugangskasten am Kapitelanfang angegeben.

Diese Freigabe gilt nicht für ein echtes schulisches Produktivsystem. Sobald
reale Schülerdaten verarbeitet werden, gehören Anwendung und individuelle
Konten in eine kontrollierte Umgebung; ein Zugriff von zu Hause erfolgt dann
ausschließlich über eine von der Schule bereitgestellte VPN-Verbindung.

Vor der Buchfreigabe wurden der aktive Kontostatus, ein verwendbarer
Passwort-Hash, die Mitgliedschaft in der Read-only-Gruppe, die ausschließlich
lesenden Modellrechte und die serverseitige Sperre schreibender Aufrufe erneut
geprüft.

## Repository und veröffentlichte Prüffassung

Der Quellstand ist öffentlich unter
[https://github.com/plebsapps/schule](https://github.com/plebsapps/schule)
nachvollziehbar. Das Repository enthält Quellcode, Buchmanuskript, künstliche
Testdaten und technische Dokumentation. Echte Schülerdaten, produktive
Zugangsdaten, Secrets, Backups und echte Zeugnisse dürfen dort nicht abgelegt
werden. Das ausdrücklich öffentliche Demo-Kennwort ist die eng begrenzte
Ausnahme und darf nicht für andere Systeme verwendet werden.

Die GPLv3 erlaubt die Nutzung, Prüfung, Änderung und Weitergabe unter ihren
Lizenzbedingungen. Issues dokumentieren Fehler oder Vorschläge; Pull Requests
machen Änderungen prüfbar; Releases ordnen veröffentlichte Artefakte einem
bestimmten Projektstand zu.

Davon zu unterscheiden ist die veröffentlichte EPUB-Prüffassung. Sie wird
außerhalb des Buchtexts bereitgestellt, während das GitHub-Repository die
Quellen und Entwicklungsgeschichte enthält.

## Was in dieser Phase dokumentiert wurde

Die neueste Arbeitsphase hatte drei gleichwertige Ziele:

1. die Laufzeit nach Neustarts stabilisieren
2. die offene Restarbeit sichtbar abschließen
3. den Lesezugang für das Praxisbeispiel sauber von der Schreibarbeit trennen

Damit ist die technische Grundlage für den Show-case festgehalten, ohne neue offene Feature-Pfade zu eröffnen.

## Abschluss

Der Show-case ist damit nicht nur fachlich beschrieben, sondern auch betrieblich eingeordnet. Das Projekt bleibt nachvollziehbar, wiederholbar und bewusst begrenzt.

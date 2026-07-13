# Vorwort

Dieses Buch zeigt die praktische Zusammenarbeit mit OpenAI Codex am Beispiel
einer schulischen Zeugnisverwaltung. Im Mittelpunkt steht nicht eine erfundene
Musteraufgabe, sondern ein tatsächlich entwickelter Show-case: von den ersten
Projektregeln über Git-Branches, Django und Docker bis zu Tests,
Datenschutzentscheidungen, Veröffentlichung und Dokumentation.

Der Anspruch ist dabei bewusst praktisch. Die folgenden Kapitel zeigen, wie
aus Arbeitsaufträgen überprüfbare Änderungen entstehen, warum Codex zuerst den
vorhandenen Projektstand lesen muss und wie Fehler, Rückfragen und
Korrekturschleifen zu einem nachvollziehbaren Ergebnis führen.

## Die wichtigsten Grundlagen in Kürze

Codex arbeitet nicht losgelöst vom Projekt. Gute Ergebnisse entstehen aus dem
Zusammenspiel mehrerer Bestandteile:

- Ein **Prompt** beschreibt Ziel, Umfang und gewünschtes Ergebnis einer
  Aufgabe.
- Der **Kontext** besteht aus vorhandenen Dateien, bisherigen Entscheidungen,
  Fehlermeldungen und den Regeln des Repositorys.
- Eine `AGENTS.md` legt verbindlich fest, wie Codex in einem Projekt arbeiten
  soll.
- Eine `PLAN.md` beschreibt Zielbild, Architektur, Grenzen und den aktuellen
  Projektstand.
- **Git** hält Änderungen nachvollziehbar. Fachlich zusammenhängende Arbeiten
  erfolgen auf eigenen Branches und werden vor der Übernahme geprüft.
- **Tests** liefern einen wiederholbaren Nachweis, dass die gewünschte Funktion
  arbeitet und bestehendes Verhalten nicht unbeabsichtigt beschädigt wurde.
- **Docker Compose** bündelt Anwendung und Datenbank zu einer reproduzierbaren
  Laufzeitumgebung.

Codex ersetzt dabei weder fachliche Entscheidungen noch Verantwortung. Das
Modell kann Dateien analysieren, Änderungen vorbereiten, Befehle ausführen und
Prüfungen auswerten. Ob eine Anforderung fachlich richtig, datenschutzrechtlich
zulässig und für einen produktiven Betrieb ausreichend ist, muss weiterhin von
den verantwortlichen Menschen entschieden werden.

## Was dieses Buch nicht vermittelt

Dieses Buch ist keine allgemeine Einführung in Linux, PuTTY, SSH, Webserver,
DNS, Git, Docker, Django oder die grundlegende Bedienung von Codex. Diese Themen
werden dort erklärt, wo sie für den Projektverlauf wichtig sind. Eine
vollständige Schulung jedes einzelnen Werkzeugs würde jedoch vom eigentlichen
Praxisbeispiel wegführen.

Hilfreich sind deshalb grundlegende Erfahrungen mit:

- Dateien und Verzeichnissen,
- einfachen Terminalbefehlen,
- einem SSH-Zugang zu einem Server,
- Git und GitHub,
- Webanwendungen und Domains sowie
- dem Lesen kurzer Konfigurations- und Fehlermeldungen.

PuTTY ist dabei nur eine mögliche Anwendung für eine SSH-Verbindung. Wer ein
anderes Terminal oder einen integrierten SSH-Client verwendet, kann die
gezeigten Prinzipien ebenso nachvollziehen. Gleiches gilt für die übrigen
Werkzeuge: Entscheidend ist das Verständnis des Ablaufs, nicht ein bestimmtes
Programmfenster.

## Fehlendes Wissen darf nachgearbeitet werden

Die genannten Voraussetzungen sollen niemanden vom Weiterlesen abhalten. Mit
etwas Fleiß lassen sich fehlende Grundlagen über offizielle Dokumentationen,
gezielte Internetsuchen, Fachforen oder eine KI-Assistenz schnell erschließen.
Oft genügt es, einen unbekannten Begriff, einen Befehl oder eine Fehlermeldung
genau zu untersuchen, bevor der nächste Projektschritt ausgeführt wird.

Bei Fragen an eine KI helfen konkrete Angaben: Welches Betriebssystem wird
verwendet? Welcher Befehl wurde ausgeführt? Welche Meldung erschien? Was sollte
stattdessen geschehen? Geheimnisse und personenbezogene Daten gehören dabei
niemals in die Anfrage.

KI-Antworten sind Vorschläge, keine automatische Freigabe. Insbesondere
Shellbefehle mit `sudo`, Änderungen an Firewall, DNS, Webserver oder
Dateirechten sowie Datenbankoperationen müssen vor der Ausführung verstanden
und auf ihre Auswirkungen geprüft werden. Im Zweifel ist ein lesender
Prüfschritt sicherer als eine vorschnelle Änderung.

## Wie dieses Praxisbeispiel gelesen werden kann

Die Kapitel folgen im Wesentlichen der tatsächlichen Projektentwicklung. Wer
den Gesamtprozess verstehen möchte, liest sie der Reihe nach. Wer bereits mit
der Technik vertraut ist, kann gezielt zu Themen wie Codex-Arbeitsweise,
Git-Workflow, Datenschutz, Backups, Stammdaten oder EPUB-Erzeugung springen.

Das öffentliche Repository ermöglicht es, die beschriebenen Entscheidungen an
den Quellen nachzuvollziehen. Für das Verständnis ist es jedoch nicht nötig,
jeden Befehl sofort selbst auszuführen. Wichtiger ist die wiederkehrende
Arbeitsweise: zuerst lesen und Risiken erkennen, dann klein und kontrolliert
ändern, anschließend testen, dokumentieren und erst danach veröffentlichen.

Dieses Buch verspricht deshalb keine Abkürzung ohne Lernaufwand. Es soll zeigen,
dass ein reales Projekt auch mit unterschiedlichen Vorkenntnissen bewältigt
werden kann, wenn Anforderungen klar formuliert, Entscheidungen sichtbar
gemacht und technische Ergebnisse konsequent geprüft werden.

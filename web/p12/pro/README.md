# Master-Readme
Stand: 29.10.2018 | Version: **1.1.1**

---

## Table of Contents
Element | Abschnitt
--------|----------
*Übersicht* | [--> Klick mich <--](#overview)
*Routing* | [--> Klick mich <--](#routing)
*Python-Applikation (Ordner /app/)* | [--> Klick mich <--](#python-app)
*JSON-Dateien (Ordner /data/)* | [--> Klick mich <--](#json-data)
*Mako-Templates (Ordner /template/)* | [--> Klick mich <--](#template-files)
*Statische HTML/CSS/JS (Ordner /content/)* | [--> Klick mich <--](#static-files)

---

<a name="overview"></a>
## Übersicht
...

---

<a name="routing"></a>
## Routing
Das Routing wird in der [Python-Server-Klasse](server.py) realisiert.
Die Datei beinhaltet ausserdem die Server-Konfiguration für die jeweilige Aufgabe.

### Webseiten
1. __.../__
    * Die Landing-Page des Servers, keine Anforderung an das Programm, nur zur Navigation.
2. __.../auswertung__
    * Die Seite mit der Projektauswertung, Anforderung an das Programm.
3. __.../projektdaten/...__
    * __.../projektdaten/__
        - Seite mit Tabelle mit allen bestehenden Projekten
    * __.../projektdaten/neu__
        - Seite um neues Projekt anzulegen
    * __.../projektdaten/<projekt_id>__
        - Seite um Projekt mit angegebener Id zu bearbeiten
4. __.../kundendaten/...__
    * __.../kundendaten/__
        - Seite mit Tabelle mit allen bestehenden Kunden
    * __.../kundendaten/neu__
        - Seite um neuen Kunden anzulegen
    * __.../kundendaten/<kunden_id>__
        - Seite um Kunden mit angegebener Id zu bearbeiten
5. __.../mitarbeiterdaten/...__
    * __.../mitarbeiterdaten/__
        - Seite mit Tabelle mit allen bestenden Mitarbeitern
    * __.../mitarbeiterdaten/neu__
        - Seite um neuen Mitarbeiter anzulegen
    * __.../mitarbeiterdaten/<mitarbeiter_id>__
        - Seite um Mitarbeiter mit angegebener Id zu bearbeiten
6. __.../api/<function\>__
    * __.../api/get__
        - TYP: POST
        - Gibt bestimmte angeforderte JSON-Informationen zurück
    * __.../api/add__ (*fehlt noch*)
        - TYP: POST
        - Fügt zu bestimmter JSON-Datei neues ebenfalls angegebenes Element hinzu, Id wird vom Programm vergeben
    * __.../api/update__ (*fehlt noch*)
        - TYP: POST
        - Updatet bestimmte JSON-Datei mit verändertem ebenfalls angegebenem Element
    * __.../api/delete__ (*fehlt noch*)
        - TYP: POST
        - Löscht in bestimmter JSON-Datei ebenfalls angegebenes Element, wenn es nicht in Benutzung ist

---

<a name="python-app"></a>
## Python-Applikation
Für mehr Informationen siehe [README.md](/app/README.md)

---

<a name="json-data"></a>
## JSON-Dateien
Für mehr Informationen siehe [README.md](/data/README.md)

---

<a name="template-files"></a>
## Mako-Templates
Für mehr Informationen siehe [README.md](/template/README.md)

---

<a name="static-files"></a>
## Statische HTML/CSS/JS
Für mehr Informationen siehe [README.md](/content/README.md)

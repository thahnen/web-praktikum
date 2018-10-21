# Praktikum: Web-Engineering

**Vorlesung: Web-Engineering (3. Semester)**

Das Praktikumsprojekt bestehend aus zwei Aufgaben für 3 Praktikumstermine.
Der Inhalt ist ein "Projektinformationssystem", alle Feinheiten siehe Technik usw.

- [ ] **Es muss noch alle READMEs gemacht werden**

## ~~Team~~-Member:
1. Tobias Hahnen (1218710)
2. ???

## Technik
1. Server:
  * Python 3.7+
  * CherryPy - Framework
  * Moko - Templateengine
2. Client:
  * HTML5
  * CSS3
  * JavaScript

## Informationen
1. Ordner "Documentation":
  * Vorversion der Dokumentation, Abgabebereit liegt in web/p1/pro/doc
2. Ordner "web/p1/pro":
  * Beinhaltet den Webserver **server.py**
  * Beinhaltet alle anderen Ordner
3. Ordner "web/p1/pro/app":
  * Beinhaltet **\_\_init\_\_.py**, **application.py**, **database.py**, **view.py**
  * Also quasi die serverseitige Logik
4. Ordner "web/p1/pro/content":
  * Beinhaltet alle **HTML-**, **CSS-** und **JS-Dateien**
  * Also quasi alles was clientseitig ankommt
5. Ordner "web/p1/pro/data":
  * Alle Daten des Webprojekts im JSON-Format
  * Also quasi alles was serverseitig verarbeitet und clientseitig serviert wird
6. Ordner "web/pi/pro/doc":
  * Abgabefertige Dateien der Dokumentation
7. Ordner "web/pi/pro/template":
  * Template-Vorlagen für Mako

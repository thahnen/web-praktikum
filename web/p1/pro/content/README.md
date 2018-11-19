# Content-Ordner
Stand: 29.10.2018 | Version: **1.0.0**

---

## Table of Contents
Element | Abschnitt
--------|----------
*Übersicht* | [--> Klick mich <--](#overview)
*HTML-Datien* | [--> Klick mich <--](#html)
*JavaScript-Dateien* | [--> Klick mich <--](#javascript)
*CSS-Dateien* | [--> Klick mich <--](#css)

---

<a name="overview"></a>
## Übersicht
Dieser Ordner und seine Unterordner beinhaltet alle statischen HTML-Seiten sowie:
* JavaScript-Logik für die generierten Webseiten
* CSS-Makeup-Regeln für die generierten Webseiten

---

<a name="html"></a>
## HTML-Dateien
### Statische Seiten
1. [index.html](index.html)
Die Landing-Page des Webservers zur Navigation zwischen Aufgabe 1 und 2
2. [404.html](404.html)
Eine Custom 404-Seite, aus einem meiner Projekte genommen als Lückenfüller
3. [500.html](500.html)
Eine Custom 500-Seite, aus einem meiner Projekte genommen als Lückenfüller

### Meta-Informationen
1. __<html lang="de" x-ms-format-detection="none"\>__
2. __<meta name="format-detection" content="telephone=no" /\>__
    * Telefonnummern nicht aus Versehen anklickbar
    * Inforamtion im HTML-Tag für MS Edge / MS Internet Explorer
3. __<meta charset="utf-8" /\>__
    * Setz die Kodierung der Seite auf UTF-8
4. __<meta name="robots" content="noindex,nofollow" /\>__
    * Verhindert Indexierung des Webservers
5. __<meta http-equiv="expires" content="0" /\>__
    * Nichts wird gecacht, sondern jedes mal neugeladen
    * Kann ggf. später weg!
6. __<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" /\>__
    * Seite skalierbar auch für mobile Endgeräte

---

<a name="javascript"></a>
## JavaScript-Dateien
Siehe: [Unterordner js für JavaScript](/js)
1. [view.js](/js/view.js)
Logik für die Übersichtsseite jedes Datenbestandes
2. [new.js](/js/new.js)
Logik für die Neu-Hinzufügen-Seite jedes Datenbestandes
3. [edit.js](/js/edit.js)
Logik für die Editieren-Seite jedes Datenbestandes

---

<a name="css"></a>
## CSS-Dateien
Namensgebung erfolgt nach der ["Block Element Modifier"-Methode](getbem.com/introduction/)
Siehe: [Unterordner css für CSS](/css)
1. [view.css](/css/view.css)
CSS-Regeln für die Übersichtsseite jedes Datenbestandes
2. [new.css](/css/new.css)
CSS-Regeln für die Neu-Hinzufügen-Seite jedes Datenbestandes
3. [edit.css](/js/edit.css)
CSS-Regeln für die Editieren-Seite jedes Datenbestandes

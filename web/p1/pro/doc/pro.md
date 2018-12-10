# <span style="color:#667db6">Projektinformationssystem (Praktikum 1 & 2)</span>

## <span style="color:#667db6">Inhaltsverzeichnis</span>
Element | Abschnitt
--------|----------
*Einleitung* | [--> Klick mich <--](#einleitung)
*Projektbeschreibung* | [--> Klick mich <--](#projektbeschreibung)
*Beschreibung der Komponenten des Servers* | [--> Klick mich <--](#beschreibung)
*Datenablage* | [--> Klick mich <--](#datenablage)
*Durchführung und Ergebnisse der geforderten Prüfungen* | [--> Klick mich <--](#ergebnisse)

---

<a name="einleitung"></a>
## <span style="color:#667db6">Einleitung</span>
Praktikumsgruppe: F

Gruppenmitglieder: **Tobias Hahnen (1218710)**

Stand: *08.12.2018* | Version: *1.2.3*

---

<a name="projektbeschreibung"></a>
## <span style="color:#667db6">Projektbeschreibung</span>

### Aufgabe der Anwendung
Projektinformationssystem: Ermöglicht das Management von Projekten, den jeweiligen Kunden und den beteiligten Mitarbeitern.

### Übersicht der fachlichen Funktionen
Das Projektinformationssystem ist als Web-Anwendung realisiert.
Es besteht die Möglichkeit, die jeweiligen

1. Projektdaten
2. Kundendaten
3. Mitarbeiterdaten

zu **bearbeiten**.
Ausserdem kann man Daten **löschen**.
Des weiteren kann man pro Datensatz je neue Daten **hinzufügen**.

Dabei wird auf die Integrität der jeweiligen Daten, soweit möglich, geachtet.

Für jede Möglichkeit der Bearbeitung gibt es entweder eine eigene Seite oder aber einige sind miteinander implementiert.

---

<a name="beschreibung"></a>
## <span style="color:#667db6">Beschreibung der Komponenten des Servers</span>

### DISCLAIMER:
Um die Übersichtlichkeit zu verbessern wurde das Projekt unterteilt für die:
- erste Teilaufgabe (siehe Ordner **web/p11/**)
- zweite Teilaufgabe (siehe Ordner **web/p12/**)

Damit gewährleistet ist, dass, bis auf wenige Ausnahmen, alle Dateien gleich sind, kann das Skript **assert-integrity.sh** ausgeführt werden. Es zeigt alle (relevanten) Dateien an, die für beide Teilaufgaben existieren!

Dieses Skript liegt im Ordner **web/test** zusammen mit anderen Skripten, auf die an der jeweiligen Stelle eingegangen wird!

### server.py

#### Zweck

#### Aufbau (Bestandteile der Komponente)

#### Zusammenwirken mit anderen Komponenten

#### API (Programmierschnittstellen), die die Leistungen der Komponente anbieten

### ...

---

<a name="datenablage"></a>
## <span style="color:#667db6">Datenablage</span>
Abgespeichert werden die Projekte mit ihren Kunden und Mitarbeitern in unterschiedlichen JSON-Dateien.

---

<a name="ergebnisse"></a>
## <span style="color:#667db6">Durchführung und Ergebnis der geforderten Prüfungen</span>






---


## <span style="color:#667db6">Projektbeschreibung</span>

Das Ziel dieses Projektes, ist es, eine Web-Anwendung zu entwerfen und entwickeln, mit der ein Unternehmen, relevante Informationen zu kundenspezifischen Projekten verwalten kann.

Dazu gehören verschiedene Gruppierungen:
1. Projektdaten
2. Kundendaten
3. Mitarbeiterdaten

Alle diese Daten soll man hinzufügen, ändern und löschen können. Zudem soll es noch eine Ansicht geben, welche die detailierten Projektdaten darstellt.

----

## <span style="color:#667db6">Fachliche Funktionen</span>

Damit der User sich durch die Anwendung navigieren kann, wurde eine Leiste erstellt, welche zu den generellen Ansichten der 3 Gruppierungen führt. Auf der Startseite hat man die Möglichkeit, die Auswertung aufzurufen.

Die generellen Ansichten sind alle gleich aufgebaut. Auf jeder Seite hat der Benutzer die Möglichkeit über den Button "Hinzufügen" ein neues Element zur Liste hinzuzufügen. Hat der Benutzer sich dafür entschieden, gelangt er auf eine neue Seite wo er die Daten des jeweiligen Elements eintragen muss.

In der generellen Ansicht kann der Benutzer jedoch auch bestehende Datensätze anpassen oder löschen. Dafür wählt der Benutzer das Element aus und klickt auf "Detail" um es zu bearbeiten oder "Löschen" um es zu löschen.

Wenn der Benutzer auf "Detail" klickt während er ein Element ausgewählt hat, gelangt er auf die Detailseite. Hier hat er die Möglichkeit, einzelne Felder zu bearbeiten. Um die Daten zu speichern wählt der Benutzer den Button "Speichern" aus.

Hierbei unterscheidet sich die Projektdetailseite leicht von den anderen Detailseiten. Bei der Projektdetailseite, kann man noch die Stunden für die jeweiligen Mitarbeiter buchen, die an dem Projekt beteiligt sind. Hat man die Kalenderwoche und die Arbeitsstunden eingetragen, klickt der Benutzer auf "Buchen" und die Stunden werden dem Mitarbeiter zugeordnet. Dabei gilt, dass nur die Stunden die der Mitarbeiter an genau diesem Projekt gearbeitet hat, eingetragen werden.

Falls man Daten falsch eingetragen hat, oder ein Mitarbeiter das Projekt verlässt, hat man die Möglichkeit unter "Detail" die Arbeitszeiten anzupassen oder unter "Löschen" die Möglichkeit den Mitarbeiter vom Projekt zu entfernen.

Zuletzt kann der Benutzer noch ganz unten Mitarbeiter zum Projekt hinzufügen. Hierbei gilt natürlich auch, dass nur Mitarbeiter hinzugefügt werden können, die noch nicht an dem Projekt beteiligt sind.

----

## <span style="color:#667db6">Komponenten</span>
Generell besteht die Anwendung aus 4 großen Python-Dateien. Jede Dieser Dateien wird nun kurz erläutert und ihre jeweilige Funktion wird beschrieben.

### Server.py
#### Zweck
Diese Datei nimmt die Anfragen der Benutzer entgegen und verarbeitet sie.
#### Aufbau
Diese Datei besteht aus einzelnen Funktionen die alle ein Verzeichnis der angefragten URL wiederspiegeln.
#### Zusammenwirken mit anderen Komponenten
Es wird hauptsächlich die entsprechende Funktion aus application.py aufgerufen, welche dann die Anfrage intern bearbeitet.

### application.py
#### Zweck
Nimmt die Anfrage von Server.py auf, verarbeitet diese und fragt die geforderten Daten bei der database.py und view.py an.
#### Aufbau
Wie auch schon die Server.py, besteht die application.py aus einzelnen Funktionen die abhängig der Anfrage aufgerufen werden.
#### Zusammenwirken mit anderen Komponenten
Ruft entweder database.py auf um Daten zu bearbeiten oder view.py um eine HTML-Seite zu erstellen.

### database.py
#### Zweck
Löscht, liest oder schreibt Daten in die JSON-Dateien.
#### Aufbau
Je nach Anfrage der application.py, wird eine bestimmte Funktion aufgerufen. Generell gibt es für lesen, schreiben und löschen jeweils eine Funktion. Abhängig vom übergebenen Typen wird dann die jeweilige JSON-Datei ausgewählt.
#### Zusammenwirken mit anderen Komponenten
Wird meist von der application.py verwendet und greift selbst nicht auf andere Komponenten zu.

### view.py
#### Zweck
Soll das Markup mit den übergebenen Daten füllen, erzeugen und zurückgeben.
#### Aufbau
Es gibt eine Funktion für alle detailierten Ansichten. Wie schon bei der database.py zuvor wird auch hier ein typ übergeben und dann jeweils das entsprechende Template erzeugt. Dies gilt auch für die "Neuen"- und "Generellen"-Seiten. Zudem gibt es noch eine Funktion für die Start- und Auswertungsseite. Alle 5 Funktionen greifen auf eine weitere Funktion zu, die dann das Template erstellt.
#### Zusammenwirken mit anderen Komponenten
Wird meist von der application.py verwendet und greift selbst nicht auf andere Komponenten zu.

----

## <span style="color:#667db6">Datenablage</span>
Generell wurden zur Datenablage selbst erstellte JSON-Dateien verwendet, die durch den Server angepasst werden können. Für dieses Projekt wurden 4 JSON Dateien angelegt, welche sich im Unterordner "data" befinden. Jeder Eintrag in den 4 Dateien fängt mit einer ID an, damit man jeden Eintrag eindeutig zuordnen kann. Die 4 Dateien heißen:
1. Projekt

Hierbei handelt es sich um alle generellen Daten die sich auf ein Projekt beziehen.

2. Worker

Diese JSON Datei beinhaltet alle Daten über die Mitarbeiter.

3. Customer

Hier werden alle Kundendaten gespeichert.

4. Project_Worker

Zuletzt werden in dieser Datei alle Mitarbeiter mit den Projekten verknüpft. Dazu kommt noch, dass die Arbeitszeit mit der Kalenderwoche verknüpft und dann in dieser Datei gespeichert wird.

Beispiel (worker.json):

```json
{
 "id": "1",
 "name": "Krause",
 "vorname": "Marvin",
 "funktion": "IT"
}
```

----

## <span style="color:#667db6">Durchführung/Ergebnis der geforderten Prüfungen</span>
Hiermit bestätige ich, dass ich alle Templates geprüft habe. Um das Markup zu prüfen, habe ich folgenden Validator verwendet:
[w3c-Validator-Dienst (Markup)](https://validator.w3.org/)

Hiermit bestätige ich, dass ich alle CSS Dateien geprüft habe. Um die CSS Datei zu prüfen, habe ich den folgenden Validator verwendet:
[w3c-Validator-Dienst (CSS)](http://jigsaw.w3.org/css-validator/)

Alle Templates und CSS Dokumente wurden getestet und als richtig anerkannt. Bei den Templates traten nur vereinzelnt Warnungen auf.

# <span style="color:#667db6">Projektinformationssystem (Praktikum 1 & 2)</span>

---

## <span style="color:#667db6">Einleitung</span>
Praktikumsgruppe: F

Gruppenmitglieder: **Tobias Hahnen (Mat. Nummer: 1218710)**

Stand: *08.12.2018* | Version: *1.2.3*

---

## <span style="color:#667db6">Projektbeschreibung</span>

### Aufgabe der Anwendung
Projektinformationssystem: Ermöglicht das Management von Projekten, den jeweiligen Kunden und den beteiligten Mitarbeitern.

Das Projektinformationssystem ist als Web-Anwendung realisiert.
Es besteht die Möglichkeit, die jeweiligen

1. Projektdaten
2. Kundendaten
3. Mitarbeiterdaten

zu **bearbeiten**.
Ausserdem kann man die Daten **löschen**.
Des weiteren kann man pro Datensatz je neue Daten **hinzufügen**.

Dabei wird auf die Integrität der jeweiligen Daten, soweit möglich, geachtet.

Für jede Möglichkeit der Bearbeitung gibt es entweder eine eigene Seite oder aber es sind einige miteinander implementiert.

### Übersicht der fachlichen Funktionen
Da es sich bei dem Projektinformationssystem um eine Web-Anwendung handelt, sind die einzelnen Funktionen jeweils über eigene Webseiten einsehbar.

#### Die Landing-Page (Adresse: /)
Hauptseite des Web-Servers, **ist nicht von der Aufgabenstellung her gefordert**, aber über sie gerät man direkt zu allen wichtigen (Übersichts-)Seiten.

#### Die Projekt-Übersicht (Adresse: /projektdaten)
Eine Übersicht über alle vorhandenen Projekten mit den jeweils dazugehörigen Informationen in einer übersichtlichen Auflistung.
Von hier aus ist es möglich, ein neues Projekt zu erstellen, ein ausgewähltes Projekt zu bearbeiten oder zu löschen.
Wenn man ein Projekt neu erstellen oder bearbeiten möchte wird man auf die zugehörige Webseite weitergeleitet.

#### Die Projekt-Hinzufügen-Seite (Adresse: /projektdaten/neu)
Hier ist es möglich ein neues Projekt zu erstellen.
Allerdings auf unterschiedliche Art und Weisen, je nachdem ob man das Programm für Aufgabenstellung *1.1* oder *1.2* verwendet.
Ausserdem unterscheidet sich das UI zum Äquivalent für Kunden bzw. Mitarbeiter um etwas mehr Übersichtlichkeit zu gewährleisten.

Bei 1.1 wird der Prozess über zwei aufeinanderfolgende Webseiten realisiert, indem man erst alle Informationen ausser die *Wöchentliche Zuordnung der Arbeit* angibt um dann im zweiten Schritt eben diese auszufüllen.

Bei 1.2 wird der Prozess über eine einzige Webseite realisiert, dabei werden alle Kunden und Mitarbeiter dynamisch geladen um diese dann auszuwählen.
Je nach Eingabe wird dann die *Wöchentliche Zuordnung der Arbeit* dynamisch verändert.

#### Die Projekt-Bearbeiten-Seite (Adresse: /projektdaten/<Projekt-Id>)
Hier ist es möglich ein vorher ausgewähltes Projekt zu bearbeiten.
Allerdings auf unterschiedliche Art und Weisen, je nachdem ob man das Programm für Aufgabenstellung *1.1* oder *1.2* verwendet.
Ausserdem unterscheidet sich das UI zum Äquivalent der Webseite für Kunden bzw. Mitarbeiter um etwas mehr Übersichtlichkeit zu gewährleisten.

Bei 1.1 wird der Prozess über zwei aufeinanderfolgende Webseiten realisiert, indem man erst alle Informationen ausser die *Wöchentliche Zuordnung der Arbeit* bearbeitet um dann im zweiten Schritt eben diese abändert.

Bei 1.2 wird der Prozess über eine einzige Webseite realisiert, dabei werden alle Kunden und Mitarbeiter dynamisch geladen um diese dann zu verändern.
Je nach Eingabe wird dann die *Wöchentliche Zuordnung der Arbeit* dynamisch modifiziert.

#### Die Kunden-Übersicht (Adresse: /kundendaten)
Eine Übersicht über alle vorhandenen Kunden mit den jeweils dazugehörigen Informationen in einer übersichtlichen Auflistung.
Von hier aus ist es möglich, einen neuen Kunden zu erstellen, einen ausgewählten Kunden zu bearbeiten oder zu löschen.
Wenn man einen Kunden neu erstellen oder bearbeiten möchte wird man auf die zugehörige Webseite weitergeleitet.

#### Die Kunden-Hinzufügen-Seite (Adresse: /kundendaten/neu)
Hier ist es möglich einen Kunden zu erstellen.
Da weniger Eingaben gefordert werden unterscheidet sich das UI zum Äquivalent für Projekte allerdings nicht für Mitarbeiter.

#### Die Kunden-Bearbeiten-Seite (Adresse: /kundendaten/<Kunden-Id>)
Hier ist es möglich einen vorher ausgewählten Kunden zu bearbeiten.
Da weniger Eingaben gefordert werden unterscheidet sich das UI zum Äquivalent für Projekte allerdings nicht für Mitarbeiter.

#### Die Mitarbeiter-Übersicht (Adresse: /mitarbeiterdaten)
Eine Übersicht über alle vorhandenen Mitarbeiter mit den jeweils dazugehörigen Informationen in einer übersichtlichen Auflistung.
Von hier aus ist es möglich, einen neuen Mitarbeiter zu erstellen, einen ausgewählten Mitarbeiter zu bearbeiten oder zu löschen.
Wenn man einen Mitarbeiter neu erstellen oder bearbeiten möchte wird man auf die zugehörige Webseite weitergeleitet.

#### Die Mitarbeiter-Hinzufügen-Seite (Adresse: /mitarbeiterdaten/neu)
Hier ist es möglich einen Mitarbeiter zu erstellen.
Da weniger Eingaben gefordert werden unterscheidet sich das UI zum Äquivalent für Projekte allerdings nicht für Kunden.

#### Die Mitarbeiter-Bearbeiten-Seite (Adresse: /mitarbeiterdaten/<Mitarbeiter-Id>)
Hier ist es möglich einen vorher ausgewählten Mitarbeiter zu bearbeiten.
Da weniger Eingaben gefordert werden unterscheidet sich das UI zum Äquivalent für Projekte allerdings nicht für Kunden.

#### Die Auswertung-Seite (Adresse: /auswertung)
Diese Webseite ist nur bei dem Programm für Aufgabenstellung *1.2* zu finden.
Hierbei handelt es sich um eine Übersicht über alle vorhandenen Projekte, erweitert deren Übersicht allerdings über eine differenziertere Übersicht des Kunden und der beteiligten Mitarbeiter.
Die Übersicht ist nach *Projektbezeichnung* sortiert und innerhalb jedes Projekts sind die Mitarbeiter nach *Namen, Vornamen* sortiert.
Ausserdem ist hier nicht nur die *Wöchentliche Zuordnung der Arbeit* aufgelistet sondern auch der gesamte Stundenaufwand und zusätzlich aufgeschlüsselt für jede einzelne Woche.

---

## <span style="color:#667db6">Beschreibung der Komponenten des Servers</span>

### DISCLAIMER:
Um die Übersichtlichkeit zu verbessern wurde das Projekt unterteilt für die:
1. erste Teilaufgabe (siehe Ordner **web/p11/**)
2. zweite Teilaufgabe (siehe Ordner **web/p12/**)

Damit gewährleistet ist, dass, bis auf wenige Ausnahmen, alle Dateien gleich sind, kann das Skript **assert-integrity.sh** ausgeführt werden. Es zeigt alle (relevanten) Dateien an, die für beide Teilaufgaben existieren, sich gleichen oder unterscheiden!

Dieses Skript liegt im Ordner **web/test** zusammen mit anderen Skripten.

### server.py
#### Zweck
Hierbei handelt es sich um den eigentlichen Web-Server, der das Routing zur Verfügung stellt sowie die Konfiguration vornimmt.
Er unterscheidet für Aufgabenstellung *1.1* und *1.2* in seinem Routing, ist allerdings in seiner Konfiguration identisch.

#### Aufbau (Bestandteile der Komponente)
Für jede im Routing vorgesehene Webseite wird eine Funktion zur Verfügung gestellt, die eine Interaktion mit ebendieser handhabt.

Für Aufgabenstellung *1.1* gibt es alle vorgesehenen Webseiten sowie ihre Formular-Handler abzüglich der Auswertung.

Für Aufgabenstellung *1.2* gibt es alle vorgesehenen Webseiten sowie eine API-Schnittstelle für AJAX-Aufrufe an ebendiese.

#### Zusammenwirken mit anderen Komponenten
In beiden Versionen werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen.

#### API (Programmierschnittstellen), die die Leistungen der Komponente anbieten
Diese gibt es nur für Aufgabenstellung *1.2* da in dieser Version einzelne Webseiten (bsp. die Hinzufügen- und Bearbeiten-Seite für Projekte) über AJAX-Aufrufe Daten anfordern bzw. ein Grossteil der Funktionen über eben solche API-Aufrufe realisiert sind.

### application.py
#### Zweck
Hierbei handelt es sich um eine Komponente, die Anfragen des Servers verarbeitet und eine höhere Abstraktionsebene darstellt.
Für beide Aufgabenstellungen ist diese Komponente identisch.

#### Aufbau (Bestandteile der Komponente)
Es gibt unterschiedliche Funktionen, die unter anderem den Aufruf von statischen oder dynamischen Webseiten handhaben, API-Aufrufe oder die Auswertung generieren.

#### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **database.py** aufgerufen und der **view.py** aufgerufen.

### database.py
#### Zweck
Hierbei handelt es sich um eine Komponente, die die Interaktion mit dem Datenbestand handhabt.
Für beide Aufgabenstellungen ist diese Komponente identisch.

#### Aufbau (Bestandteile der Komponente)
Es gibt unterschiedliche Funktionen, die unter anderem die Validierung und jegliche Operation auf die einzelnen JSON-Dateien handhaben.

#### Zusammenwirken mit anderen Komponenten
Es werden keine anderen bereitgestellten Funktionen aus anderen Komponenten aufgerufen, es werden lediglich welche bereitgestellt.

### view.py
#### Zweck
Hierbei handelt es sich um eine Komponente, die das Rendering mithilfe der Mako-Template-Engine handhabt.
Für beide Aufgabenstellungen ist diese Komponente identisch.

#### Aufbau (Bestandteile der Komponente)
Es gibt lediglich zwei Funktionen, einmal um statische Seiten zurückzugeben und zum anderen um dynamische Seiten zu rendern.

#### Zusammenwirken mit anderen Komponenten
Es werden keine anderen bereitgestellten Funktionen aus anderen Komponenten aufgerufen, es werden lediglich welche bereitgestellt.

---

## <span style="color:#667db6">Datenablage</span>
Abgespeichert werden die Projekte mit ihren Kunden und Mitarbeitern in unterschiedlichen JSON-Dateien.
Unterteilt wird für Projekte, Kunden und Mitarbeiter sowie der einzigartigen Id, die vom Web-Server verwaltet wird.
Im folgenden wird jede JSON-Datei anhand ihres Templates kurz erklärt:

### 1. Projektdaten.json

```json
{
    "Template" : {
        "unique_id" : "Eindeutige ID des Projekts (int)",
        "nummer" : "Interne Nummer des Projekts (int)",
        "beizeichnung" : "Bezeichnung fuer das Projekt (string)",
        "beschreibung" : "Kurze Beschreibung des Projekts (string)",
        "bearbeitungszeitraum" : "Anzahl Wochen (int)",
        "budget" : "Dem Projekt zugewiesenes Budget (int)",
        "kunden_id" : "Die eindeutige ID des Kunden zum zuordnen (int)",
        "mitarbeiter_ids" : "Liste aller Mitarbeiter (List[int])",
        "zuordnung_arbeit" : {
            "1. mitarbeiter_id" : "Liste mit Wochenstunden, |Liste|=Anzahl Wochen (List[int])",
            "2. mitarbeiter_id" : "...",
            "..." : "..."
        }
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für ein Projekt angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

### 2. Kundendaten.json

```json
{
    "Template": {
        "unique_id": "Eindeutige ID des Kunden (int)",
        "nummer": "Interne Nummer des Kunden (int)",
        "bezeichnung": "Bezeichnung für den Kunden (string)",
        "ansprechpartner": "Ein Ansprechpartner des Kunden ggf eine Mitarbeiter-ID! (string)",
        "ort": "Adresse des Kunden (string)"
    },
    "Elements": {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für einen Kunden angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

### 3. Mitarbeiterdaten.json

```json
{
    "Template": {
        "unique_id": "Eindeutige ID des Mitarbeiters (int)",
        "name": "Nachname des Mitarbeiters (string)",
        "vorname": "Vorname des Mitarbeiters (sting)",
        "funktion": "Funktion des Mitarbeiters (string)"
    },
    "Elements": {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für einen Mitarbeiter angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

### 4. unique_id.json

```json
{
    "unique_id": 1234567890
}
```

Diese Datei enthält nur die momentan letzte vergebene eindeutige Id, die durch den Web-Server verwaltet und vergeben wird, um die Integrität der Daten zu gewährleisten.

---

## <span style="color:#667db6">Durchführung und Ergebnis der geforderten Prüfungen</span>

Die Syntax und Stilkonventionen der Python-Dateien befolgen keinen Style Guide, sind aber am grobsten durch den [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) identifizierbar.

Die Syntax und Stilkonventionen der JavaScript-Dateien sind grob an den (sich mitunter verändernden) [AirBnB Style Guide](https://github.com/airbnb/javascript) angelehnt. Es wurde versucht, auf viele (ver-)alte JavaScript-Techniken zu verzichten und sich an den neu(st)en zu orientieren.

Die Namensgebung der CSS-Elemente ist grob an die (sich mitunter verändernde) ["Block Element Modifier"-Methode](http://getbem.com/introduction/) angelehnt.

Es wurden alle (generierten) HTML(-Templates)-Dateien mithilfe des [w3c-Validator-Dienstes](https://validator.w3.org/) auf richtige Formatierung überprüft und als fehlerfrei anerkannt.

Es wurden alle CSS-Dateien mithilfe des [w3c-Validator-Dienstes](http://jigsaw.w3.org/css-validator/) auf richtige Formatierung überprüft und als fehlerfrei anerkannt.

Es ist nicht gewährleistet, dass es sich bei der finalen Projekt-Version um die übersichtlichste, am besten optimierteste sowie stilgerechte Lösung handelt.

---

Das Copyright, das in einigen Dateien zu finden ist, schliesst das gesamte Projekt mit ein als geistiges Eigentum von:

**Tobias Hahnen (tobias.hahnen@stud.hn.de)**

# JSON-Dateien
Stand: 29.10.2018 | Version: **1.0.0**

---

## Table of Contents
Element | Abschnitt
--------|----------
*Dateien* | [--> Klick mich <--](#dateien)
*JSON-Template* | [--> Klick mich <--](#json-template)
*Template-Dateien* | [--> Klick mich <--](#template-files)

---

<a name="dateien" />
### Dateien
Es gibt lt. Aufgabenstellung drei JSON-Dateien:
1. [projektdaten.json](projektdaten.json)
    * beinhaltet alle Projekte und die dazugehörigen Daten
    * verlinkt ausserdem (indirekt) auf [kundendaten.json](kundendaten.json) und [mitarbeiterdaten.json](mitarbeiterdaten.json) über die eindeutige ID
2. [kundendaten.json](kundendaten.json)
    * beinhaltet alle Projekt-Kunden und die dazugehörigen Daten
3. [mitarbeiterdaten.json](mitarbeiterdaten.json)
    * beinhaltet alle Mitarbeiter aus allen Projekten und die dazugehörigen Daten

---

<a name="json-template" />
### JSON-Template
#### **projektdaten.json**
Verweise:
- kunden_id : [Auftraggeber](kundendaten.json) des Projekts
- mitarbeiter_id : Beteiligte  [Mitarbeiter](mitarbeiterdaten.sjon) des Projekts

```json
{
    "Template" : {
        "unique_id" : "Eindeutige ID des Projekts",
        "nummer" : "Interne Nummer des Projekts",
        "beizeichnung" : "Bezeichnung für das Projekt",
        "beschreibung" : "Kurze Beschreibung des Projekts",
        "bearbeitungszeitraum" : {
            "anfang" : "Anfangsdatum des Projekts",
            "ende" : "Enddatum des Projekts"
        },
        "budget" : "Dem Projekt zugewiesenes Budget",
        "kunden_id" : "Die eindeutige ID des Kunden zum zuordnen",
        "mitarbeiter_ids" : "[ Liste aller Mitarbeiter ]",
        "zuordnung_arbeit" : "[ Liste Arbeitseinheiten mit { Stunden -> Liste der zugeordneten Mitarbeiter } ]"
    },
    "Elements" : {
        "1...n" : {
            "..."
        }
    }
}
```

#### **kundendaten.json**
Verweise:
- mitarbeiter_id : Ggf. [Ansprechpartner](mitarbeiterdaten.json) in der JSON-Datei

```json
{
    "Template" : {
        "unique_id" : "Eindeutige ID des Kunden",
        "nummer" : "Interne Nummer des Kunden",
        "beizeichnung" : "Bezeichnung für den Kunden",
        "ansprechpartner" : "Ein Ansprechpartner des Kunden ggf eine Mitarbeiter-ID!",
        "ort" : "Ort des Kunden"
    },
    "Elements" : {
        "1...n" : {
            "..."
        }
    }
}
```

#### **mitarbeiterdaten.json**
Verweise:
- *keine*

```json
{
    "Template" : {
        "unique_id" : "Eindeutige ID des Mitarbeiters",
        "name" : "Nachname des Mitarbeiters",
        "vorname" : "Vorname des Mitarbeiters",
        "funktion" : "Funktion des Mitarbeiters"
    },
    "Elements" : {
        "1...n" : {
            "..."
        }
    }
}
```

---

<a name="template-files" />
### Template-Dateien
Werden verwendet, wenn die Integrität der JSON-Dateien nicht gewährleistet ist oder fehlerhafte Daten nicht wieder hergestellt werden können.

**TODO**: Templates hinzufügen!

- [Projektdaten]()
- [Kundendaten]()
- [Mitarbeiterdaten]()

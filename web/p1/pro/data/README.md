# JSON-Dateien
Stand: 29.10.2018 (soweit fertig) | Version: **1.1.1**

---

## Table of Contents
Element | Abschnitt
--------|----------
*Dateien* | [--> Klick mich <--](#dateien)
*JSON-Template* | [--> Klick mich <--](#json-template)
*Template-Dateien* | [--> Klick mich <--](#template-files)

---

<a name="dateien"></a>
## Dateien
Es gibt lt. Aufgabenstellung drei JSON-Dateien:
1. [projektdaten.json](projektdaten.json)
    * beinhaltet alle Projekte und die dazugehörigen Daten
    * verlinkt ausserdem (indirekt) auf [kundendaten.json](kundendaten.json) und [mitarbeiterdaten.json](mitarbeiterdaten.json) über die eindeutige ID
2. [kundendaten.json](kundendaten.json)
    * beinhaltet alle Projekt-Kunden und die dazugehörigen Daten
3. [mitarbeiterdaten.json](mitarbeiterdaten.json)
    * beinhaltet alle Mitarbeiter aus allen Projekten und die dazugehörigen Daten

---

<a name="json-template"></a>
## JSON-Template
### **projektdaten.json**
Verweise:
- kunden_id : [Auftraggeber](kundendaten.json) des Projekts
- mitarbeiter_id : Beteiligte  [Mitarbeiter](mitarbeiterdaten.sjon) des Projekts

```json
{
    "Template" : {
        "unique_id" : "Eindeutige ID des Projekts (int)",
        "nummer" : "Interne Nummer des Projekts (int)",
        "beizeichnung" : "Bezeichnung fuer das Projekt (string)",
        "beschreibung" : "Kurze Beschreibung des Projekts (string)",
        "bearbeitungszeitraum" : {
            "anfang" : "Anfangsdatum des Projekts (date)",
            "ende" : "Enddatum des Projekts (date)"
        },
        "budget" : "Dem Projekt zugewiesenes Budget (float)",
        "kunden_id" : "Die eindeutige ID des Kunden zum zuordnen (int)",
        "mitarbeiter_ids" : "Liste aller Mitarbeiter (List[int])",
        "zuordnung_arbeit" : {
            "1...n" : {
                "stunden" : "Aufwandsstunden fuer das jeweilige Arbeitspaket (int)",
                "mitarbeiter_ids" : "Liste aller dem Arbeitspaket zugeordneten Mitarbeiter (List[int])"
            }
        }
    },
    "Elements" : {
        "1...n" : {
            "..."
        }
    }
}
```

### **kundendaten.json**
Verweise:
- mitarbeiter_id : Ggf. [Ansprechpartner](mitarbeiterdaten.json) in der JSON-Datei

```json
{
    "Template" : {
        "unique_id" : "Eindeutige ID des Kunden (int)",
        "nummer" : "Interne Nummer des Kunden (int)",
        "beizeichnung" : "Bezeichnung fuer den Kunden (string)",
        "ansprechpartner" : "Ein Ansprechpartner des Kunden ggf eine Mitarbeiter-ID! (string)",
        "ort" : "Adresse des Kunden (string)"
    },
    "Elements" : {
        "1...n" : {
            "..."
        }
    }
}
```

### **mitarbeiterdaten.json**
Verweise:
- *keine*

```json
{
    "Template": {
        "unique_id" : "Eindeutige ID des Mitarbeiters (int)",
        "name" : "Nachname des Mitarbeiters (string)",
        "vorname" : "Vorname des Mitarbeiters (sting)",
        "funktion" : "Funktion des Mitarbeiters (string)"
    },
    "Elements" : {
        "1...n" : {
            "..."
        }
    }
}
```

---

<a name="template-files"></a>
## Template-Dateien
Werden verwendet, wenn die Integrität der JSON-Dateien nicht gewährleistet ist oder fehlerhafte Daten nicht wieder hergestellt werden können.
Um bei der Validierung die Datei wiederherstellen zu können!

- [Projektdaten](/template/projektdaten.json)
- [Kundendaten](/template/kundendaten-tpl.json)
- [Mitarbeiterdaten](/template/mitarbeiterdaten-tpl.json)

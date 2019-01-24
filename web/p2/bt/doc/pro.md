# <span style="color:#667db6">Bug-Tracker (Praktikum 3)</span>

---

## <span style="color:#667db6">Einleitung</span>

Die Lösung ist darüber realisiert, dass man für QS-Mitarbeiter und SW-Entwickler eine eigene Sicht des Bug-Treckers hat.

Ein QS-Mitarbeiter kann beispielsweise weniger Dinge verändern und einsehen als ein SW-Entwickler.

Realisiert über eine Web-Anwendung, zu der man erst nach erfolgreicher Authentifikation gelangt.
Danach ist alles über eine Single-Page-Applikation realisiert.

---

## <span style="color:#667db6">Implementierung des Servers</span>

### REST-Interface
Für das REST-Interface siehe Python-Module sowie die Aufgabenstellung.
Zur Validierung des REST-Interface kann das Test-Skript *test_rest.sh* im Ordner **test** genutzt werden.


### Module

#### server.py
##### Zweck
Hierbei handelt es sich um den eigentlichen Web-Server, der das Routing zur Verfügung stellt sowie die Konfiguration vornimmt.

##### Aufbau (Bestandteile der Komponente)
Für jede im Routing vorgesehene Webseite wird eine Funktion zur Verfügung gestellt, die eine Interaktion mit ebendieser handhabt.
Dabei wird insbesondere auf das Routing und das Auswerten der Anmeldedaten sowie Cookies geachtet.

Die REST-Implementierung ist auf die jeweiligen Daten im Ordner **app** aufgeteilt.

##### Zusammenwirken mit anderen Komponenten
Es werden bereitgestellte Funktionen aus der **application.py** sowie aus allen REST-Implementierungen unter **app** aufgerufen.

##### API (Programmierschnittstellen), die die Leistungen der Komponente anbieten
Der Server selbst bietet keine API.

#### application.py
##### Zweck
Hierbei handelt es sich um eine Komponente, die Anfragen des Servers verarbeitet und eine höhere Abstraktionsebene darstellt.
Für beide Aufgabenstellungen ist diese Komponente identisch.

##### Aufbau (Bestandteile der Komponente)
Es gibt unterschiedliche Funktionen, die unter anderem den Aufruf von statischen oder dynamischen Webseiten handhaben, API-Aufrufe oder die Auswertung generieren.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **database.py** aufgerufen und der **view.py** aufgerufen.

#### database.py
##### Zweck
Hierbei handelt es sich um eine Komponente, die die Interaktion mit dem Datenbestand handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt unterschiedliche Funktionen, die unter anderem die Validierung und jegliche Operation auf die einzelnen JSON-Dateien handhaben.

##### Zusammenwirken mit anderen Komponenten
Es werden keine anderen bereitgestellten Funktionen aus anderen Komponenten aufgerufen, es werden lediglich welche bereitgestellt.

#### view.py
##### Zweck
Hierbei handelt es sich um eine Komponente, die kein Rendering handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt lediglich zwei Funktionen, einmal um statische Seiten zurückzugeben und zum anderen um die Templates zurückzugeben.

##### Zusammenwirken mit anderen Komponenten
Es werden keine anderen bereitgestellten Funktionen aus anderen Komponenten aufgerufen, es werden lediglich welche bereitgestellt.

#### fehler.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */fehler* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine POST-Methode, diese behandelt den HTTP-POST-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine PUT-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### projekt.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */projekt* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine POST-Methode, diese behandelt den HTTP-POST-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine PUT-Methode, diese behandelt den HTTP-PUT-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine DELETE-Methode, diese behandelt den HTTP-DELETE-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### projektkomponenten.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */projektkomponenten* sowie */komponenten* handhabt.

##### Aufbau (Bestandteile der Komponente) fuer */projektkomponenten*
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Aufbau (Bestandteile der Komponente) fuer */komponenten*
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine POST-Methode, diese behandelt den HTTP-POST-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine PUT-Methode, diese behandelt den HTTP-PUT-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine DELETE-Methode, diese behandelt den HTTP-DELETE-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### katfehler.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */katfehler* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine POST-Methode, diese behandelt den HTTP-POST-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine PUT-Methode, diese behandelt den HTTP-PUT-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine DELETE-Methode, diese behandelt den HTTP-DELETE-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### katursache.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */katursache* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine POST-Methode, diese behandelt den HTTP-POST-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine PUT-Methode, diese behandelt den HTTP-PUT-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine DELETE-Methode, diese behandelt den HTTP-DELETE-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### qsmitarbeiter.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */qsmitarbeiter* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine POST-Methode, diese behandelt den HTTP-POST-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine PUT-Methode, diese behandelt den HTTP-PUT-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine DELETE-Methode, diese behandelt den HTTP-DELETE-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### swentwickler.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */swentwickler* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine POST-Methode, diese behandelt den HTTP-POST-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine PUT-Methode, diese behandelt den HTTP-PUT-Aufruf, wie er in der Aufgabenstellung gefordert ist.
Es gibt eine DELETE-Methode, diese behandelt den HTTP-DELETE-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### katlist.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */katlist* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### prolist.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */prolist* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen

#### templates.py
##### Zweck
Hierbei handelt es sich um eine REST-Komponente, die die HTTP-Anfragen an */templates* handhabt.

##### Aufbau (Bestandteile der Komponente)
Es gibt eine GET-Methode, diese behandelt den HTTP-GET-Aufruf, wie er in der Aufgabenstellung gefordert ist.

##### Zusammenwirken mit anderen Komponenten
Es werden unter anderem bereitgestellte Funktionen aus der **application.py** aufgerufen


### Datenhaltung

#### 1. fehler.json

```json
{
    "Template": {
        "unique_id": "Eindeutige Id des Fehlers (int)",
        "type": "Zustand des Fehlers (erkannt | beseitigt)",
        "komponente": "Eindeutige Id der Komponente (unique_id)",
        "erkannt": {
            "beschreibung": "Beschreibung des Fehlers durch QS-Mitarbeiter (string)",
            "bearbeiter": "QS-Mitarbeiter, der Fehler erfasst hat (unique_id)",
            "datum": "Datum der Fehlererfassung (string)",
            "fehlerkategorien": "Vom QS-Mitarbeiter vergebene Kategorien (List[unique_id])"
        },
        "beseitigt": {
            "beschreibung": "Beschreibung der Fehlerursache durch SW-Entwickler (string)",
            "bearbeiter": "SW-Entwickler, der Fehler bearbeitet hat (unique_id)",
            "datum": "Datum der Fehlerbearbeitung (string)",
            "fehlerursachenkategorie": "Dem Fehler final zugeordnete Fehlerursachenkategorie (unique_id)"
        }
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für einen Fehler angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

#### 2. projekte.json

```json
{
    "Template": {
        "unique_id": "Eindeutige Id des Projekts (int)",
        "komponenten": "Dem Projekt zugeh\u00f6rige Komponenten (List[unique_id])"
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für ein Projekt angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

#### 3. komponenten.json

```json
{
    "Template": {
        "unique_id": "Eindeutige Id der Komponente (int)",
        "fehler": "Die von der Komponente verursachten Fehler (List[unique_id])"
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für eine Komponente angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

#### 4. qsmitarbeiter.json

```json
{
    "Template": {
        "unique_id": "Eindeutige Id des QS-Mitarbeiter (int)",
        "username": "Benutzername des QS-Mitarbeiter (string)",
        "password": "Password-Hash des QS-Mitarbeiter zur Authentifikation (string)"
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für einen QS-Mitarbeiter angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

#### 5. swentwickler.json

```json
{
    "Template": {
        "unique_id": "Eindeutige Id des SW-Entwickler (int)",
        "username": "Benutzername des SW-Entwickler (string)",
        "password": "Password-Hash des SW-Entwickler zur Authentifikation (string)"
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für einen SW-Entwickler angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

#### 6. fehlerkategorien.json

```json
{
    "Template": {
        "unique_id": "Eindeutige Id der Fehlerkategorie (int)",
        "beschreibung": "Beschreibung der Fehlerkategorie (string)"
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für eine Fehlerkategorie angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

#### 7. fehlerursachenkategorie.json

```json
{
    "Template": {
        "unique_id": "Eindeutige Id der Fehlerursachenkategorie (int)",
        "beschreibung": "Beschreibung der Fehlerursachenkategorie (string)"
    },
    "Elements" : {
    }
}
```

Dieses Template enthält alle unterschiedlichen Daten, die für eine Fehlerursachenkategorie angegeben werden können, wobei jeweils eine eigene kurze Erklärung präsentiert wird.

#### 8. unique_id.json

```json
{
    "unique_id": 1234567890
}
```

Diese Datei enthält nur die momentan letzte vergebene eindeutige Id, die durch den Web-Server verwaltet und vergeben wird, um die Integrität der Daten zu gewährleisten.

---

## <span style="color:#667db6">Implementierung des Clients</span>

### Klassen

#### Application
##### Aufgaben:

Stellt in jeder Instanz des Bug-Treckers die Verbindung der einzelnen Views zur Verfügung.
Beinhaltet ausserdem den Einsatz des EventServices.

##### Zusammenwirken

Es gibt nur eine Instanz, beinhaltet alle Views, die für den jeweiligen Mitarbeiter möglich sind.
Ruft durch Events ebendiese auf.

#### SideBar
##### Aufgaben:

Stellt die Seitenleiste (Navigationsleiste) zur Verfügung.

##### Zusammenwirken

Bei Klick auf einzelne Links, wird über die Application in die jeweiligen Views gewechselt.

#### errorView
##### Aufgaben:

Stellt alle Views zu den Fehlern zur Verfügung, ob Übersicht, Editieren oder hinzugefuegen.

##### Zusammenwirken

Bei einzelnen Events werden die Views gewechselt oder aber REST-Aufrufe durchgeführt und der Datenbestand verändert.

#### projectView
##### Aufgaben:

Stellt alle Views zu den Projekten zur Verfügung, ob Übersicht, Editieren oder hinzugefuegen.

##### Zusammenwirken

Bei einzelnen Events werden die Views gewechselt oder aber REST-Aufrufe durchgeführt und der Datenbestand verändert.

#### componentView
##### Aufgaben:

Stellt alle Views zu den Komponenten zur Verfügung, ob Übersicht, Editieren oder hinzugefuegen.

##### Zusammenwirken

Bei einzelnen Events werden die Views gewechselt oder aber REST-Aufrufe durchgeführt und der Datenbestand verändert.

#### workerView
##### Aufgaben:

Stellt alle Views zu den QS-Mitarbeitern/ SW-Entwicklern zur Verfügung, ob Übersicht, Editieren oder hinzugefuegen.

##### Zusammenwirken

Bei einzelnen Events werden die Views gewechselt oder aber REST-Aufrufe durchgeführt und der Datenbestand verändert.

#### categoryView
##### Aufgaben:

Stellt alle Views zu den Fehlerkategorien/ Fehlerursachenkategorien zur Verfügung, ob Übersicht, Editieren oder hinzugefuegen.

##### Zusammenwirken

Bei einzelnen Events werden die Views gewechselt oder aber REST-Aufrufe durchgeführt und der Datenbestand verändert.

#### errorsByProject
##### Aufgaben:

Stellt alle die Auswertung nach Projekten zur Verfügung.

##### Zusammenwirken

Es besteht kein Zusammenwirken.

#### errorsByCategory
##### Aufgaben:

Stellt alle die Auswertung nach Kategorien zur Verfügung.

##### Zusammenwirken

Es besteht kein Zusammenwirken.


### EventService

Der EventService wird zur Navigation eingesetzt. Zwischen den Views der einzelnen Bereiche sowie zwischen den Bereichen.
Grob implementiert nach dem Schemata in der Aufgabenstellung und angelehnt an Beims seine Beispiele.


### Templateverarbeitung

#### error.[...].tpl

Dabei handelt es sich um alle Templates, die mit den Fehlern zu tun haben, ob Übersicht, Editieren oder hinzufügen.

#### project.[...].tpl

Dabei handelt es sich um alle Templates, die mit den Projekten zu tun haben, ob Übersicht, Editieren oder hinzufügen.

#### component.[...].tpl

Dabei handelt es sich um alle Templates, die mit den Komponenten zu tun haben, ob Übersicht, Editieren oder hinzufügen.

#### worker.[...].tpl

Dabei handelt es sich um alle Templates, die mit den QS-Mitarbeitern/ SW-Entwicklern zu tun haben, ob Übersicht, Editieren oder hinzufügen.

#### category.[...].tpl

Dabei handelt es sich um alle Templates, die mit den Fehlerkategorien / Fehlerursachenkategorien zu tun haben, ob Übersicht, Editieren oder hinzufügen.

#### sidebar.tpl

Dabei handel es sich um die Navigationsleiste.

#### header.tpl

Der Header für die Single-Page-Application, beinhaltet alles geforderte sowie zur Übersicht die Informationen über den angemeldeteten Benutzer.

#### home.tpl + footer.tpl

Übernommen aus Beims sein Beispiel. Einfach so drin.


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

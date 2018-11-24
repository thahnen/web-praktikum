/*
 *  new-project.js
 *  =======
 *
 *  Logik für die Projektdaten-Hinzufuegen-Seite
 *
 *  1) Eigenschaften setzen:
 *  => Verbergen der Fehlermeldung
 *  => Titel und Header richtig setzen
 *  => Laden der Kunden und ins bestimme Feld einfügen (alten auswählen!)
 *  => Laden der Mitarbeiter und ins bestimmte Feld einfügen (alte auswählen!)
 *
 *  2) Input-Event-Listener hinzufügen (alle)
 *  => onClick: Verbergen der Fehlermeldung
 *
 *  3) Input-Event-Listener hinzufügen - Zahl (Bearbeitungszeitraum)
 *  => onChange: Änderung verändert Arbeitszuordnungs-Tabelle
 *
 *  4) Select-Event-Listener hinzufügen (Mitarbeiter)
 *  => onClick: Auswahl/ Abwahl verändert die Arbeitszuordnungs-Tabelle!
 *
 *  5) "Hinzufügen" gedrückt:
 *  => überprüfen ob alle machbaren Angaben leer oder fehlerhaft sind?
 *  => XMLHttpRequest absetzen und auf Antwort warten und reagieren
*/

(function() {
    'use strict';


    // Hilfsfunktion um JSON von Server synchron(!) zu laden
    function loadJSONData(datensatz) {
        var rueckgabe;
        var http = new XMLHttpRequest();
        // hier das false, damit nicht asynchron geladen wird!
        http.open("POST", "/api/get", false);
        http.setRequestHeader("Content-Type", "application/json");
        http.onload = function() {
            rueckgabe = JSON.parse(this.responseText);
            if (rueckgabe["code"] != 200) {
                // Vielleicht kann man das hier noch etwas schöner handhaben
                alert("Fehler beim abrufen der: " + datensatz);
            }
        }
        http.send(JSON.stringify({
            "link" : datensatz,
            "token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
            "data" : ""
        }));
        // nur Rückgabe der Elemente, Rest braucht man nicht
        return rueckgabe["data"]["Elements"]
    }


    window.onload = function() {
        // 1) Eigenschaften setzen
        // Verbergen der Fehlermeldung
        var div_failure = document.querySelector(".div--failure");
        div_failure.style.setProperty("--max-height", div_failure.scrollHeight + "px");
        var offen = false;

        // Titel und Headline richtig setzen
        var link = window.location.href.split("/")[3].split("?")[0];
        link = link.charAt(0).toUpperCase() + link.slice(1);
        document.title = link + document.title;
        var headline = document.getElementById("headline");
        headline.innerHTML = link + headline.innerHTML;

        // Kunden laden und ins designierte Feld eintragen
        var kunden_select = document.getElementById("select_kunden_id");
        var kunden = loadJSONData("Kundendaten");
        for (var kunde in kunden) {
            var option = document.createElement("option");
            option.setAttribute("value", parseInt(kunden[kunde].unique_id))
            option.appendChild(
                document.createTextNode("(" + kunden[kunde].unique_id + ") " +kunden[kunde].ansprechpartner)
            )
            kunden_select.appendChild(option)
        }

        // Mitarbeiter laden und ins designierte Feld eintragen
        var mitarbeiter_select = document.getElementById("select_mitarbeiter_ids");
        var mitarbeiter = loadJSONData("Mitarbeiterdaten");
        for (var arbeiter in mitarbeiter) {
            var option = document.createElement("option")
            option.setAttribute("value", parseInt(mitarbeiter[arbeiter].unique_id))
            option.appendChild(
                document.createTextNode("(" + mitarbeiter[arbeiter].unique_id + ") " + mitarbeiter[arbeiter].vorname + " " + mitarbeiter[arbeiter].name)
            )
            mitarbeiter_select.appendChild(option)
        }


        // 2) Input-Event-Listener hinzufuegen
        [...document.getElementsByClassName("input--data")].forEach((x) => {
            // onClick-Event-Listener
            x.addEventListener("click", function() {
                if (offen) {
                    div_failure.style.removeProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }
            });
        });


        // 3) Input-Event-Listener hinzufuegen (Bearbeitungszeitraum)
        // Muss noch IDs vergeben!
        document.getElementById("bearbeitungszeitraum").addEventListener("input", function() {
            // Neue Anzahl Wochen einlesen und die ausgewählten Mitarbeiter:
            var neue = parseInt(this.value);
            var anzahl_mitarbeiter = [...document.getElementById("select_mitarbeiter_ids").selectedOptions]
            // testen, ob der Wert auch eine Zahl ist!
            if (isNaN(neue)) { return }

            // Eigentlich an Tabelle anfügen bzw. kürzen
            // Zu viel Aufwand, daher Tabelle einfach löschen und neu generieren (nicht optimal)
            var zuordnung_arbeit = document.getElementById("zuordnung_arbeit");
            while (zuordnung_arbeit.firstChild) {
                zuordnung_arbeit.removeChild(zuordnung_arbeit.firstChild)
            }

            // 1) Überschriften
            var header = document.createElement("tr")
            var header_id = document.createElement("th")
            header_id.innerText = "Id / Woche"
            header.appendChild(header_id)
            for (var i=1; i<neue+1; i++) {
                var week_n = document.createElement("th")
                week_n.innerText = "Woche " + i.toString()
                header.appendChild(week_n)
            }
            zuordnung_arbeit.appendChild(header)

            // 2) für jeden Mitarbeiter
            for (var i=0; i<anzahl_mitarbeiter.length; i++) {
                var data_row = document.createElement("tr")
                var name = document.createElement("td")
                name.innerText = anzahl_mitarbeiter[i].value
                data_row.appendChild(name)

                for (var j = 0; j < neue; j++) {
                    var week_n = document.createElement("th")
                    var week_n_input = document.createElement("input")
                    week_n_input.setAttribute("class", "mitarbeiter_wochenstunden")
                    week_n.appendChild(week_n_input)
                    data_row.appendChild(week_n)
                }

                zuordnung_arbeit.appendChild(data_row)
            }
        });


        // 4) Select-Event-Listener hinzufuegen (Mitarbeiter)
        document.getElementById("select_mitarbeiter_ids").addEventListener("click", function() {
            // Neue Anzahl Wochen einlesen und die ausgewählten Mitarbeiter:
            var neue = parseInt(document.getElementById("bearbeitungszeitraum").value)
            var anzahl_mitarbeiter = [...this.selectedOptions]
            // testen, ob der Wert auch eine Zahl ist!
            if (isNaN(neue)) { return }

            // Eigentlich an Tabelle anfügen bzw. kürzen
            // Zu viel Aufwand, daher Tabelle einfach löschen und neu generieren (nicht optimal)
            var zuordnung_arbeit = document.getElementById("zuordnung_arbeit");
            while (zuordnung_arbeit.firstChild) {
                zuordnung_arbeit.removeChild(zuordnung_arbeit.firstChild)
            }

            // 1) Überschriften
            var header = document.createElement("tr")
            var header_id = document.createElement("th")
            header_id.innerText = "Id / Woche"
            header.appendChild(header_id)
            for (var i=1; i<neue+1; i++) {
                var week_n = document.createElement("th")
                week_n.innerText = "Woche " + i.toString()
                header.appendChild(week_n)
            }
            zuordnung_arbeit.appendChild(header)

            // 2) für jeden Mitarbeiter
            for (var i=0; i<anzahl_mitarbeiter.length; i++) {
                var data_row = document.createElement("tr")
                var name = document.createElement("td")
                name.innerText = anzahl_mitarbeiter[i].value
                data_row.appendChild(name)

                for (var j = 0; j < neue; j++) {
                    var week_n = document.createElement("th")
                    var week_n_input = document.createElement("input")
                    week_n_input.setAttribute("type", "number")
                    week_n_input.setAttribute("class", "mitarbeiter_wochenstunden")
                    week_n.appendChild(week_n_input)
                    data_row.appendChild(week_n)
                }

                zuordnung_arbeit.appendChild(data_row)
            }
        })


        // 5) "Hinzufuegen" gedrückt
        document.getElementById("btn--new").addEventListener("click", function() {
            if (confirm("Wollen sie das Element wirklich hinzufuegen?")) {
                // Input-Felder auf Richtigkeit überprüfen macht das Backend
                var header = [...document.getElementsByClassName("tbl--header--info")];
                var inputs = [...document.getElementsByClassName("input--data")];

                // Alle Eingabemöglichkeiten mit ID belegen
                var nummer = parseInt(document.getElementById("nummer").value)
                var bezeichnung = document.getElementById("bezeichnung").value
                var beschreibung = document.getElementById("beschreibung").value
                var bearbeitungszeitraum = parseInt(document.getElementById("bearbeitungszeitraum").value)
                var budget = parseInt(document.getElementById("budget").value)
                if (nummer == null || isNaN(nummer) || bezeichnung == null || beschreibung == null
                    || bearbeitungszeitraum == null || isNaN(bearbeitungszeitraum)
                    || budget == null || isNaN(budget)) {
                    console.log("Irgendwelche Eingaben fehlerhaft");
                    return
                }
                try {
                    var kunden_id = parseInt([...document.getElementById("select_kunden_id").selectedOptions][0].value)
                } catch (e) {
                    console.log("kunden_id nicht ausgewählt");
                    return
                }
                var mitarbeiter_ids = [...document.getElementById("select_mitarbeiter_ids").selectedOptions].map(x => parseInt(x.value))
                if (mitarbeiter_ids.length == 0) {
                    console.log("mitarbeiter_ids nicht ausgewählt");
                    return
                }
                var zuordnung_arbeit = {}
                var stunden = [...document.getElementsByClassName("mitarbeiter_wochenstunden")].map(x => parseInt(x.value))
                for (var x = 0; x < stunden.length; x++) {
                    if (stunden[x] == null || isNaN(stunden[x])) {
                        console.log("Zuordnung der Arbeit nicht richtig ausgefüllt!");
                        return
                    }
                }

                var anz_mit = mitarbeiter_ids.length
                for (var i = 0; i < anz_mit; i++) {
                    var stunden_liste = []
                    for (var j = i*bearbeitungszeitraum; j < (i+1)*bearbeitungszeitraum; j++) {
                        stunden_liste.push(stunden[j])
                    }
                    zuordnung_arbeit[mitarbeiter_ids[i].toString()] = stunden_liste
                }

                // Der Request, der mit Daten vollgepackt wird
                var request = {
                    "link" : link,
                    "token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
                    "data" : {
                        "unique_id" : "Ich werde autogeneriert",
                        "nummer" : nummer,
                        "bezeichnung" : bezeichnung,
                        "beschreibung" : beschreibung,
                        "bearbeitungszeitraum" : bearbeitungszeitraum,
                        "budget" : budget,
                        "kunden_id" : kunden_id,
                        "mitarbeiter_ids" : mitarbeiter_ids,
                        "zuordnung_arbeit" : zuordnung_arbeit
                    }
                };

                console.log(JSON.stringify(request));
                // POST absetzen mit den neuen Daten
                var http = new XMLHttpRequest();
                http.open("POST", "/api/new");
                http.setRequestHeader("Content-Type", "application/json");
                http.onload = function() {
                    var rueckgabe = JSON.parse(this.responseText);
                    var h2_failure = document.querySelector(".h2--failure");
                    if (rueckgabe["code"] != 200) {
                        h2_failure.innerHTML = "Fehlermeldung Code: " + rueckgabe["code"];
                    } else {
                        h2_failure.innerHTML = "Hinzufuegen erfolgreich!";
                    }
                    if (!offen) {
                        div_failure.style.setProperty("max-height", "var(--max-height)");
                        offen = !offen;
                    }
                };

                http.send(JSON.stringify(request));
            }
        })
    }
})();

/*
 *  edit-project.js
 *  =======
 *
 *  Logik für die Projektdaten-Bearbeiten-Seite
 *
 *  1) Eigenschaften setzen:
 *  => Verbergen der Fehlermeldung
 *  => Titel und Header richtig setzen
 *  => Laden der Kunden und ins bestimme Feld einfügen (alten auswählen!)
 *      => Bereits bestehenden Kunden nicht neuhinzufügen, aber ausfüllen und auswählen
 *  => Laden der Mitarbeiter und ins bestimmte Feld einfügen (alte auswählen!)
 *      => Bereits bestehende Mitarbeiter nicht neuhinzufügen, aber ausfüllen und auswählen
 *
 *  2) "Editieren" gedrückt:
 *  => alle Input-Felder mit gleicher Bearbeiten-Klasse "un-disablen"
 *
 *  3) Input-Event-Listener hinzufügen (alle)
 *  => onClick: Verbergen der Fehlermeldung
 *  => alle Inputs deaktivieren (sonst wären sie bei Seitenaufruf editierbar!)
 *
 *  4) Input-Event-Listener hinzufügen - Zahl (Bearbeitungszeitraum)
 *  => onChange: Änderung verändert Arbeitszuordnungs-Tabelle
 *
 *  5) Select-Event-Listener hinzufügen (Mitarbeiter)
 *  => onClick: Auswahl/ Abwahl verändert die Arbeitszuordnungs-Tabelle!
 *
 *  6) "Speichern" gedrückt:
 *  => überprüfen ob alle machbaren Angaben leer oder fehlerhaft sind?
 *  => XMLHttpRequest absetzen und auf Antwort warten und reagieren
*/


(function () {
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
        return rueckgabe["data"]["Elements"];
    }


    window.onload = function () {
        // 1) Eigenschaften setzen
        // Verbergen der Fehlermeldung
        var div_failure = document.querySelector(".div--failure");
        div_failure.style.setProperty("--max-height", div_failure.scrollHeight + "px");
        var offen = false;

        // Titel und Header richtig setzen
        var link = window.location.href.split("/")[3].split("?")[0];
        link = link.charAt(0).toUpperCase() + link.slice(1);
        document.title = link + ": " + document.title;
        var headline = document.getElementById("headline");
        headline.innerHTML = link + ": " + headline.innerHTML;

        // Kunden laden und ins designierte Feld eintragen
        var kunden_select = document.getElementById("select_kunden_id");
        var bereits_kunde = kunden_select.firstElementChild;
        var kunden = loadJSONData("Kundendaten");
        for (var kunde in kunden) {
            if (parseInt(bereits_kunde.value) == parseInt(kunden[kunde].unique_id)) {
                // Bereits bestehde Kunden abändern
                bereits_kunde.innerHTML = "(" + kunden[kunde].unique_id + ") " + kunden[kunde].ansprechpartner;
                bereits_kunde.selected = true;
            } else {
                var option = document.createElement("option");
                option.setAttribute("value", parseInt(kunden[kunde].unique_id));
                option.appendChild(
                    document.createTextNode("(" + kunden[kunde].unique_id + ") " + kunden[kunde].ansprechpartner)
                );
                kunden_select.appendChild(option);
            }
        }

        // Mitarbeiter laden und ins designierte Feld eintragen
        var mitarbeiter_select = document.getElementById("select_mitarbeiter_ids");
        var bereits_mitarbeiter = [...mitarbeiter_select.children];
        var mitarbeiter = loadJSONData("Mitarbeiterdaten");
        for (var arbeiter in mitarbeiter) {
            var found = false;
            bereits_mitarbeiter.forEach((x) => {
                // Bereits bestehde Mitarbeiter abändern
                if (parseInt(mitarbeiter[arbeiter].unique_id) == parseInt(x.value)) {
                    x.innerHTML = "(" + mitarbeiter[arbeiter].unique_id + ") " + mitarbeiter[arbeiter].vorname + " " + mitarbeiter[arbeiter].name;
                    found = true;
                }
            });
            if (!found) {
                var option = document.createElement("option");
                option.setAttribute("value", parseInt(mitarbeiter[arbeiter].unique_id));
                option.appendChild(
                    document.createTextNode("(" + mitarbeiter[arbeiter].unique_id + ") " + mitarbeiter[arbeiter].vorname + " " + mitarbeiter[arbeiter].name)
                );
                mitarbeiter_select.appendChild(option);
            }
        }


        // 2) "Editieren" gedrückt
        document.getElementById("btn--edit").addEventListener("click", function() {
            // Alle Inputs zum bearbeiten aktivieren
            [...document.getElementsByClassName("input--edit")].forEach((x) => {
                x.disabled = false;
                if (offen) {
                    div_failure.style.removeProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }
            });
        });


        // 3) Input-Event-Listener hinzufügen
        [...document.getElementsByClassName("input--data")].forEach((x) => {
            // 3.1) onClick-Event-Listener
            x.addEventListener("click", function() {
                if (offen) {
                    div_failure.style.removeProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }
            });

            // 3.2) Alle Inputs deaktivieren (sonst wären sie bei Seitenaufruf editierbar!)
            x.disabled = true;
        });


        // 4) Input-Event-Listener hinzufuegen (Bearbeitungszeitraum)
        // Muss noch IDs vergeben!
        document.getElementById("bearbeitungszeitraum").addEventListener("input", function() {
            // Neue Anzahl Wochen einlesen und die ausgewählten Mitarbeiter:
            var neue = parseInt(this.value);
            var anzahl_mitarbeiter = [...document.getElementById("select_mitarbeiter_ids").selectedOptions];
            // testen, ob der Wert auch eine Zahl ist!
            if (isNaN(neue)) { return; }

            // Eigentlich an Tabelle anfügen bzw. kürzen
            // Zu viel Aufwand, daher Tabelle einfach löschen und neu generieren (nicht optimal)
            var zuordnung_arbeit = document.getElementById("zuordnung_arbeit");
            while (zuordnung_arbeit.firstChild) {
                zuordnung_arbeit.removeChild(zuordnung_arbeit.firstChild);
            }

            // 1) Überschriften
            var header = document.createElement("tr");
            var header_id = document.createElement("th");
            header_id.innerText = "Id / Woche";
            header.appendChild(header_id);
            for (var i=1; i<neue+1; i++) {
                var week_n = document.createElement("th");
                week_n.innerText = "Woche " + i.toString();
                header.appendChild(week_n);
            }
            zuordnung_arbeit.appendChild(header);

            // 2) für jeden Mitarbeiter
            for (var i=0; i<anzahl_mitarbeiter.length; i++) {
                var data_row = document.createElement("tr");
                var name = document.createElement("td");
                name.innerText = anzahl_mitarbeiter[i].value;
                data_row.appendChild(name);

                for (var j = 0; j < neue; j++) {
                    var week_n = document.createElement("th");
                    var week_n_input = document.createElement("input");
                    week_n_input.setAttribute("class", "mitarbeiter_wochenstunden");
                    week_n.appendChild(week_n_input);
                    data_row.appendChild(week_n);
                }

                zuordnung_arbeit.appendChild(data_row);
            }
        });


        // 5) Select-Event-Listener hinzufuegen (Mitarbeiter)
        document.getElementById("select_mitarbeiter_ids").addEventListener("click", function() {
            // Neue Anzahl Wochen einlesen und die ausgewählten Mitarbeiter:
            var neue = parseInt(document.getElementById("bearbeitungszeitraum").value);
            var anzahl_mitarbeiter = [...this.selectedOptions];
            // testen, ob der Wert auch eine Zahl ist!
            if (isNaN(neue)) { return; }

            // Eigentlich an Tabelle anfügen bzw. kürzen
            // Zu viel Aufwand, daher Tabelle einfach löschen und neu generieren (nicht optimal)
            var zuordnung_arbeit = document.getElementById("zuordnung_arbeit");
            while (zuordnung_arbeit.firstChild) {
                zuordnung_arbeit.removeChild(zuordnung_arbeit.firstChild);
            }

            // 1) Überschriften
            var header = document.createElement("tr");
            var header_id = document.createElement("th");
            header_id.innerText = "Id / Woche";
            header.appendChild(header_id);
            for (var i=1; i<neue+1; i++) {
                var week_n = document.createElement("th");
                week_n.innerText = "Woche " + i.toString();
                header.appendChild(week_n);
            }
            zuordnung_arbeit.appendChild(header);

            // 2) für jeden Mitarbeiter
            for (var i=0; i<anzahl_mitarbeiter.length; i++) {
                var data_row = document.createElement("tr");
                var name = document.createElement("td");
                name.innerText = anzahl_mitarbeiter[i].value;
                data_row.appendChild(name);

                for (var j = 0; j < neue; j++) {
                    var week_n = document.createElement("th");
                    var week_n_input = document.createElement("input");
                    week_n_input.setAttribute("type", "number");
                    week_n_input.setAttribute("class", "mitarbeiter_wochenstunden");
                    week_n.appendChild(week_n_input);
                    data_row.appendChild(week_n);
                }

                zuordnung_arbeit.appendChild(data_row);
            }
        });


        // 6) "Speichern" gedrückt
        /*
        document.getElementById("btn--save").addEventListener("click", function() {
            if (confirm("Wollen sie das Element wirklich editieren?")) {
                // Input-Felder auf Richtigkeit überprüfen macht das Backend
                var header = [...document.getElementsByClassName("tbl--header--info")];
                var inputs = [...document.getElementsByClassName("input--data")];

                var request = {
                    "link" : link,
                    "token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
                    "data" : {}
                };

                for (var i = 0; i < inputs.length; i++) {
                    request["data"][header[i].innerHTML] = inputs[i].value;
                }

                // POST absetzen mit den geänderten Daten
                var http = new XMLHttpRequest();
                http.open("POST", "/api/update");
                http.setRequestHeader("Content-Type", "application/json");
                http.onload = function() {
                    console.log(this.responseText);
                    var rueckgabe = JSON.parse(this.responseText);
                    var h2_failure = document.querySelector(".h2--failure");
                    if (rueckgabe["code"] != 200) {
                        h2_failure.innerHTML = "Fehlermeldung Code: " + rueckgabe["code"];
                    } else {
                        h2_failure.innerHTML = "Update erfolgreich!";
                    }
                    if (!offen) {
                        div_failure.style.setProperty("max-height", "var(--max-height)");
                        offen = !offen;
                    }
                };

                http.send(JSON.stringify(request));
            }
        });*/
    };
})();

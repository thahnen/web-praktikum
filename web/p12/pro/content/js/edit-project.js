'use strict';

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

import {
    loadJSONData, hide_failure, set_title_headline,
    edit_event_handler, input_event_handler, zuordnung_event_handler
} from "./lib.js";

(function () {
    let offen = false;

    window.onload = function () {
        // 1) Eigenschaften setzen
        // 1.1) Verbergen der Fehlermeldung
        let div_failure = hide_failure();

        // 1.2) Titel und Header richtig setzen
        let link = set_title_headline();

        // Kunden laden und ins designierte Feld eintragen
        let kunden_select = document.getElementById("select_kunden_id");
        let bereits_kunde = kunden_select.firstElementChild;
        let kunden = loadJSONData("Kundendaten");
        for (let kunde in kunden) {
            if (parseInt(bereits_kunde.value) == parseInt(kunden[kunde].unique_id)) {
                // Bereits bestehde Kunden abändern
                bereits_kunde.innerHTML = "(" + kunden[kunde].unique_id + ") " + kunden[kunde].ansprechpartner;
                bereits_kunde.selected = true;
            } else {
                let option = document.createElement("option");
                option.setAttribute("value", parseInt(kunden[kunde].unique_id));
                option.appendChild(
                    document.createTextNode("(" + kunden[kunde].unique_id + ") " + kunden[kunde].ansprechpartner)
                );
                kunden_select.appendChild(option);
            }
        }

        // Mitarbeiter laden und ins designierte Feld eintragen
        let mitarbeiter_select = document.getElementById("select_mitarbeiter_ids");
        let bereits_mitarbeiter = [...mitarbeiter_select.children];
        let mitarbeiter = loadJSONData("Mitarbeiterdaten");
        for (let arbeiter in mitarbeiter) {
            let found = false;
            bereits_mitarbeiter.forEach((x) => {
                // Bereits bestehde Mitarbeiter abändern
                if (parseInt(mitarbeiter[arbeiter].unique_id) == parseInt(x.value)) {
                    x.innerHTML = "(" + mitarbeiter[arbeiter].unique_id + ") " + mitarbeiter[arbeiter].vorname + " " + mitarbeiter[arbeiter].name;
                    found = true;
                }
            });
            if (!found) {
                let option = document.createElement("option");
                option.setAttribute("value", parseInt(mitarbeiter[arbeiter].unique_id));
                option.appendChild(
                    document.createTextNode("(" + mitarbeiter[arbeiter].unique_id + ") " + mitarbeiter[arbeiter].vorname + " " + mitarbeiter[arbeiter].name)
                );
                mitarbeiter_select.appendChild(option);
            }
        }

        // 2) "Editieren" gedrückt
        edit_event_handler(div_failure, offen);

        // 3) Input-Event-Listener hinzufügen
        input_event_handler(div_failure, offen, true);

        // 4) Input-Event-Listener hinzufuegen (Bearbeitungszeitraum)
        // 5) Select-Event-Listener hinzufuegen (Mitarbeiter)
        zuordnung_event_handler();

        // 6) "Speichern" gedrückt
        document.getElementById("btn--save").addEventListener("click", function () {
            if (confirm("Wollen sie das Element wirklich editieren?")) {

                // Alle Eingabemöglichkeiten mit ID belegen
                let unique_id = parseInt(document.getElementById("unique_id").value);
                let nummer = parseInt(document.getElementById("nummer").value);
                let bezeichnung = document.getElementById("bezeichnung").value;
                let beschreibung = document.getElementById("beschreibung").value;
                let bearbeitungszeitraum = parseInt(document.getElementById("bearbeitungszeitraum").value);
                let budget = parseInt(document.getElementById("budget").value);
                if (nummer == null || isNaN(nummer) || bezeichnung == null || beschreibung == null
                    || bearbeitungszeitraum == null || isNaN(bearbeitungszeitraum)
                    || budget == null || isNaN(budget)) {
                    alert("Irgendwelche Eingaben fehlerhaft");
                    return;
                }
                let kunden_id;
                try {
                    kunden_id = parseInt([...document.getElementById("select_kunden_id").selectedOptions][0].value);
                } catch (e) {
                    alert("kunden_id nicht ausgewählt");
                    return;
                }
                let mitarbeiter_ids = [...document.getElementById("select_mitarbeiter_ids").selectedOptions].map(x => parseInt(x.value));
                if (mitarbeiter_ids.length == 0) {
                    alert("mitarbeiter_ids nicht ausgewählt");
                    return;
                }
                let zuordnung_arbeit = {};
                let stunden = [...document.getElementsByClassName("mitarbeiter_wochenstunden")].map(x => parseInt(x.value));
                for (let x = 0; x < stunden.length; x++) {
                    if (stunden[x] == null || isNaN(stunden[x])) {
                        alert("Zuordnung der Arbeit nicht richtig ausgefüllt!");
                        return;
                    }
                }

                let anz_mit = mitarbeiter_ids.length;
                for (let i = 0; i < anz_mit; i++) {
                    let stunden_liste = [];
                    for (let j = i*bearbeitungszeitraum; j < (i+1)*bearbeitungszeitraum; j++) {
                        stunden_liste.push(stunden[j]);
                    }
                    zuordnung_arbeit[mitarbeiter_ids[i].toString()] = stunden_liste;
                }

                // Der Request, der mit Daten vollgepackt wird
                let request = {
                    "link" : link,
                    "token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
                    "data" : {
                        "unique_id" : unique_id,
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

                // POST absetzen mit den geänderten Daten
                let http = new XMLHttpRequest();
                http.open("POST", "/api/update");
                http.setRequestHeader("Content-Type", "application/json");
                http.onload = function () {
                    let rueckgabe = JSON.parse(this.responseText);
                    let h2_failure = document.querySelector(".h2--failure");
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
        });
    };
})();

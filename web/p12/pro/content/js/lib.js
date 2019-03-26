'use strict';

/*
 *  lib.js
 *  ======
 *
 *  Eigene Bibliothek mit allen Funktionen, die in diversen Skripten aufgerufen werden!
 *  Es darf ja kein jQuery oder so genutzt werden. Mimimi.
 *
 *  1) loadJSONData(datensatz):
 *  => Läd JSON-Daten synchron vom Web-Server zur Weiterverarbeitung
 *
 *  2) hide_failure():
 *  => Versteckt das Fehler-Div und gibt es als Objekt zurück
 *
 *  3) set_title_headline():
 *  => Füllt den Titel und die Überschrift mit dem Seitennamen auf
 *
 *  4) edit_event_handler(div_failure, offen):
 *  => Event-Handler, um deaktivierte Eingaben zu bearbeiten
 *
 *  5) input_event_handler(div_failure, offen, disabled):
 *  => Event-Handler für Input-Felder und ob sie deaktiviert werden sollen
 *
 *  6) zuordnung_event_handler():
 *  => Event-Handler für alle Elemente, bei deren Änderung die Zuordnung neugeneriert werden muss
*/

// Hilfsfunktion um JSON von Server synchron(!) zu laden
export function loadJSONData(datensatz) {
    let rueckgabe;
    let http = new XMLHttpRequest();
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
    console.log("DEBUG: loadJSONData");
    return rueckgabe["data"]["Elements"];
}

// Verbergen der Fehlermeldung
export function hide_failure() {
    let div = document.querySelector(".div--failure");
    div.style.setProperty("--max-height", div.scrollHeight + "px");
    console.log("DEBUG: hide_failure");
    return div;
}

// Titel und Headline setzen
export function set_title_headline() {
    let link = window.location.href.split("/")[3].split("?")[0];
    link = link.charAt(0).toUpperCase() + link.slice(1);
    document.title = link + document.title;
    let headline = document.getElementById("headline");
    headline.innerHTML = link + headline.innerHTML;
    console.log("DEBUG: set_title_headline");
    return link;
}

// "Editieren"-Event-Handler
export function edit_event_handler(div_failure, offen) {
    document.getElementById("btn--edit").addEventListener("click", function () {
        [...document.getElementsByClassName("input--edit")].forEach((x) => {
            x.disabled = false;
            if (offen) {
                div_failure.style.removeProperty("max-height", "var(--max-height)");
                offen = !offen;
            }
        });
    });
    console.log("DEBUG: edit_event_handler");
}

// Input-Event-Handler
export function input_event_handler(div_failure, offen, disabled) {
    [...document.getElementsByClassName("input--data")].forEach((x) => {
        x.addEventListener("click", function () {
            if (offen) {
                div_failure.style.removeProperty("max-height", "var(--max-height)");
                offen = !offen;
            }
        });
        x.disabled = disabled;
    });
    console.log("DEBUG: input_event_handler");
}

// Event-Handler (Bearbeitungszeitraum + Mitarbeiter-Auswahl)
export function zuordnung_event_handler() {
    document.getElementById("bearbeitungszeitraum").addEventListener("input", function () {
        let neue = parseInt(this.value);
        let anzahl_mitarbeiter = [...document.getElementById("select_mitarbeiter_ids").selectedOptions];
        generate_zuordnung(neue, anzahl_mitarbeiter);
    });

    document.getElementById("select_mitarbeiter_ids").addEventListener("click", function () {
        let neue = parseInt(document.getElementById("bearbeitungszeitraum").value);
        let anzahl_mitarbeiter = [...this.selectedOptions];
        generate_zuordnung(neue, anzahl_mitarbeiter);
    });
}

// Zuordnung der Arbeit/ Wochenstunden generieren (nicht exportiert)
function generate_zuordnung(neue, anzahl_mitarbeiter) {
    if (isNaN(neue)) return;
    // An Tabelle anfügen zu viel Aufwand, daher einfach neu generieren (nicht optimal)
    let zuordnung_arbeit = document.getElementById("zuordnung_arbeit");
    while (zuordnung_arbeit.firstChild) {
        zuordnung_arbeit.removeChild(zuordnung_arbeit.firstChild);
    }
    let header = document.createElement("tr");
    let header_id = document.createElement("th");
    header_id.innerText = "Id / Woche";
    header.appendChild(header_id);
    for (let i=1; i<neue+1; i++) {
        let week_n = document.createElement("th");
        week_n.innerText = "Woche " + i.toString();
        header.appendChild(week_n);
    }
    zuordnung_arbeit.appendChild(header);
    for (let i=0; i<anzahl_mitarbeiter.length; i++) {
        let data_row = document.createElement("tr");
        let name = document.createElement("td");
        name.innerText = anzahl_mitarbeiter[i].value;
        data_row.appendChild(name);
        for (let j = 0; j < neue; j++) {
            let week_n = document.createElement("th");
            let week_n_input = document.createElement("input");
            week_n_input.setAttribute("type", "number");
            week_n_input.setAttribute("class", "mitarbeiter_wochenstunden");
            week_n.appendChild(week_n_input);
            data_row.appendChild(week_n);
        }
        zuordnung_arbeit.appendChild(data_row);
    }
    console.log("DEBUG: generate_zuordnung");
}

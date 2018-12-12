'use strict';

/*
 *  view.js
 *  =======
 *
 *  Logik für alle Seiten, auf denen man ausgewählte
 *  - Projektdaten
 *  - Kundendaten,
 *  - Mitarbeiterdaten
 *  ansehen und löschen kann.
 *
 *  1. Eigenschaften setzen:
 *  => Verbergen der Fehlermeldung
 *  => Titel und Header richtig setzen
 *  => "Eintrag editieren" und "Eintrag löschen" disablen
 *
 *  2. Table-Row-Event-Listener hinzufügen
 *  => onClick:
 *      Verbergen der Fehlermeldung
 *      Als ausgewählt speichern (u.a. Farbe ändern oder so)
 *      "Eintrag editieren" und "Eintrag löschen" enablen
 *
 *  3. "Neu Hinzufügen" gedrückt:
 *  => Seite wechseln zu: /<...>/neu
 *
 *  4. "Eintrag editieren" gedrückt:
 *  => Irgendein Eintrag ausgewählt?
 *  => Seite wechseln zu: /<...>/<..._id>
 *
 *  5. "Eintrag löschen" gedrückt:
 *  => Irgendein Eintrag ausgewählt?
 *  => XMLHttpRequest an /api/delete mit Löschen-Auftrag!
 *
*/

import { hide_failure, set_title_headline } from "./lib.js";

(function () {
    let offen = false;
    let highlighted_entry = null;

    window.onload = function () {
        // 1. Eigenschaften setzen
        // 1.1) Verbergen der möglichen Fehlermeldung!
        let div_failure = hide_failure();

        // 1.2) Titel und Header richtig setzen
        let link = set_title_headline();

        // 1.3) Eintrag editieren" und "Eintrag löschen" disablen
        document.getElementById("btn--edit").disabled = true;
        document.getElementById("btn--delete").disabled = true;


        // 2. Input-Event-Listener hinzufügen
        [...document.getElementsByClassName("tbl--data")].forEach((x) => {
            x.addEventListener("click", function () {
                if (offen) {
                    div_failure.style.removeProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }

                // Überprüfen ob bereits markiertes erneut ausgewählt wurde
                if (highlighted_entry == x) {
                    x.style.removeProperty("background-color", "lightblue");
                    highlighted_entry = null;
                    document.getElementById("btn--edit").disabled = true;
                    document.getElementById("btn--delete").disabled = true;
                    return;
                }

                // (Alte markierte) CSS entfernen
                if (highlighted_entry != null) {
                    highlighted_entry.style.removeProperty("background-color", "lightblue");
                }

                highlighted_entry = x;
                x.style.setProperty("background-color", "lightblue");
                document.getElementById("btn--edit").disabled = false;
                document.getElementById("btn--delete").disabled = false;
            });
        });


        // 3. "Neues Element hinzufügen" gedrückt
        document.getElementById("btn--new").addEventListener("click", function () {
            window.location.href += "/neu";
        });


        // 4. "Eintrag editieren" gedrückt
        document.getElementById("btn--edit").addEventListener("click", function () {
            window.location.href += "/" + highlighted_entry.firstElementChild.innerHTML;
        });


        // 5. "Eintrag löschen" gedrückt
        document.getElementById("btn--delete").addEventListener("click", function () {
            if (confirm("Wollen sie das Element wirklich löschen?")) {
                let unique_id = parseInt(highlighted_entry.firstElementChild.innerHTML);

                let request = {
                    "link" : link,
                    "token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
                    "data" : unique_id
                };

                // POST absetzen zum löschen!
                let http = new XMLHttpRequest();
                http.open("POST", "/api/delete");
                http.setRequestHeader("Content-Type", "application/json");
                http.onload = function () {
                    let rueckgabe = JSON.parse(this.responseText);
                    let h2_failure = document.querySelector(".h2--failure");
                    if (rueckgabe["code"] != 200) {
                        h2_failure.innerHTML = "Fehlermeldung Code: " + rueckgabe["code"];
                    } else {
                        h2_failure.innerHTML = "Loeschen erfolgreich!";
                        // Nachdem es erfolgreich war: Element auch aus Tabelle löschen!
                        highlighted_entry.remove();
                        highlighted_entry = null;
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

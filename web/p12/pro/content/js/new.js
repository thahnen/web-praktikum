'use strict';

/*
 *  new.js
 *  ======
 *
 *  Logik für alle Seiten, auf denen man ausgewählte
 *  - Kundendaten,
 *  - Mitarbeiterdaten
 *  neu hinzufügen kann.
 *
 *  1) Eigenschaften setzen:
 *  => Verbergen der Fehlermeldung
 *  => Titel und Header richtig setzen
 *
 *  2) Input-Event-Listener hinzufügen
 *  => onClick: Verbergen der Fehlermeldung
 *
 *  3) "Hinzufügen" gedrückt:
 *  => alle Input-Felder mit gleicher Klasse "un-disablen"
*/

import {
    hide_failure, set_title_headline, input_event_handler
} from "./lib.js";

(function () {
    let offen = false;

    window.onload = function () {
        // 1) Eigenschaften setzen
        // 1.1) Verbergen der Fehlermeldung
        let div_failure = hide_failure();

        // 1.2) Titel und Header richtig setzen
        let link = set_title_headline();


        // 2) Input-Event-Listener hinzufügen
        input_event_handler(div_failure, offen, false);


        // 4) "Hinzufuegen" gedrückt
        document.getElementById("btn--new").addEventListener("click", function () {
            if (confirm("Wollen sie das Element wirklich hinzufuegen?")) {
                // Input-Felder auf Richtigkeit überprüfen macht das Backend
                let header = [...document.getElementsByClassName("tbl--header--info")];
                let inputs = [...document.getElementsByClassName("input--data")];

                let request = {
                    "link" : link,
                    "token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
                    "data" : {}
                };

                for (let i = 0; i < inputs.length; i++) {
                    request["data"][header[i].innerHTML] = inputs[i].value;
                }

                // POST absetzen mit den neuen Daten
                let http = new XMLHttpRequest();
                http.open("POST", "/api/new");
                http.setRequestHeader("Content-Type", "application/json");
                http.onload = function () {
                    let rueckgabe = JSON.parse(this.responseText);
                    let h2_failure = document.querySelector(".h2--failure");
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
        });
    }
})();

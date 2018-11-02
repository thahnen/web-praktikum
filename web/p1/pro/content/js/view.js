/*
 *  view.js
 *  =======
 *
 *  Logik für alle Seiten, auf denen man ausgewählte
 *  - Projektdaten,
 *  - Kundendaten,
 *  - Mitarbeiterdaten
 *  ansehen und Neue hinzufügen kann (NICHT bearbeiten).
 *
 *  1. Eigenschaften setzen:
 *  => Verbergen des "Neu-Hinzufügen-Divs"
 *  => Verbergen der Fehlermeldung
 *
 *  2. "Hinzufügen" gedrückt:
 *  => Eingaben überprüfen und abspeichern
 *  => unique_id durch base64 generieren!
 *  => Rückgabe vom Webserver verarbeiten!
*/

(function () {
    window.onload = function () {
        // 1. Eigenschaften setzen
        // Verbergen der möglichen Fehlermeldung!
        var new_elem = document.querySelector(".div--new");
        new_elem.style.setProperty("--max-height", new_elem.scrollHeight + "px");

        // 2. "Neues Element hinzufügen" gedrückt
        document.getElementById("p--new").addEventListener("click", function() {
            new_elem.style.setProperty("max-height", "var(--max-height)");
        });

        // 3. "Hinzufügen" gedrückt
        document.getElementById("btn--new").addEventListener("click", function() {
            console.log("Create");

            // Alle Inputs in JSON packen
            [...document.getElementsByClassName("input--data")].map((x) => {
                console.log("Noch zum JSON hinzufügen");
                //x.disabled = false;
            });
        });
    };
})();

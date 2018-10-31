/*
 *  edit.js
 *  =======
 *
 *  Logik für alle Seiten, auf denen man ausgewählte
 *  - Projektdaten,
 *  - Kundendaten,
 *  - Mitarbeiterdaten
 *  bearbeiten und speichern kann.
 *
 *  1. Eigenschaften setzen:
 *  => Verbergen der Fehlermeldung
 *
 *  2. "Editieren" gedrückt:
 *  => alle Input-Felder mit gleicher Klasse "un-disablen"
 *  => immer wenn "un-focussed" Wert auf Richtigkeit überprüfen?
 *
 *  3. "Speichern" gedrückt:
 *  => überprüfen ob Input-Felder leer?
 *  => XMLHttpRequest absetzen und auf Antwort warten und reagieren
*/

(function () {
    window.onload = function () {
        // 1. Eigenschaften setzen
        // Verbergen der möglichen Fehlermeldung!
        var failure = document.querySelector(".div--failure");
        failure.style.setProperty("--max-height", failure.scrollHeight + "px");


        // 2. "Editieren" gedrückt
        document.getElementById("btn--edit").addEventListener("click", function() {
            console.log("Edit");

            // Alle Inputs zum bearbeiten aktivieren
            [...document.getElementsByClassName("input--data")].map((x) => {
                x.disabled = false;
            });
        });


        // 3. "Speichern" gedrückt
        document.getElementById("btn--save").addEventListener("click", function() {
            console.log("Save");
            // Input-Felder auf Richtigkeit überprüfen

            // POST absetzen mit den geänderten Daten
            var http = new XMLHttpRequest();
            http.open("POST", "/update");
            http.setRequestHeader("Content-Type", "application/json");
            http.onload = function() {
                // Wenn es Daten zurückgibt, damit weiterarbeiten
                // Klappt aber auf jeden Fall!
                console.log(this.responseText);
                console.log(JSON.parse(this.responseText)["code"]);
            };

            // Kommt in JSON-Datei wenn alle das gleiche Template nutzen!
            var url_elem = (((window.location.href).split("/")).slice(-1)[0]).split("?")[0];

            http.send(JSON.stringify({name:"John Rambo", time:"2pm"}));

            // Fehlermeldung anzeigen!
            failure.style.setProperty("max-height", "var(--max-height)");
        });
    };
})();

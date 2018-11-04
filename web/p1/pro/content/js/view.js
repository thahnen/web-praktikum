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
 *  => Verbergen des "Neu-Hinzufügen"-Div
 *  => Verbergen der Fehlermeldung
 *
 *  2. Input-Event-Listener hinzufügen
 *  => onClick: Verbergen der Fehlermeldung
 *  => onInput:
 *      - Update der Unique-ID basierend auf allen Werten (kommt ggf später!)
 *      - "Neues Element Hinzufügen"-Button an-/ ausschalten
 *
 *  3. "Neues Element Hinzufügen" gedrückt:
 *  => Eingaben überprüfen und abspeichern
 *  => Rückgabe vom Webserver verarbeiten!
*/

var offen = false;

(function () {
    window.onload = function () {
        // 1. Eigenschaften setzen
        // Verbergen der möglichen Fehlermeldung!
        var div_failure = document.querySelector(".div--failure");
        div_failure.style.setProperty("--max-height", div_failure.scrollHeight + "px");

        // Jedem Link zu bestimmtem Kunden (etc) ein Editier-Icon geben
        // Geht auch im Template, aber dann sieht die HTML-Seite scheisse aus!
        [...document.getElementsByClassName("a--elem")].forEach((x) => {
            x.innerHTML = "&#x270D " + x.innerHTML;
        });


        // 2. Input-Event-Listener hinzufügen
        [...document.getElementsByClassName("input--new")].forEach((x) => {
            x.addEventListener("click", function() {
                if (offen) {
                    div_failure.style.removeProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }
            });
        });


        // 3. "Neues Element hinzufügen" gedrückt
        document.getElementById("btn--new").addEventListener("click", function() {
            if (offen) {
                div_failure.style.removeProperty("max-height", "var(--max-height)");
            } else {
                div_failure.style.setProperty("max-height", "var(--max-height)");
            }
            offen = !offen;
            [...document.getElementsByClassName("input--new")].map((x) => {
                console.log(x);
                //x.disabled = false;
            });
        });
    };
}());

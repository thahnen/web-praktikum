/*
 *  view.js
 *  =======
 *
 *  Logik für alle Seiten, auf denen man ausgewählte
 *  - Projektdaten,
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
 *  => XMLHttpRequest an /update mit Löschen-Auftrag!
 *
*/

var offen = false;
var highlighted_entry = null;

(function () {
    window.onload = function () {
        // 1. Eigenschaften setzen
        // Verbergen der möglichen Fehlermeldung!
        var div_failure = document.querySelector(".div--failure");
        div_failure.style.setProperty("--max-height", div_failure.scrollHeight + "px");

        // 1.2) Titel und Header richtig setzen
        // var link = window.location.href.split("/").slice(-2)[0].split("?")[0]
        var link = window.location.href.split("/")[3].split("?")[0];
        link = link.charAt(0).toUpperCase() + link.slice(1);
        document.title = link + document.title;
        var headline = document.getElementById("headline");
        headline.innerHTML = link + headline.innerHTML;

        // 1.3) Eintrag editieren" und "Eintrag löschen" disablen
        document.getElementById("btn--edit").disabled = true;
        document.getElementById("btn--delete").disabled = true;


        // 2. Input-Event-Listener hinzufügen
        [...document.getElementsByClassName("tbl--data")].forEach((x) => {
            x.addEventListener("click", function() {
                // Fehlermeldung entfernen
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

                    return
                }

                // (Alte markierte) CSS entfernen
                if (highlighted_entry != null) {
                    highlighted_entry.style.removeProperty("background-color", "lightblue");
                }

                // Ausgewählte Reihe abspeichern
                highlighted_entry = x;

                // (Neu markierte) mit CSS als markiert anzeigen
                x.style.setProperty("background-color", "lightblue");

                // "Eintrag editieren" und "Eintrag löschen" freigeben
                document.getElementById("btn--edit").disabled = false;
                document.getElementById("btn--delete").disabled = false;
            });
        });


        // 3. "Neues Element hinzufügen" gedrückt
        document.getElementById("btn--new").addEventListener("click", function() {
            window.location.href += "/neu";
        });


        // 4. "Eintrag editieren" gedrückt
        document.getElementById("btn--edit").addEventListener("click", function() {
            window.location.href += "/" + highlighted_entry.firstElementChild.innerHTML;
        });


        // 5. "Eintrag löschen" gedrückt
        document.getElementById("btn--delete").addEventListener("click", function() {
            // XMLHttpRequest und so weiter
        });
    };
}());

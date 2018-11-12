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
 *  1) Eigenschaften setzen:
 *  => Verbergen der Fehlermeldung
 *  => Titel und Header richtig setzen
 *
 *  2) "Editieren" gedrückt:
 *  => alle Input-Felder mit gleicher Klasse "un-disablen"
 *  => immer wenn "un-focussed" Wert auf Richtigkeit überprüfen?
 *
 *  3) Input-Event-Listener hinzufügen
 *  => onClick: Verbergen der Fehlermeldung
 *  => onInput:
 *      - Update der Unique-ID basierend auf allen Werten (kommt ggf später!)
 *      - "Neues Element Hinzufügen"-Button an-/ ausschalten
 *  => alle Inputs deaktivieren
 *
 *  4) "Speichern" gedrückt:
 *  => überprüfen ob Input-Felder leer?
 *  => XMLHttpRequest absetzen und auf Antwort warten und reagieren
*/

// TODO: Unique_id soll nicht änderbar sein! Auch in HTML ändern!

(function () {
    window.onload = function () {
        // 1) Eigenschaften setzen
        // 1.1) Verbergen der Fehlermeldung
        var failure = document.querySelector(".div--failure");
        failure.style.setProperty("--max-height", failure.scrollHeight + "px");
        var offen = false;

        // 1.2) Titel und Header richtig setzen
        // var link = window.location.href.split("/").slice(-2)[0].split("?")[0]
        var link = window.location.href.split("/")[3].split("?")[0];
        link = link.charAt(0).toUpperCase() + link.slice(1);
        document.title = link + ": " + document.title;
        var headline = document.getElementById("headline");
        headline.innerHTML = link + ": " + headline.innerHTML;


        // 2) "Editieren" gedrückt
        document.getElementById("btn--edit").addEventListener("click", function() {
            // Alle Inputs zum bearbeiten aktivieren
            [...document.getElementsByClassName("input--data")].forEach((x) => {
                x.disabled = false;
                if (offen) {
                    failure.style.removeProperty("max-height", "var(--max-height)");
                }
            });
        });


        // 3) Input-Event-Listener hinzufügen
        [...document.getElementsByClassName("input--data")].forEach((x) => {
            // 3.1) onClick-Event-Listener
            x.addEventListener("click", function() {
                if (offen) {
                    failure.style.removeProperty("max-height", "var(--max-height)");
                }
            });

            // 3.2) onInput-Event-Listener
            x.addEventListener("input", function() {
                console.log("Noch nichts");
            })

            // 3.3) Alle Inputs deaktivieren
            x.disabled = true;
        });


        // 4) "Speichern" gedrückt
        document.getElementById("btn--save").addEventListener("click", function() {
            // Input-Felder auf Richtigkeit überprüfen macht das Backend
            var header = [...document.getElementsByClassName("tbl--header--info")];
            var inputs = [...document.getElementsByClassName("input--data")];

            var request = {
                "link" : link,
                "method" : "edit",
                "data" : {}
            };

            for (var i = 0; i < inputs.length; i++) {
                request["data"][header[i].innerHTML] = inputs[i].value;
            }

            // DEBUG
            console.log(JSON.stringify(request));

            // POST absetzen mit den geänderten Daten
            var http = new XMLHttpRequest();
            http.open("POST", "/update");
            http.setRequestHeader("Content-Type", "application/json");
            http.onload = function() {
                // Wenn es Daten zurückgibt, damit weiterarbeiten
                // Klappt aber auf jeden Fall!
                var rueckgabe = JSON.parse(this.responseText);
                var header_failure = document.getElementById("header--failure");
                if (rueckgabe["code"] != 200) {
                    header_failure.innerHTML = "Fehlermeldung Code: " + rueckgabe["code"];
                } else {
                    header_failure.innerHTML = "Update erfolgreich!";
                }
                if (!offen) {
                    failure.style.setProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }
            };

            http.send(JSON.stringify(request));
        });
    };
}());

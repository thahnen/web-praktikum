/*
 *  edit.js
 *  =======
 *
 *  Logik für alle Seiten, auf denen man ausgewählte
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
 *
 *  3) Input-Event-Listener hinzufügen
 *  => onClick: Verbergen der Fehlermeldung
 *  => alle Inputs deaktivieren (sonst wären sie bei Seitenaufruf editierbar!)
 *
 *  4) "Speichern" gedrückt:
 *  => überprüfen ob Input-Felder leer?
 *  => XMLHttpRequest absetzen und auf Antwort warten und reagieren
*/

(function () {
    'use strict';


    window.onload = function () {
        // 1) Eigenschaften setzen
        // 1.1) Verbergen der Fehlermeldung
        var div_failure = document.querySelector(".div--failure");
        div_failure.style.setProperty("--max-height", div_failure.scrollHeight + "px");
        var offen = false;

        // 1.2) Titel und Header richtig setzen
        var link = window.location.href.split("/")[3].split("?")[0];
        link = link.charAt(0).toUpperCase() + link.slice(1);
        document.title = link + ": " + document.title;
        var headline = document.getElementById("headline");
        headline.innerHTML = link + ": " + headline.innerHTML;


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


        // 4) "Speichern" gedrückt
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
                    // ggf statt innerHTML -> innerText nehmen?
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
        });
    };
})();

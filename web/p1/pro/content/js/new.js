/*
 *  new.js
 *  =======
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


(function() {
    window.onload = function() {
        // 1) Eigenschaften setzen
        // 1.1) Verbergen der Fehlermeldung
        var div_failure = document.querySelector(".div--failure");
        div_failure.style.setProperty("--max-height", div_failure.scrollHeight + "px");
        var offen = false;

        // 1.2) Titel und Header richtig setzen
        var link = window.location.href.split("/")[3].split("?")[0];
        link = link.charAt(0).toUpperCase() + link.slice(1);
        document.title = link + document.title;
        var headline = document.getElementById("headline");
        headline.innerHTML = link + headline.innerHTML;


        // 2) Input-Event-Listener hinzufügen
        [...document.getElementsByClassName("input--data")].forEach((x) => {
            // 2.1) onClick-Event-Listener
            x.addEventListener("click", function() {
                if (offen) {
                    div_failure.style.removeProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }
            });
        });


        // 4) "Hinzufuegen" gedrückt
        document.getElementById("btn--new").addEventListener("click", function() {
            if (confirm("Wollen sie das Element wirklich hinzufuegen?")) {
                // Input-Felder auf Richtigkeit überprüfen macht das Backend
                var header = [...document.getElementsByClassName("tbl--header--info")];
                var inputs = [...document.getElementsByClassName("input--data")];

                var request = {
                    "link" : link,
                    "token" : "d1e11080c2e0f77d9f0d98bed3d0c8ab5d0cf62024fba955e1d33f32f14437ad",
                    "data" : {}
                };

                for (var i = 0; i < inputs.length; i++) {
                    request["data"][header[i].innerHTML] = inputs[i].value;
                }

                // POST absetzen mit den neuen Daten
                var http = new XMLHttpRequest();
                http.open("POST", "/api/new");
                http.setRequestHeader("Content-Type", "application/json");
                http.onload = function() {
                    var rueckgabe = JSON.parse(this.responseText);
                    var h2_failure = document.querySelector(".h2--failure");
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

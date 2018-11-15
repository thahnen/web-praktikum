/*
 *  new.js
 *  =======
 *
 *  Logik für alle Seiten, auf denen man ausgewählte
 *  - Projektdaten,
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
 *  => alle Inputs deaktivieren (sonst wären sie bei Seitenaufruf editierbar!)
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
        // var link = window.location.href.split("/").slice(-2)[0].split("?")[0]
        var link = window.location.href.split("/")[3].split("?")[0];
        link = link.charAt(0).toUpperCase() + link.slice(1);
        document.title = link + ": " + document.title;
        var headline = document.getElementById("headline");
        headline.innerHTML = link + ": " + headline.innerHTML;


        // 2) Input-Event-Listener hinzufügen
        [...document.getElementsByClassName("input--data")].forEach((x) => {
            // 2.1) onClick-Event-Listener
            x.addEventListener("click", function() {
                if (offen) {
                    div_failure.style.removeProperty("max-height", "var(--max-height)");
                    offen = !offen;
                }
            });

            // 2.2) Alle Inputs deaktivieren (sonst wären sie bei Seitenaufruf editierbar!)
            x.disabled = true;
        });


        // 4) "Hinzufuegen" gedrückt
        document.getElementById("btn--add").addEventListener("click", function() {
            if (confirm("Wollen sie das Element wirklich hinzufuegen?")) {
                // Input-Felder auf Richtigkeit überprüfen macht das Backend
                var header = [...document.getElementsByClassName("tbl--header--info")];
                var inputs = [...document.getElementsByClassName("input--data")];

                var request = {
                    "link" : link,
                    "method" : "new",
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

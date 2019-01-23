'use strict';

// Nur bis das aufgeteilt ist als Default-Klasse!
export default class {
    constructor (name, template) {
        this.name = name;
        this.template = template;
        this.ausgewaehle_tabellenzeile = null; // immer ein HTML-Element

        // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
    }

    render () {
        // Daten anfordern
        //let path = "/qsmitarbeiter"
        let path = "/swentwickler";
        let requester = new APPUTIL.Requester();

        //console.log("[CategoryView] Request /qsmitarbeiter");
        console.log("[WorkerView] Request /swentwickler");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (var fehler in data) {
                if (data.hasOwnProperty(fehler)) {
                    context.push(data[fehler]);
                }
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element != null) {
                html_element.innerHTML = markup;
            }

            // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
            [...document.getElementsByClassName("tr--arbeiter")].forEach((x) => {
                x.addEventListener("click", function() {
                    console.log(this.ausgewaehle_tabellenzeile);
                    console.log(x);

                    // Überprüfen ob bereits markiertes erneut ausgewählt wurde
                    if (this.ausgewaehle_tabellenzeile == x) {
                        x.style.removeProperty("background-color", "lightblue");
                        this.ausgewaehle_tabellenzeile = null;
                        return;
                    }

                    // (Alte markierte) CSS entfernen
                    if (this.ausgewaehle_tabellenzeile != null) {
                        this.ausgewaehle_tabellenzeile.style.removeProperty("background-color", "lightblue");
                    }

                    this.ausgewaehle_tabellenzeile = x;
                    x.style.setProperty("background-color", "lightblue");
                }.bind(this)); // -> muss, da sonst mit "this" das falsche gemeint ist!

                document.getElementById("btn--arbeiter--edit").addEventListener("click", function() {
                    if (this.ausgewaehle_tabellenzeile != null) {
                        let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                        APPUTIL.eventService.publish("app.cmd", ["arbeiter--edit", id]);
                    } else {
                        alert("Kein Arbeiter ausgewaehlt!")
                    }
                }.bind(this));

                document.getElementById("btn--arbeiter--add").addEventListener("click", function() {
                    APPUTIL.eventService.publish("app.cmd", ["arbeiter--add", null]);
                });
            });
        }.bind(this), function (response) {
            alert("[WorkerView] render->failed");
        });
    }
}

// Übersicht für QSM (Knöpfe: Bearbeiten + Hinzufügen)
export class QSMView {
    constructor () {
    }
}

// Übersicht für SWE (Knöpfe: Bearbeiten + Hinzufügen)
export class SWEView {
    constructor() {
    }
}

// Bearbeitung-Seite für QSM
export class QSMEditView {
    constructor() {
    }
}

// Bearbeitung-Seite für SWE
export class SWEEditView {
    constructor() {
    }
}

// Hinzufügen-Seite für QSM
export class QSMAddView {
    constructor() {
    }
}

// Hinzufügen-Seite für SWE
export class SWEAddView {
    constructor() {
    }
}

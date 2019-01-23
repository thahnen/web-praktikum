'use strict';

// Nur bis das aufgeteilt ist als Default-Klasse!
export default class {
    constructor (name, template) {
        this.name = name;
        this.template = template;
        this.ausgewaehle_tabellenzeile = null; // mit -> [...].id bekommt man die Id (td--<unique_id>)
    }

    render () {
        let path = "/fehler";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorView] render -> Request /fehler");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) {
                    context.push(data[fehler]);
                }
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) {
                alert("[ErrorView] render -> html_element=null")
            }
            html_element.innerHTML = markup;

            // EventHandler Tabellen-Zeilen jedes Mal aufs neue hinzufuegen
            [...document.getElementsByClassName("tr--fehler")].forEach((x) => {
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

                document.getElementById("btn--fehler--erkannt").addEventListener("click", function() {
                    APPUTIL.eventService.publish("app.cmd", ["fehler--erkannt", null]);
                });

                document.getElementById("btn--fehler--behoben").addEventListener("click", function() {
                    APPUTIL.eventService.publish("app.cmd", ["fehler--behoben", null]);
                });

                document.getElementById("btn--fehler--edit").addEventListener("click", function() {
                    if (this.ausgewaehle_tabellenzeile != null) {
                        let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                        APPUTIL.eventService.publish("app.cmd", ["fehler--edit", id]);
                    } else {
                        alert("Keinen Fehler ausgewaehlt!")
                    }
                }.bind(this));

                document.getElementById("btn--fehler--add").addEventListener("click", function() {
                    APPUTIL.eventService.publish("app.cmd", ["fehler--add", null]);
                });
            });
        }.bind(this), function (response) {
            alert("[ErrorView] render->failed");
        });
    }
}

// Übersicht für QSM (Knöpfe: Hinzufügen + Erkannt + Behoben)
export class ErrorQSMView {
    constructor () {
    }
}

// Übersicht für SWE (Knöpfe: Bearbeiten + Erkannt + Behoben)
export class ErrorSWEView {
    constructor() {
    }
}

// Übersicht aller erkannten Fehler
export class ErrorErkanntView {
    constructor() {
    }
}

// Übersicht aller behobenen Fehler
export class ErrorBehobenView {
    constructor() {
    }
}

// Bearbeitung-Seite für SWE
export class ErrorEditView {
    constructor() {
    }
}

// Hinzufügen-Seite für QSM
export class ErrorAddView {
    constructor() {
    }
}

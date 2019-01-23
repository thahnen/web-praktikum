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
        let path = "/komponente";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorView] Request /komponente");
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
            [...document.getElementsByClassName("tr--komponente")].forEach((x) => {
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

                document.getElementById("btn--komponente--sort").addEventListener("click", function() {
                    APPUTIL.eventService.publish("app.cmd", ["komponente--sort", null]);
                });

                document.getElementById("btn--komponente--edit").addEventListener("click", function() {
                    if (this.ausgewaehle_tabellenzeile != null) {
                        let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                        APPUTIL.eventService.publish("app.cmd", ["komponente--edit", id]);
                    } else {
                        alert("Keine Komponente ausgewaehlt!")
                    }
                }.bind(this));

                document.getElementById("btn--komponente--add").addEventListener("click", function() {
                    APPUTIL.eventService.publish("app.cmd", ["komponente--add", null]);
                });
            });
        }.bind(this), function (response) {
            alert("[ComponentView] render->failed");
        });
    }
}

// Übersicht für QSM (Knöpfe: KEINE)
export class ComponentQSMView {
    constructor () {
    }
}

// Übersicht für SWE (Knöpfe: Bearbeiten + Hinzufügen)
export class ComponentSWEView {
    constructor() {
    }
}

// Bearbeitung-Seite für SWE
export class ComponentEditView {
    constructor() {
    }
}

// Hinzufügen-Seite für SWE
export class ComponentAddView {
    constructor() {
    }
}

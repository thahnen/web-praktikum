'use strict';

// TODO: Wenn alles getan ist, alles noch zusammenfassen!

// Übersicht für QSM (Knöpfe: Hinzufügen + Erkannt + Behoben)
export class ErrorQSMView {
    constructor () {
        this.name = "main";
        this.template = "error.view-qsm.tpl";
    }

    render () {
        let path = "/fehler";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorQSMView] render -> Request /fehler");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ErrorQSMView] render -> html_element=null");
            html_element.innerHTML = markup;

            document.getElementById("btn--fehler--erkannt").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--erkannt", null]);
            });

            document.getElementById("btn--fehler--behoben").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--behoben", null]);
            });

            document.getElementById("btn--fehler--add").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--add", null]);
            });
        }.bind(this), function (response) { alert("[ErrorQSMView] render->failed"); });
    }
}


// Übersicht für SWE (Knöpfe: Bearbeiten + Erkannt + Behoben)
export class ErrorSWEView {
    constructor() {
        this.name = "main";
        this.template = "error.view-swe.tpl";
        this.ausgewaehle_tabellenzeile = null; // mit -> [...].id bekommt man die Id (td--<unique_id>)
    }

    render () {
        let path = "/fehler";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorSWEView] render -> Request /fehler");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ErrorSWEView] render -> html_element=null");
            html_element.innerHTML = markup;

            // EventHandler Tabellen-Zeilen jedes Mal aufs neue hinzufuegen
            [...document.getElementsByClassName("tr--fehler")].forEach((x) => {
                x.addEventListener("click", function() {
                    console.log(this.ausgewaehle_tabellenzeile);

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
                }.bind(this));
            });

            document.getElementById("btn--fehler--erkannt").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--erkannt", null]);
            });

            document.getElementById("btn--fehler--behoben").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--behoben", null]);
            });

            document.getElementById("btn--fehler--edit").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                    APPUTIL.eventService.publish("app.cmd", ["fehler--edit", id]);
                } else { alert("Keinen Fehler ausgewaehlt!") }
            }.bind(this));
        }.bind(this), function (response) { alert("[ErrorSWEView] render->failed"); });
    }
}


// Übersicht aller erkannten Fehler
export class ErrorErkanntView {
    constructor() {
        this.name = "main";
        this.template = "error.view-erkannt.tpl";
    }

    render () {
        let path = "/fehler/?type=erkannt";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorErkanntView] render -> Request /fehler/?type=erkannt");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ErrorErkanntView] render -> html_element=null");
            html_element.innerHTML = markup;

            document.getElementById("btn--fehler--back").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--back", null]);
            });
        }.bind(this), function (response) { alert("[ErrorErkanntView] render->failed"); });
    }
}


// Übersicht aller behobenen Fehler
export class ErrorBehobenView {
    constructor() {
        this.name = "main";
        this.template = "error.view-behoben.tpl";
    }

    render () {
        let path = "/fehler/?type=behoben";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorBehobenView] render -> Request /fehler/?type=behoben");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ErrorBehobenView] render -> html_element=null");
            html_element.innerHTML = markup;

            document.getElementById("btn--fehler--back").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--back", null]);
            });
        }.bind(this), function (response) { alert("[ErrorBehobenView] render->failed"); });
    }
}


// Bearbeitung-Seite für SWE
export class ErrorEditView {
    constructor() {
        this.name = "main";
        this.template = "error.edit.tpl";
    }

    render (id) {
        let path = "/fehler/" + id;
        let requester = new APPUTIL.Requester();

        console.log("[ErrorEditView] render -> Request /fehler/" + id);
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let markup = APPUTIL.templateManager.execute(this.template, data);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ErrorEditView] render -> html_element=null");
            html_element.innerHTML = markup;

            document.getElementById("btn--fehler--back").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["fehler--back", null]);
            });

            document.getElementById("btn--fehler--edit--save").addEventListener("click", function() {
                let unique_id = parseInt(document.getElementById("unique_id").value);
                let typ = document.getElementById("type").value;
                if (typ != "behoben") {
                    alert("Fehler wurde nicht behoben!")
                    return;
                }
                let komponente = parseInt(document.getElementById("komponente").value);
                let erkannt_beschreibung = document.getElementById("erkannt.beschreibung").value;
                let erkannt_bearbeiter = parseInt(document.getElementById("erkannt.bearbeiter").value);
                let erkannt_datum = document.getElementById("erkannt.datum").value;
                let erkannt_fehlerkategorien = document.getElementById("erkannt.fehlerkategorien").value.split(",");
                erkannt_fehlerkategorien.map((x) => parseInt(x));
                let beseitigt_beschreibung = document.getElementById("beseitigt.beschreibung").value;
                let beseitigt_bearbeiter = parseInt(document.getElementById("beseitigt.bearbeiter").value);
                let beseitigt_datum = document.getElementById("beseitigt.datum").value;
                let beseitigt_fehlerursachenkategorie = parseInt(document.getElementById("beseitigt.fehlerursachenkategorie").value);

                let put_data = {
                    "unique_id" : unique_id,
                    "type" : typ,
                    "komponente" : komponente,
                    "erkannt" : {
                        "beschreibung" : erkannt_beschreibung,
                        "bearbeiter" : erkannt_bearbeiter,
                        "datum" : erkannt_datum,
                        "fehlerkategorien" : erkannt_fehlerkategorien
                    },
                    "beseitigt" : {
                        "beschreibung" : beseitigt_beschreibung,
                        "bearbeiter" : beseitigt_bearbeiter,
                        "datum" : beseitigt_datum,
                        "fehlerursachenkategorie" : beseitigt_fehlerursachenkategorie
                    }
                };

                fetch("/fehler/" + id, {
                    method: "PUT",
                    headers : { "Content-Type" : "application/json" },
                    body : JSON.stringify(put_data)
                }).then(function (response) {
                    let rueckgabe = null;
                    if (response.ok) { // 200er-Status-Code
                        alert("[ErrorEditView] PUT hat funktioniert");
                        APPUTIL.eventService.publish("app.cmd", ["fehler--back", null]);
                    } else { alert("[ErrorEditView] PUT hat nicht funktioniert"); }
                    return rueckgabe;
                }).catch(function (error) {
                    console.log("[ErrorEditView] PUT-Problem: ", error.message);
                });
            });
        }.bind(this), function (response) { alert("[ErrorEditView] render->failed"); });
    }
}


// Hinzufügen-Seite für QSM
export class ErrorAddView {
    constructor() {
        this.name = "main";
        this.template = "error.add.tpl";
    }

    render () {
        let markup = APPUTIL.templateManager.execute(this.template, []);
        let html_element = document.querySelector(this.name);
        if (html_element == null) alert("[ErrorAddView] render -> html_element=null");
        html_element.innerHTML = markup;

        document.getElementById("btn--fehler--back").addEventListener("click", function() {
            APPUTIL.eventService.publish("app.cmd", ["fehler--back", null]);
        });

        document.getElementById("btn--fehler--add--add").addEventListener("click", function() {
            let erkannt_beschreibung = document.getElementById("erkannt.beschreibung").value;
            let erkannt_bearbeiter = parseInt(document.getElementById("erkannt.bearbeiter").value);
            let erkannt_datum = document.getElementById("erkannt.datum").value;
            let erkannt_fehlerkategorien = document.getElementById("erkannt.fehlerkategorien").value.split(",");
            erkannt_fehlerkategorien.map((x) => parseInt(x));
            let beseitigt_bearbeiter = parseInt(document.getElementById("beseitigt.bearbeiter").value);

            let post_data = {
                "unique_id" : parseInt(document.getElementById("unique_id").value),
                "type" : document.getElementById("type").value,
                "komponente" : parseInt(document.getElementById("komponente").value),
                "erkannt" : {
                    "beschreibung" : erkannt_beschreibung,
                    "bearbeiter" : erkannt_bearbeiter,
                    "datum" : erkannt_datum,
                    "fehlerkategorien" : erkannt_fehlerkategorien
                },
                "beseitigt" : {
                    "beschreibung" : "null",
                    "bearbeiter" : beseitigt_bearbeiter,
                    "datum" : "null",
                    "fehlerursachenkategorie" : 0
                }
            };

            fetch("/fehler/", {
                method: "POST",
                headers : { "Content-Type" : "application/json" },
                body : JSON.stringify(post_data)
            }).then(function (response) {
                let rueckgabe = null;
                if (response.ok) { // 200er-Status-Code
                    alert("[ErrorAddView] POST hat funktioniert");
                    APPUTIL.eventService.publish("app.cmd", ["fehler--back", null]);
                } else { alert("[ErrorAddView] POST hat nicht funktioniert"); }
                return rueckgabe;
            }).catch(function (error) {
                console.log("[ErrorAddView] POST-Problem: ", error.message);
            });
        });
    }
}

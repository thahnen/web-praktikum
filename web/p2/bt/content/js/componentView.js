'use strict';

// TODO: Wenn alles getan ist, alles noch zusammenfassen!

// Übersicht für QSM (Knöpfe: Nach Projekten sortiert)
export class ComponentQSMView {
    constructor () {
        this.name = "main";
        this.template = "component.view-qsm.tpl";
    }

    render () {
        let path = "/komponente";
        let requester = new APPUTIL.Requester();

        console.log("[ProjectQSMView] render -> Request /komponente");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ComponentQSMView] render -> html_element=null");
            html_element.innerHTML = markup;

            document.getElementById("btn--komponente--sort").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["komponente--sort", null]);
            });
        }.bind(this), function (response) { alert("[ComponentQSMView] render->failed"); });
    }
}

// Übersicht für SWE (Knöpfe: Nach Projekten sortiert + Bearbeiten + Hinzufügen)
export class ComponentSWEView {
    constructor () {
        this.name = "main";
        this.template = "component.view-swe.tpl";
        this.ausgewaehle_tabellenzeile = null; // mit -> [...].id bekommt man die Id (td--<unique_id>)
    }

    render () {
        // Daten anfordern
        let path = "/komponente";
        let requester = new APPUTIL.Requester();

        console.log("[ComponentSWEView] Request /komponente");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (var fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element != null) html_element.innerHTML = markup;

            // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
            [...document.getElementsByClassName("tr--komponente")].forEach((x) => {
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
                }.bind(this)); // -> muss, da sonst mit "this" das falsche gemeint ist!
            });

            document.getElementById("btn--komponente--edit").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                    APPUTIL.eventService.publish("app.cmd", ["komponente--edit", id]);
                } else { alert("Keine Komponente ausgewaehlt!") }
            }.bind(this));

            document.getElementById("btn--komponente--delete").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());

                    fetch("/komponente/" + id, {
                        method: "DELETE"
                    }).then(function (response) {
                        let rueckgabe = null;
                        if (response.ok) { // 200er-Status-Code
                            alert("[ComponentSWEView] DELETE hat funktioniert");
                            APPUTIL.eventService.publish("app.cmd", ["komponente--back", null]);
                        } else { alert("[ComponentSWEView] DELETE hat nicht funktioniert"); }
                        return rueckgabe;
                    }).catch(function (error) {
                        console.log("[ComponentSWEView] DELETE-Problem: ", error.message);
                    });
                } else { alert("Keine Fehlerkategorie zum loeschen ausgewaehlt!") }
            }.bind(this));

            document.getElementById("btn--komponente--add").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["komponente--add", null]);
            });
        }.bind(this), function (response) { alert("[ComponentSWEView] render->failed"); });
    }
}

// Komponenten nach Projekt sortiert
export class ComponentProjectView {
    constructor () {
        this.name = "main";
        this.template = "component.view-project.tpl";
    }

    render () { }
}

// Bearbeitung-Seite für SWE
export class ComponentEditView {
    constructor () {
        this.name = "main";
        this.template = "component.edit.tpl";
    }

    render (id) {
        let path = "/komponente/" + id;
        let requester = new APPUTIL.Requester();

        console.log("[ComponentEditView] render -> Request /komponente/" + id);
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let markup = APPUTIL.templateManager.execute(this.template, data);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ComponentEditView] render -> html_element=null");
            html_element.innerHTML = markup;

            document.getElementById("btn--komponente--back").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["komponente--back", null]);
            });

            document.getElementById("btn--komponente--edit--save").addEventListener("click", function() {
                let unique_id = parseInt(document.getElementById("unique_id").value);
                let fehler = document.getElementById("fehler").value.split(",");

                let put_data = {
                    "unique_id" : unique_id,
                    "fehler" : fehler
                };

                fetch("/komponente/" + id, {
                    method: "PUT",
                    headers : { "Content-Type" : "application/json" },
                    body : JSON.stringify(put_data)
                }).then(function (response) {
                    let rueckgabe = null;
                    if (response.ok) { // 200er-Status-Code
                        alert("[ComponentEditView] PUT hat funktioniert");
                        APPUTIL.eventService.publish("app.cmd", ["komponente--back", null]);
                    } else { alert("[ComponentEditView] PUT hat nicht funktioniert"); }
                    return rueckgabe;
                }).catch(function (error) {
                    console.log("[ComponentEditView] PUT-Problem: ", error.message);
                });
            });
        }.bind(this), function (response) { alert("[ComponentEditView] render->failed"); });
    }
}

// Hinzufügen-Seite für SWE
export class ComponentAddView {
    constructor () {
        this.name = "main";
        this.template = "component.add.tpl";
    }

    render () {
        let markup = APPUTIL.templateManager.execute(this.template, []);
        let html_element = document.querySelector(this.name);
        if (html_element == null) alert("[ComponentAddView] render -> html_element=null");
        html_element.innerHTML = markup;

        document.getElementById("btn--komponente--back").addEventListener("click", function() {
            APPUTIL.eventService.publish("app.cmd", ["komponente--back", null]);
        });

        document.getElementById("btn--komponente--add--add").addEventListener("click", function() {
            let project_id = parseInt(document.getElementById("project").value);
            let fehler = document.getElementById("fehler").value.split(",");

            let post_data = {
                "unique_id" : parseInt(document.getElementById("unique_id").value),
                "fehler" : fehler
            };

            fetch("/komponente/" + project_id, {
                method: "POST",
                headers : { "Content-Type" : "application/json" },
                body : JSON.stringify(post_data)
            }).then(function (response) {
                let rueckgabe = null;
                if (response.ok) { // 200er-Status-Code
                    alert("[ComponentAddView] POST hat funktioniert");
                    APPUTIL.eventService.publish("app.cmd", ["komponente--back", null]);
                } else { alert("[ComponentAddView] POST hat nicht funktioniert"); }
                return rueckgabe;
            }).catch(function (error) {
                console.log("[ComponentAddView] POST-Problem: ", error.message);
            });
        });
    }
}

'use strict';

// TODO: Wenn alles getan ist, alles noch zusammenfassen!

// Übersicht für QSM (Knöpfe: KEINE)
export class ProjectQSMView {
    constructor () {
        this.name = "main";
        this.template = "project.view-qsm.tpl";
    }

    render () {
        let path = "/projekt";
        let requester = new APPUTIL.Requester();

        console.log("[ProjectQSMView] render -> Request /projekt");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ProjectQSMView] render -> html_element=null");
            html_element.innerHTML = markup;

        }.bind(this), function (response) { alert("[ProjectQSMView] render->failed"); });
    }
}

// Übersicht für SWE (Knöpfe: Bearbeiten + Hinzufügen)
export class ProjectSWEView {
    constructor() {
        this.name = "main";
        this.template = "project.view-swe.tpl";
        this.ausgewaehle_tabellenzeile = null; // mit -> [...].id bekommt man die Id (td--<unique_id>)
    }

    render () {
        let path = "/projekt";
        let requester = new APPUTIL.Requester();

        console.log("[ProjectSWEView] render -> Request /projekt");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ProjectSWEView] render -> html_element=null");
            html_element.innerHTML = markup;

            // EventHandler Tabellen-Zeilen jedes Mal aufs neue hinzufuegen
            [...document.getElementsByClassName("tr--projekt")].forEach((x) => {
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
                }.bind(this));
            });

            document.getElementById("btn--projekt--edit").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                    APPUTIL.eventService.publish("app.cmd", ["projekt--edit", id]);
                } else { alert("Keinen Fehler ausgewaehlt!") }
            }.bind(this));

            document.getElementById("btn--projekt--delete").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());

                    fetch("/projekt/" + id, {
                        method: "DELETE"
                    }).then(function (response) {
                        let rueckgabe = null;
                        if (response.ok) { // 200er-Status-Code
                            alert("[ProjectSWEView] DELETE hat funktioniert");
                            APPUTIL.eventService.publish("app.cmd", ["projekt--back", null]);
                        } else { alert("[ProjectSWEView] DELETE hat nicht funktioniert"); }
                        return rueckgabe;
                    }).catch(function (error) {
                        console.log("[ProjectSWEView] DELETE-Problem: ", error.message);
                    });
                } else { alert("Keine Fehlerkategorie zum loeschen ausgewaehlt!") }
            }.bind(this));

            document.getElementById("btn--projekt--add").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["projekt--add", null]);
            });
        }.bind(this), function (response) { alert("[ProjectSWEView] render->failed"); });
    }
}

// Bearbeitung-Seite für SWE
export class ProjectEditView {
    constructor() {
        this.name = "main";
        this.template = "project.edit.tpl";
    }

    render (id) {
        let path = "/projekt/" + id;
        let requester = new APPUTIL.Requester();

        console.log("[ProjectEditView] render -> Request /project/" + id);
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let markup = APPUTIL.templateManager.execute(this.template, data);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ProjectEditView] render -> html_element=null");
            html_element.innerHTML = markup;

            document.getElementById("btn--projekt--back").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["projekt--back", null]);
            });

            document.getElementById("btn--projekt--edit--save").addEventListener("click", function() {
                let unique_id = parseInt(document.getElementById("unique_id").value);
                let komponenten = document.getElementById("komponenten").value.split(",");

                let put_data = {
                    "unique_id" : unique_id,
                    "komponenten" : komponenten
                };

                fetch("/projekt/" + id, {
                    method: "PUT",
                    headers : { "Content-Type" : "application/json" },
                    body : JSON.stringify(put_data)
                }).then(function (response) {
                    let rueckgabe = null;
                    if (response.ok) { // 200er-Status-Code
                        alert("[ProjectEditView] PUT hat funktioniert");
                        APPUTIL.eventService.publish("app.cmd", ["projekt--back", null]);
                    } else { alert("[ProjectEditView] PUT hat nicht funktioniert"); }
                    return rueckgabe;
                }).catch(function (error) {
                    console.log("[ProjectEditView] PUT-Problem: ", error.message);
                });
            });
        }.bind(this), function (response) {
            alert("[ProjectEditView] render->failed");
        });
    }
}

// Hinzufügen-Seite für SWE
export class ProjectAddView {
    constructor() {
        this.name = "main";
        this.template = "project.add.tpl";
    }

    render () {
        let markup = APPUTIL.templateManager.execute(this.template, []);
        let html_element = document.querySelector(this.name);
        if (html_element == null) alert("[ProjectAddView] render -> html_element=null");
        html_element.innerHTML = markup;

        document.getElementById("btn--projekt--back").addEventListener("click", function() {
            APPUTIL.eventService.publish("app.cmd", ["projekt--back", null]);
        });

        document.getElementById("btn--projekt--add--add").addEventListener("click", function() {
            let komponenten = document.getElementById("komponenten").value.split(",");

            let post_data = {
                "unique_id" : parseInt(document.getElementById("unique_id").value),
                "komponenten" : komponenten
            };

            fetch("/projekt/", {
                method: "POST",
                headers : { "Content-Type" : "application/json" },
                body : JSON.stringify(post_data)
            }).then(function (response) {
                let rueckgabe = null;
                if (response.ok) { // 200er-Status-Code
                    alert("[ProjectAddView] POST hat funktioniert");
                    APPUTIL.eventService.publish("app.cmd", ["projekt--back", null]);
                } else { alert("[ProjectAddView] POST hat nicht funktioniert"); }
                return rueckgabe;
            }).catch(function (error) {
                console.log("[ProjectAddView] POST-Problem: ", error.message);
            });
        });
    }
}

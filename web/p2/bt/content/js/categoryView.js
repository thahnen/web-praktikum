'use strict';

// TODO: Wenn alles getan ist, alles noch zusammenfassen!

// Übersicht für QSM (Knöpfe: Bearbeiten + Hinzufügen)
export class KatFehlerView {
    constructor () {
        this.name = "main";
        this.template = "category.view-katfehler.tpl";
        this.ausgewaehle_tabellenzeile = null; // mit -> [...].id bekommt man die Id (td--<unique_id>)
    }

    render () {
        let path = "/katfehler";
        let requester = new APPUTIL.Requester();

        console.log("[KatFehlerView] render -> Request /katfehler");
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
                alert("[KatFehlerView] render -> html_element=null")
            }
            html_element.innerHTML = markup;

            // EventHandler Tabellen-Zeilen jedes Mal aufs neue hinzufuegen
            [...document.getElementsByClassName("tr--katfehler")].forEach((x) => {
                x.addEventListener("click", function() {
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

            document.getElementById("btn--katfehler--edit").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                    APPUTIL.eventService.publish("app.cmd", ["katfehler--edit", id]);
                } else {
                    alert("Keine Fehlerkategorie zum bearbeiten ausgewaehlt!")
                }
            }.bind(this));

            document.getElementById("btn--katfehler--delete").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());

                    fetch("/katfehler/" + id, {
                        method: "DELETE"
                    }).then(function (response) {
                        let rueckgabe = null;
                        if (response.ok) { // 200er-Status-Code
                            alert("[KatFehlerView] DELETE hat funktioniert");
                            APPUTIL.eventService.publish("app.cmd", ["katfehler--back", null]);
                        } else {
                            alert("[KatFehlerView] DELETE hat nicht funktioniert");
                        }
                        return rueckgabe;
                    }).catch(function (error) {
                        console.log("[KatFehlerView] DELETE-Problem: ", error.message);
                    });
                } else {
                    alert("Keine Fehlerkategorie zum loeschen ausgewaehlt!")
                }
            }.bind(this));

            document.getElementById("btn--katfehler--add").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["katfehler--add", null]);
            });
        }.bind(this), function (response) {
            alert("[KatFehlerView] render->failed");
        });
    }
}

// Übersicht für SWE (Knöpfe: Bearbeiten + Hinzufügen)
export class KatUrsacheView {
    constructor () {
        this.name = "main";
        this.template = "category.view-katursache.tpl";
        this.ausgewaehle_tabellenzeile = null; // mit -> [...].id bekommt man die Id (td--<unique_id>)
    }

    render () {
        let path = "/katursache";
        let requester = new APPUTIL.Requester();

        console.log("[KatUrsacheView] render -> Request /katursache");
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
                alert("[KatUrsacheView] render -> html_element=null")
            }
            html_element.innerHTML = markup;

            // EventHandler Tabellen-Zeilen jedes Mal aufs neue hinzufuegen
            [...document.getElementsByClassName("tr--katursache")].forEach((x) => {
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

            document.getElementById("btn--katursache--edit").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());
                    APPUTIL.eventService.publish("app.cmd", ["katursache--edit", id]);
                } else {
                    alert("Keine Fehlerursachenkategorie ausgewaehlt!")
                }
            }.bind(this));

            document.getElementById("btn--katursache--delete").addEventListener("click", function() {
                if (this.ausgewaehle_tabellenzeile != null) {
                    // Hier muss noch ueberprueft werden, ob Fehler schon behoben und ob SWEs Id mit der im Fehler uebereinstimmt!
                    let id = parseInt(this.ausgewaehle_tabellenzeile.id.split("-").pop());

                    fetch("/katursache/" + id, {
                        method: "DELETE"
                    }).then(function (response) {
                        let rueckgabe = null;
                        if (response.ok) { // 200er-Status-Code
                            alert("[KatUrsacheView] DELETE hat funktioniert");
                            APPUTIL.eventService.publish("app.cmd", ["katursache--back", null]);
                        } else {
                            alert("[KatUrsacheView] DELETE hat nicht funktioniert");
                        }
                        return rueckgabe;
                    }).catch(function (error) {
                        console.log("[KatUrsacheView] DELETE-Problem: ", error.message);
                    });
                } else {
                    alert("Keine Fehlerkategorie zum loeschen ausgewaehlt!")
                }
            }.bind(this));

            document.getElementById("btn--katursache--add").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["katursache--add", null]);
            });
        }.bind(this), function (response) {
            alert("[KatUrsacheView] render->failed");
        });
    }
}

// Bearbeitung-Seite für QSM
export class KatFehlerEditView {
    constructor () {
        this.name = "main";
        this.template = "category.edit-katfehler.tpl";
    }

    render (id) {
        let path = "/katfehler/" + id;
        let requester = new APPUTIL.Requester();

        console.log("[KatFehlerEditView] render -> Request /katfehler/" + id);
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let markup = APPUTIL.templateManager.execute(this.template, data);
            let html_element = document.querySelector(this.name);
            if (html_element == null) {
                alert("[KatFehlerEditView] render -> html_element=null")
            }
            html_element.innerHTML = markup;

            document.getElementById("btn--katfehler--back").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["katfehler--back", null]);
            });

            document.getElementById("btn--katfehler--edit--save").addEventListener("click", function() {
                let unique_id = parseInt(document.getElementById("unique_id").value);
                let beschreibung = document.getElementById("beschreibung").value;

                let put_data = {
                    "unique_id" : unique_id,
                    "beschreibung" : beschreibung
                };

                fetch("/katfehler/" + id, {
                    method: "PUT",
                    headers : {
                        "Content-Type" : "application/json"
                    },
                    body : JSON.stringify(put_data)
                }).then(function (response) {
                    let rueckgabe = null;
                    if (response.ok) { // 200er-Status-Code
                        alert("[KatFehlerEditView] PUT hat funktioniert");
                        APPUTIL.eventService.publish("app.cmd", ["katfehler--back", null]);
                    } else {
                        alert("[KatFehlerEditView] PUT hat nicht funktioniert");
                    }
                    return rueckgabe;
                }).catch(function (error) {
                    console.log("[KatFehlerEditView] PUT-Problem: ", error.message);
                });
            });
        }.bind(this), function (response) {
            alert("[KatFehlerEditView] render->failed");
        });
    }
}

// Bearbeitung-Seite für SWE
export class KatUrsacheEditView {
    constructor () {
        this.name = "main";
        this.template = "category.edit-katursache.tpl";
    }

    render (id) {
        let path = "/katursache/" + id;
        let requester = new APPUTIL.Requester();

        console.log("[KatUrsacheEditView] render -> Request /katursache/" + id);
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let markup = APPUTIL.templateManager.execute(this.template, data);
            let html_element = document.querySelector(this.name);
            if (html_element == null) {
                alert("[KatUrsacheEditView] render -> html_element=null")
            }
            html_element.innerHTML = markup;

            document.getElementById("btn--katursache--back").addEventListener("click", function() {
                APPUTIL.eventService.publish("app.cmd", ["katursache--back", null]);
            });

            document.getElementById("btn--katursache--edit--save").addEventListener("click", function() {
                let unique_id = parseInt(document.getElementById("unique_id").value);
                let beschreibung = document.getElementById("beschreibung").value;

                let put_data = {
                    "unique_id" : unique_id,
                    "beschreibung" : beschreibung
                };

                fetch("/katursache/" + id, {
                    method: "PUT",
                    headers : {
                        "Content-Type" : "application/json"
                    },
                    body : JSON.stringify(put_data)
                }).then(function (response) {
                    let rueckgabe = null;
                    if (response.ok) { // 200er-Status-Code
                        alert("[KatUrsacheEditView] PUT hat funktioniert");
                        APPUTIL.eventService.publish("app.cmd", ["katursache--back", null]);
                    } else {
                        alert("[KatUrsacheEditView] PUT hat nicht funktioniert");
                    }
                    return rueckgabe;
                }).catch(function (error) {
                    console.log("[KatUrsacheEditView] PUT-Problem: ", error.message);
                });
            });
        }.bind(this), function (response) {
            alert("[KatUrsacheEditView] render->failed");
        });
    }
}

// Hinzufügen-Seite für QSM
export class KatFehlerAddView {
    constructor () {
        this.name = "main";
        this.template = "category.add-katfehler.tpl";
    }

    render () {
        let markup = APPUTIL.templateManager.execute(this.template, []);
        let html_element = document.querySelector(this.name);
        if (html_element == null) {
            alert("[KatFehlerAddView] render -> html_element=null")
        }
        html_element.innerHTML = markup;

        document.getElementById("btn--katfehler--back").addEventListener("click", function() {
            APPUTIL.eventService.publish("app.cmd", ["katfehler--back", null]);
        });

        document.getElementById("btn--katfehler--add--add").addEventListener("click", function() {
            let beschreibung = document.getElementById("beschreibung").value;

            let post_data = {
                "unique_id" : parseInt(document.getElementById("unique_id").value),
                "beschreibung" : beschreibung
            };

            fetch("/katfehler/", {
                method: "POST",
                headers : {
                    "Content-Type" : "application/json"
                },
                body : JSON.stringify(post_data)
            }).then(function (response) {
                let rueckgabe = null;
                if (response.ok) { // 200er-Status-Code
                    alert("[KatFehlerAddView] POST hat funktioniert");
                    APPUTIL.eventService.publish("app.cmd", ["katfehler--back", null]);
                } else {
                    alert("[KatFehlerAddView] POST hat nicht funktioniert");
                }
                return rueckgabe;
            }).catch(function (error) {
                console.log("[KatFehlerAddView] POST-Problem: ", error.message);
            });
        });
    }
}

// Hinzufügen-Seite für SWE
export class KatUrsacheAddView {
    constructor () {
        this.name = "main";
        this.template = "category.add-katursache.tpl";
    }

    render () {
        let markup = APPUTIL.templateManager.execute(this.template, []);
        let html_element = document.querySelector(this.name);
        if (html_element == null) {
            alert("[KatUrsacheAddView] render -> html_element=null")
        }
        html_element.innerHTML = markup;

        document.getElementById("btn--katursache--back").addEventListener("click", function() {
            APPUTIL.eventService.publish("app.cmd", ["katursache--back", null]);
        });

        document.getElementById("btn--katursache--add--add").addEventListener("click", function() {
            let beschreibung = document.getElementById("beschreibung").value;

            let post_data = {
                "unique_id" : parseInt(document.getElementById("unique_id").value),
                "beschreibung" : beschreibung
            };

            fetch("/katursache/", {
                method: "POST",
                headers : {
                    "Content-Type" : "application/json"
                },
                body : JSON.stringify(post_data)
            }).then(function (response) {
                let rueckgabe = null;
                if (response.ok) { // 200er-Status-Code
                    alert("[KatUrsacheAddView] POST hat funktioniert");
                    APPUTIL.eventService.publish("app.cmd", ["katursache--back", null]);
                } else {
                    alert("[KatUrsacheAddView] POST hat nicht funktioniert");
                }
                return rueckgabe;
            }).catch(function (error) {
                console.log("[KatUrsacheAddView] POST-Problem: ", error.message);
            });
        });
    }
}

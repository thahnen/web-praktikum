//------------------------------------------------------------------------------
//Demonstrator evs/tco/tmg
//------------------------------------------------------------------------------
'use strict'

class DetailView {
    constructor (name, template) {
        this.elem_name = name;
        this.template_name = template;
    }

    render (id) {
        // Daten anfordern
        let path = "/app/" + id;
        let requester = new APPUTIL.Requester();

        console.log("[DetailView] Request /app/");
        requester.request(path, function (response) {
            let data = JSON.parse(response);
            this.doRender(data);
        }.bind(this), function (response) {
            alert("Detail - render failed");
        });
    }

    doRender (data) {
        let markup = APPUTIL.templateManager.execute(this.template_name, data);
        let html_element = document.querySelector(this.elem_name);
        if (html_element != null) {
            html_element.innerHTML = markup;
            this.configHandleElement();
        }
    }

    configHandleElement () {
        let html_element = document.querySelector("form");
        if (html_element != null) {
            html_element.addEventListener("click", this.handleEvent);
        }
    }

    handleEvent (event) {
        if (event.target.id == "idBack") {
            APPUTIL.eventService.publish("app.cmd", ["idBack", null]);
            event.preventDefault();
        }
    }
}


class ListView {
    constructor (name, template) {
        this.elem_name = name;
        this.template_name = template;
        this.configHandleElement();
    }

    render () {
        // Daten anfordern
        let path = "/app/";
        let requester = new APPUTIL.Requester();

        console.log("[ListView] Request /app/");
        requester.request(path, function (response) {
            let data = JSON.parse(response);
            this.doRender(data);
        }.bind(this), function (response) {
            alert("List - render failed");
        });
    }

    doRender (data) {
        let markup = APPUTIL.templateManager.execute(this.template_name, data);
        let html_element = document.querySelector(this.elem_name);
        if (html_element != null) {
            html_element.innerHTML = markup;
        }
    }

    configHandleElement () {
        let html_element = document.querySelector(this.elem_name);
        if (html_element != null) {
            html_element.addEventListener("click", this.handleEvent);
        }
    }

    handleEvent (event) {
        if (event.target.tagName.toUpperCase() == "TD") {
            let selected_elem = document.querySelector(".clSelected");
            if (selected_elem != null) {
                selected_elem.classList.remove("clSelected");
            }

            event.target.parentNode.classList.add("clSelected");
            event.preventDefault();
        } else if (event.target.id == "idShowListEntry") {
            let selected_elem = document.querySelector(".clSelected");
            if (selected_elem == null) {
                alert("Bitte zuerst einen Eintrag auswählen!");
            } else {
                APPUTIL.eventService.publish("app.cmd", ["detail", selected_elem.id] );
            }

            event.preventDefault();
        }
    }
}


// TODO: Alles mehr zusammenfassen!
class SideBar {
    constructor (name, template) {
        this.elem_name = name;
        this.template_name = template;

        // Event-Listener setzen (aus Beims sein Beispiel)
        let html_element = document.querySelector(this.elem_name);
        if (html_element != null) {
            html_element.addEventListener("click", function(event) {
                APPUTIL.eventService.publish("app.cmd", [
                    event.target.dataset.action, null
                ]);
            });
        }
    }

    render (data) {
        let markup = APPUTIL.templateManager.execute(this.template_name, data);
        let html_element = document.querySelector(this.elem_name);
        if (html_element != null) {
            html_element.innerHTML = markup;
        }
    }
}


class Application {
    constructor () {
        // Registrieren zum Empfang von Nachrichten
        APPUTIL.eventService.subscribe(this, "templates.loaded");
        APPUTIL.eventService.subscribe(this, "templates.failed");
        APPUTIL.eventService.subscribe(this, "app.cmd");
        this.sideBar = new SideBar("aside", "sidebar.tpl");
        this.listView = new ListView("main", "list.tpl");
        this.detailView = new DetailView("main", "detail.tpl");
    }

    notify (self, message, data) {
        switch (message) {
        case "templates.failed":
            alert("Vorlagen konnten nicht geladen werden.");
            break;
        case "templates.loaded":
            /*
                Templates konnten geladen werden:
                1) Header laden mit Inhalt des Cookies
                2) Navigationsleiste laden mit vorgegebenen Seiten
                3) Startseite laden (soll ein bisschen aussehen wie ein Dashboard)
            */
            // Cookie-Aufbau: "password=<...>; type=<...>; username=<...>"
            let cookie_data = [...document.cookie.split("; ")];
            cookie_data.shift();
            cookie_data = cookie_data.map(x => x.split("=")[1]);
            console.log(cookie_data);

            let markup = APPUTIL.templateManager.execute("header.tpl", cookie_data);
            let html_element = document.querySelector("header");
            html_element.innerHTML = markup;

            // Hier dann noch die einzelnen "Kommandos zu verfassen"
            let navigation = [
                ["home", "Startseite"],
                ["overview_errors", "Bearbeitung Fehlerdaten"],
                ["overview_projects", "Pflege Projekte"],
                ["overview_components", "Pflege Komponenten"],
                ["overview_workersdata", "Pflege Daten Mitarbeiter"],
                ["overview_kategories", "Pflege Kategorien"],
                ["evaluation_projects", "Auswertung Projekte/Fehler"],
                ["evaluation_kategories", "Auswertung Kategorien/Fehler"]
            ];

            self.sideBar.render(navigation);
            markup = APPUTIL.templateManager.execute("home.tpl", null);
            html_element = document.querySelector("main");

            if (html_element != null) {
                html_element.innerHTML = markup;
            }
            break;
        case "app.cmd":
            switch (data[0]) {
            case "home":
                let markup = APPUTIL.templateManager.execute("home.tpl", null);
                let html_element = document.querySelector("main");

                if (html_element != null) {
                    html_element.innerHTML = markup;
                }
                break;
            case "overview_errors":
                alert("Bearbeitung Fehlerdaten noch nicht hinzugefuegt!")
                break;
            case "overview_projects":
                alert("Pflege Projekte noch nicht hinzugefuegt!")
                break;
            case "overview_components":
                alert("Pflege Komponenten noch nicht hinzugefuegt!")
                break;
            case "overview_workersdata":
                alert("Pflege Daten Mitarbeiter noch nicht hinzugefuegt!")
                break;
            case "overview_kategories":
                alert("Pflege Kategorien noch nicht hinzugefuegt!")
                break;
            case "evaluation_projects":
                alert("Auswertung Projekte/Fehler noch nicht hinzugefuegt!")
                break;
            case "evaluation_kategories":
                alert("Auswertung Kategorien/Fehler noch nicht hinzugefuegt!")
                break;
            case "list":
                // Daten anfordern und darstellen
                this.listView.render();
                break;
            case "detail":
                this.detailView.render(data[1]);
                break;
            case "idBack": // hier aus einem der Detail-Views, so auch fuer alle Details bei mir machen!
                APPUTIL.eventService.publish("app.cmd", ["list", null]);
                break;
            }
            break;
        }
    }
}

window.onload = function () {
    APPUTIL.eventService = new APPUTIL.EventService();
    APPUTIL.templateManager = new APPUTIL.TemplateManager();
    APPUTIL.templateManager.init();
    var application = new Application();
}

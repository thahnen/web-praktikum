'use strict'

// Seitenleiste (bei QSM/SWE gleich!)
class SideBar {
    constructor (name, template) {
        this.elem_name = name;
        this.template_name = template;
        this.html_element = document.querySelector(this.elem_name);

        if (this.html_element == null) {
            alert("[SideBar] HTML-Element nicht gefunden!")
            return;
        }

        this.html_element.addEventListener("click", function(event) {
            APPUTIL.eventService.publish("app.cmd", [
                event.target.dataset.action, null
            ]);
        });
    }

    render (data) {
        let markup = APPUTIL.templateManager.execute(this.template_name, data);
        this.html_element.innerHTML = markup;
    }
}


// Uebersicht Fehler -> QSM kann neue hinzufuegen, SWE die zugewiesenen bearbeiten!
class ErrorView {
    constructor (name, template) {
        this.name = name;
        this.template = template;

        // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
    }

    render () {
        // Daten anfordern
        let path = "/fehler";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorView] Request /fehler");
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
            if (html_element != null) {
                html_element.innerHTML = markup;
            }
        }.bind(this), function (response) {
            alert("[ErrorView] render->failed");
        });
    }
}


// Uebersicht Projekte (bei QSM/SWE gleich!)
class ProjectView {
    constructor (name, template) {
        this.name = name;
        this.template = template;

        // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
    }

    render () {
        // Daten anfordern
        let path = "/projekt";
        let requester = new APPUTIL.Requester();

        console.log("[ProjectView] Request /projekt");
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
        }.bind(this), function (response) {
            alert("[ProjectView] render->failed");
        });
    }
}


// Uebersicht Komponenten (bei QSM/SWE gleich!)
class ComponentView {
    constructor (name, template) {
        this.name = name;
        this.template = template;

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
        }.bind(this), function (response) {
            alert("[ComponentView] render->failed");
        });
    }
}


// Uebersicht Mitarbeiter -> QSM kann QSM bearbeiten, SWE kann SWE bearbeiten!
class WorkerView {
    constructor (name, template) {
        this.name = name;
        this.template = template;

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
        }.bind(this), function (response) {
            alert("[WorkerView] render->failed");
        });
    }
}


// Uebersicht Kategorien -> QSM kann Fehlerkategorien bearbeiten, SWE kann Fehlerursachenkategorien bearbeiten!
class CategoryView {
    constructor (name, template) {
        this.name = name;
        this.template = template;

        // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
    }

    render () {
        // Daten anfordern
        //let path = "/katursache"
        let path = "/katfehler";
        let requester = new APPUTIL.Requester();

        //console.log("[CategoryView] Request /katursache");
        console.log("[CategoryView] Request /katfehler");
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
        }.bind(this), function (response) {
            alert("[CategoryView] render->failed");
        });
    }
}


// Uebersicht aller Fehler nach Projekten sortiert (bei QSM/SWE gleich!)
class ErrorsByProjectsView {
    constructor (name, template) {
        this.name = name;
        this.template = template;

        // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
    }
}


// Uebersicht aller Fehler nach Kategorien (bei QSM/SWE gleich!)
class ErrorsByCategoriesView {
    constructor (name, template) {
        this.name = name;
        this.template = template;

        // Hier noch EventHandler und so hinzufuegen fuer die einzelnen Tabellen-Zeilen
    }
}


// das kann irgendwann weg, muss nur so ungefaehr in die anderen uebernommen werden
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
            let markup = APPUTIL.templateManager.execute(this.template_name, data);
            let html_element = document.querySelector(this.elem_name);
            if (html_element != null) {
                html_element.innerHTML = markup;
                let html_element = document.querySelector("form");
                if (html_element != null) {
                    html_element.addEventListener("click", this.handleEvent);
                }
            }
        }.bind(this), function (response) {
            alert("Detail - render failed");
        });
    }

    handleEvent (event) {
        if (event.target.id == "idBack") {
            APPUTIL.eventService.publish("app.cmd", ["idBack", null]);
            event.preventDefault();
        }
    }
}


// das kann irgendwann weg, muss nur so ungefaehr in die anderen uebernommen werden
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
            let markup = APPUTIL.templateManager.execute(this.template_name, data);
            let html_element = document.querySelector(this.elem_name);
            if (html_element != null) {
                html_element.innerHTML = markup;
            }
        }.bind(this), function (response) {
            alert("List - render failed");
        });
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


// Hier muss noch dran gearbeitet werden!
class Application {
    constructor () {
        // Registrieren zum Empfang von Nachrichten
        APPUTIL.eventService.subscribe(this, "templates.loaded");
        APPUTIL.eventService.subscribe(this, "templates.failed");
        APPUTIL.eventService.subscribe(this, "app.cmd");
        this.sideBar = new SideBar("aside", "sidebar.tpl");
        this.listView = new ListView("main", "list.tpl");
        this.detailView = new DetailView("main", "detail.tpl");
        this.errorView = new ErrorView("main", "overview_errors.tpl");
        this.projectView = new ProjectView("main", "overview_projects.tpl");
        this.componentView = new ComponentView("main", "overview_components.tpl");
        this.categoryView = new CategoryView("main", "overview_categories.tpl");
        this.workerView = new WorkerView("main", "overview_workersdata.tpl");
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
                ["overview_categories", "Pflege Kategorien"],
                ["evaluation_projects", "Auswertung Projekte/Fehler"],
                ["evaluation_categories", "Auswertung Kategorien/Fehler"]
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
                this.errorView.render();
                break;
            case "overview_projects":
                this.projectView.render();
                break;
            case "overview_components":
                this.componentView.render();
                break;
            case "overview_workersdata":
                this.workerView.render();
                break;
            case "overview_categories":
                this.categoryView.render();
                break;
            case "evaluation_projects":
                alert("Auswertung Projekte/Fehler noch nicht hinzugefuegt!")
                break;
            case "evaluation_categories":
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

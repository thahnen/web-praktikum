'use strict'

import SideBar from "./sideBar.js";
import ErrorView from "./errorView.js";
import ProjectView from "./projectView.js";
import ComponentView from "./componentView.js";
import WorkerView from "./workerView.js";
import CategoryView from "./categoryView.js";


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
            html_element.addEventListener("click", function (event) {
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
            });
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
        //this.listView = new ListView("main", "list.tpl");
        //this.detailView = new DetailView("main", "detail.tpl");
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

            // Alles was mit den Fehlern zu tun hat!
            case "overview_errors":
                this.errorView.render();
                break;
            case "fehler--erkannt":
                alert("'Fehler erkannt'-View noch nicht hinzugefuegt")
                break;
            case "fehler--behoben":
                alert("'Fehler behoben'-View noch nicht hinzugefuegt")
                break;
            case "fehler--edit":
                alert("'Fehler bearbeiten'-View noch nicht hinzugefuegt")
                break;
            case "fehler--add":
                alert("'Fehler hinzufuegen'-View noch nicht hinzugefuegt")
                break;

            // Alles was mit den Projekten zu tun hat!
            case "overview_projects":
                this.projectView.render();
                break;
            case "projekt--edit":
                alert("'Projekt bearbeiten'-View noch nicht hinzugefuegt")
                break;
            case "projekt--add":
                alert("'Projekt hinzufuegen'-View noch nicht hinzugefuegt")
                break;

            // Alles was mit den Komponenten zu tun hat!
            case "overview_components":
                this.componentView.render();
                break;
            case "komponente--sort":
                alert("'Komponente sortiert nach Projekt-Id'-View noch nicht hinzugefuegt")
                break;
            case "komponente--edit":
                alert("'Komponente bearbeiten'-View noch nicht hinzugefuegt")
                break;
            case "komponente--add":
                alert("'Komponente hinzufuegen'-View noch nicht hinzugefuegt")
                break;

            // Alles was mit den Mitarbeitern zu tun hat!
            case "overview_workersdata":
                this.workerView.render();
                break;
            case "arbeiter--edit":
                alert("'Arbeiter bearbeiten'-View noch nicht hinzugefuegt")
                break;
            case "arbeiter--add":
                alert("'Arbeiter hinzufuegen'-View noch nicht hinzugefuegt")
                break;

            // Alles was mit den Kategorien zu tun hat!
            case "overview_categories":
                this.categoryView.render();
                break;
            case "kategorie--edit":
                alert("'Kategorie bearbeiten'-View noch nicht hinzugefuegt")
                break;
            case "kategorie--add":
                alert("'Kategorie hinzufuegen'-View noch nicht hinzugefuegt")
                break;

            // Sortierte Fehler nach Projekten
            case "evaluation_projects":
                alert("Auswertung Projekte/Fehler noch nicht hinzugefuegt!")
                break;

            // Sortierte Fehler nach Kategorien
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

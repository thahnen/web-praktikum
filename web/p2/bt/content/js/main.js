'use strict'

import SideBar from "./sideBar.js";
import ErrorView, {ErrorErkanntView, ErrorBehobenView, ErrorEditView, ErrorAddView} from "./errorView.js";
import ProjectView, {ProjectEditView, ProjectAddView} from "./projectView.js";
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



// Hier muss noch dran gearbeitet werden!
class Application {
    constructor () {
        // Registrieren zum Empfang von Nachrichten
        APPUTIL.eventService.subscribe(this, "templates.loaded");
        APPUTIL.eventService.subscribe(this, "templates.failed");
        APPUTIL.eventService.subscribe(this, "app.cmd");
        this.sideBar = new SideBar("aside", "sidebar.tpl");

        this.errorView = new ErrorView("main", "overview_errors.tpl");
        this.errorErkanntView = new ErrorErkanntView();
        this.errorBehobenView = new ErrorBehobenView();
        this.errorEditView = new ErrorEditView();
        this.errorAddView = new ErrorAddView();

        this.projectView = new ProjectView("main", "overview_projects.tpl");
        this.projectEditView = new ProjectEditView();
        this.projectAddView = new ProjectAddView();

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
                ["fehler--view", "Bearbeitung Fehlerdaten"],
                ["projekt--view", "Pflege Projekte"],
                ["komponente--view", "Pflege Komponenten"],
                ["arbeiter--view", "Pflege Daten Mitarbeiter"],
                ["kategorie--view", "Pflege Kategorien"],
                ["fehler--projekt--evaluation", "Auswertung Projekte/Fehler"],
                ["fehler--kategorie--evaluation", "Auswertung Kategorien/Fehler"]
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
            case "fehler--view":
            case "fehler--back":
                this.errorView.render();
                break;
            case "fehler--erkannt":
                this.errorErkanntView.render();
                break;
            case "fehler--behoben":
                this.errorBehobenView.render();
                break;
            case "fehler--edit":
                this.errorEditView.render(data[1]);
                break;
            case "fehler--add":
                this.errorAddView.render();
                break;

            // Alles was mit den Projekten zu tun hat!
            case "projekt--view":
            case "projekt--back":
                this.projectView.render();
                break;
            case "projekt--edit":
                this.projectEditView.render(data[1]);
                break;
            case "projekt--add":
                this.projectAddView.render();
                break;

            // Alles was mit den Komponenten zu tun hat!
            case "komponente--view":
            case "komponente--back":
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
            case "arbeiter--view":
            case "arbeiter--back":
                this.workerView.render();
                break;
            case "arbeiter--edit":
                alert("'Arbeiter bearbeiten'-View noch nicht hinzugefuegt")
                break;
            case "arbeiter--add":
                alert("'Arbeiter hinzufuegen'-View noch nicht hinzugefuegt")
                break;

            // Alles was mit den Kategorien zu tun hat!
            case "kategorie--view":
            case "kategorie--back":
                this.categoryView.render();
                break;
            case "kategorie--edit":
                alert("'Kategorie bearbeiten'-View noch nicht hinzugefuegt")
                break;
            case "kategorie--add":
                alert("'Kategorie hinzufuegen'-View noch nicht hinzugefuegt")
                break;

            // Sortierte Fehler nach Projekten
            case "fehler--projekt--evaluation":
                alert("Auswertung Projekte/Fehler noch nicht hinzugefuegt!")
                break;

            // Sortierte Fehler nach Kategorien
            case "fehler--kategorie--evaluation":
                alert("Auswertung Kategorien/Fehler noch nicht hinzugefuegt!")
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

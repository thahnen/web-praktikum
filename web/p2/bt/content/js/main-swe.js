'use strict'

/*
    ANGEPASSTE VERSION FUER DIE SW-ENTWICKLER!
*/

import SideBarView from "./sideBar.js";
import {ErrorSWEView, ErrorErkanntView, ErrorBehobenView, ErrorEditView} from "./errorView.js";
import {ProjectSWEView, ProjectEditView, ProjectAddView} from "./projectView.js";
import {ComponentSWEView, ComponentProjectView, ComponentEditView, ComponentAddView} from "./componentView.js";
import {SWEView} from "./workerView.js";
import {KatUrsacheView, KatUrsacheEditView, KatUrsacheAddView} from "./categoryView.js";
import ErrorsByProjectView from "./errorsByProject.js";
import ErrorsByCategoryView from "./errorsByCategory.js"


class Application {
    constructor () {
        // Registrieren zum Empfang von Nachrichten
        APPUTIL.eventService.subscribe(this, "templates.loaded");
        APPUTIL.eventService.subscribe(this, "templates.failed");
        APPUTIL.eventService.subscribe(this, "app.cmd");
        this.sideBarView = new SideBarView("aside", "sidebar.tpl");

        this.errorSWEView = new ErrorSWEView();
        this.errorErkanntView = new ErrorErkanntView();
        this.errorBehobenView = new ErrorBehobenView();
        this.errorEditView = new ErrorEditView();

        this.projectSWEView = new ProjectSWEView();
        this.projectEditView = new ProjectEditView();
        this.projectAddView = new ProjectAddView();

        this.componentSWEView = new ComponentSWEView();
        this.componentProjectView = new ComponentProjectView();
        this.componentEditView = new ComponentEditView();
        this.componentAddView = new ComponentAddView();

        this.sweView = new SWEView();

        this.katUrsacheView = new KatUrsacheView();
        this.katUrsacheEditView = new KatUrsacheEditView();
        this.katUrsacheAddView = new KatUrsacheAddView();

        this.errorsByProjectView = new ErrorsByProjectView();
        this.errorsByCategoryView = new ErrorsByCategoryView();
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
                ["swentwickler--view", "Pflege Daten Mitarbeiter"],
                ["katursache--view", "Pflege Kategorien"],
                ["fehler--projekt--evaluation", "Auswertung Projekte/Fehler"],
                ["fehler--kategorie--evaluation", "Auswertung Kategorien/Fehler"]
            ];

            self.sideBarView.render(navigation);
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
                this.errorSWEView.render();
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

            // Alles was mit den Projekten zu tun hat!
            case "projekt--view":
            case "projekt--back":
                this.projectSWEView.render();
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
                this.componentSWEView.render();
                break;
            case "komponente--sort":
                alert("'Komponente sortiert nach Projekt-Id'-View noch nicht hinzugefuegt")
                break;
            case "komponente--edit":
                this.componentEditView.render(data[1]);
                break;
            case "komponente--add":
                this.componentAddView.render();
                break;

            // Alles was mit den SW-Entwicklern zu tun hat!
            case "swentwickler--view":
                this.sweView.render();
                break;

            // Alles was mit den Kategorien zu tun hat!
            case "katursache--view":
            case "katursache--back":
                this.katUrsacheView.render();
                break;
            case "katursache--edit":
                this.katUrsacheEditView.render(data[1]);
                break;
            case "katursache--add":
                this.katUrsacheAddView.render();
                break;

            // Sortierte Fehler nach Projekten
            case "fehler--projekt--evaluation":
                this.errorsByProjectView.render();
                break;

            // Sortierte Fehler nach Kategorien
            case "fehler--kategorie--evaluation":
                this.errorsByCategoryView.render();
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

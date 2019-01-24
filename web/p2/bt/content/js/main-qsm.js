'use strict'

/*
    ANGEPASSTE VERSION FUER DIE QS-MITARBEITE!
*/

import SideBarView from "./sideBar.js";
import {ErrorQSMView, ErrorErkanntView, ErrorBehobenView, ErrorAddView} from "./errorView.js";
import {ProjectQSMView} from "./projectView.js";
import {ComponentQSMView, ComponentProjectView} from "./componentView.js";
import {QSMView} from "./workerView.js";
import {KatFehlerView, KatFehlerEditView, KatFehlerAddView} from "./categoryView.js";
import ErrorsByProjectView from "./errorsByProject.js";
import ErrorsByCategoryView from "./errorsByCategory.js"


class Application {
    constructor () {
        // Registrieren zum Empfang von Nachrichten
        APPUTIL.eventService.subscribe(this, "templates.loaded");
        APPUTIL.eventService.subscribe(this, "templates.failed");
        APPUTIL.eventService.subscribe(this, "app.cmd");
        this.sideBarView = new SideBarView("aside", "sidebar.tpl");

        this.errorQSMView = new ErrorQSMView();
        this.errorErkanntView = new ErrorErkanntView();
        this.errorBehobenView = new ErrorBehobenView();
        this.errorAddView = new ErrorAddView();

        this.projectQSMView = new ProjectQSMView();

        this.componentQSMView = new ComponentQSMView();
        this.componentProjectView = new ComponentProjectView();

        this.qsmView = new QSMView();

        this.katFehlerView = new KatFehlerView();
        this.katFehlerEditView = new KatFehlerEditView();
        this.katFehlerAddView = new KatFehlerAddView();

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
                ["qsmitarbeiter--view", "Pflege Daten Mitarbeiter"],
                ["katfehler--view", "Pflege Kategorien"],
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
                this.errorQSMView.render();
                break;
            case "fehler--erkannt":
                this.errorErkanntView.render();
                break;
            case "fehler--behoben":
                this.errorBehobenView.render();
                break;
            case "fehler--add":
                this.errorAddView.render();
                break;

            // Alles was mit den Projekten zu tun hat!
            case "projekt--view":
                this.projectQSMView.render();
                break;

            // Alles was mit den Komponenten zu tun hat!
            case "komponente--view":
            case "komponente--back":
                this.componentQSMView.render();
                break;
            case "komponente--sort":
                alert("'Komponente sortiert nach Projekt-Id'-View noch nicht hinzugefuegt")
                break;

            // Alles was mit den QS-Mitarbeitern zu tun hat!
            case "qsmitarbeiter--view":
                this.qsmView.render();
                break;

            // Alles was mit den Fehlerkategorien zu tun hat!
            case "katfehler--view":
            case "katfehler--back":
                this.katFehlerView.render();
                break;
            case "katfehler--edit":
                this.katFehlerEditView.render(data[1]);
                break;
            case "katfehler--add":
                this.katFehlerAddView.render();
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

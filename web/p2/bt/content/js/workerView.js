'use strict';

// Übersicht für QSM (Knöpfe: Bearbeiten + Hinzufügen) BZW Keine!
export class QSMView {
    constructor () {
        this.name = "main";
        this.template = "worker.view-qsm.tpl";
    }

    render () {
        let path = "/qsmitarbeiter";
        let requester = new APPUTIL.Requester();

        console.log("[QSMView] render -> Request /qsmitarbeiter");
        requester.request(path, function (response) {
            let data = JSON.parse(response);
            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[QSMView] render -> html_element=null");
            html_element.innerHTML = markup;

        }.bind(this), function (response) { alert("[QSMView] render->failed"); });
    }
}

// Übersicht für SWE (Knöpfe: Bearbeiten + Hinzufügen) BZW Keine!
export class SWEView {
    constructor () {
        this.name = "main";
        this.template = "worker.view-swe.tpl";
    }

    render () {
        let path = "/swentwickler";
        let requester = new APPUTIL.Requester();

        console.log("[SWEView] render -> Request /swentwickler");
        requester.request(path, function (response) {
            let data = JSON.parse(response);
            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[SWEView] render -> html_element=null");
            html_element.innerHTML = markup;

        }.bind(this), function (response) { alert("[SWEView] render->failed"); });
    }
}

// Bearbeitung-Seite für QSM
export class QSMEditView {
    constructor () {
        this.name = "main";
        this.template = "worker.edit-qsm.tpl";
    }

    render () { }
}

// Bearbeitung-Seite für SWE
export class SWEEditView {
    constructor () {
        this.name = "main";
        this.template = "worker.edit-swe.tpl";
    }

    render () { }
}

// Hinzufügen-Seite für QSM
export class QSMAddView {
    constructor () {
        this.name = "main";
        this.template = "worker.add-qsm.tpl";
    }

    render () { }
}

// Hinzufügen-Seite für SWE
export class SWEAddView {
    constructor () {
        this.name = "main";
        this.template = "worker.add-swe.tpl";
    }

    render () { }
}

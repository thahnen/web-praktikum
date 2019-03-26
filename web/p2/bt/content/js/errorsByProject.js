'use strict';

// Uebersicht aller Fehler nach Projekten sortiert (bei QSM/SWE gleich!)
export default class {
    constructor () {
        this.name = "main";
        this.template = "error.view-project.tpl";
    }

    render () {
        let path = "/prolist";
        let requester = new APPUTIL.Requester();

        console.log("[ErrorsByProjectView] render -> Request /prolist");
        requester.request(path, function (response) {
            let data = JSON.parse(response);

            let context = [];
            for (let fehler in data) {
                if (data.hasOwnProperty(fehler)) context.push(data[fehler]);
            }

            let markup = APPUTIL.templateManager.execute(this.template, context);
            let html_element = document.querySelector(this.name);
            if (html_element == null) alert("[ErrorsByProjectView] render -> html_element=null");
            html_element.innerHTML = markup;
        }.bind(this), function (response) { alert("[ErrorsByProjectView] render->failed"); });
    }
}

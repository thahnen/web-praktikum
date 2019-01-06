//------------------------------------------------------------------------------
// Template-Manager
// - Laden und Bereitstellen von Template-Quellen
// - setzt evs.js und tco.js voraus
//------------------------------------------------------------------------------

'use strict'

var APPUTIL = APPUTIL || {};

APPUTIL.TemplateManager = class {
    constructor () {
        if (!APPUTIL.TemplateManager.instance) {
            APPUTIL.TemplateManager.instance = this;
            this.templates = {};
            this.code_compiled  = {};
            this.compiler = new APPUTIL.TemplateCompiler();
        }
        return APPUTIL.TemplateManager.instance;
    }

    // Läd direkt alle Templates vom Server
    init () {
        let pfad = "/templates";
        let requester = new APPUTIL.Requester();

        requester.request(pfad, function (response) {
            let data = JSON.parse(JSON.parse(response));

            console.log("Templates konnten geladen werden:")
            console.log(data);
            this.templates = data["templates"];

            APPUTIL.eventService.publish("templates.loaded", null);
        }.bind(this), function (response) {
            console.log("Templates konnten nicht geladen werden")
            APPUTIL.eventService.publish("templates.failed", response);
        });

        console.log(this.templates);
    }

    get (name) {
        if (name in this.templates) {
            return this.templates[name];
        } else {
            return null;
        }
    }

    execute (name, data) {
        let code_compiled = null;

        if (name in this.code_compiled) {
            code_compiled = this.code_compiled[name];
        } else {
            if (name in this.templates) {
                // Übersetzen und ausführen
                this.compiler.reset();
                code_compiled = this.compiler.compile(this.templates[name]);
                this.code_compiled[name] = code_compiled;
            }
        }

        if (code_compiled != null) {
            return code_compiled(data);
        } else {
            return null;
        }
    }
}

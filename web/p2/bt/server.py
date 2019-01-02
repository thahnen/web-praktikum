#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Webserver mit Config und Routing:
#   ================================
#
#   - "/":
#       => Hauptseite, alle anderen hier verlinkt
#
#   - "/projekt":
#       => ...
#


import os
import cherrypy
import app


class WebServer(object):
    def __init__(self, application):
        self.application = application

    # Index-Seite des Webservers (führt zu allen wichtigen Seiten)
    @cherrypy.expose
    def index(self):
        return self.application.get_static_page("index")


config = {
    "/" : {
        "tools.staticdir.root" : os.path.dirname(os.path.abspath(__file__))
    },
    "/css" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : "./content/css/"
    },
    "/js" : {
        "tools.staticdir.on" : True,
        "tools.staticdir.dir" : "./content/js/"
    }
}

config_rest = {
    "/" : {
        "request.dispatch" : cherrypy.dispatch.MethodDispatcher()
    }
}


if __name__ == '__main__':
    server_path = os.path.dirname(os.path.abspath(__file__))
    logic = app.Application(server_path)

    cherrypy.tree.mount(
        WebServer(), "/", config=config
    )

    cherrypy.tree.mount(
        app.Projekt(), "/projekt", config=config_rest
    )

    cherrypy.tree.mount(
        app.Projektkomponenten(), "/projektkomponenten", config=config_rest
    )

    cherrypy.tree.mount(
        app.Komponente(), "/komponente", config=config_rest
    )

    cherrypy.tree.mount(
        app.QSMitarbeiter(), "/qsmitarbeiter", config=config_rest
    )

    cherrypy.tree.mount(
        app.SWEntwickler(), "/swentwickler", config=config_rest
    )

    cherrypy.tree.mount(
        app.KatFehler(), "/katfehler", config=config_rest
    )

    cherrypy.tree.mount(
        app.KatUrsache(), "/katursache", config=config_rest
    )

    cherrypy.tree.mount(
        app.Fehler(), "/fehler", config=config_rest
    )

    cherrypy.tree.mount(
        app.ProList(), "/prolist", config=config_rest
    )

    cherrypy.tree.mount(
        app.KatList(), "/katlist", config=config_rest
    )

    cherrypy.tree.mount(
        app.Templates(), "/templates", config=config_rest
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

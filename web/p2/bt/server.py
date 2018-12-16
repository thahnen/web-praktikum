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
    def __init__(self):
        self.server_path = None #os.path.dirname(os.path.abspath(__file__))
        self.application = None #app.Application(self.server_path)

    # Index-Seite des Webservers (führt zu allen wichtigen Seiten)
    @cherrypy.expose
    def index(self):
        return self.application.get_static_page("index")


@cherrypy.expose
class Projekt(object):
    def GET(self, projekt_id=None):
        pass

    @cherrypy.tools.json_in()
    def POST(self):
        pass

    @cherrypy.tools.json_in()
    def PUT(self, projekt_id=None):
        pass

    def DELETE(self, projekt_id=None):
        pass


@cherrypy.expose
class Projektkomponenten(object):
    def GET(self, projekt_id=None):
        pass


@cherrypy.expose
class Komponente(object):
    def GET(self, komponente_id=None):
        pass

    @cherrypy.tools.json_in()
    def POST(self, projekt_id=None):
        pass

    @cherrypy.tools.json_in()
    def PUT(self, komponente_id=None):
        pass

    def DELETE(self, komponente_id=None):
        pass


@cherrypy.expose
class QSMitarbeiter(object):
    def GET(self, qsmitarbeiter_id=None):
        pass

    @cherrypy.tools.json_in()
    def POST(self):
        pass

    @cherrypy.tools.json_in()
    def PUT(self, qsmitarbeiter_id=None):
        pass

    def DELETE(self, qsmitarbeiter_id=None):
        pass


@cherrypy.expose
class SWEntwickler(object):
    def GET(self, swentwickler_id=None):
        pass

    @cherrypy.tools.json_in()
    def POST(self):
        pass

    @cherrypy.tools.json_in()
    def PUT(self, swentwickler_id=None):
        pass

    def DELETE(self, swentwickler_id=None):
        pass


@cherrypy.expose
class KatFehler(object):
    def GET(self, katfehler_id=None):
        pass

    @cherrypy.tools.json_in()
    def POST(self):
        pass

    @cherrypy.tools.json_in()
    def PUT(self, katfehler_id=None):
        pass

    def DELETE(self, katfehler_id=None):
        pass


@cherrypy.expose
class KatUrsache(object):
    def GET(self, katursache_id=None):
        pass

    @cherrypy.tools.json_in()
    def POST(self):
        pass

    @cherrypy.tools.json_in()
    def PUT(self, katursache_id=None):
        pass

    def DELETE(self, katursache_id=None):
        pass


@cherrypy.expose
class Fehler(object):
    def GET(self, fehler_id=None, type=None):
        pass

    @cherrypy.tools.json_in()
    def POST(self):
        pass

    @cherrypy.tools.json_in()
    def PUT(self, fehler_id=None):
        pass


@cherrypy.expose
class ProList(object):
    def GET(self):
        pass


@cherrypy.expose
class KatList(object):
    def GET(self):
        pass


@cherrypy.expose
class Templates(object):
    def GET(self):
        pass


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
    cherrypy.Application.currentDir_s = os.path.dirname(os.path.abspath(__file__))

    cherrypy.tree.mount(WebServer(), "/", config=config)
    cherrypy.tree.mount(Projekt(), "/projekt", config=config_rest)
    cherrypy.tree.mount(Projektkomponenten(), "/projektkomponenten", config=config_rest)
    cherrypy.tree.mount(Komponente(), "/komponente", config=config_rest)
    cherrypy.tree.mount(QSMitarbeiter(), "/qsmitarbeiter", config=config_rest)
    cherrypy.tree.mount(SWEntwickler(), "/swentwickler", config=config_rest)
    cherrypy.tree.mount(KatFehler(), "/katfehler", config=config_rest)
    cherrypy.tree.mount(KatUrsache(), "/katursache", config=config_rest)
    cherrypy.tree.mount(Fehler(), "/fehler", config=config_rest)
    cherrypy.tree.mount(ProList(), "/prolist", config=config_rest)
    cherrypy.tree.mount(KatList(), "/katlist", config=config_rest)
    cherrypy.tree.mount(Templates(), "/templates", config=config_rest)

    cherrypy.engine.start()
    cherrypy.engine.block()

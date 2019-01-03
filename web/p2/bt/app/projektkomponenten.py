#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Ver-/Bearbeitung aller (Projekt-)Komponenten:
#   ============================================
#
#   1. GET /projektkomponenten/<projekt_id>
#   => Rückgabe aller Projektkomponenten zum Projekt mit entsprechender Projekt-Id
#
#   2. GET /komponente/
#   => Rückgabe aller Projektkomponenten
#
#   3. GET /komponente/<komponente_id>
#   => Rückgabe einer einzelnen Projektkomponente mit entsprechender Komponenten-Id
#
#   4. POST /komponente/ + JSON-Daten
#   => Neue Projektkomponente speichern, gibt neue Komponenten-Id zurück
#
#   5. PUT /komponente/<komponente_id> + JSON-Daten
#   => Projektkomponente mit entsprechender Komponenten-Id verändern
#
#   6. DELETE /komponente/<komponente_id>
#   => Projektkomponente mit entsprechender Komponenten-Id löschen
#


import cherrypy


@cherrypy.expose
class Projektkomponenten(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, projekt_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "Komponenten" : "Komponente"-Objekt | List["Komponente"-Objekt]
        # }
        pass


@cherrypy.expose
class Komponente(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, komponente_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "Komponenten" : "Komponente"-Objekt | List["Komponente"-Objekt]
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, projekt_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "komponente_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, komponente_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, komponente_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass

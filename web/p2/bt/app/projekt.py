#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Ver-/Bearbeitung aller Projekte:
#   ===============================
#
#   1. GET /projekt/
#   => Rückgabe aller Projekte
#
#   2. GET /projekt/<projekt_id>
#   => Rückgabe eines einzelnen Projekts mit entsprechender Projekt-Id
#
#   3. POST /projekt/ + JSON-Daten
#   => Neues Projekt speichern, gibt neue Projekt-Id zurück
#
#   4. PUT /projekt/<projekt_id> + JSON-Daten
#   => Projekt mit entsprechender Projekt-Id verändern
#
#   5. DELETE /projekt/<projekt_id>
#   => Projekt mit entsprechender Projekt-Id löschen
#


import cherrypy


@cherrypy.expose
class Projekt(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, projekt_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "projekte" : "Projekt"-Objekt | List["Projekt"-Objekt]
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "projekt_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, projekt_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, projekt_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass

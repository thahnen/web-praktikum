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
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   ("1...n" : "Projekt"-Objekt) oder "Projekt"-Objekt-Inhalt
        # }

        code, data = self.application.get_values("projekte.json", projekt_id)
        cherrypy.response.status = code
        if code == 200:
            return data


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   "unique_id" : int
        # }

        try:
            input_json = cherrypy.request.json
        except Exception as e:
            cherrypy.response.status = 400
            return

        code, data = self.application.add_values("projekte.json", input_json)
        cherrypy.response.status = code

        if code == 200:
            return {
                "unique_id" : data
            }


    @cherrypy.tools.json_in()
    def PUT(self, projekt_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        try:
            input_json = cherrypy.request.json
        except Exception as e:
            cherrypy.response.status = 400
            return

        code = self.application.add_values("projekte.json", projekt_id, input_json)
        cherrypy.response.status = code


    @cherrypy.tools.json_out()
    def DELETE(self, projekt_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        code = self.application.delete_values("projekte.json", projekt_id)
        cherrypy.response.status = code

        if code == 200:
            # Hier alle anderen Dateien bereinigen!
            pass

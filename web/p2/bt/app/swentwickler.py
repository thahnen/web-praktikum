#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Ver-/Bearbeitung aller Software-Entwickler:
#   ==========================================
#
#   1. GET /swentwickler/
#   => Rückgabe aller Software-Entwickler
#
#   2. GET /swentwickler/<swentwickler_id>
#   => Rückgabe eines einzelnen Software-Entwicklers mit entsprechender Software-Entwickler-Id
#
#   3. POST /swentwickler/ + JSON-Daten
#   => Neuen Software-Entwickler speichern, gibt neue Software-Entwickler-Id zurück
#
#   4. PUT /swentwickler/<swentwickler_id> + JSON-Daten
#   => Software-Entwickler mit entsprechender Software-Entwickler-Id verändern
#
#   5. DELETE /swentwickler/<swentwickler_id>
#   => Software-Entwickler mit entsprechender Software-Entwickler-Id löschen
#


import cherrypy


@cherrypy.expose
class SWEntwickler(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, swentwickler_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   ("1...n" : "SW-Entwickler"-Objekt) oder "SW-Entwickler"-Objekt-Inhalt
        # }

        code, data = self.application.get_values("sw-entwickler.json", swentwickler_id)
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

        code, data = self.application.add_values("sw-entwickler.json", input_json)
        cherrypy.response.status = code

        if code == 200:
            return {
                "unique_id" : data
            }


    @cherrypy.tools.json_in()
    def PUT(self, swentwickler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        try:
            input_json = cherrypy.request.json
        except Exception as e:
            cherrypy.response.status = 400
            return

        code = self.application.add_values("sw-entwickler.json", swentwickler_id, input_json)
        cherrypy.response.status = code


    @cherrypy.tools.json_out()
    def DELETE(self, swentwickler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        code = self.application.delete_values("sw-entwickler.json", swentwickler_id)
        cherrypy.response.status = code

        if code == 200:
            # Hier alle anderen Dateien bereinigen!
            pass

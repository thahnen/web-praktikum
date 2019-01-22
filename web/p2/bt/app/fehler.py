#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ver-/Bearbeitung aller Fehler:
#   ==============================
#
#   1. GET /fehler/
#   => Rückgabe aller Fehler
#
#   2. GET /fehler/?type=erkannt
#   => Rückgabe aller erkannten Fehler
#
#   3. GET /fehler/?type=behoben
#   => Rückgabe aller behobenen Fehler
#
#   4. GET /fehler/<fehler_id>
#   => Rückgabe eines einzelnen Fehlers mit entsprechender Fehler-Id
#
#   5. POST /fehler/ + JSON-Daten
#   => Neuen Fehler speichern, gibt neue Fehler-Id zurück
#
#   6. PUT /fehler/<fehler_id> + JSON-Daten
#   => Fehler mit entsprechender Fehler-Id verändern


import json
import cherrypy


@cherrypy.expose
class Fehler(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, fehler_id=None, type=None):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 400 | 404 | 500
        #
        # {
        #   ("1...n" : "Fehler"-Objekt) oder "Fehler"-Objekt-Inhalt
        # }

        filename = "fehler.json"

        if type == None:
            code, data = self.application.get_values(filename, fehler_id)
            cherrypy.response.status = code
            if code == 200:
                return data
            return

        code, fehler = self.application.get_values(filename, None)
        cherrypy.response.status = code
        if code != 200:
            return

        return_dict = {}
        if fehler_id == None and type == "erkannt":
            # Alle erkannten Fehler zurückgeben
            for elem in fehler:
                if fehler[elem]["type"] == "erkannt":
                    return_dict[elem] = fehler[elem]
            if len(return_dict) != 0:
                return return_dict
            cherrypy.response.status = 204
            return
        elif fehler_id == None and type == "behoben":
            # Alle behobenen Fehler zurückgeben
            for elem in fehler:
                if fehler[elem]["type"] == "behoben":
                    return_dict[elem] = fehler[elem]
            if len(return_dict) != 0:
                return return_dict
            cherrypy.response.status = 204
            return

        cherrypy.response.status = 400


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene Daten mit folgenden Aufbau,
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

        code, data = self.application.add_values("fehler.json", input_json)
        cherrypy.response.status = code

        if code == 200:
            return { "unique_id" : data }


    @cherrypy.tools.json_in()
    def PUT(self, fehler_id):
        # Zurückgegebene Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 400 | 404 | 500

        try:
            input_json = cherrypy.request.json
        except Exception as e:
            cherrypy.response.status = 400
            return

        code = self.application.update_values("fehler.json", fehler_id, input_json)
        cherrypy.response.status = code

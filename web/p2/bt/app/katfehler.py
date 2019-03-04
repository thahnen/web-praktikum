#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ver-/Bearbeitung aller Fehlerkategorien:
#   =======================================
#
#   1. GET /katfehler/
#   => Rückgabe aller Fehlerkategorien
#
#   2. GET /katfehler/<katfehler_id>
#   => Rückgabe einer einzelnen Fehlerkategorie mit entsprechender Fehlerkategorie-Id
#
#   3. POST /katfehler/ + JSON-Daten
#   => Neue Fehlerkategorie speichern, gibt neue Fehlerkategorie-Id zurück
#
#   4. PUT /katfehler/<katfehler_id> + JSON-Daten
#   => Fehlerkategorie mit entsprechender Fehlerkategorie-Id verändern
#
#   5. DELETE /katfehler/<katfehler_id>
#   => Fehlerkategorie mit entsprechender Fehlerkategorie-Id löschen

import cherrypy


@cherrypy.expose
class KatFehler(object):
    def __init__(self, application):
        self.application = application
        self.data_path :str = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, katfehler_id :int = None):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 400 | 404 | 500
        #
        # {
        #   ("1...n" : "Fehlerkategorie"-Objekt) oder "Fehlerkategorie"-Objekt-Inhalt
        # }

        code, data = self.application.get_values("fehlerkategorien.json", katfehler_id)
        cherrypy.response.status = code
        if code == 200:
            return data


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
        except Exception:
            cherrypy.response.status = 400
            return

        code, data = self.application.add_values("fehlerkategorien.json", input_json)
        cherrypy.response.status = code

        if code == 200:
            return { "unique_id" : data }


    @cherrypy.tools.json_in()
    def PUT(self, katfehler_id :int):
        # Zurückgegebene Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 400 | 404 | 500

        try:
            input_json = cherrypy.request.json
        except Exception:
            cherrypy.response.status = 400
            return

        code :int = self.application.update_values("fehlerkategorien.json", katfehler_id, input_json)
        cherrypy.response.status = code


    @cherrypy.tools.json_out()
    def DELETE(self, katfehler_id :int):
        # Zurückgegebene Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 400 | 404 | 500

        code :int = self.application.delete_values("fehlerkategorien.json", katfehler_id)
        cherrypy.response.status = code

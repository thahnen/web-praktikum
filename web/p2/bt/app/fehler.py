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
#


import cherrypy


@cherrypy.expose
class Fehler(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, fehler_id=None, type=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "fehler" : "Fehler"-Objekt | List["Fehler"-Objekt]
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "fehler_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, fehler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass

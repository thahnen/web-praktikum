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
        # {
        #   "code" : 200 | 404 | 500,
        #   "swentwickler" : "Software-Entwickler"-Objekt | List["Software-Entwickler"-Objekt]
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
        #   "swentwickler_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, swentwickler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, swentwickler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass

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
#


import cherrypy


@cherrypy.expose
class KatFehler(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, katfehler_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "fehler" : "Fehlerkategorie"-Objekt | List["Fehlerkategorie"-Objekt]
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "katfehler_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, katfehler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, katfehler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass

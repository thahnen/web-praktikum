#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Ver-/Bearbeitung aller Fehlerursachenkategorien:
#   ===============================================
#
#   1. GET /katursache/
#   => Rückgabe aller Fehlerursachenkategorien
#
#   2. GET /katursache/<katursache_id>
#   => Rückgabe einer einzelnen Fehlerursachenkategorie mit entsprechender Fehlerursachenkategorie-Id
#
#   3. POST /katursache/ + JSON-Daten
#   => Neue Fehlerursachenkategorie speichern, gibt neue Fehlerursachenkategorie-Id zurück
#
#   4. PUT /katursache/<katursache_id> + JSON-Daten
#   => Fehlerursachenkategorie mit entsprechender Fehlerursachenkategorie-Id verändern
#
#   5. DELETE /katursache/<katursache_id>
#   => Fehlerursachenkategorie mit entsprechender Fehlerursachenkategorie-Id löschen
#


import cherrypy


@cherrypy.expose
class KatUrsache(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, katursache_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "fehler" : "Fehlerursachenkategorie"-Objekt | List["Fehlerursachenkategorie"-Objekt]
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
        #   "katursache_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, katursache_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, katursache_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass

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
        # cherrypy.response.status = 200 | 204 | 400 | 404 | 500
        #
        # {
        #   ("1...n" : "Fehlerursachenkategorie"-Objekt) oder "Fehlerursachenkategorie"-Objekt-Inhalt
        # }

        code, data = self.application.get_values("fehlerursachenkategorien.json", katursache_id)
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

        code, data = self.application.add_values("fehlerursachenkategorien.json", input_json)
        cherrypy.response.status = code

        if code == 200:
            return {
                "unique_id" : data
            }


    @cherrypy.tools.json_in()
    def PUT(self, katursache_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        try:
            input_json = cherrypy.request.json
        except Exception as e:
            cherrypy.response.status = 400
            return

        code = self.application.add_values("fehlerursachenkategorien.json", katursache_id, input_json)
        cherrypy.response.status = code


    @cherrypy.tools.json_out()
    def DELETE(self, katursache_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #

        code = self.application.delete_values("fehlerursachenkategorien.json", katursache_id)
        cherrypy.response.status = code

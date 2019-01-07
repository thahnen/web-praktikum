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

        try:
            swentwickler = self.application.database.read_json_into_dict("sw-entwickler.json")
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            swentwickler = swentwickler["Elements"]
            # Erstmal hier, vlt geht das irgendwie besser (400 anstatt 500)
            a = int(swentwickler_id) if swentwickler_id != None else None
        except Exception as e:
            cherrypy.response.status = 500
            return

        # so umstellen, dass das hier nicht bei fehlerhafter Anfrage auch ausgelöst wird!
        if len(swentwickler) == 0:
            cherrypy.response.status = 204
            return

        if swentwickler_id == None:
            # Alle SW-Entwickler zurückgeben
            return swentwickler

        # Speziellen SW-Entwickler (falls vorhanden) zurückgeben
        # ansonsten 404 nicht gefunden zurückgeben
        for elem in swentwickler:
            print(elem)
            if int(elem["unique_id"]) == int(swentwickler_id):
                return elem

        cherrypy.response.status = 404
        return


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   "swentwickler_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, swentwickler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # ggf so? oder wie auswerten?
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass


    @cherrypy.tools.json_out()
    def DELETE(self, swentwickler_id):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # ggf so? oder wie auswerten?
        #
        # {
        #   "code" : 200 | 404 | 500
        # }
        pass

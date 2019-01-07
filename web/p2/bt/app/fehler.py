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


import json
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
        # cherrypy.response.status = 200 | 204 | 400 | 404 | 500
        #
        # {
        #   ("1...n" : "Fehler"-Objekt) oder "Fehler"-Objekt-Inhalt
        # }

        try:
            fehler = self.application.database.read_json_into_dict("fehler.json")
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            fehler = fehler["Elements"]
            # Erstmal hier, vlt geht das irgendwie besser (400 anstatt 500)
            a = int(fehler_id) if fehler_id != None else None
        except Exception as e:
            cherrypy.response.status = 500
            return

        # so umstellen, dass das hier nicht bei fehlerhafter Anfrage auch ausgelöst wird!
        if len(fehler) == 0:
            cherrypy.response.status = 204
            return

        if fehler_id == None and type == None:
            # Alle Fehler zurückgeben
            return fehler
        elif fehler_id != None and type == None:
            # Speziellen Fehler (falls vorhanden) zurückgeben
            # ansonsten 404 nicht gefunden zurückgeben
            for elem in fehler:
                print(elem)
                if int(elem["unique_id"]) == int(fehler_id):
                    return elem

            cherrypy.response.status = 404
            return
        elif fehler_id == None and type == "erkannt":
            # Alle erkannten Fehler zurückgeben
            for elem in fehler:
                if elem["type"] != "erkannt":
                    del elem
            if len(fehler) != 0:
                return fehler

            cherrypy.response.status = 204
            return
        elif fehler_id == None and type == "behoben":
            # Alle behobenen Fehler zurückgeben
            for elem in fehler:
                if elem["type"] != "behoben":
                    del elem
            if len(fehler) != 0:
                return fehler

            cherrypy.response.status = 204
            return

        cherrypy.response.status = 400


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   "fehler_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, fehler_id):
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

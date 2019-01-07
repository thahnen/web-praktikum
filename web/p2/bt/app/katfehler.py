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
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 400 | 404 | 500
        #
        # {
        #   ("1...n" : "Fehlerkategorie"-Objekt) oder "Fehlerkategorie"-Objekt-Inhalt
        # }

        """
        # GGF nur so kurz?
        code, data = self.application.get_values("fehlerkategorien.json", katfehler_id)
        cherrypy.response.status = code
        if code == 200:
            return data
        """

        try:
            katfehler = self.application.database.read_json_into_dict("fehlerkategorien.json")
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            katfehler = katfehler["Elements"]
            # Erstmal hier, vlt geht das irgendwie besser (400 anstatt 500)
            a = int(katfehler_id) if katfehler_id != None else None
        except Exception as e:
            cherrypy.response.status = 500
            return

        # so umstellen, dass das hier nicht bei fehlerhafter Anfrage auch ausgelöst wird!
        if len(katfehler) == 0:
            cherrypy.response.status = 204
            return

        if katfehler_id == None:
            # Alle Fehlerkategorien zurückgeben
            return katfehler

        # Spezielle Fehlerkategorie (falls vorhanden) zurückgeben
        # ansonsten 404 nicht gefunden zurückgeben
        for elem in katfehler:
            print(elem)
            if int(elem["unique_id"]) == int(katfehler_id):
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
        #   "katfehler_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, katfehler_id):
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
    def DELETE(self, katfehler_id):
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

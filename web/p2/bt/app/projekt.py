#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Ver-/Bearbeitung aller Projekte:
#   ===============================
#
#   1. GET /projekt/
#   => Rückgabe aller Projekte
#
#   2. GET /projekt/<projekt_id>
#   => Rückgabe eines einzelnen Projekts mit entsprechender Projekt-Id
#
#   3. POST /projekt/ + JSON-Daten
#   => Neues Projekt speichern, gibt neue Projekt-Id zurück
#
#   4. PUT /projekt/<projekt_id> + JSON-Daten
#   => Projekt mit entsprechender Projekt-Id verändern
#
#   5. DELETE /projekt/<projekt_id>
#   => Projekt mit entsprechender Projekt-Id löschen
#


import cherrypy


@cherrypy.expose
class Projekt(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self, projekt_id=None):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 404 | 500
        #
        # {
        #   ("1...n" : "Projekt"-Objekt) oder "Projekt"-Objekt-Inhalt
        # }

        try:
            projekte = self.application.database.read_json_into_dict("projekte.json")
            # Annahme aus database.py dass "Elements" in JSON exisitert!
            projekte = projekte["Elements"]
            # Erstmal hier, vlt geht das irgendwie besser (400 anstatt 500)
            a = int(projekt_id) if projekt_id != None else None
        except Exception as e:
            cherrypy.response.status = 500
            return

        # so umstellen, dass das hier nicht bei fehlerhafter Anfrage auch ausgelöst wird!
        if len(projekte) == 0:
            cherrypy.response.status = 204
            return

        if projekt_id == None:
            # Alle Projekte zurückgeben
            return projekte

        # Spezielles Projekt (falls vorhanden) zurückgeben
        # ansonsten 404 nicht gefunden zurückgeben
        for elem in projekte:
            print(elem)
            if int(elem["unique_id"]) == int(projekt_id):
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
        #   "projekt_id" : int
        # }
        pass


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, projekt_id):
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
    def DELETE(self, projekt_id):
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

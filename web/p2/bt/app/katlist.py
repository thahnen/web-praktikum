#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Auswertung aller Fehler nach Projekt/Komponente/Status:
#   ======================================================
#
#   1. GET /katlist/
#   => Rückgabe einer Liste aller Fehler nach Projekt/Komponente/Status sortiert
#


import cherrypy


@cherrypy.expose
class KatList(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau:
        #
        # {
        #   "code" : 200 | 404 | 500,
        #   "fehler" : List["Fehler"-Objekte]
        # }

        # Fehler aus Application auslesen und hier sortieren
        pass

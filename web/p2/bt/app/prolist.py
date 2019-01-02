#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Auswertung aller Fehler nach Kategorie/Status:
#   =============================================
#
#   1. GET /prolist/
#   => Rückgabe einer Liste aller Fehler nach Kategorie/Status sortiert
#


import cherrypy


@cherrypy.expose
class ProList(object):
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

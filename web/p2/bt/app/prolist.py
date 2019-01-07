#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Auswertung aller Fehler nach Kategorie/Status:
#   =============================================
#
#   1. GET /prolist/
#   => Rückgabe einer Liste aller Fehler nach Kategorie/Status sortiert
#

# REVIEW: Ist eigentlich soweit fertig, auf Richtigkeit überprüfen

import cherrypy


@cherrypy.expose
class ProList(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene JSON-Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 500
        #
        # {
        #   "1...n" : "Fehler"-Objekt
        # }

        code, data = self.application.get_values("fehler.json", None)
        if code != 200:
            cherrypy.response.status = code
            return

        try:
            # Fehler nach:
            # 1) Fehlerkategorien (eine Liste)
            # 2) Status (erkannt oder behoben)
            # sortieren
            data = dict(sorted(
                data, key=lambda elem: (elem["erkannt"]["fehlerkategorien"], elem["status"])
            ))

            return data
        except Exception as e:
            cherrypy.response.status = 500

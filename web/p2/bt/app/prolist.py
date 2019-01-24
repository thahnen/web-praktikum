#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Auswertung aller Fehler nach Kategorie/Status:
#   =============================================
#
#   1. GET /prolist/
#   => Rückgabe einer Liste aller Fehler nach Kategorie/Status sortiert

import cherrypy


@cherrypy.expose
class ProList(object):
    def __init__(self, application):
        self.application = application
        self.data_path = self.application.server_path + "/data/"


    @cherrypy.tools.json_out()
    def GET(self):
        # Zurückgegebene Daten mit folgenden Aufbau,
        # bei Fehler wird nur der Code zurückgegeben!
        #
        # cherrypy.response.status = 200 | 204 | 500
        #
        # {
        #   "1...n" : "Fehler"-Objekt
        # }

        # REVIEW: Funktioniert mit Curl ohne Probleme! Nur Online: fetch sortiert selbst!

        code, data = self.application.get_values("fehler.json", None)
        if code != 200:
            cherrypy.response.status = code
            return

        try:
            # Fehler nach:
            # 1) Projekt-Komponente (eine Zahk)
            # 2) Status (erkannt oder behoben)
            # sortieren
            data = {int(k):v for k,v in data.items()}
            return dict(sorted(
                data.items(), key=lambda kv: (int(kv[1]["komponente"]), kv[1]["type"])
            ))
        except Exception as e:
            print(e)
            cherrypy.response.status = 500

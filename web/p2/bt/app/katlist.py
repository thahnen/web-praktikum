#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Auswertung aller Fehler nach Projekt/Komponente/Status:
#   ======================================================
#
#   1. GET /katlist/
#   => Rückgabe einer Liste aller Fehler nach Projekt/Komponente/Status sortiert

import cherrypy


@cherrypy.expose
class KatList(object):
    def __init__(self, application):
        self.application = application
        self.data_path :str = self.application.server_path + "/data/"


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
            # 1) Kategorie (Liste von Zahlen) -> hier einfach nur das erste Element!
            # 3) Status (erkannt oder behoben)
            # sortieren
            data = {int(k):v for k,v in data.items()}
            return dict(sorted(
                data.items(), key=lambda kv: (int(kv[1]["erkannt"]["fehlerkategorien"][0]), kv[1]["type"])
            ))
        except Exception as e:
            cherrypy.response.status = 500
